# ifp_opi

- **Series:** lecture-python.myst
- **File:** `lectures/ifp_opi.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-006` ×5; `qe-writing-002` ×3; `qe-writing-007` ×1. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 6/10  | `qe-code-002` ×2; `qe-code-001` ×3; `qe-code-004` ×14, +1 more. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-003` ×3; `qe-fig-005` ×2; `qe-fig-008` ×3, +1 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 14. *Lines:* 305, 308, 315, 318, 326, 329, 336, 339, 391, 394, …. *Example:* bare time() reading.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 5. *Lines:* 56, 107, 219, 245, 293. *Example:* H2 Title Case: 'Model and Primitives' (Primitives).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 96, 124, 133. *Example:* line 96 closes the `create_consumption_model` signature with `    ):` at 4 spaces, leaving the arguments at the same indent as the body (E121/E125). Line 124 pads before `=` to align with the line above (E221), and the two staged-`vmap` blocks pad both before `=` and inside the `in_axes` tuples (133-135 and 194-195; E221, E241).
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 102. *Example:* spelled-out `rho`.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 361, 369, 408. *Example:* .set(xlabel='current assets', ylabel='next period assets', title=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 353, 401. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 3. *Lines:* 359, 367, 403. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 30. *Example:* raw link to dp.quantecon.org.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 60, 109, 376. *Example:* roughly a hundred lines are restated from {doc}`ifp_discrete` rather than referenced: `B` (114-127) is that lecture's 428-441 verbatim, the three staged `vmap` calls (133-135) are its 447-449, `T` and `get_greedy` (141-157) are its 456-469, and `value_function_iteration` (224-243) is its 475-492. The lecture says why - 'We repeat the key elements here for convenience' (60), 'We repeat some functions' (109) - but the material it repeats is the predecessor's *exercise solution*, so the duplication also silently makes this lecture depend on an answer the reader may not have seen. Separately, the same conclusion is drawn twice: 'confirming both algorithms converge to the same solution' (349) and 'confirming both methods produce the same solution' (376).

### Low severity
- **[qe-code-005]** — Use quantecon timeit for benchmarking. *Count:* 1. *Lines:* 387. *Example:* hand-rolled benchmark loop — use qe.timeit.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 354. *Example:* figsize=.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 473. *Example:* the exercise computes speedup factors over a 3x3 grid of $(\rho, \nu)$ values and reports them as nine `print` lines (473-476), in a lecture whose entire subject is comparative speed and which plots its other sweep - OPI time against $m$ - as a figure with the VFI reference line drawn in (401-410). Nine numbers on a 3x3 grid is a small heatmap or a grouped bar chart, and the claim being tested ('the speed gains achieved by OPI are quite robust to parameter changes', 425) is a statement about a surface.


## Strengths

- The speed comparison is set up so that its numbers mean something: both algorithms are run once to compile and once to time (303-341), the two value functions are then checked with `jnp.allclose` (346) and the two policies compared side by side (353-374), so the speedup at 381 rests on both methods having solved the same problem.
- The $m$-sweep (386-410) is the right experiment for OPI and the figure shows the interior optimum, with the prose naming the mechanism behind the degradation at large $m$ - too much time iterating the policy operator (416-417) - rather than just reporting the shape.
- The policy operator is written in mathematics (165-167) before it is coded, and the code's index convention is documented in the docstring of `B` (119-121), which is what makes the staged-`vmap` style readable.
- The staged-`vmap` idiom is applied consistently to both operators (133-135 for `B`, 194-195 for `T_σ`), so the two vectorisations can be compared line for line.
- The exercise tests the robustness claim by varying the income process rather than the algorithm's own tuning parameter, which is the harder and more informative check, and it reports both raw timings and the ratio (471).

## Recommended actions

1. Plot the exercise's 3x3 speedup grid instead of printing it (473-476), matching how the $m$-sweep is presented at 401-410.
2. Replace the 14 bare `time()` readings at 305, 308, 315, 318, 326, 329, 336, 339, 391, 394, ... with the `quantecon.Timer` context manager - `qe` is already imported at 46 - and the hand-rolled benchmark loop at 387 with `qe.timeit` (qe-code-004, qe-code-005).
3. Make the $m$-sweep timings comparable with the reference line: the loop at 390-396 times the first value of $m$ without a warm-up call, while `vfi_time` drawn at 404 is a compile-free second run, so the leftmost point may carry compilation the others do not.
4. Sentence-case the five Title Case headings at 56, 107, 219, 245 and 293 (qe-writing-006), and replace the raw dp.quantecon.org link at 30 with a proper cross-series reference (qe-link-002).
5. Figure hygiene: add mystnb name/caption metadata to the two figure cells at 353 and 401 (qe-fig-005), move the embedded titles at 361, 369 and 408 into captions (qe-fig-003), set `lw=2` on the plots at 359, 367 and 403 (qe-fig-008), and drop `figsize=` at 354 (qe-fig-001).
6. Reduce the duplication from {doc}`ifp_discrete`: keep `T_σ`, `iterate_policy_operator` and `optimistic_policy_iteration`, which are this lecture's contribution, and point at the predecessor for `B`, `T`, `get_greedy` and `value_function_iteration` - or promote them out of that lecture's exercise solution so both lectures can rely on one definition.
7. Code tidy: the closing-paren indent at 96, the alignment padding at 124, 133-135 and 194-195, and the unused `num_iter` and `error` unpacked at 286.
