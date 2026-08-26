# numba

- **Series:** lecture-python-programming
- **File:** `lectures/numba.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.6 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×6; `qe-writing-001` ×2; `qe-writing-005` ×4, +3 more. |
| Math         | 7.5/10 | `qe-math-010` (proposed) ×2. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7.5/10 | `qe-fig-005` ×4; `qe-fig-008` ×2; `qe-fig-002` ×1. |
| References   | N/A   | no citations in this lecture. |
| Links        | 9/10  | `qe-link-002` ×1. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-math-010 (proposed)]** — Blackboard \mathbb{P}, \mathbb{E}, \mathbb{V} with braces. *Count:* 2. *Lines:* 975, 1014. *Example:* missing braces: `\mathbb E`.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 6. *Lines:* 87, 100, 183, 217, 267, 300. *Example:* H3 Title Case: 'An Example' (Example).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 109, 116, 176. *Example:* the body of the `for` loop in `qm` is indented six spaces instead of four (109, pycodestyle E111); `ax.set_ylabel('$x_{t}$', fontsize = 12)` at 116 puts spaces around a keyword-argument `=` (E251) one line after 115 writes `fontsize=12` correctly; and 176 has two spaces around the division in `timer1.elapsed /  timer3.elapsed` (E222).
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 4. *Lines:* 104, 340, 575, 885. *Example:* {image} without :name:.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 349, 899. *Example:* plot() without lw=.
- **[qe-link-002]** — Use doc links for cross-series references. *Count:* 1. *Lines:* 566. *Example:* raw link to intro.quantecon.org.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 69, 211. *Example:* 3 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 531, 856. *Example:* 39- and 32-word single sentences at the two points where the exercise sequence most needs to be clear: 529-531 on which cells are actually being timed, and 856 on why the data race destroys reproducibility.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 441, 552. *Example:* 441 says "We generate them here and store them in `u_draws` and `v_draws`" before any draws have been mentioned - "them" has no antecedent, and the sentence forward-references two exercise labels that do not yet exist; and the three exercises on pre-drawing versus drawing in the loop reach conclusions that read as contradictory in sequence: 552-556 warns that drawing inside the loop "interacts badly with parallelization", 912 offers pre-drawing as "the other safe option", and 951 concludes "Drawing inside the loop is much faster" - the distinction that reconciles them (legacy `np.random` versus a `Generator`) is stated at 869 but not at 951 where the recommendation lands.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 196, 199, 212, 852. *Example:* the bullet list at 196-200 carries five italic spans in five bullets - *ahead of time*, *call*, *other variables*, the whole clause *can be inferred once the input types are known*, and *wait until the function is called* - which is the overuse of emphasis formatting the rule names; *decorator* (212) is a term being defined and belongs in bold, as **just in time (JIT) compiler** (57) and **data race** (845) correctly are; and 852 and 865 italicise entire sentences ("*Symptom 1: the result is no longer reproducible.*") as pseudo-headings.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 3. *Lines:* 70, 198, 219. *Example:* 2 spaces.

### Low severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 1. *Lines:* 575. *Example:* static image .png.


## Strengths

- The Numba case is made by measurement rather than assertion: the same `qm` is timed unjitted (125), jitted (155) and jitted-with-cache (168), and the ratio is computed in the notebook at 176.
- "Sharp Bits" (217-296) is unusually honest for an introductory lecture - it shows the type-inference failure as a caught exception (247-250) and the frozen-global surprise (274-291) instead of only the happy path.
- The `numba_ex_race` exercise (791-915) is the best thing here: it takes a program that runs, returns roughly the right answer, and is silently wrong, then diagnoses it with two symptoms - non-reproducibility under a fixed seed (858-861) and an inflated spread shown as a confidence band against the correct version (885-908).
- Parallelization is applied to the dimension that admits it and the lecture says so: "we parallelize across households rather than over time -- updates of an individual household across time periods are inherently sequential" (432-433).
- Large arrays are flagged before they are allocated (`{note}` at 732-735) and released when finished with (`del u_big, v_big`, 777) - the kind of housekeeping most lectures skip.

## Recommended actions

1. Add braces to `\mathbb E` at 975 and 1014 (qe-math-010 (proposed)) - the only math violations in the lecture.
2. Sentence-case the six headings (87, 100, 183, 217, 267, 300).
3. Reconcile the three pre-draw-versus-in-loop conclusions (552-556, 912, 951) into one recommendation that restates the `Generator`-versus-legacy distinction where the recommendation is actually made.
4. Add mystnb caption/name to the four figures (104, 340, 575, 885), add `lw=2` at 349 and 899, and regenerate the static PNG at 575 from code.
5. Replace the raw intro.quantecon.org link at 566 with a `{doc}` cross-reference (qe-link-002).
6. Fix the code cells: the six-space loop body at 109, `fontsize = 12` at 116, and the double space at 176; give 441 a real antecedent.
7. Cut the italic emphasis at 196-200 to at most one span per bullet, bold *decorator* at 212, promote the italic pseudo-headings at 852 and 865 to real subheadings, fix "libaries" at 263, and delete the double spaces at 70, 198 and 219.
