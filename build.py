# ლექციების ბიბლიოთეკის ბილდი.
#   python3 build.py              → ყველა ლექცია + მთავარი გვერდი → რეპოს root (index.html, <კურსი>/<ლექცია>/)
#   python3 build.py efcore/03    → მხოლოდ ის ლექციები, რომელთა გზაც ამას შეიცავს (+ მთავარი გვერდი)
#
# სტრუქტურა:
#   engine/                       ერთი ძრავი ყველა ლექციისთვის (engine.js, engine.css, theme-light.css, index.html)
#   courses/<კურსი>/course.json   {"title", "audience", "order"}
#   courses/<კურსი>/<NN-slug>/    deck.html (სლაიდები + შენიშვნები), lecture.json {"title"}, materials/ (არასავალდებულო)
#
# შენიშვნების პრეფიქსები (<aside class="notes">-ში):
#   "→ " ნაბიჯი · "? " კითხვა · "⏱ " დრო · "! " მნიშვნელოვანი · "~ " ლექტორისთვის · დანარჩენი = სათქმელი
import html, json, pathlib, re, shutil, sys
from pygments.lexers import get_lexer_by_name
from pygments.token import STANDARD_TYPES

ROOT = pathlib.Path(__file__).parent
ENGINE = ROOT / 'engine'
OUT = ROOT   # GitHub Pages serves main/root: built pages live next to the sources
GENERATED = '.generated'   # list of folders build.py created — only these are ever deleted
CSS = (ENGINE / 'engine.css').read_text() + '\n' + (ENGINE / 'theme-light.css').read_text()
JS = (ENGINE / 'engine.js').read_text()
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Georgian:wght@400;600;700;800'
         '&family=JetBrains+Mono:wght@400;600;700;800&display=swap" rel="stylesheet">')

# ---------- code highlighting (<code-block lang="csharp" ...>) ----------
def _short(tt):
    while tt not in STANDARD_TYPES:
        tt = tt.parent
    return STANDARD_TYPES[tt]

def highlight(code, lang):
    lines = code.strip('\n').split('\n')
    ind = min((len(l) - len(l.lstrip()) for l in lines if l.strip()), default=0)
    code = '\n'.join(l[ind:] for l in lines)
    toks = [(None, code)] if lang == 'plain' else list(get_lexer_by_name(lang, stripnl=False, ensurenl=False).get_tokens(code))
    out = [[]]
    for tt, val in toks:
        cls = _short(tt) if tt is not None else ''
        for n, part in enumerate(val.split('\n')):
            if n:
                out.append([])
            if part:
                e = html.escape(part, quote=False)
                if lang.startswith('aspx') or lang == 'asp':
                    e = re.sub(r'(&lt;%[=#:]?|%&gt;)', r'<span class="asp-delim">\1</span>', e)
                out[-1].append(f'<span class="{cls}">{e}</span>' if cls else e)
    while out and not ''.join(out[-1]).strip():
        out.pop()
    return ''.join(f'<span class="ln">{"".join(l) or " "}</span>' for l in out)

def code_block(m):
    a = dict(re.findall(r'(\w+)="([^"]*)"', m.group(1)))
    idattr = f' id="{a["id"]}"' if 'id' in a else ''
    style = f' style="{a["style"]}"' if 'style' in a else ''
    ttl = f'<span class="ttl">{a["title"]}</span>' if 'title' in a else ''
    w = ' data-with' if 'data-with' in m.group(1) else ''
    cls = ('code ' + a.get('cls', '')).strip()
    return f'<pre class="{cls}"{idattr}{style}{w}>{ttl}<code>{highlight(m.group(2), a.get("lang", "plain"))}</code></pre>'

# dark-theme SVG colours → light theme (all decks use the light theme)
LIGHT_MAP = [
    ('#151935', '#ffffff'), ('#1b1f3d', '#f1ece3'), ('#0a0c16', '#fbf8f3'), ('#0d1024', '#ffffff'), ('#e8ecff', '#dbeafe'),
    ('#1d1640', '#f3effe'), ('#2a1d4d', '#ede7fd'), ('#0e2a33', '#eaf2fe'), ('#33240b', '#fef5e4'), ('#123321', '#eaf8ef'),
    ('#272c52', '#e6dfd2'), ('#353b6b', '#cfc6b6'),
    ('#22d3ee', '#2563eb'), ('#3b82f6', '#2563eb'), ('#22c55e', '#16a34a'), ('#f5a524', '#d97706'), ('#8b6cff', '#6d28d9'),
    ('#ec4899', '#db2777'), ('#f43f5e', '#dc2626'), ('#a78bfa', '#0d9488'),
    ('rgba(34,211,238,', 'rgba(37,99,235,'), ('rgba(59,130,246,', 'rgba(37,99,235,'), ('rgba(34,197,94,', 'rgba(22,163,74,'),
    ('rgba(245,165,36,', 'rgba(217,119,6,'), ('rgba(244,63,94,', 'rgba(220,38,38,'), ('rgba(167,139,250,', 'rgba(13,148,136,'),
    ('rgba(139,108,255,', 'rgba(109,40,217,'),
]

# ---------- notes ----------
def note_html(text):
    out, c = [], 0
    for line in (l.strip() for l in text.strip().split('\n')):
        if not line:
            continue
        e = html.escape
        if line.startswith('→'):
            c += 1
            out.append(f'<div class="nl cue" data-c="{c}"><span class="ck">→ {c}</span>{e(line[1:].strip())}</div>')
        elif line.startswith('⏱'): out.append(f'<div class="nl t">{e(line)}</div>')
        elif line.startswith('?'): out.append(f'<div class="nl q">❓ {e(line[1:].strip())}</div>')
        elif line.startswith('!'): out.append(f'<div class="nl imp">{e(line[1:].strip())}</div>')
        elif line.startswith('~'): out.append(f'<div class="nl dir">{e(line[1:].strip())}</div>')
        else: out.append(f'<div class="nl say">{e(line)}</div>')
    return ''.join(out), c

def count_steps(slide):
    n = 0
    for tag in re.findall(r'<(?!/)[^>]+>', slide):
        cls = re.search(r'\b(?:class|cls)="([^"]*)"', tag)
        if cls and {'step', 'codestep', 'trigger'} & set(cls.group(1).split()) and 'data-with' not in tag:
            n += 1
    return n

# ---------- one lecture ----------
SCRIPT_CSS = '''body{font:17px/1.6 "Noto Sans Georgian",system-ui,sans-serif;color:#1e2132;background:#fbf8f3;max-width:860px;margin:0 auto;padding:40px 16px}
h1{font-size:28px;margin:0 0 4px} .back{font:600 14px "JetBrains Mono",monospace;color:#6d28d9;text-decoration:none}
section{background:#fff;border:1px solid #e6dfd2;border-radius:12px;padding:16px 22px;margin:14px 0;break-inside:avoid}
h2{font-size:19px;margin:0 0 8px} h2 span{display:inline-block;min-width:34px;color:#6d28d9;font-family:"JetBrains Mono",monospace}
.nl{margin:3px 0} .t{color:#6d28d9;font:600 14px "JetBrains Mono",monospace} .cue{color:#0d9488;font-weight:700} .ck{margin-right:8px}
.q{color:#b45309} .imp{color:#15803d;font-weight:700} .dir{color:#7b8096;font-style:italic;font-size:15px}
@media print{body{background:#fff} section{border-color:#ccc} .back{display:none}}'''

HOME_CSS = '''#home{position:fixed;left:12px;top:10px;z-index:41;font:600 13px var(--mono);color:var(--muted);text-decoration:none;
padding:6px 10px;border-radius:8px;opacity:0;transition:opacity .25s}
#home:hover,#home:focus-visible{opacity:1;background:rgba(0,0,0,.05)}
:fullscreen #home,body.presenter #home{display:none}'''

def build_lecture(course, lec_dir, meta):
    src = (lec_dir / 'deck.html').read_text()
    slides = re.findall(r'<section class="slide.*?</section>', src, re.S)
    problems, script = [], []
    for i, sl in enumerate(slides, 1):
        m = re.search(r'<aside class="notes">(.*?)</aside>', sl, re.S)
        body, cues = note_html(m.group(1)) if m else ('', 0)
        steps = count_steps(re.sub(r'<aside class="notes">.*?</aside>', '', sl, flags=re.S))
        if steps != cues:
            problems.append(f'slide {i}: steps={steps} cues={cues}')
        h = re.search(r'<h[12][^>]*>(.*?)</h[12]>', sl, re.S)
        script.append((i, re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h.group(1))).strip() if h else '', body))
        if m:
            src = src.replace(sl, sl.replace(m.group(0), f'<aside class="notes" data-cues="{cues}">{body}</aside>'), 1)
    for a, b in LIGHT_MAP:
        src = src.replace(a, b).replace(a.upper(), b)
    src = re.sub(r'<code-block([^>]*)>(.*?)</code-block>', code_block, src, flags=re.S)

    num = lec_dir.name.split('-', 1)[0]
    title = f'{course["title"]} · {int(num)} — {meta["title"]}'   # also the presenter BroadcastChannel key: must be unique
    out = OUT / lec_dir.parent.name / lec_dir.name
    out.mkdir(parents=True, exist_ok=True)
    (out / 'index.html').write_text(f'''<!doctype html>
<html lang="ka"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
{FONTS}
<style>{CSS}
.slide .notes{{display:none}}
{HOME_CSS}</style></head>
<body>
<a id="home" href="../../" title="ყველა ლექცია">← ლექციები</a>
<div id="stage"><div id="deck">
{src}
<div id="hud"><span class="sec"></span><span class="dots"></span><span class="num"></span></div><div id="bar"></div>
</div></div>
<div id="notes"></div><div id="overview"></div>
<div id="help">← → · F</div>
<script>{JS}</script>
</body></html>''')
    rows = ''.join(f'<section><h2><span>{n}</span>{t}</h2>{b}</section>' for n, t, b in script)
    (out / 'script.html').write_text(f'''<!doctype html><html lang="ka"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>სცენარი — {html.escape(title)}</title>{FONTS}<style>{SCRIPT_CSS}</style></head>
<body><a class="back" href="../../">← ლექციები</a><h1>📜 {html.escape(title)}</h1>
<p style="color:#7b8096">→ = შემდეგი ნაბიჯი სლაიდზე · ❓ კითხვა აუდიტორიას · მწვანე = ხაზგასასმელი · ნაცრისფერი = მხოლოდ ლექტორისთვის</p>{rows}</body></html>''')

    materials = []
    if (lec_dir / 'materials').is_dir():
        shutil.copytree(lec_dir / 'materials', out / 'materials', dirs_exist_ok=True)
        materials = sorted(p.name for p in (lec_dir / 'materials').iterdir() if p.is_file())
    print(f'  {lec_dir.parent.name}/{lec_dir.name}: {len(slides)} slides' + ('  ⚠ ' + '; '.join(problems) if problems else ''))
    return {'num': int(num), 'slug': lec_dir.name, 'title': meta['title'], 'slides': len(slides),
            'materials': materials, 'problems': problems}

# ---------- everything ----------
def main(filters):
    marker = OUT / GENERATED
    if not filters and marker.exists():
        for d in marker.read_text().split():
            if (OUT / d).is_dir() and d not in ('courses', 'engine', '.git', '.github'):
                shutil.rmtree(OUT / d)
    catalog = []
    for cdir in sorted((ROOT / 'courses').iterdir()):
        if not (cdir / 'course.json').exists():
            continue
        course = json.loads((cdir / 'course.json').read_text())
        lectures = []
        for ldir in sorted(p for p in cdir.iterdir() if (p / 'deck.html').exists()):
            meta = json.loads((ldir / 'lecture.json').read_text())
            rel = f'{cdir.name}/{ldir.name}'
            if filters and not any(f in rel for f in filters):
                continue
            lectures.append(build_lecture(course, ldir, meta))
        catalog.append({'slug': cdir.name, 'title': course['title'], 'audience': course.get('audience', ''),
                        'order': course.get('order', 99), 'lectures': lectures})
    catalog.sort(key=lambda c: c['order'])
    if not filters:
        page = (ENGINE / 'index.html').read_text().replace('/*CATALOG*/[]', json.dumps(catalog, ensure_ascii=False))
        (OUT / 'index.html').write_text(page)
        (OUT / '.nojekyll').write_text('')
        marker.write_text('\n'.join(c['slug'] for c in catalog) + '\n')
        print(f'index: {sum(len(c["lectures"]) for c in catalog)} lectures in {len(catalog)} courses')
    if any(l['problems'] for c in catalog for l in c['lectures']):
        sys.exit('⚠ step/cue mismatch — see above')

if __name__ == '__main__':
    main(sys.argv[1:])
