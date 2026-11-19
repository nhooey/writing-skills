---
name: writing-hygiene-group-by-reader-action
description: >-
  Sort a long, flat run of like items into groups by the one attribute that decides what the reader does with each, such as outcome, risk, owner or next action, with each group's count in its heading and the groups in order of importance. Covers the test for the group key (each group gets one action from the reader), keys that fail it (run order, alphabet, the writer's categories), headings that name the value and its count, emoji as markers (one per group, risk or status, the same every time, never decoration), when not to group (a handful of items, a sequence, a comparison across properties, a list looked up by name), and keeping the grouping faithful (every item in exactly one group, no invented groups). Any format: reports, audit results, status updates, PR descriptions, replies. Use when a list or table runs past a screen, when the reader must scan every row to find the ones that need them, or when the user asks to "group these", "sort by outcome", "mark these with emoji" or "make this easy to skim".
tags: [writing, structure]
---

# Group by what the reader acts on

_A long, flat run of like items is sorted into groups by the one attribute that decides what the reader does with each item, each group headed by its value and its count, the groups in order of importance, and each kind marked by one emoji._

A reader of a long list is looking for the items that need them.
In a flat list those items sit wherever the order happened to put them, so the reader scans every row and sorts the rows in their head.
Grouping does that sorting once, on the page: the reader reads the headings, opens the groups that are theirs and skips the rest.

## The pattern

1. **Name the item.**
   Say what one row is: a repository, a finding, a task.
   Every row is one of those, and each appears once.
2. **Pick the key.**
   The key is the attribute whose value decides what the reader does with an item, as [Choosing the key](#choosing-the-key) lays out.
3. **Sort every item into the group for its value.**
   Each item lands in exactly one group.
4. **Head each group with its value and its count,** as [Headings and counts](#headings-and-counts) lays out.
5. **Order the groups by importance to the reader,** what needs action first and what needs nothing last.
6. **Order the items inside a group** by a second attribute the reader cares about, or by name when there is none.
7. **Mark each kind with one emoji** where the eye should find it before reading, as [Markers](#markers) lays out.

## Choosing the key

The key passes one test: the reader does one thing with every item in a group, and a different thing with the items of the next group.
"Fix these", "decide on these", "nothing to do here" are three groups.
Two groups the reader treats the same are one group.

Attributes that often pass:

- **Outcome:** failed, changed, unchanged, skipped.
- **Risk:** what could lose data, what needs a look, what is safe.
- **Owner:** whose move each item is.
- **Next action:** merge, review, rerun, wait.

Which of them passes depends on the reader this document has.
A report to the person who will fix the failures groups by outcome, and the same items sent to a team lead group by owner.

Attributes that fail the test, because the reader does nothing different across their values:

- **The order the work ran in,** and the alphabet.
  These are orders inside a group, not groups.
- **The writer's categories:** the tool that found each item, the step that produced it, the file the data came from.
- **An attribute with a value per item,** which is a sort order.
- **An attribute with one value for every item,** which is a sentence above the list.

A key gives a handful of groups, 2 to about 7.
More than that and the headings are themselves a long list, so merge the groups the reader treats alike.

When 2 attributes pass, the key is the one the reader acts on first, and the second is the order inside each group.
Nest a second level of groups only where a group is still too long to scan.

## Headings and counts

- **The heading names the value in the reader's words, then the count in parentheses:** "Failed (3)", not "Exit code 1" or "Category B".
- **Where the action isn't plain from the value, the heading says it:** "Needs a decision: a major version (2)".
- **The counts add up to a total stated above the groups,** so the reader sees the proportions at once and can tell that nothing is missing.
- **A group the reader would look for and that is empty** is stated in the line that holds the total, "none failed", and gets no heading.
- **The heading is a real heading** where the document has them, and the parent item of a nested list inside a section or a short reply.

## Markers

A marker is one emoji that stands for one value of one attribute: this group, this risk, this status.
The same value carries the same emoji everywhere it appears, and no emoji stands for 2 values.
The eye then finds every item of a kind, and how the kinds are spread, before it reads a word.

- **Mark what the reader looks for first.**
  That is the key's values, on each group's heading and on its count in the total.
  Or it is a second attribute, marked on each item in place of a second level of groups.
- **The marker leads its line,** so the markers run down the margin as a column.
- **The word stays.**
  A marker sits beside the name of its value and never replaces it, since an emoji can fail to draw and says nothing when the text is searched or read aloud.
- **A legend where a marker appears away from its name:** on items, or once there are more kinds than the reader holds in mind, about 4.
  It sits above the groups, and it is a set of parallel items, each marker with its meaning, so it follows `writing-hygiene-prose-to-lists`.
- **Mark, don't decorate.**
  An emoji that tells no kind from another is removed: if deleting it loses the reader nothing, it was decoration.
- **An emoji the reader already reads one way keeps that meaning.**
  ✅ and ❌ mark a pass and a fail, and a kind that is neither takes another emoji.
- **In a terminal an emoji's width varies.**
  `markdown-hygiene-terminal-rendering` has the check to run before one goes in a table or under an underline.

Groups keyed by owner, which decides who acts, with status marked on each item:

```text
Open pull requests (7):
- 🔴 checks failing (2)
- 🟡 waiting on review (3)
- 🟢 ready to merge (2)

Yours (4)
- 🔴 Bump the parser to 4.0
- 🟡 Cache the index between runs
- 🟡 Split the release job
- 🟢 Drop the legacy flag

The platform team's (3)
- 🔴 Pin the base image
- 🟡 Retry flaky uploads
- 🟢 Rename the config key
```

The reader finds both failing pull requests at a glance, in either group, with no second level of headings.

## When to leave it alone

- **A handful of items,** few enough to take in at a glance.
  Order them by importance and stop.
- **The order is the content:** steps, a timeline, a ranking.
  Grouping would break the sequence.
- **The reader compares the items against several properties** to choose among them.
  That is a table, as `writing-hygiene-tables-for-comparison` says, and the key is at most the column it is sorted by.
- **The reader looks an item up by its name,** as in a glossary or a list of options.
  Alphabetical order serves a lookup, and no attribute is acted on.

## Keeping it faithful

- **Every item is in exactly one group.**
  An item that fits 2 groups goes in the more important one, with the other fact kept in its text.
- **No item is dropped,** the awkward one included.
- **No group is invented.**
  A group's value is a fact about its items, not a label that makes the page look even.
- **A leftover group is named for what its items share,** "Not checked (2)", never "Other" or "Misc".
- **Each item keeps its own facts.**
  The heading carries what the group shares, and only that is removed from the item.

## Example

A flat list, in alphabetical order:

```text
Dependency update, dry run:

- auth: already current
- billing: 3 patch updates
- catalog: build fails on parser 4.0
- checkout: 1 patch update
- docs: already current
- gateway: needs router 6, a major version
- inventory: 2 patch updates
- mail: already current
- payments: needs router 6, a major version
- reports: build fails on parser 4.0
- search: 1 patch update
- web: already current
```

Grouped by outcome, which decides what the reader does with each service:

```text
Dependency update, dry run over 12 services: 2 fail to build, 2 need a decision, 8 need nothing from you.

Fails to build (2)
- catalog: parser 4.0
- reports: parser 4.0

Needs a decision: a major version (2)
- gateway: router 6
- payments: router 6

Patch updates, safe to apply (4)
- billing: 3
- checkout: 1
- inventory: 2
- search: 1

Already current (4)
- auth
- docs
- mail
- web
```

The 4 services that need the reader moved from rows 3, 6, 9 and 10 to the top.
The alphabet, which was the whole order, is the order inside each group.
Every service is still there once, and the counts add up to 12.

## Quick heuristic

> Ask what the reader will do with each item, and write the answers down.
> If a handful of different answers come back, those are the groups, in the order the reader should get to them.
> If the answer is the same for every item, say so once and leave the list flat.

## When to apply

- Writing or reviewing a report, an audit, a dry run's results or a status update that lists more items than fit on a screen.
- A table whose reader acts on one column, whose values repeat down the rows.
- A list the reader must scan in full to find the items that need them.
- Putting an emoji in a report, a list or a table, to check that it marks a kind.
- The user asks to group, sort or break down a list, or to make a report easy to skim.

## Related skills

When one of these applies and it's in your skill listing, load it
without asking. If it isn't in your listing, tell the user which skill is
missing and ask whether to install it from the same collection this skill
came from; don't apply it from memory.

- `writing-hygiene-progressive-disclosure`: which groups stay open and which are folded away or left to the end.
- `writing-hygiene-tables-for-comparison`: when the reader compares items across several properties, a table instead of groups.
- `writing-hygiene-prose-to-lists`: turning a run-on sentence into the list that is then grouped, and the shape of a legend.
- `writing-hygiene-headings-as-outline`: the heading tree the group headings join.
- `markdown-hygiene-terminal-rendering`: checking an emoji's width before it marks anything read in a terminal.
