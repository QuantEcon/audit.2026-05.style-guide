# mccall_model_with_sep_markov

- **Series:** lecture-python.myst
- **File:** `lectures/mccall_model_with_sep_markov.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-003` ×2; `qe-writing-002` ×2; `qe-writing-001` ×1, +2 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7/10  | `qe-code-001` ×21. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×5; `qe-fig-003` ×4; `qe-fig-001` ×5. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 21. *Lines:* 210, 260, 284, 285, 286, 289, 292, 341, 343, 407, …. *Example:* four separate PEP8 groups. Trailing whitespace on nine code lines (210, 260, 289, 292, 341, 343, 435, 488, 490 - 292 is whitespace-only). Annotated parameters with no spaces around `=`: `tol: float=1e-6` and `max_iter: int=1_000` (284, 285), where the same file writes `tol: float = 1e-6` correctly at 405 and `T: int = 2_000` at 601. Closing brackets parked at column 4 under an 8-space hanging indent, matching neither PEP8 option (286, 407, 603, 805, 845). Four code lines past 79 characters (455, 589, 787, 864 - the last is 86). And the continuation at 657 is indented 11 spaces against a visual indent of 12, so `label=` sits one column left of the arguments it continues.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 340, 487, 515, 642, 870. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 339, 486, 505, 633, 951. *Example:* code-cell figure without mystnb figure metadata.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 650, 660, 676, 880. *Example:* .set_title.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 937. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 691, 708. *Example:* line 691-693 is ungrammatical in its main clause - 'positive correlation means that a high current $w$ is often leads a high new draw' - in the sentence that explains the lecture's most distinctive dynamic, why a separated worker so often lands another job at once; and the sentence beginning at 708 ('The reason is that the process $(S_t, W_t)$, where ...') is interrupted by a two-item bullet list before its predicate arrives six lines later at 713-714 ('is Markovian, since ..., and ergodic'), so the reader has to hold the subject across the list to find out what is being claimed.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 903, 525. *Example:* line 903 computes the time-average unemployment rate as `jnp.mean(unemployed_indicator)`, but `unemployed_indicator` was created at 664 as a local by-product of the three-panel plotting cell in a different section, 240 lines earlier - nothing in the prose says the ergodicity comparison depends on that cell having been run, and the variable name appears nowhere in between. Line 525 asks the reader 'Can you provide an intuitive economic story behind the outcome that you see in this figure?' and the lecture never answers it and never turns it into an exercise, so the sensitivity section ends on an open question the reader cannot resolve.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 651, 486. *Example:* line 651 sets `ax1.set_xticks((0, 1))` on the employment-status panel, but ax1's x-axis is time over 2,000 periods - the two ticks belong on the y-axis (0 = unemployed, 1 = employed), as the panel title at 650 says, so the top panel of the lecture's main simulation figure has a time axis marked only at t = 0 and t = 1. Separately, the figure at 486-494 is a byte-for-byte repeat of the figure at 340-347 - same data, same code, same styling - produced to show that the efficient method gives the same answer, which 471-473 has already established numerically to six decimals; and neither figure marks the reservation wage that 350 says is the point of the plot.

### Low severity
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 713. *Example:* iid.


## Strengths

- The efficiency improvement is earned in three steps and then checked: the employed worker's Bellman equation is solved for $v_e$ in closed form (361-364), substituted to leave a single fixed-point problem in $v_u$ (370-377), and the resulting reservation wage is printed against the first method's to six decimals with their difference (471-473).
- `P_cumsum` is carried in the `Model` tuple and the lecture says why in both places it matters - at 202-203 where the field is introduced and again at 536-541, where the inverse-transform sampling that needs it is explained.
- Ergodicity is argued rather than asserted: 716 gives the reason (irreducibility) and 722-724 lists the three transitions that make the chain on (status, wage) irreducible, before the time-average-equals-cross-section claim is stated at 734.
- The two unemployment rates being compared come from genuinely different code paths - a 2,000-period single-agent Python loop and a vmapped 20,000-agent `fori_loop` - and 754-760 explains why the second routine exists instead of reusing the first.
- The Markov generalisation is introduced by naming exactly what changes from the IID lecture (125-127), and the $(Ph)(w)$ operator that the rest of the lecture leans on is introduced with a parenthetical telling the reader to read it as a matrix times a column vector (148-154).

## Recommended actions

1. Change `ax1.set_xticks((0, 1))` at 651 to `set_yticks` - as it stands the main simulation figure's top panel has no usable time axis.
2. Add `mystnb: figure: caption/name` metadata to the five un-named figure cells (339, 486, 505, 633, 951) and to the two figures produced by `plot_cross_sectional_unemployment` at 916 and 925, and drop the five `figsize` overrides (340, 487, 515, 642, 870) unless the aspect ratios are deliberate (qe-fig-005 x5, qe-fig-001 x5).
3. Delete the duplicate figure at 486-494 - the numeric comparison at 471-473 already makes the point - and mark $\bar w$ on the figure at 340 so that 350's claim about the intersection can be seen.
4. Move the four `set_title` strings (650, 660, 676, 880) into mystnb captions (qe-fig-003, 4 occurrences).
5. Make the ergodicity comparison self-contained: recompute the time-average rate in the cell at 897, or return `unemployed_indicator` from the simulation, instead of reaching back into the plotting cell at 664.
6. Fix the prose: repair the clause at 691-693, restate 708-714 so the subject and predicate are not separated by a bullet list, write 'IID' at 713 (qe-writing-009 (proposed), proposed), split the two-sentence paragraph at 937 (qe-writing-001), and either answer the question at 525 or promote it to an exercise.
7. Clear the PEP8 items: strip the trailing whitespace at 210, 260, 289, 292, 341, 343, 435, 488 and 490, space the annotated defaults at 284-285, pull the four over-length lines (455, 589, 787, 864) under 79 characters, and align the continuation at 657.
