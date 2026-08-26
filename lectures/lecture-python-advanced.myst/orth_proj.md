# orth_proj

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/orth_proj.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-004` ×2; `qe-writing-001` ×3; `qe-writing-003` ×4, +3 more. |
| Math         | 3/10  | `qe-math-002` ×52; `qe-math-003` ×6; `qe-math-009` ×5. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×6; `qe-fig-002` ×6. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 8/10  | `qe-link-002` ×2. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 6. *Lines:* 73, 79, 85, 154, 195, 249. *Example:* static image .png.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 73, 79, 85, 154, 195, 249. *Example:* {figure} without :name:.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 52. *Lines:* 351, 356, 364, 366, 375, 383, 385, 402, 417, 420, …. *Example:* apostrophe transpose `X'`.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 6. *Lines:* 535, 545, 560, 569, 777, 791. *Example:* array used as matrix.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 5. *Lines:* 259, 377, 402, 567, 617. *Example:* the book already defines the macros this lecture writes out by hand: `_config.yml` sets `Span: span` and `col: col`, yet the file writes `\mathop{\mathrm{span}}` twelve times (259, 274, 397 twice, 412, 471, 475, 478, 648, 649, 659) and `\mathop{\mathrm{col}}` four times (397 twice, 412, 683), and it brackets the operator three different ways - bare (`\mathop{\mathrm{span}} X` at 397, 412), with braces (274, 648, 659) and with parentheses (471, 475, 478). The number of regressors changes case inside a single proof: the theorem at 348 declares $X$ to be $n \times k$, its own proof writes $b \in \mathbb R^K$ at 377 and 380, 437-482 returns to lowercase $k$, and the whole regression section (498, 522, 585, 586) uses uppercase $K$ for the same quantity. 402 drops the distinction between the operator and its value: "$P = X (X' X)^{-1} X' y$ projects $y$ onto $S$" has a spurious $y$ inside the definition of the matrix, which 351, 356, 598 and 740 all state correctly as $P = X(X'X)^{-1}X'$. 567 writes `:=:` between the two representations of $X$. And 617-619 sets three definitions as "The **total sum of squares** is $:= \| y \|^2$", so the sentence reads "is := ..." three times over.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 16. *Lines:* 71, 77, 111, 130, 186, 311, 333, 348, 394, 437, …. *Example:* 2 spaces.

### Medium severity
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 2. *Lines:* 53, 665. *Example:* raw link to python-intro.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 348, 740, 883. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 158, 490, 631, 883. *Example:* 158-162 sits under a heading that already says what it does: the section is titled "### Proof of sufficiency" and opens "We'll omit the full proof." / "But we will prove sufficiency of the asserted conditions." 490-494 spends three paragraphs announcing the next section ("Let's apply the theory of orthogonal projection to least squares regression." / "This approach provides insights about many geometric properties of linear regression." / "We treat only some examples."). 631-637 does the same again in three more ("Let's return to the connection ... touched on above." / "A result of much interest is a famous algorithm ..." / "The next section gives details.") immediately before the heading that gives the details. And the exercise solution's commentary is filler where a number belongs: "This is the same answer. So far so good." (883) and "Again, we obtain the same answer." (896).
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 216, 655, 838, 883. *Example:* the orthogonal complement is defined twice, and the second definition is weaker than the first: 83 gives it correctly as $S^{\perp} := \{x \in \mathbb R^n : x \perp S\}$, and 216-217 re-introduces the same bold term as "the linear subspace $S^{\perp}$ that satisfies $x_1 \perp x_2$ for every $x_1 \in S$ and $x_2 \in S^{\perp}$" - a property that $\{0\}$ also satisfies, so as written it does not pin down $S^\perp$ at all. 655 breaks the index: the theorem at 642-652 and the algorithm at 659-663 both run to $k$, and the sentence between them says the procedure "constructs an orthogonal set $\{u_1, u_2, \ldots, u_n\}$". The comment at 838 is off by one - `Z = X[:, :i]` is the first $i$ columns, not the "First i-1 columns of X" - in the one line of the Gram-Schmidt implementation a reader has to trust. And the exercise's three-way verification is settled by eye: 866-893 prints `Py1`, `Py2` and `Py3` as three bare arrays and the prose then asserts "This is the same answer" (883) and "Again, we obtain the same answer" (896), where one `np.max(np.abs(Py1 - Py2))` would say it.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 55, 104. *Example:* mid-sentence 'Theory'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 73, 595, 639. *Example:* every one of the six figures is a static PNG (73, 79, 85, 154, 195, 249) with an empty directive body - no caption, no `:name:` - in a lecture whose entire subject is two- and three-dimensional geometry that matplotlib draws directly, and the prose consequently has to point at them by position ("The next figure provides some intuition" at 152, "The next figure illustrates" at 247) instead of by `{numref}`. Second, the six that exist all illustrate the abstract definitions of §Key definitions, and the section where a picture would carry the most - least squares regression, 595-629, where $y = \hat y + \hat u$ with $\hat u \perp \hat y$ gives TSS = ESS + SSR by the Pythagorean law - has no figure at all, even though it is the same right triangle the earlier PNGs already draw abstractly. Third, Gram-Schmidt (639-667) is a sequential geometric construction described in three bullets - project $x_i$ onto $S_{i-1}^{\perp}$, normalise, repeat - and the natural picture, the first two or three steps in $\mathbb R^3$, is neither drawn in the exposition nor in the exercise that implements it.

### Low severity
_None found._


## Strengths

- Bold-for-definitions is applied without a single exception across twenty-two defined terms - law of cosines (69), orthogonal (71), orthogonal to (77), orthogonal complement (83), orthogonal set (102), Pythagorean Law (104), orthogonal projection (149), wide-sense expectations operator (191), orthogonal projection mapping onto (193), orthonormal set (255), orthonormal basis (259), projection matrix (404), annihilator matrix (406), overdetermined (439), risk (499), empirical risk (507), empirical risk minimization (513), linear least squares problem (526), vector of fitted values (603), vector of residuals (609), the three sums of squares (617-619) and Gram-Schmidt orthogonalization (655) - with italic reserved for emphasis.
- One labelled theorem does all the work and is cited rather than restated: `opt` (134-150) is referenced by `{prf:ref}` at 186, 200, 232, 452, 625 and 627, so the sufficiency proof (158-176), the operator properties (200-210), the matrix formula, the overdetermined-systems theorem and TSS = ESS + SSR each reduce to it plus the Pythagorean law of 104-118.
- The projection formula is derived twice from opposite directions and the two are explicitly reconciled: 293-326 proves $Py = \sum_i \langle y, u_i\rangle u_i$ directly for an orthonormal basis, 408-428 obtains $Py = UU'y$ from the general $X(X'X)^{-1}X'$ by substituting $U'U = I$, and 430-431 stops to say "We have recovered our earlier result about projecting onto the span of an orthonormal basis".
- The regression section names nothing it has not defined: risk (502), empirical risk (510), the hypothesis space (515), the two data matrices written out entry by entry (533-576), the rank condition (578), $\hat\beta$ (592), $P$ and $M$ (598-600), fitted values (606) and residuals (612) all arrive before 617-623, which is why TSS = ESS + SSR needs only two lines (627-629).
- Two claims are handed to the reader instead of being waved past - 122-126 states that an orthogonal set not containing zero is independent, says the proof is a nice exercise, and points forward to the partial converse at the `gram_schmidt` label; and 328 asks why orthogonality to each basis vector suffices for orthogonality to the whole span, immediately after the proof that used it.
- The Gram-Schmidt exercise verifies one projection three independent ways - the projection matrix at 866, the reader's own `gram_schmidt` output at 874-879, and `scipy.linalg.qr` at 887-892 - which is exactly the check 667 promises ("you are asked to implement this algorithm and test it using projection"), and the docstring at 813-824 states the shape contract for both argument and return.
- The QR route to $\hat\beta$ is three lines of algebra with the one non-obvious cancellation justified in the sentence below it (704-713), and 715 then says what a numerical routine would do instead - solve $R\hat\beta = Q'y$ by back substitution - which is the practical point the derivation exists for.

## Recommended actions

1. Remove the spurious $y$ at 402: "$P = X (X' X)^{-1} X' y$ projects $y$ onto $S$" defines the projection matrix, and 351, 356, 598 and 740 all give it correctly as $P = X(X'X)^{-1}X'$.
2. Fix the index at 655 - the procedure constructs $\{u_1, \ldots, u_k\}$, not $\{u_1, \ldots, u_n\}$, per the theorem at 644-645 and the algorithm at 659-663 - and settle $k$ against $K$ for the number of regressors, which flips inside the proof at 377 and 380 and again between 482 and 498.
3. Repair the second definition of the orthogonal complement at 216-217, which re-bolds a term already defined at 83 and states a property that $\{0\}$ also satisfies; either delete it or make it the $Y = S \oplus S^{\perp}$ statement that 219-230 actually needs.
4. Correct the comment at 838: `Z = X[:, :i]` selects the first $i$ columns of `X`, not the first $i-1$, and it is the line the whole Gram-Schmidt implementation turns on; while there, use one norm expression instead of `np.sqrt(np.sum(v1 * v1))` at 833 and `np.sqrt(u @ u)` at 845.
5. Generate the six geometry figures (73, 79, 85, 154, 195, 249) rather than shipping PNGs - they are 2-D and 3-D vector diagrams in a lecture that already imports numpy - and give each a caption and a `:name:` so 152 and 247 can reference them by number instead of by position (qe-fig-002, qe-fig-005).
6. Use the `\Span` and `\col` macros the book already defines in `_config.yml` in place of the twelve `\mathop{\mathrm{span}}` and four `\mathop{\mathrm{col}}` spellings, and pick one bracketing convention - 397 and 412 use none, 274, 648 and 659 use braces, 471, 475 and 478 use parentheses.
7. Add a difference check to the exercise solution (`np.max(np.abs(Py1 - Py2))` and the same for `Py3`) so "This is the same answer" at 883 and 896 is demonstrated rather than asserted, and add a figure of the least-squares triangle to 595-629.
8. Cut the three announcement paragraphs at 490-494 and 631-637, and the two sentences at 158-162 that restate the heading they sit under.
9. Finish the mechanical items: the six `array` displays recast as `bmatrix` (535, 545, 560, 569, 777, 791 - qe-math-003), the 52 apostrophe transposes to `\top` (all genuine: $X'$, $X'X$, $b'$, $x_n'$, $(Xb)'$, $Q'$, $R'$, $U'$), the two raw links to `{doc}` (53, 665), the 16 double spaces, "Theory" and "Law" mid-sentence (55, 104), the stray `\quad` at the end of the display at 783, and the `is $:=$` constructions at 617-619.
