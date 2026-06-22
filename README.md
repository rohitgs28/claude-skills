# Claude Skills — Engineering & Product

A small, opinionated collection of **generic [Agent Skills](https://agentskills.io)**
for everyday software engineering and product work. Each skill is a focused,
reusable instruction set that teaches Claude to do one job well — reviewing a
diff, writing a PRD, polishing a repo — the same way every time.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/rohitgs28/claude-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/rohitgs28/claude-skills/actions/workflows/ci.yml)
[![Skills](https://img.shields.io/badge/skills-10-blue.svg)](#whats-inside)
[![Agent Skills spec](https://img.shields.io/badge/spec-agentskills.io-black.svg)](https://agentskills.io/specification)

## What's inside

### Software engineering

| Skill | What it does |
|-------|--------------|
| [`repo-polisher`](skills/repo-polisher) | Audit and modernize a repo: fix real bugs, upgrade legacy code, add scaffolding (deps, `.gitignore`, tests, CI), and write a polished README. |
| [`code-reviewer`](skills/code-reviewer) | Review a diff/PR like a senior engineer — correctness, security, design — reported by severity with concrete fixes. |
| [`test-author`](skills/test-author) | Write meaningful tests that assert real behavior and cover the risky paths, not coverage filler. |
| [`commit-and-pr`](skills/commit-and-pr) | Write clear Conventional-Commit messages and reviewer-friendly PR descriptions from a diff. |
| [`debugger`](skills/debugger) | Find a bug's root cause systematically — reproduce, isolate, hypothesize, verify — instead of guessing at fixes. |
| [`tech-design-doc`](skills/tech-design-doc) | Write an RFC / design doc: context, goals, proposed design, alternatives considered, and risks. |
| [`security-review`](skills/security-review) | Review code/diffs for vulnerabilities (injection, authz, secrets, SSRF) with severity-ranked, actionable findings. |

### Product

| Skill | What it does |
|-------|--------------|
| [`prd-writer`](skills/prd-writer) | Turn a feature idea into a crisp, decision-ready Product Requirements Document. |
| [`user-stories`](skills/user-stories) | Break a feature/PRD into INVEST user stories with Given/When/Then acceptance criteria, and prioritize with RICE/MoSCoW. |
| [`competitive-analysis`](skills/competitive-analysis) | Compare competitors across buyer-relevant dimensions in a matrix and draw out positioning, gaps, and recommendations. |

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

## Development

The marketplace and every skill's frontmatter are validated in CI on each push and PR:

```bash
python scripts/validate.py
```

## Contributing

New skills are welcome if they're generic and genuinely useful (not a thin
wrapper around one API). Follow the structure above and the conventions in
[`CLAUDE.md`](CLAUDE.md), then open a PR.

## License

[MIT](LICENSE) © Rohit Gollarahalli
