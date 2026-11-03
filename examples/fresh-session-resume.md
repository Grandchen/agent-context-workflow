# Synthetic example: fresh-session resume

This example is illustrative and uses no real project data.

In a fresh session, the user provides checkpoint revision 2 for project `paper-lantern`, task `design-review-1`. The assistant verifies the identity and reads the listed source revisions. `notes/color.md` has changed, so the assistant pauses the dependent recommendation and reports the changed source.

The assistant does not replay a command from the old transcript, treat the checkpoint as new permission, or regenerate the missing comparison table. It may independently re-read the changed note because that work is clearly in scope. After reconciling the changed evidence and checking that permission still covers the next step, it may create revision 3 with the new source revision and any newly archived exact WIP; no repeated approval is needed for an unchanged valid scope.
