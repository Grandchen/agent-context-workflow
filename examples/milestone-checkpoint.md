# Synthetic example: milestone checkpoint

This example is illustrative and uses no real project data.

At milestone 2 of `paper-lantern` task `design-review-1`, Execute authorization permits patching the existing `notes/task.md` record. The assistant writes revision 2 and reads it back.

- Accepted outcome: compare the two design notes and preserve the unresolved choice.
- Exact archived WIP: `drafts/review-2.md`, which contains the unfinished comparison table.
- Summary: the chat summary says the contrast is incomplete; it is not presented as the missing table.
- Verification: both notes were read at their recorded revisions; the task record write was read back.
- Effects: no external action was attempted, so there is no receipt or unknown effect.
- Next prerequisite: confirm which design choice the user approves before editing either note.

The checkpoint was triggered by a meaningful milestone, not by an arbitrary token or tool-call count.
