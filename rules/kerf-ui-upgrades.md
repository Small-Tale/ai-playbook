---
root: true
targets: ["*"]
description: "Lockstep Kerf package upgrades with setup, catalog, and guidance refresh"
---

<!-- hotsheet:begin section=kerf-ui-upgrades v=1 -->

## Kerf UI Upgrades

- Pin `kerfjs`, `@kerfjs/ui`, `eslint-plugin-kerfjs`, and `create-kerf-component` to one exact version and assert the match in a unit test.
- On each Kerf release: bump all four in lockstep; re-run `npx kerfjs setup` with the project's options (`--ui`, `--guidance-source`) as a dry run and then with `--write --yes`; regenerate the catalog; run the full root check; re-read `node_modules/@kerfjs/ui/ai/skill.md` and the changelog for newly Discouraged Web Awesome elements and new primitives; remove app workarounds and profile exceptions the release makes obsolete; file a `KF-*` ticket for anything the release broke.
- Never work around a Kerf regression locally: stay on the last good version, file the ticket, and upgrade when the fix ships.

<!-- hotsheet:end section=kerf-ui-upgrades -->
