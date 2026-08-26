# ifp_egm_transient_shocks

- **Series:** lecture-python.myst
- **File:** `lectures/ifp_egm_transient_shocks.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-006` ×9; `qe-writing-002` ×3; `qe-writing-003` ×1, +2 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-001` ×4; `qe-code-004` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×7; `qe-fig-003` ×3; `qe-fig-008` ×10, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 6. *Lines:* 590, 592, 595, 598, 601, 604. *Example:* time.time(.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 7. *Lines:* 365, 616, 631, 795, 933, 982, 1048. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 10. *Lines:* 368, 369, 618, 619, 656, 658, 937, 944, 994, 1068. *Example:* plot() without lw=.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 9. *Lines:* 59, 69, 174, 189, 377, 384, 814, 821, 894. *Example:* H2 Title Case: 'The Household Problem' (Household, Problem).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 267, 656, 730, 848. *Example:* line 267 closes a hanging-indent signature with `    ) -> np.ndarray:` at 4 spaces, leaving arguments at body indent (E121/E125); the pattern recurs at 331, 435, 516, 713, 758 and 849. Line 656 puts a space before the comma in `+ y_bar(k) , label=label` (E203). Lines 730 and 774 bind lambdas to names where PEP8 asks for `def` (E731), and 770 and 774 are dead locals into the bargain. Line 848 writes the annotated default without spaces, `p: float=0.01` (E252). Trailing whitespace at 309, 473, 638, 639 and 862.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 3. *Lines:* 805, 940, 947. *Example:* .set(xlabel='assets', title=.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 34, 129, 816. *Example:* the lecture tells the reader at 66-67 to consult `` {doc}`ifp_egm` `` for the extensive discussion, and then reproduces that lecture's EGM derivation almost verbatim at 129-171 - 'To do so we use the EGM', 'We begin with an exogenous savings grid', 'We fix a current guess of the policy function', the boundary case, the endogenous grid, the interpolation - which is ifp_egm.md:273-320 with the integral added. Line 34 reads 'we continue extend the IFP' and line 816 'Lets' look at wealth inequality by computing some standard measures of this phenomenon', both carried over from sibling lectures with their defects.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 2. *Lines:* 570, 706. *Example:* 2 spaces.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 934. *Example:* figsize=.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 1017. *Example:* `` {cite} `` in narrative flow: '`` {cite} ``'.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 968. *Example:* exercise `ifp_egm_ex1` instructs the reader to 'Step `r` through `np.linspace(0, 0.016, 4)`' (968), and its own solution uses `np.linspace(0, 0.04, 4)` with a comment justifying the different upper bound (983-984). A reader who follows the exercise as written produces a different figure from the one shown.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 809. *Example:* the lecture's whole contribution over `` {doc}`ifp_egm` `` is the transient shock, and its effect is described in words rather than shown: 'As was the case in `` {doc}`ifp_egm` ``, the wealth distribution looks implausible. While we have at least gained a nontrivial right tail, we still have a left skew' (809-811). The right tail that was gained is exactly what a two-panel comparison of the two models' wealth histograms - or the two consumption policies - would display, and the lecture already draws seven figures.


## Strengths

- The single change from the predecessor is threaded through consistently: the Euler equation gains an integral against $\phi$ (112-118, 142-150), the solver integrates it by Monte Carlo over `η_draws`, and `y_bar` documents in its docstring exactly which expectation it is approximating and how (637-651), with the approximation written out in the text at 674-677.
- The NumPy and JAX implementations are cross-checked before either is timed (542-620), so the reported speedup rests on the two paths agreeing.
- The interest-rate experiment is run as a hypothesis test: the conjecture is stated first (898-899), then computed over eight values of $r$ (903-929), and the finding is reported with its limits - the effect is real, the differences are minor, and $r$ cannot be pushed further without violating $\beta R < 1$ (954-958).
- The lecture is candid about the model's failure and points at the argument that no model of this structure can succeed (885-887), then names the sequel that tries to fix it (889-890) - so the disappointing wealth distribution is framed as a result rather than an embarrassment.
- Every display carries a label distinct from its predecessor's - `eqst_ts`, `eqeul1_ts`, `cfequ_ts` - and the Euler equation is cited at 127 and 129 by reference; the code names shocks and parameters in unicode (`η_draws`, `β`, `γ`, `Π`, `σ`) to match the mathematics.

## Recommended actions

1. Remove or repair the dead warm-starts: all three sweeps assign `c_init = c_vec` and `a_init = a_vec` at the end of the loop body (926-928, 995-997, 1065-1067) with a comment saying the last solution seeds the next solve, but the top of each body immediately overwrites both from `s` (916-917, 990-991, 1056-1057), so the stated optimisation never happens.
2. Reconcile exercise `ifp_egm_ex1` with its solution: the prompt says `np.linspace(0, 0.016, 4)` (968) and the solution uses `np.linspace(0, 0.04, 4)` (984).
3. Add the comparison the text asserts: plot this model's wealth distribution (or consumption policy) against the one from `` {doc}`ifp_egm` ``, so 'we have at least gained a nontrivial right tail' (811) is visible rather than claimed.
4. Sentence-case the eight Title Case headings at 59, 174, 189, 377, 384, 814, 821 and 894 (qe-writing-006), and fix 'we continue extend' (34), "Lets'" (816) and 'Following on from Exercises 1' (1013).
5. Figure hygiene, the largest mechanical block here: add mystnb name/caption metadata to the seven figure cells at 365, 616, 631, 795, 933, 982 and 1048 (qe-fig-005), set `lw=2` on the ten plot calls at 368, 369, 618, 619, 656, 658, 937, 944, 994 and 1068 (qe-fig-008), move the embedded titles at 805, 940 and 947 into captions (qe-fig-003), and drop `figsize=` at 934 (qe-fig-001).
6. Cut the derivation duplicated from `` {doc}`ifp_egm` `` at 129-171 down to what is new here - the integral over $\eta'$ - and point at the predecessor for the rest, which is what 66-67 already promises.
7. Code housekeeping: replace the six bare `time.time()` readings at 590-604 with `quantecon.Timer` (qe-code-004); fix the closing-paren indents, the `p: float = 0.01` annotation, the two lambda bindings and the dead locals `n_z` and `σ` at 770 and 774; clear the trailing whitespace at 309, 473, 638, 639 and 862; and make the narrative citations at 686 and 1017 `{cite:t}` (qe-ref-001).
