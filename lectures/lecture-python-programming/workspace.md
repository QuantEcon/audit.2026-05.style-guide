# workspace

- **Series:** lecture-python-programming
- **File:** `lectures/workspace.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-004` ×4; `qe-writing-005` ×3; `qe-writing-003` ×2, +2 more. |
| Math         | N/A   | no mathematical content. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5.5/10 | `qe-fig-005` ×17; `qe-fig-003` ×2; `qe-fig-008` ×2. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 17. *Lines:* 56, 141, 149, 164, 169, 185, 199, 221, 227, 232, …. *Example:* {figure} without :name:.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 211. *Example:* H2 Title Case: 'A walk through Visual Studio Code' (Visual, Studio, Code).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 89, 90, 104. *Example:* the two example scripts, which are the reader's model for 'longer programs', are not PEP8: a space before the annotation colon in `def plot_wave(title : str = 'Sine Wave')` (89), a 2-space body indent instead of 4 (90-97), and one space before the inline comment where PEP8 asks for two in `import sine_wave # Import the sine_wave script` (104).
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 2. *Lines:* 69, 96. *Example:* plt.title.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 2. *Lines:* 66, 93. *Example:* plot() without lw=.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 31, 75. *Example:* line 31 ('Jupyter Notebooks are well suited to interactive computing ... and can help execute chunks of code one at a time') restates the point already made at 29 ('While they are efficient and adaptable when working with short pieces of code, Notebooks are not the best choice for longer programs'), interrupting the Overview's argument to repeat its premise; and 75 pads a simple claim - 'One major advantage of using Python scripts lies in the fact that you can "import" functionality' - where 'One major advantage of Python scripts is that you can import' says the same thing.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 114, 259. *Example:* '## Development environments' (114-121) states that 'This lecture takes you through the workings of two development environments' and then ends, with both environments following as sibling H2s (123, 211) rather than as its subsections, so the heading structure denies the relationship the text asserts; and at 259 'Further discussions about version control can be found in the next section' points forward across two intervening subsections (286, 301) to '## Git your hands dirty' at 319.
- **[qe-writing-004]** — Avoid unnecessary capitalization in narrative text. *Count:* 4. *Lines:* 37, 213, 246, 252. *Example:* mid-sentence 'Code'.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 294, 323, 325. *Example:* the two definitions in the Git section are italicised, not bolded - Git 'is a *version control system*' (323) and 'the associated collections of files --- called *repositories* ---' (325) - which is the reverse of the rule; and at 294 bold is used for a UI label (**Run Current File in Interactive Window**) although every other UI label in the lecture is plain text (155-156, 246, 252, 261).

### Low severity
_None found._


## Strengths

- The `%%writefile` cell at 83 creates the very file that the next cell imports at 104, so the 'import from another script' lesson actually executes rather than being described.
- Every step of both walkthroughs is anchored to a screenshot of the exact screen the reader is looking at - 16 `{figure}` directives between 141 and 309 - which is what makes a UI tour followable.
- The three `{note}` admonitions carry genuine asides: the Anaconda assumption (44-48), the ipykernel console alternative (203-209) and Docker being out of scope (313-317). None of them is used for emphasis.
- The script listings carry `:caption:` and `:lineno-start:` (57-58, 80-81, 101-102), so each cell is labelled with the file it stands for and its line numbers match the file.
- One sentence per paragraph holds across the whole file - the scanner records no qe-writing-001 at all, which is unusual for a 371-line lecture.

## Recommended actions

1. Add a `:name:` (and a caption) to each of the 17 figures (56, 141, 149, 164, 169, 185, 199, 221, 227, 232, 237, 248, 254, 267, 290, 296, 309) - qe-fig-005, 17 occurrences and the largest fix here; a screenshot walkthrough is exactly where `{numref}` pointers pay off and none of these can currently be referenced.
2. Bold the definitions at 323 and 325 and keep italics for emphasis; then either drop the bold on the UI label at 294 or bold every UI label, since all the others are plain.
3. Make the two example scripts PEP8-clean: 4-space indent at 90-97, `title: str` at 89, two spaces before the inline comment at 104.
4. Fix the forward reference at 259 - point at '## Git your hands dirty' (319) with a `{ref}`, or move the sentence to the end of the VS Code section.
5. Decide what '## Development environments' (114) is for: demote 123 and 211 to subsections under it, or fold its three lines into the Overview.
6. Repair the typos: 'write to to a file' (77), 'go ahead an install' (230), 'in the the current working directory' (279).
7. Move the two `plt.title(...)` calls (69, 96) out of the code into mystnb figure captions and set `lw=2` on the two plots (66, 93) - qe-fig-003 and qe-fig-008, 2 occurrences each.
