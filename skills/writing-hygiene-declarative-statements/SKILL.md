---
name: writing-hygiene-declarative-statements
description: |
  Write every artifact as state: a snapshot says what is true, a delta says
  what became true (before → after), and neither narrates the steps that
  got there. Classify the artifact first: docs, code comments, SKILL.md
  files and plans' end-state nodes are snapshots; commits, PRs, turn
  replies and release notes are deltas. Covers the `key: old → new`
  notation, postconditions and invariants a test could check, describing
  the semantic change rather than the textual one ("formatting only" when
  nothing semantic changed), and the two word lists: timeless words a
  snapshot avoids (currently, now, new, no longer, previously, dates…) and
  narration a delta avoids (I, we, this commit, today, "as requested
  by"…). Use when writing or reviewing docs, comments, skills, plans,
  commit messages, PR bodies, release notes or an agent's turn replies.
tags: [writing, style]
---

# Declarative statements

_Write every artifact as state: a snapshot says what is true, a delta says what became true (before → after), and neither narrates the steps that got there._

A reader wants the state: what holds, or what changed. The steps the
writer took are the writer's story, and they bury the state under it.

## Snapshot or delta: classify first

Decide which the artifact is before writing a word:

| Kind     | States                                  | Artifacts                                                   |
| -------- | --------------------------------------- | ----------------------------------------------------------- |
| Snapshot | what is true, read at any time          | docs, code comments, SKILL.md files, plans' end-state nodes |
| Delta    | what became true, read against a before | commits, PRs, turn replies, release notes                   |

A snapshot read a year later must still be true or plainly wrong, never
"true as of when it was written". A delta is anchored to its change, so
it can say what was true before.

## State, not steps

- **Snapshot:** "X is Y". "Retries cap at 5", not "we set retries to 5".
- **Delta:** "X: before → after". "Retries: 3 → 5, because the upstream
  rate-limits at 6 a minute", not "I looked at the logs, then bumped the
  retry count".

Steps belong only where the steps are the content: a how-to, a runbook,
a plan's implementation node.

## Before → after notation

Write a changed value as `key: old → new`: `timeout: 30s → 60s`,
`default branch: main → trunk`. For several, one per line or a table row
each. An added thing is `→ new` and a removed one `old →`, or say
"added" and "removed" outright in a delta.

## Postconditions and invariants

State the outcome as a present-tense claim a test could check:

- Postcondition: "after `apply`, every repository has a ruleset named
  `default`".
- Invariant: "the lock file's inputs match `flake.nix`'s".

"Should work", "improved" and "cleaned up" are not checkable; name what
holds afterwards.

## Semantic, not textual

Describe the meaning that changed, not the characters. "Requests with a
BOM now parse" over "changed the regex on line 40". When nothing
semantic changed (reflowed text, renamed locals, reordered imports), say
"formatting only" and stop.

## Word lists

Timeless words, kept out of snapshots, since each one dates the text:

- currently, now, new, no longer, existing, latest
- soon, yet, used to, previously, as of
- dates and versions as markers of when ("since v3", "in 2026")

Narration, kept out of deltas, since the change's date and author are
already recorded:

- I, we, this commit, this change
- tonight, today, this morning, yesterday
- "as requested by" (credit goes in a trailer or a byline)

A delta may say "X now does Y": "now" there marks the after side of the
change, not the time of writing.

## Credit

The timeless list follows the reasoning of the
[Google developer documentation style guide's "Timeless documentation"](https://developers.google.com/style/timeless-documentation)
page, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## When to apply

- Writing or reviewing a doc, comment, skill or plan: it's a snapshot.
- Writing or reviewing a commit, PR body, release note or turn reply:
  it's a delta.
- Shaping a list or table of changes, or referring to things a delta
  changed.

## Related skills

When one of these applies and it's in your skill listing, load it
without asking. If it isn't in your listing, tell the user which skill is
missing and ask whether to install it from the same collection this skill
came from; don't apply it from memory.

- `writing-hygiene-prose-to-lists`: turning a run of before → after changes into a list.
- `writing-hygiene-refer-by-canonical-label`: naming the things a delta changed by their canonical labels.
- `git-hygiene-commit-message-format`: the commit message, the most common delta.
- `git-hygiene-no-history-in-tracked-files`: tracked files are snapshots, and their history goes in commit messages.
