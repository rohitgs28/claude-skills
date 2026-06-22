---
name: repo-polisher
description: >-
  Audit and modernize a code repository end to end: fix real bugs, upgrade
  legacy language/runtime usage, add missing project scaffolding (dependency
  manifest, .gitignore, tests, CI), and write a polished README. Use this
  whenever the user wants to "clean up", "modernize", "polish", "improve",
  "refactor", or "open-source" a repo or project, asks to make a project
  "look professional" or "presentable" for recruiters/portfolios, points at an
  old or messy codebase, or shares a GitHub repo and wants it improved — even
  if they don't say the word "polish".
---

# Repo Polisher

Take a rough, dated, or undocumented repository and turn it into something a
maintainer would be proud to publish. The goal is a repo that a stranger can
understand in two minutes and run in five.

Work in this order. Each phase builds on the last, and doing them out of order
(e.g. rewriting the README before you understand the code) produces shallow,
inaccurate results.

## 1. Understand before you touch anything

Read the actual code, not just the file names. Identify the language(s), the
entry points, how the project is run, what it depends on, and what it is
actually trying to do. Note the state of the basics: is there a dependency
manifest, a README, tests, a license, a .gitignore? Skim the commit history if
it is available.

Do not start editing until you can state, in one sentence, what the project
does and how someone runs it. If you cannot, keep reading.

## 2. Find the real bugs

Surface-level tidying is not the value here — correctness is. Look for genuine
problems, not just style: code that wouldn't run on a current runtime,
hardcoded absolute paths, broken data loading, silent failures, off-by-one
logic, resource leaks, and incorrect assumptions about inputs. When you find a
bug, verify it (run the code or the relevant path) before claiming it, and
verify your fix after.

Be honest about severity. A misleading data pipeline that makes results wrong
matters far more than inconsistent quote style.

## 3. Modernize

Bring the code up to current, idiomatic practice for its language without
gold-plating. Typical moves: migrate off end-of-life language versions, replace
deprecated APIs, remove dead code, extract repeated logic, add type hints or
signatures where they aid clarity, and make configuration explicit instead of
hardcoded. Keep the diff focused — the point is a codebase the author can still
recognize, not a rewrite.

## 4. Add the missing scaffolding

A repo that can't be installed or trusted won't be used. Add whatever is
missing from the project's hygiene baseline:

- Dependency manifest (`requirements.txt`, `package.json`, `go.mod`, `Cargo.toml`, etc.)
- `.gitignore` appropriate to the stack
- A test or two that actually exercise the core path (even one meaningful test signals quality)
- A license, if the author wants one
- Basic CI (e.g. a GitHub Actions workflow that installs and runs tests) when it fits

See `references/checklist.md` for a per-language scaffolding checklist.

## 5. Write the README last

Now that the code is correct and runnable, write a README that reflects
reality. A strong README opens with a one-line description of what the project
does, then covers: why it exists, how to install it, how to run it (copy-paste
commands that actually work), and a short note on results or output where
relevant. Keep it honest — if the dataset is tiny or the model is a baseline,
say so. Overclaiming reads as junior.

## 6. Verify and summarize

Run the code and the tests one more time. Then tell the user what you changed
and *why*, grouped by impact (bugs fixed, then modernization, then scaffolding,
then docs) — they have to defend these changes, so give them the reasoning, not
just a file list.

## Guardrails

- Prefer the smallest change that achieves the goal. Resist rewriting working code for taste.
- Never invent results, benchmarks, or features in the README. Verify claims against the code.
- If you can't run the project in the environment, say so and reason carefully instead of guessing.
- Keep the original authors' intent and authorship intact unless asked otherwise.

## Example

Input: "Here's my old college project, can you make it look good for my GitHub?"
Output: A repo where the Python 2 script now runs on Python 3, a data-loading
bug that silently trained on the wrong column is fixed, a `requirements.txt`,
`.gitignore`, and one real test are added, and the README explains what it does,
how to run it, and honest accuracy numbers — plus a short changelog of what was
fixed and why.
