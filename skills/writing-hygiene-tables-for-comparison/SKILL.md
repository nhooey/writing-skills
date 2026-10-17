---
name: writing-hygiene-tables-for-comparison
description: |
  Rewrite prose or lists as a table for one of two reasons: comparison or
  alignment. Comparison: several items described against the same
  properties ("X supports A, costs B; Y supports A', costs B'"), so the
  reader has to align them mentally to choose. Alignment: many parallel
  label-to-value rows (shortcuts, flags, environment variables, glossary
  entries) that scan better as columns than as bullets. Covers spotting the
  item-by-property grid, choosing the axes (items in rows, first column
  names the item), which properties earn a column (notable, shared, values
  differ), pulling uniform properties into a list under the table, when not
  to tabulate, and keeping the table faithful (every cell filled, no
  invented attributes). Any format: docs, READMEs, decision docs, "X vs Y"
  sections, PR descriptions, reports. Use when two or more items share the
  same dimensions, or when the user asks to "compare these", "tabulate
  this", "show the trade-offs", "which should I pick" or "make a reference
  table".
tags: [writing, structure]
---

# writing-hygiene-tables-for-comparison

When you describe several items and keep mentioning the _same_ attributes
for each, you've written a table in prose form. The reader has to align it
in their head, scanning paragraph three to find what paragraph one said
about cost. A table aligns it on the page: items down one axis, shared
properties across the other, every comparison a glance instead of a search.
A good comparison table lets a reader find the answer in seconds, because
it shows only what distinguishes the items.

This skill covers when to tabulate and what goes in the table, in any
format. Table syntax in a given format (Markdown pipes and alignment, line
breaks inside a cell, yes/no symbols, a linked first column) is in
`markdown-hygiene-lists-headings-tables`.

## How to load this skill

Passive reference. Loading it doesn't mean the user wants a table now; it
means that when you compare things in writing, you'll shape the comparison
as a table.

## When this applies

Convert to a table when the content is an **item × property grid**: two or
more items, each described against the same set of dimensions.

- **Repeated attributes across items**: every paragraph or bullet restates
  the same properties. "Postgres is relational, ACID-compliant,
  self-hosted; DynamoDB is key-value, eventually consistent, fully
  managed." The shared properties are columns; the items are rows.
- **The reader's question is "which one"**: the text supports a choice
  between alternatives. A decision over shared criteria is a table by
  nature.
- **A list where each item has the same sub-structure**: "Plan A: $10/mo, 5
  seats, no SSO" / "Plan B: $25/mo, 20 seats, SSO". The parallel sub-fields
  are columns waiting to happen.
- **You keep writing "whereas", "by contrast", "on the other hand"**: those
  connectives are manual cell alignment. A table makes the contrast
  positional, not verbal.

## Tables for alignment, not comparison

Even when nobody is choosing, a table lines a repeated **label → value**
structure into columns the eye tracks straight down. Reach for one when you
have **many parallel rows sharing the same two or three fields**, reference
material people scan for one row:

- Keyboard shortcuts: Key, Action.
- Command-line flags: Flag, Default, Meaning.
- Environment variables or config keys: Name, Value, Purpose.
- Glossary or field reference: Term, Definition; Field, Type, Notes.

A short set (two or three rows) is better as a list. The table earns its
borders once the set is long enough that aligned columns make a specific
row faster to find: a dozen shortcuts or every flag of a command.

## When to leave it alone

- **Only one item**: nothing to compare against. One thing's attributes are
  a list or prose.
- **The items share no common properties**: there are no columns to align,
  and the table is mostly empty cells.
- **Only one property and few rows**: a one-column table is a list with
  extra borders.
- **The cells would hold paragraphs**: tables are for short values (a word,
  a number, a yes/no, a clipped phrase). If each cell needs sentences, the
  comparison is genuinely prose.
- **The order is a sequence, not a comparison**: steps, a pipeline, a
  timeline. Those are numbered lists; the relationship is "then", not
  "versus".
- **It's a single dense summary line** where one sentence is the
  convention: a description field, a one-line title.

When in doubt: _am I measuring several items against the same yardsticks,
or describing things that happen to be near each other?_ Same yardsticks:
table. Incidental neighbors: leave it.

## What goes in a comparison table

### Items in rows; the first column names the item

Each item is one row, and its first cell is the item's name. Rows let the
eye scan one property down a single column ("which ones are wireless?");
items as columns force a slower read-the-label-then-jump-across pattern.
When the item has an address (an official site, its docs, a repository),
the name links to it, so the canonical page is one click away instead of a
search.

Flip to items as columns only as a deliberate exception: two or three items
against many properties (six or more, or twenty dimensions for two items),
where a two-row table would be forced into ten columns that wrap off the
screen.

### Include the columns readers expect

Each category has properties a reader looks for first: products have price,
license, platforms and use case; libraries have language, license,
maintenance and size; services have free tier, hosting model and pricing;
physical goods have dimensions, weight, materials and warranty. Aim for four
to eight load-bearing columns. Three informative columns beat ten weak ones.

### A column per notable, shared, differing property

A property earns a column when all three hold:

- **Notable**: readers care about it for this category.
- **Shared by at least half the items**: a real axis, not a one-off
  feature.
- **Values differ**: the column actually separates the items.

A property relevant to only one or two items belongs in prose or a note
under the table; a column of mostly "N/A" cells wastes space.

### Pull uniform properties into a list under the table

A property with the same value for every item can't help the reader choose.
Move it to a short list directly below the table ("Shared by all three: …").
This includes yes/no columns that are yes for every item. Do the same for
properties every item lacks ("None of these: …"). Every column left in the
table is then load-bearing, and the fact is still stated.

### One main table

Resist splitting one comparison into many small tables: a 4-item, 7-column
table reads better than three 4-item, 3-column ones stacked up. Split only
when the dimensions are genuinely orthogonal, such as a pricing-tier table
beside a feature table. Nuances that don't fit a cell (history,
version-specific behavior, caveats) go in prose or notes beneath it.

## How to do the rewrite

1. **Identify the items.** These become the rows.
2. **Extract the shared properties.** Collect every attribute that appears
   for more than one item, then keep the ones that pass the column test
   above. Uniform ones go to the list under the table.
3. **Fill the grid.** For each item and property, take the value from the
   source. If the source doesn't say, write an explicit "—" or "N/A"; never
   leave a cell blank and never invent a value.
4. **Clip cells to scannable values.** A number, a word, a yes/no, a short
   phrase. Push real explanation into a qualifier under the value or a note
   beneath the table.
5. **Normalize phrasing down each column.** Same units, same yes/no
   convention, same grammatical form, so the column reads as one axis
   ("$10/mo" in every row, not "ten dollars a month" in the next).
6. **Order rows and columns meaningfully.** Put the decision-driving
   property in an early column; order rows by what the reader cares about
   (price, default first, recommended first), not by accident of the source.

### Before

```text
Bitwarden is GPL-3.0, can be self-hosted with its official Docker image,
has browser extensions for Chrome, Firefox, Safari and Edge, offers a
family plan at $40/yr for 6 users, runs on Linux, macOS and Windows, and
generates TOTP codes. 1Password is proprietary and can't be self-hosted,
but it also has extensions for the same four browsers and a family plan,
$60/yr for 5 users; it too runs on all three desktop systems and generates
TOTP codes. KeePassXC, by contrast, is GPL-2.0+ and keeps a local-file
database, reaches browsers only through a plugin and a bridge, is a
single-user app with no family plan, and likewise runs on Linux, macOS and
Windows and generates TOTP codes.
```

### After

Shown in Markdown; the content rules are the same in any format.

```markdown
| Manager                             | License     | Self-hostable                | Browser extensions                   | Family plan            |
| ----------------------------------- | ----------- | ---------------------------- | ------------------------------------ | ---------------------- |
| [Bitwarden](https://bitwarden.com/) | GPL-3.0     | ✅<br/>Official Docker image | ✅<br/>Chrome, Firefox, Safari, Edge | ✅<br/>$40/yr for 6    |
| [1Password](https://1password.com/) | Proprietary | ❌                           | ✅<br/>Chrome, Firefox, Safari, Edge | ✅<br/>$60/yr for 5    |
| [KeePassXC](https://keepassxc.org/) | GPL-2.0+    | ✅<br/>Local-file database   | ❌<br/>Via plugin and bridge         | ❌<br/>Single-user app |

Shared by all three: Linux, macOS and Windows desktop apps; TOTP code
generation.
```

Three paragraphs that each restated the same properties became one grid
with the items in rows, named in the first column. The desktop platforms
and TOTP support were the same for every item, so they moved to the line
under the table, leaving only columns that separate the items. "By
contrast" disappeared because the contrast is positional. Nothing was
dropped and nothing invented.

## Faithfulness rules: don't let the table lie

- **Fill every cell.** A blank cell is ambiguous: "no", "same as above" or
  "unknown"? Use an explicit value, "—" or "N/A".
- **Don't invent attributes.** Tabulate only properties the source stated.
  An empty-looking grid tempts you to fill cells with plausible guesses;
  that fabricates comparisons the source never made.
- **Don't drop the awkward item.** Every source item gets a row, even one
  that doesn't fit the columns cleanly.
- **Keep the values, clip the prose.** Shorten phrasing to fit a cell, but
  the number, the yes/no and the named option must match the source
  exactly.
- **Preserve qualifiers that change meaning.** "Eventually consistent _by
  default_" is not "eventually consistent": keep a load-bearing hedge in the
  cell or a note.
- **Don't bury detail the table can't hold.** A crucial caveat that won't
  fit a cell goes in a note beneath the table, not a paragraph crammed into
  one cell.

## Quick heuristic

> Picture the content as a spreadsheet. If you can name the column headers
> and every row has a value (even "N/A") under each, it's a table. If the
> "columns" differ per item or every cell wants a paragraph, it's prose.
> Tabulate the first; leave the second.

## When to apply

- Writing or editing anything that compares two or more concrete things
  (products, libraries, services, tools, plans, options) for a reader
  deciding between them: decision docs, "alternatives" sections, "X vs Y"
  sections, buyer's guides, PR descriptions, reports.
- Writing reference material with many parallel label-to-value rows.
- The user asks to compare, tabulate or show trade-offs.

## Related skills

When one of these applies and it's in your skill listing, load it
without asking. If it isn't in your listing, tell the user which skill is
missing and ask whether to install it from the same collection this skill
came from; don't apply it from memory.

- `markdown-hygiene-lists-headings-tables`: Markdown syntax for tables: pipes and alignment, `<br/>` inside cells, ✅/❌ cells, a hyperlinked first column.
- `writing-hygiene-prose-to-lists`: when the items don't share properties, or there is only one property and few rows, a list instead of a table.
- `writing-hygiene-refer-by-canonical-label`: naming each item by its canonical label and linking it.
