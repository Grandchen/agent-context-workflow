# v0.1.0-preview

First public preview of the standalone Context Workflow Skill.

- Manage task context throughout multi-step work: select relevant sources, preserve exact available work and evidence, checkpoint milestones, reconstruct context and verify before continuing.
- Reuse existing indexes and task records; keep simple actions lightweight.
- Use native compaction or isolation only when the host supports it and the task permits it; otherwise use a manual handoff.
- Keep uncertainty, pending commitments and unknown external effects visible.

The core is original and MIT licensed. Research links do not imply that upstream code or text was copied or relicensed. No required personal workflow, API, service, database or other Skill.

This is a preview. See [status](STATUS.md) and [compatibility](COMPATIBILITY.md) for evidence and limits. In particular, the isolated evaluator trial is not a successful GUI new-chat or native compaction test.

To try: read [SKILL.md](skills/context-workflow/SKILL.md) explicitly in an assistant with the appropriate file capabilities, or preserve its folder structure in your host's documented Skill directory. Verify discovery in that host. No installer or hook runs automatically.
