---
name: writing-hygiene-refer-by-canonical-label
description: Load before writing or editing prose that mentions a file, branch, document, person, event, earlier message, list item or code, in a report, GitHub issue, PR body, commit message, message to another project, reply, review or doc. Names each by one readable label, never a bare identifier, and links code by a pinned permalink. For issues, PRs and commits, `github-hygiene-refer-to-issues-and-pull-requests` has the format.
---

# Refer by canonical label

_Each thing defined elsewhere has one canonical label, used word for word every time, with its machine identifiers in parentheses after it and a link when it has an address._

Writers refer to things by the identifier they happen to have in hand: a
bare pull request number (#206), a branch name
(`up/22-bats-copy-path-macos`), a short SHA (`8127188`), an event by its
date ("the 2026-10-16 comment"). To the writer each is unambiguous. To the
reader each is a lookup: open the tracker, search the log, scroll the
thread, then come back and find their place. Three of those in one
paragraph and the reader stops following.

## Choosing the canonical label

- **Use the label the thing already has where the reader would look.** An
  issue or pull request: its title. A commit: its subject line. A section
  of a document: its heading. A person: their name. A file: its title, or
  its name when it has no title.
- **Several candidates: pick the one the reader sees where they'd look.** A
  pull request has a number, a branch and a title; the reader looking at
  the tracker sees the title, so the title is the label, not the branch.
- **None: coin a short descriptive name at first mention.** "The macOS copy
  fix", "the flaky-login investigation". From then on that coined name is
  canonical: use it exactly, don't drift to a synonym.

### The only variation: truncation

A long label may be cut at a word boundary, marked with `…`:
#206 "Fix new_project.bats on macOS…". Never paraphrase, abbreviate or
reorder it; the reader should be able to search for the words and find the
thing.

## Rules for using it

- **Machine identifiers go after the label, in parentheses, never in its
  place.** Numbers, branch names, SHAs, paths and dates help the reader
  find the thing once they know what it is; they don't tell them what it
  is. Branch names read especially badly: dashes, slashes and underscores
  in place of words. A GitHub issue, pull request or commit is the one
  exception: its number or short SHA leads, as in
  `#206 "Fix new_project.bats on macOS…"`, the form
  `github-hygiene-refer-to-issues-and-pull-requests` sets out, since
  GitHub renders and links the number.
- **An acronym comes first, its expansion after it in parentheses, at its
  first use in a text:** CRP (C-reactive protein). Don't coin an acronym
  where none is in common use.
- **Name an event by what happened, with the date after it.** "The
  maintainer's reply agreeing to Q2 and Q3 (2026-10-16)", not "the
  2026-10-16 comment".
- **Anything with an address is a link**, so the label itself is clickable:
  an issue's URL, a commit's page, a file's path in the repository, a
  message's permalink.
  A spot in code is linked the same way, by a permalink pinned to a commit, as [Pointing at code](#pointing-at-code) says.
- **No vague pointers back.** "The fix above", "those PRs", "that branch",
  "the earlier issue": repeat the canonical label instead. The reader may
  have skipped "above", and in a long text "those" has several candidates.
- **The same label every time.** Don't call it "the macOS fix" in one
  paragraph, "the bats patch" in the next and "#206" in the third. Three
  names read as three things.

### Pointing at code

Prose that points at code refers to the diff and never repeats it, so it holds no list of the commits, the changed files or what each file does.
The diff is one click away and always exact, while a copy of it in prose is more to read and drifts as soon as the branch moves on.
Say what the change achieves and why, and leave the how to the diff.

Where one spot in the code matters to the point, link that file and line range with a GitHub permalink pinned to a full commit SHA, such as `https://github.com/<owner>/<repo>/blob/<sha>/<path>#L10-L20`.
A SHA never moves, so the link shows the same lines after later pushes, rebases and merges.
A branch link, `blob/<branch>/<path>`, shows whatever the branch holds when the reader clicks, so it's only for "the current version".
The link's text is the name of what it points at, such as a function, a setting or a file.

This holds in pull request descriptions, commit messages, reports and agent replies alike.

## Before and after

Links below are written in Markdown; use the link form of whatever format
you're writing in.

### Issues, pull requests, commits and branches

`github-hygiene-refer-to-issues-and-pull-requests` sets out the forms for
these, with before-and-after examples: the number or short SHA, then the
title or subject in quotes, linked, and a branch only in parentheses after
its pull request.

### Files and documents

Before:

```text
See docs/adr/0007.md for the reasoning.
```

After:

```markdown
See ["ADR 7: Store sessions in Redis"](docs/adr/0007.md) for the reasoning.
```

### Code a change touches

Before:

```text
This PR changes three files:
- config.py: adds a retry_limit setting
- client.py: retries failed requests up to retry_limit times
- test_client.py: adds tests for the retry loop
```

After:

```markdown
Failed requests are retried up to `retry_limit` times before the error reaches the caller.
The backoff resets after any success, in [`send_with_retry`](https://github.com/acme/widget/blob/4f2c9e1a7b3d5e8f0a1c2b3d4e5f6a7b8c9d0e1f/client.py#L42-L58), so one bad minute doesn't slow every request after it.
```

The file list is the diff's job.
The one spot worth reading is a click away, at the lines the sentence was written about, even after the branch moves on.

### Dated events

Before:

```text
Per the 2026-10-16 comment, we're dropping Q1. The 10/14 meeting already
covered Q4.
```

After:

```markdown
Per [the maintainer's reply agreeing to Q2 and Q3 but not Q1 (2026-10-16)](https://github.com/acme/widget/issues/190#issuecomment-123456),
we're dropping Q1. Q4 was already deferred in the planning call with the
maintainers (2026-10-14).
```

### Agent turns and earlier messages

Before:

```text
As I said two turns ago, the second option is safer. The change from
earlier is still uncommitted.
```

After:

```text
As I said when comparing the two migration options, "migrate in place
with a backup" is safer than "dump and restore". The "Rename the config
loader" change is still uncommitted.
```

A turn number or "earlier" makes the reader scroll back; the option's own
name and the change's own name don't.

### List items and kanban items

Before:

```text
Item 3 is done and 5 is blocked on 3, so I moved 5 to Todo.
```

After:

```text
"Add the --dry-run flag" (item 3) is done, and "Document --dry-run in the
README" (item 5), which was waiting on it, moved to Todo.
```

Numbers change when a list is reordered or regenerated; the item's text
doesn't. Keep the number only as a parenthetical aid.

### Vague pointers

Before:

```text
The section above also needs those diagrams redrawn first.
```

After:

```text
"Rollback plan" also needs the "Session lifecycle" and "Cache eviction"
diagrams redrawn first.
```

## When to apply

The narrower the reader's context (someone arriving from a notification, a
reviewer skimming, the user returning after a break), the more each label
saves them.

- Writing any sentence that mentions an issue, pull request, commit,
  branch, file, document, person, event, earlier message or list item, in
  any prose: status reports, pull request bodies, commit messages, issue
  comments, replies, code review comments, docs, release notes, and an
  agent's progress updates and turn summaries.
- Reviewing text that uses bare numbers, SHAs, branch names, paths or dates
  as references, or points back with "above", "those" or "that".
- Describing a change: link the code that matters instead of listing commits or files.
- Coining a name for something that has none: use it identically from then
  on.

## Your preferences

!`cat "${CLAUDE_SKILL_DIR}/../writing-hygiene-refer-by-canonical-label.preferences.md" "${CLAUDE_PROJECT_DIR}/.agents/skills/writing-hygiene-refer-by-canonical-label.preferences.md" 2>/dev/null || true`

If your agent doesn't run the line above, read these files yourself if they
exist: `writing-hygiene-refer-by-canonical-label.preferences.md` next to this skill's folder, then
`.agents/skills/writing-hygiene-refer-by-canonical-label.preferences.md` in the project. A project's
file overrides the user's, and the user's overrides this skill's defaults.

## Related skills

When one of these applies and it's in your skill listing, load it
without asking. If it isn't in your listing, tell the user which skill is
missing and ask whether to install it from the same collection this skill
came from; don't apply it from memory.

- `github-hygiene-refer-to-issues-and-pull-requests`: this rule applied to GitHub, and the one source for the forms of issue, pull request, commit and branch references: titles, cross-repo references, commit SHAs with subjects, fetching labels with `gh`.
- `coding-agent-skill-references`: the preferences files this skill reads.
- `git-hygiene-commit-message-format`: what a commit body cuts, such as diff paraphrase, which a permalink to the code replaces.
