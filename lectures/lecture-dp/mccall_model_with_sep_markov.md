# mccall_model_with_sep_markov

- **Series:** lecture-dp
- **File:** `lectures/mccall_model_with_sep_markov.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-005` ×2; `qe-writing-003` ×3; `qe-writing-002` ×4, +3 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-001` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×5; `qe-fig-003` ×4; `qe-fig-001` ×5. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 210, 284, 619, 787, 864, 874. *Example:* eighteen lines carry trailing whitespace, including inside code cells (210, 260, 289, 292, 341, 343, 488, 490); `tol: float=1e-6` and `max_iter: int=1_000` (284-285) omit the spaces PEP8 requires around a default on an annotated parameter (E252), which `create_js_with_sep_model` gets right eight lines earlier (`n: int = 200`, 221); `for t in range(T)` (619) never uses `t`; lines 787 (81 chars) and 864 (86 chars) exceed 79 (E501); and 874-876 pass `density=True` together with a `weights` array that already sums to one, so the histogram is normalised twice while the comment above claims one normalisation. Add to that the model unpacking at 259, 271, 287, 392, 442, 564 and 610, which binds eight names where at most four are read.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 5. *Lines:* 340, 487, 515, 642, 870. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 339, 486, 505, 633, 951. *Example:* code-cell figure without mystnb figure metadata.

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 650, 660, 676, 880. *Example:* .set_title.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 937. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 110, 350, 691, 728. *Example:* 'positive correlation means that a high current $w$ is often leads a high new draw' (691-693) has a stray verb. Line 728 puts an equals sign in a sentence: 'the ergodic theorem guarantees that time averages = cross-sectional averages'. Line 350 has a comma between a symbol and its conjunction, 'the intersection of $v_e$, and the continuation value function'. Line 110 opens 'Actually, in practice, we approximate this wage process as follows' with two hedges doing the same job. Also 'the unemployed agents value function' at 435-436 wants an apostrophe, and 713-714 splits 'is Markovian ... and ergodic' with a twelve-word clause so that 'and ergodic' arrives adrift from its verb.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 202, 651, 903. *Example:* line 651 sets the wrong axis: `ax1.set_xticks((0, 1))` on the employment-status panel, whose x axis is time running 0 to 2000, so the panel is drawn with exactly two tick marks at t=0 and t=1. It should be `set_yticks`, which is what the sibling lecture writes for the identical panel (`mccall_fitted_vfi.md:572`) - a copy that drifted, and it visibly breaks the figure. Line 202-203 promises that the reason `P_cumsum` is stored in the model is 'explained below', and the explanation arrives 330 lines later at 536-541, after `P_cumsum` has been unpacked and ignored in five functions (259, 271, 287, 392, 442). And line 903 reads `unemployed_indicator`, a name created at 664 inside a plotting cell 240 lines earlier, so the ergodicity comparison - the point of the whole section - silently depends on the reader having executed a figure cell.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 182, 716. *Example:* there is no bold and no italic anywhere in the file - the only `**` in it is the exponent at 197 - yet the lecture introduces several terms that want marking: 'a reservation wage strategy' at 182, 'the inverse transform method' at 536-537, and 'Ergodicity holds as a result of irreducibility' at 716, which names two properties for the first time in one sentence. The lecture this one builds on (37-38) bolds **continuation value** and **reservation wage** at their definitions, so a reader moving between the two loses the visual cue.

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 92. *Example:* '### The wage offer process' (92-114) is the one thing that distinguishes this lecture from its predecessor, and it is entirely prose: an AR(1), a Tauchen discretisation to a 200-point grid, and the claim that 'the higher the current wage offer, the more likely we are to get a high offer tomorrow' (105-106). Nothing shows it. A heatmap of $P$, or two or three sample paths of $W_t$ at different $\rho$, would make the persistence visible - and it is the property the closing paragraph at 686-693 has to appeal to in order to explain why the agent so often moves straight from one job to another.
- **[qe-writing-009 (proposed)]** — Write "IID" — not "i.i.d." or "iid". *Count:* 1. *Lines:* 713. *Example:* iid.


## Strengths

- The model is solved twice and the two answers are checked against each other: the direct two-vector iteration (253-315) and then the reduction that expresses $v_e$ in closed form and iterates on $v_u$ alone (358-455), with 470-473 printing both reservation wages and the difference between them - so 'we can do much better' (356) is verified rather than claimed.
- The operator notation is introduced with an explicit instruction for how to read it - '(To understand this expression, think of $P$ as a matrix, $h$ as a column vector, and $w$ as a row index.)' (154) - and then $(Pv_u)(w)$ is used consistently in every subsequent display (159, 168, 179, 363, 374), so the transition from sums to matrix products costs the reader nothing.
- The ergodicity section (697-746) is unusually careful for a lecture at this level: it states what will be compared, argues irreducibility from three specific transitions the model permits (720-724), writes the limit it implies (734), notes the burn-in caveat (737-739), and then tests it numerically at 897-911 - claim, reason, caveat, measurement.
- Why `P_cumsum` exists is explained at the point of use rather than left as an optimisation: the inverse-transform method is described (536-538) and then implemented with `jnp.searchsorted(P_cumsum[wage_idx, :], ...)` (569-571), with a comment saying which method it is.
- The two simulation routines are contrasted before either is used - full history versus final state, Python loop versus `lax.fori_loop`, and why that matters for vmap (756-760) - so the reader knows why the same model is simulated two different ways.
- Density and CDF conventions are clean throughout: lowercase $\pi$ for the stationary distribution (726, 734), $P(w, w')$ for the transition kernel, and no uppercase/lowercase confusion between them (qe-math-015 (proposed)).

## Recommended actions

1. Change `ax1.set_xticks((0, 1))` to `set_yticks` at 651. As written, the employment-status panel of the lecture's main simulation figure has a time axis with two ticks on it.
2. Figures are the weakest category (5.5/10) and it is all mechanical: add mystnb caption/name metadata to the 5 code-cell figures (339, 486, 505, 633, 951), drop the 5 hand-set `figsize` (340, 487, 515, 642, 870) and move the 4 `set_title` calls into captions (650, 660, 676, 880).
3. Add a figure to '### The wage offer process' - a heatmap of $P$ or sample $W_t$ paths at two values of $\rho$ - since persistence is this lecture's only substantive addition to its predecessor and is currently invisible.
4. Compute `unemployed_indicator` where the ergodicity comparison uses it (897-908) instead of relying on the name defined at 664 inside a figure cell, and either move the `P_cumsum` explanation (536-541) up to line 202 where it is promised or drop the forward reference.
5. Strip the trailing whitespace on 18 lines (141, 165, 176, 210, 260, 289, 292, 341, 343, 362, 371, 435, 488, 490, 546, 549, 711, 714), fix the annotated defaults at 284-285, and wrap lines 787 and 864.
6. Repair the prose: 'is often leads' at 691, the equals sign in the sentence at 728, the comma at 350, the doubled hedge at 110, the missing apostrophe at 435; write 'IID' for 'iid' at 713 (qe-writing-009 (proposed), proposed) and split the two-sentence paragraph at 937.
7. Bold the terms at their definitions - reservation wage strategy (182), inverse transform method (536), irreducibility and ergodicity (714-716) - to match the treatment in `mccall_model_with_separation`; gloss the indicator $\mathbb{1}\{\cdot\}$ at 734, which is the file's only unexplained notation; give the question at 525 ('Can you provide an intuitive economic story...') either an answer or an `{exercise}` directive; and consider folding the two-line '## Lower unemployment compensation (c=0.5)' section (919-926) into exercise 1, which asks for the same sweep done properly.
