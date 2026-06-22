---
name: test-author
description: >-
  Write meaningful automated tests for existing code — tests that assert real
  behavior and cover the risky paths, not filler that only inflates coverage.
  Use this whenever the user asks to "write tests", "add unit tests", "add test
  coverage", "test this function/module", set up a test suite, or asks "how do I
  test this?"; or when they've just written code and want it covered — even if
  they don't name a test framework.
---

# Test Author

Tests exist to catch regressions and document intended behavior. A test that
can't fail is worse than no test, because it gives false confidence. Write
tests that would actually break if the code broke.

## Process

1. **Understand the contract.** Read the code under test and determine what it
   promises: inputs, outputs, side effects, error conditions. Test the contract,
   not the implementation details — tests coupled to internals break on every
   refactor.
2. **Pick the framework the project already uses.** Match the existing
   convention (pytest, jest/vitest, go test, cargo test, JUnit, etc.) and file
   layout. Don't introduce a new framework unless asked.
3. **Cover the cases that matter**, in priority order:
   - The happy path (the main thing it's supposed to do)
   - Boundaries and edges: empty, zero, one, many, max, null/None, negative, unicode
   - Error paths: invalid input, failures, exceptions — assert they're handled as promised
   - Known-tricky logic surfaced by reading the code
4. **Make each test independent and deterministic.** No shared mutable state, no
   reliance on test order, no real network/clock/filesystem unless that's the
   point — inject or mock those. A flaky test erodes trust in the whole suite.
5. **Run the tests.** Confirm they pass against correct code. Where practical,
   sanity-check that a test fails if you break the code — that's how you know it
   has teeth.

## What makes a test good

- **Named for behavior**, not mechanics: `test_rejects_expired_token`, not `test_func2`.
- **Arrange–Act–Assert** structure, one logical behavior per test.
- **Asserts outcomes**, not just "it ran without throwing".
- **Readable as documentation** — someone should learn how the code behaves by reading the tests.

## Guardrails

- Don't chase 100% coverage with trivial tests. Coverage is a means, not the goal.
- Don't assert on incidental details (log strings, exact float equality, dict ordering) that will break spuriously.
- If the code is hard to test, that's a design signal — say so and suggest the seam (dependency injection, pure function extraction) rather than writing a tortured test.
- Prefer a few sharp tests over many shallow ones.

## Example

Input: "Write tests for this `parse_duration('1h30m')` helper."
Output: pytest cases covering a normal value (`1h30m` → 5400s), units alone
(`45m`, `2h`), zero, missing units, garbage input (asserts it raises
`ValueError`), and whitespace — each named for the behavior it pins down, all
passing, with one deliberately checked to fail if the parser regresses.
