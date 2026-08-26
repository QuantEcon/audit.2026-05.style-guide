# dovis_accounting_mf

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/dovis_accounting_mf.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.3 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-002` ×10; `qe-writing-001` ×3; `qe-writing-009` (proposed) ×1, +2 more. |
| Math         | 4.5/10 | `qe-math-010` (proposed) ×17; `qe-math-011` (proposed) ×1. |
| Code         | 7/10  | `qe-code-002` ×47. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4.5/10 | `qe-fig-003` ×9; `qe-fig-007` ×2; `qe-fig-005` ×2, +1 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 47. *Lines:* 560, 561, 565, 572, 573, 574, 578, 591, 592, 597, …. *Example:* spelled-out `phi`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 7. *Lines:* 504, 604, 1226, 1618, 1976, 2132, 2166. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 9. *Lines:* 1619, 1624, 1628, 1641, 1646, 1650, 1654, 1658, 1663. *Example:* .suptitle.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 17. *Lines:* 132, 137, 193, 207, 314, 323, 331, 360, 363, 383, …. *Example:* non-blackboard `\Pr`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 10. *Lines:* 66, 282, 375, 995, 1565, 1580, 1597, 1599, 2042, 2048. *Example:* twenty-four sentences in this file run past 34 words and ten of them past 42: 2048 is 56 words comparing Colombia and Chile on two channels at once, 1580 is 55, 1565 and 1599 are 53, 2042 is 51, 1597 is 50, 66 is 48, and 282, 375 and 995 are 42-43 each; the pattern is a main clause followed by two or three subordinate clauses that each deserve their own sentence, and it is worst exactly where the argument is hardest (the disinflation mechanics at 1565-1599 and the case studies at 2042-2048).

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 2116, 2165. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 2. *Lines:* 666, 667. *Example:* spine removal.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 1. *Lines:* 1775. *Example:* decorated distribution `\mathcal{N}`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 2054, 2062, 2074. *Example:* 2 sentences in one paragraph.

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 409. *Example:* the Ramsey and Markov benchmarks are set up at 350-427 as the two poles the model lives between - line 409 says "The full model *interpolates* between these two extremes depending on the cost $\xi_t$" - and that interpolation is never drawn; the section is entirely prose and bullet lists, the next figure (497) is about indirect utility, and no later figure plots inflation or debt against $\xi$ with the two benchmarks marked, although the model is solved on a $\xi$ grid and the values needed are already in hand.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 272. *Example:* 2 spaces.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 688. *Example:* i.i.d..


## Strengths

- Figures are named and then actually referenced: `fig-credibility-targets` is cited at 308 before it appears, `fig-fundamental` at 1584 and 1734, `fig-institutional` at 1756 - this is the only lecture in the series that uses `{numref}` as a matter of course.
- The lecture is explicit about where its stripped-down implementation departs from the paper: 1576-1590 states that the debt-issuance policy shifts the wrong way, names the two reasons (fixed $\theta$ instead of an AR(1), coarse grids putting debt near the lower bound at roughly 15% of GDP against the paper's 34.9%), and says which of the two experiments is unaffected.
- Bold marks definitions and italic marks emphasis with almost no slippage across 2201 lines - **fiscal dominance** / **monetary dominance** (43), **real primary surplus** (165), **regime indicator** (284), **fundamental** / **institutional disinflation** (1557) against *endogenous* (263), *state-contingent* (366), *interpolates* (409), *upward* (1578).
- The reason for dampened value function iteration is derived rather than asserted: 995-997 explains that the value function feeds back within the period through $J$ and the surplus, so $T$ need not be a contraction, which is why $\omega = 0.01$ appears in `solve_model` at 1002.
- Code uses Unicode Greek throughout (`θ`, `φ`, `ξ`, `χ`, `ψ`, `β_hat`), keeps JAX kernels small and jitted, and reports the Bellman residual it converged on (1044-1049) instead of silently returning.

## Recommended actions

1. Split the ten 42-plus-word sentences listed above - starting with 2048, 1580, 1599 and 1565 - into one clause per sentence; at 24 sentences over 34 words this is the dominant readability issue in the lecture.
2. Replace the 17 `\Pr` operators with `\mathbb{P}` at 132, 137, 193, 207, 314, 323, 331, 360, 363, 383 and 7 more (qe-math-010 (proposed)).
3. Move the nine embedded matplotlib titles at 1619, 1624, 1628, 1641, 1646, 1650, 1654, 1658 and 1663 into figure captions (qe-fig-003), add `mystnb: figure: caption/name` to the two case-study cells at 2116 and 2165 so Colombia and Chile can be cross-referenced like the other figures (qe-fig-005), and set `lw=2` on the eight `plot` calls at 1623, 1627, 1631, 1645, 1649, 1653, 1657 and 1662 (qe-fig-008).
4. Add a figure for the Ramsey-Markov interpolation claimed at 409 - inflation and debt as functions of $\xi$ with the two benchmark levels marked - which would also give the reader something to hold on to across the 250 prose-and-code lines of the computational algorithm section.
5. Drop the seven `figsize=` overrides at 504, 604, 1226, 1618, 1976 and 2132, 2166 (qe-fig-001) and restore the spines removed at 666-667 (qe-fig-007).
6. Sweep the small items: `\mathcal{N}` to plain `N` at 1775 (qe-math-011 (proposed)), `i.i.d.` to `IID` at 688 (qe-writing-009 (proposed)), split the two-sentence paragraphs at 2054, 2062 and 2074 (qe-writing-001), and collapse the double space at 272 (qe-writing-008).
