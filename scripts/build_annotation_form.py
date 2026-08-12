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
import hashlib
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
TRANSLATIONS = PACK / "translations.json"


def _sid(text: str) -> str:
    """Same stable id scheme as scripts/translate_packet.py."""
    return "q_" + hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]

# (code, English gloss, Chinese gloss)
OUTCOMES = [
    ("answered",
     "The literature substantially RESOLVED it — you could now state the answer",
     "已解决 —— 后续文献实质性地解决了它，你现在能根据这些摘要说出答案"),
    ("partially_addressed",
     "Real directly-relevant progress, but the core question is still open",
     "部分推进 —— 有直接相关的实质进展，但核心问题仍未解决"),
    ("posed_but_open",
     "Later work asks the SAME question too, without resolving it",
     "被提出但未解决 —— 后续文献也独立提出了同一个问题，但没有解决"),
    ("not_addressed",
     "No abstract engages it substantively (same topic does NOT count)",
     "未被触及 —— 没有摘要实质性涉及这个问题（同话题不算）"),
]
PREMISES = [
    ("supported",
     "Later evidence CONFIRMS the assumption the question rests on",
     "假设被证实 —— 后续证据支持这个问题所依赖的假设"),
    ("refuted",
     "Later evidence FALSIFIES that assumption",
     "假设被推翻 —— 后续证据证伪了该假设"),
    ("weakened",
     "Later evidence seriously undermines it without falsifying it",
     "假设被动摇 —— 后续证据严重削弱它，但未彻底证伪"),
    ("still_plausible",
     "The assumption was never directly tested",
     "假设未受检验 —— 该假设没有被直接检验过"),
    ("not_applicable",
     "The question rests on no contestable assumption",
     "不适用 —— 这个问题不依赖任何可争议的假设"),
]

GUIDE = """
<details class="guide"><summary>标注手册 / Codebook — 点开看判断标准和例子</summary>
<div class="guidebody">
<p><strong>你看到的是：</strong>一个写于 <strong>2021 年之前</strong>的科研问题，加上最多 8 篇
<strong>之后</strong>发表的论文摘要。<strong>只根据这些摘要判断</strong>——不要上网查，
因为 AI 裁判当时看到的就是这几篇，你多用外部知识对比就不公平了。</p>
<p><em>You see a question written before 2021 and up to 8 abstracts published after it.
Judge only from these abstracts — do not look anything up.</em></p>

<p class="warn">⚠️ <strong>最容易犯的错：把「同话题」当成「有人研究了这个问题」。</strong><br>
摘要讲的是同一颗行星、同一个分子，<strong>不算</strong>。必须真的碰到<strong>这个问题要检验的东西</strong>，
或者碰到<strong>它依赖的那个假设</strong>。<br>
<em>The single most common error is confusing topic overlap with engagement.</em></p>

<h4>例子 / Worked examples</h4>
<p><strong>问题：</strong>「HD 209458 b 大气里检索出的极低含水量，是真实的大气性质，还是检索方法造成的假象？」<br>
<strong>摘要：</strong>三篇独立重新分析，都得出含水量接近太阳组成。<br>
→ <code>answered</code> + <code>refuted</code>（问题解决了，而且是靠推翻它质疑的那个假设解决的）</p>

<p><strong>同一个问题，但摘要：</strong>几篇测量<em>别的</em>热木星含水量的论文。<br>
→ <code>not_addressed</code>（同话题、不同天体，跟这个检验无关）</p>

<p><strong>问题：</strong>「不均匀的晨昏线会怎样系统性地影响检索出的丰度？」<br>
<strong>摘要：</strong>几篇证明这种偏差普遍存在，但没有解决问题里问的那个具体情形。<br>
→ <code>partially_addressed</code> + <code>still_plausible</code></p>

<h4>两个标签是独立的 / The two labels are independent</h4>
<p>一个问题可以<strong>正因为</strong>它的假设被推翻而得到解决——
<code>answered</code> + <code>refuted</code> 是合理组合，不是矛盾。</p>

<h4>信心度 / Confidence</h4>
<p>1 = 没把握，2 = 一般，3 = 很有把握。该给 1 就给 1，低信心的条目会单独分析，
它们是有用的信息，不是失败。犹豫的地方请在 notes 里写一句你在纠结什么。</p>
</div></details>
"""

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
label.opt .zh { display:block; margin-left:24px; font-size:14px; color:var(--fg); }
label.opt .en { display:block; margin-left:24px; color:var(--muted); font-size:12.5px; }
.guide { border:1px solid var(--line); border-radius:12px; padding:14px 18px;
         margin:0 0 26px; background:var(--card); }
.guide > summary { font-size:15px; font-weight:600; color:var(--fg); }
.guidebody { padding-top:10px; font-size:14.5px; }
.guidebody h4 { margin:18px 0 6px; font-size:14px; }
.guidebody code { background:var(--bg); padding:1px 5px; border-radius:4px; font-size:13px; }
.warn { border-left:3px solid #e0a800; padding:8px 0 8px 12px; background:var(--bg);
        border-radius:0 6px 6px 0; }
.qzh { font-size:16px; font-weight:600; color:var(--accent); margin:-10px 0 16px; }
.zhtext { margin-top:8px; padding-top:8px; border-top:1px dashed var(--line); }
.zhtext h4 { margin:0 0 4px; font-size:14px; color:var(--muted); font-weight:600; }
.zhtext p { font-size:14px; }
body.hide-zh .qzh, body.hide-zh .zhtext { display:none; }
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
document.getElementById('togglezh').addEventListener('click', e => {
  const hidden = document.body.classList.toggle('hide-zh');
  e.target.textContent = hidden ? '显示中文 Show Chinese' : '隐藏中文 Hide Chinese';
  localStorage.setItem(KEY + '_hidezh', hidden ? '1' : '');
});
if (localStorage.getItem(KEY + '_hidezh')) {
  document.body.classList.add('hide-zh');
  document.getElementById('togglezh').textContent = '显示中文 Show Chinese';
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

    zh = (json.loads(TRANSLATIONS.read_text(encoding="utf-8"))
          if TRANSLATIONS.exists() else {})
    if not zh:
        print("  note: annotation/translations.json missing — building "
              "English-only. Run scripts/translate_packet.py first.")

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
            bib = d["paper_id"]
            zh_title = zh.get(f"t:{bib}", "")
            zh_abs = zh.get(f"a:{bib}", "")
            zh_block = ""
            if zh_title or zh_abs:
                zh_block = (f'<div class="zhtext"><h4>[{i}] {html.escape(zh_title)}</h4>'
                            f'<p>{html.escape(zh_abs)}</p></div>')
            abstracts.append(
                f'<div class="abs"><h4>[{i}] {html.escape(d.get("title") or "")}</h4>'
                f'<div class="meta">{html.escape(d.get("pubdate") or "")}</div>'
                f'<p>{html.escape(abstract)}</p>{zh_block}</div>')
        outcome_opts = "".join(
            f'<label class="opt"><input type="radio" name="{item_id}::outcome" '
            f'value="{code}"> <code>{code}</code>'
            f'<span class="zh">{html.escape(zh)}</span>'
            f'<span class="en">{html.escape(en)}</span></label>'
            for code, en, zh in OUTCOMES)
        premise_opts = "".join(
            f'<label class="opt"><input type="radio" name="{item_id}::premise_status" '
            f'value="{code}"> <code>{code}</code>'
            f'<span class="zh">{html.escape(zh)}</span>'
            f'<span class="en">{html.escape(en)}</span></label>'
            for code, en, zh in PREMISES)
        conf_opts = "".join(
            f'<label class="opt" style="display:inline-block"><input type="radio" '
            f'name="{item_id}::confidence" value="{v}"> {v}</label>' for v in (1, 2, 3))
        question_en = questions.get(key, "")
        question_zh = zh.get(_sid(question_en), "")
        question_zh_html = (f'<div class="qzh">{html.escape(question_zh)}</div>'
                            if question_zh else "")
        parts.append(f"""
<section class="item" id="{item_id}">
  <div class="qid">{item_id} &middot; {meta['system_code']}</div>
  <div class="q">{html.escape(question_en)}</div>
  {question_zh_html}
  <details open><summary>{len(docs)} 篇截止日之后发表的候选摘要 / candidate abstracts</summary>
    {''.join(abstracts)}
  </details>
  <fieldset><legend>outcome — 这个<strong>问题</strong>后来怎么样了？ / what happened to the question?</legend>{outcome_opts}</fieldset>
  <fieldset><legend>premise_status — 它<strong>依赖的那个假设</strong>怎么样了？ / what happened to its underlying assumption?</legend>{premise_opts}</fieldset>
  <div class="row">
    <div><div class="hint">confidence 信心度（1 没把握 / 2 一般 / 3 很有把握）</div>{conf_opts}</div>
    <div class="notes"><div class="hint">notes 备注（选填；犹豫在哪里、为什么这么判）</div>
      <input type="text" name="{item_id}::notes" placeholder="例如：摘要[3]讲的是另一颗行星，与本题检验无关"></div>
  </div>
</section>""")

    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>标注 Annotation — {annotator}</title><style>{CSS}</style></head>
<body>
<header>
  <h1>盲化标注 Blinded annotation — {annotator}</h1>
  <span id="count" class="hint">0 / {len(item_ids)}</span>
  <div class="bar"><div></div></div>
  <button id="togglezh">隐藏中文 Hide Chinese</button>
  <button id="jump">跳到下一道未答 Next unanswered</button>
  <button id="export" class="primary">导出 CSV</button>
</header>
<main>
  <p class="hint"><strong>只根据下面显示的摘要判断。同话题不等于有人研究了这个问题。</strong>
  中文为机器翻译的辅助阅读版，<strong>以英文原文为准</strong>——AI 裁判读的是英文原文，
  两边看同一份材料，对比才成立。
  答案会自动保存在本浏览器里，随时可以关掉再回来；全部做完点右上角
  <em>Export CSV</em> 导出文件。<br>
  <em>Judge only from the abstracts shown; same topic is not engagement.
  Answers autosave locally; press Export CSV when done.</em></p>
  {GUIDE}
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
