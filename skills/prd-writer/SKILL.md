---
name: prd-writer
description: >-
  Write a clear, decision-ready Product Requirements Document (PRD): the
  problem, goals, users, scope, requirements, success metrics, and open
  questions. Use this whenever the user wants to "write a PRD", "spec out a
  feature", "write a product spec", "document requirements", create a
  one-pager or product brief, or turn a feature idea into a structured doc the
  team can build from — even if they don't use the term "PRD".
---

# PRD Writer

A PRD aligns a team on *what* to build and *why* before anyone argues about
*how*. The best PRDs are short, opinionated, and honest about what they don't
know. A vague PRD wastes a quarter; a crisp one saves one.

## Before writing: get the essentials

A PRD is only as good as its inputs. If the user hasn't provided these, ask for
the few that genuinely block a useful draft (don't interrogate — make
reasonable assumptions and flag them):

- The problem and who has it (the user/segment and their pain)
- The goal and how success is measured
- Constraints: timeline, platform, dependencies, non-goals
- Any known requirements or prior decisions

## Structure

Use this template (it's also in `assets/prd-template.md`). Trim sections that
don't apply; never pad.

```
# <Feature name> — PRD

**Author:** <name>   **Status:** Draft / In review / Approved   **Last updated:** <date>

## 1. Problem
What problem are we solving, for whom, and why now? Include evidence
(data, support tickets, research) where you have it.

## 2. Goals & non-goals
- Goals: the outcomes this must achieve (not features — outcomes).
- Non-goals: what we are explicitly NOT doing, to bound scope.

## 3. Users & use cases
Primary persona(s) and the concrete scenarios they're in.

## 4. Requirements
What the solution must do, ranked. Use P0 (must) / P1 (should) / P2 (nice).
Write each as a capability, not an implementation.

## 5. Success metrics
The specific, measurable signals that tell us this worked (and guardrail
metrics that tell us it didn't hurt something else).

## 6. Open questions & risks
What we don't yet know, and what could go wrong.

## 7. Appendix (optional)
Mocks, links, prior art, alternatives considered.
```

## Principles

- **Outcomes over features.** "Reduce time-to-first-value" beats "add an onboarding wizard" — the second is one possible solution to the first.
- **Make scope explicit with non-goals.** Most PRD failures are scope creep; naming non-goals is the cheapest insurance.
- **Metrics must be measurable.** "Improve engagement" is not a metric; "increase D7 retention from 22% to 28%" is.
- **Prioritize ruthlessly.** If everything is P0, nothing is. Force the ranking.
- **Surface unknowns** rather than papering over them — a PRD that pretends certainty misleads the team.

## Guardrails

- Don't invent data or research findings. If a claim needs evidence you don't have, mark it as an assumption to validate.
- Keep it readable in one sitting. Length is not rigor.
- Stay solution-agnostic in the requirements section; implementation belongs in a design doc.

## Example

Input: "Write a PRD for letting users export their data to CSV."
Output: A one-to-two page PRD stating the problem (users can't get their data
out, blocking trust and churn-prevention), goals (self-serve export, no support
ticket), non-goals (no scheduled/automated exports in v1), P0/P1 requirements,
a success metric (X% of churned users who exported vs. didn't), and open
questions (PII handling, size limits) — with any assumed numbers flagged as
needing validation.
