# lagrangian_lqdp

- **Series:** lecture-dp
- **File:** `lectures/lagrangian_lqdp.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 6.7 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×7; `qe-writing-002` ×5; `qe-writing-004` ×3, +5 more. |
| Math         | 3/10  | `qe-math-002` ×69; `qe-math-003` ×6; `qe-math-009` ×4. |
| Code         | 6.5/10 | `qe-code-001` ×5; `qe-code-002` ×1; `qe-code-005` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | N/A   | no figures or plotting code. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 7.5/10 | `qe-link-002` ×5. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 5. *Lines:* 470, 599, 604, 638, 686. *Example:* the `raise ValueError(...)` at 599-601 puts its message and closing paren at indent 4 while the `raise` is at indent 8, so the continuation is under-indented relative to its own statement (E128) and the block reads as if it had fallen out of the function. Line 604-605 uses `'    W11: {}'.format(...)` five lines after an f-string at 600. In `stationary_P`, `n, k = lq.n, lq.k` (638) binds two names that are never read, and `L, N, M = construct_LNM(...)` plus `W, V, P = stable_solution(...)` (640-641) discard four more - only `P` is returned. Line 470-471 pads `[0,              1]` with fourteen spaces to align a 2x2 (E241), and line 686 writes `H[0, :] = ρ,δ` with no space after the comma while 687 puts a space after a unary minus.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 5. *Lines:* 61, 66, 676, 827. *Example:* raw link to python-advanced.quantecon.org.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 69. *Lines:* 87, 94, 102, 107, 113, 125, 128, 132, 161, 162, …. *Example:* apostrophe transpose `x'`.
- **[qe-math-003]** — Use square brackets for matrix notation. *Count:* 6. *Lines:* 341, 356, 815, 817, 818, 820. *Example:* matrix environment.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 5. *Lines:* 141, 279, 372, 759, 780. *Example:* 'The positive define solution is associated with the maximum of our problem' (141) and 'where $P$ is a positive define matrix' (192) both want 'definite'. Line 279 is not a sentence at all: 'The determinant of a symplectic, then $\textrm{det}(M) = 1$' - one of two bullets listing the salient properties of symplectic matrices. Line 372 repeats verbatim, four lines later, the definition already given at 367-368 ('Let $V^{ij}$ denote the $(i,j)$ piece of the partitioned $V^{-1}$ matrix'). Line 759 contradicts itself inside one sentence: 'we can first transform a discounted LQ problem to an undiscounted one and then solve that discounted optimal regulator problem'. Line 780 reads 'it is useful explicitly briefly to describe'. Also 'to sbe' (835), 'Stackelberg and Ramsey problem' (65), and 'contruct' in a docstring (683).
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 7. *Lines:* 70, 236, 258, 672, 699, 705, 778. *Example:* H2 Title Case: 'Undiscounted LQ DP Problem' (Problem).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 72. *Lines:* 38, 46, 52, 53, 73, 79, 87, 128, 177, 186, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-005]** — Use quantecon timeit for benchmarking. *Count:* 2. *Lines:* 662, 667. *Example:* %%timeit.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 4. *Lines:* 161, 216, 230, 279. *Example:* the transpose is spelled two ways and the switch is arbitrary. Sections 'Undiscounted LQ DP Problem' and 'Application' use the bare apostrophe (87, 94, 102, 107, 113, 125, 128, 132, 181, 743, 749, 806, 815, 816, 832-897), while 'Lagrangian', 'Reciprocal Pairs Property' and 'Lagrangian for Discounted Problem' use `^\prime` (161-162, 173, 216, 230-231, 273, 283, 287, 290, 713, 787-788, 798) - and `` {eq}`Mdefn` `` at 230-231 manages both spacings of the same thing, `A^{\prime-1}` on one line and `A^{\prime -1}` on the next, which also reads ambiguously as $A^{\prime-1}$ rather than $(A^\top)^{-1}$. The Lagrangian itself is `{\cal L}` at 161 and `{\cal{L}}` at 787: two spellings, both using the deprecated `\cal` rather than `\mathcal`, for a symbol that appears twice. And line 279 writes `\textrm{det}(M)` where `\det M` exists.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 446. *Example:* 2 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 699, 743, 823. *Example:* '## Discounted Problems' (699) has no body: the heading is followed by a `+++` marker, three blank lines and the next heading - one of seven stray `+++` cell separators left in the prose (27, 154, 234, 256, 701, 761, 825). The two transformed-problem formulas at 743 and 749 mix hatted and unhatted matrices in a way that cannot be read as a derivation: `\hat F=(Q+B'\hat PB)^{-1}\hat B'P \hat A` and `\hat P=R+\hat A'P \hat A-\hat A'P \hat B(Q+B'\hat P \hat B)^{-1} \hat B'P \hat A` use $P$ and $B'$ unhatted inside the equations that are supposed to define $\hat P$ and $\hat F$ - the conclusion $\hat F = F$, $\hat P = P$ arrives only at 752, so at 743 the reader has an equation defining a hat in terms of a non-hat. And line 823 says system `` {eq}`eq663` `` 'in the special case that $\beta = 1$ agrees with equation `` {eq}`lag-lqdp-eq2` ``' - `lag-lqdp-eq2` is the pair of first-order conditions (173-175); the matrix system it agrees with is `` {eq}`eq:systosolve` `` (209-211).
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 3. *Lines:* 676. *Example:* mid-sentence 'Linear'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 55, 58, 245, 270. *Example:* the bold is doing too much work in a file with only two italics (*undiscounted* 457, *any* 874). **symplectic** is bolded at its definition (48) and bolded again at the formal Definition (270); **state** and **costate** are bolded three separate times (53, 55, 197-198), and the hyphenation changes inside the bold - '**states** and **costates**' at 53 against '**state** and **co-state**' at 55. Line 58 puts the full stop inside the bold, '**invariant subspaces.**'. And '**stable** solution' at 245 is emphasis rather than definition, which is what the italic is for.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 50, 528. *Example:* this is a lecture about where eigenvalues sit relative to the unit circle - reciprocal pairs (50, 302-303), all eigenvalues of $W_{22}$ exceeding 1 in modulus and all of $W_{11}$ below it (323-324, 534-535), 'the eigenvalues of $M$ split half inside and half outside the unit circle' (443-444) - and it contains no figures at all. Line 528 already computes the eigenvalues of $M$ and line 529 prints them as a bare Python list; plotting those four numbers in the complex plane against the unit circle would make the reciprocal-pairs property, the stable/unstable split and the effect of the $\beta^{1/2}$ rescaling visible in one panel. The same figure would carry the 'Other Applications' section at 672-697, where $H$ is a 2x2 whose eigenvalue split is the whole point.

### Low severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 1. *Lines:* 476. *Example:* spelled-out `beta`.


## Strengths

- The Lagrangian route to the Riccati equation is carried out without gaps: the Lagrangian (161-163), the first-order conditions (173), the envelope condition supplying the $t=0$ counterpart (177-184), the identification $\mu_{t+1} = Px_{t+1}$ tied back to the value-function gradient computed 40 lines earlier (146-152, 189-195), and then a three-bullet recipe (200-206) for turning the conditions into the state-costate system `` {eq}`eq:systosolve` `` - a reader can reproduce every step.
- The reciprocal-pairs result is proved rather than quoted: $J$ is introduced (265), symplecticity defined (270-274), $M^\prime = J^{-1}M^{-1}J$ derived from it (287), and then three one-line facts about similar matrices, inverses and transposes (295-299) deliver the conclusion (301-303). The derivation is four displays long and complete.
- $P = V_{21}V_{11}^{-1}$ is derived, not asserted: stability forces $y^\ast_{20} = 0$ (370-378), that gives $\mu_0 = -(V^{22})^{-1}V^{21}x_0$ (383), the block-inverse identity $V^{21}V_{11} + V^{22}V_{21} = 0$ (397-403) converts it, and `` {eq}`eqn:Pvaughn` `` follows (431) - and the code then computes exactly that, via `np.linalg.solve(V[:n, :n].T, V[n:, :n].T).T` (608) rather than forming an explicit inverse, with a comment saying so.
- The claim that the Schur method is faster is settled by measurement rather than assertion: `stationary_P` and `LQ.stationary_values` are run against each other at 661-669, immediately after their outputs are shown to agree (648, 656).
- The `sort_fun` device (542-546) is a genuinely useful piece of exposition: it explains what `scipy.schur`'s `sort` argument has to do to put the stable block top-left, checks `stable_dim` against $n$ and raises if the split is wrong (598-601), and then prints the two diagonal blocks so the reader can confirm the split by eye (562-569).
- The 'Other Applications' section (672-697) reuses `stable_solution` unchanged on a rational-expectations model with no optimisation behind it, which is exactly the third bullet promised in the overview (46).

## Recommended actions

1. Convert all 71 transposes to `^\top`. This is the densest transpose debt in the series and the file uses two spellings for it - the apostrophe in the first and last thirds, `^\prime` in the middle (see the qe-math-009 finding for the line list). One pass with a consistent replacement clears qe-math-002 entirely and is by far the highest-payoff edit here. Note the reported count of 73 overstates the 71 that exist; see scanner_doubts.
2. Fix the two transformed-problem formulas at 743 and 749: every $P$, $B$ and $A$ inside an equation defining $\hat P$ or $\hat F$ should carry the hat. As written, `\hat P = R + \hat A' P \hat A - ...` defines the transformed matrix in terms of the untransformed one, which is circular until the reader reaches line 752.
3. Add a figure plotting the eigenvalues of $M$ in the complex plane with the unit circle, right after line 529 where they are already computed. Reciprocal pairs, the stable/unstable split and the effect of the $\beta^{1/2}$ rescaling are the three ideas the lecture turns on, and none of them is currently visible anywhere.
4. Clear the 72 double spaces (qe-writing-008 x72, the largest single mechanical item) and sentence-case the 7 Title Case headings: 'Undiscounted LQ DP Problem' (70), 'State-Costate Dynamics' (236), 'Reciprocal Pairs Property' (258), 'Other Applications' (672), 'Discounted Problems' (699), 'Transforming States and Controls to Eliminate Discounting' (705), 'Lagrangian for Discounted Problem' (778).
5. Repair the prose errors: 'positive define' at 141 and 192, the non-sentence bullet at 279, the verbatim repeat at 372 (delete it, 367-368 already says it), the self-contradiction at 759 ('that discounted optimal regulator problem' should be 'undiscounted'), 'useful explicitly briefly to describe' at 780, 'to sbe' at 835, and the wrong cross-reference at 823 (should be `` {eq}`eq:systosolve` ``, not `` {eq}`lag-lqdp-eq2` ``).
6. Convert the 5 raw quantecon URLs to `{doc}` references (61 x2, 66, 676, 827) - note that 676 links the same lecture that line 34 already reaches through the `intermediate:re_with_feedback` intersphinx target, so the two should agree (qe-link-002 x5) - convert the 6 `matrix` environments to `bmatrix` (341, 356, 815, 817, 818, 820), and replace the 2 `%%timeit` cells with `qe.Timer()` (662, 667, qe-code-005 x2).
7. Delete the 7 stray `+++` markers (27, 154, 234, 256, 701, 761, 825) and give '## Discounted Problems' (699) an introductory sentence or merge it into its subsection; then the PEP8 items above - the mis-indented `raise` at 599-601, the dead unpacking at 638 and 640-641, the `.format` at 604-605, and the padding at 470-471 and 686. Note that the 1 qe-code-002 hit at 476 is a false positive; see scanner_doubts.
