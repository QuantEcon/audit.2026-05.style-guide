"""MyST lexer shared by the deterministic style checks.

Splits a MyST markdown lecture into typed regions so that each rule is applied
only where it is meaningful: ``qe-math-002`` (transpose) must not fire on an
apostrophe in prose, ``qe-writing-008`` (double spaces) must not fire inside a
code cell, and so on.

The lexer is deliberately line-oriented. Lecture sources are hand-written MyST,
not arbitrary CommonMark, so a fence/state machine reproduces the structure the
Jupyter Book build sees without pulling in a full markdown parser.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

# A fence line: optional indent, 3+ backticks/tildes/colons, optional {directive},
# optional info string (a language for plain code fences).
FENCE_RE = re.compile(r"^(\s*)(`{3,}|~{3,}|:{3,})[ \t]*(?:\{([^}]*)\})?[ \t]*(.*?)\s*$")

HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.*)$")

# Directives whose bodies are literal, never nested markdown.
CODE_DIRECTIVES = {
    "code-cell", "code", "code-block", "sourcecode", "literalinclude",
    "raw", "math", "eval-rst",
}
# ...of which these hold mathematics, and these hold neither code nor prose.
MATH_DIRECTIVES = {"math", "amsmath"}
OPAQUE_DIRECTIVES = {"raw", "eval-rst", "literalinclude"}


def body_kind(directive: str) -> str:
    """What a literal directive's body should be scanned as."""
    name = (directive or "").split()[0] if directive else ""
    if name in MATH_DIRECTIVES:
        return "math"
    if name in OPAQUE_DIRECTIVES:
        return "raw"
    return "code"

# Directives that open an exercise/solution region. ``qe-fig-003`` exempts
# embedded matplotlib titles inside these.
EXERCISE_DIRECTIVES = {"exercise", "solution", "exercise-start", "solution-start"}

# amsmath environments that are display math at the top level of a MyST file.
AMS_ENVS = (
    "align", "align*", "alignat", "alignat*", "aligned", "equation", "equation*",
    "gather", "gather*", "multline", "multline*", "flalign", "flalign*",
    "split", "eqnarray", "eqnarray*",
)
AMS_BEGIN_RE = re.compile(r"^\s*\\begin\{(" + "|".join(re.escape(e) for e in AMS_ENVS) + r")\}")
AMS_END_RE = re.compile(r"^\s*\\end\{(" + "|".join(re.escape(e) for e in AMS_ENVS) + r")\}")

INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
INLINE_MATH_RE = re.compile(r"(?<![\\$])\$(?!\$)((?:[^$\\\n]|\\.)+)\$(?!\$)")


@dataclass
class Fence:
    """One open fence on the stack."""

    marker: str
    directive: str
    info: str
    indent: int
    line_no: int

    @property
    def is_code(self) -> bool:
        if self.directive:
            return self.directive.split()[0] in CODE_DIRECTIVES
        # A plain fence is always literal content.
        return True


@dataclass
class Line:
    """One source line, tagged with the context the lexer found it in."""

    no: int                      # 1-indexed
    raw: str
    kind: str                    # text | code | math | fence | option | directive
    directives: tuple = ()       # enclosing directive names, outermost first
    in_exercise: bool = False
    in_table: bool = False

    @property
    def is_text(self) -> bool:
        return self.kind == "text"

    @property
    def is_code(self) -> bool:
        return self.kind == "code"

    @property
    def is_math(self) -> bool:
        return self.kind == "math"


@dataclass
class Doc:
    """A lexed lecture."""

    path: str
    stem: str
    series: str
    lines: list = field(default_factory=list)
    # display-math blocks: (start_line, end_line, delimiter, text)
    math_blocks: list = field(default_factory=list)
    # fence nesting observed: (line_no, marker, directive, parent_marker, parent_directive)
    nestings: list = field(default_factory=list)
    # directive openings: (line_no, directive, argument, options dict, marker)
    directives: list = field(default_factory=list)
    # closed directive blocks: (start, end, directive, argument, options, body_lines)
    blocks: list = field(default_factory=list)
    # gated ``*-start`` / ``*-end`` fences left open — a real tick-management fault
    unclosed_gated: list = field(default_factory=list)

    @property
    def n_lines(self) -> int:
        return len(self.lines)

    def text_lines(self):
        return [l for l in self.lines if l.kind == "text"]

    def code_lines(self):
        return [l for l in self.lines if l.kind == "code"]

    def math_lines(self):
        return [l for l in self.lines if l.kind == "math"]

    def code_text(self) -> str:
        return "\n".join(l.raw for l in self.lines if l.kind == "code")

    def narrative_text(self) -> str:
        return "\n".join(l.raw for l in self.lines if l.kind == "text")

    # Inline math spans, resolved across line breaks: (line_no, source).
    inline_spans: list = field(default_factory=list)
    # Narrative text per line with inline code and inline math blanked out.
    masked: dict = field(default_factory=dict)

    def math_text(self) -> str:
        parts = [l.raw for l in self.lines if l.kind == "math"]
        parts.extend(src for _, src in self.inline_spans)
        return "\n".join(parts)

    def headings(self):
        """(line_no, level, title) for every ATX heading in narrative text."""
        out = []
        for l in self.lines:
            if l.kind != "text":
                continue
            m = HEADING_RE.match(l.raw)
            if m:
                out.append((l.no, len(m.group(1)), m.group(2).strip()))
        return out


def _parse_options(lines, start):
    """Collect ``:key: value`` option lines (and a YAML ``---`` block) after a fence.

    Keys are flattened, but the raw block is kept under ``__raw__`` so checks that
    care about nesting (``mystnb.figure.name``, for instance) can look at it.
    """
    opts = {}
    raw = []
    i = start
    n = len(lines)
    if i < n and lines[i].strip() == "---":
        i += 1
        while i < n and lines[i].strip() != "---":
            raw.append(lines[i])
            if ":" in lines[i]:
                k, _, v = lines[i].partition(":")
                opts[k.strip().lstrip("-").strip()] = v.strip()
            i += 1
        i += 1
    while i < n:
        m = re.match(r"^\s*:([A-Za-z0-9_-]+):\s*(.*)$", lines[i])
        if not m:
            break
        raw.append(lines[i])
        opts[m.group(1)] = m.group(2).strip()
        i += 1
    opts["__raw__"] = "\n".join(raw)
    return opts, i


def lex(path: str, series: str) -> Doc:
    """Lex one lecture file into a :class:`Doc`."""
    with open(path, encoding="utf-8") as fh:
        raw_lines = fh.read().splitlines()

    stem = path.rsplit("/", 1)[-1][:-3]
    doc = Doc(path=path, stem=stem, series=series)

    stack: list = []          # open fences, outermost first
    open_blocks: list = []    # directive blocks still accumulating a body
    math_dir_buf: list = []   # body of the {math} directive being read
    gated_depth = 0           # inside a gated exercise/solution region
    in_dollar_math = False    # inside a $$ ... $$ block
    dollar_start = 0
    dollar_buf: list = []
    ams_env = None            # inside a bare \begin{align} ... at top level
    ams_start = 0
    ams_buf: list = []
    in_frontmatter = False
    in_html_comment = False   # <!-- ... --> content is not published
    cell_meta = None          # a ``{code-cell}``'s leading ``---`` YAML block

    for idx, raw in enumerate(raw_lines):
        no = idx + 1
        # Display math is sometimes wrapped in a blockquote (``> $$``). Strip the
        # quote marker before looking for delimiters, or the ``$$`` state machine
        # inverts and tags the rest of the lecture as the wrong region type.
        stripped = re.sub(r"^\s*(?:>\s*)+", "", raw).strip()

        # --- Jupytext YAML front matter -------------------------------------
        if no == 1 and stripped == "---":
            in_frontmatter = True
            doc.lines.append(Line(no, raw, "option"))
            continue
        if in_frontmatter:
            doc.lines.append(Line(no, raw, "option"))
            if stripped == "---":
                in_frontmatter = False
            continue

        top = stack[-1] if stack else None
        in_code_fence = bool(top and top.is_code)

        # --- HTML comments ----------------------------------------------------
        # Commented-out prose and maths never reach the published page, so no rule
        # should fire on it.
        if not in_code_fence:
            if in_html_comment:
                doc.lines.append(Line(no, raw, "raw", tuple(f.directive for f in stack)))
                if "-->" in raw:
                    in_html_comment = False
                continue
            if "<!--" in raw and "-->" not in raw[raw.index("<!--"):]:
                in_html_comment = True
                doc.lines.append(Line(no, raw, "raw", tuple(f.directive for f in stack)))
                continue
            # A line starting with ``%`` is a MyST comment and never reaches the page.
            # ``money_inflation`` has a commented-out draft derivation at 443-447 whose
            # LaTeX was being read as narrative, which was that lecture's whole Math
            # finding. ``%%`` is a notebook magic and is left alone — but only inside a
            # code fence, which this branch already excludes.
            if raw.lstrip().startswith("%") and not raw.lstrip().startswith("%%"):
                doc.lines.append(Line(no, raw, "raw", tuple(f.directive for f in stack)))
                continue

        # --- fence handling --------------------------------------------------
        m = FENCE_RE.match(raw)
        if m:
            indent, marker, directive, info = (
                len(m.group(1)), m.group(2), (m.group(3) or "").strip(), (m.group(4) or "").strip()
            )
            bare = not directive and not info
            # A closing fence: same marker char, at least as long, nothing after it.
            if top and bare and marker[0] == top.marker[0] and len(marker) >= len(top.marker):
                closed = stack.pop()
                if closed.directive and open_blocks:
                    blk = open_blocks.pop()
                    doc.blocks.append((blk[0], no, blk[1], blk[2], blk[3], blk[4]))
                if closed.directive and body_kind(closed.directive) == "math":
                    doc.math_blocks.append(
                        (closed.line_no, no, "math-directive", "\n".join(math_dir_buf)))
                    math_dir_buf = []
                doc.lines.append(Line(no, raw, "fence", tuple(f.directive for f in stack)))
                continue
            if not in_code_fence:
                name = directive.split()[0] if directive else ""
                # A directive argument may sit inside the braces
                # (``{solution-start} lbl`` puts it in the info string instead).
                arg = (directive[len(name):].strip() if directive else "") or info
                if top is not None and directive:
                    doc.nestings.append((no, marker, name, top.marker, top.directive))
                fence = Fence(marker, name, info, indent, no)
                opts, after = _parse_options(raw_lines, idx + 1)
                if directive:
                    doc.directives.append((no, name, arg, opts, marker))
                # A gated directive (``{exercise-start}``, ``{solution-end}``) is a
                # marker, not a container: its fence must close right after its
                # options. When it does not, treating it as a container would make
                # every later directive look nested. Record the fault and move on.
                if name.endswith(("-start", "-end")):
                    nxt = raw_lines[after] if after < len(raw_lines) else ""
                    if not re.match(r"^\s*(`{3,}|~{3,}|:{3,})\s*$", nxt):
                        doc.unclosed_gated.append((no, name, len(marker)))
                        if name.endswith("-start"):
                            gated_depth += 1
                        else:
                            gated_depth = max(0, gated_depth - 1)
                        doc.lines.append(Line(no, raw, "fence",
                                              tuple(f.directive for f in stack)))
                        continue
                    if name.endswith("-start"):
                        gated_depth += 1
                    else:
                        gated_depth = max(0, gated_depth - 1)
                if directive:
                    open_blocks.append([no, name, arg, opts, []])
                stack.append(fence)
                # A ``{code-cell}`` may open with a ``---`` YAML metadata block. Its body
                # is options, not Python: ``caption: … $f(\omega,t)$ …`` was being scanned
                # as code and counted as a spelled-out Greek variable.
                cell_meta = "pending" if body_kind(fence.directive) == "code" else None
                doc.lines.append(Line(no, raw, "fence", tuple(f.directive for f in stack)))
                continue

        if in_code_fence:
            if open_blocks:
                open_blocks[-1][4].append(raw)
            kind = body_kind(top.directive)
            if cell_meta == "pending":
                cell_meta = "in" if raw.strip() == "---" else None
            elif cell_meta == "in" and raw.strip() == "---":
                cell_meta = "closing"
            if cell_meta in ("in", "closing"):
                kind = "option"
                if cell_meta == "closing":
                    cell_meta = None
            if kind == "math":
                math_dir_buf.append(raw)
            doc.lines.append(
                Line(no, raw, kind, tuple(f.directive for f in stack),
                     in_exercise=_in_exercise(stack) or gated_depth > 0)
            )
            continue

        # --- display math ----------------------------------------------------
        if not in_dollar_math and ams_env is None:
            if stripped.startswith("$$"):
                body = stripped[2:]
                # A single-line $$ ... $$ equation.
                if body.endswith("$$") and len(stripped) > 4:
                    doc.math_blocks.append((no, no, "$$", body[:-2]))
                    doc.lines.append(Line(no, raw, "math", tuple(f.directive for f in stack),
                                          in_exercise=_in_exercise(stack) or gated_depth > 0))
                    continue
                in_dollar_math = True
                dollar_start = no
                dollar_buf = [body]
                doc.lines.append(Line(no, raw, "math", tuple(f.directive for f in stack),
                                      in_exercise=_in_exercise(stack) or gated_depth > 0))
                continue
            if AMS_BEGIN_RE.match(raw):
                ams_env = AMS_BEGIN_RE.match(raw).group(1)
                ams_start = no
                ams_buf = [raw]
                doc.lines.append(Line(no, raw, "math", tuple(f.directive for f in stack),
                                      in_exercise=_in_exercise(stack) or gated_depth > 0))
                continue
        elif in_dollar_math:
            doc.lines.append(Line(no, raw, "math", tuple(f.directive for f in stack),
                                  in_exercise=_in_exercise(stack) or gated_depth > 0))
            # A block may be closed by a bare ``$$`` line, by ``$$ (label)``, or by
            # ``$$`` appended to the end of the last content line.
            if stripped.startswith("$$") or stripped.endswith("$$"):
                if stripped.endswith("$$") and not stripped.startswith("$$"):
                    dollar_buf.append(raw[:raw.rindex("$$")])
                doc.math_blocks.append((dollar_start, no, "$$", "\n".join(dollar_buf)))
                in_dollar_math = False
                dollar_buf = []
            else:
                dollar_buf.append(raw)
            continue
        else:  # inside a bare amsmath environment
            doc.lines.append(Line(no, raw, "math", tuple(f.directive for f in stack),
                                  in_exercise=_in_exercise(stack) or gated_depth > 0))
            ams_buf.append(raw)
            if AMS_END_RE.match(raw) and AMS_END_RE.match(raw).group(1) == ams_env:
                doc.math_blocks.append((ams_start, no, ams_env, "\n".join(ams_buf)))
                ams_env = None
                ams_buf = []
            continue

        # --- directive option lines -----------------------------------------
        if re.match(r"^\s*:[A-Za-z0-9_-]+:", raw) and stack:
            doc.lines.append(Line(no, raw, "option", tuple(f.directive for f in stack),
                                  in_exercise=_in_exercise(stack) or gated_depth > 0))
            continue

        # --- narrative text ---------------------------------------------------
        is_table = "|" in raw and raw.strip().startswith("|")
        doc.lines.append(
            Line(no, raw, "text", tuple(f.directive for f in stack),
                 in_exercise=_in_exercise(stack) or gated_depth > 0, in_table=is_table)
        )

    _resolve_inline(doc)
    return doc


def _in_exercise(stack) -> bool:
    return any(f.directive in EXERCISE_DIRECTIVES for f in stack)


# Inline math may wrap across source lines (``$N(0,\n\sigma^2)$`` is common), so
# it has to be resolved over a joined narrative stream rather than line by line.
# A span may not contain a blank line and is length-limited, which keeps an odd
# stray ``$`` from swallowing half a lecture.
STREAM_MATH_RE = re.compile(r"(?<![\\$])\$(?!\$)((?:[^$\\\n]|\\.|\n(?!\s*\n)){1,400}?)\$(?!\$)")
# ``[^`\n]``, not ``[^`]``: the first alternative used to match newlines itself, so
# the ``\n(?!\s*\n)`` guard beside it was dead code and an unbalanced backtick could
# pair with one hundreds of lines away. One stray `` `shock' `` in five_preferences
# masked 381 of its 798 narrative lines, leaving 18 inline math spans out of hundreds.
STREAM_CODE_RE = re.compile(r"(`+)((?:[^`\n]|\n(?!\s*\n))*?)\1")


def _resolve_inline(doc: Doc) -> None:
    """Fill ``doc.inline_spans`` and ``doc.masked`` from the narrative stream."""
    text_lines = [l for l in doc.lines if l.kind == "text"]
    if not text_lines:
        return
    stream_parts, line_of, pos = [], [], 0
    for l in text_lines:
        stream_parts.append(l.raw)
        line_of.append((pos, pos + len(l.raw), l.no))
        pos += len(l.raw) + 1
    stream = "\n".join(stream_parts)

    def line_at(idx):
        for a, b, no in line_of:
            if a <= idx <= b:
                return no
        return line_of[-1][2]

    mask = list(stream)

    # Masked spans are filled with NUL, not spaces: blanking with spaces would
    # manufacture runs of whitespace and make ``qe-writing-008`` fire on them.
    def blank(start, end):
        for i in range(start, end):
            if mask[i] != "\n":
                mask[i] = "\x00"

    for m in STREAM_CODE_RE.finditer(stream):
        blank(m.start(), m.end())
    masked_code = "".join(mask)
    for m in STREAM_MATH_RE.finditer(masked_code):
        doc.inline_spans.append((line_at(m.start()), m.group(1)))
        blank(m.start(), m.end())

    masked_stream = "".join(mask)
    for chunk, (a, b, no) in zip(masked_stream.split("\n"), line_of):
        doc.masked[no] = chunk


def strip_inline(text: str) -> str:
    """Remove inline code spans and inline math so prose checks do not fire on them."""
    text = INLINE_CODE_RE.sub(" ", text)
    text = INLINE_MATH_RE.sub(" ", text)
    return text
