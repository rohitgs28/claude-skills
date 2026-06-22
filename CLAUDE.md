# CLAUDE.md

Guidance for Claude (and contributors) when working in this repository.

## What this repo is

A collection of generic Agent Skills for software engineering and product work.
Each skill lives in `skills/<name>/` and is self-contained. The repo doubles as
a Claude Code plugin marketplace via `.claude-plugin/marketplace.json`.

## Repository layout

```
.
├── .claude-plugin/marketplace.json   # marketplace + plugin/bundle definitions
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md                  # required: frontmatter + instructions
│       ├── references/               # optional: docs loaded on demand
│       └── assets/                   # optional: templates/files used in output
├── README.md
├── CLAUDE.md
└── LICENSE
```

## Conventions for SKILL.md

Every skill must follow these, because consistency is what makes the collection
trustworthy and the skills reliably triggerable:

1. **Frontmatter has exactly two required fields**: `name` and `description`.
   - `name` is lowercase with hyphens and matches the folder name.
   - `description` states both *what the skill does* and *when to use it*,
     including concrete trigger phrases. This field is the sole mechanism that
     decides whether the skill fires, so make it specific and slightly
     "pushy" — list the phrasings a real user would type, and note that it
     should fire even when they don't name the skill explicitly.
2. **Instructions use the imperative mood** and explain the *why*, not just the
   *what*. These models reason well; a rule with its rationale generalizes far
   better than a bare `ALWAYS`/`NEVER`.
3. **Keep SKILL.md focused** (aim < ~200 lines). Push long lookup material into
   `references/` and point to it from the body so it loads only when needed.
4. **Include a short, concrete example** showing the expected output shape.
5. **Add a Guardrails section** covering honesty (never fabricate results/data),
   scope, and failure modes.

## Adding a new skill

1. Create `skills/<name>/SKILL.md` following the conventions above.
2. Add supporting `references/` or `assets/` only if they earn their place.
3. Register the skill in `.claude-plugin/marketplace.json` under the right
   bundle (`software-engineering-skills` or `product-skills`), or add a new
   bundle if it's a new category.
4. Add a row to the table in `README.md`.
5. Validate before committing (see below).

## Quality bar

A skill belongs here only if it is **generic and genuinely useful** — something
people would reuse across many projects. A thin wrapper around a single API, or
something a person would just do themselves in one session, doesn't meet the
bar. Prefer a few excellent skills over many shallow ones.

## Validation

Before committing, confirm:

- `python -c "import json; json.load(open('.claude-plugin/marketplace.json'))"` parses.
- Every path listed in `marketplace.json` exists and contains a `SKILL.md`.
- Every `SKILL.md` has valid YAML frontmatter with `name` (matching its folder)
  and a `description`.
