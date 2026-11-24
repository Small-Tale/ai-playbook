---
root: true
targets: ["*"]
description: "Draft release notes and commit messages with gitgist, configured once per repository"
---

<!-- hotsheet:begin section=gitgist-release-notes v=2 -->

## gitgist Release Notes

Pin gitgist as a dev dependency. Wire `commit:msg` to `gitgist --staged --commit-message` and release notes to `gitgist <last-tag>..HEAD` (default: latest tag to HEAD). Use these for large commits and every release; edit drafts and retain `git-commit-and-push` subject shape.

- Configure once in root `gitgist.config.json` or the `package.json` `gitgist` key: `exclude`, `provider`, `maxDiffChars`, `linkCommits`. Never repeat repository settings as flags in CI. Unknown keys fail; CLI `--exclude` appends. Since 1.2.0 notes read code diffs, so permitted input is a repository decision, not ad hoc flags.
- Built-ins exclude lockfiles, source maps and `dist/`. Add all generated/imported files (captures, guidance mirrors, benchmark imports, snapshots); keep additions in an instruction table of pattern/reason. Exclusions hide diff bodies, not change listings. Keep hand-authored content included regardless of size.
- Default to signed-in `claude` CLI (`claude-cli`); never add repository/CI API keys for notes alone. Configure `--fallback-provider`; `--no-ai` is the deterministic offline release floor.
- Commit fixed-section/order/emoji templates and pass `--template` from the release script. Enable `linkCommits` for GitHub/GitLab/Bitbucket remotes.
- Before tagging, read every draft: remove internal noise, verify claims against the diff and add migration steps, then write changelog/tag notes. Never commit unread drafts.

Project-level deviations require a compelling/necessary reason in conventions.

<!-- hotsheet:end section=gitgist-release-notes -->
