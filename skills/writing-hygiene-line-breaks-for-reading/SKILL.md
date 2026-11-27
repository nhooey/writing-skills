---
name: writing-hygiene-line-breaks-for-reading
description: >-
  Break lines in code and config for the reader, never to save lines; prose is out of scope. Never pack items (parameters, arguments, fields, list elements, conditions) several to a line to save lines or because the width allows it; a group that spans lines puts each item on its own line. Keep items on one line where that reads better: a short list of plain names, an aligned or stacked group, or a fixed-arity tuple such as a coordinate. A list literal in config or a manifest (Nix lists and attribute sets, JSON and TOML arrays, YAML sequences, Python, JavaScript and shell lists) puts each of two or more elements on its own line, so a diff and a merge work per item. Covers formatters: nixfmt enforces the list rule, prettier joins JSON, JavaScript and YAML flow lists that fit, and black and ruff keep a list expanded after a trailing comma. Use when writing or reviewing a parameter list, call, struct, condition or list literal in code, config, a manifest or a code example, or setting up a formatter.
tags: [writing, code]
---

# Line breaks for reading

_Break lines in code and config where they help the reader, never to save lines._
_Packing items onto a line can read well, when the items are short names, line up in columns or form one value; packing them only to save lines makes them hard to read._

This skill covers source code, config files, manifests and code examples.
Where to break lines in prose is out of its scope.

## When to apply

- Writing a parameter list, a call's arguments, a struct's or record's fields, a list literal or a compound condition.
- Writing a list, array or set literal in a config file, a manifest, or a code example in docs or a skill.
- Reviewing a diff that adds or edits one.
- Choosing or configuring a formatter for a project.

## The rule

1. **Never pack items to save lines.**
   Parameters, arguments, fields, list elements and conditions are items.
   Once a group spans more than one line, each item gets a line of its own, with the closing bracket on its own line.
2. **Never pack by width.**
   Several items to a line, broken where the line runs out, put the break at an arbitrary place and hide where one item ends and the next begins.
3. **Keep items on one line where that reads better:**
   - a short list of plain names, such as an enum's cases or a pattern's bindings, that reads as one phrase;
   - an aligned or stacked group, such as the rows of a matrix or a table of test cases, one row per line with its columns lined up;
   - a fixed-arity tuple, such as a coordinate `[x, y]`, a range's two ends or a version triple, whose positions have meanings and are not items.
4. **A list literal in config or a manifest is one element per line** once it has two or more elements, even when every element would fit on one line.
   One element stays on one line: `[ "a" ]`.

The test for a packed line is why it is packed.
If the answer is that it reads as one phrase, lines up with its neighbours or is one value, keep it.
If the answer is that it saves lines, split it.

## Packed to save lines

A Swift initializer with one parameter per line, except for three packed onto one line to save two lines:

```swift
init(
    id: UUID,
    key: String,
    series: String,
    firedWallNs: Int64? = nil, fireSeq: UInt64 = 0, fired: UInt64 = 0,
) {
```

The packed line hides the second and third parameters' names, types and defaults in the middle of a line, and an edit to one of them shows in a diff as a change to all three.
Split it:

```swift
init(
    id: UUID,
    key: String,
    series: String,
    firedWallNs: Int64? = nil,
    fireSeq: UInt64 = 0,
    fired: UInt64 = 0,
) {
```

## Packed because it reads better

A Swift `CodingKeys` enum whose cases are short plain names:

```swift
enum CodingKeys: String, CodingKey {
    case id, key, series, state, flags, suspects, held, evidence, fired
}
```

The line reads as one list of names, with nothing to tell apart but the names themselves.
Split one per line, it is no easier to read, only longer:

```swift
enum CodingKeys: String, CodingKey {
    case id
    case key
    case series
    case state
    case flags
    case suspects
    case held
    case evidence
    case fired
}
```

Keep the packed form.
Once the cases carry raw values, such as `case firedWallNs = "fired_wall_ns"`, each is an item with a part of its own, and goes on its own line.

## List literals in config and manifests

A list literal in a config file or a manifest puts each of its two or more elements on its own line, whatever their length.
Such a list is edited, sorted and merged one element at a time, so one element per line keeps a diff to one line per element added or removed, and lets a sort, a merge or a `git blame` work per element.

```nix
{
  inputs = [
    "nixpkgs"
    "flake-parts"
    "systems"
  ];
}
```

| Format         | One element per line                         |
| -------------- | -------------------------------------------- |
| Nix            | lists `[ … ]` and attribute sets `{ … }`     |
| JSON, JSON5    | arrays                                       |
| TOML           | arrays                                       |
| YAML           | block sequences (`- a`), never flow `[a, b]` |
| Python         | lists, sets, tuples of items                 |
| JavaScript, TS | arrays, and objects with more than one key   |
| Shell          | arrays, `( … )` with one word per line       |

A Nix function's argument pattern `{ a, b, ... }:` and an `inherit a b;` are short lists of plain names, not list literals, and stay on one line while they read as one.

## Working with formatters

A formatter that owns a file has the last word on its layout, since the project's format check fails on anything else.
Find out what it does with a list before relying on it:

- **nixfmt enforces the list rule.**
  It puts every list of two or more elements, and every attribute set with a binding, one per line, and keeps a single-element list on one line.
  In Nix, write the list either way and let nixfmt lay it out.
- **prettier undoes it** for JSON and JavaScript arrays and YAML flow sequences: it joins the elements onto one line whenever the literal fits the print width, and has no option to keep them apart.
  It does keep a JavaScript or JSON object expanded when there is a newline after its `{`, and keeps a YAML block sequence one item per line.
  Inside Markdown it formats `json`, `yaml` and `js` fences the same way, and leaves fences in languages it doesn't format, such as `nix` and `swift`, as written.
- **black and ruff format** keep a collection, a call or a signature one item per line when its last item has a trailing comma (the magic trailing comma), and join it otherwise.
  Write the trailing comma.

Under prettier:

- **YAML:** write block sequences, which prettier keeps.
- **A list where the layout matters,** such as one edited often: put `// prettier-ignore` on the line before the statement in JavaScript, TypeScript, JSONC or JSON5, `# prettier-ignore` before the key in YAML, and `<!-- prettier-ignore -->` before a fence in Markdown.
- **A plain `.json` file,** which can't hold a comment: accept prettier's layout, or leave the file out of prettier's includes in the treefmt config.

A formatter that keeps whatever layout it is given, such as gofmt for composite literals, leaves the rule to the writer.

## Checking it holds

- Run the project's formatter, then look for a line holding several items of a group that spans more than one line, and for a config or manifest list literal of two or more elements still on one line, in a file the formatter doesn't reflow.
- In review, ask why each packed line is packed: one packed to save lines, in a file no formatter owns, is a finding; one a formatter produced points at the formatter setup above.

## Related skills

When one of these applies and it's in your skill listing, load it
without asking. If it isn't in your listing, tell the user which skill is
missing and ask whether to install it from the same collection this skill
came from; don't apply it from memory.

- `writing-hygiene-prose-to-lists`: the same one-item-per-line choice in prose, where an inline run of parallel items becomes a list.
- `nix-flakes`: setting up treefmt and its formatters in a flake.
