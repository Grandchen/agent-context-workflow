# Synthetic example: small-project start

This example is illustrative and uses no real project data.

User request: “Plan a two-turn review of the tiny `paper-lantern` project. Read its rules and two design notes, but do not write yet.”

The workflow qualifies because the task spans turns and several sources, not because the project is large. The assistant records:

- Identity: project `paper-lantern`, task `design-review-1`.
- Permission: Plan only; no checkpoint write or external action.
- Targeted reads: the project rules, `notes/shape.md`, and `notes/color.md`; no whole-project scan.
- Output: a short selected-source map, open questions, and a proposed checkpoint location.

The start is lightweight. It does not invent token limits, create a task registry, or checkpoint after each read.
