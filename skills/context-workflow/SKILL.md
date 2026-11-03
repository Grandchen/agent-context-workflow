---
name: context-workflow
license: MIT
description: "For authorized multi-step or multi-turn tasks with several relevant sources, noisy outputs, or checkpoint/resume needs, select and preserve useful context; includes small projects and excludes self-contained work."
metadata:
  version: "0.1.0-preview"
  status: preview
  scope: "Portable manual context workflow for source-heavy tasks"
  reviewed_at: "2026-11-02"
---

# Context Workflow

This is a portable preview of a manual workflow, not runtime authority. Use it when task characteristics call for multiple turns, several relevant sources, noisy output, or checkpoint/resume; small projects qualify when their work spans sources or turns. Keep a self-contained action lightweight and ceremony proportional; do not turn every task into a full protocol. Do not scan a whole project, create a second registry, or assume a hidden service.

## Route

1. Establish the current request, project/task identity, actual permissions, applicable project rules, and existing task records. Read mandatory governing instructions before dependent work.
2. Select targeted sources and cross-source relationships, using existing indexes when available. If a named source is missing, use a bounded fallback search and label the gap; do not pretend it was recovered.
3. Distinguish raw evidence, summaries, assumptions, decisions, and verification. A path plus hash identifies source revision, not truth or quality. Save exact necessary work only to an authorized location and return retrievable pointers.
4. Load only the reference needed now: [navigation](references/navigation.md), [checkpoint](references/checkpoint.md), [resume](references/resume.md), or [compaction](references/compaction.md). Do not preload all references.

## Authority and fidelity

- Reuse the user's existing task records and one task writer; this package supplies a contract, not a global state system. Create a record only at an authorized location when no equivalent exists.
- A valid approval for the same unchanged scope may persist, subject to expiry, revocation, one-shot use, and changed prerequisites. A checkpoint expands no authority.
- Unknown external effects are never replayed or rolled back by context changes. Plan is read-only; if file access is unavailable, provide a manual checkpoint or recovery report instead.
- No token threshold, arbitrary directory depth, native compaction, fresh-session persistence, external API, script, or subagent is assumed or required. Optional host operations require verified capability and authorization.

## Checkpoint boundary

Checkpoint at a meaningful milestone or user trigger instead of waiting for an estimated context limit; never after every tool call by default. Preserve exact archived WIP in an authorized artifact, and label summaries as summaries. Read back actual writes. A checkpoint is state evidence, not an authorization or an external rollback.

Keep private data and raw payloads to the minimum necessary. State what cannot be recovered. Leave unsupported host behavior unverified rather than promising lossless recovery or savings.

Runtime authority comes from the user's actual platform/project instructions, not this package's development documents. Research provenance is maintained in the repository; this preview has no required dependency on another skill.
