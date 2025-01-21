"""Highlighting for code snippets."""

import re
import typing


def _highlight(txt: str, comment_start: str, keywords: typing.List[str]) -> str:
    """General highlight function."""
    out = []
    for line in txt.split("\n"):
        comment = ""
        if comment_start in line:
            lsp = line.split(comment_start, 1)
            line = lsp[0]
            comment = f"<span style='color:#FF8800'>{comment_start}{lsp[1]}</span>"

        lsp = line.split('"')
        line = lsp[0]

        for i, j in enumerate(lsp[1:]):
            if i % 2 == 0:
                line += f"<span style='color:#DD2299'>\"{j}"
            else:
                line += f'"</span>{j}'

        for keyword in keywords:
            line = re.sub(
                rf"(&nbsp;|^)({keyword})(&nbsp;|$)",
                r"\1<span style='color:#FF8800'>\2</span>\3",
                line,
            )
        out.append(line + comment)

    return "<br />".join(out)


def python_highlight(txt: str) -> str:
    """Apply syntax highlighting to Python snippet.

    Args:
        txt: Python snippet

    Returns:
        Snippet with syntax highlighting
    """
    return _highlight(
        txt,
        "#",
        [
            "for",
            "while",
            "from",
            "import",
            "return",
            "if",
            "elif",
            "else",
            "def",
            "in",
            "global",
            "assert",
        ],
    )


def rust_highlight(txt: str) -> str:
    """Apply syntax highlighting to Rust snippet.

    Args:
        txt: Python snippet

    Returns:
        Snippet with syntax highlighting
    """
    return _highlight(
        txt,
        "//",
        [
            "use",
            "while",
            "for",
            "return",
            "if",
            "else",
            "function",
            "let",
        ],
    )


def bash_highlight(txt: str) -> str:
    """Apply syntax highlighting to Bash snippet.

    Args:
        txt: Bash snippet

    Returns:
        Snippet with syntax highlighting
    """
    txt = re.sub(
        r"(python3?(?:&nbsp;-m&nbsp;.+?)?&nbsp;)", r"<span style='color:#FF8800'>\1</span>", txt
    )
    for keyword in ["wget", "mkdir", "tar", "cd", "cmake", "make", "ls", "cargo"]:
        txt = re.sub(
            rf"(&nbsp;|^)({keyword})(&nbsp;|$)",
            r"\1<span style='color:#FF8800'>\2</span>\3",
            txt,
        )
    return "<br />".join(txt.split("\n"))


def code_highlight(txt: str, lang: typing.Optional[str] = None):
    for a, b in [
        (" ", "&nbsp;"),
        ("<", "&lt;"),
        (">", "&gt;"),
    ]:
        txt = txt.replace(a, b)
    if lang == "python":
        return python_highlight(txt)
    if lang == "rust":
        return rust_highlight(txt)
    if lang == "bash":
        return bash_highlight(txt)
    return txt
