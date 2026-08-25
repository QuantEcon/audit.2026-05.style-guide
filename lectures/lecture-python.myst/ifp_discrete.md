# ifp_discrete

- **Series:** lecture-python.myst
- **File:** `lectures/ifp_discrete.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-006` ×2; `qe-writing-002` ×2; `qe-writing-007` ×2. |
| Math         | 6/10  | `qe-math-001` ×2; `qe-math-002` ×1; `qe-math-005` ×1, +1 more. |
| Code         | 6.5/10 | `qe-code-002` ×2; `qe-code-001` ×3; `qe-code-004` ×10. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-005` ×1; `qe-fig-008` ×1. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 10. *Lines:* 312, 314, 322, 325, 332, 335, 499, 502, 509, 512. *Example:* bare time() reading.
- **[qe-math-002]** — Use \top for transpose notation. *Count:* 1. *Lines:* 130. *Example:* apostrophe transpose `a'`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 87, 353. *Example:* H2 Title Case: 'Set Up' (Up).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 176, 210, 447. *Example:* line 176 closes a hanging-indent signature with `    ):` at 4 spaces, leaving the arguments at the same indent as the body (E121/E125). Lines 210-211 pad before `=` to align the three reshape assignments (E221), 438 does the same (`a, y, ap  = ...`), and 447-449 pad both before `=` and inside the `in_axes` tuples (E221, E241).
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 182. *Example:* spelled-out `rho`.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 2. *Lines:* 132, 145. *Example:* unicode `β` inside a math environment.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 2. *Lines:* 110, 113. *Example:* the value function is $V$ where it is defined (113, 118) and $v$ everywhere it is used (130, 132, 145) and in the code, so one object carries two symbols eighteen lines apart. And both sets are set in sans-serif for no reason - $\mathsf Y$ for the finite income set (106, 110) and $\mathsf S$ for the state space (110, 113) - where plain $Y$ and $S$ would read the same and match the $Q$, $R$, $B$ used around them.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 148, 191. *Example:* line 148 reads 'the encapsulate the right hand side of the Bellman equation' - the sentence introducing $B$, the function the whole implementation is built around, does not parse. Line 191 reads 'Your are invited to explore an alternative style based around `jax.vmap` in the Exercises'.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 353, 383. *Example:* the lecture solves for $v^*$ and the greedy policy and then plots neither of them. Its single figure (359-372) is a 45-degree diagram of next-period assets against current assets; the value function defined at 113-122 and computed at 323 never appears, and the consumption policy $c = Ra + y - a'$ implied by `σ_star_jax` is never drawn either, although both are one line of plotting away. Line 383 then asserts that 'the dynamics suggest convergence to a stationary distribution' with nothing shown - no simulation, no cross-section, no invariant density.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 359. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 366. *Example:* plot() without lw=.
- **[qe-math-005]** — Use curly brackets for sequences. *Count:* 1. *Lines:* 106. *Example:* parenthesised sequence.


## Strengths

- The `{note}` at 49-59 states the trade-off that organises the whole series - faster algorithms exploit more structure and are therefore less robust to changes in the model - and gives the reason rather than just the rule, right where the reader is asked to accept a slow method.
- Every implementation is verified against the previous one before it is timed: the Python loop against `jax.lax.while_loop` at 339-349, and the exercise's staged-`vmap` version against both at 516-526, so each reported speedup rests on an equality check.
- The exercise's conclusion is honest rather than promotional - 'the execution times for the two JAX versions are relatively similar' (529) - and it says why the second method is still worth knowing (531-533).
- The hard part of the vectorised style is documented in place: the docstring of `B` gives the array it builds (200-202) and each reshape carries the index correspondence it establishes (210-217).
- 64-bit precision is turned on explicitly with the reason stated in one line (81-84), and the model is a `NamedTuple` whose six fields are each commented and named in unicode Greek to match the mathematics (159-184).

## Recommended actions

1. Plot the value function and the consumption policy: both are computed at 323 and neither is shown, which leaves a lecture titled 'Discretization and VFI' with no picture of what VFI produced.
2. Replace the ten bare `time()` readings at 312, 314, 322, 325, 332, 335, 499, 502, 509 and 512 with the `quantecon.Timer` context manager - `qe` is already imported at 72 - and drop `from time import time` at 77 (qe-code-004).
3. Rename the exercise solution's `B` at 428: it shadows the module-level `B` defined at 195 with an incompatible signature, so after that cell runs `T` (236) and `get_greedy` (246) can no longer be called - the later comparison only works because it reuses values computed earlier.
4. Settle the notation: one symbol for the value function ($V$ at 113-118 versus $v$ at 130-145), and plain $Y$ and $S$ instead of $\mathsf Y$ and $\mathsf S$.
5. Fix the two broken sentences at 148 and 191, and sentence-case the headings '## Set Up' (87) and '### Asset Dynamics' (353) (qe-writing-006).
6. Correct the stale comments at 211 and 216-217, which still describe the income variable as `z` although the code renamed it `y`, and remove the alignment padding at 210-211, 438 and 447-449.
7. Housekeeping: add mystnb name/caption metadata to the figure cell at 359 (qe-fig-005) and `lw=2` to the plots at 366 (qe-fig-008); brace the income sequence at 106 as $\{y_t\}_{t \geq 0}$ (qe-math-005); and replace the unicode `β` inside the display math at 132 and 145 with `\beta` (qe-math-001).
