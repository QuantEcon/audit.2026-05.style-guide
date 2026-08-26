# eig_circulant

- **Series:** lecture-python.myst
- **File:** `lectures/eig_circulant.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.9 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×5; `qe-writing-005` ×4; `qe-writing-003` ×4, +3 more. |
| Math         | 7.5/10 | `qe-math-003` ×4; `qe-math-009` ×3. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-003` ×2; `qe-fig-005` ×1; `qe-fig-001` ×2. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 5. *Lines:* 44, 105, 149, 368, 445. *Example:* H2 Title Case: 'Constructing a Circulant Matrix' (Circulant, Matrix).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 44. *Lines:* 46, 129, 143, 180, 183, 203, 205, 207, 249, 253, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 264, 522. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 280, 528. *Example:* .set_title.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 4. *Lines:* 54, 170, 186, 297. *Example:* array used as matrix.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 199, 205, 456. *Example:* line 199 writes `\textrm{det}(P - \lambda I)` where `\det` is the standard operator; line 205 uses the relation macro `\mid \lambda_i \mid` as absolute-value delimiters where `|\lambda_i|` would do; and the imaginary unit changes symbol mid-lecture - $j$ at 258 and 292, then $i$ at 456 and 541 - in a file where $i$ and $j$ are already carrying duty as row and column indices (132, 268, 351-361).
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 153, 205. *Example:* line 153 spends a sentence announcing which definition comes first rather than giving it, and the sentence that follows at 155 contains the doubled phrase 'a permutation of a set of the set of non-negative integers' and is then partly re-given for a different index set at 157. Line 205 names the same object twice in nine words: 'Magnitudes $\mid \lambda_i \mid$ of these eigenvalues $\lambda_i$ all equal $1$'.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 207, 294, 313, 368. *Example:* line 207 concludes 'Thus, **singular values** of the permutation matrix $P$ ... all equal $1$' from the eigenvalue magnitudes at 205, but the fact that licenses that step - $P P^\top = I$ - is only stated two lines later at 209-213. The matrix $F_8$ is introduced at 294, called 'a Discrete Fourier Transform' at 309 and used continuously to 366, while the section that defines the DFT is at 445. Line 313 is a one-item bullet, 'stare at the first column of $F_8$ above to convince yourself of this fact', whose antecedent - the normalisation sentence at 311 - is not something the first column demonstrates. '## Associated Permutation Matrix' at 368 reopens material already presented at 286-290 and repeats its display at 375.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 137, 153, 207, 451. *Example:* bold is used for emphasis and for repetition, not only for definitions: 153 bolds 'matrix' and 'permutation' in a sentence that merely announces the order of the two definitions to come; 207 bolds 'singular values', a term the lecture uses but never defines; 137 re-bolds '**convolution**', already defined in bold at 129; 451 re-bolds '**Discrete Fourier Transform**', already defined in bold at 447.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 129, 180. *Example:* the two ideas in this lecture that are pictures rather than formulas get no figure. Line 180 describes the action of $P$ in words - 'shifts entries in rows $2$ through $N$ up one row and shifts the entry in row $1$ to row $N$' - where a single arrow diagram would show it; and the convolution defined at 129-133 is presented only as a summation index formula. The lecture is otherwise willing to draw (263-285, 504-533), so both are within reach.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 263. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- Every result that gets reused carries an equation label and every later reference goes through it: `eqn:circulant` (63) cited at 143 and 371, `eqn:conv` (133) cited at 137, `eqn:exampleP` (178) cited at 183 and 207 - no 'see equation (2)' anywhere.
- The `prf:definition` at 67-78 pins the shift pattern down with the index formula $C_{ij} = c_{(j-i) \bmod N}$ instead of leaving it to be read off the displayed matrix at 53-63.
- Every claim is checked numerically rather than asserted: the two constructions of $C$ differenced at 419, the eigenvector residuals at 358-361 and 440-442, unitarity at 348, and the DFT-as-matrix identity at 636-647.
- The frequency-leakage pair at 562-608 is a controlled comparison - the same code path run at $11/40$ and then at $10/40$ - so the reader sees exactly what an integer-multiple frequency changes.
- Eigenvalue arrays use the unicode name `𝜆` (241, 272, 425, 429) so the code reads as the mathematics does, and one-sentence-per-paragraph discipline holds across the whole file (0 qe-writing-001 violations).

## Recommended actions

1. Sentence-case the five Title Case headings at 44, 105, 149, 368 and 445 - the highest-weight mechanical item in the file (qe-writing-006).
2. Convert the four `\left[\begin{array}{...}...\right]` displays at 54, 170, 186 and 297 to `bmatrix`, which gives the brackets without the manual `\left[`/`\right]` pair (qe-math-003).
3. Fix the ordering problem: either retitle '## Associated Permutation Matrix' (368) and fold it into the permutation section at 149, or move the $F_8$/DFT material at 292-315 after the DFT is defined at 445 - at present the transform is used 150 lines before it is introduced.
4. Repair the definition passage at 151-157: drop the announcement sentence at 153, fix 'a permutation of a set of the set of non-negative integers' at 155, and give one permutation definition rather than two.
5. Figure hygiene: add mystnb name/caption metadata to the eigenvalue-circle cell at 263 (qe-fig-005), move the embedded titles at 280 and 528 into captions (qe-fig-003), and drop `figsize=` at 264 and 522 (qe-fig-001).
6. Add the two missing pictures: an arrow diagram for the cyclic shift at 180 and an overlap sketch for the convolution at 129.
7. Tidy the notation - `\det` at 199, `|\lambda_i|` at 205, one symbol for the imaginary unit - and sweep the 44 double-space runs in the prose (46, 129, 143, 180, 183, 203, 205, 207, 249, 253, ...).
