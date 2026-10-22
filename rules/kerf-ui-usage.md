---
root: true
targets: ["*"]
description: "Where Kerf UI guidance lives, its retrieval order, the gates, Web Awesome policy, and component gaps"
---

<!-- hotsheet:begin section=kerf-ui-usage v=1 -->

## Kerf UI Usage

Kerf's own guidance is authoritative for component selection, layout and spacing, the styling boundary, accessibility, overlays, responsive layouts, theming tokens, writing style, and catalog authoring. Read it from the installed packages rather than restating it; in a workspace the paths are relative to the package that installs `@kerfjs/ui`.

- **Retrieval order, before touching any file that imports `kerfjs` or `@kerfjs/ui`:** `node_modules/kerfjs/ai/skill.md`; then `node_modules/@kerfjs/ui/llms.txt` and the order it prescribes (`docs/component-selection.md`, `ai/components/README.md` plus the pages for the components you use, `ai/public-api-signatures-v1.md`, `ai/skill.md`); then the project's consumer catalog extension and `ai/component-catalog.json`, respecting declared geometry ownership rather than inferring it from screenshots. For a screen add `docs/app-layouts.md`, `docs/layout.md`, and `docs/design-philosophy.md`; for controls `docs/accessibility.md`; for copy `docs/writing.md`.
- **Styling boundary.** `ai/skill.md` and `docs/design-philosophy.md` define what app CSS may do. In short: configure through props, variants, and public `--kui-*` tokens; never target `.kui-*` classes, parts, private tokens, or an app class placed on a Kerf root; never pad, size, or position a component from outside; import `foundation.css` then `document.css` and keep the browser-default root font size. Styling a Kerf component with application CSS is a bug, even when the maintainer asks for the visual directly: name the conflict and the missing API, and file the gap.
- **Setup and gates.** Run `npx kerfjs setup --ui` as a dry run, then with `--write --yes`, on day one and after every upgrade; add `--guidance-source AGENTS.md` when the project keeps one instruction file. Keep `kerf.components.json` authored and `component-composition.json` generated and byte-checked, and keep `kerf:check` (typecheck, Kerf ESLint `recommended-ui`, `kerf-component-catalog --check`, `kerf-ui-doctor --full` with `failOn: warning` and no suppressions) inside the root check command.
- **Web Awesome.** Never render a Discouraged `wa-*` element where a Kerf component replaces it (`Button`, `TextField`, `Select`, `PopupMenu`, `DialogSurface`, `TabBar`, `LucideIcon`); `docs/webawesome-migration.md` lists them. Inside `ToolbarControlGroup` use plain `<button type="button">`, not `wa-button` or a standalone `Button`.
- **Component gaps.** A missing prop, variant, or component is a `KF-*` ticket in the Kerf store (`hotsheet-cli -C <kerf-store> new --title "…" --category feature`) that describes the gap, referenced from the app ticket, which stays blocked rather than shipping an override; adopt the capability when it ships and remove any interim profile exception. Doctor budgets and profile exceptions only decrease.

<!-- hotsheet:end section=kerf-ui-usage -->
