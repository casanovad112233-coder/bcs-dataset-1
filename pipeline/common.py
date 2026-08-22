"""Shared helpers: text cleaning, filename normalization, mojibake detection."""
import re
from pathlib import Path

from bs4 import NavigableString, Tag

MOJIBAKE_MARKERS = ["à¦", "à§", "â€", "Â", "\ufffd"]

SUP_SRC = "0123456789০১২৩৪৫৬৭৮৯+-=()"
SUB_SRC = "0123456789০১২৩৪৫৬৭৮৯+-=()"
SUP_MAP = dict(zip("0123456789০১২৩৪৫৬৭৮৯+-=()", "⁰¹²³⁴⁵⁶⁷⁸⁹⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"))
SUB_MAP = dict(zip("0123456789০১২৩৪৫৬৭৮৯+-=()", "₀₁₂₃₄₅₆₇₈₉₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"))
MJX_OPERATORS = set("+-=<>≠≤≥×÷()")

LATEX_SYMBOLS = {
    "times": "×", "cdot": "·", "cdotp": "·", "div": "÷",
    "le": "≤", "leq": "≤", "leqslant": "≤", "ge": "≥", "geq": "≥", "geqslant": "≥",
    "ne": "≠", "neq": "≠", "pm": "±", "mp": "∓",
    "infty": "∞", "therefore": "∴", "because": "∵",
    "circ": "°", "degree": "°",
    "ldots": "…", "cdots": "…", "dots": "…",
    "to": "→", "implies": "⇒", "impliedby": "⇐", "iff": "⇔",
    "in": "∈", "notin": "∉", "subset": "⊂", "supset": "⊃",
    "subseteq": "⊆", "supseteq": "⊇", "cup": "∪", "cap": "∩",
    "approx": "≈", "sim": "~", "propto": "∝", "perp": "⊥",
    "partial": "∂", "nabla": "∇", "forall": "∀", "exists": "∃",
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ",
    "theta": "θ", "lambda": "λ", "mu": "μ", "pi": "π", "sigma": "σ",
    "phi": "φ", "omega": "ω", "Delta": "Δ", "Pi": "Π", "Sigma": "Σ", "Omega": "Ω",
    "vert": "|", "lvert": "|", "rvert": "|",
}
UNWRAP_CMDS = {"mathrm", "text", "textbf", "textit", "mbox", "textnormal",
               "operatorname", "emph", "underline", "uline", "bm", "boldsymbol",
               "rm", "it", "bf", "sf", "tt", "sc", "overline", "overbrace",
               "underbrace", "small", "large", "normal", "cmidrule", "textrm"}
DROP_CMDS = {"displaystyle", "textstyle", "scriptstyle", "huge", "Huge",
             "normalsize", "footnotesize", "scriptsize", "tiny", "nolimits",
             "limits", "phantom", "hspace", "vspace", "qquad", "quad"}
FUNC_CMDS = {"log", "ln", "lg", "sin", "cos", "tan", "cot", "sec", "cosec",
             "lim", "max", "min", "mod", "gcd", "arg", "deg", "Pr", "det"}


def _math_sup(text: str) -> str:
    text = text.strip()
    if text and all(c in SUP_SRC for c in text):
        return "".join(SUP_MAP.get(c, c) for c in text)
    if text and re.fullmatch(r"[A-Za-z0-9]+", text):
        return f"^{text}"
    return f"^({text})" if text else ""


def _math_sub(text: str) -> str:
    text = text.strip()
    if text and all(c in SUB_SRC for c in text):
        return "".join(SUB_MAP.get(c, c) for c in text)
    if text and re.fullmatch(r"[A-Za-z0-9]+", text):
        return f"_{text}"
    return f"_({text})" if text else ""


def _math_frac(num: str, den: str) -> str:
    def wrap(s: str) -> str:
        s = s.strip()
        if not s:
            return ""
        if any(c in MJX_OPERATORS for c in s) or " " in s:
            return f"({s})"
        return s
    return f"{wrap(num)}/{wrap(den)}"


def _render_svg(el: Tag) -> str:
    return "".join(t.get_text("", strip=True) for t in el.find_all("text"))


def _svg_is_duplicate(svg: Tag) -> bool:
    p = svg.parent
    while p is not None and isinstance(p, Tag):
        if "MathJax_Preview" in (p.get("class") or []):
            return True
        if any(isinstance(c, Tag) and "MathJax_Preview" in (c.get("class") or []) for c in p.children):
            return True
        p = p.parent
    return False


def _render_node(node) -> str:
    if isinstance(node, NavigableString):
        return str(node).replace("\xa0", " ")
    if not isinstance(node, Tag):
        return ""
    cls = node.get("class") or []

    if "MJXp-mfrac" in cls:
        num = node.find("span", class_="MJXp-script")
        denom = node.find("span", class_="MJXp-denom")
        n = _render_node(num) if num is not None else ""
        d = _render_node(denom) if denom is not None else ""
        return _math_frac(n, d)

    if "MJXp-msubsup" in cls or "MJXp-msup" in cls or "MJXp-msub" in cls:
        kids = [c for c in node.children if isinstance(c, Tag)]
        base = _render_node(kids[0]) if kids else ""
        script = _render_node(kids[1]) if len(kids) > 1 else ""
        style = (kids[1].get("style") or "") if len(kids) > 1 else ""
        if "MJXp-msubsup" in cls and "-0.4em" in style:
            return base + _math_sub(script)
        if "MJXp-msubsup" in cls and "0.5em" in style:
            return base + _math_sup(script)
        if "MJXp-msup" in cls:
            return base + _math_sup(script)
        if "MJXp-msub" in cls:
            return base + _math_sub(script)
        return base + script

    out: list[str] = []
    for child in node.children:
        if isinstance(child, NavigableString):
            out.append(str(child).replace("\xa0", " "))
        elif isinstance(child, Tag):
            if child.name == "br":
                out.append(" ")
            elif child.name == "img":
                continue
            elif child.name == "svg":
                if not _svg_is_duplicate(child):
                    out.append(_render_svg(child))
            else:
                ccls = child.get("class") or []
                has_frac = "MJXp-mfrac" in ccls or child.find("span", class_="MJXp-mfrac") is not None
                if has_frac:
                    cur = "".join(out)
                    if cur and cur[-1].isdigit():
                        out.append(" ")
                out.append(_render_node(child))
    return "".join(out)


def clean_html_to_text(el: Tag) -> str:
    text = _render_node(el)
    text = latex_to_text(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _read_group(s: str, i: int) -> tuple[str, int]:
    """s[i] must be '{'. Return (content, next_index)."""
    depth = 0
    start = i + 1
    while i < len(s):
        c = s[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return s[start:i], i + 1
        i += 1
    return s[start:i], i


def _split_over(content: str) -> list[str]:
    parts, depth, i, n = [], 0, 0, len(content)
    seg = 0
    while i < n:
        c = content[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        elif depth == 0 and content[i:i + 5] == "\\over":
            parts.append(content[seg:i])
            i += 5
            seg = i
            continue
        i += 1
    parts.append(content[seg:])
    return parts


def _read_script(s: str, i: int) -> tuple[str, int]:
    """i points at '^' or '_'. Return (arg, next_index)."""
    j = i + 1
    while j < len(s) and s[j] in " \t\n":
        j += 1
    if j < len(s) and s[j] == "{":
        return _read_group(s, j)
    if j < len(s) and s[j] == "\\":
        m = re.match(r"\\[a-zA-Z]+", s[j:])
        if m:
            return m.group(0), j + len(m.group(0))
    return (s[j], j + 1) if j < len(s) else ("", j)


def _convert_group(content: str) -> str:
    parts = _split_over(content)
    if len(parts) == 2:
        return _math_frac(latex_to_text(parts[0]), latex_to_text(parts[1]))
    return latex_to_text(content)


def latex_to_text(s: str) -> str:
    """Convert raw LaTeX (\\frac, \\over, \\sqrt, ^, _, \\mathrm, ...) to readable text."""
    if not s:
        return s
    s = s.replace("\u2061", "").replace("\u200b", "")
    parts = _split_over(s)
    if len(parts) == 2:
        return _math_frac(latex_to_text(parts[0]), latex_to_text(parts[1]))
    out: list[str] = []
    i, n = 0, len(s)
    while i < n:
        c = s[i]
        if c == "\\":
            i += 1
            if i >= n:
                break
            if s[i] == "\\":
                out.append(" ")
                i += 1
                continue
            m = re.match(r"[a-zA-Z]+", s[i:])
            if not m:
                ch = s[i]
                if ch in "()[]":
                    i += 1
                    continue
                if ch == " ":
                    out.append(" ")
                    i += 1
                    continue
                out.append(ch)
                i += 1
                continue
            name = m.group(0)
            i += len(name)
            j = i
            while j < n and s[j] in " \t\n":
                j += 1
            has_group = j < n and s[j] == "{"
            i = j
            if name in ("frac", "dfrac", "tfrac", "cfrac"):
                if has_group:
                    a, i = _read_group(s, i)
                else:
                    a, i = (s[j], j + 1) if j < n else ("", j)
                j2 = i
                while j2 < n and s[j2] in " \t\n":
                    j2 += 1
                if j2 < n and s[j2] == "{":
                    b, i = _read_group(s, i)
                else:
                    b, i = (s[j2], j2 + 1) if j2 < n else ("", j2)
                out.append(_math_frac(latex_to_text(a), latex_to_text(b)))
            elif name == "sqrt":
                if has_group:
                    a, i = _read_group(s, i)
                    inner = _convert_group(a)
                else:
                    a, i = (s[j], j + 1) if j < n else ("", j)
                    inner = latex_to_text(a)
                if inner and (any(o in inner for o in "=+-×÷/") or " " in inner or "(" in inner):
                    out.append(f"√({inner})")
                else:
                    out.append("√" + inner)
            elif name in UNWRAP_CMDS:
                if has_group:
                    a, i = _read_group(s, i)
                    out.append(_convert_group(a))
                else:
                    tok, i = (s[j], j + 1) if j < n else ("", j)
                    out.append(latex_to_text(tok))
            elif name in ("big", "Big", "bigg", "Bigg", "left", "right", "middle"):
                if j < n and s[j] in "()[]{}|.":
                    if s[j] != ".":
                        out.append(s[j])
                    i = j + 1
            elif name in LATEX_SYMBOLS:
                out.append(LATEX_SYMBOLS[name])
                if has_group:
                    _, i = _read_group(s, i)
            elif name in DROP_CMDS:
                pass
            elif name in FUNC_CMDS:
                out.append(name)
            else:
                if has_group:
                    a, i = _read_group(s, i)
                    out.append(_convert_group(a))
        elif c == "{":
            content, i = _read_group(s, i)
            out.append(_convert_group(content))
        elif c == "}":
            i += 1
        elif c in "^_":
            j = i + 1
            while j < n and s[j] in " \t\n":
                j += 1
            nxt = s[j] if j < n else ""
            if nxt == "{" or nxt.isdigit() or nxt in "+-":
                arg, i = _read_script(s, i)
                conv = latex_to_text(arg)
                if c == "^":
                    out.append("°" if conv == "°" else _math_sup(conv))
                else:
                    out.append(_math_sub(conv))
            else:
                out.append(c)
                i += 1
        else:
            out.append(c)
            i += 1
    return "".join(out)


def norm_stem(path: Path) -> str:
    return re.sub(r"\s+", "_", path.stem).lower().strip("_")


def mojibake_markers(text: str) -> list[str]:
    return [m for m in MOJIBAKE_MARKERS if m in text]


def all_text_fields(q: dict) -> str:
    return " ".join(
        [q.get("question", ""), q.get("option_a", ""), q.get("option_b", ""),
         q.get("option_c", ""), q.get("option_d", ""), q.get("solve_note", "")]
    )
