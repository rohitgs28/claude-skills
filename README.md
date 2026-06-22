# Claude Skills — Engineering & Product

A small, opinionated collection of **generic [Agent Skills](https://agentskills.io)**
for everyday software engineering and product work. Each skill is a focused,
reusable instruction set that teaches Claude to do one job well — reviewing a
diff, writing a PRD, polishing a repo — the same way every time.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-6-blue.svg)](#whats-inside)
[![Agent Skills spec](https://img.shields.io/badge/spec-agentskills.io-black.svg)](https://agentskills.io/specification)

## What's inside

### Software engineering

| Skill | What it does |
|-------|--------------|
| [`repo-polisher`](skills/repo-polisher) | Audit and modernize a repo: fix real bugs, upgrade legacy code, add scaffolding (deps, `.gitignore`, tests, CI), and write a polished README. |
| [`code-reviewer`](skills/code-reviewer) | Review a diff/PR like a senior engineer — correctness, security, design — reported by severity with concrete fixes. |
| [`test-author`](skills/test-author) | Write meaningful tests that assert real behavior and cover the risky paths, not coverage filler. |
| [`commit-and-pr`](skills/commit-and-pr) | Write clear Conventional-Commit messages and reviewer-friendly PR descriptions from a diff. |

### Product

| Skill | What it does |
|-------|--------------|
| [`prd-writer`](skills/prd-writer) | Turn a feature idea into a crisp, decision-ready Product Requirements Document. |
| [`user-stories`](skills/user-stories) | Break a feature/PRD into INVEST user stories with Given/When/Then acceptance criteria, and prioritize with RICE/MoSCoW. |

## Install

### Claude Code (as a plugin marketplace)

```
/plugin marketplace add rohitgs28/claude-skills
```

Then install a bundle:

```
/plugin install software-engineering-skills@rohitgs28-skills
/plugin install product-skills@rohitgs28-skills
```

Once installed, just describe your task — Claude picks the right skill. For
example: *"review the diff on my current branch"* or *"write a PRD for CSV export."*

### Claude.ai / API

Each skill is a self-contained folder under [`skills/`](skills). Upload an
individual skill (the folder containing its `SKILL.md`) following
[Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude),
or reference the [Skills API guide](https://docs.claude.com/en/api/skills-guide).

## How a skill is structured

```
skills/<name>/
├── SKILL.md        # YAML frontmatter (name, description) + instructions
├── references/     # docs loaded only when needed (optional)
└── assets/         # templates used in output (optional)
```

The `description` field is what triggers the skill, so it states both *what the
skill does* and *when to use it*. See [`CLAUDE.md`](CLAUDE.md) for the
conventions used in this repo and how to add a new skill.

## Contributing

New skills are welcome if they're generic and genuinely useful (not a thin
wrapper around one API). Follow the structure above and the conventions in
[`CLAUDE.md`](CLAUDE.md), then open a PR.

## License

[MIT](LICENSE) © Rohit Gollarahalli
