# inventory_dynamics

- **Series:** lecture-python.myst
- **File:** `lectures/inventory_dynamics.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.9 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-005` ×3; `qe-writing-003` ×2; `qe-writing-002` ×3, +1 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 9.5/10 | `qe-code-004` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×6; `qe-fig-008` ×6; `qe-fig-001` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 6. *Lines:* 161, 181, 209, 252, 293, 383. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 6. *Lines:* 168, 169, 170, 185, 186, 290. *Example:* plot() without lw=.

### Medium severity
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 142. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 55, 438, 510. *Example:* 55 spends 35 words ("While our Markov environment and many of the concepts we consider are related to those found in our lecture on finite Markov chains, ...") to say that the state space here is continuous rather than finite; 438 loses its verb agreement - "we have written a specialized JAX-jitted function and using `jax.vmap` to use parallelization across firms" - and says "use" twice; and the printed label at 510, "Frequency of at least two stock outs", names the wrong event, since the exercise (424-425) and the function docstring (446-450) both count restocks, and a firm that restocks at $X_t \leq s$ has not run out of stock.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 159, 272. *Example:* "Let's run a first simulation, of a single path:" at 159 sits after the cell that actually runs it (153-157) and introduces the cell that only plots it, so the reader meets the result before the announcement; and 272 asks the reader to consult "figure with paths above" to see why the distribution is bimodal, which means jumping back over two intervening figures to the one at 181 - the bimodality argument is never made in the text where it is stated.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 42, 77, 275. *Example:* the file contains no bold at all, so every term it defines arrives in plain text: "so-called s-S inventory dynamics" (42), which is the subject of the lecture; the notation `$a^+ := \max\{a, 0\}$` (77), introduced mid-sentence as "With notation"; and "kernel density estimator" (275), where the term is carried by a Wikipedia link instead. The one emphasis mark in the file, *new* at 142, is correctly italic.

### Low severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 1. *Lines:* 507. *Example:* %%time.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 215. *Example:* figsize=.


## Strengths

- The `{note}` at 141-147 anticipates the reader's objection to `X.at[t].set(x_new)` - that copying an array every period looks wasteful - and answers it with the XLA in-place argument, so the JAX idiom is explained where it is first used rather than assumed.
- Notation is deliberately minimal and there is nothing decorative in it: $X_t$, $D_t$, $Z_t$, $\psi_t$, $a^+$, with no `\mathcal`, no transposes and no bold matrices anywhere, and the lowercase $\psi$ for the marginal density is the correct case under proposed qe-math-015 (proposed).
- The `Firm` NamedTuple uses unicode `μ` and `σ` (103-104) that read identically to the $\mu$ and $\sigma$ of the display at 91, and each field carries a one-line comment saying what it is.
- The two-panel figure at 209-247 is the one that earns its place: sample paths on the left with a vertical rule at $T$ and the black dots marking $X_T$, the cross-section histogram of exactly those dots on the right - it makes "marginal distribution of $X_T$" concrete before $\psi_T$ is used again.
- Both exercises use gated `exercise` + `solution-start`/`solution-end` with `:class: dropdown` and carry labels (`id_ex1`, `id_ex2`), and the solution to the first reuses `plot_kde` from 284 rather than re-implementing the density estimate.
- "IID" is written in the correct form both times it appears (75, 94).

## Recommended actions

1. Add `mystnb: figure: caption`/`name` metadata to the six un-named figures (161, 181, 209, 252, 293, 383) - the largest fix here, and the one that lets "figure with paths above" (272) and "the histogram just above" (299) become `{numref}` references.
2. Add `lw=2` to the six line plots at 168, 169, 170, 185, 186 and 290, but leave `lw=0.5` at 192 as it is: thin lines are what make the 400 overlaid paths readable.
3. Bold the three definitions - s-S inventory dynamics (42), $a^+$ (77) and kernel density estimator (275) - so the lecture's central term is not the only one in the file typeset like ordinary prose.
4. Rewrite line 438 ("and using `jax.vmap` to use parallelization") and change the printed label at 510 from "stock outs" to "restocks", matching the exercise statement and the docstring.
5. Move the sentence at 159 above the simulation cell at 153, and split the two-sentence paragraph at 142 into two blocks (qe-writing-001).
6. Replace `%%time` at 507 with the `quantecon.Timer` context manager (qe-code-004), and drop `figsize=(11, 6)` at 215 unless the side-by-side panels need the extra width.
7. Compress line 55 to something like "Unlike the finite Markov chains lecture, the state space here is a continuum".
