# hansen_singleton_1983

- **Series:** lecture-python.myst
- **File:** `lectures/hansen_singleton_1983.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-002` ×4; `qe-writing-004` ×1; `qe-writing-001` ×1, +2 more. |
| Math         | 3/10  | `qe-math-010` (proposed) ×42; `qe-math-004` ×143; `qe-math-009` ×2. |
| Code         | 7/10  | `qe-code-002` ×3; `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9.5/10 | `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-004]** — Do not use bold face for matrices or vectors. *Count:* 143. *Lines:* 139, 141, 146, 149, 156, 278, 283, 286, 299, 307, …. *Example:* \mathbf.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 42. *Lines:* 134, 156, 168, 174, 180, 186, 194, 204, 215, 234, …. *Example:* bare expectation `E_0 \sum`.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 22. *Lines:* 43, 45, 49, 53, 55, 61, 63, 65, 1573, 1798, …. *Example:* 3 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 100, 1129, 1331. *Example:* lines 99-101 split a conditional expression across continuation lines at a 9-space indent matching neither the bracket nor a hanging indent (E128) - the same helper as in hansen_singleton_1982.md:85-87; line 1129 leaves trailing whitespace and then continues the expression at an under-indented 12 spaces (E128); and lines 1330-1331 use a backslash continuation with an over-indented second line (E127) where PEP8 asks for parentheses. The slice spacing at 412, 1351, 1352 and 1357 is correct for compound slice expressions and is left alone.
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 3. *Lines:* 1328, 1329, 1331. *Example:* spelled-out `sigma`.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 2. *Lines:* 217, 1216. *Example:* $U$ is the period utility function at 124-134 and 199, and then $U_{i,t} := \log u_{it}$ at 217-222, with $\sigma_U^2$ at 311-314 belonging to the second meaning - so $U(c_t)$ and $U_{i,t}$ are unrelated objects on one letter. Similarly $R_t$ is the log return throughout while $R^2_R$ and $R^2_X$ at 1216-1229 are coefficients of determination subscripted by the same letters, giving expressions like $R_R^2$ whose two R's mean different things.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 1427. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 45, 53, 63, 1819. *Example:* the Overview carries four defects in twenty lines: 'They detect a defects in their model' (45), 'restrictions on a the joint distribution' (53), 'To keep lecture this lecture narrowly focused' (63), and the equity-premium attribution given twice, at 45 and again at 61. At the other end, '## Another approach' (1819-1825) is a two-paragraph section that repeats the hand-off to `` {doc}`hansen_singleton_1982` `` already made at 1794, and line 1788 reads 'departures from bell curve with fatter tails'.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 33. *Example:* mid-sentence 'Critique'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 1193, 1796. *Example:* 1825 lines carry exactly one figure (the residual diagnostics at 1739-1770); every other result is a LaTeX table built by `display_table`. Two sections are pictures waiting to be drawn. '## Predictability and the R-squared restriction' (1193-1281) is about a proportionality - the predictable part of $R_t$ is $-\alpha$ times the predictable part of $X_t$ (`` {eq}`hs83-predictable-return` ``) - and computes `pred_x` and `pred_r` at 1246-1248 without ever plotting one against the other. '## Connection to the equity premium puzzle' (1796-1817) states the Mehra-Prescott trade-off between the 6% premium and the 1% risk-free rate as two numbered lines (1812-1813), where the canonical exhibit is one curve of each against risk aversion with the estimated $-\hat\alpha$ marked.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 1751. *Example:* figsize=.


## Strengths

- The epigraph earns its place: Sargent's 'A rational expectations equilibrium is a likelihood function. Maximize it.' (32-39) is exactly what the lecture then does, and the companion GMM lecture is positioned as the response to its failure.
- The derivation is a fully labelled chain from preferences to likelihood - `hs83-crra`, `hs83-objective`, `hs83-budget`, `hs83-lagrangian`, `hs83-euler`, `hs83-u-def`, `hs83-v-it`, `hs83-cond-mean`, `hs83-x-forecast`, `hs83-restricted`, `hs83-r2` - with the central restriction `` {eq}`hs83-cond-mean` `` cited at 258, 292, 1197 and 1288 rather than restated.
- Before any data appear, the central restriction is interpreted through three special cases - risk neutrality, log utility, risk aversion (264-268) - so the reader knows what $\alpha$ is doing before seeing an estimate of it.
- The likelihood is verified on 50000 observations simulated from the restricted system itself, and reported as a true-versus-estimate table with t-statistics against the true values (992-1042) - not merely 'the estimates look close'.
- The lecture tests its own maintained assumption and reports the failure: Jarque-Bera rejects normality for both residual series (1788-1792), which is precisely the motivation for the GMM companion.
- Estimation code names parameters as the mathematics does - `α_true`, `β_true`, `σ_x_true`, `μ_x_true` (993-1000), `α`, `β`, `σ_x`, `σ_r`, `μ_x` (1238-1248) - and the log-likelihood uses a Cholesky factorisation with `LinAlgError` handling rather than an explicit inverse.

## Recommended actions

1. Strip the bold-face vector notation: 143 `\mathbf{...}` and `\boldsymbol{...}` occurrences (139, 141, 146, 149, 156, 278, 283, 286, 299, 307, ...) become plain letters - by far the largest fix in this lecture, and a mechanical one (qe-math-004).
2. Brace the 33 bare expectation operators - `E_{t-1}[`, `E_0`, `E(` become `\mathbb{E}_{t-1}[` and so on (215, 234, 237, 248, 250, 255, 268, 276, 283, 314, ...) (qe-math-010 (proposed)).
3. Repair the Overview: fix 45, 53 and 63 as quoted above, and delete one of the two equity-premium attributions at 45 and 61.
4. Add the two missing exhibits described above - predictable return against predictable consumption growth in the R-squared section, and the premium/risk-free-rate trade-off against risk aversion in the equity-premium section.
5. Rename either the period utility function $U(\cdot)$ or the log Euler variable $U_{i,t}$ so that one letter does not carry both, and reconsider $R^2_R$ where $R$ is already the log return.
6. Fold '## Another approach' (1819-1825) into the hand-off already made at 1794, and fix 'departures from bell curve' at 1788.
7. Housekeeping: the escaped percent signs at 1812-1813 (`6\%`) render literally outside math - use plain `%` or `$6\%$`; drop `figsize=` at 1751 (qe-fig-001); rename the `sigmas` array at 1329 to `σs`; and sweep the 22 double-space runs (43, 45, 49, 53, 55, 61, 63, 65, 1573, 1798, ...) plus the whitespace-only line at 59.
