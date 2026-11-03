# Agent Context Workflow

A portable Agent Skill for managing task context across multi-step work: find useful sources, preserve work evidence and progress, rebuild context after a pause or new session, and verify before resuming.

**Preview version: `v0.1.0-preview`.** Core instructions are original. Original project files use the [MIT License](LICENSE). Referenced third-party projects retain their own licenses. No runtime adapter, automatic compaction, context-size telemetry or performance improvement is claimed without evidence.

[中文说明](README.zh-CN.md) · [Compatibility](COMPATIBILITY.md) · [Sources](SOURCES.md) · [Status](STATUS.md)

## What the workflow does

| Function | What it preserves or checks |
|---|---|
| Ground the task | Request, task/project identity, governing instructions, authority, existing records, and write scope |
| Select sources | Existing indexes, targeted reads, and cross-source constraints; missing hits get a bounded, labelled fallback search |
| Filter and offload | Keep a useful working set, filter noisy/long output, and save authorized exact work as a retrievable pointer without changing the original |
| Separate state | Keep raw facts, assumptions, decisions, exact recoverable WIP, and test/verification state distinct |
| Checkpoint | At a milestone or request, save to the existing task record, preserve accepted outcomes and pending commitments, then read back the actual write |
| Reconstruct and verify | Recheck task identity, checkpoint/source revisions, current permission, and unknown external effects before dependent work |
| Compact or isolate | Use a host operation only when it is verified and authorized; otherwise make a manual checkpoint, bounded handoff, or read-only report |

The workflow rebuilds current task context from saved state, then checks what changed before dependent work continues. It fits existing records and works without a required database, service, or native compaction API; these are design characteristics, not measured superiority.

### Reconstruct, verify, continue

After a pause or new session, rebuild the working context from saved task state, source pointers and revisions, and exact drafts that are available. Then recheck current sources, permissions, and unknown external effects before continuing. If exact content was not saved, mark it unknown rather than presenting a later rewrite as the original.

A checkpoint is evidence of state, not new permission or a rollback; unknown effects are held rather than replayed.

## Who it helps

Use it for research, planning, and small projects spanning turns, sources, phases, or noisy outputs. Skip it for a self-contained edit or short question. Project size is not a context budget, and the workflow does not enlarge a model window.

## Try the preview

Read [the skill](skills/context-workflow/SKILL.md) explicitly and request a bounded trial. Keep the folder intact if installing it in a host's documented skill directory; verify actual discovery behavior rather than assuming installation worked.

Example requests:

- “Use context-workflow for this multi-step task. Reuse my existing index and task record; keep the start lightweight.”
- “Checkpoint this milestone into the existing task record, preserve all remaining commitments and exact recoverable drafts, then read it back.”
- “Resume from this task record in read-only mode first. Check identity, source changes and unresolved external effects.”
- “Plan only: show a checkpoint proposal without writing files.”

## How it works

```text
Current task → select sources → work → checkpoint at a useful boundary
                                      ↓
                    changed/compacted/new context
                                      ↓
                  verify identity, sources and effects → continue
```

Only the reference needed for the current decision is loaded. Reuse existing task records rather than creating another task database. New files and external actions require actual permission. Without file access, return an explicit unsaved checkpoint draft; without native compaction or isolation, use the manual path.

## Examples and verification

[Examples](examples/README.md) are synthetic. The [evaluation cases](evals/cases.json) define observable failure boundaries. Run `python evals/check_package.py` for packaging/link/public-data checks. Use an available Python 3 interpreter; this checker has no external dependencies. It does not evaluate semantic accuracy or prove real host compaction.

The [continuity trial](evals/continuity-trial/README.md) records actual synthetic file work and a fresh evaluation context, including the initial correction history. It is distinct from native host compaction or cross-host validation.

Observed results and untested capabilities belong in [STATUS.md](STATUS.md) and [COMPATIBILITY.md](COMPATIBILITY.md). Do not replace those with a universal “works everywhere” badge.

## Boundaries

No automatic transcript capture, network upload, user-memory writes, hook installation, external operation replay, or global instruction replacement. Source hashes identify content, not truth. A conversation rewind does not undo files, requests, deployments or other external effects. Interrupted unsaved facts may be unrecoverable.

## Contributing and release


Propose a concrete failure case, minimal original change and evidence. Do not contribute private records, copied unlicensed templates or fabricated metrics. Keep changes portable and include reproducible synthetic evidence. Keep license notices and compatibility evidence accurate. See [release notes](RELEASE_NOTES.md).
