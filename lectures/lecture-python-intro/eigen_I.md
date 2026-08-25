# eigen_I

- **Series:** lecture-python-intro
- **File:** `lectures/eigen_I.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3.5/10 | `qe-writing-004` ×5; `qe-writing-005` ×2; `qe-writing-003` ×2, +3 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-001` ×5. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 3.5/10 | `qe-fig-003` ×7; `qe-fig-007` ×6; `qe-fig-005` ×7, +3 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 226, 231, 576, 1136, 1281. *Example:* `ax[0].set_title("points $x_1, x_2, \cdots, x_k$")` at 226 and 231 puts `\cdots` in a plain (non-raw) string, an invalid escape sequence (pycodestyle W605) - the identical titles at 543, 547 and 551 are correctly written `r"..."`; `grid_composition_transform(B,A)` at 576 drops the space after the comma that the parallel call at 568 has; `plt.quiver(*origin, - eigenvectors[0], - eigenvectors[1], ...)` at 1136-1137 puts a space after the unary minus; `ax.quiver(x, y, u_imag, u_real-x, v_real-y, v_imag-u_imag, ...)` at 1281 omits the spaces around the binary minus that the same expression has at 1125.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 6. *Lines:* 212, 238, 530, 741, 1032, 1181. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 7. *Lines:* 226, 231, 266, 278, 543, 547, 551. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 7. *Lines:* 129, 730, 996, 1041, 1114, 1179, 1248. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-007]** — Keep figure box and spines. *Count:* 6. *Lines:* 138, 221, 247, 539, 616, 746. *Example:* spine removal.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 5. *Lines:* 34, 918, 925, 939, 965. *Example:* mid-sentence 'Series'.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 858. *Example:* H2 Title Case: 'The Neumann Series Lemma' (Series, Lemma).

### Medium severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 263, 274, 1036. *Example:* plot() without lw=.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 493, 1112, 1156. *Example:* line 493 "This means first apply transformation $B$ and then transformation $A$" restates 486-487 word for word in meaning; line 1112 "(This is a more advanced topic in linear algebra, please step ahead if you are comfortable with the math.)" reads as the opposite of what is meant - the reader who is comfortable is the one who should stay; line 1156 repeats 1154 with "Specifically" and adds only the superlative.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 699, 854. *Example:* line 699 promises "We now discuss the property of A that determines this behavior" after the three spiral-in / ellipse / spiral-out experiments, but the eigenvalue sections never return to those three matrices; line 854 defers with "This is discussed further later" and gives no pointer - the connection is in fact only made inside exercise `eig1_ex3` (1163-1242), so the main narrative closes without answering the question it posed.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 343, 720. *Example:* definitions set in italics instead of bold: line 343 "is called a _rotation matrix_" and line 720 "we say that $\lambda$ is an *eigenvalue* of $A$, and $v$ is the corresponding *eigenvector*" - these are the two central definitions of the lecture, and the lecture bolds correctly elsewhere (**spectral radius** at 913).

### Low severity
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 1. *Lines:* 1299. *Example:* axis label `Im`.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 858. *Example:* the Neumann Series Lemma section (858-965) is the only substantive section with no figure, although its whole content is the condition $r(A) < 1$ - the natural picture, eigenvalues plotted inside the unit disk, or the truncated sum converging to $(I-A)^{-1}$, is absent even though the lecture gives every other concept a panel.


## Strengths

- The transformation taxonomy is built on one reusable pair of functions, `grid_transform` and `circle_transform` (194-281), then applied unchanged to scaling, shearing, rotation and permutation - so the four sections are directly comparable panel for panel.
- Non-commutativity is argued twice over: numerically at 404-484, where `\underbrace` / `\overbrace` labels tie every `bmatrix` to $A$, $B$, $x$ and $Bx$, and then visually with the shear-then-rotate / rotate-then-shear grids at 567 and 575.
- Both labelled equations are cited: `gp_sum` (873) at 905 and `neumann_eqn` (895) at 902 - no orphan labels, and no manual "equation (1)" references anywhere.
- `plot_series` carries its own `(plot_series)=` anchor at 600 and is reached by `{ref}`Previously <plot_series>`` from exercise `eig1_ex3` at 1166, so the exercise points back at the exact cell it builds on.
- Every matrix is written with `bmatrix` rather than `array`, and Greek names in code are Unicode (`θ` at 249, 348, 618), so qe-math-003 and qe-code-002 are clean throughout.

## Recommended actions

1. Move the 7 `ax.set_title(...)` calls (226, 231, 266, 278, 543, 547, 551) into mystnb figure captions and add `mystnb: figure: name/caption` metadata to the 7 plotting cells at 129, 730, 996, 1041, 1114, 1179 and 1248 - these two fixes travel together and are the largest item in the lecture (qe-fig-003 x7, qe-fig-005 x7).
2. Lower-case the theorem name in narrative text and headings: "Neumann Series Lemma" -> "Neumann series lemma" at 34, 858, 918, 925, 939 and 965 (qe-writing-004 x5, qe-writing-006 x1).
3. Bold the two definitions instead of italicising them - **rotation matrix** at 343 and **eigenvalue** / **eigenvector** at 720 - matching the **spectral radius** at 913.
4. Close the loop the lecture opens at 699: after the eigenvalue definitions, come back to the three matrices from 647-687 and say which spectral radius produces spiral-in, ellipse and spiral-out, rather than deferring with "discussed further later" at 854.
5. Drop the 6 hand-set `figsize=` arguments (212, 238, 530, 741, 1032, 1181), set `lw=2` on the 3 default-width line plots (263, 274, 1036), and lower-case the `Im` axis label at 1299 (qe-fig-001 x6, qe-fig-008 x3, qe-fig-006 x1).
6. Fix the code slips: make the titles at 226 and 231 raw strings as 543-551 already are, restore the comma space at 576, and even out the minus-sign spacing at 1136-1137 and 1281.
7. Give the Neumann series section one figure - eigenvalues in the unit disk, or the partial sums of $\sum A^k$ approaching $(I-A)^{-1}$ - and rewrite the parenthetical at 1112, which currently tells comfortable readers to skip ahead.
