---
name: user-stories
description: >-
  Turn a feature idea or PRD into well-formed user stories with clear acceptance
  criteria, and prioritize them (e.g. RICE or MoSCoW). Use this whenever the
  user wants to "write user stories", "break this into stories/tickets", "write
  acceptance criteria", "create a backlog", "groom the backlog", or prioritize
  features — even if they just describe a feature and ask "how would you break
  this down?"
---

# User Stories

User stories turn intent into buildable, testable units of work. A good story
is small, independent, and has acceptance criteria precise enough that everyone
agrees when it's done. A bad story is a vague title that spawns three meetings.

## Writing a story

Use the canonical form, then add acceptance criteria:

```
As a <type of user>, I want <capability> so that <benefit>.

Acceptance criteria (Given/When/Then):
- Given <context>, when <action>, then <observable outcome>.
- Given <edge case>, when <action>, then <expected handling>.
```

Apply the **INVEST** test — a good story is:
- **I**ndependent — can ship without depending on another story's internals
- **N**egotiable — describes the need, leaves room on the how
- **V**aluable — delivers visible value to a user or the business
- **E**stimable — the team can size it
- **S**mall — fits comfortably in a sprint; split if not
- **T**estable — acceptance criteria make "done" objective

## Splitting big stories

If a story is too large (an "epic"), split it along real seams, not arbitrarily:
by workflow step, by user type, by happy-path-then-edge-cases, by CRUD
operation, or by rules/variations. Each slice should still deliver value on its
own.

## Acceptance criteria that work

- Cover the happy path **and** the important edge/error cases.
- Be observable and objective — a tester or PM can verify each without asking the author.
- Avoid implementation detail; describe behavior, not the mechanism.

## Prioritization

When asked to prioritize, default to **RICE** and show the scoring so the
ranking is defensible:

```
RICE score = (Reach × Impact × Confidence) / Effort
```

- **Reach**: how many users/events per time period
- **Impact**: per-user effect (e.g. 3 = massive, 2 = high, 1 = medium, 0.5 = low)
- **Confidence**: how sure you are, as a % (100 / 80 / 50)
- **Effort**: person-weeks (or sprints)

Present results as a ranked table with the inputs visible. Use **MoSCoW**
(Must / Should / Could / Won't) instead when the user wants a lighter,
release-scoping view. State your assumptions for any numbers you estimate.

## Guardrails

- Don't fabricate reach/impact numbers as if they were real — label estimates and assumptions.
- Keep stories user-centric; "refactor the service" is a task, not a user story (track it, but don't dress it as one).
- Prefer a few well-formed stories over a long list of vague ones.

## Example

Input: "Break down 'let users reset their password' into stories."
Output: Stories for requesting a reset link, setting a new password from a valid
token, and handling expired/invalid tokens — each with Given/When/Then
acceptance criteria (including rate-limiting and the don't-reveal-if-email-exists
edge case) — followed by a RICE table ranking them, with assumptions noted.
