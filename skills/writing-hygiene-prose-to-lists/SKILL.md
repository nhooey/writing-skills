---
name: writing-hygiene-prose-to-lists
description: Load before writing or editing any report, summary, GitHub issue or comment, PR description, commit body, message to another project, doc or reply that lists three or more things, or code that prints such text. Writes each inline run of parallel items as a flat or nested list, whatever joins its items, and leaves narrative as prose. Also for "condense", "make this scannable", "break up this wall of text" or "use lists here".
---

# Prose to lists

_An inline run of parallel items is a list written on one line, whatever joins the items._
_Rewrite it as a flat or nested list where it really is one, and leave genuine prose alone._

Whatever sits between the items, be it punctuation, a conjunction or a separator glyph, it does the job that list items and indentation do better: making each item visible, countable and skimmable.
The syntax of a list in a given format (Markdown indentation, line breaks inside an item) is in `markdown-hygiene-lists-headings-tables`.

## When this applies

Convert to a list when a sentence, a line or a chain of them is an inline run of parallel items: three or more items of the same kind, set side by side and told apart only by what sits between them.
The run is the pattern, not its separator.
A few of the shapes it takes:

- **Clauses in a sentence**: "Covers input pinning, input ordering, the `@inputs` convention, `inherit` vs `with`, and formatting."
- **Fields on a status line**: "build ✅ · tests ❌ 3 failing · lint ✅ · deploy skipped".
- **Pairs between slashes**: "Owner: platform / On call: Ana / Escalation: #infra-alerts / Runbook: docs/oncall.md".
- **Lines forced apart outside a table cell**: `Changed: README.md<br/>flake.nix<br/>skills/x/SKILL.md` in a paragraph of a generated report.
- **A legend line**: "Legend: ✅ passed, ❌ failed, ⏭ skipped, 🔄 retrying" above a table of results.

The run also hides structure that a list shows:

- **Items that carry their own sub-detail**: an item with a parenthetical or a "such as" tail.
  That sub-detail wants a child item, not burial mid-line.
- **A colon followed by a series**: "It exposes three apps: install, which writes the symlink; uninstall, which removes it; and reap, which sweeps broken entries."
  The colon announces a list out loud.
- **Parallel options or cases** joined by "or" / "either … or": each alternative is a sibling item.
- **A line you re-read to count the items.**
  If you can't tell at a glance whether there are four or five, neither can the reader.

Text a program writes counts as much as text a person writes: a script's Markdown report, a CLI's summary, a generated PR body.
There, fix the code that builds the line, so every run it prints comes out as a list.

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
- **It's a single dense summary line** where one scannable line is the convention: a description field, a one-line title, a commit subject, a status bar that must fit one row.
- **It's inside a table cell**, where Markdown allows no list: `<br/>` between the cell's lines is the right form there.

When in doubt: _are these items parallel and independently meaningful, or
one connected thought?_ Parallel and independent: list. Connected thought:
leave it.

## How to do the rewrite

1. **Find the spine.** Identify the head clause (often everything before
   the first colon, or the verb governing the series). It becomes the
   lead-in line or the parent item.
2. **Split on the top-level joins.** Each join at the top level of the run, whatever it is, becomes a boundary between sibling items.
   Watch for joins one level down: a comma inside a parenthetical or a "such as X, Y" tail marks a child, not a sibling.
   A character that belongs to an item, such as the slash in a path or the comma in a number, is no join at all.
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

> Read the line aloud.
> If you naturally pause and count ("one… two… three…"), it's a list.
> If you'd never list it on a whiteboard, it's prose.
> Convert the first; leave the second.

## When to apply

- Writing or editing any text meant to be read by someone else: docs, READMEs, PR descriptions, commit bodies, release notes, status reports, replies.
- Writing or reviewing code that generates text for a reader, such as a script that writes a Markdown report or a tool that prints a summary to the terminal.
- Reviewing text where a sentence or line strings three or more parallel items together.
- The user asks to condense, clean up or make text scannable.

## Your preferences

!`cat "${CLAUDE_SKILL_DIR}/../writing-hygiene-prose-to-lists.preferences.md" "${CLAUDE_PROJECT_DIR}/.agents/skills/writing-hygiene-prose-to-lists.preferences.md" 2>/dev/null || true`

If your agent doesn't run the line above, read these files yourself if they
exist: `writing-hygiene-prose-to-lists.preferences.md` next to this skill's folder, then
`.agents/skills/writing-hygiene-prose-to-lists.preferences.md` in the project. A project's
file overrides the user's, and the user's overrides this skill's defaults.

## Related skills

When one of these applies and it's in your skill listing, load it
without asking. If it isn't in your listing, tell the user which skill is
missing and ask whether to install it from the same collection this skill
came from; don't apply it from memory.

- `markdown-hygiene-lists-headings-tables`: Markdown syntax for lists: nesting indents, numbered lists, hard line breaks inside an item.
- `writing-hygiene-tables-for-comparison`: when the items all share the same properties, a table instead of a list.
- `writing-hygiene-group-by-reader-action`: when the list runs past a screen, its items sorted into groups by what the reader does with each.
- `coding-agent-skill-references`: the preferences files this skill reads.
