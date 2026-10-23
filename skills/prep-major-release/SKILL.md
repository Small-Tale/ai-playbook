---
name: prep-major-release
description: Prepare a major release: ground yourself in what actually shipped since the last major, refresh every published package README against its manifest, exports, and tests, verify cross-package contracts, review the demo captures the docs embed, and hand the maintainer a precise list of what to retake.
allowed-tools: Read, Grep, Glob, Bash, Edit, Write, Agent
---

<!-- ai-playbook:skill name=prep-major-release v=1 -->

A lot changes between major releases. Prepare **every package released from the same tag**:
review their published READMEs and cross-package contracts, then review the demo captures and
hand the maintainer a precise list of which to re-capture. Work the parts in order and leave a
clear handoff. Tagging and publishing stay with the project's release command (see the
`release-scripts` rule); this skill prepares, it does not release.

## Ground yourself first

Before touching anything, build an accurate picture of what actually changed:

1. **What shipped.** Read `CHANGELOG.md` (the unreleased section plus the releases since the
   last major) for the user-visible changes. Read each package's manifest and current README;
   do not infer a package's state from the root changelog alone. If the release script has
   already moved the unreleased section, inspect the committed pre-release changelog too.
   When the changelog is thin, run the `technical-changelog` skill for the diff-grounded view.
2. **The current public API.** Read the API reference document and the real exports: the
   barrel files and subpath entries, the CLI's `--help`, the public routes. README claims about
   "N exports" or "a small API" must match.
3. **The pitch.** Re-read the overview document (what the product is and when to use it) and
   the root `README.md` end to end so your edits stay in the project's voice.
4. **The numbers.** Bundle-size and performance claims come **only from the project's
   documented benchmark source** (an upstream benchmark import, a CI-measured size gate).
   Never paste a number from an ad-hoc local run. If the story changed but the official source
   has not re-run, keep the qualitative framing rather than inventing figures.

## Part 1: every published README

Enumerate the published packages from the workspace manifests (`package.json` `workspaces`,
`Cargo.toml` `[workspace]`, or the release script's package list). Make the root `README.md`
compelling, accurate, and current; it is the landing page, not a changelog. Then review each
package README independently against its own manifest, public exports, tests, and
package-specific docs:

| Check | Against |
| --- | --- |
| Exports, subpaths, and entry points | the barrel, the `exports` map, or the public module list |
| Install and usage examples | run or compile them where the repository has a gate for it |
| Peer and version ranges | the manifests and the lockstep policy (`kerf-ui-upgrades` when installed) |
| Commands and scripts | the manifest scripts and the CLI's help output |
| Counts, limits, versions, and links | the code and the current release numbers |
| Generated templates | the generator's output for the current API |

Update stale claims, links, versions, counts, and command names. Record explicitly when a
README needs no edit. Do not skip a package because its README changed recently.

## Part 2: cross-package contracts

Verify that packages released together agree with each other: pinned versions between
lockstep packages, peer ranges, shared catalog or schema files, generated templates, and the
examples one package's README gives for another. A mismatch is a finding and usually a ticket,
not a silent edit.

## Part 3: demo captures

List every image the READMEs and docs embed. For each, open the current UI (the demo route or
an isolated instance) and compare. Produce the precise retake list: file, what it shows now,
what changed, and the state and viewport to capture. Capture yourself only when the project
has scripted capture tooling and the maintainer authorized it; otherwise the list is the
maintainer's handoff.

## Handoff

End with:

- the README edits made per package, and the packages that needed none;
- cross-package contract findings and their tickets;
- the retake list;
- anything blocking the release command, as tickets.

Do not run the release command, move the changelog's unreleased section, or push unless the
maintainer asked; the release script owns those steps.
