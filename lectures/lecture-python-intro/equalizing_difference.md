# equalizing_difference

- **Series:** lecture-python-intro
- **File:** `lectures/equalizing_difference.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-002` ×5; `qe-writing-005` ×2; `qe-writing-008` ×42, +1 more. |
| Math         | 8/10  | `qe-math-001` ×2. |
| Code         | 7.5/10 | `qe-code-001` ×5. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-006` ×5; `qe-fig-005` ×7; `qe-fig-008` ×8. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 190, 316, 565, 569, 611. *Example:* the closing `):` of `create_edm` at 190 and of `create_edm_π` at 316 is indented three columns short of the visually-aligned arguments above it; the exercise solutions pad assignments and arguments to align them - `gaps_free   = [...]` / `gaps_costly = [...]` at 565-566, `ax.plot(T_arr, gaps_free,   'o-', ...)` at 569-570, `gap_plus  = ...` / `dϕ_dR_fd  = ...` at 611-613 - which PEP8 rules out (multiple spaces before an operator, multiple spaces after a comma) and which the body of the lecture does not do.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 7. *Lines:* 233, 249, 268, 345, 512, 562, 648. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 5. *Lines:* 522, 572, 573, 656, 657. *Example:* axis label `College wage premium $\phi$`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 8. *Lines:* 238, 254, 273, 350, 519, 569, 570, 654. *Example:* plot() without lw=.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 22, 34, 44, 178, 368. *Example:* line 22 is a 38-word sentence carrying Friedman's motive, the dentists/doctors comparison and the entry-barrier alternative at once; line 34 runs 31 words and ends with the redundant "between going to college and not going to college but instead going to work immediately"; line 44 "And doing that will let illustrate how good Python is at doing calculus!" is ungrammatical; line 178 restates line 170 almost verbatim across the section break ("write Python code to compute $\phi$ and plot it as a function of ... its determinants"); and 362-372 spends five sentences re-announcing the calculus section that lines 42-46 already announced in the Overview.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 42. *Lines:* 22, 25, 27, 30, 32, 34, 38, 42, 69, 75, …. *Example:* 3 spaces.

### Medium severity
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 2. *Lines:* 447, 462. *Example:* unicode `γ` inside a math environment.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 38, 244. *Example:* bold used where italic is called for: **Wealth of Nations** at 38 is a book title, and **waiting** at 244 is emphasis ("must rise to compensate a prospective high school student for **waiting** to start receiving income") - neither is a definition, while the genuine definitions **equalizing difference** (130) and **free college** (160) use the same weight.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 25. *Example:* `` {cite} `` in narrative flow: 'of `` {cite} ``'.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 428. *Example:* "Thus, as with our earlier graph, we find that raising $R$ increases the initial college wage premium $\phi$" sits directly under the cells at 417-425, which compute and evaluate $\partial\phi/\partial D$, not $\partial\phi/\partial R$ - the $R$ derivative is not computed until 480 and is correctly discussed at 490, so the reader meets the conclusion 60 lines before its evidence.


## Strengths

- The model is packaged once as a `namedtuple` plus a `create_edm` factory with the economics written into the default comments (181-192), so every comparative-statics cell reduces to one list comprehension over `create_edm(...)` (235, 251, 270, 347) instead of re-deriving $A_h$ and $A_c$.
- Greek parameters in code are Unicode and match the mathematics symbol for symbol - `γ_h`, `γ_c`, `ϕ`, `π`, `ε`, `w_h0` - so a reader can move between the display equations and the cells without a translation table.
- Every comparative static is established twice: graphically at 233-277 and again symbolically with SymPy at 376-490, and each derivative's sign is checked back against the corresponding graph (460, 475, 490).
- The entrepreneur-worker reinterpretation at 279-356 reuses the same indifference equation with a single extra parameter $\pi$, which makes the model's real subject - waiting and risk, not college - visible without new algebra.
- All four exercises are gated `{exercise}` / `{solution-start}` ... `{solution-end}` with `:class: dropdown`, and three of them close the loop numerically against the lecture's own symbolic results (531-535, 616-620, 663-667).

## Recommended actions

1. Fix the conclusion at 428: the cells above it differentiate with respect to $D$, so either state the $D$ result there or move the sentence down to 480-490 where $\partial\phi/\partial R$ is actually computed.
2. Stop the second model from shadowing the first: line 307 rebinds the name `EqDiffModel` and 321 rebinds `compute_gap`, so the 6-field `create_edm` from 184 is unusable from that point on - which is why every exercise has to call `create_edm_π(..., π=1.0)` and explain the workaround in a comment (515, 565-566, 611-612). Give the entrepreneur version its own names, and change the `π=0` default at 315, which makes `compute_gap` divide by zero.
3. Replace the literal Unicode gamma inside the two math spans at 447 and 462 with `\gamma_h` and `\gamma_c` - as written they are the only two math expressions in the lecture that do not render as LaTeX (qe-math-001 x2).
4. Squash the 42 runs of two and three spaces in the prose - they are concentrated in the Overview at 22-46 and in 102-176 (qe-writing-008 x42).
5. Add `mystnb: figure: name/caption` metadata to the 7 plotting cells (233, 249, 268, 345, 512, 562, 648) and lower-case the 5 Title Case axis labels at 522, 572, 573, 656, 657 (qe-fig-005 x7, qe-fig-006 x5); while there, move the three `ax.set_title` calls in the solution cells (523, 574, 658) into captions as well, even though the checker exempts titles inside solutions.
6. Set `lw=2` on the 8 default-width line plots at 238, 254, 273, 350, 519, 569, 570, 654 (qe-fig-008 x8).
7. Tidy the prose: shorten the 38-word opener at 22, delete the calculus preamble at 362-372 that repeats 42-46, un-bold *Wealth of Nations* (38) and *waiting* (244), and lift the `{cite}` at 25 out of the middle of the sentence (qe-ref-001). Also either cite the `eq:wagepremium` label from 158 or drop it - `eq:equalize` is cited at 154, this one never is.
