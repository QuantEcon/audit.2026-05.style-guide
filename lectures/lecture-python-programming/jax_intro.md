# jax_intro

- **Series:** lecture-python-programming
- **File:** `lectures/jax_intro.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.5 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×9; `qe-writing-001` ×3; `qe-writing-005` ×3, +3 more. |
| Math         | N/A   | no mathematical content. |
| Code         | 7.5/10 | `qe-code-001` ×8. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×2; `qe-fig-003` ×1; `qe-fig-008` ×2, +1 more. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 8. *Lines:* 172, 435, 441, 673, 681, 714, 722, 738. *Example:* four statements end in a redundant semicolon, `jax.block_until_ready(y);` (673, 681, 714, 722 - pycodestyle E703); trailing whitespace inside code cells at 172 (a comment), 435 and 441 (W291); and `pass # put function body here` at 738 has one space before the inline comment where PEP8 wants two (E262).
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 9. *Lines:* 51, 193, 294, 321, 354, 396, 429, 606, 696. *Example:* H2 Title Case: 'JAX as a NumPy Replacement' (Replacement).

### Medium severity
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 560. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 495, 891. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 894, 895. *Example:* plot() without lw=.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 3. *Lines:* 160, 900, 971. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 4. *Lines:* 61, 356, 612, 689. *Example:* 61 reads "this interface conform to the NumPy API"; 356 reads "an example of a *impure* function"; 612 is broken outright - "We saw the power of JAX's JIT compiler combined with parallel hardware when we `` {ref}`above <jax_speed>` ``, when we applied `cos` to a large array" - and it is the lecture's own back-reference to its headline result; and the three JIT passages at 640-649, 687-694 and 725-730 are written as verbless presentation bullets ("Minimal parallelization", "Lots of memory read/write", "Also, many separate kernels launched on the GPU") rather than prose.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 117, 317. *Example:* 117 and 141 introduce H5 subsections ("With NumPy", "With JAX") nested four deep under `## JAX as a NumPy Replacement` > `### Differences` > `#### Speed!`, each wrapping one or two code cells, which splits a single timing comparison across four headings; and 317's aside - "Although it can in fact be efficient inside JIT-compiled functions -- but let's put this aside for now" - is never returned to, even though the JIT section arrives 300 lines later.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 287, 337, 743. *Example:* three definitions are set in italic where the lecture's own good practice is bold - "a *functional programming style*" (287) against "**immutable**" (253) and "**Eager** execution model" (640); the two defining properties of a pure function, *Deterministic* and *No side effects* (337-338); and "JAX *traces* it" (743), the term the whole JIT section turns on.

### Low severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 1. *Lines:* 498. *Example:* figsize=.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 901. *Example:* 2 spaces.


## Strengths

- Purity is defined once (331-350) and then used as the lecture's organizing test: the impure `add_tax` (358-374), NumPy's hidden generator state (431-450) and the frozen global under `jit` (763-799) are each diagnosed against the same two criteria.
- The key-splitting diagram (495-563) is drawn in matplotlib rather than described - root key, split, subkey consumed by a draw, repeated three levels down - which is precisely the part of JAX's RNG design that prose does not convey.
- Immutability is a two-cell diff: the NumPy mutation that works (264-267) followed immediately by the same assignment caught as an exception in JAX (277-283).
- Every timing cell holds the interpreter with `block_until_ready` and the `{note}` at 159-164 says why - without it the numbers would be meaningless under asynchronous dispatch.
- The JIT section separates measurement from explanation: first-call versus second-call timings (668-682, 709-723), then a plain-language account of tracing and XLA (743-753).

## Recommended actions

1. Sentence-case the nine headings (51, 193, 294, 321, 354, 396, 429, 606, 696).
2. Repair the broken sentence at 611-612 - as written the lecture cannot point back to its own `jax_speed` result.
3. Add mystnb caption/name to the two code-cell figures (495, 891), drop `figsize=` at 498, and move the `set_title` at 560 into the caption (qe-fig-005, qe-fig-001, qe-fig-003).
4. Rewrite the slide-style fragments at 640-649, 687-694 and 725-730 as sentences - this is the lecture's core explanation of eager execution versus kernel fusion.
5. Clean the code cells: drop the four trailing semicolons (673, 681, 714, 722), strip trailing whitespace at 172, 435, 441, and use two spaces before the inline comment at 738.
6. Bold the definitions at 287, 337-338 and 743, matching `**immutable**` at 253; fix "conform" (61) and "a impure" (356).
7. Split the three multi-sentence paragraphs at 160, 900 and 971 and delete the double space at 901 (qe-writing-001, qe-writing-008).
