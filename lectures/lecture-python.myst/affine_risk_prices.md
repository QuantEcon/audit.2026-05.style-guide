# affine_risk_prices

- **Series:** lecture-python.myst
- **File:** `lectures/affine_risk_prices.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-001` ×2; `qe-writing-005` ×3; `qe-writing-003` ×2, +4 more. |
| Math         | 4/10  | `qe-math-010` (proposed) ×3; `qe-math-011` (proposed) ×9; `qe-math-003` ×2. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-006` ×16; `qe-fig-004` ×4; `qe-fig-001` ×5. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 581, 705, 798, 980, 1343. *Example:* figsize=.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 16. *Lines:* 610, 611, 620, 712, 713, 807, 808, 821, 822, 991, …. *Example:* axis label `Maturity (quarters)`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 3. *Lines:* 234, 238, 869. *Example:* non-blackboard `\text{Var}`.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 9. *Lines:* 110, 222, 231, 234, 331, 454, 1041, 1049, 1083. *Example:* decorated distribution `\mathcal{N}`.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 520, 552, 1347. *Example:* twelve assignment lines pad with multiple spaces before `=` to line up columns (552-558, 577-578, 762, 763, 765), which PEP8 names specifically as something not to do; three continuation blocks are indented to a column that matches neither the opening bracket nor a hanging indent - 521-522 sit at column 24 under a paren opened at 20, 764 and 770 sit one space past their opening bracket, and 1002 and 1004 likewise; and 1348-1349 indent the `label=` continuation to column 10 under a paren opened at column 23.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 4. *Lines:* 567, 782, 958, 1324. *Example:* caption of 7 words.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 2. *Lines:* 731, 1303. *Example:* pmatrix environment.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 652, 680. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 848, 1295, 1402. *Example:* the same result is stated three times in eight lines: the display at 848, then "The term premium equals the inner product of the bond's shock exposure $\bar B_n^\top C$ with the risk price vector $\lambda_t$" (851-852), then "Because the term premium equals $\bar B_n^\top C \lambda_t$, its sign depends on the *current* risk-price vector" (854-855). Line 1295 is a 34-word sentence introducing three separate processes at once, and the list item at 1402-1404 runs to 40 words with a parenthetical cross-reference inside it.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 859, 875. *Example:* the term-premium argument at 854-878 and the figure that follows it disagree. Line 859 says "consider a state where $C\lambda_t$ is negative componentwise (for example, $z_t = 0$ in our calibration below)", but the figure at 958-1027 plots term premiums at $z = (-3, 2)$ and $z = (3, -2)$ - the $z_t = 0$ case appears only as the right-hand decomposition panel, so the promised example is never the one shown. Worse, lines 875-878 say the sign flip and negative long-maturity premiums occur in "the low-rate regime of our two-state calibration", and line 1029 reads the resulting figure the other way round: "the term premium is positive at all maturities in the low-rate state, but becomes negative at longer maturities in the high-rate state".
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 69, 91, 1400. *Example:* structural list labels are set in italic in one place and bold in another for exactly the same job: the four "Key applications" at 69-74 use italic (*Pricing risky assets*, *Affine term structure models*, *Risk-neutral probabilities*, *Distorted beliefs*), the two model components at 91 and 116 use italic (*Component 1*, *Component 2*), and the four "Key features" at 1400-1409 use bold (**Analytical tractability:**, **Empirical flexibility:**, **Multiple risks:**, **Belief distortions:**). None of the ten is a defined term or an emphasised word, and the lecture's genuine definitions - roughly twenty of them, from **short rate** at 113 to **subjective conditional distribution** at 1206 - are all correctly bolded.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 4. *Lines:* 51, 54, 653, 680. *Example:* 2 spaces.

### Low severity
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 63. *Example:* `` {cite} `` in narrative flow: 'and `` {cite} ``'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 1068. *Example:* "Risk-neutral probabilities" (1031-1167) is the one section built on an inherently visual operation - multiplying a conditional density by a likelihood ratio to shift its mean from $\mu + \phi z_t$ to $\mu - C\lambda_0 + (\phi - C\lambda_z) z_t$ (1068-1086) - and it has no figure; two overlaid normal densities, or the two conditional means as a function of $z_t$, would show the twist that the whole section describes in words. What the section does produce is a four-row printed table of Monte Carlo versus analytic bond prices (1156-1163), which validates the algebra but does not illustrate the measure change.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 110. *Example:* i.i.d..


## Strengths

- Every non-trivial derivation is set as an exercise with a full solution behind a dropdown - the SDF moments (191-258), the excess-return formula (307-342), the Riccati equations (413-480), the long-run yield (633-687) and the term premium (880-954) - so the algebra is available without interrupting the argument for a reader who takes it on trust.
- The Riccati recursion is checked against a Monte Carlo simulation under the risk-neutral measure (1134-1163), and the check is reported as pricing errors in basis points at four maturities rather than as a pass/fail.
- `create_affine_model` precomputes the risk-neutral parameters `φ_rn=φ - C @ λ_z` and `μ_rn=μ - C @ λ_0` at construction (155), so the change of measure introduced 900 lines later at 1079 is already the object the bond-pricing code uses.
- Both yield-curve figures carry a second x-axis in years above the quarters axis (615-620, 826-831), which is the right courtesy for a term-structure plot, and every figure has `mystnb: figure: caption/name` metadata.
- The distorted-beliefs section derives the identification problem exactly - the econometrician's $\lambda_t$ is $\lambda^\star_t + \kappa_t$ (1286-1287) - and then plots the two term-premium curves with the distortion shaded between them (1345-1352), so the confounding is visible and not just asserted.

## Recommended actions

1. Lower-case the sixteen axis labels (610, 611, 620, 712, 713, 807, 808, 821, 822, 991, 992, 1013, 1014, 1354, 1355, 1367) - `Maturity (quarters)`, `Yield (% per annum)`, `Short rate (% p.a.)`, `Term premium (% p.a.)` (qe-fig-006, 16 occurrences, the largest mechanical item here).
2. Replace the nine `\mathcal{N}` distribution names with plain `N` (110, 222, 231, 234, 331, 454, 1041, 1049, 1083) and brace the `\text{Var}`/`\text`` {std}`/` ``\text{Cov}` operators as `\mathbb{V}` where they are variances (234, 238, 869) (qe-math-011 (proposed) and qe-math-010 (proposed), both proposed).
3. Reconcile the term-premium narrative with its figure: fix the low-rate/high-rate assignment that 875-878 and 1029 state in opposite directions, and either plot the $z_t = 0$ state that 859 points at or point at a state that is plotted.
4. Convert the two `pmatrix` matrix displays at 731 and 1303 to `bmatrix` (qe-math-003, 2 occurrences) and drop the five `figsize=` overrides at 581, 705, 798, 980 and 1343 (qe-fig-001, 5 occurrences).
5. Pick one convention for list labels - bold or italic - and use it in both the "Key applications" list at 69-74 and the "Key features" list at 1400-1409.
6. Shorten the four seven-word-plus captions at 567, 782, 958 and 1324 (qe-fig-004, 4 occurrences), set `lw=2` on the two plot calls at 594 and 805 (qe-fig-008, 2 occurrences), and give the y-axis label at 1367 a single-symbol name - `$\hat{tp}/tp^\star$` renders as products of italic $t$ and $p$.
7. Sweep the small items: strip the multi-space `=` alignment at 552-558, 577-578 and 762-765 and fix the four mis-indented continuation blocks; write "IID" at 110 (qe-writing-009 (proposed)); move the mid-narrative `{cite}` at 63 (qe-ref-001); split the two-sentence paragraphs at 652 and 680 (qe-writing-001); and collapse the double spaces at 51, 54, 653 and 680 (qe-writing-008).
