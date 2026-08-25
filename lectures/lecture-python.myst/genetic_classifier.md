# genetic_classifier

- **Series:** lecture-python.myst
- **File:** `lectures/genetic_classifier.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `e25fdf2345`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.7 / 10
- **Priority:** NONE

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 5.5/10 | `qe-writing-005` ×4; `qe-writing-002` ×3; `qe-writing-006` ×1, +2 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 8.5/10 | `qe-code-001` ×3. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-004` ×2; `qe-fig-003` ×1; `qe-fig-001` ×4. |
| References   | 10/10 | no mechanical violations detected. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 1. *Lines:* 178. *Example:* H2 Title Case: 'Associative memory: the Hopfield network' (Hopfield).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 3. *Lines:* 111, 359, 402. *Example:* line 111 pads the assignment operator to align with the line above (`players    = ...`) and pads inside the mean vector (E221, E241); lines 359-361 put the return statement on the same line as the `if` (E701) with padding after the colon; and lines 402-406 define the five panel strategies as one-line `def ... : return ...` bodies (E704), again column-aligned. All three read as deliberate tables, but PEP8 rules out the construct rather than the spacing.
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 4. *Lines:* 151, 262, 458, 588. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 1. *Lines:* 275. *Example:* .set_title.
- **[qe-fig-004]** — Caption formatting conventions. *Count:* 2. *Lines:* 252, 563. *Example:* caption of 7 words.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 3. *Lines:* 306, 812, 818. *Example:* three sentences run past 40 words with the argument hung off a colon: 48 words at 306-309 (the simulated-annealing geometry), 40 at 812-814 (sign reversals), and 42 at 818-820, which also restates what 306-309 already explained about declining random shaking - the solution can point back to the section instead of re-deriving it.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 4. *Lines:* 47, 560, 599, 670. *Example:* four bolds carry emphasis rather than definition: 'They **discover the rule itself**' (47), 'start with **equal** strengths' (560), 'converges, but **not to one**' (599), and 'must **emerge** from how agents choose to trade' (670). The file is otherwise disciplined - italic does the emphasis (39, 165, 284, 307, 319, 335, 339, 478, 487, 523, 541, 622, 641, 652) and bold names the terms being introduced (83, 93, 128, 188, 318, 365, 523, 534-543, 626, 649).
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 164, 626. *Example:* two claims that the lecture makes visually elsewhere are left as prose. The Minsky-Papert critique at 164-166 - a single perceptron 'cannot separate classes that a line cannot' - is the canonical two-panel picture, and the separable case is already plotted 15 lines above at 151-159, so the non-separable partner costs almost nothing. The bucket brigade at 626-635 is the one component of the classifier system that is described but never drawn or run: reward seeping backward along a chain of rules is a diagram, and it is the mechanism the lecture says the next one depends on.

### Low severity
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 622. *Example:* '### A two-armed bandit' outgrows its title: from 615 to 635 the text leaves the bandit behind and discusses accounting schemes in general, sequential credit assignment, and the bucket brigade - material about classifier systems as such, which belongs in the parent section at 519 rather than inside its worked example.


## Strengths

- All four figure cells carry mystnb `caption` and `name` metadata (145-149, 253-257, 452-456, 564-568), so every figure in the lecture is addressable.
- The claim that a perceptron is essentially a linear discriminant is checked rather than asserted: the trained boundary normal and Fisher's direction are computed and compared by cosine similarity at 132-141, which is what licenses 'the two directions are all but identical' at 162.
- Axelrod's headline result is reproduced and then honestly bounded - 'The margin is not large, and it should not be' (514) followed by the reason (516-517) - and the champion is scored opponent by opponent (471-476) rather than by a single aggregate.
- The probability-matching result is established three ways: as a figure against both the matching and the optimal benchmark (588-596), as a sweep over three reward pairs (603-608), and then as the motive for exercise gc_ex3's softmax fix (910-972).
- The gc_ex2 solution ends with a `{note}` retracting part of its own conclusion at higher mutation rates (896-905) instead of leaving the reader with a result that does not generalise.
- Code identifiers use unicode Greek where the mathematics does - `σ`, `Σ`, `μ`, `τ`, `β` (218, 223, 570-581, 940-950) - and each helper carries a one-line docstring saying what it computes (221, 228, 232, 358, 375, 412, 571).

## Recommended actions

1. Convert the four bold emphases at 47, 560, 599 and 670 to italic, which is what the rest of the file uses.
2. Add the two missing pictures: a non-separable companion to the perceptron scatter at 164-166, and a bucket-brigade diagram at 626-635 - currently the only classifier-system component with neither figure nor code.
3. Bring the three compact code tables into PEP8 form: one statement per line at 359-361 and 402-406, and drop the alignment padding at 111.
4. Make the panel randomizer explicit: `random_play` reads the module-level `panel_rng`, which is reset at 445, 501 and 869-871 so that comparisons line up, and any cell re-run out of order silently changes the reported fitnesses. Passing an rng into `play` and `fitness` removes the ordering dependence.
5. Move the general accounting discussion at 615-635 out of '### A two-armed bandit' and into '## Classifier systems'.
6. Split the three 40-plus-word sentences at 306, 812 and 818, and replace the annealing recap at 818-820 with a pointer back to 306-309.
7. Trim the two seven-word figure captions at 252 and 563 (qe-fig-004) and drop the four `figsize=` overrides at 151, 262, 458 and 588 (qe-fig-001).
