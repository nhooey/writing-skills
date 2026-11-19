---
name: writing-hygiene-progressive-disclosure
description: >-
  Order a long document in layers, so a reader can stop after any one and still hold a true, complete picture at that depth: the summary with its totals, then what needs action, then the groups with their counts, then the detail, folded away where the medium folds and last or on request where it doesn't. Covers what belongs in each layer, the test that each layer stands without the ones below it, what is never folded (an action, a failure, a caveat), a fold's label that says what it holds and how much, the choice by medium (a fold on GitHub, order and an offer in a terminal reply, a closing section elsewhere), and when to leave a document alone (one screen, a reference read by lookup, a procedure). Any format: reports, audit results, PR descriptions, issues, replies. Use when a report runs past a screen, when its conclusion or the items needing action sit below routine detail, or when the user asks to "lead with the summary", "collapse the detail", "fold this away" or "give me the short version first".
tags: [writing, structure]
---

# Progressive disclosure

_A long document is ordered in layers, the summary and what needs action first, then the groups, then the detail folded away or last, so a reader can stop after any layer and still hold a true, complete picture at that depth._

Readers of one document need different depths.
Most need the result and whether anything is asked of them, a few need to check one group, and one may need every line.
A document written in the order the work produced it makes all of them read to the end to learn the result.
Layers let each reader stop where their need is met, and trust that what they skipped only adds detail.

## The layers

1. **The summary:** the result in a sentence or two, with the totals.
2. **What needs action:** each item the reader must act on or decide, by name and in full.
3. **The groups:** every group's heading and count, with the items of the groups that are short or that matter, as `writing-hygiene-group-by-reader-action` lays them out.
4. **The detail:** the evidence behind a claim already made, the full list behind a count, the items that need nothing, the raw output.

The test of a layer: cut the document off below it, and what is left is still true, and its totals still account for every item.
A summary that says "2 fail to build" stands without the list of failures.
A summary that says "some problems came up" does not, since the reader has to go down a layer to learn what it means.

A document with nothing to act on says so in its summary and has no second layer.

Where the groups carry emoji markers, as `writing-hygiene-group-by-reader-action` lays out, the summary's totals and each fold's label carry the same ones, so the eye ties a count in the first layer to its group further down.

## What goes in which layer

A fact moves up when leaving it out changes what the reader does or believes:

- an action or a decision asked of the reader;
- a failure, or anything the reader wouldn't expect;
- a caveat that changes what the summary means, such as "dry run, nothing was changed".

A fact moves down when the layer above already carries its conclusion:

- the evidence for a claim the summary makes;
- the items behind a count, where each needs nothing from the reader;
- output a reader opens only to check the writer's work.

Nothing in a lower layer contradicts a higher one.
A fact that would is a caveat, and belongs in the higher layer.

## Folds

A fold hides a block behind one line that the reader opens.

- **The label says what the fold holds and how much:** "Already current (4)", "Full log of the run, 212 lines".
  From the label alone the reader can decide not to open it.
- **Never folded:** an action, a failure or a caveat.
  A reader who opens nothing must still have seen all three.
- **Fold whole groups and whole blocks,** never the middle of a sentence or a list.
- **Fold from the bottom:** the uneventful majority and the raw output first.
  A document that is mostly folds has too little in its upper layers, or didn't need folding.

## By medium

Where the medium folds, fold the detail.
Where it doesn't, put the detail last, or leave it out and say where it is.

- **A medium that folds,** such as a GitHub issue, pull request or comment: fold the fourth layer.
  The syntax of a fold in Markdown, and where it renders, is in `markdown-hygiene-lists-headings-tables`.
- **A reply in a terminal,** where nothing folds and the reader can ask: give the first 3 layers, then name what was left out, its count, and the file or command that shows it.
  The reader who wants the detail asks for it or opens it.
  `markdown-hygiene-terminal-rendering` has what a terminal shows in place of a fold.
- **A document nobody can ask about and that doesn't fold,** such as a file read raw or a commit message: the detail goes last, under a heading of its own, or in a file the document links to.

## When to leave it alone

- **It fits on one screen.**
  The reader sees every layer at once, and a fold only adds a click.
- **It's reference material read by lookup,** such as a table of options.
  The reader jumps to one entry, and no entry is detail to another.
- **It's a procedure.**
  Every step is needed, in order, by the one reader who follows it.
- **Every item needs action.**
  Nothing is detail, so the order of importance is the whole structure.

## Example

A dry run's report in a medium that folds, each `▸` line standing for a fold drawn closed:

```text
Dependency update, dry run over 12 services: 2 fail to build, 2 need a decision, 8 need nothing from you.
Nothing was changed.

Fails to build (2)
- catalog: parser 4.0 removes `parse_legacy`, called in 3 files
- reports: parser 4.0 removes `parse_legacy`, called in 1 file

Needs a decision: a major version (2)
- gateway: router 6
- payments: router 6

▸ Patch updates, safe to apply (4)
▸ Already current (4)
▸ Full log of the run, 212 lines
```

The same report as a reply in a terminal, its last 3 blocks left out and pointed at:

```text
Dependency update, dry run over 12 services: 2 fail to build, 2 need a decision, 8 need nothing from you.
Nothing was changed.

Fails to build (2)
- catalog: parser 4.0 removes `parse_legacy`, called in 3 files
- reports: parser 4.0 removes `parse_legacy`, called in 1 file

Needs a decision: a major version (2)
- gateway: router 6
- payments: router 6

The 4 services with patch updates and the 4 already current are listed in `update-dry-run.log`, with the run's full output.
```

A reader who stops after the first 2 lines knows the result, that 4 services need them, and that nothing was changed.
One who reads on has every failure and decision in full, and never has to open a fold to find one.

## Quick heuristic

> Read only the first screen, then stop.
> If you know the result and everything asked of you, the layers are right.
> If you had to keep reading to learn either, something in the detail belongs higher.

## When to apply

- Writing or reviewing a report, an audit, a dry run's results, a long pull request description or a status update that runs past a screen.
- A document whose result, or whose items needing action, come after routine detail.
- Deciding what to fold in a medium that folds, and what to leave out of a reply in one that doesn't.
- The user asks for the summary first, the short version, or the detail collapsed.

## Related skills

When one of these applies and it's in your skill listing, load it
without asking. If it isn't in your listing, tell the user which skill is
missing and ask whether to install it from the same collection this skill
came from; don't apply it from memory.

- `writing-hygiene-group-by-reader-action`: sorting the items into the groups the third layer holds, each with its count.
- `markdown-hygiene-lists-headings-tables`: the Markdown syntax of a fold, `<details>` and `<summary>`, and where it renders.
- `markdown-hygiene-terminal-rendering`: Markdown read in a terminal, where nothing folds.
