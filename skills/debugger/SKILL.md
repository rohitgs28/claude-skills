---
name: debugger
description: >-
  Systematically find the root cause of a bug instead of guessing at fixes:
  reproduce it, isolate it, form and test hypotheses, then verify the fix. Use
  this whenever the user is stuck on a bug, says something "doesn't work",
  "crashes", "throws an error", "returns the wrong result", "fails
  intermittently", pastes a stack trace or error message, or asks "why is this
  happening?" — even if they haven't used the word "debug".
---

# Debugger

Most time lost to bugs is lost to guessing — changing things at random and
hoping. The cure is a disciplined loop that narrows the search space until the
cause is cornered. Resist the urge to patch symptoms before you understand them.

## The loop

1. **Reproduce it reliably.** A bug you can't reproduce, you can't fix with
   confidence. Find the minimal, deterministic steps that trigger it. If it's
   intermittent, look for the hidden input that varies (timing, ordering, state,
   environment, data). A reliable repro is over half the battle.
2. **Read the actual evidence.** Read the full error and stack trace top to
   bottom — the real cause is often a few frames down, not the last line. Note
   exactly what's observed vs. what's expected.
3. **Isolate.** Shrink the surface: bisect the input, comment out halves,
   `git bisect` across commits, or add logging at the boundaries. The goal is to
   get from "somewhere in this system" to "this function, this line."
4. **Form one hypothesis at a time.** State a specific, falsifiable guess: "the
   list is empty because the filter runs before the data loads." Then design the
   cheapest test that would prove it true or false. Change one thing at a time —
   changing several hides which one mattered.
5. **Fix the cause, not the symptom.** Once confirmed, fix the underlying cause.
   A `try/except` that swallows the error is a symptom patch; ask why the error
   happened at all.
6. **Verify and guard.** Confirm the fix resolves the repro, check you didn't
   break neighbors, and add a regression test so the bug can't return silently.

## Useful techniques

- **Rubber-ducking**: explain the code line by line; the wrong assumption usually surfaces as you narrate.
- **Bisection** (input, code, or history) is the fastest way to localize.
- **Trust nothing, verify everything**: print/inspect actual values rather than assuming what they are. The bug lives in the gap between what you assume and what's true.
- **Check the boundaries**: nulls, empties, off-by-one, type coercion, timezones, encoding, concurrency.

## Guardrails

- Don't apply a fix you can't explain. "It works now" without knowing why means it'll break again.
- Don't change multiple things at once — you'll lose the signal.
- State your confidence. If you're inferring rather than confirming, say so and propose how to confirm.
- If you can't reproduce it, say that plainly and focus on getting a repro before proposing fixes.

## Example

Symptom: "API returns 500 intermittently under load."
Approach: reproduce with a concurrent request burst; read the trace to a
connection-pool-exhausted error; hypothesize connections aren't released on the
error path; confirm by logging pool checkouts; fix by using a context manager so
connections release on every path; verify with the same burst and add a test
that exercises the error path.
