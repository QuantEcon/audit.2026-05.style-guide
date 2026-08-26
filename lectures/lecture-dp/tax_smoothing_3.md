# tax_smoothing_3

- **Series:** lecture-dp
- **File:** `lectures/tax_smoothing_3.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `c30490a2f4`
- **Categories audited:** writing, math, code, figures, references, links  *(JAX out of scope)*
- **Overall score:** 8.0 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 6/10  | `qe-writing-003` ×2; `qe-writing-002` ×2; `qe-writing-008` ×19, +1 more. |
| Math         | 8.5/10 | `qe-math-011` (proposed) ×1; `qe-math-009` ×1. |
| Code         | 10/10 | no mechanical violations detected. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 5/10  | `qe-fig-003` ×4; `qe-fig-006` ×4; `qe-fig-005` ×2, +2 more. |
| References   | 8.5/10 | `qe-ref-001` ×2. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | N/A   | no admonitions, exercises or solutions. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 19. *Lines:* 29, 32, 33, 35, 39, 41, 44, 100, 101, 103, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 2. *Lines:* 273, 314. *Example:* figsize=.
- **[qe-fig-003]** — No matplotlib embedded titles. *Count:* 4. *Lines:* 275, 278, 316, 319. *Example:* .set_title.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 2. *Lines:* 262, 290. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 4. *Lines:* 276, 279, 317, 320. *Example:* axis label `Time`.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 4. *Lines:* 274, 277, 315, 318. *Example:* plot() without lw=.
- **[qe-math-011 (proposed)]** — Distribution names in plain letters, not \mathcal / \mathbb. *Count:* 1. *Lines:* 97. *Example:* decorated distribution `{\cal N}`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 2. *Lines:* 32, 35. *Example:* `` {cite} `` in narrative flow: 'of  `` {cite} ``'.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 254, 296. *Example:* (1) The second experiment's cell (290-322) repeats the first almost entirely: `As`, `Bs`, `Cs`, `Rs` and `Qs` are rebuilt at 297-302 with values identical to 235-239, the taxation loop at 309-311 repeats 268-270, and the six plotting lines at 314-320 repeat 273-279. Only `M` at 291 differs from 225, and the derived `Q` and `W`. (2) The reading of the tax series at 252-260 breaks its own parallel structure: 'positive spikes occur when debt is positive...' is a single-item bullet at 254-255, and its counterpart 'Negative spikes occur when the government has positive asset holdings' is a plain paragraph at 257 - the same pattern as the one-item list at 143 and the one-space-indented list at 100-103, so none of the lecture's three lists is formed the same way.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 2. *Lines:* 143, 222. *Example:* two claims the reader is asked to take on trust in a lecture that is otherwise careful. (1) The '## A dead end' section turns on the assertion that the government 'would have an incentive to set $b_{t,t+1}$ to a large negative number in state 2 - it would accumulate large amounts of *assets* to bring into period $t+1$ because that is cheap' (138-141, which also ends without a full stop), and the entire support for it is a one-item bullet list: '* Riccati equations will tell us this' (143). Since this is the reason the whole four-state construction exists, it needs the Riccati equation, a reference, or a computed counter-example. (2) The prose says 'we put a large penalty on the $b_{t-1,t}$ element of the state vector in states 2 and 4' (171-172) and the code does two things: `R2[0, 0] = R[0, 0] + 1e12` (223), which is that penalty, and `R1[0, 0] = R[0, 0] + 1e-9` (222), which is never mentioned anywhere in the lecture. A reader cannot tell whether the 1e-9 is a modelling choice or a numerical-conditioning fix.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 2. *Lines:* 178, 290. *Example:* (1) The four-state Markov chain is the lecture's central construction and is presented only as a $4\times4$ matrix (181-185). The prose that follows it is a description of a graph - 'This transition matrix ensures that the Markov state cannot move, for example, from state 3 to state 1. Because state 3 is "bad today", the next period cannot have "good yesterday"' (188-191) - and the structural zeros are exactly what a four-node diagram with the good/bad labelling would make obvious. (2) The lecture's conclusion is a comparison between two parameterisations, and the two runs are plotted in two separate figures 30 lines apart (273-280 and 314-321) whose panels carry identical titles ('One-period debt issuance', 'Taxation'), identical axis labels and no indication of which price each uses. The claim at 324-328 - that with the lower interest rate 'the government has an incentive to increase debt over time' but debt is 'recurrently reset to zero' - is a statement about the difference between the two, and the reader has to hold one figure in memory while looking at the other.

### Low severity
- **[qe-math-009]** *(reviewer)* — Choose simplicity in mathematical notation. *Count:* 1. *Lines:* 77. *Example:* the debt variable carries two indices everywhere it is defined and used - $b_{t,t+1}$ for what is promised at $t$ and $b_{t-1,t}$ for what falls due (68-69, 86, 100-102, 132, 135, 138, 149) - and exactly one place, the statement of the government's problem at 77, writes the plan as $\{b_{t+1}, T_t\}_{t=0}^\infty$ with the first index dropped. That is the line a reader looks at to see what the government chooses, and it is the one line whose notation does not match the constraint two lines below it.


## Strengths

- The lecture shows the wrong model first and says why it is wrong: '## A dead end' (113-145) works out what happens if roll-over risk is modelled by setting the price $p^t_{t+1}$ to zero in the bad state, finds that the government responds by accumulating assets rather than by not borrowing, and only then introduces the four-state formulation. Spending thirty lines on an approach that fails is what makes the four-state construction look necessary rather than arbitrary.
- Every element of that construction is justified in turn: the four states as (today, yesterday) pairs (152-155), the meaning of 'effectively' spelled out as a penalty on inherited debt in the bad-yesterday states (157-176), and the structural zeros of $\Pi$ read off the labelling ('Because state 3 is "bad today", the next period cannot have "good yesterday"', 191).
- The code is a transcription of that structure rather than a re-derivation: `Rs = [R1, R2, R1, R2]` at 238 puts the penalty in states 2 and 4 as the prose says, and `As`, `Bs`, `Cs`, `Qs`, `Ws` are written as four-element lists of identical matrices (235-240) so a reader can see at a glance which primitives depend on the Markov state and which do not.
- Taxation is reconstructed from the budget constraint - `tax[i, :] = S @ x[:, i] + M @ u[:, i]` (270) - rather than read out of the LQ solution, so the spikes discussed at 252-260 are a consequence of the model's constraint rather than an artefact of the solver.
- The second experiment changes exactly one primitive and says which and why: 'we simply raise $p^t_{t+1}$ to $\beta + 0.02 = 0.97$' (287-288), implemented as `M = np.array([[-β - 0.02]])` (291), which makes the resulting change in the debt path attributable.
- The notation is set up in one place before it is used, with each symbol given its economic meaning in the same sentence (67-71: $T_t$, $b_{t,t+1}$, $G_t$, $p^t_{t+1}$), and the three-way classification into controls, endogenous state and exogenous price (100-103) tells the reader what the LQ formulation will need.

## Recommended actions

1. Put the two experiments in one figure - the two debt paths on one axis and the two tax series on another - or at minimum retitle the four panels so they name the price they were computed with; as written both cells produce panels called 'One-period debt issuance' and 'Taxation'.
2. Document the two penalty constants: say in prose that `1e12` (223) is the 'large penalty' of 171-172, and say what `1e-9` at 222 is for, or remove it.
3. Support the claim at 138-143 with the Riccati equation or a reference rather than the one-item bullet 'Riccati equations will tell us this', and end the sentence at 141 with a full stop.
4. Rewrite the second cell (290-322) to reuse the matrices built at 197-240 - only `M`, `Q` and `W` change - and make the two model cells consistent about `stationary_values()`, which the first calls at 243 and the second never does.
5. Write $b_{t,t+1}$ at 77 as it is written everywhere else, and draw the four-state transition graph beside the matrix at 181-185.
6. Fix the unbalanced ')' after the citations at 32 - there is no opening parenthesis in that sentence. The same stray character appears in `tax_smoothing_1.md` (41, 61) and `tax_smoothing_2.md` (32), so it is a family-wide copy; while there, check that `barro2003religion` is the intended second reference in all four places.
7. Mechanical items from the draft: `{cite:t}` at 32 and 35 where the citations are the sentence's subject and object (qe-ref-001 x2), plain `N` for `{\cal N}` at 97 (qe-math-011 (proposed)), the 19 double spaces (qe-writing-008), and on both figure cells - drop `figsize=` (273, 314), move the four embedded titles into mystnb captions (275, 278, 316, 319), lowercase the four `'Time'` axis labels (276, 279, 317, 320), add `lw=2` to the four plot calls (274, 277, 315, 318) and `name:` metadata to the two code-cell figures (262, 290).
8. This file is byte-identical to `lecture-python-advanced.myst/lectures/tax_smoothing_3.md`, so every fix belongs upstream; the findings are double-counted in the corpus totals until the two are re-synced.
