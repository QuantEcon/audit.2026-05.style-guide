# `qe-writing-009` — Write "IID", not "i.i.d." or "iid"

**Target file:** `style_checker/rules/writing-rules.md`
**Style-guide source:** [`writing.md` § General writing advice](https://github.com/QuantEcon/QuantEcon.manual/blob/main/manual/styleguide/writing.md); [`math.md` § IID](https://github.com/QuantEcon/QuantEcon.manual/blob/main/manual/styleguide/math.md)

---

## Rule entry (ready to append to `writing-rules.md`)

```markdown
### Rule: qe-writing-009
**Type:** rule  
**Title:** Write "IID" in text — not "i.i.d." or "iid"

**Description:**  
When referring to independent and identically distributed random variables in narrative text, always write "IID" (uppercase, no dots). Do not use "i.i.d.", "iid", "I.I.D.", or other variants.

**Check for:**
- "i.i.d." (any case combination) in narrative text
- "iid" (any case combination) in narrative text
- Inside math environments, "IID" should not appear at all — use mathematical notation

**Examples:**
```markdown
<!-- ✅ Correct -->
Let $\{X_t\}_{t=0}^{\infty}$ be a sequence of IID random variables.

The errors are assumed to be IID with mean zero and variance $\sigma^2$.

<!-- ❌ Incorrect -->
Let $\{X_t\}_{t=0}^{\infty}$ be a sequence of i.i.d. random variables.

The errors are assumed to be iid with mean zero and variance $\sigma^2$.

The errors are I.I.D. normal.
```

**Implementation note:**  
Case-sensitive regex outside fenced code, inline code, and math blocks:
- `\bi\.i\.d\.\b` — matches "i.i.d.", "I.i.d.", etc.
- `\biid\b` (case-insensitive) — matches "iid", "IID" (negative match), "Iid"

Replace with `IID`.
```

---

## Rationale (for issue / PR body, not for the rules file)

**Style-guide quote** (`writing.md`):
> If you have a choice between two reasonable options, always pick the simplest one. […] write "IID" in text (not "i.i.d." or "iid")

`math.md` § IID also documents this convention.

**Corpus evidence (May 2026 audit):** ~30 lectures across the corpus. Concentrated in `lecture-python.myst` (21 / 110 lectures), with smaller counts in `lecture-python-advanced.myst` (5 / 55).

**Why mechanical:** This is a pure regex check with zero ambiguity. Strong Phase 4.3 candidate.
