# greek_square

- **Series:** lecture-python-intro
- **File:** `lectures/greek_square.md`
- **Audit date:** 2026-05-28
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 6.7 / 10
- **Priority:** MEDIUM

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 8/10  | H1 Title Case OK; H2 sentence case mostly. |
| Math         | 6/10  | `{\bf R}^2` for reals (M5 violation); `{\mathcal I}` for integers (W8); bmatrix used. |
| Code         | 8/10  | Unicode Greek (`λ`, `η`) used (qe-code-002 OK); standard Anaconda imports. |
| JAX          | out of scope | — |
| Figures      | 5/10  | `figsize=` on lines 531, 690; 2 `ax.set_title(r'$\frac{y_t}{y_{t-1}}$ after Muting $\lambda_1$', ...)` outside exercise context (lines 699, 710) — Title Case "Muting". |
| References   | 7/10  | `{cite}` used; "Chapter 24 of {cite}\`russell2004history\`" (line 19) is in-text. |
| Links        | 9/10  | `{doc}` links used (5 occurrences). |
| Admonitions  | 9/10  | Solution gated, dropdown, exercise-linked (qe-admon-001, -002, -005 OK). |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **M5** — `{\bf R}^2` (lines 317, 321, 323, 329) uses bold for set notation; should be `\mathbb{R}^2` or plain `R^2`. *Count:* 4 occurrences.
- **W8** — `{\mathcal I}` (lines 188, 190, 192, 194) used for integers; simpler `\mathbb{Z}_{>1}` or `I` would suffice.
- **[qe-fig-003]** — `axs[0].set_title(...)` / `axs[1].set_title(...)` on lines 699, 710 outside exercise context. *Count:* 2 occurrences.
- **[qe-ref-001]** — In-text citation should use `{cite:t}`. *Example:* `lectures/greek_square.md:19` ("Chapter 24 of {cite}\`russell2004history\`"). *Count:* 1 occurrence.

### Low severity
- **W7** — "Ancient Greeks" capitalized — debatable.
- **W1** — Some short two-sentence paragraphs.
- **[qe-fig-001]** — `figsize=` on lines 531, 690. *Count:* 2 occurrences.
- **[qe-fig-005]** — No figures use `{figure}` directive with `:name:`.

## Strengths
- Equation labels and references throughout.
- bmatrix used for matrices.
- Italic for emphasis (*solves*, *general*, *invariant subspace*, *perfect square*).
- Unicode Greek used in code.
- `{doc}` cross-references used.

## Recommended actions
1. Replace `{\bf R}^2` with `\mathbb R^2`.
2. Simplify `{\mathcal I}` notation per W8.
3. Move `set_title` calls (lines 699, 710) to mystnb metadata.
4. Convert in-text citation on line 19 to `{cite:t}` form.
5. Remove `figsize=` overrides.
