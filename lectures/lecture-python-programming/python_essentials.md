# python_essentials

- **Series:** lecture-python-programming
- **File:** `lectures/python_essentials.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, math, code, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.3 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×14; `qe-writing-005` ×5; `qe-writing-001` ×2, +4 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-001` ×4. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | N/A   | no figures or plotting code. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 5. *Lines:* 256, 258, 543, 610, 714. *Example:* the first half of the lecture bolds its definitions correctly - **Boolean values** (63), **Boolean arithmetic** (89), **Complex numbers** (117), **tuples** (136), **immutable** (148), **mutable** (150) - and then the convention collapses. 'The names ... are called the *keys*' (256) is italic and the matching sentence one line later, 'are called the `values`' (258), is a code span, so the paired terms get two different treatments and neither is bold; *list comprehension* (543) and *docstrings* (714) are likewise defined in italics; and 610 reverses the rule outright by bolding **any** for emphasis.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 14. *Lines:* 31, 58, 61, 111, 188, 234, 284, 435, 485, 538, …. *Example:* H2 Title Case: 'Data Types' (Types).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 4. *Lines:* 224, 338, 376, 975. *Example:* one space before the inline comment where PEP8 asks for two (`a[-2::-1] # Walk backwards...`, 224); trailing whitespace on the `with` line and the `f.write` line that follows it (338-339); an 8-space body under the single-line double `with` at 375, where 4 is correct because no nesting remains (376-377); and a 2-space function body in the 'more pythonic' solution at 975, which sits 300 lines after the lecture's own '### Python Style Guidelines: PEP8' section.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 353, 403. *Example:* 2 sentences in one paragraph.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 305, 696, 868. *Example:* three sentences the reader has to repair on the fly: 'the present working directory (pwd) that can be located from with Jupyter or IPython via' (305) has two prepositions where one belongs; 'We've all heard the saying about consistency and little minds' (696) alludes to a quotation it never gives, so the paragraph's argument rests on something unstated; and 'Write a function `p` such that `p(x, coeff)` that computes the value in `` {eq}`polynom0` ``' (868) has a doubled relative clause in an exercise statement.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 413, 543. *Example:* both are references to material that is not where the text implies. '### Paths' opens with 'Note that if `newfile.txt` is not in the present working directory then this call to `open()` fails' (413), but no `open()` call is under discussion at that point - the last one shown is 15 lines earlier at 398, inside a different topic. And 543 offers to 'simplify the code for generating the list of random draws', which is the loop from python_by_example (labelled `firstloopprog` there) and appears nowhere above in this lecture; it finally surfaces 500 lines later in exercise pyess_ex6 (1068-1077).
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 1. *Lines:* 47. *Example:* mid-sentence 'Point'.

### Low severity
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 188. *Example:* '#### Slice Notation' (188-232) is entirely about positions in a sequence - `a[m:n]` returning `n - m` elements (207), negative indices (209-213), a step (215-219) and a negative step that walks backwards (221-225) - and it is carried by six REPL transcripts with no picture of the index positions. In a lecture with no figures at all, this is the one subsection whose subject is spatial, and a single labelled strip of `a[0]..a[4]` over `a[-5]..a[-1]` would do the work of the six cells.


## Strengths

- Every container type is introduced by constructing one and immediately printing `type(...)` (65-74, 138-146, 247-250, 263-266), so the reader watches the type system rather than reading about it.
- The `with`-statement material is built in four steps - write (338), read (349), nested read-and-write (357), then two contexts on one line (375) - and each step prints the resulting file back (367, 382, 397) so the effect is visible.
- The iteration example is self-contained: `%%writefile` puts `us_cities.txt` in the working directory (442-453) so the loop at 461-469 runs for every reader instead of assuming a downloaded file.
- Exercise solutions routinely give a plain version and then a more idiomatic one (819-839, 915-933, 957-989), which teaches the idiom instead of asserting it.
- Backward references are `{ref}` links to real labels - `lists_ref` at 131, `tuple_unpacking_example` at 184 - rather than prose pointers.

## Recommended actions

1. Lower-case the 14 Title Case headings (31, 58, 61, 111, 188, 234, 284, 435, 485, 538, 567, 631, 682, 687) - qe-writing-006, 14 occurrences and by far the largest fix.
2. Restore one convention for definitions: bold at 256, 258, 543 and 714 as the lecture already does at 63, 89, 117, 136, 148 and 150, and make **any** at 610 italic.
3. Repair the three broken sentences at 305, 868 and the lower-case sentence opening at 390 ('we can switch the mode to `a`').
4. Fix the PEP8 slips: two spaces before the inline comment at 224, trailing whitespace at 338-339, the 8-space body at 376-377, and the 2-space indent at 975.
5. Add one small figure to '#### Slice Notation' (188) showing the index positions of a five-element list from both ends - it is the only spatial subsection in a lecture with no figures.
6. Give 543 a `{ref}` to the loop it is recalling (`firstloopprog` in python_by_example) and open '### Paths' (408-415) by naming the `open()` call it is talking about.
7. Split the two-sentence paragraphs at 353 and 403 (qe-writing-001, 2 occurrences), and either cut the 'consistency and little minds' allusion at 696 or give the quotation.
