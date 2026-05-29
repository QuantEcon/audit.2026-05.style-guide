# QuantEcon Style Audit — May 2026

A style-guide compliance audit of **299 lectures** across 5 series, scored against 7 categories. **Overall: 8.0 / 10.**

This page is for triage — *where should we put our attention?* Start here, then open a [series report](#where-to-focus-first) for the detail, the [charts](charts.md) for a visual overview, or the [full findings](details.md) for the complete breakdown.

---

## Where to focus first

Series ranked worst → best. **Needs work** counts the HIGH + MEDIUM lectures (the rest are LOW / NONE — fine or only minor polish).

| Attention | Series | Score | Needs work | The main story |
|-----------|--------|-------|-----------|----------------|
| 🔴 **High** | [lecture-python-advanced.myst](lecture-python-advanced.myst/index.md) | 7.0 | 33 / 62 | Math notation debt in older LQ lectures — transpose (`'` → `^\top`) and expectation (`E_t` → `\mathbb{E}_t`). 6 lectures score ≤ 5. |
| 🔴 **High** | [lecture-dp](lecture-dp/index.md) | 7.5 | 22 / 50 | **The biggest backlog: 17 HIGH lectures.** Mostly single-category drags — citations, cross-series links, and figures — plus the same LQ math debt. |
| 🟠 **Some** | [lecture-python-intro](lecture-python-intro/index.md) | 7.6 | 10 / 51 | Figures need the most love (names + sizes), plus a heading-case sweep. Only 1 HIGH lecture. |
| 🟠 **Some** | [lecture-python-programming](lecture-python-programming/index.md) | 8.0 | 3 / 26 | Exemplary on code; the only weak spot is figures (titles + sizes). |
| 🟢 **Low** | [lecture-python.myst](lecture-python.myst/index.md) | 9.0 | 2 / 110 | In great shape — 86 % of lectures are clean. **Use this series as the model.** Just a heading-case sweep left. |

**Bottom line:** put `lecture-python-advanced.myst` and `lecture-dp` first — together they hold 23 of the 29 HIGH-priority lectures. `lecture-python.myst` is the standard to aim for.

---

## The biggest wins

Fix one of these *once* and it lifts dozens of lectures at a time. Ordered by reach. 🔧 = scriptable sweep · ✋ = needs a human pass.

| Fix this | What it means | Lectures helped | Effort |
|----------|---------------|-----------------|--------|
| **Heading capitalization** | Section headings → sentence case (capitalize only the first word + proper nouns) | **~170** | 🔧 |
| **Greek letters in code** | Use `α`, `β`, `γ` instead of `alpha`, `beta`, `gamma` | **~150** | 🔧 |
| **Figure sizes** | Drop `figsize=` overrides — let the site defaults apply | **~125** | 🔧 |
| **Name your figures** | Add a `:name:` so figures can be cross-referenced with `numref` | **~120** | 🔧 |
| **Plot titles → captions** | Move `ax.set_title(...)` out of the plot into the figure caption | **~90** | ✋ |
| **Cross-series links** | Replace raw `quantecon.org` URLs with `{doc}` references | **~60** | 🔧 |

Beyond these, a **math-notation cluster** (transpose `^\top` ~46, expectation `\mathbb{E}` ~60, distribution `N` ~30) is concentrated in the older LQ lectures of `lecture-python-advanced.myst` and `lecture-dp` — best tackled as one careful pass over that cluster.

The first four are mechanical and together touch the majority of the corpus — they're the highest-leverage place to start. See the [full remediation plan](details.md#step-by-step-remediation-plan) for the ordered list and the exact lectures.

---

## Fix immediately ⚠️

Two findings can break the published builds — worth fixing regardless of the broader effort:

| Where | Problem | Why it's urgent |
|-------|---------|-----------------|
| [`lecture-python.myst` · `divergence_measures.md:134`](https://github.com/QuantEcon/lecture-python.myst/blob/main/lectures/divergence_measures.md#L134) | `\begin{align}` inside a `$$ … $$` block | **Breaks the PDF build.** Change `align` → `aligned`. |
| [`lecture-python.myst` · `cross_product_trick.md:133`](https://github.com/QuantEcon/lecture-python.myst/blob/main/lectures/cross_product_trick.md#L133) | Broken `{eq}` reference (mismatched braces, label on a bare `align*` block) | Cross-reference silently fails to render. |

---

## Navigating this report

- **[Series reports](lecture-dp/index.md)** (sidebar) — the focused, per-series detail: scores, ranked lectures, and every lecture's own report. *Start here once you've picked a series above.*
- **[Charts](charts.md)** — visual overview (heatmap, priority distribution, category averages).
- **[Full findings](details.md)** — the complete scoreboard, all 15 systemic issues, all 29 HIGH lectures, and the step-by-step remediation plan.
- **[Scoring spec](spec.md)** — how the 0–10 scores and HIGH/MEDIUM/LOW/NONE priorities are defined.

> Rules are cited by their `action-style-guide` IDs (e.g. `qe-fig-001`). Seven are tagged **(proposed)** — documented in the style guide but not yet in the rule registry ([issue #18](https://github.com/QuantEcon/action-style-guide/issues/18)).
