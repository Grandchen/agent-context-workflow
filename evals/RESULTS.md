# Preview verification — 2026-11-02

Version: 0.1.0-preview. This is local preview evidence, not a released benchmark.

- Actual-root subset packaging/link check: 22 relative links passed before this report was added. This is not full YAML validation or a complete secret scan.
- Package failure-detection tests: first run failed because the execution sandbox's default temporary directory did not permit fixture writes/cleanup. No test assertions ran successfully in that attempt. Rerunning with an explicitly writable test scratch succeeded. The tests are isolated synthetic copies and do not mutate project files.
- Independent read-only reviewer: six user requests covering small multi-step projects, one-label edits, Plan-only drafts, changed sources/unknown receipts, absent native telemetry, and private-history import. Responses respected task/permission boundaries and manual fallback.
- Reviewer identified two medium findings: stale compatibility wording and narrow local-path detection. Compatibility/progress wording was corrected; detection was broadened to Windows roots, UNC, POSIX home/system roots and file URIs, with synthetic negative cases. Sources resolving outside the package are rejected before their text is read.
- A targeted follow-up review found extended UNC prefixes missing and a system-root example absent. The marker pattern and subcases now include conventional/extended UNC, device prefixes, Windows roots, POSIX home/system examples and file URIs. These are bounded marker checks, not complete local-path parsing or a full privacy audit.
- After these changes, the staged package check passed 23 relative links and five tests passed, including eight path forms exercised as subcases. Actual-root rerun is recorded separately when performed.
- At the initial-preview phase, actual file persistence and fresh-context recovery for this public package were untested. The later phase-2 results below supersede those two pending statuses only. Real host compaction/hooks, performance comparisons and cross-host execution remain untested. Personal workflow tests are not substituted as public-product evidence.
- The system Python alias was unavailable and the available runtime lacked PyYAML. No dependency was installed; official quick_validate.py has not passed. The independent checker reports its supported subset explicitly.

Run: `python evals/check_package.py` and `python -B -m unittest discover -s evals -p "test_*.py"`. If the system temporary directory is restricted, set the task-specific `ACW_TEST_TMP` environment variable to a verified writable scratch directory. Test-generated recursive cleanup stays within a resolved owned temporary subdirectory. Do not repurpose an existing project directory as that scratch.

Final actual-root rerun after targeted follow-up: packaging passed 23 relative links; five tests passed, including eight path-marker subcases (2026-11-02). This remains a bounded check, not a full privacy audit or host-continuity test.

## Phase 2: file continuity and communication materials

Public `context-workflow` v0.1.0-preview was used in a separate synthetic workspace. A fresh executor wrote the existing record and read it back. Review caught wording that incorrectly attributed authorization to the checkpoint itself; the first attempt is archived unchanged, and a corrective write/readback produced revision 2 with authorization correctly attributed to the current user request. The unrelated task section, three accepted outcomes and exact draft wording remained intact.

Afterward, the test author changed a requirement from revision 1 to 2 without backfilling the checkpoint. A fresh evaluator, given no parent task history or expected answer, recovered the identity, commitments, exact draft and verification limits; it detected the source revision mismatch/new case-insensitive-search rule and held dependent actions while retaining the unknown synthetic outcome. No write, network call, app operation, replay or compaction was performed during recovery.

See [trial and correction history](continuity-trial/README.md), [actual recovery answer](continuity-trial/recovery-report.md) and [physical fixture checks](phase2-verification.json). The six additional scenario responses are decision evidence, not executed external effects. A one-case corrected trial is not a success rate, cross-host certification or proof of lossless recovery.

GitHub/video materials describe these evidence levels. Their recording sequence uses an authorized disposable copy reset from saved initial fixtures; a real user-facing new AI session remains a separate recording/host check. No video has been recorded or uploaded in this phase.

An independent communication review identified wording that could imply the proposed pre-drift GUI recording had already been tested. The runbook now explicitly separates that future live recording from the archived after-drift fresh-evaluator result, requires preserving its actual output/failure record, and avoids presenting a planned video segment as completed evidence.

Phase-2 actual-root integration: 56 relative links passed; five package failure-detection tests passed (2026-11-02). This adds packaging evidence only; semantic continuity evidence is the archived corrected trial above.

## Phase 3: bounded negative fixtures

See [negative fixture report](negative-trial/README.md) and [machine observations](negative-trial/trial-report.json). Five deterministic tests passed; combined suite had ten tests. They simulate replacement failure, malformed/wrong-task records, a stale writer and an unknown synthetic effect. These are fixture/invariant checks of test helpers; there is no production save engine and they do not demonstrate live Skill behavior. The final package check is recorded at its actual run, after integration.

The existing runtime and video environment both lacked PyYAML during the recheck. No dependency was installed, and official quick_validate.py remains unpassed. The subset checker cannot substitute for it.
