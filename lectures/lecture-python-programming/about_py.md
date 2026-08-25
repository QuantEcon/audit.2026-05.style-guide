# about_py

- **Series:** lecture-python-programming
- **File:** `lectures/about_py.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, figures, links  *(JAX out of scope)*
- **Overall score:** 7.1 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×10; `qe-writing-005` ×2; `qe-writing-003` ×2, +2 more. |
| Math         | N/A   | no mathematical content. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-005` ×5. |
| References   | N/A   | no citations in this lecture. |
| Links        | 8/10  | `qe-link-002` ×2. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 5. *Lines:* 140, 411, 417, 423, 464. *Example:* {figure} without :name:.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 10. *Lines:* 50, 69, 101, 127, 159, 252, 269, 347, 438, 493. *Example:* H3 Title Case: "Can't I Just Use LLMs?" (Just, Use).

### Medium severity
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 2. *Lines:* 84, 440. *Example:* raw link to jax.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 27. *Example:* 3 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 274, 364, 519. *Example:* the same promise is made five times in five sections - "We will discuss the details later in the lecture series, where we cover NumPy in depth" (344), "as we'll explain later in this series" (356), "This lecture series will provide you with extensive background in NumPy" (364), "Later we'll discuss SciPy in more detail" (393), "In this lecture series we will learn how to use many of these libraries" (519); and 274 opens a section with "We have already discussed the importance of Python for AI, machine learning and data science", which restates 254-257, which restates 133, which restates 78.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 50, 142. *Example:* the two rhetorical asides "Can't I Just Use LLMs?" (50) and "Isn't MATLAB Better?" (69) sit under `## Overview` and before `## Introducing Python` (88), so MATLAB, JAX, deep learning and reinforcement learning are all invoked before Python itself has been introduced; and 142 ("PyTorch is just one of several Python libraries for deep learning and AI.") is stranded after the `{figure}` block at 140-141, where it reads as a caption but is a body paragraph.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 2. *Lines:* 47, 170. *Example:* the only two bold spans in the lecture are both emphasis, which the rule reserves for italic: "You do **not** need to understand everything" (47) and "You do **not** need to read and understand this code" (170); no term the lecture introduces - high-level language (148), open source (92) - is bolded at its point of definition.

### Low severity
_None found._


## Strengths

- The Java-versus-Python comparison (173-248) makes the "simple and elegant design" claim at 164 concrete instead of asserting it: the same task, 47 lines of Java against 12 lines of Python, with the reader told twice that they need not read the Java.
- The NumPy walk-through (296-336) builds from a three-element Python list to a 100-point grid to `b @ c`, so the motivation for the library arrives before the library does.
- Every library named is hyperlinked to its own documentation, and the SciPy list at 384-389 links each subpackage to its own reference page rather than to the project root.
- Greek unicode identifiers appear in narrative code exactly where the convention wants them - `ϕ = norm()` (377) and the comment "Create even grid from -π to π" (321).
- The lecture is honest about its own level: "You do not need to understand everything you see in this lecture" (47) sets the right expectation for a showcase chapter.

## Recommended actions

1. Sentence-case the 10 H2/H3 headings (50, 69, 101, 127, 159, 252, 269, 347, 438, 493) - the single largest fix, and the only thing holding Writing at 4.5.
2. Add `:name:` and a caption to the five figures (140, 411, 417, 423, 464), and fold the orphan sentence at 142 into the caption of the figure above it.
3. Regenerate `qs.png` (411), `bn_density1.png` (417) and `career_vf.png` (423) from code - they are a LaTeX-annotated 2D plot, a contour plot and a 3D surface, not screenshots (see scanner doubt).
4. Replace the raw links to jax.quantecon.org (84) and networks.quantecon.org (440) with `{doc}` cross-references (qe-link-002).
5. Cut the repeated "we will cover this later" promises at 274, 364 and 519 to one, and move the LLM and MATLAB asides after "Introducing Python".
6. Change `**not**` to `*not*` at 47 and 170, and bold the terms the lecture actually defines.
7. Fix the missing full stops at 133 and 274 and the "we are interesting in studying" at 443.
