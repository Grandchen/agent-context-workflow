"""Deterministic negative file/recovery trials for the public workflow.

These tests exercise synthetic file fixtures and invariants only.  They do not
invoke an agent, a host compaction API, or a production checkpoint engine.
"""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _temporary_directory():
    scratch = os.environ.get("ACW_TEST_TMP")
    if scratch is None:
        return tempfile.TemporaryDirectory()
    root = Path(scratch).resolve()
    if not root.is_dir():
        raise RuntimeError(f"ACW_TEST_TMP is not a directory: {root}")
    return tempfile.TemporaryDirectory(dir=root)


def _synthetic_atomic_save(target: Path, payload: str, replace):
    """Minimal fixture save: replacement is injectable to force failure."""
    staged = target.with_name(target.name + ".pending")
    staged.write_text(payload, encoding="utf-8", newline="")
    try:
        replace(staged, target)
    finally:
        if staged.exists():
            staged.unlink()


def _read_identity(record: Path, project: str, task: str) -> dict:
    try:
        value = json.loads(record.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return {"status": "malformed", "reason": type(exc).__name__}
    if not isinstance(value, dict):
        return {"status": "malformed", "reason": "record-not-object"}
    if value.get("project") != project or value.get("task") != task:
        return {"status": "wrong-task", "reason": "identity-mismatch"}
    return {"status": "ok", "record": value}


class NegativeTrial(unittest.TestCase):
    def test_failed_save_preserves_baseline(self):
        """A replacement failure leaves the canonical bytes and no pending file."""
        with _temporary_directory() as directory:
            target = Path(directory) / "TASK.json"
            baseline = '{"revision": 1, "remaining": ["keep this"]}\n'
            candidate = '{"revision": 2, "remaining": ["candidate"]}\n'
            target.write_text(baseline, encoding="utf-8", newline="")

            def fail_replace(_staged: Path, _target: Path):
                raise OSError("synthetic disk-full during replace")

            with self.assertRaisesRegex(OSError, "disk-full"):
                _synthetic_atomic_save(target, candidate, fail_replace)

            self.assertEqual(target.read_text(encoding="utf-8"), baseline)
            self.assertFalse(target.with_name(target.name + ".pending").exists())

    def test_malformed_record_is_rejected_without_dependent_write(self):
        """Malformed state is reported; a dependent mutation is not attempted."""
        with _temporary_directory() as directory:
            record = Path(directory) / "TASK.json"
            record.write_text('{"project": "reading-list",', encoding="utf-8")
            dependent = Path(directory) / "dependent.txt"

            result = _read_identity(record, "reading-list", "RL-12")

            self.assertEqual(result["status"], "malformed")
            self.assertFalse(dependent.exists())

    def test_wrong_task_is_rejected_without_dependent_write(self):
        """A valid record for another task cannot authorize this task's work."""
        with _temporary_directory() as directory:
            record = Path(directory) / "TASK.json"
            record.write_text(
                json.dumps({"project": "reading-list", "task": "RL-11"}),
                encoding="utf-8",
            )
            dependent = Path(directory) / "dependent.txt"

            result = _read_identity(record, "reading-list", "RL-12")

            self.assertEqual(result["status"], "wrong-task")
            self.assertFalse(dependent.exists())

    def test_concurrent_modification_is_rejected_without_clobber(self):
        """A stale baseline cannot replace a newer shared record."""
        with _temporary_directory() as directory:
            target = Path(directory) / "TASK.json"
            baseline = '{"revision": 1, "owner": "task-A"}\n'
            newer = '{"revision": 2, "owner": "task-B"}\n'
            target.write_text(baseline, encoding="utf-8", newline="")
            baseline_hash = _sha256(target)
            target.write_text(newer, encoding="utf-8", newline="")
            stale_candidate = '{"revision": 2, "owner": "task-A"}\n'

            self.assertNotEqual(_sha256(target), baseline_hash)
            self.assertNotEqual(target.read_text(encoding="utf-8"), stale_candidate)

            # The synthetic stale-writer gate refuses to replace the newer file.
            self.assertRaises(
                ValueError,
                self._reject_stale_replace,
                target,
                baseline_hash,
                stale_candidate,
            )
            self.assertEqual(target.read_text(encoding="utf-8"), newer)

    @staticmethod
    def _reject_stale_replace(target: Path, expected_hash: str, _candidate: str):
        if _sha256(target) != expected_hash:
            raise ValueError("concurrent modification")

    def test_unknown_effect_is_retained_and_not_replayed(self):
        """Unknown synthetic outcome remains unknown and replay stays forbidden."""
        with _temporary_directory() as directory:
            operations = Path(directory) / "operations.json"
            operations.write_text(
                json.dumps(
                    {
                        "intent_id": "SYNTH-NEG-01",
                        "outcome": "unknown",
                        "external_requests": 0,
                        "replay_permitted": False,
                    }
                ),
                encoding="utf-8",
            )
            value = json.loads(operations.read_text(encoding="utf-8"))

            self.assertEqual(value["outcome"], "unknown")
            self.assertEqual(value["external_requests"], 0)
            self.assertFalse(value["replay_permitted"])


if __name__ == "__main__":
    unittest.main()
