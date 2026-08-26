# need_for_speed

- **Series:** lecture-python-programming
- **File:** `lectures/need_for_speed.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×10; `qe-writing-001` ×2; `qe-writing-005` ×3, +3 more. |
| Math         | N/A   | no mathematical content. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 8.5/10 | `qe-fig-005` ×3. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 10. *Lines:* 70, 103, 130, 136, 217, 223, 236, 441, 450, 481. *Example:* H2 Title Case: 'Major Scientific Libraries' (Scientific, Libraries).

### Medium severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 313, 458, 492. *Example:* {figure} without :name:.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 424, 466. *Example:* 3 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 300, 421. *Example:* 38- and 33-word single sentences carrying two clauses each: 300-302 on subcontracting matrix inversion to pre-compiled machine code, and 421 on splitting an array operation across a laptop's cores.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 272, 313. *Example:* 272 announces "three related techniques for accelerating Python code" (the same triple listed at 96-98), but only vectorization and JIT compilers arrive under that heading - Parallelization is promoted to its own H2 at 387, so the promised grouping is split across two top-level sections; and the `matlab.png` figure at 313 is dropped between two sentences that read continuously (310 and 316) with no caption saying what it shows.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 82, 90, 288. *Example:* "**Python is small**" (82) and "**Python is slow**" (90) use bold as a substitute for headings - neither is a definition nor an emphasis - and at 288 the term the whole section turns on is introduced in quotation marks: "Many economists usually refer to array programming as \"vectorization.\""; the lecture does get bold right later for **GPUs** (453), **core** (466) and **TPUs** (477).

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 225. *Example:* "Data Access" (217-247) is the lecture's second explanation of why pure Python is slow and it is entirely verbal: a contiguous block of 8-byte integers (225-228) against CPython's "pointers to data rather than actual data" (243) is the canonical box-and-arrow memory diagram, and the section has no figure. The lecture's three figures are a MATLAB screenshot (313) and two hardware photographs (458, 492), none of which carries an idea.


## Strengths

- The "why pure Python is slow" argument is built from two named mechanisms - type checking (136-214) and data access (217-247) - each set against the C program at 191-205 rather than against an abstraction.
- It refuses the obvious wrong conclusion out loud: "Does the discussion above mean that we should just switch to C or Fortran for everything? The answer is: Definitely not!" (252-254), with the reason given in the two sentences that follow.
- The vectorization claim is measured in the notebook, not asserted - the same sum of squares as a Python loop (331-337) and as three NumPy batch operations (342-347), with those three operations then named (353-355).
- GPUs and cores are defined at the point of first use inside `{note}` blocks (423-429, 465-472), so a reader who does not know what a core is is not left behind.
- The parallelization taxonomy is complete and decided: multithreading, multiprocessing, and a "Which Should We Use?" section that actually answers the question (441-447).

## Recommended actions

1. Sentence-case the 10 headings (70, 103, 130, 136, 217, 223, 236, 441, 450, 481) - the whole of the Writing score of 4.
2. Move Parallelization (387) under "Accelerating Python" (270) as the third of the three techniques promised at 96-98 and 272, or change the promise.
3. Add `:name:` and captions to the three figures (313, 458, 492); `matlab.png` in particular needs a caption saying what the reader is looking at.
4. Add a memory-layout diagram to "Data Access" (217-247) - contiguous integers against an array of pointers is the picture the section spends 30 lines describing.
5. Turn the bold pseudo-headings at 82 and 90 into real H4s, and bold "vectorization" at 288 where it is defined instead of quoting it.
6. Trim the two long sentences at 300-302 and 421, and split the two multi-sentence `{note}` paragraphs at 424 and 466.
7. Make the numbering at 96-98 consistent (it runs 1., 1., 2.) and the slash spacing at 98 uniform ("threads/ CPUs / GPUs /TPUs").
