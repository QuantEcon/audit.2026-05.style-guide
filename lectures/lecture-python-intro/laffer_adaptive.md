# laffer_adaptive

- **Series:** lecture-python-intro
- **File:** `lectures/laffer_adaptive.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-005` ×5; `qe-writing-002` ×5; `qe-writing-003` ×2, +2 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7/10  | `qe-code-001` ×13. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×2; `qe-fig-004` ×2; `qe-fig-008` ×7, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×4. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 13. *Lines:* 183, 243, 250, 302, 329, 344, 381, 459, 483, 525, …. *Example:* invalid escape sequences in non-raw strings - `'$\pi_l$'`, `'$\pi$'` (243, 250), which pycodestyle flags as W605 and which the exercise solutions correctly write as `r'$\pi_l$'` (541); `eq_g = lambda x: ...` bound to a name instead of a `def`, twice (329, 344); a backslash continuation inside an expression that is already parenthesisable, with a misaligned second line (302-303); two different continuation indents for the same `axes[2].text(...)` call (380-383); a continuation line under-indented relative to the opening paren (183); and alignment padding before `=` that PEP8 rules out (459, 483, 525, 535, 557, 559).
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 7. *Lines:* 241, 373, 374, 375, 376, 468, 469. *Example:* plot() without lw=.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 20, 31, 44, 94, 282. *Example:* line 20 is a 38-word sentence that cites `{doc}`money_inflation`` twice within itself ("As in the lecture money_inflation ... in place of the linear demand function used in this lecture money_inflation"), and lines 18, 20 and 31 all repeat the same cross-reference; 44-46 is a 48-word sentence; and two sentences have lost a word, so the reader has to reconstruct them: "Equation the expressions for $m_{t+1}$" (94, for "Equate") and "if we initial $\pi_{-1}^*, p_{-1}$ appropriately" (282, for "initialise").
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 5. *Lines:* 36, 37, 101, 124. *Example:* bold used for emphasis where the rule asks for italic: **lower** (36), **reduced** and **lower** (two on line 37), **lower** (124); and **Pseudo-code** at 101 is a bolded pseudo-heading rather than a definition - the parallel material at 103-112 is real body text under a real heading.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 31. *Lines:* 14, 18, 20, 22, 23, 31, 33, 37, 44, 46, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 364, 529. *Example:* figsize=.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 219, 398. *Example:* caption of 10 words.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 457, 524. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-ref-001]** — Use correct citation style. *Count:* 4. *Lines:* 23, 49, 51. *Example:* `` {cite} `` in narrative flow: 'by  `` {cite} ``'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 33. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 158, 261. *Example:* 158-160 describes both sides of the same equation the same way - "The left side of `` {eq}`eq:ada_steadypi` `` is steady state revenue raised by printing money" followed by "The right side ... is the quantity of time $t$ goods that the government raises by printing money" - when the right side is $g$, defined at 68 as the part of government *expenditure* financed by printing money; and the initial condition changes index between sections without comment: the claims at 126-130 are stated for $p_0$ and $m_1 - p_0 = -\alpha\bar\pi$, while 261-266 and the code compute $p_{-1} = m_0 + \alpha\pi^*$, and the figure caption at 402 calls the same object $\pi_0$.

### Low severity
_None found._


## Strengths

- Every equation the argument depends on is labelled and then actually re-used: `eq:ada_msupply` (66) at 70, `eq:ada_msupply2` (74) at 94 and 110, `eq:ada_mdemand` (80) at 94, `eq:adaptex` (88) at 31, 46, 94 and 109, `eq:ada_steadypi` (148) at 158, 160 and 162.
- The pseudo-code block at 105-112 states the algorithm as three ordered steps, each pointing at the equation it solves - a reader can implement `solve_laffer_adapt` (287-316) from that list alone.
- The `{note}` at 48 parks the least-squares-learning literature out of the main line of argument rather than interrupting it.
- Parameters live in a `namedtuple` with a `create_model` factory using Unicode Greek fields (`α`, `δ`), so the two exercises can sweep $g$ and $\delta$ without touching the solver.
- The verification cells at 321-347 check the claimed steady state numerically - printing $m_{t+1}-m_t$, $p_{t+1}-p_t$ and `np.isclose(eq_g(...), g)` - instead of asserting convergence in prose.

## Recommended actions

1. Convert the author-position citations to `{cite:t}` (20, 23, 42, 49, 51) - "the adaptive expectations assumption used by `` {cite:t}`Cagan` `` and `` {cite:t}`Friedman1956` ``".
2. Fix the mislabelled seigniorage curve at 242: the legend string reads `exp(-αx) - exp(-(1-α)x)` while `compute_seign` (228-229) and `` {eq}`eq:ada_steadypi` `` both use $1+\alpha$.
3. Rewrite 158-160 so the two sides of `` {eq}`eq:ada_steadypi` `` are described differently, and settle on one time index for the initial condition across 126-130, 261-266 and the caption at 402.
4. Strip the 31 runs of double spaces - they are dense enough in the Overview (14, 18, 20, 22, 23, 31, 33, 37, 44, 46) to be a pattern rather than typos - and split the two-sentence paragraph at 33.
5. Add `mystnb: figure: caption/name` metadata to the three un-named figures (360, 457, 524); the steady-state comparison in exercise 1 is a headline result and currently cannot be cross-referenced.
6. Fix the code items above - raw strings for the LaTeX labels, `def` instead of the two named lambdas, and no alignment padding before `=` - and set `lw=2` on the seven line plots.
7. Cut the repeated `{doc}`money_inflation`` cross-references in the Overview down to one, break the 38- and 48-word sentences, use italic for the emphasised words at 36, 37 and 124, and settle on either `\bar \pi` or `\overline \pi` (both appear, at 126 and 120).
