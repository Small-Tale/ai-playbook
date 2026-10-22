---
root: true
targets: ["*"]
description: "Design-system-first UI construction: look it up, name the owner, earn every control"
---

<!-- hotsheet:begin section=ui-composition v=2 -->

## UI Composition

Build interfaces from the design system's components, configured through their public API, and from the project's existing patterns. The design system's own guidance governs selection, layout, the styling boundary, and the interaction defaults (Kerf: see `kerf-ui-usage` and `kerf-ui-interaction-defaults`); this rule governs the process around it.

- **Look it up before you build it.** Before writing any UI, read the library guidance in its retrieval order, the project's component catalog and demo route, and the named reference project's same surface. Copy a working reference implementation rather than approximating it, and cite the paths you read in the preliminary note.
- **Name the owner of every region.** For a screen or redesign, the preliminary note lists each region and the public component that owns it: shell and rails, toolbars, search, tabs, columns, popups, banners, empty states, dialogs, the demo route. A handwritten `nav`, `button`, or `input` with CSS for border, selected, hover, or disabled state, position, or z-index is a defect unless the catalog has no component; then file the gap upstream and say so in the ticket. Raw `div`, `p`, or `span` where the library has a primitive is the same defect.
- **Configure, never override.** A missing prop, variant, or token is an upstream ticket referenced from the app ticket, which stays blocked rather than shipping an override. This holds even when the maintainer asks for the visual directly: name the conflict and the missing API, and file the gap.
- **Earn every control.** Every control, container, and line of copy traces to a human requirement or a reference precedent. Do not add explanatory paragraphs, permanent caveats, counts, "view options" menus, custom back and forward, theme toggles, duplicate titles, nested boxes, or editable fields for values the interaction already knows; use browser history and `prefers-color-scheme`. When a human says remove, remove; do not relocate.
- **Human words are the spec.** Carry the human's exact component, placement, state, and viewport nouns into derived tickets and test names. AI notes, preliminary thoughts, and rewritten requirements never supersede them; when a phrase admits two behaviors, ask with a `CHOICE` note before building.
- **Sign off before fanning out.** For a new screen or redesign, especially from a title-only ticket, post the region plan or wide and narrow captures and wait for feedback before building further; never fan dozens of tickets off an unreviewed layout.
- **Reuse semantics.** The same feature uses the same component everywhere, in a read-only variant when needed, never a copy; new lists inherit the app's selection, context-menu, edit, and autosave grammar; one concept per indicator and one name per concept.

<!-- hotsheet:end section=ui-composition -->
