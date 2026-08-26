# sir_model

- **Series:** lecture-python.myst
- **File:** `lectures/sir_model.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, links  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-006` ×5; `qe-writing-003` ×4; `qe-writing-007` ×3. |
| Math         | 7.5/10 | `qe-math-001` ×3; `qe-math-009` ×2. |
| Code         | 8.5/10 | `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-005` ×1; `qe-fig-008` ×2. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 5. *Lines:* 68, 82, 236, 284, 347. *Example:* H2 Title Case: 'The SIR Model' (Model).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 217, 307, 56, 293. *Example:* two lambdas are bound to names where the rule asks for `def` - `G = lambda x, t: F(x, t, R0)` at 217 and `R0 = lambda t: R0_mitigating(t, η=η)` at 329 (E731) - and 307 writes `η_vals = 1/5, 1/10, 1/20, 1/50, 1/100` with no spaces around any of the five divisions (E226) on a line whose whole content is arithmetic. 56 imports `from numpy import exp` alongside `import numpy as np` at 55, so 293 uses the bare `exp` while every other numpy call in the lecture goes through `np.`; one of the two conventions should go. And `R0` is bound four different ways: a parameter of `F` (167), a local inside `R0_mitigating` (293), a module-level lambda (329), and a loop variable over a tuple of lambdas (377) - so the same three characters mean a scalar, a function and a loop item within 210 lines. flake8 finds nothing else: the file is short, spacing is otherwise clean, and Unicode Greek is used throughout (`γ`, `σ`, `β`, `η`, `ν`).
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 261, 317. *Example:* plot() without lw=.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 3. *Lines:* 103, 105. *Example:* unicode `σ` inside a math environment.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 2. *Lines:* 144, 353. *Example:* the reproduction number is written four ways in a 412-line lecture, and the text flags only one of the collisions. 144 introduces $R(t)$, and 146-147 helpfully warns that "$R(t)$ is different to $R$, the symbol that represents the removed state". Then 353-354 switches to $R_t$ for the same object, the code calls it `R0` throughout (167, 179, 190, 211, 243, 292-294, 329, 370-377) even though 190 says it "can be either constant or a given function of time" - so `R0`, conventionally the *basic* reproduction number, names a time-varying $R(t)$ - and the figure legends print it as `$R0 = 1.60$` (244). A reader mapping the algebra onto the code has to hold $R$, $R(t)$, $R_t$ and `R0` apart, three of which are the same thing and one of which is a state. One symbol and one subscript convention would remove the whole problem, and 146-147 shows the author already noticed half of it.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 4. *Lines:* 39, 173, 211, 20. *Example:* the lecture calls its model SIR and implements SEIR. 39 says "a standard SIR (Susceptible-Infected-Removed) model", 68 heads the section "The SIR Model", and 70 then says "In the version of the SIR model we will analyze there are four states" - S, E, I and R at 74, where E is exactly the state the acronym at 39 omits, and $\sigma$ (103, 105) is exactly the extra parameter the exposed state requires. The word SEIR never appears. Second, the docstring of `F` at 173 says "R0 is the effective transmission rate", but 111 defines the transmission rate as $\beta(t)$ and 144 defines $R(t)$ as the **effective reproduction number** with $\beta(t) := R(t)\gamma$ - so the docstring names `R0` after a different object, and 274 repeats the error in prose ("lower effective transmission rates defer the peak of infections" describes an experiment that varies $R_0$). Third, `solve_path`'s default is bound once at definition: `def solve_path(R0, t_vec, x_init=x_0)` at 211 captures the `x_0` set at 204 ($i_0 = 10^{-7}$, about 33 people), and 361-364 then rebinds `x_0` to the 25,000-infection scenario without changing that default. The lecture gets the right answer only because 378 passes `x_init=x_0` explicitly; a reader who re-runs the Experiment 1 cell at 248 after reaching 364 silently gets the old initial condition. Fourth, the disease is spelled two ways: the H1 at 20 is "Modeling COVID 19" while the body writes "COVID-19" (28, 34). Also, $\nu$ enters the lecture only as `ν = 0.01` in code (394); no equation ever defines it.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 256, 244, 391. *Example:* `plot_paths` (256-266) sets no axis label, no y-label and no title - it calls `ax.plot`, `ax.legend` and `plt.show` and nothing else - and it draws seven of the lecture's eight figures (271, 281, 338, 344, 386, 401, 408). The quantities on those seven y-axes are not comparable: fraction of the population infected (271, 338), cumulative fraction infected (281, 344), cumulative *number* of deaths (401), and deaths per day (407), the last two scaled by `pop_size` so they run into the millions. Nothing on any chart says which; the only cue is the sentence immediately before the cell, so a reader who scrolls, or who sees the figures in a gallery, cannot tell a fraction from a body count. Adding two arguments to `plot_paths` and passing them at each of the seven call sites is the whole fix, and it is why qe-fig-006 measures zero here - there are no axis labels to be miscapitalised. Second, the legend is the *only* identifying text on those figures and it is broken: 244 builds `f'$R0 = {r:.2f}$'`, which renders as $R0$ - an italic $R$ times an italic $0$ - where $R_0$ is meant, while the sibling label at 308 gets it right with `fr'$\eta = {η:.2f}$'`. Third, the lecture has no admonition anywhere (Admonitions is `N/A`) and it needs one: 391, "Suppose that 1% of cases result in death", is the assumption that converts every remaining figure from epidemiology into a death toll, and it is delivered as a five-word sentence with no full stop.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 313. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- The model is stated once, completely, and in the form the code will take: the three differential equations as a labelled display (97-107), a bullet naming each of the three rate parameters in words (111-113), the reason the fourth state needs no equation (116-118), the definition of the cumulative caseload (120-121), and then the vector form $\dot x = F(x,t)$ at 128 that the implementation mirrors exactly in `F` (167-187).
- Every parameter value is sourced to a duration a reader can sanity-check: $\sigma = 1/5.2$ 'to reflect an average incubation period of 5.2 days' and $\gamma = 1/18$ 'to match an average illness duration of 18 days' (139-140), the population set to the US at 154, and the horizon given in both units at 228 ('550 days, or around 18 months').
- 146-147 stops to warn the reader about a notational collision it has just created - '(The notation is slightly confusing, since $R(t)$ is different to $R$, the symbol that represents the removed state.)' - which is the right instinct, and the kind of aside most lectures omit.
- `F` is written so that the interesting parameter can be either a number or a path, with the branch made explicit in one line - `β = R0(t) * γ if callable(R0) else R0 * γ` (179) - and 190 tells the reader that this is what makes the mitigation experiments possible; the same function then serves all three experiments unchanged.
- The three experiments are ordered so that each isolates one thing: constant $R_0$ across six values (236-282), then $R_0$ falling from 3 to 1.6 at five different speeds (284-345), then two lockdown-exit dates with the same initial conditions (347-387) - and the last one is stated in units a policy reader recognises, 'lifting lockdown in 30 days' against 'in 4 months' (353-354).
- The mortality section converts model output into the two quantities that were actually argued about in 2020 - cumulative deaths (400) and the daily death rate, $\nu\gamma$ times current infections (407) - and 411-412 states the resulting policy claim in one conditional sentence rather than overstating it.
- Bold is used for exactly the four terms the lecture defines - **transmission rate** (111), **infection rate** (112), **recovery rate** (113), **effective reproduction number** (144) - so qe-writing-005 has nothing to report.
- The source is credited precisely rather than generally: Atkeson's page, the NBER working paper number, and the specific additional results being replicated are all linked at 29, 33-34 and 349, and 36-37 states whose objective the lecture is serving.

## Recommended actions

1. Give `plot_paths` axis labels. It draws seven of the eight figures (271, 281, 338, 344, 386, 401, 408) with no x-label, y-label or title, and the y-quantities range from a population fraction to millions of deaths - add `xlabel` and `ylabel` parameters and pass them at each call, then fix `$R0$` to `$R_0$` in the legend labels at 244, which is currently the only text identifying those charts.
2. Call the model SEIR, or say why not: 39 expands the acronym as 'Susceptible-Infected-Removed' while 74 lists four states including exposed, and $\sigma$ exists only because of that state. The section heading at 68 and the sentence at 70 carry the same problem.
3. Fix the docstring at 173: `R0` is the effective reproduction number (144), not 'the effective transmission rate', which is $\beta(t) = R(t)\gamma$ (111, 144). Then correct the same slip in the prose at 274.
4. Remove the stale default: `x_init=x_0` at 211 captures the `x_0` from 204, and 364 rebinds `x_0` without changing it, so re-running any earlier experiment cell after 364 silently uses the wrong initial condition. Use `x_init=None` with an in-body fallback, or pass the initial condition at every call site.
5. Settle on one symbol for the reproduction number - $R(t)$ at 144, $R_t$ at 353-354, `R0` in code and `$R0$` in legends - and stop reusing the name `R0` for a parameter (167), a local (293), a lambda (329) and a loop variable (377).
6. Convert the two `lambda` bindings at 217 and 329 to `def`, space the five divisions at 307, and choose between `from numpy import exp` (56) and `np.exp`, since `numpy` is already imported at 55.
7. Put the mortality assumption in a `{note}`: 391 ('Suppose that 1% of cases result in death') is what turns the last three figures into death counts, and the lecture has no admonition of any kind. While there, give 391 a full stop and fix 411 ('the peak of curve').
8. Sweep the mechanical items: the five Title-Case headings (68, 82, 236, 284, 347), the three Unicode Greek characters inside the displayed system - `σ` at 103 and 105 and `γ` at 105, in the same `aligned` block where 101 correctly writes `\beta(t)` (qe-math-001) - the missing `mystnb` metadata on the figure at 313, and `lw=2` at 261 and 317. Note that the H1 at 20 wraps the title in an `{index}` role, which is why no rule checks its capitalisation.
