---
root: true
targets: ["*"]
description: "Draft release notes and commit messages with gitgist, configured once per repository"
---

<!-- hotsheet:begin section=gitgist-release-notes v=1 -->

## gitgist Release Notes

gitgist turns a commit range into grounded, user-facing release notes and drafts a commit message from the staged diff. Since 1.2.0 it reads the range's actual code diff, so what it is allowed to read is a repository decision recorded in config, not a flag typed per run.

- **Install and wire.** A pinned dev dependency with two call sites: a `commit:msg` script that runs `gitgist --staged --commit-message`, and the release script calling `gitgist <last-tag>..HEAD` (no range means latest tag to `HEAD`). Draft large commits and every release's notes with these rather than summarizing a diff by hand; the author edits the draft and keeps the repository's slug-first subject shape (`git-commit-and-push`).
- **Configure once.** Settings live in `gitgist.config.json` at the repository root or under the `gitgist` key of `package.json`, never repeated as flags in CI: `exclude`, `provider`, `maxDiffChars`, `linkCommits`. Command-line `--exclude` patterns append to the file's list, and unknown keys are rejected, so keep the file to documented keys.
- **Exclude generated and vendored files.** The built-in list already covers lockfiles, source maps, and `dist/`. Add every file the repository generates or imports (demo captures, AI guidance mirrors, benchmark imports, snapshots), because one regeneration would otherwise consume the diff budget and crowd out real source changes. Excluded files still show as changed, only without a diff body. Keep the project's additions in a two-column table in the instructions, pattern and why, and leave hand-authored content included however large it is.
- **Provider.** Default to the signed-in `claude` CLI (`claude-cli`), which needs no API key; never add an API key to the repository or CI for notes alone. Configure `--fallback-provider` so one flaky backend does not block a release. `--no-ai` is the deterministic offline path and the floor the release script falls back to.
- **House style.** When the project wants fixed sections, order, or emoji, commit a template file and pass it with `--template` from the release script instead of post-editing every draft.
- **Traceable bullets.** Enable `linkCommits` in a repository with a GitHub, GitLab, or Bitbucket remote so each bullet ends with the commit it came from.
- **Review before tagging.** The draft is an input, not the notes: remove internal noise it kept, check each claim against the diff, add the migration steps it cannot know, and only then let the release script write the changelog and the tag message. A draft is never committed unread.

Deviate only at the project level for a compelling or necessary reason, recorded in the project's conventions document.

<!-- hotsheet:end section=gitgist-release-notes -->
