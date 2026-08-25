# ifp_discrete

- **Series:** lecture-dp
- **File:** `lectures/ifp_discrete.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-006` ×2; `qe-writing-003` ×2. |
| Math         | 7/10  | `qe-math-001` ×2; `qe-math-005` ×1; `qe-math-009` ×3. |
| Code         | 7/10  | `qe-code-002` ×2; `qe-code-004` ×10; `qe-code-001` ×1. |
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
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 2. *Lines:* 87, 353. *Example:* H2 Title Case: 'Set Up' (Up).

### Medium severity
- **[qe-code-002]** — Use Unicode symbols for Greek letters in code. *Count:* 2. *Lines:* 182. *Example:* spelled-out `rho`.
- **[qe-math-001]** — Prefer UTF-8 unicode for simple parameter mentions, be consistent. *Count:* 2. *Lines:* 132, 145. *Example:* unicode `β` inside a math environment.
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 3. *Lines:* 106, 110, 113. *Example:* `\mathsf` used decoratively where plain letters would do: $\mathsf Y$ for the income support at 106, $\mathsf S := \mathbb{R}_+ \times \mathsf Y$ at 110, and $V \colon \mathsf S \to \mathbb{R}$ at 113. Both symbols appear only in these three lines and neither reaches the code, so nothing is gained by the sans-serif face - $Y$ and $S$ carry the same meaning and match how the lecture writes every other set and space.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 130, 412. *Example:* line 113 defines the value function as $V$ and equation `eqvfs` at 118 states it in $V$; then the Bellman equation at 130 switches to lowercase $v$ and everything downstream - the display at 145, the operator $T$ at 232, `B`, `T`, `get_greedy` and every code cell - stays lowercase. The switch is never mentioned, $V$ is never used again, and `eqvfs` is never cited, so the reader has to guess that $v$ and $V$ are the same object. Separately, exercise step 2 at line 412 says to 'use staged vmap as shown in earlier examples' - there are no earlier vmap examples in this lecture; the staged-vmap idiom first appears in this file at 447-449, inside the solution to that very exercise.

### Low severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 1. *Lines:* 438. *Example:* line 438 writes `a, y, ap  = a_grid[i], y_grid[j], a_grid[ip]` with two spaces before the `=` (pycodestyle E221). The aligned assignment blocks at 210-212 and 447-449 are a separate matter and should stay: the reshape comments and the `in_axes` tuples are column-aligned so the index mapping reads as a table, which is the 'closer to mathematical notation' latitude the rule allows.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 359. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 366. *Example:* plot() without lw=.
- **[qe-math-005]** — Use curly brackets for sequences. *Count:* 1. *Lines:* 106. *Example:* parenthesised sequence.


## Strengths

- The `{note}` at 49-59 answers the question the reader is actually forming - why learn the slow method first - and answers it with a general principle ('less robust precisely because they exploit more structure'), so the ordering of the whole series is justified rather than just asserted.
- Every reshape inside `B` (210-218) carries a trailing comment mapping the incoming index shape to the outgoing one (`a[i] -> a[i, j, ip]`, `Q[j, jp] -> Q[i, j, ip, jp]`), which makes the 3D and 4D broadcasting auditable line by line instead of something the reader has to re-derive.
- The Python-loop and `jax.lax.while_loop` implementations are both kept (259-273 and 279-298), and their outputs are checked against each other on both values and policies (342-343) before the speed ratio is printed at 349 - the correctness check precedes the speed claim, and the same discipline is repeated for the vmap version at 519-526.
- The anticipated objection is raised and answered where it arises: 'Some readers might be concerned that we are creating high dimensional arrays' at 224-230, immediately after the 4D reshape that provokes it.
- The exercise at 388-417 is a 6-step specification precise enough to attempt without the solution, and the solution closes at 529-533 by admitting the vmap version is no faster and saying why it is still worth knowing - the honest answer rather than a manufactured win.
- Only the three real definitions are bold - **income fluctuation problem** and **household problem** at 24, **value function** at 113 - with no emphasis-bold anywhere in the file.

## Recommended actions

1. Replace the 10 bare `time()` readings with the `qe.Timer` context manager (312, 314, 322, 325, 332, 335, 499, 502, 509, 512) - the largest single item, and it removes six near-identical `start = time()` / `... = time() - start` pairs (qe-code-004 x10).
2. Settle on one symbol for the value function: either state at 130 that $v$ is the $V$ of {eq}`eqvfs`, or write the Bellman equation in $V$. While there, cite `eqvfs` somewhere (it is currently a labelled equation with no reference) and either use or delete the `(prgm:create-consumption-model)=` anchor at 156, which nothing links to.
3. Replace `\mathsf Y` and `\mathsf S` with $Y$ and $S$ at 106, 110 and 113, and write the income sequence with curly brackets - `$\{y_t\}_{t \geq 0}$` at 106, matching `$\{c_t\}_{t \geq 0}$` at 89 (qe-math-009 x3, qe-math-005 x1).
4. Replace the two Unicode `β` characters inside display math at 132 and 145 with `\beta`, as the surrounding math already does at 92 and 120 (qe-math-001 x2).
5. Fix the prose slips that survive into the published page: 'the encapsulate the right hand side' at 148 (should be 'to encapsulate', and the fragment needs joining to the display above it), 'Your are invited' at 191, 'i.e,' at 531, and the stale comment at 211 which names the variable `z` where the code calls it `y`.
6. Sentence-case the two headings at 87 and 353 - 'Set up', 'Asset dynamics' - and add mystnb `name`/`caption` metadata plus `lw=2` to the 45-degree diagram at 359-366 (qe-writing-006 x2, qe-fig-005 x1, qe-fig-008 x1).
7. Give the solution's `B` at 428 a distinct name (say `B_indexed`). It currently shadows the module-level `B` defined at 195 with an incompatible 5-argument signature, so any reader who re-runs the earlier `T` cell after opening the solution gets a TypeError - a real trap in a notebook that executes top to bottom.
