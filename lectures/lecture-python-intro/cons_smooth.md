# cons_smooth

- **Series:** lecture-python-intro
- **File:** `lectures/cons_smooth.md`
- **Audit date:** 2026-08-26
- **Corpus snapshot:** `a12d17c0ef`
- **Categories audited:** writing, math, code, figures, references, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.1 / 10
- **Priority:** LOW

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4.5/10 | `qe-writing-002` ×9; `qe-writing-001` ×2; `qe-writing-005` ×3, +2 more. |
| Math         | 10/10 | no mechanical violations detected. |
| Code         | 7.5/10 | `qe-code-001` ×6. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 6/10  | `qe-fig-005` ×7; `qe-fig-008` ×10; `qe-fig-006` ×1, +1 more. |
| References   | 9/10  | `qe-ref-001` ×1. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 6. *Lines:* 316, 366, 451, 463, 475, 579. *Example:* lines 316 and 366 write `figsize=(12,5)` with no space after the comma; line 579 writes `ϕs= [.95, 1.02]` with a space after the equals sign and none before; lines 451, 463 and 475 put spaces around the exponentiation operator (`λ ** np.arange(t_max)`) where the rest of the file consistently writes it tight (`β**i` at 148, `growth**(T+1)` at 558, `ϕ**t` at 562).
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 7. *Lines:* 312, 575, 634, 652, 859, 923, 991. *Example:* code-cell figure without mystnb figure metadata.
- **[qe-fig-008]** — Use lw=2 for line charts. *Count:* 10. *Lines:* 596, 600, 637, 644, 655, 662, 885, 936, 943, 1020. *Example:* plot() without lw=.
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 9. *Lines:* 19, 27, 51, 57, 136, 254, 348, 428, 670. *Example:* nine over-long or redundant sentences. Line 27-30 is a single 48-word sentence carrying three ideas (what inspired Friedman, that wages are a dividend stream, that asset-pricing formulas then apply); line 19 is 41 words and opens the lecture; lines 51, 57, 136, 254, 428 and 670 run 30-36 words each. Line 348 contains a duplicated word - 'different sequences sequences of non-financial income'.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 86. *Lines:* 19, 21, 23, 25, 27, 30, 33, 34, 51, 55, …. *Example:* 2 spaces.

### Medium severity
- **[qe-fig-001]** — Do not set figure size unless necessary. *Count:* 3. *Lines:* 316, 366, 931. *Example:* figsize=.
- **[qe-writing-001]** — Use one sentence per paragraph. *Count:* 2. *Lines:* 746, 822. *Example:* 2 sentences in one paragraph.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 3. *Lines:* 110, 542, 673. *Example:* bold doing emphasis work at line 110 ('there are **many** budget feasible consumption paths') and line 673 ('**lowers** the government expenditure multiplier'), both of which want italic; and line 542 uses bold as a pseudo-heading ('**Key Idea:**'). The lecture's other eight bolds correctly mark definitions.

### Low severity
- **[qe-fig-006]** — Lowercase axis labels. *Count:* 1. *Lines:* 1023. *Example:* axis label `Welfare`.
- **[qe-ref-001]** — Use correct citation style. *Count:* 1. *Lines:* 183. *Example:* `` {cite} `` in author position: '`` {cite}`Hall1978` `` showed'.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 1. *Lines:* 92. *Example:* lines 92-105 walk the reader through an iterative procedure - guess a consumption path, compute wealth, check the terminal condition, and 'if the candidate consumption path is not budget feasible, propose a less greedy consumption path and start over'. The lecture never implements it: section 201 computes c_0 in closed form from eq:conssmoothing and no search ever happens, so the reader has been taught an algorithm the lecture abandons.


## Strengths

- The four income experiments (one-time windfall, permanent raise, late starter, geometric earner) all run through the `plot_cs` helper introduced at line 350, and the text at line 352 says why - so the four sets of panels are drawn on the same footing and are directly comparable.
- The variational argument at lines 482-546 is constructed rather than asserted: a two-parameter admissible variation class is defined, the zero-present-value constraint is solved for xi_0 across four displayed steps, and the resulting welfare surface is then differentiated numerically with `np.gradient` at line 609.
- The claim that terminal wealth is exactly zero is checked in code at lines 302-332 rather than trusted from the algebra, and the text at line 332 points at the computed result.
- The appendix at lines 678-895 shows the same matrix-inversion technique solving first-, second- and third-order difference equations, and at lines 770-786 verifies a claimed closed-form inverse against the identity matrix instead of just stating it.
- The lecture is explicit about where it sits in the series - the Keynesian consumption function in geom_series, present-value formulas in pv - and returns to that thread at lines 668-675 to say what the model implies for the fiscal multiplier.

## Recommended actions

1. Remove the 86 double spaces flagged by qe-writing-008 (starting at lines 19, 21, 23, 25, 27, 30, 33, 34, 51, 55) - at that density the source reads as if it had been pasted together, and several of them sit inside sentences the reader is meant to parse carefully.
2. Break the nine long sentences at lines 19, 27, 51, 57, 136, 254, 428 and 670 into one idea each, starting with the 48-word sentence at 27-30, and delete the duplicated word at line 348.
3. Either implement the iterative budget-feasibility search described at lines 92-105 or replace it with a forward pointer to the closed-form solution the lecture actually uses at line 195.
4. Add mystnb figure metadata to the eight figure cells at lines 312, 354, 575, 634, 652, 859, 923 and 991 (qe-fig-005), set `lw=2` on the ten plot calls at 596, 600, 637, 644, 655, 662, 885, 936, 943 and 1020 (qe-fig-008), drop the `figsize=` overrides at 316, 366 and 931 (qe-fig-001), and lowercase the axis label at 1023 (qe-fig-006).
5. Move the five author-position citations at lines 19, 35, 127, 183 and 670 into the parenthetical form (qe-ref-001), and delete the stray unmatched closing parenthesis after `{cite}`Hall1978`` at lines 19 and 670.
6. Switch the emphasis bolds at lines 110 and 673 to italic and turn the '**Key Idea:**' at line 542 into a real heading or an ordinary sentence.
7. Fix the six PEP8 spacing sites, the two-sentence paragraphs at lines 746 and 822, and the typos: 'streams on non-financial income' (136), 'consumption-smoothingmodel' (673), 'Compute an time 0 consumption' (218), 'two given initial equations' (796), and the missing full stop at the end of line 428.
