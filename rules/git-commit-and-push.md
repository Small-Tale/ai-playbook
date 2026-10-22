---
root: true
targets: ["*"]
description: "Commit shape, staging discipline, history safety, and a declared push policy"
---

<!-- hotsheet:begin section=git-commit-and-push v=1 -->

## Git Commit and Push

Every repository declares its push policy in its project instructions. An agent that cannot find one does not guess: it commits, files a ticket to add the declaration, and leaves the push to a person. Commit discipline is the same everywhere.

- **One commit per ticket.** Commit a finished, verified ticket before starting the next one. Combine tickets in one commit only when their changes cannot be separated safely, and name every slug the commit addresses.
- **Subject shape.** `<SLUG> <imperative summary>`, slug first so `git log --oneline` reads as a ticket list, under 72 characters, no trailing period, no type prefix. The only exception is the release script's own `release: vX.Y.Z` commit. The body says why the change was made and what behavior changed, not which files; it names follow-up slugs and any deliberate deviation from a rule. A tool may draft the body from the staged diff (`gitgist-release-notes`); the author edits it and keeps the subject shape.
- **Stage by path.** Stage named files, never `git add -A` or `git add .`, and read `git diff --cached` before every commit to remove anything you did not change. Generated artifacts regenerate in the same commit as their source and are staged by name.
- **Never rewrite shared history.** No amend, rebase, reset, or force-push on a commit that has reached the shipping branch or any remote; fix forward with a new commit. Local unpushed commits may be amended before they leave the machine. Never pass `--no-verify`: a failing hook is a failing gate, and the fix is the code, not the flag.
- **Gates before the remote opens.** A pre-commit hook runs the cheap whitespace and format checks; a pre-push hook runs the root check once per push and skips when the same tree already passed. Provide a `push` script that runs the check first and then `git push`, so a long gate does not run inside an idle remote connection that times out.
- **Declared push policy.** The instructions name exactly one of two policies and carry a standing authorization sentence so agents stop asking at ticket boundaries ("The maintainer has authorized routine fast-forward pushes of verified ticket commits to `<branch>`; do not ask again").
  - `push-per-ticket`: push each verified ticket commit immediately after committing it and confirm the push succeeded before taking the next ticket. This is the default for applications and services.
  - `push-per-batch`: hold verified ticket commits locally and push once per queue drain, or sooner when a fix must reach CI. Choose it only for a measured reason recorded beside the declaration (for example a multi-minute pre-push gate plus a long CI run that cancels superseded runs), and still push before ending the session.
- **Trunk-based.** Commit to the shipping branch. Use a branch only for a change that must land through review or for a worktree another agent works in, and integrate it per the Hot Sheet workflow: merge or cherry-pick, confirm the commit is reachable from the shipping branch, remove the worktree.
- **What never enters a commit.** Secrets and tokens, machine-local paths, customer content (`customer-data-hygiene`), build output that is not a declared generated artifact, and editor or OS files. `.gitignore` covers them, and a policy test fails on machine-local paths in tracked files.
- **Verify, then record.** After a push, confirm the remote has the commit (no ahead count in `git status -sb`) and record the CI gate commit in the ticket per the Hot Sheet workflow. A push that was never confirmed is not a push.

Deviate only at the project level for a compelling or necessary reason, recorded beside the policy declaration.

<!-- hotsheet:end section=git-commit-and-push -->
