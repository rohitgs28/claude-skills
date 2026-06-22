---
name: code-reviewer
description: >-
  Review code changes the way a thoughtful senior engineer would: find real
  bugs, security issues, and design problems, and report them grouped by
  severity with concrete fixes. Use this whenever the user asks to "review",
  "look over", "check", or "give feedback on" code, a diff, a pull request, or a
  branch; asks "is this correct/safe?"; pastes a function and asks what's wrong;
  or wants a PR reviewed before merging — even if they don't say the word
  "review".
---

# Code Reviewer

A good review changes the outcome: it catches the bug before production and
teaches something in the process. A bad review lists nitpicks and misses the
real problem. Aim for the former.

## What to actually look for

Review in roughly this priority order, because a missed correctness bug costs
far more than a missed style preference:

1. **Correctness** — Does it do what it claims? Edge cases (empty input, nulls,
   large input, concurrency, unicode), off-by-one errors, incorrect conditions,
   wrong error handling, resource leaks.
2. **Security** — Injection (SQL, shell, template), missing authz/authn checks,
   secrets in code, unsafe deserialization, path traversal, unvalidated input
   crossing a trust boundary.
3. **Design & maintainability** — Is the abstraction right? Duplicated logic,
   leaky boundaries, functions doing too much, names that mislead, hidden
   coupling. Will the next person understand it?
4. **Tests** — Are the risky paths covered? Do the tests actually assert
   behavior, or just run the code?
5. **Style & polish** — Only after the above. Formatting, naming conventions,
   docs. Keep this brief; linters handle most of it.

## How to obtain the diff

If the user gave you a diff or file, review that. If they point at a branch or
PR, get the actual changes first (e.g. `git diff main...HEAD`) and review the
diff, but read enough surrounding code to understand context — a change can be
wrong because of code it *doesn't* touch.

## Output format

Lead with a one-line verdict, then group findings by severity. Each finding
names the location, explains the problem and *why it matters*, and gives a
concrete fix.

```
**Verdict:** <Approve / Approve with comments / Request changes> — <one line>

### Blocking
- `path/to/file.py:42` — <problem>. <why it matters>. Suggested fix: <fix>.

### Should fix
- ...

### Nits (optional)
- ...

### What's good
- <call out genuinely solid choices — reviews shouldn't be only negative>
```

## Guardrails

- Be specific. "This could be cleaner" is useless; show the cleaner version.
- Explain the why behind each comment so the author learns, not just complies.
- Distinguish must-fix from preference. Don't block a PR over taste.
- Praise good decisions honestly — it builds trust and signals what to repeat.
- If you're unsure whether something is a bug, say so and explain how to check, rather than asserting.

## Example

**Verdict:** Request changes — solid structure, but one SQL injection and an
unhandled empty-list case.

### Blocking
- `api/search.py:88` — query is built with f-string interpolation of `term`,
  which is user-controlled — SQL injection. It matters because any caller can
  read or drop tables. Fix: use a parameterized query (`cur.execute(sql, (term,))`).
