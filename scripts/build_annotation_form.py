#!/usr/bin/env python3
"""Render the blinded annotation packet as a single self-contained HTML form.

    python scripts/build_annotation_form.py --annotator annotator_1

The Markdown packet plus a separate CSV is awkward to work through: the
question is in one file and the answer box in another. This produces one
offline page per annotator with the question, its abstracts, and the
label choices side by side; it autosaves to the browser's localStorage
and exports exactly the CSV columns scripts/human_annotation.py expects.

Blinding is preserved: the page contains no system identity beyond the
anonymised code and no LLM label of any kind.
"""

import argparse
import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark.schemas import load_jsonl  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "annotation"
SAMPLE = ROOT / "results" / "judge_validation" / "sample.json"
CORPUS = ROOT / "data" / "corpus" / "future_corpus_large_frozen_window.jsonl"

OUTCOMES = [
    ("answered", "The literature substantially RESOLVED it — you could now state the answer"),
    ("partially_addressed", "Real directly-relevant progress, but the core question is still open"),
    ("posed_but_open", "Later work asks the SAME question too, without resolving it"),
    ("not_addressed", "No abstract engages it substantively (same topic does NOT count)"),
]
PREMISES = [
    ("supported", "Later evidence CONFIRMS the assumption the question rests on"),
    ("refuted", "Later evidence FALSIFIES that assumption"),
    ("weakened", "Later evidence seriously undermines it without falsifying it"),
    ("still_plausible", "The assumption was never directly tested"),
    ("not_applicable", "The question rests on no contestable assumption"),
]

CSS = """
:root { --bg:#fff; --fg:#1a1a1a; --muted:#666; --line:#e3e3e3; --accent:#1f6feb;
        --card:#fafafa; --done:#e8f5e9; }
@media (prefers-color-scheme: dark) { :root {
  --bg:#15171a; --fg:#e8e8e8; --muted:#9aa0a6; --line:#2c2f34; --accent:#5c9bff;
  --card:#1c1f24; --done:#1e2b20; } }
* { box-sizing:border-box; }
body { margin:0; background:var(--bg); color:var(--fg); font:16px/1.6 -apple-system,
       BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"PingFang SC",
       "Microsoft YaHei",sans-serif; }
header { position:sticky; top:0; z-index:10; background:var(--bg);
         border-bottom:1px solid var(--line); padding:12px 20px;
         display:flex; gap:16px; align-items:center; flex-wrap:wrap; }
header h1 { font-size:16px; margin:0; font-weight:600; }
.bar { flex:1; min-width:160px; height:8px; background:var(--line); border-radius:4px; }
.bar > div { height:100%; width:0; background:var(--accent); border-radius:4px;
             transition:width .2s; }
button { font:inherit; padding:7px 14px; border-radius:7px; border:1px solid var(--line);
         background:var(--card); color:var(--fg); cursor:pointer; }
button.primary { background:var(--accent); color:#fff; border-color:transparent; }
main { max-width:900px; margin:0 auto; padding:20px; }
.item { border:1px solid var(--line); border-radius:12px; padding:18px 20px;
        margin:0 0 26px; background:var(--card); }
.item.done { background:var(--done); }
.qid { font:12px ui-monospace,SFMono-Regular,Menlo,monospace; color:var(--muted); }
.q { font-size:18px; font-weight:600; margin:6px 0 16px; }
details { border-top:1px solid var(--line); padding-top:10px; margin-top:6px; }
summary { cursor:pointer; color:var(--accent); font-size:14px; }
.abs { border-left:3px solid var(--line); padding:2px 0 2px 12px; margin:14px 0; }
.abs h4 { margin:0 0 4px; font-size:15px; }
.abs .meta { color:var(--muted); font-size:12px; margin-bottom:6px; }
.abs p { margin:0; font-size:14px; color:var(--fg); }
fieldset { border:none; padding:0; margin:16px 0 0; }
legend { font-size:13px; font-weight:600; color:var(--muted); text-transform:uppercase;
         letter-spacing:.04em; margin-bottom:6px; }
label.opt { display:block; padding:7px 10px; border-radius:7px; cursor:pointer; }
label.opt:hover { background:var(--bg); }
label.opt code { font-weight:600; }
label.opt span { color:var(--muted); font-size:13px; }
.row { display:flex; gap:20px; flex-wrap:wrap; align-items:flex-end; margin-top:14px; }
input[type=text] { width:100%; padding:8px 10px; border:1px solid var(--line);
                   border-radius:7px; background:var(--bg); color:var(--fg); font:inherit; }
.notes { flex:1; min-width:260px; }
.hint { color:var(--muted); font-size:13px; }
"""

JS = """
const KEY = 'sqb_annotation_' + ANNOTATOR;
const state = JSON.parse(localStorage.getItem(KEY) || '{}');

function render(id) {
  const card = document.getElementById(id);
  const s = state[id] || {};
  card.classList.toggle('done', !!(s.outcome && s.premise_status));
}
function save() {
  localStorage.setItem(KEY, JSON.stringify(state));
  const done = ITEMS.filter(i => state[i] && state[i].outcome && state[i].premise_status).length;
  document.getElementById('count').textContent = done + ' / ' + ITEMS.length;
  document.querySelector('.bar > div').style.width = (100 * done / ITEMS.length) + '%';
}
document.addEventListener('change', e => {
  const el = e.target;
  if (!el.name) return;
  const [id, field] = el.name.split('::');
  if (!ITEMS.includes(id)) return;
  state[id] = state[id] || {};
  state[id][field] = el.value;
  render(id); save();
});
document.addEventListener('input', e => {
  const el = e.target;
  if (!el.name || !el.name.endsWith('::notes')) return;
  const id = el.name.split('::')[0];
  state[id] = state[id] || {}; state[id].notes = el.value; save();
});
function restore() {
  for (const id of ITEMS) {
    const s = state[id]; if (!s) continue;
    for (const f of ['outcome', 'premise_status', 'confidence']) {
      if (!s[f]) continue;
      const el = document.querySelector(`input[name="${id}::${f}"][value="${s[f]}"]`);
      if (el) el.checked = true;
    }
    const n = document.querySelector(`input[name="${id}::notes"]`);
    if (n && s.notes) n.value = s.notes;
    render(id);
  }
  save();
}
function toCSV() {
  const esc = v => `"${String(v == null ? '' : v).replace(/"/g, '""')}"`;
  const rows = [['item_id', 'outcome', 'premise_status', 'confidence', 'notes']];
  for (const id of ITEMS) {
    const s = state[id] || {};
    rows.push([id, s.outcome || '', s.premise_status || '', s.confidence || '', s.notes || '']);
  }
  return rows.map(r => r.map(esc).join(',')).join('\\n');
}
function download() {
  const blob = new Blob([toCSV()], {type: 'text/csv;charset=utf-8'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = ANNOTATOR + '_sheet.csv';
  a.click();
}
document.getElementById('export').addEventListener('click', download);
document.getElementById('jump').addEventListener('click', () => {
  const next = ITEMS.find(i => !(state[i] && state[i].outcome && state[i].premise_status));
  if (next) document.getElementById(next).scrollIntoView({behavior: 'smooth', block: 'start'});
});
restore();
"""


def build(annotator: str) -> Path:
    sample = json.loads(SAMPLE.read_text(encoding="utf-8"))
    decode = json.loads((PACK / "decode.json").read_text(encoding="utf-8"))
    papers = {p["paper_id"]: p for p in load_jsonl(CORPUS)}

    questions: dict[tuple[str, str], str] = {}
    retrieval: dict[tuple[str, str], list] = {}
    for name, spec in sample.items():
        for q in load_jsonl(ROOT / spec["questions_file"]):
            questions[(name, q["question_id"])] = q["question"]
        for r in load_jsonl(ROOT / spec["retrieval_file"]):
            retrieval[(name, r["question_id"])] = r["documents"]

    parts, item_ids = [], []
    for item_id in sorted(decode):
        meta = decode[item_id]
        key = (meta["system"], meta["question_id"])
        item_ids.append(item_id)
        docs = [papers[d["bibcode"]] for d in retrieval.get(key, [])
                if d["bibcode"] in papers]
        abstracts = []
        for i, d in enumerate(docs, start=1):
            abstract = " ".join((d.get("abstract") or "").split())
            abstracts.append(
                f'<div class="abs"><h4>[{i}] {html.escape(d.get("title") or "")}</h4>'
                f'<div class="meta">{html.escape(d.get("pubdate") or "")}</div>'
                f'<p>{html.escape(abstract)}</p></div>')
        outcome_opts = "".join(
            f'<label class="opt"><input type="radio" name="{item_id}::outcome" '
            f'value="{code}"> <code>{code}</code> — <span>{html.escape(desc)}</span></label>'
            for code, desc in OUTCOMES)
        premise_opts = "".join(
            f'<label class="opt"><input type="radio" name="{item_id}::premise_status" '
            f'value="{code}"> <code>{code}</code> — <span>{html.escape(desc)}</span></label>'
            for code, desc in PREMISES)
        conf_opts = "".join(
            f'<label class="opt" style="display:inline-block"><input type="radio" '
            f'name="{item_id}::confidence" value="{v}"> {v}</label>' for v in (1, 2, 3))
        parts.append(f"""
<section class="item" id="{item_id}">
  <div class="qid">{item_id} &middot; {meta['system_code']}</div>
  <div class="q">{html.escape(questions.get(key, ''))}</div>
  <details open><summary>{len(docs)} candidate abstracts published after the cutoff</summary>
    {''.join(abstracts)}
  </details>
  <fieldset><legend>outcome — what happened to the question?</legend>{outcome_opts}</fieldset>
  <fieldset><legend>premise_status — what happened to its underlying assumption?</legend>{premise_opts}</fieldset>
  <div class="row">
    <div><div class="hint">confidence</div>{conf_opts}</div>
    <div class="notes"><div class="hint">notes (optional, especially where you hesitated)</div>
      <input type="text" name="{item_id}::notes" placeholder="…"></div>
  </div>
</section>""")

    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Annotation — {annotator}</title><style>{CSS}</style></head>
<body>
<header>
  <h1>Blinded annotation — {annotator}</h1>
  <span id="count" class="hint">0 / {len(item_ids)}</span>
  <div class="bar"><div></div></div>
  <button id="jump">Next unanswered</button>
  <button id="export" class="primary">Export CSV</button>
</header>
<main>
  <p class="hint">Judge only from the abstracts shown. Same topic is
  <strong>not</strong> engagement — the abstract must bear on the question's actual
  test or its assumption. Answers autosave in this browser; press
  <em>Export CSV</em> when done and put the file in <code>annotation/</code>.
  Full definitions and worked examples: <code>codebook.md</code>.</p>
  {''.join(parts)}
</main>
<script>const ANNOTATOR = {json.dumps(annotator)};
const ITEMS = {json.dumps(item_ids)};
{JS}</script></body></html>"""

    out = PACK / f"{annotator}_form.html"
    out.write_text(page, encoding="utf-8")
    print(f"OK: {len(item_ids)} items -> {out} ({out.stat().st_size // 1024} KB)")
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--annotator", default="annotator_1")
    args = parser.parse_args()
    build(args.annotator)


if __name__ == "__main__":
    main()
