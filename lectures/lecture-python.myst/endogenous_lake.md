# endogenous_lake

- **Series:** lecture-python.myst
- **File:** `lectures/endogenous_lake.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-003` ×2; `qe-writing-002` ×2; `qe-writing-006` ×1, +1 more. |
| Math         | 7.5/10 | `qe-math-010` (proposed) ×2. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-006` ×2; `qe-fig-005` ×3; `qe-fig-003` ×1, +2 more. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 319, 385. *Example:* missing braces: `\mathbb P`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 71. *Example:* H2 Title Case: 'Set Up' (Up).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 104, 427, 649. *Example:* line 104 closes a hanging-indent signature with `    ):` at 4 spaces - matching neither column 0 nor the 8-space argument indent, and leaving the arguments at the same indent as the body (E121/E125); the same pattern recurs at 165, 254, 423, 442 and 476. Lines 427-429 over-indent the continuation of `return Economy(...)` past the visual indent set by the opening parenthesis (E127). Lines 649-650 wrap a division with a backslash continuation where PEP8 asks for parentheses, and then over-indent the second line.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 572, 654. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 579. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 3. *Lines:* 124, 571, 610. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 2. *Lines:* 656, 657. *Example:* axis label `Separation rate $\alpha$`.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 1. *Lines:* 668. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 47, 75. *Example:* the setup is stated three times. Line 45 says the lecture continues {doc}`lake_model` and 47 then says to read that lecture first; 49-52 says the previous lecture had exogenous transition rates and this one makes the job finding rate endogenous; 73-77 says it again ('The basic structure ... will be as discussed in the lake model lecture. The only difference is that the hiring rate is endogenous'), re-citing McCall1970 already cited at 54. Line 75 is also the file's longest sentence at 34 words.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 385, 388. *Example:* the welfare criterion at 385 is built from $V$ and $U$, and 388 says 'the notation $V$ and $U$ is as defined above' - but they are never defined above in prose. They first appear as arguments of `T` inside the code cell at 181-191, and the Bellman equations that define them are given only in Python (188-189), never in mathematics, in a lecture whose central object is the reservation wage those equations determine.

### Low severity
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 1. *Lines:* 128. *Example:* plot() without lw=.


## Strengths

- The event in the job-finding-rate definition is written with braces - $\gamma \mathbb P \{ w_t \geq \bar w\}$ at 319 - so the proposed qe-math-014 (proposed) convention holds, and the wage offer distribution is lowercase $p$ at 320 and 326 against uppercase $V$, $U$, $W$ for the value functions, matching proposed qe-math-015 (proposed).
- Both model containers are `NamedTuple`s with the parameter meaning documented on the field itself (152-158, 240-246, 401-411), so the twelve parameters are named once and passed by keyword everywhere after.
- Greek unicode identifiers are used consistently for the model parameters in code - `α`, `β`, `γ`, `σ`, `λ`, `τ` (152-156, 414-419, 437-438) - matching the mathematics one-for-one (0 qe-code-002 violations).
- The equation that couples the two models carries a label and is cited where it is used: `endogenous_lake_lambda` at 316 is referenced at 371 by {eq}, not as 'the equation above'.
- The exercise is a real extension rather than a repetition - it re-solves the whole fixed point across separation rates - and its solution explains why it takes a welfare-weighted centroid instead of `argmax` (638-642), which is the kind of numerical caveat usually left out.

## Recommended actions

1. Write the McCall Bellman equations and the definitions of $V$ and $U$ in mathematics before the welfare criterion at 385 uses them, so that 'as defined above' at 388 has an antecedent.
2. Brace the two blackboard operators - `\mathbb P` at 319 and `{\mathbb E}` at 385 become `\mathbb{P}` and `\mathbb{E}` (qe-math-010 (proposed), proposed).
3. Figure hygiene, the largest mechanical block here: add mystnb name/caption metadata to the three figure cells at 124, 571 and 610 (qe-fig-005), move the embedded titles at 579 and 658 into captions (qe-fig-003), lowercase the axis labels at 656-657 (qe-fig-006), drop `figsize=` at 572 and 654 (qe-fig-001), and add `lw=2` to the plot at 128 (qe-fig-008).
4. Compress the three-times-told setup at 45-52 and 73-77 into one statement of what changes relative to {doc}`lake_model`.
5. Sentence-case the heading at 71: '## Set Up' becomes '## Set up' (qe-writing-006).
6. Split the two-sentence paragraph at 668-670 (qe-writing-001), fix the typo 'paramters' at 339, and either mark the welfare maximum on the welfare panel at 572-582 or drop the hard-coded 'approximately 62' at 587, which will go stale the first time a parameter moves.
7. Clean the code-cell whitespace: trailing spaces at 106, 163, 414, 415, 417, 418, 437, 438, 439 and 440, and the unused unpackings at 519 (`e` and `w` are computed and discarded) and 528 (`i`).
