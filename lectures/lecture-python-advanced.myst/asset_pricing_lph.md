# asset_pricing_lph

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/asset_pricing_lph.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 6.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-005` ×8; `qe-writing-002` ×5; `qe-writing-004` ×2, +5 more. |
| Math         | 3/10  | `qe-math-010` (proposed) ×26; `qe-math-006` ×2; `qe-math-002` ×2, +2 more. |
| Code         | 5.5/10 | `qe-code-002` ×13; `qe-code-001` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-003` ×1; `qe-fig-005` ×1; `qe-fig-008` ×3. |
| References   | 8.5/10 | `qe-ref-001` ×4. |
| Links        | 7.5/10 | `qe-link-001` ×3; `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 358, 360, 366, 367, 864, 866. *Example:* the rule's two explicit examples are both broken, in opposite directions: 358 and 360 write `alpha + beta*x` and `alpha - beta*x` with no spaces around the multiplication, while 864 and 866 write `(ERf + ξ) ** 2 + λ ** 2 + σf ** 2` with spaces around every `**`, which the rule says to write as `a**b`; 366-367 write `1/Em` and `sigmam/Em` unspaced. The two one-line helpers at 357 and 359 are also separated by no blank line at all (E302) and are named `y` and `z`, which says nothing about what they compute.
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 13. *Lines:* 357, 358, 359, 360, 367, 373, 374. *Example:* spelled-out `alpha`.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 2. *Lines:* 508. *Example:* \prime transpose.
- **[qe-math-006]** — Use aligned environment correctly for PDF compatibility. *Count:* 2. *Lines:* 684, 713. *Example:* bare \begin{align*} display block; the corpus convention is $$ … \begin{aligned} … $$.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 26. *Lines:* 118, 144, 266, 307, 394, 414, 470, 477, 633, 640, …. *Example:* bare expectation `E(`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 22, 111, 224, 421, 575. *Example:* 22-23 opens the lecture with a 45-word sentence that defines three symbols inside its own subordinate clauses; 111 is 42 words ("refers to the fact that interesting restrictions can be deduced by recognizing that ... and then using that fact to rearrange ..."); 224-225 duplicates its own noun phrase - "For a constant relative risk aversion (CRRA) utility function $U(C) = ...$ utility function $U'(C) = C^{-\gamma}$"; 421 is a 41-word sentence with a parenthetical gloss that restates the clause before it; and 575-576 is 33 words and ungrammatical ("Our basic tools are random number generator that we shall use to ...").
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 8. *Lines:* 84, 192, 210, 271, 457, 464, 560, 679. *Example:* bold carries emphasis rather than definition throughout - **positively**/**lower**/**negatively**/**higher** (192-193), **perfectly** (197), **high**/**low** eight times over (271-279), **not** (397, 467), **exact**/**residual** (457), **orthogonal to** (560), **estimate**/**choose** (679), **linear** (834) - and 464 sets an entire sentence in bold. The emphasis markup is also not consistent with itself: 84 and 87 use `__law of one price__` and `__absence of an arbitrage__` while every other term uses `**`, and 212 and 787 use `_representative consumer_` and `_true_` where the rest of the file would use `*`. Bold is separately used for block labels that want a directive: **Example** (210), **Testing strategies:** (538), **Step 1:**/**Step 2:** (545, 550), **Direct Problem:** (725), **Inverse Problem:** (773).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 76. *Lines:* 22, 23, 25, 35, 39, 44, 51, 57, 63, 83, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 383. *Example:* plt.title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 380, 381, 387. *Example:* plot() without lw=.
- **[qe-link-001]** — Use markdown style links for lectures in same lecture series. *Count:* 3. *Lines:* 57, 59, 93. *Example:* full URL to own series (python-advanced.quantecon.org).
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 96. *Example:* raw link to python.quantecon.org.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 2. *Lines:* 174, 456. *Example:* $\beta$ carries two different meanings that meet inside the same bullet: it is the intertemporal discount factor at 218, 221 and 508, and the regression coefficient $\beta_{i,m}$, $\beta_{i,a}$, $\beta_{i,R^{mv}}$ at 174, 185, 473, 488 and 492 - and 508 uses both readings in one line ("specifies the factor to be $m_{t+1} = \beta \frac{u'(c_{t+1})}{u'(c_t)}$" in a passage about $\beta_{i,j}$ exposures). Separately, the scalar $a$ names three unrelated objects: the slope of the affine frontier relation at 456-457, one of four scalars at 462, and the SDF intercept at 705-708 and 852.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 1. *Lines:* 241. *Example:* decorated distribution `{\mathcal N}`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 4. *Lines:* 28, 83, 105. *Example:* {cite} in narrative flow: 'of {cite}`'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 105, 457. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 688, 701, 769. *Example:* exercise `apl_ex3` opens at 672 and does not close until 718, and at 701 a bold "**More Exercises**" heading starts a *second* question inside it - find the scalars $a, b$ such that $m_t = a + bR^m_t$ - which is then posed again as exercise `apl_ex4` at 830-838, so one exercise contains the next one's problem; the parameter list at 684-699 specifies $\lambda = 0.04$ while the solution's code at 734 sets `λ = 0.08`, so the simulation does not use the stated parameters; and 769-771 is an empty code cell holding only the comment `# Code for the inverse problem`, placed *before* the "**Inverse Problem:**" heading at 773 that introduces the section it belongs to.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 725, 773. *Example:* mid-sentence 'Problem'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 414, 818. *Example:* the figure at 352-390 is one line segment short of the text it illustrates: 414-419 describes "the length of a horizontal line from the point $\sigma(R^j), E(R^j) = .05, 1.015$ to the frontier" and gives its formula, and the plot draws the point (387) but not that segment, so the quantity the section is about is invisible. Second, the exercises end by printing `βi_hat, σi_hat` (818) beside `βi, σi` (822) and then asking the reader at 825 "How close did your estimates come to the parameters we specified?" - a scatter of estimated against true betas with a 45-degree line answers that question at a glance, and the lecture already has matplotlib imported.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 352. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 747. *Example:* i.i.d..


## Strengths

- The whole lecture is built from one equation and says so: $E m R^i = 1$ is labelled `eq:EMR1` at 66 and then genuinely cited at 83, 102, 133, 147 and 297 as each result is derived from it, and the derivation chain `eq:EMR2` to `eq:EMR3` to `eq:ERbetarep` to `eq:EMR5` to `eq:ERM6` is fully cross-referenced.
- The mean-variance frontier is not just stated - the Cauchy-Schwarz step is given an intuition a reader can hold (299: "an $R^2$ in any regression has to be less than or equal to 1"), and 301 heads off the notation clash by warning that this $R^2$ is a coefficient of determination and not a return.
- The two `underbrace` displays at 174 and 557 label every term in place - regression coefficient, price of risk, regressor, pricing errors, least squares orthogonality condition - which is a good use of math typography to teach the structure of an estimator.
- The frontier figure is calibrated rather than schematic: 350 sets $\sigma(m) = .25$ and $Em = .99$ and says these are "roughly consistent with what many studies calibrate from quarterly US data", so the picture has a scale.
- The exercises are properly gated with `{exercise-start}` / `{solution-start}` and `:class: dropdown`, and they run the direct problem and the inverse problem on the same simulated panel so the estimates can be compared against the parameters that generated them.

## Recommended actions

1. Delete the developer note left in the published code at 732 - `σf = 0.00 # Zejin: Hi tom, here is where you manipulate σf` - and remove the empty cell at 769-771 and the two stray `+++` cell markers at 480 and 536.
2. Reconcile the exercise with its solution: 688 states $\lambda = 0.04$ and 734 sets `λ = 0.08`; and split exercise `apl_ex3` (672-718) so the "**More Exercises**" question at 701-716 is not sitting inside it, given that `apl_ex4` at 830 asks it again.
3. Write the expectation and moment operators as the guide asks - $\mathbb{E}$ for the 26 bare `E`/`E(` uses (118, 144, 266, 307, 394, 414, 470, 477, 633, 640 and 16 more) and `\operatorname{cov}` / `\operatorname{var}` for the bare `Cov(` and `Var(` at 666 (qe-math-010 (proposed), proposed, 26 occurrences - the largest single item here).
4. Wrap the two bare `\begin{align*}` blocks at 684-699 and 713-716 in `$$ ... \begin{aligned} ... $$` (qe-math-006 ×2, a PDF build risk), and replace the `\left\{\begin{array}{ll}` construct at 342-345 with `\begin{cases}`.
5. Fix the broken math and typos: the unbalanced bracket and missing square in 266 (`E(m) [ \exp(\sigma_c^2 \gamma^2) - 1) ]`), the unbalanced paren in 394 (`$( \sigma(R^i), E(R^i)$`), "twice-diffential" (222), "per capital consumption" (243), "importnt" (521), and "Cauchy-Schwartz" at 46 and 299 against "Cauchy-Schwarz" at 297.
6. Rename the spelled-out Greek in code - `alpha`, `beta`, `sigmam`, `Em` at 357-374 - to the Unicode letters the rest of the lecture already uses (`β_hat`, `σ_hat`, `ξ`, `λ`) so the two halves match (qe-code-002 ×13); and convert the four raw quantecon URLs at 57, 59, 93 and 96 to `{doc}` references (qe-link-001 ×3, qe-link-002 ×1).
7. Add the horizontal segment described at 414-419 to the frontier figure, move `plt.title` at 383 into a figure caption with `mystnb: figure: caption/name` metadata, set `lw=2` at 380, 381 and 387, convert the bold emphases listed above to italic, and strip the 76 runs of double spaces.
