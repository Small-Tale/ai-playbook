---
root: true
targets: ["*"]
description: "Test isolation, build-once, flake and quarantine policy, and quiet output"
---

<!-- hotsheet:begin section=test-operations v=3 -->

## Test Operations

- **Isolation.** Tests never touch the developer's real home, stores, or running services. Force an isolated home and data directory at config level (environment in the test runner or build config, not in each test), and keep a test that fails on machine-local paths in fixtures or output.
- **Build once.** Binaries and client bundles build in the suite's global setup, skipped when fresh, never inside a test file. The full gate executes the built artifact (boot the bundle or binary and hit its health endpoint), not only builds it.
- **Waiting.** Wait on events, readiness signals, or state, never fixed delays. Fixtures that simulate pending responses gate on a promise or channel, not a timer.
- **Flakes.** A flake fix is done when the test passes repeatedly with retries disabled under full-suite load (for example `--repeat-each=20 --retries=0`). Retries run only in the full CI job, bounded at two, visible in the report, and every retried test gets a ticket. Quarantine markers name the fix ticket, one table row per marker, checked one-to-one in CI. A retry or quarantine is a reprieve, not a fix.
- **Output.** The quiet-output rule lives in `hotsheet-testing-philosophy`; the project's failure-only wrapper prints a summary, capped failure excerpts, and a log path. Keep a slowest-tests profile and act on it.
- **Record.** A script validates the coverage matrix (unit, end-to-end, manual per feature) by checking each status against its evidence paths; the manual test plan holds only what CI cannot do reliably.

<!-- hotsheet:end section=test-operations -->
