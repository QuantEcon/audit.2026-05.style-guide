# numpy_vs_numba_vs_jax

- **Series:** lecture-python-programming
- **File:** `lectures/numpy_vs_numba_vs_jax.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×7; `qe-writing-005` ×2; `qe-writing-003` ×3, +3 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-005` ×1; `qe-fig-001` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 7. *Lines:* 77, 180, 201, 424, 459, 465, 518. *Example:* H3 Title Case: 'Problem Statement' (Statement).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 187, 352, 434. *Example:* trailing whitespace after `grid.nbytes` at 187 (W291); a lambda assigned to a name at 352, `compute_column_max = lambda y: jnp.max(f(grid, y))`, where a `def` is called for (E731); and the loop body of `qm` indented six spaces instead of four at 434 (E111) - the same defect as numba.md:109, from which this cell is copied.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 405. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 491, 493, 594. *Example:* 32- and 33-word single sentences at 491 (on pinning to the CPU) and 493 (on in-place updates under JIT), the two claims a reader is most likely to need to re-read; and "## Overall recommendations" (579-605) restates "### Summary" (562-575) point for point - Numba readable, JAX less intuitive, JAX differentiable - in the section immediately following it.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 297, 562, 606. *Example:* at 297-299 `f` is silently redefined from the NumPy function at 94-95 to a `jax.jit`-decorated JAX function, so re-running the NumPy timing at 166-167 afterwards times the wrong thing and the memory figures at 186-194 no longer correspond to the `f` in scope; "### Summary" at 562 is the second H3 with that exact title (the first is at 395), so the table of contents shows "Summary" twice; and the lecture stops mid-thought at 604-606 - "if, say, we want to compute sensitivities of a trajectory to model parameters" - with no full stop and no conclusion.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 583, 594. *Example:* "For **vectorized operations**" (583) and "For **sequential operations**" (594) put bold on emphasis, not on definitions - and both phrases were already defined as section titles at 70 and 412; the lecture's genuinely new terms (`vmap`, meshgrid, eager) are left unmarked.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 101. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 92. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 493. *Example:* "Important:" is written inline as the lead-in to the lecture's key claim about `at[t].set` being an in-place update under JIT, in a lecture that already uses `{note}` for exactly this purpose at 404-409.


## Strengths

- The comparison is set up so all four implementations solve the identical problem on the identical grid, and each prints its result to six decimals (177, 282, 319, 381), so the reader can confirm the speed comparison is between correct programs.
- The wrong vectorization is shown first - `np.max(f(grid, grid))` at 146, flagged "# This is wrong!" - and diagnosed against the surface plot: "it only computes the values of `f` along the diagonal" (151-152).
- Memory is measured, not just time: `grid.nbytes` against `x_mesh.nbytes + y_mesh.nbytes` (186-194) makes the meshgrid cost concrete before `vmap` removes it.
- `compute_max_vmap` (349-358) is commented line by line, and the payoff is stated as the explicit list of the three arrays that are never created (361-365).
- The verdict is split by problem type instead of declared for the library as a whole - JAX for vectorized work, Numba for sequential work, with the readability argument spelled out at 564-575 rather than asserted.

## Recommended actions

1. Sentence-case the seven headings (77, 180, 201, 424, 459, 465, 518).
2. Merge "### Summary" (562-575) into "## Overall recommendations" (579-605) - they cover the same ground, and the duplicate heading title (395 and 562) makes the table of contents ambiguous.
3. Finish the closing sentence at 604-606 and give the lecture a conclusion.
4. Rename the JAX `f` at 297-299 or note that it replaces the NumPy `f` from 94 - as written the NumPy timings above it are not reproducible on a re-run.
5. Fix 341: `z_max` is a scalar from `jnp.max`, not one of the "big arrays" the section is about avoiding.
6. Turn "Important:" (493) into a `{note}` and split the two 32-word sentences at 491 and 493.
7. Clean the code cells: trailing whitespace at 187, the assigned lambda at 352, the six-space loop body at 434, and the unused `Axes3D` import at 63; add mystnb metadata to the surface plot (92) and drop `figsize=` at 101.
