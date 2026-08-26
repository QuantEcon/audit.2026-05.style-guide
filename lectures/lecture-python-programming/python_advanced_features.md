# python_advanced_features

- **Series:** lecture-python-programming
- **File:** `lectures/python_advanced_features.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.4 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-001` ×2; `qe-writing-005` ×4; `qe-writing-003` ×2, +2 more. |
| Math         | N/A   | no mathematical content. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 9/10  | `qe-fig-005` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
_None found._

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 361, 374, 417. *Example:* trailing whitespace at the ends of the `legend_kargs` dict lines (361, 362, 364) and a whitespace-only line inside the `for` body (374); and `kargs` throughout (`line_kargs`, `legend_kargs` at 360-361, then `**kargs` at 417, 440, 443, 458, 460) where every Python codebase - including the matplotlib signature the lecture quotes four lines earlier, `Axes.plot(*args, ..., **kwargs)` at 412 - writes `kwargs`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 473, 477. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 298, 458, 952. *Example:* 'When we operate on a list of parameters, we often need to extract the content of the list as individual arguments instead of a collection when passing them into functions' (298) is a 30-word opening for a section whose point is one clause long; the two-sentence summary at 458-460 restates the summary already given at 399-401 in the same shape ('The difference is that ... will unpack ... into *positional arguments*, while ...'), so the reader is summarised at twice; and 'The function `sum()` calls `next()` to get the items, adds successive terms' (952) has lost its conjunction.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 1107, 1173. *Example:* '### Advantages of iterators' (1107-1163) answers a question raised 800 lines earlier in '## Iterables and iterators' (34-287) but sits as the last subsection of '## Generators', with nothing at either end connecting the two - and its closing summary is about iterables (1160-1163), not generators. And exercise paf_ex1 (1173) tells the reader to fetch `test_table.csv` from GitHub 'which we assume that you've put in your current working directory', although the cell at 107-119 wrote that exact file to the working directory earlier in the same lecture.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 53, 784, 837, 906. *Example:* '## Type hints' bolds its own definition - 'Python supports optional **type hints**' (471) - and every other section italicises instead: 'Formally, an *iterator* is an object with a `__next__` method' (53), 'this issue is solved using *descriptors*' (784), 'The objects `miles` and `kms` are *properties*, a common kind of descriptor' (837) and 'The easiest way to build generators is using *generator expressions*' (906). The lecture's other italics are all doing emphasis correctly (25, 529, 1021, 1087), which makes the four definitional ones read as the same thing.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 2. *Lines:* 140, 1122. *Example:* 2 spaces.

### Low severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 1. *Lines:* 345. *Example:* code-cell figure without mystnb figure metadata.


## Strengths

- The Overview tells the reader to skip the lecture on a first pass and says exactly what it is for (25-31), which is the right framing for a reference chapter.
- Failure is demonstrated rather than described: six cells carry `tags: [raises-exception]` (193, 226, 237, 282, 1005, 1070), so the `StopIteration` and `TypeError` appear in the rendered page instead of being promised.
- The decorator section builds in four stages - duplicated `assert` lines (619-631), a manual wrapper (646-664), a line-by-line reading of `f = check_nonneg(f)` (668-679), then the `@` form (715-723) - and then answers *why* the syntax exists (727-734) rather than only what it does.
- The `Car` class is shown three times (751-759, 794-817, 864-888) so the problem, the getter/setter fix and the decorator form sit side by side.
- Re-displaying the generator body with a pointing comment - `# This line!` (1026) and `# execution continues from here` (1093) - marks the resume point without needing a diagram.

## Recommended actions

1. Fix `iterator.___next___()` at 151 - three underscores on each side, in the one line that spells out how the `for` loop calls `__next__`.
2. Correct the memory claim at 1122: `range(n)` is lazy in Python 3, so `draws` is the only huge list here; and support 'very slow' (1124) with a `qe.Timer` comparison rather than asserting it.
3. Rename `kargs` to `kwargs` throughout (360, 361, 417, 440, 443, 458, 460) to match the matplotlib signature quoted at 412.
4. Reconcile exercise paf_ex1 (1173) with the lecture - the reader already has `test_table.csv` from the cell at 107-119, so the download instruction and the 'we assume' hedge can go.
5. Bold the definitions at 53, 784, 837 and 906, keeping italics for the emphasis they are already doing well at 25, 529, 1021 and 1087.
6. Cut the repetition between the two summaries (399-401 and 458-460), trim the 30-word opening at 298, and restore the conjunction at 952.
7. Housekeeping: split the two-sentence paragraphs at 473 and 477 (qe-writing-001), remove the double spaces at 140 and 1122 (qe-writing-008), close the space before the period at 55, 102 and 608, clear the trailing and blank-line whitespace at 361-364 and 374, and add mystnb caption/name metadata to the plot cell at 345 (qe-fig-005).
