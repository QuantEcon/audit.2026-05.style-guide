# `qe-math-012` — Multiplication: `\cdot` or juxtaposition, never `*`

**Target file:** `style_checker/rules/math-rules.md`
**Style-guide source:** [`math.md` § Multiplication in equations](https://github.com/QuantEcon/QuantEcon.manual/blob/main/manual/styleguide/math.md)

---

## Rule entry (ready to append to `math-rules.md`)

```markdown
### Rule: qe-math-012
**Type:** rule  
**Title:** Multiplication: use \cdot or juxtaposition — never *

**Description:**  
In math environments, multiplication is written as either `\cdot` (centered dot) or by juxtaposition (no operator). Never use the asterisk `*`, which renders as a low star $*$ and conventionally means convolution, optimum, or pullback in mathematical writing.

**Check for:**
- `*` between two math tokens inside `$...$` or `$$...$$`
- `*` in `{math}` roles
- `*` inside `aligned` environments

**Important exceptions:**  
- Code blocks (where `*` is valid Python multiplication) — must not be flagged
- `**` (double asterisk) — bold markdown emphasis or Python exponentiation, not math multiplication
- `\ast` — legitimate operator with a different meaning (e.g., convolution); don't flag

**Examples:**
```markdown
<!-- ✅ Correct -->
$a \cdot b$
$ab$ (juxtaposition)
$2x$, $\pi r^2$
$$
y = X \beta
$$

<!-- ❌ Incorrect -->
$a * b$
$\pi * r^2$
$$
y = X * \beta
$$
```

**Implementation note:**  
Regex `\*` (single asterisk) restricted to text inside `$...$`, `$$...$$`, and `{math}` regions. Exclude code blocks. Watch for `**` which is markdown bold or Python `pow`, not multiplication.
```

---

## Rationale (for issue / PR body, not for the rules file)

**Style-guide quote** (`math.md`):
> Use `\cdot` or juxtaposition for multiplication in LaTeX — never use `*`.

**Corpus evidence (May 2026 audit):** Small count (~5 lectures), notably `python_by_example.md:* in $\pi * r^2$`. Low frequency but clear, unambiguous rule with zero judgment cost.

**Why mechanical:** Regex check inside math environments only. Need careful exclusion of code blocks (where `*` is valid Python operator) and `**` (markdown bold / Python exponent). Phase 4.3 candidate, low priority by frequency but high priority by rendering correctness — `*` renders as $*$ which is visually a different operator.
