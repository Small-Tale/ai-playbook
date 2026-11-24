---
root: true
targets: ["*"]
description: "Design-system-first UI construction: look it up, name the owner, earn every control"
---

<!-- hotsheet:begin section=ui-composition v=4 -->

## UI Composition

Use design-system public APIs and existing project patterns. Its guidance owns selection, layout, styling and interaction defaults (Kerf: `kerf-ui-usage`, `kerf-ui-interaction-defaults`).

- Before UI edits read library guidance in order, project catalog/demo and the named reference's same surface. Copy the working reference; cite paths in preliminary thoughts.
- For screens/redesigns, post a region plan naming every public component owner, including shell/rails, toolbars/search/tabs/columns, popups/banners/empty states/dialogs and demo. Handwritten styled navigation/controls or raw elements replacing library primitives are defects unless the catalog lacks one; ticket that gap upstream. Honor explicit design-system composition exceptions (e.g. Kerf toolbar plain buttons).
- Configure, never override: a missing prop/variant/token blocks the app ticket pending a linked upstream capability. Even for a maintainer-requested visual, name conflict/API and file the gap.
- Every control/container/copy needs a human requirement or reference precedent. No unsolicited explanations/caveats/counts, view menus, custom history, theme toggles, duplicate titles/nested boxes or fields for known values; use browser history and `prefers-color-scheme`. Remove means remove, never relocate.
- Carry human component/placement/state/viewport nouns into tickets/tests. AI notes or rewrites never supersede them; ambiguous behaviors need a `CHOICE` note before building.
- For new screens/redesigns, post a region plan or wide/narrow captures and wait for feedback before building further. **Bounded one-screen exception:** when its ticket states intent, proceed after posting the region plan in preliminary thoughts; wait before deriving further tickets or screens. Never fan dozens of tickets from an unreviewed layout.
- Reuse the same component per feature, read-only variant when needed, never a copy. Lists inherit selection/context-menu/edit/autosave grammar. One concept per indicator and one name per concept.

<!-- hotsheet:end section=ui-composition -->
