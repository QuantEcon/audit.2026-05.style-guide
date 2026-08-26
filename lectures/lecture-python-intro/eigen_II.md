# eigen_II

- **Series:** lecture-python-intro
- **File:** `lectures/eigen_II.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-004` ×2; `qe-writing-005` ×3; `qe-writing-003` ×2, +4 more. |
| Math         | 9.5/10 | `qe-math-009` ×1. |
| Code         | 7.5/10 | `qe-code-001` ×7. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | N/A   | no figures or plotting code. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 7. *Lines:* 138, 139, 148, 149, 322, 550, 561. *Example:* `{v[:,0]}`, `{-v[:,1]}`, `{w[:,0]}`, `{-w[:,1]}` at 138-139 and `{e[:,0]}` ... `{ε[:,1]}` at 148-149 omit the space after the comma in the index, which the same lecture writes correctly as `v[:, i]` at 311-312; `def check_convergence(M)` at 322 follows the previous top-level def with a single blank line (PEP8 asks for two); `#dominant eigenvalue/spectral radius` at 550 has no space after the hash; `d.shape = (3,1)` at 561 has no space after the comma.

### Medium severity
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 267. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 63, 222. *Example:* line 63 packs the irreducibility definition into 33 words and then mis-states its own condition: "$A + A^2 + A^3 + \cdots \gg 0$, where $\gg 0$ indicates that every element in $A$ is strictly positive" - the positivity is a property of the sum, not of $A$; line 222 "We know that in real world situations it's hard for a matrix to be everywhere positive (although they have nice properties)" leaves "they" and the parenthetical unattached to anything.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 191, 453. *Example:* line 191 says "Let's build our intuition for the theorem using a simple example we have seen [before](mc_eg1)" but the next section (195-203) introduces a fresh matrix and never returns to `mc_eg1`, so the promised link is not made; line 453 "Recall that eigenvalues are ordered from smallest to largest from $i = 1 ... n$" asks the reader to recall a convention this lecture has not stated - and the code at 305-308 picks the dominant eigenvalue with `np.max`/`np.argmax`, giving no ordering at all.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 457, 554. *Example:* mid-sentence 'Theorem'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 63, 118, 265. *Example:* definitions left unbolded while emphasis is bolded - the exact reversal the rule forbids: "is called irreducible" at 63 and "is called a left eigenvector" at 118 carry no bold, although **nonnegative** (49), **dominant eigenvalue** (164), **primitive** (228) and **Perron projection** (267) are all correctly bolded; at 265 bold is used for emphasis instead, "the inequality $|\lambda| \leq r(A)$ is **strict**".
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 169, 355, 465. *Example:* the lecture has no figure at all across 569 lines, and three passages are about things only a picture shows: the Perron-Frobenius statement at 169-184 compares $|\lambda|$ against $r(A)$ for every eigenvalue, which is a plot of the spectrum against a circle of radius $r(A)$; the convergence of $r(A)^{-m} A^m$ to the Perron projection is delivered at 355-362 as printed Frobenius norms for n = 1, 10, 100, 1000, 10000 rather than an error curve; and the $O(\eta^t)$ rate at 462-468 is asserted with no plot of $\|\psi P^t - \psi^*\|$ against the spectral gap.

### Low severity
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 1. *Lines:* 447. *Example:* $\psi \in \mathscr{D}(S)$ at 447 reaches for a script alphabet for the set of distributions on $S$ - the only decorative symbol in a lecture that otherwise uses plain letters - and the symbol is never defined here or linked to where it is defined.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 443. *Example:* `` {cite} `` in narrative flow: 'in `` {cite} ``'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 266. *Example:* 2 spaces.


## Strengths

- The lecture is stitched into the series rather than standing alone - `{ref}` and `{doc}`-style links reach mc_irreducible (57), la_eigenvalues (104), mc_eg1 (191), mc1_ex_1 (386, 431), mc_eg3 and mc_eg2 (395), and la_neumann (534) - so every borrowed concept has a destination.
- Transpose is `^\top` in all six places it appears (118, 120, 156, 267, 440, 450); no apostrophes and no `^T`.
- The theorem is split into two `prf:Theorem` blocks with continuing claim numbers - 1-5 at 169-184 and 6-7 at 260-268 - and each numbered claim is then checked back one by one in the worked lists at 213-217 and 290-295.
- The non-primitive counterexample at 369-380 runs `check_convergence` on a matrix that fails, immediately after the primitive cases, so the necessity of primitivity is demonstrated instead of asserted.
- Greek names in code are Unicode throughout - `λ` (129, 132, 550), `ε` (145, 149), `ψ_star` (407, 421).

## Recommended actions

1. Give the lecture its first figure. Three places pay off immediately: the spectrum of $A$ plotted against the circle of radius $r(A)$ next to the theorem at 169, the `check_convergence` errors at 355 plotted as a curve instead of printed, and $\|\psi P^t - \psi^*\|$ against $t$ for two matrices with different spectral gaps at 465.
2. Bold the two definitions that are currently plain - irreducible at 63, left eigenvector at 118 - and take the bold off **strict** at 265, where it is emphasis; this makes the lecture consistent with its own **nonnegative** / **primitive** / **Perron projection**.
3. Repair the irreducibility sentence at 63: the condition is that every element of $A + A^2 + A^3 + \cdots$ is strictly positive, not every element of $A$; then split it so the definition and the elementwise restatement at 65 stand as separate sentences.
4. State the eigenvalue ordering convention before line 453 recalls it, and either define $\mathscr{D}(S)$ at 447 or replace it with a plain letter.
5. Either use the `mc_eg1` matrix promised at 191 in the irreducible example at 195, or drop the promise - and collapse the three consecutive transition lines at 189, 191, 193 into one.
6. Lower-case the theorem names in narrative text: "Gershgorin Circle Theorem" at 457 and "Neumann Series Lemma" at 554 (qe-writing-004 x2), split the two-sentence paragraph at 267 (qe-writing-001), move the `{cite}` at 443 out of the sentence flow (qe-ref-001), and reduce the double space at 266 (qe-writing-008).
7. Fix the code slips listed above: `v[:, 0]` spacing in the four f-strings at 138-139 and 148-149, a second blank line before `def check_convergence` at 322, `# dominant` at 550, and `(3, 1)` at 561.
