# jv

- **Series:** lecture-python.myst
- **File:** `lectures/jv.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×3; `qe-writing-002` ×5; `qe-writing-005` ×3, +4 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-001` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6.5/10 | `qe-fig-005` ×3; `qe-fig-003` ×1; `qe-fig-008` ×4, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 212, 213, 275, 400, 475, 486. *Example:* the parameter named `ɛ` at 213, and used at 222, 224, 225 and 226, is U+025B LATIN SMALL LETTER OPEN E, not the Greek U+03B5 - a confusable that will not be found by a search for `ε` and is out of step with the genuine Greek `α`, `β`, `ϕ`, `π` used everywhere else in the same file; three lambdas are bound to names instead of being defined with `def` (275 `v_func`, 475 `s`, 476 `ϕ`, PEP8 E731), and the last two shadow the model's own $s$ and $\phi$ policy arrays; 400 has two spaces after a comma inside the list literal `["s policy", "ϕ policy",  "value function"]`; 212 has a single space before the inline comment `search_grid_size=15, # Size of each action grid`; and the docstring line at 486 runs to 108 characters because a second sentence was appended to it rather than wrapped.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 155, 175, 417, 419, 585. *Example:* the prose drops definite articles and reads as note form rather than sentences: "marginal cost of investment via either $\phi$ or $s$ is identical" (155), "Return from investment via $\phi$ dominates expected return from search" (175), "Worker switches from one investment strategy to the other depending on relative return" (417), "worker does better by investing in human capital" (419) - the same clipping appears at 101 ("Agent's objective: maximize...") and 180. And 585-586 stacks three hedges on one claim: "This seems reasonable and helps us confirm that our dynamic programming solutions are probably correct".
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 3. *Lines:* 59, 144, 380. *Example:* H3 Title Case: 'Model Features' (Features).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 402, 500, 569. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 406. *Example:* .set(title=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 398, 469, 561. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 4. *Lines:* 405, 507, 508, 571. *Example:* plot() without lw=.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 182. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 21, 413. *Example:* the H1 at 21 announces "Job Search VIII" but nothing in the lecture says what the preceding seven are or where to find them - there is no link to the series and no `{doc}` reference, so a reader arriving here cannot place it; and 413 ("The horizontal axis is the state $x$, while the vertical axis gives $s(x)$ and $\phi(x)$") describes a two-panel figure while the figure above it at 398-410 has three panels, the third being the value function, which the sentence does not mention.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 72, 118, 263. *Example:* 263 uses bold for emphasis - "written for a **single** state $x$ and a **single** action pair" - where the rule wants italic, and it is the only bold in the file; meanwhile the terms the lecture actually defines are in plain text, including "job-specific human capital" at 72, which is the central concept, and the notation $a \vee b := \max\{a, b\}$ introduced mid-sentence at 118. The one italic in the file, *infinitely* at 536, is correct.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 72, 83, 182. *Example:* 2 spaces.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 45. *Example:* {cite} in narrative flow: 'and {cite}`'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 143. *Example:* "### Back-of-the-Envelope Calculations" (143-184) is the analytical heart of the lecture and it has no figure. It evaluates the two returns at $x = 0.05$ (0.5 from search against 0.23 from investment) and at $x = 0.4$ (0.5 against 0.8), then states as a prediction that the ranking flips somewhere in between. That is one two-line plot - the flat $\pi(1)\mathbb{E}u = 0.5$ against the increasing $g(x, 1) = A x^{\alpha}$, with the crossing marked - and the crossing point is precisely what the policy figure at 398 is later asked to confirm, so the reader has no picture to compare it against.


## Strengths

- The vectorization is written to be read: `_B` at 267 handles one state and one action pair so that it lines up term by term with {eq}`defw`, and the three stacked `jax.vmap` calls at 298-300 replace a triple loop with the argument-order comment at 297 sitting directly above the matching `in_axes` tuples - the extra alignment spaces there earn their PEP8 exemption.
- Every display equation that is reused later is labelled and then actually cited: `jd` (94) at 103 and 429, `jvbell` (107) at 247, `defw` (251) at 264 - and the two internal targets work the same way, with `(jvboecalc)=` (143) referenced at 415 and `(jv_policies)=` (387) referenced at 521, so the lecture closes the loop between its informal predictions and its computed policies.
- The probability at 430 is written `\mathbb{P}\{b_{t+1} = 1\} = \pi(s_t)`, with braces around the event as proposed qe-math-014 (proposed) asks, and $f$ stays lowercase for the offer distribution throughout (83, 132, 202) per proposed qe-math-015 (proposed).
- The `{note}` at 370-378 states plainly that these grids would run fine in NumPy and gives the actual reason for JAX (finer grids, more state variables, GPU) instead of implying the model requires it.
- The second exercise checks its own answer against the first: 577 finds the maximizer near 0.6 and 579-583 ties it back to the $\phi_t \approx 0.6$ found in `jv_ex1`, so the two exercises corroborate rather than merely accumulate.
- Notation in the code tracks notation in the prose - `α`, `β`, `ϕ_grid`, and `π` as an actual function name at 242 - and the docstrings at 268-274 and 308-313 state array shapes and the infeasibility convention rather than restating the function name.

## Recommended actions

1. Add `mystnb: figure: caption`/`name` metadata to the three un-named figures (398, 469, 561) and move `ax.set(title=title)` at 406 into panel labels; the three-panel figure at 398 is the lecture's headline result and is currently reachable only through the bare `(jv_policies)=` anchor.
2. Rename `ɛ` to `ε` at 213, 222, 224, 225 and 226 - it is currently the Latin open-e U+025B rather than Greek epsilon, which makes the parameter unsearchable and inconsistent with the rest of the file.
3. Add the crossover plot to the back-of-the-envelope section (143-184): the expected return from search against the return from investment as functions of $x$, with the crossing marked, so the prediction at 181-182 can be seen before it is tested.
4. Sentence-case the three headings flagged at 59, 144 and 380 ("Model features", "Back-of-the-envelope calculations", "Solving for policies"), switch the citation at 45 to `{cite:t}`, and close the three double spaces at 72, 83 and 182.
5. Fix line 413 so it accounts for all three panels of the figure above it, and repair the article-dropping sentences at 155, 175, 417 and 419.
6. Add `lw=2` to the three line plots at 405, 507 and 571, but not to 508 - that call draws the scatter of realizations with the marker-only format `'go'` (see scanner doubts). Keep `figsize=(8, 8)` at 500: a 45 degree diagram has to be square; the other two (402, 569) can go.
7. Bold the definitions at 72 and 118, change the two bold **single**s at 263 to italic, split the two-sentence paragraph at 182, and add a sentence or a `{doc}` link near the title saying which lectures Job Search I-VII are.
