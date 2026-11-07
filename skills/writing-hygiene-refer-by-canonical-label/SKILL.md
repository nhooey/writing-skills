---
name: writing-hygiene-refer-by-canonical-label
description: |
  Refer to each thing defined elsewhere (an issue, pull request, commit,
  branch, file, document, person, event, earlier message or list item) by
  one canonical label, used word for word every time, never by a cryptic
  identifier alone: no bare "#206", branch names, short SHAs, file paths or
  "the 2026-10-16 comment". The label is the one the thing already has where
  the reader would look (its title, subject, heading or name), or a short
  descriptive name coined at first mention. Machine identifiers go in
  parentheses after the label; an acronym comes first, with its expansion
  in parentheses at its first use; anything with an address is a link; vague
  pointers like "the fix above" are replaced by the label. Use whenever
  writing prose that refers to things defined elsewhere: status reports,
  PR bodies, commit messages, replies, reviews, docs, an agent's turn
  summaries.
tags: [writing, references]
---

# writing-hygiene-refer-by-canonical-label

Writers refer to things by the identifier they happen to have in hand: a
bare pull request number (#206), a branch name
(`up/22-bats-copy-path-macos`), a short SHA (`8127188`), an event by its
date ("the 2026-10-16 comment"). To the writer each is unambiguous. To the
reader each is a lookup: open the tracker, search the log, scroll the
thread, then come back and find their place. Three of those in one
paragraph and the reader stops following.

The rule: **each thing has one canonical label, and you use it word for
word every time you refer to it.** Identifiers ride along after it, in
parentheses; addresses make it a link.

## How to load this skill

Passive reference. Loading it doesn't mean the user wants anything
rewritten now; it means that whenever you refer to something defined
elsewhere, you'll name it so the reader doesn't have to look it up.

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
  in place of words.
- **An acronym comes first, its expansion after it in parentheses, at its
  first use in a text:** CRP (C-reactive protein). Don't coin an acronym
  where none is in common use.
- **Name an event by what happened, with the date after it.** "The
  maintainer's reply agreeing to Q2 and Q3 (2026-10-16)", not "the
  2026-10-16 comment".
- **Anything with an address is a link**, so the label itself is clickable:
  an issue's URL, a commit's page, a file's path in the repository, a
  message's permalink.
- **No vague pointers back.** "The fix above", "those PRs", "that branch",
  "the earlier issue": repeat the canonical label instead. The reader may
  have skipped "above", and in a long text "those" has several candidates.
- **The same label every time.** Don't call it "the macOS fix" in one
  paragraph, "the bats patch" in the next and "#206" in the third. Three
  names read as three things.

## Before and after

Links below are written in Markdown; use the link form of whatever format
you're writing in.

### Issues and pull requests

Before:

```text
#206 is ready, but it depends on #198. Once that lands I'll rebase.
```

After:

```markdown
[#206 "Fix new_project.bats on macOS…"](https://github.com/acme/widget/pull/206)
is ready, but it depends on
[#198 "Add a portable copy_path helper"](https://github.com/acme/widget/pull/198).
Once "Add a portable copy_path helper" lands I'll rebase
"Fix new_project.bats on macOS…" onto it.
```

### Branches

Before:

```text
I pushed up/22-bats-copy-path-macos and opened a PR from it.
```

After:

```markdown
I pushed the fix and opened
[#206 "Fix new_project.bats on macOS…"](https://github.com/acme/widget/pull/206)
(branch `up/22-bats-copy-path-macos`).
```

The branch is a detail of the pull request, so it goes in parentheses after
the pull request's label, never as the reference itself.

### Commits

Before:

```text
8127188 fixes it; 3f0a9c2 was a partial attempt, reverted in 77b1e04.
```

After:

```markdown
[`8127188` "Copy paths with cp -R on macOS"](https://github.com/acme/widget/commit/8127188)
fixes it. An earlier partial attempt,
[`3f0a9c2` "Use rsync to copy test fixtures"](https://github.com/acme/widget/commit/3f0a9c2),
was reverted in
[`77b1e04` "Revert: Use rsync to copy test fixtures"](https://github.com/acme/widget/commit/77b1e04).
```

### Files and documents

Before:

```text
See docs/adr/0007.md for the reasoning.
```

After:

```markdown
See ["ADR 7: Store sessions in Redis"](docs/adr/0007.md) for the reasoning.
```

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
The fix above also needs those PRs merged first.
```

After:

```text
"Copy paths with cp -R on macOS" also needs "Add a portable copy_path
helper" (#198) and "Pin bats to 1.11" (#201) merged first.
```

## Where it applies

Any prose that refers to things defined elsewhere: status reports, pull
request bodies, commit messages, issue comments, replies, code review
comments, docs, release notes, and an agent's progress updates and turn
summaries. The narrower the reader's context (someone arriving from a
notification, a reviewer skimming, the user returning after a break), the
more each label saves them.

Platform specifics, such as how to label GitHub issues, pull requests and
commits and how to fetch their titles, are in
`github-hygiene-refer-to-issues-and-pull-requests`.

## When to apply

- Writing any sentence that mentions an issue, pull request, commit,
  branch, file, document, person, event, earlier message or list item.
- Reviewing text that uses bare numbers, SHAs, branch names, paths or dates
  as references, or points back with "above", "those" or "that".
- Coining a name for something that has none: use it identically from then
  on.

## Related skills

When one of these applies and it's in your skill listing, load it
without asking. If it isn't in your listing, tell the user which skill is
missing and ask whether to install it from the same collection this skill
came from; don't apply it from memory.

- `github-hygiene-refer-to-issues-and-pull-requests`: this rule applied to GitHub: issue and pull request titles, cross-repo references, commit SHAs with subjects, fetching labels with `gh`.
