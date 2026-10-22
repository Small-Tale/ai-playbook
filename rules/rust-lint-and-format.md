---
root: true
targets: ["*"]
description: "Clippy, rustfmt, pinned toolchain, and test isolation defaults for Rust crates"
---

<!-- hotsheet:begin section=rust-lint-and-format v=1 -->

## Rust Lint and Format

- `cargo clippy --all-targets -- -D warnings -D clippy::dbg_macro -D clippy::todo -D clippy::unimplemented` and `cargo fmt --check` run in the root check command, on a toolchain pinned by `rust-toolchain.toml`. Give the lint run its own target directory when it would otherwise invalidate the build cache.
- Force an isolated home for tests through `.cargo/config.toml` `[env]` so no test can touch the developer's real stores or settings; a test asserts the isolation.
- Libraries define errors with `thiserror`; binaries aggregate with `anyhow`.
- Build binaries once in test global setup, never per test file; integration tests spawn the built binary.
- An `#[allow]` carries a reason and a ticket slug; `#[ignore]` names the quarantine ticket (see `conventions-as-code` and `test-operations`).

<!-- hotsheet:end section=rust-lint-and-format -->
