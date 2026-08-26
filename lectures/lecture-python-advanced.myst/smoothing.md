# smoothing

- **Series:** lecture-python-advanced.myst
- **File:** `lectures/smoothing.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `b83d6da399`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 6.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-005` ×8; `qe-writing-003` ×5; `qe-writing-002` ×6, +4 more. |
| Math         | 3/10  | `qe-math-010` (proposed) ×15; `qe-math-002` ×3; `qe-math-011` (proposed) ×1. |
| Code         | 7.5/10 | `qe-code-001` ×8. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×4; `qe-fig-006` ×4; `qe-fig-005` ×2, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 7.5/10 | `qe-link-002` ×6. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 8. *Lines:* 272, 282, 313, 632, 730, 920. *Example:* 730 writes `y.shape = (n, 1)`, which reshapes the caller's array in place - `y` here is `cp.y` (724), so the call at 914 permanently changes the state of the `ConsumptionProblem` instance and `consumption_complete(cp)` would fail on a (2,1) `y` at 696 if the two calls were ordered the other way; `y = y.reshape(n, 1)` avoids it. `complete_ss` carries five lines of commented-out code inside the function body (282-285, 290), including an alternative augmented state construction that the docstring's comment at 279-281 still refers to. Its signature declares `T=12` (272) but every call passes 80 (323). 632-635 uses mutable lists as default arguments for `y` and `P`. Spacing and layout: 313 and 316 carry double spaces inside array literals (`[α,  ρ1, ρ2]`, `[[1,  1.0, 0.]]`) and 316 mixes an int literal with floats; 312-314 indents the continuation to column 12 against an opening bracket at column 13; 920-921 indents a continuation to column 20 against an opening parenthesis at column 12; and 331 and 339 run past 90 characters where every other plot call in the file is wrapped.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 10. *Lines:* 330, 331, 338, 339, 919, 920, 922, 927, 928, 930. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 6. *Lines:* 87, 121, 126, 263, 362, 793. *Example:* raw link to python-intro.quantecon.org.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 3. *Lines:* 151, 177, 190. *Example:* apostrophe transpose `C'`.
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 15. *Lines:* 177, 184, 204, 236, 378, 381, 398, 493, 799, 809, …. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 6. *Lines:* 89, 364, 462, 487, 519, 775. *Example:* six sentences carry slips that a reader stumbles on: 89 "a prologomenon to a lecture on tax-smoothing"; 364 "In that incomplete markerts setting"; 462 "even if he consumers zero forevermore"; 487 "It is timely please to recall that the gross one-period risk-free interest rate..."; 519 "(Why is this is a plausible guess?)"; and 775 "where $\beta$ is the price at time $t$ of a risk-free claim on one unit of time consumption at time $t+1$", which has lost its "$t+1$" before "consumption". 461-463 is also a three-sentence paragraph where the rest of the lecture keeps to one.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 5. *Lines:* 190, 308, 331, 737, 938. *Example:* (i) 938-945 opens "In the graph on the left, for the same sample path of nonfinancial income $y_t$, notice that" and then gives two bullets, the second of which is entirely about the right-hand panel - the consumer's debt, plotted at 926-933. (ii) The comment at 737, `# Optimal decisions from (12) and (13)`, points at equation numbers that exist nowhere in the lecture; the equations meant are `` {eq}`cs_12` `` and `` {eq}`cs_13` `` at 868-880, which the prose at 900 cites correctly by label. (iii) The same conditional expectation is written two ways in adjacent displays: $\mathbb E_t b_{t+1}$ at 177 and 184, then $E_t b_{t+1}$ at 190, 196 and 199, in the three lines whose whole purpose is to identify the two. (iv) The simulation length is stored twice - `N_simul = 80` at 308 for the axes and the literal `80` passed at 323 for the simulation - while the function's own default `T=12` (272) is never used, so the figure is correct only as long as two unconnected constants stay equal. (v) The two panels of the first figure label the same series differently, `label='income'` at 331 and `label='Income'` at 339.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 8. *Lines:* 39, 42, 199, 431, 461, 510. *Example:* the lecture defines its two central terms twice, once in each convention, two lines apart: **complete markets** and **incomplete markets** in bold at 39-40, then *Complete markets* and *Incomplete markets* in italic at 42-44 where the actual definitions are given ("allow a consumer to buy and sell claims contingent on all possible states of the world"). The same split runs through the rest: bold definitions at 105 (**complete markets version**), 115 (**incomplete markets version**), 146 (**pricing kernel**), 426-427 (**one-period ahead Arrow securities**), 458-459 (**financial income**, **expenditures**) and 477 (**implied price**); italic definitions at 374 (*state*), 431 (*Exogenous* - "means that they are unaffected by the consumer's decisions", a definition in form as well as function), 462 (*natural debt limits*), 508 (*guess and verify*) and 834 (*Bellman equation*). 199 uses bold for emphasis, "is the **value** of time $t+1$ state-contingent claims", where 98 (*smooth*) and 519 (*tomorrow's*) correctly use italic for the same job; and 461 and 510 set `**Remark:**` and `**Guess:**` as bold labels standing in for directives.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 52. *Lines:* 26, 40, 42, 44, 54, 65, 68, 93, 99, 103, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 326, 916. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 329, 337, 918, 926. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 271, 907. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 4. *Lines:* 333, 342, 924, 933. *Example:* axis label `Periods`.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 1. *Lines:* 140. *Example:* decorated distribution `{\cal N}`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 461, 519. *Example:* 2 sentences in one paragraph.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 87. *Example:* mid-sentence 'Savings'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 3. *Lines:* 461, 519, 916. *Example:* the lecture's central claim about complete markets is that debt "switches between two values" indexed by the Markov state (609-612, 942-943), and the figure that is supposed to show it (916-935) never shows the state: `debt_complete[s_path]` is plotted as a line, so the reader sees a two-valued series but has no way to tell which periods are state 1 and which are state 2, in either panel. Shading the axes by $s_t$, or adding a third panel plotting the state path that 909 already computes, would connect the two-valued debt to the Markov chain, and the two-state chain with its transition matrix $P$ is never drawn anywhere in the lecture. Second, the lecture asks the reader two direct questions - "(Why is this is a plausible guess?)" (519) and the parenthetical at 562 about $s_0 = 2$ - and has no `{exercise}` or `{hint}` directive anywhere to hold them, so both read as asides. Third, `**Remark:**` at 461-463, which sets aside the natural debt limits the whole complete-markets construction quietly assumes, is precisely a `{note}`.

### Low severity
_None found._


## Strengths

- The comparison the lecture exists to make is run as a controlled experiment: 908-914 builds one `ConsumptionProblem`, draws one Markov path, and feeds both to `consumption_complete` and `consumption_incomplete`, so the two panels at 916-935 differ only in market structure and the bullets at 941-945 can be checked against them.
- The complete-markets counterpart of Hall's interest-rate assumption is derived rather than asserted: 468-472 posits $q(j\,|\,i) = \beta P_{ij}$, 474-482 shows that buying one unit of consumption for sure then costs $\sum_j \beta P_{ij} = \beta$, and 487-488 closes the loop by reminding the reader that the gross risk-free rate is the reciprocal of that price.
- The complete-markets solution is an explicitly labelled guess-and-verify carried all the way through: the guess (510-519), the budget constraints it implies (523-532), the count of two equations in three unknowns (555-556), the third equation supplied by the $t=0$ constraint under $s_0 = 1$ (558-570), the two conclusions $b(1) = b_0$ (577-581) and the linear equation for $b(2)$ (585-592), and then 613 stating that the guess has been verified.
- The linear-state-space version is placed first for a reason the lecture gives (73-74, "because it is so closely linked to earlier lectures"), and the object that makes it work is introduced as a deliberate guess - the pricing kernel `` {eq}`cs_14` `` at 148-152 - followed immediately by the identity that makes it usable, $\beta\int b(x_{t+1})\phi(x_{t+1}|Ax_t, CC')dx_{t+1} = \beta \mathbb E_t b_{t+1}$ (176-178).
- The key discounted-value term is developed in the five forms a reader needs, in order: definition (830-832), Bellman equation (836-838), two scalar equations for the two-state case (844-850), vector form $\vec v = \vec y + \beta P \vec v$ (854-856), and the closed form $(I - \beta P)^{-1}\vec y$ (862-864) - which is the single line the code implements at 731.
- The two sets of results are summarised in parallel lists that answer the same questions in the same order - 598-615 for complete markets, 884-896 for incomplete markets - so the reader can compare the two models without re-deriving either.
- The augmented linear system in `consumption_complete` (691-711) is built so that the algebra is visible in the matrices: the extra first row carries the $t=0$ budget constraint at the initial state `init`, which is exactly the third equation that 558-570 introduces to pin down $\bar c$.
- 461-463 names the technicality it is setting aside - that state-contingent debt choices must respect natural debt limits - rather than leaving a silent gap, and says a later lecture will treat it.

## Recommended actions

1. Make the first figure reproducible: 321-322 draws the seed from the unseeded global RNG (`s = np.random.randint(0, 10000)` then `np.random.seed(s)`), so the published figure changes on every build, while the second figure fixes `random_state=1` (653, 663) - the lecture uses two seeding conventions and only one of them is repeatable.
2. Fix the orientation of the closing discussion at 938-945, whose second bullet describes the right-hand panel under the heading "In the graph on the left".
3. Replace the phantom equation numbers in the comment at 737 with the real labels `` {eq}`cs_12` `` and `` {eq}`cs_13` ``, and settle on `\mathbb E_t` for the conditional expectation - 190, 196 and 199 write plain $E_t$ for the operator that 177 and 184 write as $\mathbb E_t$.
4. Resolve the emphasis convention on the lecture's own two key terms: **complete markets** and **incomplete markets** are bold at 39-40 and italic at 42-44, where the definitions actually appear; then apply the same choice to the other twelve defined terms and un-bold the emphasis at 199.
5. Clean the code cells: delete the five commented-out lines inside `complete_ss` (282-285, 290), replace `y.shape = (n, 1)` at 730 with a non-mutating reshape (it currently rewrites the caller's `cp.y`), and remove the duplicated simulation length - `N_simul = 80` at 308, the literal `80` at 323, and the unused default `T=12` at 272.
6. Show the Markov state in the second figure - shade the axes by $s_t$ or add a panel for the path already computed at 909 - so the claim at 942-943 that complete-markets debt "oscillates between two values that are functions of the Markov state" can be seen; and turn `**Remark:**` (461) into a `{note}` and the two questions at 519 and 562 into `{exercise}` directives.
7. Sweep the mechanical load: the 52 double-space runs, the six raw `python-intro.quantecon.org` links (87, 121, 126, 263, 362, 793) rewritten as `{doc}` references, the four embedded `set_title` calls (329, 337, 918, 926) moved into `mystnb` captions with `name:` fields, the ten `plot()` calls without `lw=2`, the four capitalised axis labels, the three apostrophe transposes, and the `{\cal N}` at 140; also replace the bare author-year references "Hall (1978)" at 761 and 791 with `{cite}`Hall1978``, which the lecture uses correctly at 40, 46 and 757.
