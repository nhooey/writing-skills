# writing-skills

Agent skills for what to say and how to structure it, for any author, in
any format, packaged as a Nix flake.

Most writing that's hard to read isn't wrong, it's shaped wrong: an
enumeration buried in a run-on sentence, a long document with no outline, a
comparison the reader has to line up in their head, a reference that sends
them off to look up `#206`. Each skill here names one of those shapes, when
to fix it, when to leave it alone and how to keep the rewrite faithful.

These skills cover the reasoning and apply to any format. The syntax of a
given format, such as Markdown list indents, heading levels and table pipes,
lives in separate format skills such as
`markdown-hygiene-lists-headings-tables`.

Each skill is a self-contained directory under [`skills/`](skills/) with a
`SKILL.md` that an agent loads on demand. Skills are built by
[`agent-skill-flake`](https://github.com/nhooey/agent-skill-flake).

## Skills

| Skill                                                                                                  | What it does                                                                                                         |
| ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| [`writing-hygiene-prose-to-lists`](skills/writing-hygiene-prose-to-lists/SKILL.md)                     | Rewrite run-on sentences that are really enumerations as nested lists, faithfully; leave real narrative alone.       |
| [`writing-hygiene-headings-as-outline`](skills/writing-hygiene-headings-as-outline/SKILL.md)           | Give a long, multi-topic document a heading hierarchy that reads as its outline.                                     |
| [`writing-hygiene-tables-for-comparison`](skills/writing-hygiene-tables-for-comparison/SKILL.md)       | Lift items described against the same properties into a table: items in rows, only differing properties as columns.  |
| [`writing-hygiene-refer-by-canonical-label`](skills/writing-hygiene-refer-by-canonical-label/SKILL.md) | Refer to each issue, commit, file or event by one canonical label, linked, with identifiers in parentheses after it. |

## Install

```bash
# Preview what installing every skill would change, without writing anything
nix run github:nhooey/writing-skills#preview

# Install all skills into the agent's skill directory
nix run github:nhooey/writing-skills#install
```

Package outputs:

- `agent-skills-nhooey-writing-all` — the aggregate of every skill (also `default`)
- `agent-skill-nhooey-writing-hygiene-prose-to-lists`
- `agent-skill-nhooey-writing-hygiene-headings-as-outline`
- `agent-skill-nhooey-writing-hygiene-tables-for-comparison`
- `agent-skill-nhooey-writing-hygiene-refer-by-canonical-label`

## Development

```bash
nix develop      # enter the dev shell; run `menu` to list commands
nix fmt          # nixfmt over *.nix, prettier over *.md / *.yaml
nix flake check  # runs the treefmt check (fails on any unformatted file)
```
