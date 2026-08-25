# names

- **Series:** lecture-python-programming
- **File:** `lectures/names.md`
- **Audit date:** 2026-08-25
- **Corpus snapshot:** `ceec881028`
- **Categories audited:** writing, code, figures, links, admonitions  *(JAX out of scope)*
- **Overall score:** 7.7 / 10
- **Priority:** HIGH

## Score breakdown

| Category     | Score | One-line note |
|--------------|-------|---------------|
| Writing      | 3/10  | `qe-writing-006` ×8; `qe-writing-005` ×5; `qe-writing-003` ×3, +3 more. |
| Math         | N/A   | no mathematical content. |
| Code         | 8.5/10 | `qe-code-001` ×2. |
| JAX          | out of scope | JAX rules target `lecture-jax`. |
| Figures      | 7/10  | `qe-fig-005` ×9; `qe-fig-002` ×9. |
| References   | N/A   | no citations in this lecture. |
| Links        | 10/10 | no mechanical violations detected. |
| Admonitions  | 10/10 | no mechanical violations detected. |

## Issues

### Critical
_None found._

### High severity
- **[qe-fig-002]** — Prefer code-generated figures. *Count:* 9. *Lines:* 453, 459, 469, 477, 524, 529, 536, 560, 564. *Example:* static image .png.
- **[qe-fig-005]** — Descriptive figure names for cross-referencing. *Count:* 9. *Lines:* 453, 459, 469, 477, 524, 529, 536, 560, 564. *Example:* {figure} without :name:.
- **[qe-writing-005]** *(reviewer)* — Use bold for definitions, italic for emphasis. *Count:* 5. *Lines:* 217, 273, 300, 304, 407. *Example:* the file gets bold right five times - **name** and **binds** (54), **rebound** (78), **namespace** (115), **LEGB rule** (421), **mutable** (507) - and then inverts it: "**all** code executed by the interpreter" (217) is emphasis in bold, while four definitions are in italic - the global namespace is "*the namespace of the module currently being executed*" (273), a *local namespace* (300), *local variables* (304) and the *enclosing function* (407).
- **[qe-writing-006]** — Capitalize lecture titles properly. *Count:* 8. *Lines:* 35, 180, 212, 266, 295, 327, 367, 482. *Example:* H2 Title Case: 'Variable Names in Python' (Names).

### Medium severity
- **[qe-code-001]** *(reviewer)* — Follow PEP8 unless closer to mathematical notation. *Count:* 2. *Lines:* 83, 177. *Example:* trailing whitespace inside code cells after `x = 'bar'` (83) and `math.__dict__['pi']` (177) - pycodestyle W291.
- **[qe-writing-003]** *(reviewer)* — Maintain logical flow. *Count:* 3. *Lines:* 93, 281, 302. *Example:* 93-95 is a two-sentence aside on garbage collection as a research area, with a link, and the lecture never returns to it; 281-285 drops from executed cells to a hypothetical `no-execute` `import amodule` for the whole global-namespace section, breaking the demonstrate-everything pattern the rest of the lecture holds to; and 302's "The reason for this will be explained in just a moment" is never redeemed - name resolution arrives at 367, three sections later, without ever picking that thread up.

### Low severity
- **[qe-writing-002]** *(reviewer)* — Keep writing clear, concise, and valuable. *Count:* 1. *Lines:* 87. *Example:* "In this case, after we rebind `x` to `'bar'`, no names bound are to the first object `'foo'`" - the word order is broken in the sentence that carries the reason garbage collection is triggered.
- **[qe-writing-007]** *(reviewer)* — Use visual elements to enhance understanding. *Count:* 1. *Lines:* 300. *Example:* "Important fact:" is written inline as the lead-in to the lecture's key claim about local namespaces, in a file that establishes its own admonition conventions with `{admonition} Definition` at 114 and `{note}` at 539 - the rule explicitly lists opportunities to use admonitions for important notes.
- **[qe-writing-008]** — Remove excessive whitespace between words. *Count:* 1. *Lines:* 383. *Example:* 2 spaces.


## Strengths

- Binding is demonstrated before it is named: `g = f` with `id(g) == id(f)` (60-66), then the rebinding of `x` and its consequence for garbage collection (80-91).
- The LEGB rule is derived rather than announced - two directly accessible namespaces (385-388), three inside a function (390-394), then enclosing functions (398-408) - and only given its name at 421.
- The `test.py` trace (431-478) walks five namespace snapshots with a figure at each step, which is the right medium for this material and the reason the lecture works.
- The mutable-versus-immutable pair (488-495 against 509-516) differs by a single character in the function body, so the difference in behaviour cannot be attributed to anything else.
- `math.pi` against `mathfoo.pi` (123-152) shows two identical names coexisting, using a module the reader writes in the notebook with `%%file` rather than one they have to imagine.

## Recommended actions

1. Sentence-case the eight headings (35, 180, 212, 266, 295, 327, 367, 482).
2. Move the nine figures out of `/_static/lecture_specific/oop_intro/` into a `names/` directory and rename the `(oop_names)=` target at 12 - both are leftovers from when this content lived in `oop_intro`.
3. Regenerate the nine namespace diagrams from code and give each a `:name:` and caption (qe-fig-002 ×9, qe-fig-005 ×9 at 453, 459, 469, 477, 524, 529, 536, 560, 564) - the prose refers to them only by position.
4. Bold the four definitions now in italic (273, 300, 304, 407) and italicise the bold emphasis at 217; the file already bolds five terms correctly, so this is consistency work.
5. Turn "Important fact:" (300) into a `{note}`, matching the `{admonition} Definition` at 114.
6. Fix 87 ("no names bound are to the first object"), cut the garbage-collection aside at 93-95, and either redeem or delete the promise at 302.
7. Update 336-337: `__builtin__` is the Python 2 module name - in Python 3 it is `builtins`; also strip the trailing whitespace at 83 and 177 and the double space at 383.
