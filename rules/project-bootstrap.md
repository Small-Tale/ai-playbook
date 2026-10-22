---
root: true
targets: ["*"]
description: "Day-one quality gate, skeleton, and reference parity for a new project"
---

<!-- hotsheet:begin section=project-bootstrap v=1 -->

## Project Bootstrap

Install the full quality gate and the directory skeleton before the first feature commit of a new project or new package; do not defer them until there is more code. Adding them later costs a correction commit across the whole tree.

- **Gate first.** One root check command, run by CI, chains: formatter check; type-aware strict lint with the UI library's plugin; typecheck; unit tests; the UI library's catalog check and doctor with warnings failing and no suppressions; an end-to-end smoke. A bare `recommended` lint preset is not a gate. Wire the selected language rules (for example `typescript-lint-and-format`, `rust-lint-and-format`) into this command.
- **Reference project.** When a project is "based on" or "like" another, that project is a source to copy, not inspiration: open its config files, instruction files, directory layout, and the same screens, and carry them over before customizing. Record where the reference lives so later sessions find it. When the project must not name its sources in committed files (an internal project whose code becomes public), keep the pointer in a local, uncommitted note and say in the instructions that such a note exists.
- **First commit contents.** The directory skeleton the selected organization rule prescribes; the catalog or demo route with the first component demonstrated; the requirements doc, codebase map, requirements summary, and a UI conventions doc that points at the design system's guidance (each may be short); the structural policy-test file (empty is fine); the UI library's setup output (Kerf: `npx kerfjs setup`, then `npx kerfjs setup --write --yes`) with its generated files kept.
- **Instructions.** Add the library pointer block to the project instructions in the first commit so every session reads the library's guidance before building (Kerf: see `kerf-ui-usage`).

Deviate only at the project level for a compelling or necessary reason, recorded in the project's conventions doc.

<!-- hotsheet:end section=project-bootstrap -->
