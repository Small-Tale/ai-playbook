---
root: true
targets: ["*"]
description: "Directory roles, component granularity, CSS ownership, and size limits for web clients"
---

<!-- hotsheet:begin section=web-client-organization v=1 -->

## Web Client Organization

- **Layout.** Split the client by role: `app/` (entry, composition roots, interaction wiring), `components/` (reusable across features), `features/<domain>/` or `views/<area>/` (vertical slices: `index.tsx` plus a local `components/`), `lib/` or `platform/` (pure, UI-free modules), `shared/` (contracts shared with the server), and `ux-demo/demos/` (one file per component). Match the named reference project's layout when one exists. Kebab-case file names, PascalCase component names.
- **Components.** One exported PascalCase component per `.tsx` file; no private components defined inside another component's file. A component takes no props or one destructured named-props object. Its root class is the component name in kebab-case; its stylesheet sits beside it and is imported only by it. A view's `index.css` may import sub-sheets but never owns a sub-component's styles, and no component styles another component's markup. A component stylesheet is rare, and every rule in it has a stated reason.
- **Logic.** Pure logic lives in flat modules with a sibling unit test, not inside components. No import-time side effects: no listeners, observers, timers, or polling at module load; wiring happens in `app/` and returns a disposer. Server and client share schema-validated contracts (for example zod under `shared/contract`); the client imports inferred types only, and dev and test builds throw on response drift.
- **Size.** Split a file over about 500 lines, or one that mixes session orchestration with rendering, before the next feature lands in it; keep composition roots small. Extract discrete sections, dialogs, and repeated domain controls; never duplicate logic another module owns.
- **Generated artifacts** (catalogs, composition manifests, API contracts) are checked in and byte-checked in CI; regenerate them in the same change.

Deviate only at the project level for a compelling or necessary reason, recorded in the project's conventions doc.

<!-- hotsheet:end section=web-client-organization -->
