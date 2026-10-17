---
name: writing-hygiene-prose-to-lists
description: |
  Rewrite run-on sentences that pile clauses behind commas, semicolons and
  "and"/"or" as nested lists when the prose is really an enumeration, a
  hierarchy or a set of parallel options. Covers how to tell a list in
  disguise from genuine prose, how to map comma, semicolon and colon
  structure onto list nesting, when not to convert (narrative, a short pair,
  a short sequence that reads fine inline, a one-line summary), and how to
  keep the rewrite faithful (no dropped items, no invented hierarchy). Any
  format: docs, READMEs, PR descriptions, commit bodies, release notes,
  reports, replies. Use when a sentence enumerates three or more items,
  hides sub-items behind its commas or strings parallel clauses together, or
  when the user asks to "condense", "clean up", "make this scannable",
  "break up this wall of text" or "use lists here".
tags: [writing, structure]
---

# writing-hygiene-prose-to-lists

A run-on sentence that enumerates things is a list wearing prose clothing.
Commas, semicolons and a trailing "and" do the job that list items and
indentation do better: making each item visible, countable and skimmable.
This skill spots those sentences and rewrites them as nested lists, **where
appropriate**, which is the load-bearing qualifier.

It covers when and why to make a list, in any format. The syntax of a list
in a given format (Markdown indentation, line breaks inside an item) is in
`markdown-hygiene-lists-headings-tables`.

## How to load this skill

Passive reference. Loading it doesn't mean the user wants a document
rewritten now; it means that when you write or edit prose, you'll notice
the lists hiding in it.

## When this applies

Convert to a nested list when a sentence, or a chain of them, is
structurally an enumeration:

- **Three or more parallel items** strung behind commas: "Covers input
  pinning, input ordering, the `@inputs` convention, `inherit` vs `with`,
  and formatting."
- **Items that carry their own sub-detail**: a comma clause with a
  parenthetical or a "such as" tail. That sub-detail wants a child item, not
  burial mid-line.
- **A colon followed by a comma series**: "It exposes three apps: install,
  which writes the symlink; uninstall, which removes it; and reap, which
  sweeps broken entries." The colon announces a list out loud.
- **Parallel options or cases** joined by "or" / "either … or": each
  alternative is a sibling item.
- **A sentence you re-read to count the items.** If you can't tell at a
  glance whether there are four or five, neither can the reader.

## When to leave it alone

Not every comma is a latent list item. Keep prose as prose when:

- **It's genuine narrative or argument**: cause and effect, contrast, a
  claim with its justification. "The build failed because the lock was
  stale, so we re-ran the update." A sentence, not a list.
- **There are only two items**: "Covers install and uninstall." A two-item
  list is usually noisier than the inline form.
- **The order is the point and reads fine inline**: a short sequence
  ("clone, build, run") belongs in prose or, if it must be a list, a
  numbered list, not an unordered one.
- **Breaking it up would orphan the connective tissue**: if clauses depend
  on each other grammatically (a shared subject mid-clause, a "which"
  modifying the whole preceding idea), splitting them strands fragments that
  no longer parse.
- **It's a single dense summary line** where one scannable sentence is the
  convention: a description field, a one-line title, a commit subject.

When in doubt: _are these items parallel and independently meaningful, or
one connected thought?_ Parallel and independent: list. Connected thought:
leave it.

## How to do the rewrite

1. **Find the spine.** Identify the head clause (often everything before
   the first colon, or the verb governing the series). It becomes the
   lead-in line or the parent item.
2. **Split on the top-level separators.** Each top-level comma, semicolon,
   "and" or "or" becomes one sibling item. Watch for nested commas: a comma
   inside a parenthetical or a "such as X, Y" tail marks a child, not a
   sibling.
3. **Nest the sub-detail.** Move each item's qualifier, example or
   "(because …)" onto a child item. This is where two-level nesting earns
   its keep.
4. **Normalize to parallel grammar.** Make every sibling start the same way
   (all noun phrases, all imperative verbs, or all "X: does Y") so the list
   reads as one set.
5. **Keep the lead-in honest.** End the lead-in with a colon when it
   introduces the list; don't when the items complete the sentence
   grammatically. Mixing the two is the most common slip.

### Before

```text
The installer supports several scopes: personal, which writes to the home
directory's skills folder and is the default for a single user; project,
which writes to the repo's skills folder so the skill is committed alongside
the code; and custom, which takes an explicit root path for anywhere else,
such as a temporary directory in a test.
```

### After

```text
The installer supports several scopes:

- personal: writes to the home directory's skills folder; the default for a
  single user.
- project: writes to the repo's skills folder, so the skill is committed
  alongside the code.
- custom: takes an explicit root path for anywhere else.
  - For example, a temporary directory in a test.
```

The colon-introduced series became three sibling items; the "such as" tail,
a comma nested inside the third item, became its child, not a fourth
sibling. Nothing was dropped, and no hierarchy was invented beyond what the
prose implied.

## Faithfulness rules: don't let the rewrite lie

- **Conserve items.** The list contains exactly the items the sentence did:
  no merging two into one, no silently dropping the awkward last clause.
- **Don't invent nesting.** Nest only when the prose actually subordinated
  something (a parenthetical, "such as", "because"). Turning siblings into a
  fake hierarchy misrepresents the content.
- **Don't promote nesting away.** A genuinely subordinate clause stays a
  child; pulling it up to a sibling implies a parallelism that wasn't there.
- **Preserve ordered-ness.** If the original order encoded sequence or
  priority, use a numbered list; if order was incidental, an unordered list
  is fine.
- **Keep the words.** Condensing structure is not rewriting voice. Trim only
  the connectives the list makes redundant ("and", "which is", "such as");
  leave the substance verbatim where you can.

## Quick heuristic

> Read the sentence aloud. If you naturally pause and count ("one… two…
> three…"), it's a list. If you'd never list it on a whiteboard, it's prose.
> Convert the first; leave the second.

## When to apply

- Writing or editing any prose meant to be read by someone else: docs,
  READMEs, PR descriptions, commit bodies, release notes, status reports,
  replies.
- Reviewing text where a sentence enumerates three or more parallel items.
- The user asks to condense, clean up or make text scannable.

## Related skills

When one of these applies and it's in your skill listing, load it
without asking. If it isn't in your listing, tell the user which skill is
missing and ask whether to install it from the same collection this skill
came from; don't apply it from memory.

- `markdown-hygiene-lists-headings-tables`: Markdown syntax for lists: nesting indents, numbered lists, hard line breaks inside an item.
- `writing-hygiene-tables-for-comparison`: when the items all share the same properties, a table instead of a list.
