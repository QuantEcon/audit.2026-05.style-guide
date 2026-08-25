# lake_model

- **Series:** lecture-python-intro
- **File:** `lectures/lake_model.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-002` ×6; `qe-writing-005` ×2; `qe-writing-003` ×2, +1 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-001` ×8. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-003` ×4; `qe-fig-005` ×3; `qe-fig-007` ×1, +3 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 8. *Lines:* 127, 128, 153, 292, 340, 349, 357, 473. *Example:* the whole body of `plot_time_paths` is indented eight spaces instead of four (292-360); column-alignment padding inside the `np.array` literal (127-128); `x_ts= np.zeros((2, T))` with a space on only one side of `=` (153); a dangling comma in `ax.scatter(..., s=4,)` (340); spaces around `=` in the `dict(arrowstyle = "->")` keyword arguments (349, 357); and `label='u_bar'` where the surrounding labels are LaTeX (473).
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 6. *Lines:* 189, 191, 214, 217, 425, 427. *Example:* six sentences are missing words and have to be re-read to parse: "the fact there is only one inflow source" (189), "The inflow and outflow of labor market system is determined by constant exit rate and entry rate" (191), "Since by intuition if we consider unemployment pool and employment pool as a closed system..." (214, a fragment), "whether the long-run growth rates of $e_t$ and $u_t$ also dominated by $1+b-d$ as labor force" (217, no verb), "as $t$ is large enough" (425, a dangling clause after a display equation) and "the growth of $u_t$ and $e_t$ also dominated by $r(A) = 1+g$" (427, no verb).
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 25. *Example:* H2 Title Case: 'The Lake model' (Lake).

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 171, 315, 470, 552. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 175, 178, 181, 482. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 160, 456, 551. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 343, 351. *Example:* plot() without lw=.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 404, 490. *Example:* the "### Properties" heading at 404 names nothing (properties of what?) and opens by asserting "the column sums of $A$ are $r(A)=1$", which contradicts the result two sections earlier that $r(A) = 1 + b - d$ (269-272); and 490-517 is a second, self-contained derivation of the same convergence result "without the Perron-Frobenius theorem" - 28 lines of diagonalisation algebra tacked onto the end of another section with no heading of its own.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 258, 286. *Example:* the lecture bolds **lake model** at 27 and then nothing else, so the two terms it goes on to define in the body - the dominant eigenvalue ("$r(A)$ can be considered as the dominant eigenvalue in this lecture", 258) and the dominant eigenvector ("we call $\bar{x}$ the dominant eigenvector", 286) - are introduced in plain text.

### Low severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 41. *Example:* static image .png.
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 1. *Lines:* 324. *Example:* spine removal.


## Strengths

- The two labelled equations are both genuinely re-used: `lake_model` (56) is cited at 64 when the system is put in matrix form, and `steady_x` (278) is cited in the exercise solution at 540.
- Every matrix is written with `bmatrix` and every transpose with `^\top` (86, 194, 274, 414) - no `array` environments and no apostrophe transposes anywhere in the file.
- Model parameters use Unicode Greek throughout the code (`λ`, `α` in the `LakeModel` signature and in `lm_high_α`, `lm_low_λ`), matching the notation in the prose exactly.
- The lecture answers the question it poses: 92-96 asks whether long-run outcomes depend on $x_0$, and 369-377 and 427-433 answer it with the set $D$ and the $x_t \to n_t \bar{x}$ result.
- The exercise solution reuses `plot_time_paths` with an `ax=` argument to put the two comparative-statics panels side by side (551-576), rather than duplicating the plotting code.

## Recommended actions

1. Rename the scalar in $D := \{x \in \mathbb{R}^2 : x = \alpha \bar{x} \text{ for some } \alpha > 0\}$ (370, 530): $\alpha$ is already the separation rate in this model, so the definition of $D$ reads as if it depended on the dismissal rate.
2. Fix "the column sums of $A$ are $r(A)=1$" at 406 - the column sums equal $r(A) = 1 + b - d$, which is what makes $\mathbb{1}^\top$ the left eigenvector.
3. Repair the six sentences with missing words listed above (189, 191, 214, 217, 425, 427); the Perron-Frobenius subsection at 212-229 is the hardest-hit passage.
4. Move the four embedded `set_title` calls (175, 178, 181, 482) into mystnb figure captions and add `caption`/`name` metadata to the four un-named figures (160, 290, 456, 551) so the prose can stop saying "the above figure" (373) and "visualised below" (389).
5. Re-indent `plot_time_paths` to four spaces (292-360) and fix the remaining PEP8 items above; also drop the `figsize=` from the four figures (171, 315, 470, 552) unless the tall layout is deliberate.
6. Give the "Properties" section at 404 a descriptive heading, and put the alternative derivation at 490-517 under its own subheading.
7. Lower-case the H2 at 25 to "The lake model", bold the definitions of the dominant eigenvalue (258) and dominant eigenvector (286), fix the `e_o` typo at 96, keep the figure spines at 322-324, and replace the static PNG at 41 with a code-generated diagram.
