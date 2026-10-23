---
root: true
targets: ["*"]
description: "Per-worker isolation, readiness waits, real pointer geometry, and flake criteria for Playwright suites"
---

<!-- hotsheet:begin section=playwright-operations v=2 -->

## Playwright Operations

- **Isolation.** Each worker gets its own server, port, and data directory (keyed on `parallelIndex`); each spec seeds its own data and addresses it by id; nothing shares state across specs or depends on order. Build the client once in global setup.
- **Waiting.** Wait on events, readiness signals, or state, never `waitForTimeout`. Route fixtures gate pending responses behind a promise, not a timer, and mirror the real endpoints' fields, optional values, and status codes.
- **Realism.** Interaction tests hit real targets (the glyph, the line number), use real pointer events rather than synthesized shortcuts, assert positive fitted geometry and distinct drag coordinates, hit-test overlays for clipping, and assert live `value`, focus, and emitted events rather than attributes. Resize wide to narrow to wide inside the test when layout is under test.
- **Engines and fonts.** Include WebKit for sizing, overflow, sticky layers, and focus rings; pin CI fonts to match local metrics when specs measure text.
- **Flakes.** A flake fix is done when `--repeat-each=N --workers=M --retries=0` passes under full-suite load; retries only in the full CI job, bounded at two, with a ticket per retried test; quarantine with a tagged title naming the fix ticket (see `test-operations`).
- **Captures.** Write screenshots to the runner's output directory as `<slug>-<state>-<width>.png`; wait for the state's settled readiness signal (enabled controls, finished transitions) and disable animations before capturing; attach the inspected captures to the ticket and never commit them; do not add snapshot diffing by default; review captures per `ui-evaluation`.

<!-- hotsheet:end section=playwright-operations -->
