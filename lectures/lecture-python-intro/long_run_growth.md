# long_run_growth

- **Series:** lecture-python-intro
- **File:** `lectures/long_run_growth.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.8 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5/10  | `qe-writing-001` ×2; `qe-writing-003` ×3; `qe-writing-002` ×4, +2 more. |
| Math         | N/A   | no mathematical content. |
| Code         | 7.5/10 | `qe-code-001` ×8. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-004` ×5; `qe-fig-005` ×2; `qe-fig-001` ×3, +1 more. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 8. *Lines:* 177, 280, 285, 287, 364, 370, 425, 577. *Example:* a statement terminated with a semicolon to suppress notebook output (177), which PEP8 rules out; missing space after the comma in `'international dollars','year'` (280, 364, 425) and in `header=(0,1,2)` (577); missing space after the dict colons in `{'color':'grey', ...}` and `{'va':'center', 'ha':'center'}` (285, 287); and the `events` list literal at 369-394 with its elements flush at column zero, where the identical literal at 431-456 indents them by four.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 5. *Lines:* 162, 190, 264, 351, 412. *Example:* Title Case caption (Capita).
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 7. *Lines:* 38, 40, 47, 50, 506, 539, 566. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 275, 359, 420. *Example:* figsize=.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 34, 525. *Example:* {figure} without :name:.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 40, 504. *Example:* `` {cite} `` in narrative flow: 'of `` {cite} ``'.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 38, 181. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 29, 42, 539, 566. *Example:* sentences of 36-48 words at 29 (41w), 539 (48w) and 566 (36w), plus a sentence at 42-43 that keeps the subordinate structure of the sentence before it and so has no main clause: "By the end of the nineteenth century, US GDP had caught up with GDP of the British Empire, and how during the first half of the 20th century, US GDP surpassed that of the British Empire".
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 38, 258, 348. *Example:* line 38 tells the reader the opening PNG "is just a copy of our figure `` {numref}`gdp1` ``", but `gdp1` (486-500) plots CHN, SUN, JPN, GBR, USA while the PNG is written by the un-named cell at 525-537, which plots DEU, USA, SUN, BEM, FRA, JPN - the reader is pointed at the wrong figure; line 258 says "As you can see from this chart" immediately after a cell that defines the `draw_interp_plots` function and produces no chart at all, the nearest figure being 50 lines earlier; and the bullet at 348, "how the Self-Strengthening Movement seemed mostly to help China to grow", contradicts line 342 and the figure it describes, both of which show GDP per capita declining across 1861-1895.

### Low severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 34. *Example:* static image .png.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 1. *Lines:* 181. *Example:* the lecture contains no bold and no italic anywhere, so the one term it stops to define - international dollars, defined in the `{note}` at 181 along with its alias Geary-Khamis dollars - is introduced in plain text.


## Strengths

- `draw_interp_plots` (219-256) is the right abstraction for this lecture: it draws observed data solid and interpolated data dashed, so every one of the six country figures distinguishes real observations from filled gaps in the same visual language.
- The `color_mapping` built at 141-151 keeps each country the same colour across all six figures, and the British Empire aggregate is deliberately given Great Britain's colour at 518.
- Historical events are annotated declaratively through an `Event` namedtuple and a single `draw_events` helper (273, 314-323), so the Navigation Act, Industrial Revolution and Reform-and-Opening-up bands are consistent across the China and UK/US panels.
- Figures carry `name`s and the prose genuinely uses them: `{numref}`gdp1`` at 38 and 566, `{numref}`gdp2`` at 50 - the lecture is built around a forward reference the reader is invited to jump to.
- Cross-series references use the `{doc}` form with an intersphinx prefix (`pyprog:pandas`, `pyprog:matplotlib` at 18) rather than raw URLs.

## Recommended actions

1. Fix the figure reference at 38: the opening PNG reproduces the un-named cell at 525-537, not `gdp1`; give that cell `mystnb: figure: caption/name` metadata and point line 38 at it.
2. Replace the static `tooze_ch1_graph.png` at 34 with the generated figure, and remove the `plt.savefig` into `_static/` at 534 - a code cell that writes a PNG back into the source tree at build time is why the copy at 34 can drift from the code.
3. Move the "As you can see from this chart" paragraph at 258-262 above the `draw_interp_plots` definition, or after the figure it refers to.
4. Lower-case the five Title Case captions (162, 190, 264, 351, 412) - "GDP per Capita" -> "GDP per capita" - and give the two figures at 34 and 525 names so they can be cross-referenced.
5. Correct the Self-Strengthening Movement bullet at 348 so it agrees with the data, and fix "GDP per capital" at 342.
6. Convert the two narrative-position citations to `{cite:t}` (40, 504) and break the four long or broken sentences listed above.
7. Fix the PEP8 items above, set `lw=2` on the four remaining plots (199, 204, 236, 243), and drop `figsize=(10, 6)` where `dpi=300` already controls the output size (275, 359, 420).
