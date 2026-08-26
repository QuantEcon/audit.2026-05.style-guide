# ak_aiyagari

- **Series:** lecture-python.myst
- **File:** `lectures/ak_aiyagari.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 7.4 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-005` ×3; `qe-writing-003` ×3; `qe-writing-002` ×4, +2 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7/10  | `qe-code-001` ×4; `qe-code-003` ×1; `qe-code-004` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 4/10  | `qe-fig-003` ×18; `qe-fig-005` ×8; `qe-fig-008` ×19, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×3. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 6. *Lines:* 603, 988, 1202, 1255, 1338, 1420. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 18. *Lines:* 570, 610, 617, 1039, 1040, 1041, 1153, 1207, 1212, 1224, …. *Example:* plt.title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 8. *Lines:* 563, 599, 1136, 1201, 1252, 1337, 1373, 1417. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 19. *Lines:* 565, 605, 606, 612, 613, 989, 990, 991, 1026, 1027, …. *Example:* plot() without lw=.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 53. *Lines:* 30, 33, 34, 44, 99, 101, 109, 193, 246, 253, …. *Example:* 2 spaces.

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 456, 565, 1019, 1259. *Example:* ten code lines exceed 79 characters, the worst being 104 at line 565 and 86 at 742 and 959 (742, 959, 1094, 1142, 1192, 1243, 1249, 1324, 1407 are the rest); three places use backslash line continuations where parentheses are the PEP8 preference (1019-1021, 1045-1046, 1123-1124); and four continuation lines are indented one column off their opening bracket (457, 730, 1260, 1425). Line 1302 also carries trailing whitespace.
- **[qe-code-003]** — Package installation at lecture top. *Count:* 1. *Lines:* 1. *Example:* non-Anaconda import with no install cell: ['jax'].
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 3. *Lines:* 519, 557, 742. *Example:* %time.
- **[qe-ref-001]** — Use correct citation style. *Count:* 3. *Lines:* 33, 34, 35. *Example:* `` {cite} `` in narrative flow: 'in   `` {cite} ``'.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 91, 145, 159, 265. *Example:* the environment is described three times over. Line 91 ("An agent's effective labor supply depends on a life-cycle efficiency profile and an idiosyncratic stochastic process") adds nothing to 87-89 immediately above it; lines 141-145 restate 87-89 again under a new heading; and "Key features" (155-171) restates the Overview bullets at 39-44. Line 159 also states something the model does not contain - "asset holdings typically follow a lifecycle pattern of accumulation during working years and decumulation during retirement" - when every agent supplies labour for all 50 periods and $l(j) = 0.5 + 0.05j - 0.0008j^2$ is still 1.03 at $j = 49$. Line 265 is a 34-word sentence that begins "For a candidate sequence of prices interest rates $r_t$ and wages $w_t$".
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 203, 1369, 1439. *Example:* line 150 promises that agents "hold assets $a_{i,j,t}$ (subject to borrowing constraints)", but the household problem at 197-211 constrains only $c \geq 0$ and no borrowing limit is ever stated - it enters silently as `a_min=0.` in `create_household` at 390. Line 1369 reads "Notice how prices and quantities respond immediately to the anticipated tax rate increase" in a section titled "Experiment 2: Preannounced tax cut", whose figure at 1380 is annotated `tax cut`. And the lecture stops at 1439 in the middle of a figure cell: two pairs of 3-D consumption mean/variance surfaces are produced (1252-1273, 1417-1439) and neither pair is discussed, there is no concluding section, and the four questions the Overview poses at 39-44 are never answered.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 157, 163, 167. *Example:* the three organising concepts of the "Key features" section - *Lifecycle patterns* (157), *Within-cohort heterogeneity* (163) and *Cross-cohort interactions* (167) - are each named and then explained, which is a definition, and each is set in italic. The lecture uses no bold outside the `prf:algorithm` block at 916-956, so there is no competing convention; it also switches emphasis markers mid-file, using `_backward induction_` and `_forward iteration_` with underscores at line 273 where everything else uses asterisks.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 326, 1252. *Example:* the age-efficiency profile $l(j)$ is the primitive that generates the entire life-cycle savings motive the lecture is about, and it is never plotted: it appears only as three magic constants at line 326 (`l1, l2, l3 = 0.5, 0.05, -0.0008`) and a one-line quadratic at 332, so the reader has no idea what shape it has or where it peaks. Separately the two pairs of 3-D surfaces at 1252-1273 and 1417-1439 are the lecture's punchline - how the reform moves the mean and the *dispersion* of consumption across ages and dates - and they are drawn at `figsize=[20, 20]`, 170 lines apart, with no shared colour scale and no side-by-side comparison of the two experiments.

### Low severity
_None found._


## Strengths

- The algorithm is written out as a labelled `prf:algorithm` block (916-956) with inputs, outputs, the outer while loop, the backward-induction and forward-simulation passes, the convergence metric and the damped price update - so the 90 lines of `path_iteration` that follow have a specification to be read against.
- The two directions of the computation are separated into `solve_backwards` (826-857) and `simulate_forwards` (883-911), and line 790 says exactly why two steady states are needed: the initial one for the forward pass's initial condition, the final one for the backward pass's continuation values.
- Every heavy step is timed with `%time ... .block_until_ready()` (519, 557, 742) and line 516 explains why `block_until_ready` is necessary with JAX's asynchronous dispatch - a trap that silently reports near-zero times.
- The marginal savings distributions at 563-575 are read back to the reader age group by age group (578-592), each bullet naming the colour and the age it belongs to, so the five overlaid curves are interpretable without a legend lookup.
- The step from `ak2`'s two-period model to fifty cohorts is handled explicitly (1157-1165): the lecture says the representative young/old aggregation no longer exists, then defines two equal-sized age groups splitting at age 25 so the transition figures stay comparable with the earlier lecture's.

## Recommended actions

1. Write the discussion the lecture is missing: interpret the four 3-D surfaces (1252-1273, 1417-1439), compare the two experiments, and close with a section that answers the four questions posed at 39-44.
2. Move the eighteen embedded matplotlib titles into figure captions (570, 610, 617, 1039-1041, 1153, 1207, 1212, 1224, and the rest) and add `mystnb: figure: caption/name` metadata to the eight bare figures at 563, 599, 1136, 1201, 1252, 1337, 1373 and 1417 (qe-fig-003 18 occurrences, qe-fig-005 8 occurrences - together the largest mechanical load here).
3. Collapse the six verbatim copies of the consumption-computation block (1117-1129, 1136-1154, 1181-1199, 1235-1249, 1313-1330, 1399-1414) into one function; each copy recomputes `ap`, `δ`, `inc` and `c` identically, and the cell at 1106-1108 computes an `ap` that is immediately overwritten at 1120.
4. Set `lw=2` on the nineteen plot calls that lack it (565, 605, 606, 612, 613, 989, 990, 991, 1026, 1027 and nine more) and drop the six `figsize=` overrides at 603, 988, 1202, 1255, 1338 and 1420 - `figsize=[20, 20]` at 1255 and 1420 in particular (qe-fig-008 19 occurrences, qe-fig-001 6 occurrences).
5. Plot the age-efficiency profile $l(j)$ before it is used, and state the borrowing constraint in the household problem at 203-208 rather than leaving it to `a_min=0.` at line 390.
6. Fix "tax rate increase" at 1369 (the experiment is a cut) and "Sum across cohorts both" at 289, and cut the duplicated environment description at 91, 141-145 and 155-171.
7. Sweep the code hygiene: replace `%time` with the `quantecon` `Timer` context manager at 519, 557 and 742 (qe-code-004, 3 occurrences), collapse the 53 double spaces (qe-writing-008, 53 occurrences), wrap the ten over-length lines, remove the unused `verbose` parameter of `find_ss` (669, passed as `True` at 736 with no effect), the unused `firm` parameter of `solve_backwards` (827), the unused `num_action` bindings at 481, 803 and the `ϕ, k_bar = 0., 0.` machinery at 308-314 that makes `V_bar` a constant zero.
