---
root: true
targets: ["*"]
description: "One resumable release command that tags; CI publishes from the tag"
---

<!-- hotsheet:begin section=release-scripts v=2 -->

## Release Scripts

One resumable command from a clean shipping checkout creates the annotated tag; CI publishes. Never publish locally or release by hand checklist.

- **Flow:** `release` runs pre-flight → version choice → notes → changelog → local gate → every lockstep version bump → release commit → annotated tag → push commit/tag. Expose noninteractive flags (`--version`, `--notes <file>`, `--skip-checks`, `--dry-run`); flags cannot waive mandatory project gates.
- **Beta:** `release:beta` is tag-only from HEAD: no version bump, changelog or commit. Use `vX.Y.Z-beta.N`, incrementing the highest beta in that series. Automation must work without an editor.
- Refuse dirty tree, wrong branch, missing tools, existing tag or stale lockfile before mutation; print the fix. Require local git/toolchain, not registry login used only by CI.
- Record steps/answers in ignored state; resume without repeated bumps/prompts, remove state on success. After a partial release commit, stage nothing and proceed to tag.
- Use semver, one version/tag per lockstep group. Sync manifests, scaffold templates and documented ranges from the root version; gate its `--check` mode. Widen supported ranges only with tests.
- Keep a Changelog with `[Unreleased]` bullets (ticket slug) in each behavior change. Stable releases move the whole body to a dated version, then append the distinct draft; never replace curated history. Format before lint; betas never write it.
- Draft notes from last-tag..HEAD via `gitgist-release-notes`, review in editor (or supplied notes), require nonempty user-facing text and store it in the tag message. Provider failure falls back to deterministic grouping then a git-log pointer; it never blocks release.
- **Publish only from `v*` tags.** Test/build/pack jobs hold no publish credential. Only the publisher has registry token/OIDC; it downloads and publishes already-packed bytes, never checks out or executes repository code. Betas use `beta` dist-tag and prerelease GitHub release; stable GitHub releases use the final notes. Dependents await registry-visible core, fail fast on core failure; rerun core first, then dependents.
- Unpublished tags may be deleted locally/remotely and re-cut. Published versions are never unpublished or re-tagged; ship a patch.
- Copy a working reference release script, changelog helper and workflow, adapting names/packages/gates; record provenance in the codebase map or a local note when the project cannot name it.

Project-level deviations require a compelling/necessary reason in conventions.

<!-- hotsheet:end section=release-scripts -->
