# getting_started

- **Series:** lecture-python-programming
- **File:** `lectures/getting_started.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×17; `qe-writing-005` ×9; `qe-writing-003` ×2, +2 more. |
| Math         | N/A   | no mathematical content. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×12. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 12. *Lines:* 154, 182, 195, 207, 230, 276, 320, 338, 357, 363, …. *Example:* {figure} without :name:.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 9. *Lines:* 88, 102, 199, 211, 224, 240, 242, 372, 415. *Example:* the convention is inverted throughout: the four bold spans are all emphasis - "the core Python language **and**" (88), the whole sentence at 102, "**depends on which mode you are in**" (242), "**static** html representations" (415) - while the terms being defined are italic or unmarked: the Jupyter *dashboard* (199), an *active cell* (211), *edit mode* (224), a *modal* editing system (240), and "Debugging is the process of identifying and removing errors from a program" (372) with nothing marked at all.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 17. *Lines:* 50, 67, 77, 213, 220, 238, 261, 268, 306, 329, …. *Example:* H2 Title Case: 'Python in the Cloud' (Cloud).

### Medium severity
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 63, 74, 394. *Example:* three sentences are broken rather than merely long: 63-64 "Most of our lectures include a \"Launch notebook\" button (with a play icon) on the top right connects you to an executable version on Colab" is missing its relative pronoun; 74 reads "runs you through the some details"; and 394 reads "using the buttons on the \"Next\" button on the CALLSTACK toolbar".
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 56, 268. *Example:* Colab is recommended as the way to start (52-64) two sections before Jupyter notebooks are introduced at 131, so the reader is told to run notebooks in the cloud before being told what a notebook is; and "A Test Program" - item 4 of the five-item plan at 42-48 - arrives at 268 as an H4 buried under "Notebook Basics", so the promised structure and the delivered structure do not line up.

### Low severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 144. *Example:* 2 spaces.


## Strengths

- The cloud-first ordering is the right call for a first lecture: Colab (50-64) gets a reader executing code before any local install is attempted, and the local route is honestly framed as the one that "require[s] more work" (72).
- Twelve screenshots carry the walkthrough (154, 182, 195, 207, 230, 320, 338, 357, 363, 378, 397), so every instruction is paired with what the reader should actually see on screen.
- Modal editing - the thing that most confuses new notebook users - gets its own subsection with both modes tabulated and both switching keystrokes given (238-259).
- The test program is deliberately arbitrary and says so ("Don't worry about the details for now", 296), which keeps the reader's attention on running a cell rather than on polar bar charts.
- Cross-reference targets are set for exactly the things later lectures need to point at: `install_anaconda` (104), `a_test_program` (267), `gs_help` (328), `gs_install_qe` (452).

## Recommended actions

1. Sentence-case the 17 headings (50, 67, 77, 213, 220, 238, 261, 268, 306, 329 ...) - this alone accounts for the Writing score of 5.
2. Add `:name:` and a caption to the 12 figures (154, 182, 195, 207, 230, 276, 320, 338, 357, 363, 378, 397) - none can be cross-referenced today, yet the prose says "in the previous figure" (222) and "like so" (336).
3. Fix the three broken sentences at 63-64, 74 and 394.
4. Invert the emphasis convention: bold the definitions (dashboard 199, active cell 211, edit mode 224, debugging 372) and italicise the four emphases now in bold (88, 102, 242, 415).
5. Remove the leftover author comments and the inline `<style>` block from published source (21, 23-32, 385, 396) - move the CSS into `_static` and file the two IDEAs as issues.
6. Add a forward reference at 56 so the reader knows what a notebook is before being sent to run one in the cloud, or move the Colab recommendation after 131.
7. Delete the double space at 144 and the trailing double-space line breaks at 372, 383, 390, 392.
