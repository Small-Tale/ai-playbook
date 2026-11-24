---
root: true
targets: ["*"]
description: "Commit shape, staging discipline, history safety, and a declared push policy"
---

<!-- hotsheet:begin section=git-commit-and-push v=3 -->

## Git Commit and Push

The Hot Sheet workflow owns ticket commit boundaries, integration and CI records. This rule adds:

- **Subject:** `<SLUG> <imperative summary>`, under 72 characters, no trailing period or type prefix; only release scripts use `release: vX.Y.Z`. Body explains why/behavior, follow-up slugs and deliberate deviations, not a file list. Review tool drafts (`gitgist-release-notes`).
- Stage explicit files, never `git add -A` or `git add .`; inspect `git diff --cached` before every commit and remove others' changes. Regenerate declared artifacts with their sources and stage by name.
- Never amend/rebase/reset/force-push commits that reached any remote or the shipping branch; fix forward. Local unpushed commits may be amended. Never bypass hooks with `--no-verify`; fix failing gates.
- Pre-commit runs cheap whitespace/format checks. Pre-push runs the root check once per push, reusing a passing identical tree. Provide a `push` script that checks before opening the remote connection.
- Declare exactly one policy with standing maintainer authorization for routine fast-forward verified pushes to the named shipping branch. If absent, commit, ticket the missing declaration and leave pushing to a person; never guess.
  - `push-per-ticket`: default for apps/services; push each verified ticket immediately and confirm success before the next.
  - `push-per-batch`: only with a measured reason beside the declaration; push at queue drain, earlier for CI when needed, always before session end.
- Use the shipping branch unless review or another agent's worktree requires a branch; follow workflow integration/reachability/cleanup requirements.
- Never commit secrets/tokens, machine-local paths, customer content (`customer-data-hygiene`), undeclared build output or editor/OS files. Cover them in `.gitignore` and reject tracked machine-local paths by policy test.
- Confirm the remote contains the commit after push (no ahead count); record the CI gate commit per the workflow.

Project-level deviations require a compelling/necessary reason beside the policy declaration.

<!-- hotsheet:end section=git-commit-and-push -->
