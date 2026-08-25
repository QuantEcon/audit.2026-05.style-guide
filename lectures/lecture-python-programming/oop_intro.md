# oop_intro

- **Series:** lecture-python-programming
- **File:** `lectures/oop_intro.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, links, admonitions  *(JAX out of scope)*
- **Overall score:** 8.2 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 4/10  | `qe-writing-006` ×3; `qe-writing-005` ×5; `qe-writing-002` ×2, +2 more. |
| Math         | N/A   | no mathematical content. |
| Code         | 9/10  | `qe-code-001` ×1. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | N/A   | no figures or plotting code. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 5. *Lines:* 74, 131, 193, 199, 209. *Example:* the lecture's four central terms are all defined in italic: "an *object* is a collection of data and instructions" (74), "Python is *strongly typed*" (131), "Any name following a dot is called an *attribute*" (193), "attributes that act like functions, called *methods*" (199) and "Methods are *functions that are bundled with objects*" (209) - an italicised definitional clause; the same file bolds **methods** correctly at 36 and **callable** at 211, so the pattern it needs is already there.
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 3. *Lines:* 168, 261, 283. *Example:* H3 Title Case: 'Object Content: Data and Attributes' (Content, Attributes).

### Medium severity
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 2. *Lines:* 302, 346. *Example:* 302-303 reads "It's quite common for users to add methods to their that measure the length of the object" - the noun after "their" is missing; and the lecture's closing sentence at 346 reads "Remember that everything is an object will help you interact with your programs".

### Low severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 1. *Lines:* 398. *Example:* the `for` body in the exercise solution is indented two spaces instead of four at 398-401 (pycodestyle E111), and the accumulator it fills is named `callablels` (395).
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 150. *Example:* "Identity" (144-166) makes the point that `y` and `z` can hold the same value at different memory addresses, and "the identity of an object is in fact just the address of the object in memory" (166) - the canonical two-boxes-one-value diagram, in a lecture that has no figures at all, while its companion `names.md` draws exactly this picture for a neighbouring idea.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 342. *Example:* 2 spaces.


## Strengths

- The paradigm question is answered concretely: procedural, object-oriented and functional are each characterised in a few bullets (27-44) before the lecture commits to "in Python, everything is an object" (56) as the claim to be explained.
- `x[0] = 'aa'` is shown to be `x.__setitem__(0, 'aa')` (243-257) - the cheapest possible demonstration that syntax the reader already uses is a method call.
- "A Little Mystery" (283-330) takes the obvious objection seriously - why `len(x)` and not `x.len()` - gives the design reason, and then closes it by calling `x.__len__()` directly.
- `rich`'s `inspect` (261-279) lets the reader see an object's attributes and then its methods without a `dir()` wall of text, and the install cell sits at the top of the lecture where qe-code-003 wants it.
- The four constituents of an object announced at 76-79 each get their own H3 in exactly that order (84, 145, 168, 204).

## Recommended actions

1. Bold the five italicised definitions (74, 131, 193, 199, 209) - italic is for emphasis only, and this file already uses bold correctly at 36 and 211.
2. Fix the two broken sentences at 302-303 and 346; 346 is the last sentence of the lecture.
3. Sentence-case the three headings (168, 261, 283).
4. Add a figure to "Identity" (144-166): two names, two addresses, one value - this lecture currently has no figures, and `names.md` already has the diagram.
5. Re-indent the exercise solution at 397-401 to four spaces and rename `callablels` (395).
6. Add the missing blank lines after the code cells at 272 and 324, so the prose at 273 and 325 is not glued to the closing fence.
7. Replace the double-backtick ``imag`` at 195 with single backticks, and delete the double space at 342 (qe-writing-008).
