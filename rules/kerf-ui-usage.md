---
root: true
targets: ["*"]
description: "Where Kerf UI guidance lives, its retrieval order, the gates, Web Awesome policy, and component gaps"
---

<!-- hotsheet:begin section=kerf-ui-usage v=3 -->

## Kerf UI Usage

Installed Kerf guidance owns selection, layout/spacing, styling, accessibility, overlays, responsive behavior, tokens, copy and catalogs. Paths below are relative to the package installing `@kerfjs/ui`.

- Before editing any file importing `kerfjs`/`@kerfjs/ui`, read `node_modules/kerfjs/ai/skill.md`, then `node_modules/@kerfjs/ui/llms.txt` and its order: `docs/component-selection.md`, `ai/components/README.md` plus used components, `ai/public-api-signatures-v1.md`, `ai/skill.md`; then the project's consumer extension and `ai/component-catalog.json`. Respect declared geometry ownership, not screenshot guesses. For screen/toolbar/list/dialog/editor read `docs/interaction-conventions.md`; screens also `docs/app-layouts.md`, `docs/layout.md`, `docs/design-philosophy.md`; controls `docs/accessibility.md`; copy `docs/writing.md`.
- Configure public props/variants/`--kui-*` tokens only. Never target `.kui-*`, parts, private tokens or an app class on a Kerf root, nor externally pad/size/position it. Import `foundation.css` then `document.css`; preserve default root font size. Read styling contracts in `ai/skill.md` and `docs/design-philosophy.md` before styling.
- Day one and each upgrade: dry-run `npx kerfjs setup --ui`, then `--write --yes`; add `--guidance-source AGENTS.md` for single-file instructions. Author `kerf.components.json`; generate/byte-check `component-composition.json`. Root check includes `kerf:check`: typecheck, Kerf ESLint `recommended-ui`, `kerf-component-catalog --check`, `kerf-ui-doctor --full`, `failOn: warning`, no suppressions.
- Never render Discouraged `wa-*` where Kerf replaces it; read `docs/webawesome-migration.md`. Inside `ToolbarControlGroup` use plain `<button type="button">`, neither `wa-button` nor standalone `Button`.
- Missing API/component: file `KF-*` in Kerf's store, describe the gap and link from the blocked app ticket; never ship CSS overrides, even for a maintainer-requested visual. Name the conflict/missing API, adopt upstream capability and remove interim profile exceptions when shipped. Doctor budgets/profile exceptions only decrease.

<!-- hotsheet:end section=kerf-ui-usage -->
