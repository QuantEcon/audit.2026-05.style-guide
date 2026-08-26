# bayes_intro

- **Series:** lecture-python-intro
- **File:** `lectures/bayes_intro.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.8 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-005` ×3; `qe-writing-003` ×1; `qe-writing-007` ×1. |
| Math         | 9.5/10 | `qe-math-014` (proposed) ×2. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×10; `qe-fig-003` ×2; `qe-fig-001` ×3. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 10. *Lines:* 31, 233, 343, 398, 418, 456, 538, 661, 738, 778. *Example:* code-cell figure without mystnb figure metadata.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 46, 238, 473. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 241, 478. *Example:* .set_title.
- **[qe-math-014 (proposed)]** *(reviewer)* — Braces \{…\} for events, parentheses (…) for sets. *Count:* 2. *Lines:* 196, 198. *Example:* the Bernoulli likelihood is written as an event with parentheses - `P(Y_i = 1 \mid \theta)` and `P(Y_i = 0 \mid \theta)` - where `\mathbb{P}\{Y_i = 1 \mid \theta\}` is called for; the H/L/D probabilities at lines 82-130 are named sets and correctly take parentheses. The lecture writes plain `P` for probability throughout even though it uses `\mathbb{E}` at lines 654 and 730, which is why the mechanical blackboard-bold check saw nothing here.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 203, 489, 491. *Example:* bold used for emphasis rather than definition: 'the bank does **not** know' (203), 'the posterior **concentrates**' (489), 'the posterior becomes **tighter**' (491). These are emphasis and belong in italic; the lecture's own bold-for-definition usage (lines 21, 78, 201, 211, 263, 527) is otherwise correct.

### Low severity
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 591. *Example:* the 'Further observations' preamble at lines 499-504 announces exactly two observations - the closed form and batch updating - but a third top-level section, 'Sequential and batch updates agree' (line 591), continues the same thread with no signpost, so the reader is told the thread ended one section early.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 96. *Example:* the risky-borrowing example (lines 96-133) walks through P(H)=0.2, P(D|H)=0.40, P(D)=0.12, P(H|D)=0.667 in prose alone; a probability tree or a 100-borrower box would carry it, and the lecture already shows it can draw that kind of schematic in the prior/data/posterior diagram at line 31.


## Strengths

- The density-versus-probability case convention holds without exception: lowercase for the Bernoulli and binomial likelihoods (`p(y \mid \theta)` at line 268, `p(k \mid \theta)` at line 571) and for the belief densities pi, pi_0, pi_n, with uppercase reserved for probabilities of events.
- The trapezoidal-rule figure at line 343 draws the numerical method itself - eight coarse trapezoids shaded under the fine integrand - rather than naming the method and moving on.
- The closed-form section verifies itself: line 538 overlays the analytical Beta(a_0+1, b_0) density on the grid posterior instead of asserting that the two agree.
- The `{note}` at lines 614-630 raises and answers the objection a careful reader would actually have - that the sequential update appears never to use independence - instead of leaving it to fester.
- Code is PEP8-clean and uses Unicode Greek consistently (`theta_grid`, `theta_true`, and a bare Unicode theta as the function argument at line 313); no spacing or naming deviations found anywhere in the 12 code cells.

## Recommended actions

1. Add mystnb figure metadata (name and caption) to the ten plotting cells at lines 31, 233, 343, 398, 418, 456, 538, 661, 738 and 778, so the figures can be cross-referenced from the text (qe-fig-005, 10 occurrences).
2. Remove the two embedded matplotlib titles at lines 241 and 478 and move that text into figure captions (qe-fig-003), and drop the `figsize=` overrides at lines 46, 238 and 473 unless the panel aspect genuinely requires them (qe-fig-001).
3. Switch the three emphasis bolds at lines 203, 489 and 491 to italic, keeping bold for the defined terms.
4. Write probability as `\mathbb{P}` throughout to match the `\mathbb{E}` already used at lines 654 and 730, and use braces for the two events at lines 196 and 198: `\mathbb{P}\{Y_i = 1 \mid \theta\}`.
5. Rewrite the 'Further observations' preamble at lines 499-504 to name three items, or fold 'Sequential and batch updates agree' (line 591) in as a subsection of it, so the section count the reader is given matches what follows.
6. Add a probability tree (or a 100-borrower box) to the risky-borrowing example at line 96, in the style of the schematic already drawn at line 31 - it is the one place in the lecture where a numerical argument runs for nearly forty lines with no picture.
