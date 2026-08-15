#!/usr/bin/env python3
"""Render annotation/BRIEF.md as a standalone, printable HTML page.

    python scripts/build_brief.py

The brief is what an annotator reads before opening the form, so it has to
survive being emailed: one self-contained file, readable on a phone,
printable to PDF, no external assets. Markdown is converted with a small
purpose-built renderer rather than a dependency, since the brief uses only
headings, tables, lists, blockquotes, rules and inline emphasis.
"""

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "annotation" / "BRIEF.md"
OUT = ROOT / "annotation" / "BRIEF.html"

CSS = """
:root { --bg:#fff; --fg:#1a1a1a; --muted:#5b5b5b; --line:#e2e2e2; --accent:#1f6feb;
        --card:#f7f8fa; --warn:#b26a00; }
@media (prefers-color-scheme: dark) { :root {
  --bg:#15171a; --fg:#e9e9e9; --muted:#a0a6ac; --line:#2c3036; --accent:#6aa5ff;
  --card:#1c1f24; --warn:#e0a800; } }
* { box-sizing:border-box; }
body { margin:0 auto; max-width:780px; padding:36px 24px 80px; background:var(--bg);
       color:var(--fg); font:16.5px/1.7 -apple-system,BlinkMacSystemFont,"Segoe UI",
       Roboto,"Helvetica Neue",Arial,"PingFang SC","Microsoft YaHei",sans-serif; }
h1 { font-size:25px; line-height:1.35; margin:0 0 4px; }
h1 + h1 { color:var(--muted); font-weight:600; margin-bottom:26px; }
h2 { font-size:19px; margin:38px 0 6px; padding-top:14px; border-top:1px solid var(--line); }
h2 + h2 { border-top:none; padding-top:0; color:var(--muted); font-size:17px;
          font-weight:600; margin-top:0; margin-bottom:14px; }
h3 { font-size:17px; margin:22px 0 6px; }
p { margin:10px 0; }
strong { font-weight:650; }
em { color:var(--muted); }
code { background:var(--card); padding:1.5px 6px; border-radius:5px;
       font:14px ui-monospace,SFMono-Regular,Menlo,monospace; }
blockquote { margin:16px 0; padding:12px 18px; border-left:4px solid var(--accent);
             background:var(--card); border-radius:0 8px 8px 0; }
blockquote h3 { margin:4px 0; color:var(--warn); }
table { border-collapse:collapse; width:100%; margin:14px 0; font-size:15.5px; }
th,td { border:1px solid var(--line); padding:8px 11px; text-align:left; vertical-align:top; }
th { background:var(--card); font-weight:650; }
hr { border:none; border-top:1px solid var(--line); margin:34px 0; }
ol,ul { margin:10px 0; padding-left:26px; }
li { margin:7px 0; }
a { color:var(--accent); }
@media print {
  body { max-width:none; padding:0; font-size:11pt; color:#000; background:#fff; }
  h2 { page-break-after:avoid; } table,blockquote { page-break-inside:avoid; }
}
"""


def inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = text.replace("⇒", "&rArr;").replace("→", "&rarr;")
    return text


def render(md: str) -> str:
    out: list[str] = []
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()

        if not line.strip():
            i += 1
            continue

        if line.startswith("---") and set(line.strip()) == {"-"}:
            out.append("<hr>")
            i += 1
            continue

        m = re.match(r"^(#{1,3})\s+(.*)", line)
        if m:
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            i += 1
            continue

        if line.lstrip().startswith("|"):           # table
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows]
            body = [r for r in cells if not all(set(c) <= set("-: ") for c in r)]
            if body:
                out.append("<table><thead><tr>"
                           + "".join(f"<th>{inline(c)}</th>" for c in body[0])
                           + "</tr></thead><tbody>")
                for row in body[1:]:
                    out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row)
                               + "</tr>")
                out.append("</tbody></table>")
            continue

        if line.startswith(">"):                    # blockquote
            block = []
            while i < len(lines) and lines[i].startswith(">"):
                block.append(lines[i].lstrip("> ").rstrip())
                i += 1
            out.append("<blockquote>")
            for b in block:
                if not b:
                    continue
                h = re.match(r"^(#{1,3})\s+(.*)", b)
                out.append(f"<h3>{inline(h.group(2))}</h3>" if h
                           else f"<p>{inline(b)}</p>")
            out.append("</blockquote>")
            continue

        m = re.match(r"^(\d+)\.\s+(.*)", line)       # ordered list
        if m:
            items, start = [], m.group(1)
            while i < len(lines) and re.match(r"^\d+\.\s+", lines[i]):
                text = re.sub(r"^\d+\.\s+", "", lines[i]).rstrip()
                i += 1
                while i < len(lines) and lines[i].startswith("   ") and lines[i].strip():
                    text += " " + lines[i].strip()
                    i += 1
                items.append(text)
            out.append(f'<ol start="{start}">'
                       + "".join(f"<li>{inline(t)}</li>" for t in items) + "</ol>")
            continue

        paragraph = [line]                           # paragraph
        i += 1
        while (i < len(lines) and lines[i].strip()
               and not re.match(r"^(#{1,3}\s|\||>|\d+\.\s|---)", lines[i])):
            paragraph.append(lines[i].rstrip())
            i += 1
        out.append(f"<p>{inline(' '.join(paragraph))}</p>")

    return "\n".join(out)


def main() -> None:
    if not SRC.exists():
        sys.exit(f"missing {SRC}")
    body = render(SRC.read_text(encoding="utf-8"))
    page = (f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">\n'
            f'<title>Annotation brief 标注说明书</title>\n<style>{CSS}</style>\n'
            f'</head>\n<body>\n{body}\n</body></html>\n')
    OUT.write_text(page, encoding="utf-8")
    print(f"OK -> {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
