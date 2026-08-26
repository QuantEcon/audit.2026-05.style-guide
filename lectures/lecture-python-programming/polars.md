# polars

- **Series:** lecture-python-programming
- **File:** `lectures/polars.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-004` ×2; `qe-writing-001` ×4; `qe-writing-005` ×3, +2 more. |
| Math         | N/A   | no mathematical content. |
| Code         | 9/10  | `qe-code-004` ×10. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×4; `qe-fig-003` ×1; `qe-fig-001` ×2, +1 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-004]** — Use quantecon Timer context manager. *Count:* 10. *Lines:* 430, 436, 439, 445, 482, 486, 493, 501, 508, 517. *Example:* time.perf_counter(.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 706, 785. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 593. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 322, 584, 701, 784. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 4. *Lines:* 87, 317, 532, 662. *Example:* 3 sentences in one paragraph.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 53, 344, 417. *Example:* the `{tip}` at 49-55 leads with "**Speed**: Polars is 10--100x faster for many common operations", and the lecture's own measurements never show that - 447 reports parity on eight rows, 487-518 a more modest gain on five million, and 523-527 quietly restates the claim as "can be significantly faster" without ever reconciling it with the headline; 344-346 has to reload the same CSV a third time ("# Reload the dataset") because `df` was overwritten by the visualization pipeline at 299-311, and a fourth time at 421; and 417-418 imports `pandas` and `time` in a mid-lecture cell although 57 states that the lecture assumes the three imports at 59-63.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 2. *Lines:* 76, 87. *Example:* mid-sentence 'Series'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 50, 523, 525. *Example:* this is the series' best lecture for bold-as-definition - **column expressions** (219), **lazy evaluation** (337), **eager**/**lazy** API (349, 360), the three optimizations (382-384) - which makes the three exceptions stand out: an entire question italicised as a heading inside the `{tip}` ("*Why consider Polars over pandas?*", 50), and bold on emphasis at 523 and 525 ("For **small data**", "For **medium to large data**"), where both phrases are section titles from 413 and 453 rather than new terms.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 591. *Example:* plot() without lw=.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 380. *Example:* "Query optimization" (378-407) carries the lecture's conceptual core - predicate pushdown, projection pushdown and common subexpression elimination (382-384) - entirely through two `explain()` text dumps (368, 400). Pushdown is a picture: the same three-node plan before and after the filter moves to the scan. The lecture's four figures are all matplotlib result plots, so nothing illustrates the mechanism it is selling.


## Strengths

- Every pandas habit that Polars breaks is named exactly where the reader would trip over it: no row index (86-91), expression-based updates instead of index assignment (131-141), `map_elements` flagged as an escape hatch to avoid (251-255), and joins not preserving row order (661-668).
- The performance claim is tested rather than repeated - the same filter-select-sort timed on eight rows (428-448) and on five million (481-519) - and the honest conclusion is stated first: "On a handful of rows the speed difference is immaterial" (450-451).
- Lazy evaluation is shown by printing the query plan (368, 400), so "predicate pushdown" is something the reader watches happen instead of something they are told about.
- `read_data_polars` (633-656) handles the awkward part properly - per-ticker frames joined on Date with `coalesce=True` and an explicit final `sort` - and the `{note}` at 661-668 explains why that sort is not optional.
- Bold marks definitions consistently (219, 337, 349, 360, 382-384), which is the convention most of this series inverts.

## Recommended actions

1. Replace the 10 `time.perf_counter()` calls with the `quantecon` Timer context manager (430, 436, 439, 445, 482, 486, 493, 501, 508, 517) - qe-code-004, and the only High-severity finding in the lecture.
2. Reconcile the "10--100x faster" headline at 53 with the lecture's own timings at 447 and 487-518, or move it behind the measurement.
3. Add `:name:` and captions to the four code-cell figures (322, 584, 701, 784), drop `figsize=` at 706 and 785, and move the `set_title` at 593 into a caption.
4. Add a small before/after query-plan diagram to "Query optimization" (378-401) - the pushdown mechanism is the lecture's selling point and is carried entirely by `explain()` text.
5. Move `import pandas as pd` and `import time` (417-418) into the imports cell at 59-63, which line 57 says holds everything the lecture assumes.
6. Stop overwriting `df` in the visualization pipeline (299-311) so the dataset need not be reloaded at 345 and 421; lowercase "Series" mid-sentence at 76 and 87 (qe-writing-004).
7. Split the four multi-sentence paragraphs at 87, 317, 532 and 662 (see scanner doubt - all four are admonition bodies); turn the italic question at 50 into the tip's own opening text and drop the bold emphasis at 523 and 525.
