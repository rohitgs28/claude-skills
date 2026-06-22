---
name: commit-and-pr
description: >-
  Write clear commit messages and pull-request descriptions that explain what
  changed and why. Use this whenever the user asks to "write a commit message",
  "commit this", "write a PR description", "open a PR", "summarize my changes",
  or needs a changelog entry or release note from a diff — even if they just
  staged changes and ask "what should the message be?"
---

# Commit & PR

Commit messages and PR descriptions are read far more often than they're
written — by reviewers, by future debuggers running `git blame`, by you in six
months. Optimize for the reader who has no context.

## Commit messages

Follow the Conventional Commits convention by default (see
`references/conventional-commits.md` for the full type list and rules):

```
<type>(<optional scope>): <imperative summary, <=72 chars>

<body: what changed and WHY, wrapped ~72 cols. Explain the motivation and
context, not just the diff — the diff already shows what changed.>

<optional footer: BREAKING CHANGE:, issue refs like "Closes #123">
```

Rules that matter:

- **Summary in the imperative mood**: "add retry logic", not "added" or "adds".
- **Explain why, not what.** "Fix race condition in cache eviction" beats
  "change mutex to RWMutex" — the reader can see the code, but not your reasoning.
- **One logical change per commit.** If the summary needs "and", consider splitting.
- Reference issues in the footer (`Closes #123`).
- Inspect the actual staged diff before writing — never guess at what changed.

## Pull-request descriptions

Use this structure; trim sections that don't apply:

```
## What
<one or two sentences on the change>

## Why
<the problem or motivation — link the issue>

## How
<key implementation decisions a reviewer should know; call out anything subtle or risky>

## Testing
<how it was verified — tests added, manual steps, edge cases checked>

## Notes
<screenshots, follow-ups, breaking changes, deployment steps>
```

A reviewer should be able to read the description and know what to look for
before reading a single line of the diff.

## Guardrails

- Never fabricate. Base the message strictly on the actual diff; if you can't see it, ask for it.
- Do not attribute the work to anyone but the author, and don't add co-author or tool trailers unless the user asks.
- Keep summaries tight; put detail in the body, not a 100-character title.
- Match the repo's existing convention if it clearly differs from Conventional Commits.

## Example

Staged diff: switched an image-classification data loader to parse a CSV column
instead of the whole row, and balanced the classes.

```
fix(data): parse moment text from CSV and balance classes

The not-depressed corpus is HappyDB CSV; the loader was feeding entire rows
(IDs, timestamps, category tags) into the model, so it learned dataset
artifacts instead of language. Parse only the cleaned-text column and
down-sample the majority class so predictions aren't biased.

Accuracy on the held-out split rises from ~0.70 to ~0.87.
```
