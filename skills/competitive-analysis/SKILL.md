---
name: competitive-analysis
description: >-
  Produce a structured competitive or market analysis: identify the relevant
  competitors, compare them across meaningful dimensions in a matrix, and draw
  out positioning, gaps, and takeaways. Use this whenever the user wants to
  "analyze competitors", "do a competitive analysis", "compare us to X/Y/Z",
  "market/landscape analysis", "where do we fit", or needs a feature/pricing
  comparison to inform product or go-to-market decisions — even if they just
  ask "who else does this and how are we different?"
---

# Competitive Analysis

A competitive analysis is only useful if it drives a decision: what to build,
how to position, where the gap is. Avoid a flat feature checklist — the value is
in the *interpretation*. Be honest, including about the user's own product;
flattering analysis is worse than none.

## Process

1. **Frame the question.** What decision is this informing — product roadmap,
   positioning, pricing, build-vs-buy? The frame determines which competitors
   and dimensions matter.
2. **Pick the right competitors.** Include direct competitors, notable indirect
   ones (different approach, same job-to-be-done), and the status-quo
   alternative (often "do nothing" or a spreadsheet). 4–7 is usually right.
3. **Choose dimensions that matter to the buyer**, not just features you can
   list. Think: core capability, target user, pricing model, ease of adoption,
   integrations, performance, support, and any axis specific to the domain.
4. **Fill the matrix with evidence.** Use what's verifiable. When you're
   inferring or a fact isn't confirmed, mark it (e.g. "~", "unclear") rather
   than stating it as fact. Cite sources where you have them.
5. **Interpret.** This is the payoff: where is the market crowded vs. empty?
   What's the user's defensible edge? Where are they weak? What's the
   positioning that follows?

## Output structure

```
## Competitive Analysis: <market / product>

### Scope
What decision this informs; which competitors are included and why.

### Comparison matrix
| Dimension | Us | Competitor A | Competitor B | ... |
|-----------|----|--------------|--------------|-----|
| <buyer-relevant axis> | ... | ... | ... | ... |

### Landscape read
- Where the market is saturated vs. underserved.
- Each competitor's core strength and weakness (1–2 lines each).

### Our position
Honest strengths, honest gaps, and the differentiation that holds up.

### Takeaways & recommendations
The 2–4 decisions or moves this analysis points to.

### Sources & confidence
What's verified vs. estimated; links where available.
```

## Principles

- **Decisions over description.** End with "so what," not just "here's everyone."
- **Buyer's lens.** Compare on what makes someone choose, not on internal feature names.
- **Intellectual honesty.** Name your product's real weaknesses; a rosy self-assessment misleads the team.
- **Mark uncertainty.** Competitor facts go stale and are often guessed — label inferences and cite sources.

## Guardrails

- Do not fabricate competitor pricing, metrics, or features. If unverified, say so and mark it as an estimate.
- Avoid disparagement; be fair and factual about competitors.
- If you researched the web, cite sources and note the date — this data ages quickly.

## Example

Input: "Competitive analysis for my open-source MCP gateway vs. the alternatives."
Output: A matrix comparing it to Microsoft MCP Gateway, Docker MCP Gateway, and
Kong's AI proxy across setup time, dependencies, config model, security features,
and target user; a landscape read showing the enterprise space is crowded but
the lightweight single-binary niche is open; an honest position (edge: zero-infra
and tool-integrity; gap: no UI/cluster story); and the takeaway to lead
positioning on "5-minute, one-binary MCP security for devs and small teams."
