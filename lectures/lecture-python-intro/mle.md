# mle

- **Series:** lecture-python-intro
- **File:** `lectures/mle.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-004` ×2; `qe-writing-005` ×3; `qe-writing-003` ×2, +2 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7/10  | `qe-code-001` ×14. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-005` ×8. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 14. *Lines:* 97, 254, 255, 258, 325, 345, 374, 385, 404, 407, …. *Example:* spaces around `=` in keyword arguments, which PEP8 rules out: `scale = exp(μ_hat)` (254, 404), `pareto(b = b_hat, scale = xm_hat)` (325, 428), `expon(scale = 1/λ_hat)` (484), `bins= 500` (433); missing space after commas in `np.linspace(0,50,10000)` (255), `set_xlim(-1,20)` (258), `set_ylim(0,1.75)` (345), `set_xlim(0,50)` (385, 407), `set_ylim(0,0.65)` (432); and whitespace before a closing bracket plus a comment with no space after the hash in `df.loc[df['n_wealth'] > 1 ]   #restrcting data...` (97, repeated at 374).
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 105, 170, 253, 342, 383, 399, 424, 505. *Example:* code-cell figure without mystnb figure metadata.

### Medium severity
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 214, 442. *Example:* line 214 drops into the abbreviation "wrt" in the one sentence that sets up the two derivations that follow; and 442-445 restates 359-361 almost word for word ("there is no 'best' distribution --- each choice is an assumption") thirty lines after the original.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 363, 440. *Example:* line 363 states "The plots above suggested that the lognormal distribution is optimal" four lines after 359 states "There is no 'best' distribution", and two sections later the lognormal is rejected for the tail (414); and the H3 at 440, "So what is the best distribution?", repeats the text of the H2 at 357 that contains it, so the table of contents shows the same question nested inside itself.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 85, 298. *Example:* mid-sentence 'Consumer'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 146, 191, 202. *Example:* the lecture contains no bold and no italic anywhere, so all three terms it defines are introduced in plain text with only an external hyperlink to carry the weight: maximum likelihood estimation (146), the likelihood function (191) and the log likelihood function (202).

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 88. *Example:* 2 spaces.


## Strengths

- The lecture is framed around a question a policymaker would actually ask - how much revenue does this wealth tax raise - and the answer changes by an order of magnitude when the distributional assumption changes (330-336), which makes the point about assumptions land.
- Density notation follows the lowercase convention throughout: $f$ for the density (129, 186), $\ell$ for the log likelihood, $L$ for the likelihood, and hatted symbols for every estimate (proposed qe-math-015 (proposed) satisfied).
- The MLE formulas are derived rather than quoted - the log likelihood is written out (204-212) and both first-order conditions are solved (218-235) before any code appears.
- `total_revenue(dist)` (275-278) takes any frozen scipy distribution, so the lognormal, Pareto and exponential assumptions are compared through one identical code path.
- The tail analysis (367-438) is the right follow-up to the whole-sample fit: the same two distributions are re-estimated above a threshold, and the conclusion reverses.

## Recommended actions

1. Fix the lognormal density at 186-188: the squaring is outside the `\exp`, so the formula as typeset is $\exp(\cdot)^2$ rather than $\exp((\ln x - \mu)^2 / 2\sigma^2)$, and the minus-one-half is applied to an unsquared term.
2. Replace `\delta` with `\partial` in the two first-order conditions (219, 228) - these are partial derivatives, and `\delta` reads as a variation.
3. Add `mystnb: figure: caption/name` metadata to all eight figures (105, 170, 253, 342, 383, 399, 424, 505) - not one figure in the lecture can currently be cross-referenced, and the prose refers to them as "The plots above" (363) and "as we did" (447).
4. Escape the currency signs at 369 (`\$500,000`) - as written the unescaped `$` opens a math span, the same way the histogram label at 110 correctly writes `r"unit: $\$100,000$"`.
5. Run the code cells through a PEP8 formatter for the 14 spacing items above, and fix the comment typo "restrcting" at 97.
6. Bold the three defined terms at their point of definition, cut the restatement at 442-445, and give the H3 at 440 a distinct heading.
7. Put the two derivations at 218-223 and 227-235 in `aligned` environments - as written they use bare `\\` line breaks inside `$$`, and settle the `\hat{x_m}` versus `\hat{x}_m` inconsistency at 304 and 306.
