# amss3

- **Series:** lecture-dp
- **File:** `lectures/amss3.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-005` ×13; `qe-writing-002` ×5; `qe-writing-003` ×2, +2 more. |
| Math         | 9/10  | `qe-math-013` (proposed) ×1. |
| Code         | 8.5/10 | `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×5; `qe-fig-003` ×3; `qe-fig-008` ×3, +2 more. |
| References   | 7.5/10 | `qe-ref-001` ×5. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 177, 212, 226, 238, 259. *Example:* {figure} without :name:.
- **[qe-ref-001]** — Use correct citation style. *Count:* 5. *Lines:* 40, 60, 231, 301, 398. *Example:* `` {cite} `` in narrative flow: 'of `` {cite} ``'.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 54, 379, 521, 545, 659. *Example:* line 54 reads 'comes as close as possible to providing full spanning in a precise a sense defined by BEGS'; line 379 opens 'Therefor,' for 'Therefore'; line 521 says the formula 'supports full fiscal insurance via fluctuating interest parameters' where 'interest rates' is meant; line 545's comment reads '# Initial guess of τ (to displays calcs along the way)'. Line 659 states 'Note that 0.2 is the initial value for $\tau$ in the root-finding algorithm' immediately after line 652 passes `.1` - and the same routine is called with `.5` at 667, `0.05` at 699 and `.5` at 679, each time under a comment saying the result is 'Very sensitive to initial value', so the one number the reader is told is the one number that is wrong.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 13. *Lines:* 54, 60, 97, 232, 299, 379, 383, 389, 390, 394, …. *Example:* bold carrying emphasis: **as close as possible** (54), **three** (97), **before** (232), **effective** twice at 299 where the terms being defined are 'effective government deficit' and 'effective government debt' - so the bold lands on the adjective and not the term, **in advance** (379), **confirms** (383), **first** / **then** (389, 390), **without** (394), **minus** / **plus** (423), **surplus** (454), **constant** (519). Line 60 uses '**Warning:**' as a bold label inside a `{note}`, where the admonition's own title would do. The real definitional bolds - **fiscal risks** (311), **fiscal-risk minimization problem** (384), **effective return** / **effective government deficit** (443-444) - are the minority.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 69. *Lines:* 29, 34, 35, 37, 39, 42, 44, 46, 50, 52, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 202, 587, 688, 694. *Example:* line 202 uses `id` as a loop variable, shadowing the builtin. The `div` expression at 587-589 packs three spacing faults into one statement - a backslash continuation inside parentheses where PEP8 asks for implicit continuation, two spaces before that backslash, and two spaces after each `+` on the continuation lines - and it is repeated verbatim at 688-690. Line 694 writes `B_star/div` unspaced while line 709 writes `1 / (1 + u.β**2 * variance(R_star, s))` spaced.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 200, 241. *Example:* figsize=.
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 3. *Lines:* 212, 226, 259. *Example:* static image .png.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 204, 249, 250. *Example:* .set(title=.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 203, 244, 246. *Example:* plot() without lw=.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 676, 529. *Example:* the Execution section does not follow the seven steps it is executing. Its headings run Step 1 (538), Step 2 (560), Step 3 (636), Step 4 (662), Step 6 (676) - Step 5 and Step 7 have no headings at all, and the contents are shifted: `min_J` at 665 is what Step 5 describes ('put ${\rm var}(J({\mathcal B}))$ into a Python function minimizer', 483-484) but sits under 'Step 4', while the `minimize` call at 679 sits under 'Step 6' and Step 7's divisor and $\hat b$ (688-696) sit under it too, unlabelled. A reader working the description at 409-513 against the code cannot line them up. Separately, lines 528-530 are broken: a sentence begins in lower case mid-thought and the next line opens with a stray colon ('so while the approximation circumvents the chicken and egg problem that surrounds / : the much better approximation...'), which MyST will render as a definition-list fragment.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 226, 679. *Example:* the lecture's central figure exists only as a bitmap and its own computations are never drawn onto it. The histogram at 226 - the ergodic distribution of par debt with three vertical lines, described in detail at 229-232 - has no generating code anywhere in the file, so a reader cannot see how the sample mean, ${\mathcal B}^*/E u_c$ and the BEGS $\hat b$ were placed, nor move them. Then the Execution section computes `B_star` (679), `B_hat` (694) and `rate` (709) and prints them as bare scalars: ${\rm var}(J({\mathcal B}))$ against ${\mathcal B}$ is never plotted even though `min_J` at 665 evaluates exactly that function, and $\hat b$ is never overlaid on the histogram it is said at 531 to be the red line of. Two figures the code is already one line away from producing would replace the entire 'stare and digest' instruction at 400-401.

### Low severity
- **[qe-math-013 (proposed)]** — Reference equations via `` {eq}`label` ``. *Count:* 1. *Lines:* 422. *Example:* manual reference 'equation (42)'.


## Strengths

- The lecture corrects its source and says exactly where: a `{note}` up front warns that 'Key equations in `` {cite}`BEGS1` `` section III.D carry typos that we correct below' (59-61), then two 'typo alert' paragraphs identify the sign error in BEGS equation (42) at 422-425 and the sign on the left side of equation (46) at 456-459, each stating that the displayed version is the corrected one.
- The reason this lecture exists is stated as a structural fact before any computation: two Markov states allow endogenous interest-rate fluctuations to deliver full spanning asymptotically, three do not (44-50), so the ergodic distribution of par debt is a point mass there and nontrivial here - the reader knows what to look for in the histogram before seeing it.
- The chicken-and-egg problem is named, isolated and resolved (374-395): the variance-minimisation characterisation `` {eq}`eq_criterion_fiscal_1` `` needs the ergodic distribution to evaluate, so its role is confirmation, not prediction; the separate BEGS approximation is the one computable in advance. Lines 389-390 point back to how amss2 used them in that order.
- The 'Note about code' at 566-576 explains why `s = 0` is hard-coded throughout - $\pi$ has identical rows in the IID case, so one row suffices - which is exactly the sort of detail that otherwise reads as a bug to anyone adapting the code to a non-IID chain.
- Step 7's discussion at 515-532 is careful about what transfers from amss2 and what does not: there $\hat b$ described a constant par value that is the limit of debt; here it approximates the mean of a distribution around which par debt keeps fluctuating - and line 532 concedes the approximation is 'fairly accurate but not perfect'.
- The moment helpers at 129-140 take the conditioning state as an explicit third argument (`mean(x, s)`, `variance(x, s)`, `covariance(x, y, s)`), an improvement on the versions in amss2 (666-677) which closed over a module-level `s` - so the three-state generalisation cannot silently pick up the wrong row of $\pi$.

## Recommended actions

1. Fix the step numbering in the Execution section (534-716) so it matches the description at 407-533: add the missing '#### Step 5' and '#### Step 7' headings, and move `min_J` (665) under Step 5 and the `minimize` call (679) under Step 5's minimisation rather than Step 6. As it stands two of seven steps have no heading and three cells sit under the wrong one.
2. Resolve the duplicated figures. The `{figure}` PNGs at 212-214 and 259-261 sit immediately after code cells (177-210, 238-257) that draw the same panels, so the built page shows each figure twice - once executed, once as a bitmap. Either mark the code cells as non-executing or drop the PNGs. The histogram at 226-227 is the opposite case and the more important one: it has no generating code at all, and it is the figure the whole lecture is about (qe-fig-002 x3).
3. Clear the 69 double spaces (qe-writing-008) and fix the broken markdown at 528-530, where a stray leading colon turns the sentence into a definition-list fragment.
4. Add the missing imports to the cell at 75-78: the lecture uses `np.` (131, 139, 179, 181-183, 552, 586, 714) and `root` (552, 557, 586, 652, 667, 699, 714) without importing either. Both arrive only because one of the `:load:`ed files at 153, 160 or 167 happens to import them, which hides a dependency and makes the cells non-portable.
5. Switch the 13 emphasis bolds to italic; at 299 move the bold from '**effective**' onto the whole terms being defined ('**effective government deficit**', '**effective government debt**'), matching 443-444.
6. Finish the figure cells: mystnb `name`/`caption` metadata on the 5 figure sites (177, 212, 226, 238, 259), the 3 `ax.set(title=...)` calls moved into captions (204, 249, 250), the hand-set `figsize=` dropped (200, 241) and `lw=2` added (203, 244, 246) (qe-fig-005 x5, qe-fig-003 x3, qe-fig-008 x3, qe-fig-001 x2).
7. Fix the prose slips - 'in a precise a sense' (54), 'Therefor' (379), 'interest parameters' (521), 'to displays calcs' (545) - and correct line 659, which names 0.2 as the root-finder's initial value where the code at 652 passes 0.1. Also write `\mathrm`` {div}` rather than bare ` ``div` in the display at 506, which currently renders as a product of three italic letters, and replace the deprecated `{\rm cov}` / `{\rm var}` / `{\rm argmin}` / `{\rm rate}` forms (324, 337, 361, 481, 487, 494) with `\operatorname`.
