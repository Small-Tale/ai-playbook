---
root: true
targets: ["*"]
description: "Prettier, strict type-aware ESLint, and tsconfig defaults for TypeScript packages"
---

<!-- hotsheet:begin section=typescript-lint-and-format v=1 -->

## TypeScript Lint and Format

- **Format.** Prettier runs repo-wide (code, docs, YAML) as the first step of the lint command; house defaults are 120 columns and single quotes. Lint bans `prettier-ignore`; generated files go in `.prettierignore`.
- **Lint.** ESLint flat config with `typescript-eslint` `strictTypeChecked`, `strict-boolean-expressions`, `switch-exhaustiveness-check`, `consistent-type-imports`, import sorting, JSX self-closing, and the UI library's preset (Kerf: `eslint-plugin-kerfjs` `recommended-ui`). Run with `--max-warnings 0` and `reportUnusedDisableDirectives: error`. Restrict barrel imports that defeat tree-shaking (for example icon libraries) with `no-restricted-imports`.
- **Types.** `tsconfig` `strict` plus `noUncheckedIndexedAccess`; scripts and config files are linted without type information rather than excluded.
- **Order.** Format check, lint, typecheck, then the UI library doctor last (Kerf: `kerf-ui-doctor --full` with `failOn: warning` and `suppressions: []`), all inside the root check command.
- Fix lint and type errors as you go; never finish with a warning. Suppression and policy-test governance is in `conventions-as-code`.

Deviate only at the project level for a compelling or necessary reason, recorded in the project's conventions doc.

<!-- hotsheet:end section=typescript-lint-and-format -->
