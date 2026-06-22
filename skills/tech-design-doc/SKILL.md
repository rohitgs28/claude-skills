---
name: tech-design-doc
description: >-
  Write a clear technical design document (RFC / design doc) before building:
  context and problem, goals and non-goals, the proposed design, alternatives
  considered, and risks. Use this whenever the user wants to "write a design
  doc", "RFC", "technical spec", "architecture doc", "design proposal", needs
  to plan or get review on how to build something non-trivial, or asks "how
  should I architect/approach this?" — even if they don't say "design doc".
---

# Technical Design Doc

A design doc exists to get alignment and catch mistakes while they're still
cheap — on paper, not in production. Its real value is the thinking it forces:
stating goals, weighing alternatives, and naming risks before code is written.
Optimize for a reviewer who will skim it in ten minutes and needs to find the
decision and its justification fast.

## Before writing

Make sure you understand the problem and constraints. If key inputs are missing
(scale, latency/throughput targets, existing systems it must fit, team, deadline),
ask for the few that genuinely change the design, and state assumptions for the rest.

## Structure

Use this template (also in `assets/design-doc-template.md`). Trim what doesn't apply.

```
# <Title> — Design Doc

**Author:** <name>  **Status:** Draft / In review / Approved  **Reviewers:** <names>

## Context & problem
What are we solving and why now? What exists today, and why is it insufficient?

## Goals & non-goals
- Goals: what this design must achieve (measurable where possible).
- Non-goals: explicitly out of scope, to bound the discussion.

## Proposed design
The recommended approach. Lead with a diagram or the shape of the solution,
then the key components, data model, interfaces/APIs, and how data flows.
Call out the decisions that matter.

## Alternatives considered
The other real options and why you didn't pick them. This is the heart of the
doc — a design with no alternatives looks unconsidered.

## Risks & trade-offs
What could go wrong, what you're trading away, failure modes, and mitigations.

## Rollout & operability
Migration/backfill, feature flags, monitoring, rollback. How do we ship it safely?

## Open questions
What's still undecided.
```

## Principles

- **Lead with the decision.** Reviewers want to know what you propose and why before the details.
- **Alternatives are mandatory.** Showing the paths not taken — and why — is what earns trust and surfaces better options.
- **Be concrete about trade-offs.** Every real design gives something up; pretending otherwise reads as naive.
- **Right-size it.** A two-pager for a small change, more for a system. Length should track risk, not effort.
- **Make it measurable.** Tie the design back to goals you can verify post-launch.

## Guardrails

- Don't invent requirements or numbers; mark estimates and assumptions as such.
- Stay at the design level — this is not the implementation. Pseudocode and interfaces, not full code.
- Surface open questions honestly rather than implying false certainty.

## Example

Input: "Write a design doc for adding rate limiting to our public API."
Output: A doc stating the problem (abuse and noisy-neighbor risk), goals
(per-key limits, low added latency) and non-goals (no billing integration in v1),
a proposed token-bucket design with where state lives and how limits are
configured, alternatives (fixed window, leaky bucket, gateway-level vs. app-level)
with trade-offs, risks (hot keys, clock skew, Redis dependency) with mitigations,
and a rollout plan behind a flag with metrics.
