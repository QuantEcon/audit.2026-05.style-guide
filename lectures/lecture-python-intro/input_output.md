# input_output

- **Series:** lecture-python-intro
- **File:** `lectures/input_output.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 7.5/10 | `qe-writing-008` ×12; `qe-writing-005` ×1; `qe-writing-007` ×2. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 6.5/10 | `qe-code-001` ×9; `qe-code-002` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×5; `qe-fig-006` ×1; `qe-fig-008` ×7, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 9. *Lines:* 89, 152, 155, 168, 285, 298, 304, 471, 593. *Example:* missing space after a comma in `colorise_weights(centrality,beta=False)` (89, 593), `[(2,'c')]` (155), `nx.draw_networkx_edges(G,pos=pos, ...)` (168) and `[0,0]` (471); `nodes= (1, 2, 'c')` with a space on only one side of `=` (152); a continuation line under-indented by one column relative to the opening bracket (285); and single-space-before-hash inline comments where PEP8 asks for two (298, 304).
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 147, 197, 453, 539, 586. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 7. *Lines:* 206, 207, 208, 222, 462, 463, 477. *Example:* plot() without lw=.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 12. *Lines:* 109, 118, 136, 230, 249, 253, 335, 337, 404, 405, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 89, 593. *Example:* spelled-out `beta`.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 38, 87. *Example:* style override.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 373, 608. *Example:* {cite} in author position: '{cite}`DoSSo` argue'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 366, 506. *Example:* the production possibility frontier is the section's whole subject and ends in the concrete line $10d_1 + 500d_2 = x_0$ (366) that is never plotted, even though the lecture already draws the feasible set for the primal constraints at 197; and the demand-shock decomposition $\Delta x = \Delta d + A\Delta d + A^2\Delta d + \cdots$ (506) describes successive rounds of propagation through the very network drawn in {numref}`us_15sectors`, with no figure showing the rounds decaying.

### Low severity
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 1. *Lines:* 595. *Example:* axis label `Output multipliers`.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 1. *Lines:* 185. *Example:* "*Feasible allocations must satisfy*" is a lead-in to an equation set in italic, not an emphasised word; the parallel lead-in at 230 ("More generally, constraints on production are") is correctly plain.


## Strengths

- Every equation that later gets referenced carries a label and is cited by `{eq}` - `eq:inout_1` (237) at 243 and 404, `eq:inout_2` (247) at 253 and 487, `eq:inout_ex` (280) at 342, `eq:inout_frontier` (327) at 337, `eq:inout_price` (396) at 404.
- All matrices and vectors use `bmatrix`; there is not a single `array` environment or apostrophe transpose in the file - transposes are written `^\top` throughout.
- The lecture explicitly tells the reader what its notation means where it could be ambiguous: line 577 states that $\mathbb{1}$ denotes a vector of ones.
- Defined terms are consistently bolded at the point of definition - Leontief function (136), Hawkins-Simon conditions (253), production possibility frontier (337), conjugate pair (405), primal/dual (413, 426), output multiplier (558).
- The network figure `us_15sectors` is built once and then re-used as the reference point for three later sections via `{numref}` (523, 537, 584), which ties the graph-theory material back to the same data.

## Recommended actions

1. Resolve the notation collision in the demand-shock section: $x_0$ and $d_0, d_1$ at 499-501 denote a pre-shock output vector and two demand vectors, but $x_0$ is the exogenous labor input everywhere else in the lecture (125, 191, 320, 326, 366, 623) and $d_1, x_1$ are the first components of $d$ and $x$ (189, 366, 691) - rename the shock-era objects.
2. Add `mystnb: figure: caption/name` metadata to the five un-named figures (147, 197, 453, 539, 586); as it stands only the opening network graph can be cross-referenced, and the two bar charts are referred to as "the above figure" (552) and "the following figure" (583).
3. Plot the production possibility frontier (366) and, in the demand-shock section, the decaying rounds of $A^k \Delta d$ - both sections currently describe a picture in prose.
4. Convert the two author-position citations to `{cite:t}`: "{cite:t}`DoSSo` argue" (373) and "{cite:t}`DoSSo` Chapter 9 discusses" (608).
5. Set `lw=2` on the seven constraint lines (206, 207, 208, 222, 462, 463, 477), lower-case the axis label at 595, and drop the `figsize=` at 87 unless the tall aspect ratio is deliberate.
6. Replace the spelled-out `beta=False` keyword arguments (89, 593) and remaining Latin Greek names (543) with Unicode where they stand for Greek symbols, and clean up the nine PEP8 spacing items listed above.
7. Fix the stray capital $X$ at 253 (the solution of {eq}`eq:inout_2` is $x$, not $X$), settle on "Leontief inverse" in lower case (249 and 487 currently write "Leontief Inverse"), and strip the 12 runs of double spaces.
