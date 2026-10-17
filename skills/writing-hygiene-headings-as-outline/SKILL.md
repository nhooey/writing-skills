---
name: writing-hygiene-headings-as-outline
description: |
  Break a long, single-stream document into a heading hierarchy that mirrors
  its topic structure, so the headings alone read as an outline and the
  reader can skim the shape before committing to the prose. Covers when a
  wall of text is hiding sections (topic shifts, parallel sub-topics,
  "first… also… finally" seams), how to assign levels (one title, sections,
  sub-sections, no skipped levels), how to write heading text that scans,
  why a bold line is not a heading, and when not to add headings (a few
  paragraphs on one topic, a chat message, a single linear argument). Any
  format: docs, READMEs, design docs, RFCs, long PR descriptions, release
  notes, reports. Use when a document runs longer than a screen and covers
  more than one topic, or when the user asks to "add headings", "give this
  structure", "make it skimmable", "outline this" or "break this into
  sections".
tags: [writing, structure]
---

# writing-hygiene-headings-as-outline

A document longer than a screen is read in two passes: first the reader
skims to find the part they need, then they read that part. Headings are
what the first pass lands on. A good heading tree is an outline the eye can
walk (the title, the major sections, their sub-points), so the reader builds
a map of the whole before reading a word of body text. A document with no
headings forces every reader to read linearly to find anything; a document
with the wrong headings sends them to the wrong place. This skill gives a
document a heading shape that matches its actual topic hierarchy.

It covers when and why, in any format. Heading syntax in a given format
(Markdown's `#` levels, ATX style) is in
`markdown-hygiene-lists-headings-tables`.

## How to load this skill

Passive reference. Loading it doesn't mean the user wants a document
restructured now; it means that when you write or edit a long document,
you'll give it an outline.

## When this applies

Add or restructure headings when the document has structure its formatting
hides:

- **It runs longer than a screen and covers more than one topic**: the
  reader can't see the whole at once, so they need signposts.
- **Topic shifts are buried mid-stream**: a paragraph quietly changes
  subject ("Now, on deployment…", "A separate concern is…"). Each seam is a
  heading waiting to be cut.
- **Parallel sub-topics sit at the same level**: three install methods, four
  config sections, five API endpoints. Sibling topics want sibling headings
  so their parity is visible.
- **You navigate by searching instead of by eye**: if finding a section
  means searching for a word rather than scanning the margin, the structure
  isn't surfaced.
- **Bold pseudo-headings are doing a heading's job**: a bold label on its
  own line followed by a paragraph is a heading that forgot to be one. It
  won't appear in the table of contents or outline view and gets no link
  anchor.

## When to leave it alone

Not every document wants a heading tree. Keep it flat when:

- **It's short: a few paragraphs on one topic.** Headings over three
  paragraphs add navigation nobody needs and break the flow.
- **It's a single linear argument or narrative**: a chain where each
  paragraph depends on the last. Chopping it into sections implies an
  independence the prose doesn't have.
- **It's a chat message, a commit body or a one-screen note**: formats read
  top to bottom in one pass, where a heading is overhead.
- **The "sections" would each be one sentence**: those are list items or
  just prose, not sections.

When in doubt: _would a reader ever want to jump straight to one part?_ If
yes, that part is a section. If the document is only ever read start to
finish, it doesn't need headings.

## How to do it

1. **Find the seams.** Mark every place the topic changes: the "now…",
   "separately…", "another thing…" transitions. Each genuine shift is a
   candidate section boundary.
2. **Assign levels by hierarchy, not by size.** One top-level heading is the
   document's title. Major topics are the next level down; a topic's own
   sub-points are the level below that. The level encodes containment (a
   child heading is part of its parent's topic), not how long the section
   is.
3. **Don't skip levels.** Go from a section straight to its sub-section,
   never from a section to a sub-sub-section. A skipped level breaks the
   outline and most table-of-contents generators.
4. **Write headings that scan.** Front-load the keyword ("Authentication",
   not "How we handle authentication"), keep them short, make siblings
   grammatically parallel (all noun phrases, or all "Verb the thing"), and
   don't end them with a period: a heading is a label, not a sentence.
5. **Promote pseudo-headings.** Turn a standalone bold label that introduces
   a block into a real heading, so it joins the outline and gets a linkable
   anchor.
6. **Check the balance.** If one section dwarfs all others, it probably
   hides sub-sections. If a section is one sentence, it probably isn't a
   section.

### Before

Shown in Markdown; the shape is the same in any format.

```markdown
# Widget CLI

The widget CLI builds and ships widgets. To install it, run `npm i -g widget`,
or on macOS `brew install widget`; the brew formula also pulls the shell
completions. Once installed, configure it by setting WIDGET_TOKEN in your env
and optionally WIDGET_REGION, which defaults to us-east. To build a widget run
`widget build`, which reads widget.toml; to ship one run `widget ship`, which
needs a configured token.
```

### After

```markdown
# Widget CLI

The widget CLI builds and ships widgets.

## Installation

- npm: `npm i -g widget`
- macOS: `brew install widget` (also pulls shell completions)

## Configuration

Set `WIDGET_TOKEN` in your env. `WIDGET_REGION` is optional and defaults to
`us-east`.

## Usage

- `widget build`: reads `widget.toml`.
- `widget ship`: requires a configured token.
```

One run-on paragraph carried three distinct topics: install, configure, use.
Putting each under its own section heading turns the headings into a table
of contents the reader skims first; nothing in the prose was added or
dropped.

## Faithfulness rules: don't let the structure lie

- **Headings describe their section, accurately.** A heading is a promise
  about what's beneath it; don't label a section "Security" if it's really
  about logging.
- **Don't use a heading for emphasis.** A bigger font to make a line stand
  out misuses the outline; use bold or a callout, and reserve heading levels
  for actual hierarchy.
- **One title per document.** Several top-level headings flatten the
  hierarchy and confuse table-of-contents tools; demote extra top-level
  topics to sections.
- **Keep nesting shallow.** Past three or four levels the hierarchy is
  usually too fine: flatten it or split the document. Deep nesting is as
  hard to skim as none.
- **Don't invent sections the content doesn't have.** Headings follow the
  document's real topic seams; imposing a template (Overview / Details /
  Notes) on prose that doesn't divide that way creates empty or mislabeled
  sections.

## Quick heuristic

> Collapse the document to its headings and read only those. If they form a
> sensible outline, a table of contents you could navigate by, the hierarchy
> is right. If the headings don't tell you what's in the document, or there
> are none to read, the shape needs work.

## When to apply

- Writing or editing a document longer than a screen that covers more than
  one topic: docs, READMEs, design docs, RFCs, long PR descriptions, release
  notes, reports.
- Reviewing a document whose sections are marked only by bold lines or by
  "now, on…" transitions.
- The user asks to add headings, outline a document or make it skimmable.

## Related skills

When one of these applies and it's in your skill listing, load it
without asking. If it isn't in your listing, tell the user which skill is
missing and ask whether to install it from the same collection this skill
came from; don't apply it from memory.

- `markdown-hygiene-lists-headings-tables`: Markdown syntax for headings: `#` levels, ATX style, anchors.
- `writing-hygiene-prose-to-lists`: when a "section" is really one sentence, a list item instead of a heading.
