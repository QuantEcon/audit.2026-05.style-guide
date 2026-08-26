# lagrangian_lqdp

- **Series:** lecture-python.myst
- **File:** `lectures/lagrangian_lqdp.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 6.8 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×7; `qe-writing-002` ×5; `qe-writing-004` ×3, +5 more. |
| Math         | 3/10  | `qe-math-002` ×69; `qe-math-003` ×6; `qe-math-009` ×3. |
| Code         | 7/10  | `qe-code-001` ×5; `qe-code-005` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | N/A   | no figures or plotting code. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 7.5/10 | `qe-link-002` ×4; `qe-link-001` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 591, 599, 612, 638, 686. *Example:* 599-601 breaks the `raise ValueError(` block open: the f-string argument is indented four spaces while the `raise` sits at eight, so the continuation and the closing paren are left of the statement that owns them (PEP8 E128); 612 leaves one blank line between the top-level `stable_solution` and `stationary_P` where PEP8 asks for two (E302); 638 binds `n, k = lq.n, lq.k` and uses neither, and 640-641 bind `L`, `N`, `W` and `V` and use none of them (F841 x6 in one 30-line function); 591-595 redefines `tol` and `sort_fun` inside `stable_solution` although both already exist at module scope from 540-544; and 686 writes `H[0, :] = ρ,δ` with no space after the comma (E231). The `stable_solution` docstring is also misleading - the system it draws at 579-580 as `y' = |a b| y` / `x' = |c d| x` is not the block system the function solves.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 69. *Lines:* 87, 94, 102, 107, 113, 125, 128, 132, 161, 162, …. *Example:* apostrophe transpose `x'`.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 6. *Lines:* 341, 356, 815, 817, 818, 820. *Example:* matrix environment.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 52, 279, 372, 780, 827. *Example:* 52-53 is a 46-word sentence, and 55 then repeats its content ("describes the joint dynamics of a system of equations describing the states and costates" against "describes the first-order dynamics of state and co-state vectors"), spelling "costates" one way at 53 and "co-state" the other at 55; 372 repeats 367-368 verbatim ("Let $V^{ij}$ denote the $(i,j)$ piece of the partitioned $V^{-1}$ matrix") four lines after the same sentence; 279 is not a sentence at all ("The determinant of a symplectic, then $\textrm{det}(M) = 1$"); 780-781 stacks two adverbs ungrammatically ("it is useful explicitly briefly to describe"); and 827 is 46 words that use the phrase "this lecture" twice to mean two different lectures. The file also carries the typos "positive define" for positive definite (141, 192), "sbe" (835) and "contruct" (683).
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 7. *Lines:* 70, 236, 258, 672, 699, 705, 778. *Example:* H2 Title Case: 'Undiscounted LQ DP Problem' (Problem).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 72. *Lines:* 38, 46, 52, 53, 73, 79, 87, 128, 177, 186, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-005]** — Use quantecon timeit for benchmarking. *Count:* 2. *Lines:* 662, 667. *Example:* %%timeit.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 4. *Lines:* 61, 66, 827. *Example:* raw link to python-advanced.quantecon.org.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 316, 465, 682. *Example:* three symbols are reused for unrelated objects. $V$ is the value function from 87 ("$V(x) = -x'Px$") and 149, and becomes the Schur transformation matrix at 316, then is used that way through 361-431 and in the code at 546-555 and 608 - so the docstring at 614-616 writes "V(x) = x' P x" inside the very function whose local `V` is the Schur basis. $\mu$ is the costate vector from 161 to 209 and 791-891, and at 465 becomes a scalar income parameter (`μ = 1`) that then enters the $A$ matrix at 470. $\lambda$ is an eigenvalue at 50 and 302 and becomes a model parameter at 682-691 (`construct_H(ρ=.9, λ=.5, δ=0)`). Separately the Lagrangian is written `{\cal L}` at 161 and `{\cal{L}}` at 787 - the deprecated plain-TeX form, spelled two different ways, where `\mathcal{L}` is standard.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 446. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 454, 699, 763. *Example:* "## Application" (452) applies the method to the discounted permanent-income problem and 456-458 introduces the transformed matrices $\hat A = \beta^{1/2}A$, $\hat B = \beta^{1/2}B$ as a given - but the transformation is not derived until "### Transforming States and Controls to Eliminate Discounting" at 705-752, 250 lines later, so the reader must accept the trick before seeing why it works; 699 is an H2 ("## Discounted Problems") whose entire body is a `+++` marker and two blank lines before its first H3; and 767-775 re-runs `stationary_P(lq)` and `lq.stationary_values()`, the identical two cells already executed at 646-657, producing the same output a second time.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 3. *Lines:* 676. *Example:* mid-sentence 'Linear'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 53, 146, 245. *Example:* 53 bolds **states** and **costates** for emphasis in the middle of a long sentence and 197-198 then bolds **costate** and **state** again where they are actually defined, so the reader sees the marker twice and the definition second; 146 bolds "**gradient of the value function**", which is not a term the lecture coins but an object it computes; and 245 bolds the adjective in "a **stable** solution", pure emphasis where the rule asks for italic. 58 also bolds its own full stop ("**invariant subspaces.**").

### Low severity
- **[qe-link-001]** — Use markdown style links for lectures in same lecture series. *Count:* 1. *Lines:* 676. *Example:* full URL to own series (python.quantecon.org).
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 258. *Example:* the lecture has no figures at all, and the one it most needs is already computed. "## Reciprocal Pairs Property" (258-324) establishes the organising fact of the whole lecture - the eigenvalues of the symplectic $M$ come in reciprocal pairs, so exactly half lie inside the unit circle - and then 527-530 computes those eigenvalues and prints them as a bare Python list, while 562-570 prints the diagonals of $W_{11}$ and $W_{22}$ as two more lists. One scatter of `np.linalg.eigvals(M)` in the complex plane with the unit circle drawn, stable and unstable eigenvalues marked differently, shows the reciprocal pairing, the half-in-half-out split, and why `sort_fun` at 542 can separate them - all from data the notebook already holds.


## Strengths

- Twenty-four display equations are labelled and every one of them is cited where it is used - `riccati` at 135, 137, 192 and 435, `eqn:valgrad` at 152, 167 and 194, `lag-lqdp-eq2` at 184, 202, 206, 811 and 823, `eq663` at 823, 827, 829 and 882 - which is what lets a lecture this dense in algebra refer back precisely instead of restating.
- The lecture verifies its own claims numerically instead of asserting them: 516-523 checks $MJM^\prime = J$ directly, 527-530 exhibits the reciprocal eigenvalue pairs, 562-570 confirms that the moduli split either side of one, and 646-668 computes $P$ by Schur decomposition, compares it against `LQ.stationary_values()`, and then times both to support the efficiency claim at 659.
- `stable_solution` is written with numerical care: 607-608 computes $V_{21}V_{11}^{-1}$ through `np.linalg.solve` on transposes with a comment saying it avoids forming the inverse, and `sort_fun` (542, 593) tests `abs(x) < 1 - tol` rather than `abs(x) < 1`, so an eigenvalue sitting numerically on the unit circle is not silently counted as stable.
- The `stable_dim != n` guard at 598-601 turns the half-inside-half-outside eigenvalue condition - the assumption the whole method rests on, stated at 443-444 - into a runtime check whose message reports both the expected and the found count.
- The claim at 674 that the method is not limited to optimization problems is then demonstrated rather than left standing: `stable_solution` is applied unchanged to the rational-expectations $H$ matrix at 682-696, which is exactly the case 446-450 says has no underlying optimum problem.
- Both `{note}` blocks supply something the next display actually needs: 100-104 gives the three matrix-differentiation rules used immediately at 107, and 868-870 gives the partitioned-inverse formula that verifies `` {eq}`eqn:twofeedbackloops` ``.

## Recommended actions

1. Replace all 73 apostrophe and `^\prime` transposes with `^\top` (87, 94, 102, 107, 113, 125, 128, 132, 161, 162 and 63 more). This is the largest single fix in the corpus for this lecture and it is mechanical - but note that $x'_t$ and $u'_t$ appear inside `$$` displays and in prose, so a blind substitution will need checking around 76 and 251.
2. Add the eigenvalue plot described above to section 258-324, and consider a second panel showing the same eigenvalues before and after the $\beta^{1/2}$ rescaling - it would make the discounting transformation at 705-752 visible as a radial contraction.
3. Move the discounting transformation (705-752) ahead of "## Application" (452), which already uses it, and delete the duplicate cells at 767-775; give "## Discounted Problems" (699) either an introductory paragraph or no H2 of its own.
4. Rename the three overloaded symbols: the Schur matrix $V$ at 316 onward (it collides with the value function $V(x)$ from 87, including inside the `stationary_P` docstring at 616), the income parameter $\mu$ at 465 (it collides with the costate $\mu_t$), and the parameter $\lambda$ at 682-691 (it collides with the eigenvalue $\lambda$ at 50 and 302).
5. Fix the code defects: re-indent the `raise ValueError` block at 599-601, add the second blank line before `stationary_P` at 612, drop the six unused bindings at 638-641, remove the duplicate `tol`/`sort_fun` at 591-595, and correct the `stable_solution` docstring so the system it draws (579-580) is the block system the function actually solves.
6. Sentence-case the seven Title Case H2/H3 headings (70, 236, 258, 672, 699, 705, 778), convert the six `matrix`/`bmatrix`-free `\left[\begin{matrix}` environments to `bmatrix` (341, 356, 815, 817, 818, 820), replace `{\cal L}` and `{\cal{L}}` with `\mathcal{L}` (161, 787), and turn the hand-rolled "**Definition:**" at 270 into a `prf:definition` directive.
7. Repair the broken prose - 279 (not a sentence), 780 ("explicitly briefly"), 835 ("sbe"), 141 and 192 ("positive define"), 683 ("contruct") - delete the duplicated sentence at 372, close the 72 double spaces, replace the five bare "this lecture" links (61 twice, 66, 676, 827) with `{doc}` references, and replace the two `%%timeit` cells (662, 667) with `quantecon.Timer` (qe-code-005).
