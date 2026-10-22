---
root: true
targets: ["*"]
description: "One resumable release command that tags; CI publishes from the tag"
---

<!-- hotsheet:begin section=release-scripts v=1 -->

## Release Scripts

A release is one command, run from a clean checkout of the shipping branch, that produces an annotated tag CI publishes from. Nothing publishes from a developer machine, and nobody performs a release by hand from a checklist.

- **One entry point.** `npm run release` (or the language's equivalent task runner) drives the stable flow in order: pre-flight, version choice, release notes, changelog update, local gate, version bump in every lockstep package, release commit, annotated tag, push of commit and tag. `npm run release:beta` is tag-only: no version-file bump, no changelog write, no commit; it tags `vX.Y.Z-beta.N` off `HEAD` with `N` one more than the highest existing beta in that series. A non-interactive variant answers every prompt from flags (`--version`, `--notes <file>`, `--skip-checks`, `--dry-run`) so automation and agents can cut a beta without an editor.
- **Pre-flight refuses.** A dirty tree, the wrong branch, a missing tool, an existing tag, or a stale lockfile stops the script before it changes anything, and it prints the fix rather than a stack trace. Pre-flight distinguishes what the local machine needs (git, the toolchain) from what CI holds (registry credentials), and does not demand a local registry login the publish path does not use.
- **Resumable and idempotent.** The script records each completed step and the answers so far in an ignored state file and resumes after an interruption without repeating the bump or re-asking; a finished release removes the file. A re-run after a partial release commit stages nothing and proceeds to tag.
- **Versions.** Semantic versioning. Packages that release together carry one version and one tag; the script bumps every embedded version (manifests, scaffold templates, documented ranges) from the one root version, and a `--check` mode of that sync runs in the root gate so drift fails long before release day. Widening a supported-version range is a tested act, never a convenience edit.
- **Changelog.** Keep a Changelog format with an `[Unreleased]` section maintained in the same commit as each behavior change, with the ticket slug in the bullet. The stable release moves the whole `[Unreleased]` body into the new dated version entry and then appends the distinct release-note draft; a draft never replaces hand-curated history. Betas do not write the changelog. The script formats the changelog before the lint gate runs.
- **Notes.** Draft notes from the commit range since the last tag with gitgist (`gitgist-release-notes`), open the draft in the editor, and require a non-empty, user-facing result; the annotated tag message carries the final notes. Without an AI provider, fall back to deterministic grouping, then to a `git log` pointer; a notes provider never blocks a release.
- **CI publishes from the tag.** The release workflow triggers on `v*` tags only. Jobs that test, build, or pack hold no publish credential; the one job that holds the registry token or OIDC identity only downloads and publishes already-packed bytes and never checks out or executes repository code. Betas publish under a `beta` dist-tag with a prerelease GitHub release; stable releases create the GitHub release from the notes. When several packages publish from one tag, dependents wait until the core package is visible on the registry and fail fast when the core run fails, so a failed core release is re-run first and the dependents after.
- **Rollback.** A tag CI has not yet published is deleted locally and remotely and re-cut. A published version is never unpublished or re-tagged; ship a patch.
- **Reference.** A new project copies the reference release script, changelog helper, and release workflow from an existing repository and changes names, packages, and gate commands; it does not write them from scratch. Record the source in the codebase map (or in a local note when the project must not name it).

Deviate only at the project level for a compelling or necessary reason, recorded in the project's conventions document.

<!-- hotsheet:end section=release-scripts -->
