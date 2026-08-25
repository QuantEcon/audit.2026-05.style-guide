# QuantEcon Style Audit

A style-guide compliance audit of the QuantEcon lecture corpus, scored against 7 rule
categories from the [`action-style-guide`](https://github.com/QuantEcon/action-style-guide)
registry.

This page is for triage — *where should we put our attention?* Start here, then open a
[series report](#where-to-focus-first) for the detail, the [charts](charts.md) for a
visual overview, or the [full findings](details.md) for the complete breakdown.

---

## Where to focus first

Series ranked worst → best. **Needs work** counts the HIGH + MEDIUM lectures; the rest
are LOW or NONE.

<!-- qe:focus -->
| Attention | Series | Score | Needs work | Weakest categories |
|-----------|--------|-------|-----------|--------------------|
| 🟠 **Some** | [lecture-python-advanced.myst](lecture-python-advanced.myst/index.md) | 8.1 | 30 / 68 | Math (5.9), Figures (6.3) |
| 🟠 **Some** | [lecture-dp](lecture-dp/index.md) | 8.2 | 17 / 52 | Math (6.4), Figures (6.4) |
| 🟠 **Some** | [lecture-python.myst](lecture-python.myst/index.md) | 8.4 | 41 / 145 | Figures (6.5), Writing (6.9) |
| 🟢 **Low** | [lecture-python-intro](lecture-python-intro/index.md) | 8.5 | 11 / 56 | Figures (6.5), Writing (6.6) |
| 🟢 **Low** | [lecture-python-programming](lecture-python-programming/index.md) | 8.6 | 5 / 27 | Writing (5.7), Figures (7.3) |
<!-- /qe:focus -->

**Every HIGH-priority lecture in this pass is HIGH because of one weak category, not
because of a low overall score.** No lecture in the corpus has an overall score at or
below 5.0. So the useful triage question is not *which lectures* but *which category*:
Math is the binding constraint on most of them, then Writing, then Figures. Fix a
category across a series and a large block of HIGH lectures clears at once.

---

## The biggest wins

Fix one of these *once* and it lifts dozens of lectures. Ordered by reach.

<!-- qe:wins -->
| Fix this | What it means | Lectures helped | Effort |
|----------|---------------|-----------------|--------|
| **Name your figures** | Add a `name:` so figures can be cross-referenced with `numref` | **273** | 🔧 |
| **Collapse double spaces** | Reduce runs of spaces between words to one | **237** | 🔧 |
| **Figure sizes** | Drop `figsize=` overrides — let the site defaults apply | **224** | 🔧 |
| **Line widths** | Pass `lw=2` on line plots for consistent weight | **216** | 🔧 |
| **Plot titles → captions** | Move `ax.set_title(...)` out of the plot into the figure caption | **165** | ✋ |
| **Heading capitalization** | Section headings → sentence case (first word + proper nouns only) | **146** | 🔧 |
| **Transpose notation** | Replace `'` and `^T` with `^\top` | **122** | 🔧 |
| **Narrative citations** | Use `{cite:t}` where the author name is part of the sentence | **110** | ✋ |

Reach is out of 348 lectures. 🔧 = scriptable sweep · ✋ = needs a human pass.
<!-- /qe:wins -->

The mechanical sweeps at the top of that list touch most of the corpus and need no
judgment — they are the highest-leverage place to start. The
[remediation plan](details.md#remediation-plan) has the ordered list and the exact
lectures.

---

## Fix immediately ⚠️

Four findings are structural rather than stylistic — they change what the build
produces, so they are worth fixing regardless of the broader effort.

| Where | Problem | Why it matters |
|-------|---------|----------------|
| [`lecture-python-programming` · `python_by_example.md:499` and `:549`](https://github.com/QuantEcon/lecture-python-programming/blob/main/lectures/python_by_example.md#L499) | Two `{exercise-start}` fences are never closed, so the directive swallows the rest of the exercise, including a nested `{hint}` at the same tick count (`qe-admon-003`) | These are the only two malformed gated directives in 690 across the corpus. The exercise and its hint do not render as intended. |
| [`lecture-python.myst` · `cross_product_trick.md:133`](https://github.com/QuantEcon/lecture-python.myst/blob/main/lectures/cross_product_trick.md#L133) | `` {eq}`eq:Kalman102} `` — mismatched braces, and the label is attached to a bare `align*` block that carries no label | The cross-reference silently fails to render. |
| [`lecture-dp` · `cross_product_trick.md:133`](https://github.com/QuantEcon/lecture-dp/blob/main/lectures/cross_product_trick.md#L133) | The same defect — `lecture-dp` syncs this lecture from `lecture-python.myst` | Fixing it upstream fixes both. |
| [`lecture-python.myst` · `ifp_advanced.md:158`](https://github.com/QuantEcon/lecture-python.myst/blob/main/lectures/ifp_advanced.md#L158) (and the `lecture-dp` copy) | Raw LaTeX `\label{a:y0}` inside a `$$` block (`qe-math-007`) | MyST does not resolve `\label`; the equation cannot be referenced with `` {eq}` ` ``. |

```{note}
**A correction to the previous pass.** It reported `divergence_measures.md:134` as
`\begin{align}` inside a `$$ … $$` block that "breaks the PDF build". Re-checked
mechanically against the pinned snapshot, **there is no `align` inside `$$` anywhere in
the corpus** — not in that file and not in any of the other 347 lectures. The block at
that line is a *bare* top-level `\begin{align}`, which MyST's amsmath extension handles.
It is still a convention outlier — 17 bare alignment blocks against 6,094 `$$` blocks and
1,783 `{math}` directives — and it is reported under `qe-math-006` as such, but it is not
the build breaker the earlier report described.
```

---

## What changed since the previous pass

The same checks were run over both corpus snapshots, so the comparison is a measurement
of the lectures rather than of the method. See the
[trend chart](charts.md#change-since-the-previous-pass) for every rule.

The corpus grew from 300 to 348 lectures. Against that, most rules held roughly flat as a
share of the corpus, three improved and two got worse:

| Direction | Rule | Share of corpus |
|-----------|------|-----------------|
| 🟢 Improving | `qe-writing-008` — remove excessive whitespace between words | 78% → 68% |
| 🟢 Improving | `qe-writing-006` — capitalize lecture titles properly | 48% → 42% |
| 🟢 Improving | `qe-writing-001` — use one sentence per paragraph | 55% → 50% |
| 🔴 Worsening | `qe-fig-004` — caption formatting conventions | 9% → 19% |
| 🔴 Worsening | `qe-fig-001` — do not set figure size unless necessary | 62% → 64% |

Both regressions are in Figures, and for the same reason: new lectures add figures faster
than the figure conventions are applied to them. `qe-fig-004` doubled because the newer
lectures do add captions — which is progress — but write them in Title Case and over the
six-word limit.

---

## How this pass was measured

41 of the 49 rules are checked by program, over a **pinned corpus snapshot** — one commit
per series, recorded in every report header and in
[`lectures/data/snapshot.json`](https://github.com/QuantEcon/audit.2026-05.style-guide/blob/main/lectures/data/snapshot.json).
Scores and priority buckets are then derived arithmetically from the rubric. The 8
judgment-only rules are reviewed by reading. [Spec §8](spec.md) describes the layers and
why they are separate; [§9](spec.md) lists exactly which rules fall where.

That matters for reading the numbers: a category scoring 10 means *no mechanical
violation was measured in it*, not that a human declared it perfect.

---

## Navigating this report

- **Series reports** (sidebar) — per-series detail: scores, ranked lectures, and every
  lecture's own report. *Start here once you've picked a series above.*
- **[Charts](charts.md)** — heatmap, rule reach, the cross-pass trend, priority mix.
- **[Full findings](details.md)** — the complete scoreboard, every recurring rule, every
  HIGH lecture, and the remediation plan.
- **[Scoring spec](spec.md)** — the rubric, the pass methodology, and the measured
  deterministic coverage.
- **[Appendix — feedback](appendix.md)** — what this audit fed back to the style guide and
  `action-style-guide` (proposed rules and tooling, issues #18–#21).

> Rules are cited by their `action-style-guide` IDs (e.g. `qe-fig-001`). Seven are tagged
> **(proposed)** — documented in the style guide but not yet in the rule registry
> ([issue #18](https://github.com/QuantEcon/action-style-guide/issues/18)).
