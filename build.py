# ლექციების ბიბლიოთეკის ბილდი.
#   python3 build.py              → ყველა ლექცია + მთავარი გვერდი → რეპოს root (index.html, <კურსი>/<ლექცია>/)
#   python3 build.py efcore/03    → მხოლოდ ის ლექციები, რომელთა გზაც ამას შეიცავს (მთავარი გვერდის გარეშე)
#
# courses/<კურსი>/course.json — {"title", "order"}: ერთი კურსი = ერთი ჩანართი მთავარ გვერდზე (C#, EF Core, ASP.NET, SQL, DevOps)
# ლექციის საქაღალდე courses/<კურსი>/<NN-slug>/:
#   deck.html       სლაიდები. ყოველ სლაიდში შეიძლება <aside class="study">…markdown…</aside> — სტუდენტის ახსნა
#   lecture.json    {"title", "why", "outcomes": [...], "review": [{"q", "a"}, ...], "starts_series": true?
#   classwork.md    კლასში დავალება            homework.md    საშინაო (+ "## ამოხსნა" — ჩანს მხოლოდ შემდეგ ლექციაზე)
#   materials/      ფაილები ჩამოსატვირთად
# courses/<კურსი>/syllabus.md — კურსის სილაბუსი → /<კურსი>/syllabus.html (მთავარ გვერდზე „📄 სილაბუსი“)
#
# HTML გვერდები იშიფრება კოდით (.access-code ან LECTURES_CODE) — engine/gate.html კოდს ერთხელ ითხოვს.
# გამონაკლისი: study.html (კონსპექტი) და materials/ — ღიაა, სტუდენტები კოდის გარეშე ხსნიან.
#
# deck.html-ში ლექციის ნაწილები ცხადად იწერება (build მათ სლაიდებად აქცევს):
#   <lecture-review/>            გამეორება — წინა ლექციის review კითხვები
#   <lecture-homework-review/>   წინა ლექციის საშინაო + ამოხსნა
#   <lecture-intro/>             დღის თემა — why + outcomes
#   <lecture-classwork/>         კლასში დავალება (classwork.md)
#   <lecture-check/>             შევამოწმოთ — ამ ლექციის review კითხვები
#   <lecture-homework/>          საშინაო (homework.md, ამოხსნის გარეშე)
import colorsys, base64, html, json, os, pathlib, re, shutil, sys
import markdown
from pygments.lexers import get_lexer_by_name
from pygments.token import STANDARD_TYPES
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

ROOT = pathlib.Path(__file__).parent
ENGINE = ROOT / 'engine'
# LECTURES_OUT=dist → separate output folder (Vercel); default: repo root (GitHub Pages serves main/root)
OUT = (ROOT / os.environ['LECTURES_OUT']).resolve() if os.environ.get('LECTURES_OUT') else ROOT
GENERATED = '.generated'   # list of folders build.py created — only these are ever deleted
CSS = (ENGINE / 'engine.css').read_text() + '\n' + (ENGINE / 'theme-light.css').read_text() + '\n' + (ENGINE / 'theme-dark.css').read_text()
JS = (ENGINE / 'engine.js').read_text()
TOKEN_CSS = '\n'.join(l for l in (ENGINE / 'theme-light.css').read_text().split('\n') if l.startswith('.code .'))
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Georgian:wght@400;600;700;800'
         '&family=JetBrains+Mono:wght@400;600;700;800&display=swap" rel="stylesheet">')
esc = html.escape

# ---------- access code ----------
# Every published HTML page is AES-GCM encrypted with a key derived from the access code; engine/gate.html asks for
# the code once, remembers it in the browser and decrypts the page. The code lives in .access-code (not in git).
CODE_FILE = ROOT / '.access-code'
PBKDF2_ITERATIONS = 200_000
_key = None

def access_key():
    global _key
    if _key is None:
        code = os.environ.get('LECTURES_CODE') or (CODE_FILE.read_text().strip() if CODE_FILE.exists() else '')
        if not code:
            sys.exit('⚠ კოდი არ არის: შექმენი .access-code ფაილი (ერთი ხაზი — კოდი) ან LECTURES_CODE ცვლადი')
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=PBKDF2_ITERATIONS)
        _key = (salt, kdf.derive(code.encode()))
    return _key

def write_page(path, page, encrypt=True):
    if not encrypt:                       # კონსპექტი სტუდენტებისთვის ღიაა — კოდის გარეშე
        path.write_text(page)
        return
    salt, key = access_key()
    iv = os.urandom(12)
    b = lambda x: base64.b64encode(x).decode()
    payload = {'s': b(salt), 'i': b(iv), 'n': PBKDF2_ITERATIONS, 'c': b(AESGCM(key).encrypt(iv, page.encode(), None))}
    path.write_text((ENGINE / 'gate.html').read_text().replace('/*PAYLOAD*/{}', json.dumps(payload)))

# ---------- მუქი თემა ----------
# გვერდები ღია ფერებითაა დაწერილი (inline style-ებიც). build-ისას ყველა ფერი, რომელსაც მუქ თემაში სხვა ფერი სჭირდება,
# იცვლება var(--xb-HEX,#HEX)-ით (ფონი/ჩარჩო) ან var(--xc-HEX,#HEX)-ით (ტექსტი): ღია თემაში ცვლადი არ არსებობს → ზუსტად
# იგივე ფერია; html[data-theme=dark]-ში ცვლადებს მუქი მნიშვნელობა ეძლევა. SVG-ის fill/stroke ატრიბუტებს — CSS სელექტორებით.
THEME_HEAD = ('<script>(()=>{const d=document.documentElement,K="lectures:theme";'
              'try{d.dataset.theme=localStorage.getItem(K)||"light"}catch(e){d.dataset.theme="light"}'
              'window.toggleTheme=()=>{const t=d.dataset.theme==="dark"?"light":"dark";d.dataset.theme=t;try{localStorage.setItem(K,t)}catch(e){}};'
              'document.addEventListener("click",e=>{const b=e.target.closest(".themebtn");if(b){b.blur();toggleTheme()}});'
              'addEventListener("storage",e=>{if(e.key===K)d.dataset.theme=e.newValue||"light"})})()</script>')
THEME_BTN = '<button class="themebtn" type="button" title="ღია / მუქი თემა (T)"><span class="l">🌙</span><span class="d">☀️</span></button>'
THEME_BTN_CSS = ('.themebtn .d{display:none}html[data-theme=dark] .themebtn .l{display:none}html[data-theme=dark] .themebtn .d{display:inline}')
# სილაბუსის / LMS-ის გვერდები: მუქი ცვლადები + ღილაკის სტილი ({{THEME}} შაბლონში)
PAGE_THEME = (THEME_HEAD + '<style>html[data-theme=dark]{color-scheme:dark;--bg:#16181d;--card:#1e2128;--ink:#e6e2da;--ink2:#bebab1;'
              '--muted:#8a8e98;--line:#2d313b;--line2:#3c414d;--accent:#ab9ff2;--accent-soft:#272439;--teal:#72bfb3;--green:#8fc8a1;'
              '--soft:#252932;--code-ink:#cfc6ff}'
              '.top .themebtn{font:700 14px var(--sans);line-height:1.25;border:1px solid var(--line2);background:var(--card);color:var(--ink);'
              'border-radius:10px;padding:5px 9px;cursor:pointer}' + THEME_BTN_CSS + '</style>')
_HEX = re.compile(r'#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b')
_PAPER = {'#f1ece3', '#f6f1e8', '#fbf8f3', '#f4efe6', '#efe8dc', '#fffdf9', '#ebe5d8', '#e6dfd2', '#e4ddcf', '#cfc6b6', '#d6ccbb', '#d6cdbb'}   # თბილი „ქაღალდი“ — მუქში ნეიტრალური
_TEXT_PROPS = ('color', '-webkit-text-fill-color', 'caret-color')

def _rgb(h):
    h = h.lstrip('#').lower()
    if len(h) == 3: h = ''.join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))

def _hex(h, l, s):
    return '#' + ''.join(f'{round(x * 255):02x}' for x in colorsys.hls_to_rgb(h, l, s))

def dark_of(hx, kind):
    """kind 'b' — ფონი/ჩარჩო/SVG, 'c' — ტექსტი. None → ფერი მუქ თემაშიც იგივე რჩება."""
    h, l, s = colorsys.rgb_to_hls(*_rgb(hx))
    neutral = s < .15 or l > .985 or hx.lower() in _PAPER
    if kind == 'c':
        if l > .97: return '#16181d'                       # თეთრი ტექსტი ფერად ფონზე → მუქი (ფონი პასტელი ხდება)
        if l < .47: return _hex(h, .85, 0) if neutral else _hex(h, .8, min(s, .6))   # მუქი ტექსტი → ღია
        return None
    if l > .985: return '#1e2128'                          # თეთრი ბარათი
    if l > .93: return '#1d2027' if neutral else _hex(h, .16, min(s, .3))   # ღია ფონი / ტინტი
    if l > .8: return '#3c414d' if neutral else _hex(h, .27, min(s, .35))  # ღია ჩარჩო
    if l > .64: return '#4a4f5c' if neutral else _hex(h, .36, min(s, .4))
    if l > .25 and s > .3: return _hex(h, .74, min(s, .6))                   # აქცენტი → პასტელი
    return None

def _skip_block(decls):
    # განზრახ მუქი ბლოკი (ტერმინალი, კოდის ფანჯარა) — ფერებს არ ვეხებით
    for prop, val in decls:
        if prop in ('background', 'background-color'):
            for hx in _HEX.findall(val):
                if colorsys.rgb_to_hls(*_rgb(hx))[1] < .3: return True
    return False

def _themeify_css(css, used):
    def block(body):
        decls = [(m.group(1).lower(), m.group(2)) for m in re.finditer(r'([a-zA-Z-]+)\s*:\s*([^;]*)', body)]
        if _skip_block(decls): return body
        def decl(m):
            prop, val = m.group(1), m.group(2)
            if prop.startswith('--'): return m.group(0)
            kind = 'c' if prop.lower() in _TEXT_PROPS else 'b'
            def rep(hm):
                hx = hm.group(0).lower()
                d = dark_of(hx, kind)
                if not d: return hm.group(0)
                name = f'--x{kind}-{hx[1:]}'; used[name] = d
                return f'var({name},{hm.group(0)})'
            return prop + ':' + _HEX.sub(rep, val)
        return re.sub(r'(--[\w-]+|[a-zA-Z-]+)\s*:\s*([^;{}]*)', decl, body)
    # თითო წესის შიგთავსი {…} ცალკე (selector-ებში #id-ს არ ვეხებით)
    return re.sub(r'\{([^{}]*)\}', lambda m: '{' + block(m.group(1)) + '}', css)

def themeify(page):
    used, svg = {}, set()
    page = re.sub(r'(<style[^>]*>)(.*?)(</style>)', lambda m: m.group(1) + _themeify_css(m.group(2), used) + m.group(3), page, flags=re.S)
    page = re.sub(r'(\sstyle=")([^"]*)(")', lambda m: m.group(1) + _themeify_css('{' + m.group(2) + '}', used)[1:-1] + m.group(3), page)
    for attr, hx in re.findall(r'\s(fill|stroke|stop-color)="(#[0-9a-fA-F]{3,6})"', page):
        d = dark_of(hx, 'b')
        if d: svg.add(f'html[data-theme=dark] svg [{attr}="{hx}"]{{{attr}:{d}}}')
    css = 'html[data-theme=dark]{' + ';'.join(f'{k}:{v}' for k, v in sorted(used.items())) + '}\n' + '\n'.join(sorted(svg))
    return page.replace('</head>', f'<style>{css}</style>\n</head>', 1)

# ---------- code highlighting ----------
def _short(tt):
    while tt not in STANDARD_TYPES:
        tt = tt.parent
    return STANDARD_TYPES[tt]

def highlight(code, lang):
    lines = code.strip('\n').split('\n')
    ind = min((len(l) - len(l.lstrip()) for l in lines if l.strip()), default=0)
    code = '\n'.join(l[ind:] for l in lines)
    toks = [(None, code)] if lang in ('plain', 'text', '') else list(get_lexer_by_name(lang, stripnl=False, ensurenl=False).get_tokens(code))
    out = [[]]
    for tt, val in toks:
        cls = _short(tt) if tt is not None else ''
        for n, part in enumerate(val.split('\n')):
            if n:
                out.append([])
            if part:
                e = esc(part, quote=False)
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

LIGHT_MAP = [  # dark-theme SVG colours → light theme (all decks use the light theme)
    ('#151935', '#ffffff'), ('#1b1f3d', '#f1ece3'), ('#0a0c16', '#fbf8f3'), ('#0d1024', '#ffffff'), ('#e8ecff', '#dbeafe'),
    ('#1d1640', '#f3effe'), ('#2a1d4d', '#ede7fd'), ('#0e2a33', '#eaf2fe'), ('#33240b', '#fef5e4'), ('#123321', '#eaf8ef'),
    ('#272c52', '#e6dfd2'), ('#353b6b', '#cfc6b6'),
    ('#22d3ee', '#2563eb'), ('#3b82f6', '#2563eb'), ('#22c55e', '#16a34a'), ('#f5a524', '#d97706'), ('#8b6cff', '#6d28d9'),
    ('#ec4899', '#db2777'), ('#f43f5e', '#dc2626'), ('#a78bfa', '#0d9488'),
    ('rgba(34,211,238,', 'rgba(37,99,235,'), ('rgba(59,130,246,', 'rgba(37,99,235,'), ('rgba(34,197,94,', 'rgba(22,163,74,'),
    ('rgba(245,165,36,', 'rgba(217,119,6,'), ('rgba(244,63,94,', 'rgba(220,38,38,'), ('rgba(167,139,250,', 'rgba(13,148,136,'),
    ('rgba(139,108,255,', 'rgba(109,40,217,'),
]

# ---------- study markdown ----------
# Fenced blocks:  ```csharp Title   ```prompt Title   ```check (? კითხვა / = პასუხი)   ```terms (ტერმინი — ახსნა)   ```note / ```warn
def md_inline(text):
    h = markdown.markdown(text.strip(), extensions=['sane_lists'])
    return re.sub(r'^<p>(.*)</p>$', r'\1', h, flags=re.S)

def render_fence(kind, arg, body):
    body = body.strip('\n')
    if kind == 'prompt':
        return (f'<div class="prompt"><div class="ph"><span>🤖 {esc(arg or "AI-სთვის — დააკოპირე და ჰკითხე")}</span>'
                f'<button class="copy" type="button">კოპირება</button></div><div class="pb">{esc(body)}</div></div>')
    if kind == 'check':
        items, cur = [], None
        for line in body.split('\n'):
            if line.startswith('?'):
                cur = [line[1:].strip(), []]; items.append(cur)
            elif line.startswith('=') and cur:
                cur[1].append(line[1:].strip())
            elif cur and cur[1] and line.strip():
                cur[1].append(line.strip())
        qs = ''.join(f'<details><summary>{md_inline(q)}</summary><div class="ans">{md_inline(" ".join(a))}</div></details>' for q, a in items)
        return f'<div class="selfcheck"><div class="sh">✅ შეამოწმე თავი <small>დაფიქრდი, მერე გახსენი პასუხი</small></div>{qs}</div>'
    if kind == 'terms':
        rows = [l.split('—', 1) for l in body.split('\n') if '—' in l]
        dl = ''.join(f'<dt>{md_inline(t)}</dt><dd>{md_inline(d)}</dd>' for t, d in rows)
        return f'<div class="terms"><div class="th">📘 ტერმინები</div><dl>{dl}</dl></div>'
    if kind in ('note', 'warn', 'tip'):
        ico = {'note': '💡', 'warn': '⚠️', 'tip': '👉'}[kind]
        return f'<div class="callout {kind}"><span class="ci">{ico}</span><div>{markdown.markdown(body, extensions=["sane_lists"])}</div></div>'
    lang = kind or 'plain'
    arg = arg.rstrip('!').strip()   # '!' only marks the block shown on the homework-review slide
    title = esc(arg) if arg else esc(lang)
    return (f'<div class="codebox"><div class="ch"><span>{title}</span><button class="copy" type="button">კოპირება</button></div>'
            f'<pre class="code"><code>{highlight(body, lang)}</code></pre></div>')

FENCE = re.compile(r'^```(\w*)[ \t]*([^\n]*)\n(.*?)^```[ \t]*$', re.M | re.S)

def md(text):
    lines = text.strip('\n').split('\n')
    ind = min((len(l) - len(l.lstrip()) for l in lines if l.strip()), default=0)
    text = '\n'.join(l[ind:] for l in lines)
    blocks = []
    def keep(m):
        blocks.append(render_fence(m.group(1), m.group(2).strip(), m.group(3)))
        return f'\n\n@@B{len(blocks) - 1}@@\n\n'
    text = FENCE.sub(keep, text)
    h = markdown.markdown(text, extensions=['tables', 'sane_lists'])
    return re.sub(r'<p>@@B(\d+)@@</p>|@@B(\d+)@@', lambda m: blocks[int(m.group(1) or m.group(2))], h)

def md_doc(path):
    """# სათაური / შესავალი / ## სექციები → {'title', 'intro', 'parts': [(heading, md)]}"""
    if not path.exists():
        return None
    t = path.read_text()
    title = re.search(r'^# (.+)$', t, re.M).group(1).strip()
    t = re.sub(r'^# .+\n', '', t, count=1, flags=re.M)
    chunks = re.split(r'^## (.+)$', t, flags=re.M)
    return {'title': title, 'intro': chunks[0].strip(), 'parts': [(chunks[i].strip(), chunks[i + 1].strip()) for i in range(1, len(chunks), 2)]}

def part(doc, key):
    return next((b for h, b in doc['parts'] if key in h), '')

def slide_md(text):   # markdown → slide markup (deck classes)
    h = markdown.markdown(text, extensions=['sane_lists']).replace('<code>', '<code class="i">')
    return h.replace('<ul>', '<ul class="clean small">').replace('<ol>', '<ol class="clean small">')

def first_code(text):   # the code fence marked with a trailing "!" in its title, else the first code fence
    fences = [m for m in FENCE.finditer(text) if m.group(1) not in ('prompt', 'check', 'terms', 'note', 'warn', 'tip')]
    m = next((f for f in fences if f.group(2).strip().endswith('!')), fences[0] if fences else None)
    return (m.group(1), m.group(2).strip().rstrip('!').strip(), m.group(3)) if m else None

# ---------- generated slides ----------
def qa_rows(review):
    cls = 'qa-list two' if len(review) > 4 else 'qa-list'   # 5+ questions: two columns, so the slide never overflows
    return f'<div class="{cls}">' + ''.join(f'<div class="qa"><span class="n">{n}</span><span class="q">{md_inline(r["q"]).replace("<code>", "<code class=\"i\">")}</span>'
                   f'<span class="a step">{md_inline(r["a"]).replace("<code>", "<code class=\"i\">")}</span></div>' for n, r in enumerate(review, 1)) + '</div>'

def check_md(review):
    return '```check\n' + '\n'.join(f'? {r["q"]}\n= {r["a"]}' for r in review) + '\n```'

def gen_review(prev):
    pm, num = prev['meta'], prev['num']
    return f'''<section class="slide" data-section="გამეორება">
  <div class="kicker">გამეორება · ლექცია {num}</div>
  <h2>გავიხსენოთ: <span class="grad">{esc(pm["title"])}</span></h2>
  {qa_rows(pm["review"])}
  <aside class="study">
## გავიხსენოთ წინა ლექცია

ლექცია {num} — **{esc(pm["title"])}**. ახალ თემამდე ვამოწმებთ, რა დაგვამახსოვრდა. ჯერ თვითონ უპასუხე, მერე გახსენი პასუხი. თუ რომელიმე გაგიჭირდა, [წინა ლექციის კონსპექტს]({prev["href"]}study.html) გადახედე.

{check_md(pm["review"])}
  </aside>
</section>'''

def gen_homework_review(prev):
    hw = prev['homework']
    sol = part(hw, 'ამოხსნ')
    code = first_code(sol)
    if code and code[2].strip('\n').count('\n') >= 20:
        print(f'  ⚠ ლექცია {prev["num"]}-ის ამოხსნის კოდი სლაიდზე {code[2].strip(chr(10)).count(chr(10)) + 1} ხაზია — ≤20 ჯობია (მონიშნე სხვა ბლოკი "!"-ით)')
    right = (f'<code-block lang="{code[0]}" cls="sm" title="{esc(code[1])}">\n{code[2]}</code-block>' if code else '')   # code-block escapes itself
    return f'''<section class="slide" data-section="საშინაოს განხილვა">
  <div class="kicker">🏠 საშინაოს განხილვა · ლექცია {prev["num"]}</div>
  <h2>{esc(hw["title"])}</h2>
  <div class="grid2" style="grid-template-columns:1fr 1.25fr;align-items:start;gap:30px">
    <div class="card accent step" style="--a:var(--mvc)"><h3><span class="ico">📝</span>რა უნდა გაგეკეთებინათ</h3>{slide_md(part(hw, "მოთხოვნ"))}</div>
    <div class="step">{right}</div>
  </div>
  <div class="callout step mt" style="--a:var(--api)">შეადარეთ თქვენს კოდს. რა გამოგივიდათ სხვანაირად — და რატომ?</div>
  <aside class="study">
## საშინაოს განხილვა

წინა ლექციის საშინაო: **{esc(hw["title"])}**. ქვემოთ არის ერთ-ერთი სწორი ამოხსნა. შენი კოდი შეიძლება სხვანაირად იყოს დაწერილი — მთავარია, მოთხოვნები სრულდებოდეს.

### მოთხოვნები
{part(hw, "მოთხოვნ")}

### ამოხსნა
{sol}
  </aside>
</section>'''

def gen_intro(meta):
    outs = ''.join(f'<li class="step">{md_inline(o).replace("<code>", "<code class=\"i\">")}</li>' for o in meta['outcomes'])
    return f'''<section class="slide" data-section="დღის თემა">
  <div class="kicker">დღის თემა</div>
  <h2><span class="grad">{esc(meta["title"])}</span></h2>
  <div class="grid2" style="grid-template-columns:1fr 1fr;align-items:start;gap:40px">
    <div class="card accent step" style="--a:var(--asp)"><h3><span class="ico">🤔</span>რატომ გჭირდებათ</h3><p class="small">{md_inline(meta["why"]).replace("<code>", "<code class=\"i\">")}</p></div>
    <div class="card accent" style="--a:var(--mvc)"><h3><span class="ico">🎯</span>ლექციის ბოლოს შეძლებთ</h3><ul class="clean small">{outs}</ul></div>
  </div>
  <aside class="study">
## დღის თემა: {esc(meta["title"])}

{meta["why"]}

**ლექციის ბოლოს შეძლებ:**

{chr(10).join("- " + o for o in meta["outcomes"])}
  </aside>
</section>'''

def gen_task(doc, section, kicker, ico, color, footer, study_head):
    bonus = part(doc, 'ბონუს')
    done = part(doc, 'მზადაა')
    steps = part(doc, 'ნაბიჯ') or part(doc, 'მოთხოვნ')
    right = f'<div class="card accent step" style="--a:var(--asp)"><h3><span class="ico">⭐</span>ბონუსი</h3>{slide_md(bonus)}</div>' if bonus else ''
    cols = '1.5fr 1fr' if bonus else '1fr'
    study_parts = '\n\n'.join(f'### {h}\n\n{b}' for h, b in doc['parts'] if 'ამოხსნ' not in h)
    return f'''<section class="slide" data-section="{section}">
  <div class="kicker">{kicker}</div>
  <h2>{esc(doc["title"])}</h2>
  <div class="grid2" style="grid-template-columns:{cols};align-items:start">
    <div class="card accent step" style="--a:{color}">
      <h3><span class="ico">{ico}</span>{md_inline(doc["intro"]).replace("<code>", "<code class=\"i\">") if doc["intro"] else "დავალება"}</h3>
      {slide_md(steps)}
      {f'<p class="tiny" style="margin-top:14px">✓ მზადაა, როცა: {md_inline(done)}</p>' if done else ''}
    </div>
    {right}
  </div>
  <div class="callout step mt" style="--a:var(--api)">{footer}</div>
  <aside class="study">
## {study_head}: {esc(doc["title"])}

{doc["intro"]}

{study_parts}
  </aside>
</section>'''

def gen_check(meta):
    return f'''<section class="slide" data-section="შეჯამება">
  <div class="kicker">შევამოწმოთ</div>
  <h2>{len(meta["review"])} კითხვა</h2>
  {qa_rows(meta["review"])}
  <aside class="study">
## შეამოწმე, რა დაგამახსოვრდა

ეს კითხვები შემდეგი ლექციის დასაწყისშიც დაისმება.

{check_md(meta["review"])}
  </aside>
</section>'''

def expand(src, meta, ldir, prev):
    gen = {
        'lecture-review': lambda: gen_review(prev) if prev and prev['meta'].get('review') else None,
        'lecture-homework-review': lambda: gen_homework_review(prev) if prev and prev['homework'] else None,
        'lecture-intro': lambda: gen_intro(meta),
        'lecture-classwork': lambda: gen_task(md_doc(ldir / 'classwork.md'), 'პრაქტიკა', '🧑‍💻 თქვენ აკეთებთ · კლასში', '📝', 'var(--mvc)',
                                              'წესი: <b>ჯერ ცდი თვითონ</b> → გვერდით მჯდომს ჰკითხე → მერე მე', 'კლასში დავალება'),
        'lecture-check': lambda: gen_check(meta),
        'lecture-homework': lambda: gen_task(md_doc(ldir / 'homework.md'), 'საშინაო', '🏠 საშინაო დავალება', '🏠', 'var(--net)',
                                             'შემდეგი ლექციის დასაწყისში ამ დავალებას <b>ერთად განვიხილავთ</b>', 'საშინაო დავალება'),
    }
    problems = []
    if '<lecture-intro/>' in src:   # new-format lecture: every part is required
        # classwork.md / homework.md are optional (e.g. an intro lecture without tasks) — but tag and file go together
        need = ['lecture-intro', 'lecture-check']
        for tag, f in (('lecture-classwork', 'classwork.md'), ('lecture-homework', 'homework.md')):
            if (ldir / f).exists(): need.append(tag)
            elif f'<{tag}/>' in src: problems.append(f'<{tag}/> არის, მაგრამ {f} აკლია')
        if prev and prev['meta'].get('review'): need.append('lecture-review')
        if prev and prev['homework']: need.append('lecture-homework-review')
        problems += [f'<{n}/> აკლია' for n in need if f'<{n}/>' not in src]
        for k in ('why', 'outcomes', 'review'):
            if not meta.get(k): problems.append(f'lecture.json: "{k}" აკლია')
        if problems:
            return src, problems
    for tag, fn in gen.items():
        if f'<{tag}/>' in src:
            out = fn()
            src = src.replace(f'<{tag}/>', out or '')
    return src, problems

# ---------- one lecture ----------
HOME_CSS = '''#home{position:fixed;left:12px;top:10px;z-index:41;font:600 13px var(--mono);color:var(--muted);text-decoration:none;
padding:6px 10px;border-radius:8px;opacity:0;transition:opacity .25s}
#home:hover,#home:focus-visible{opacity:1;background:rgba(0,0,0,.05)}
:fullscreen #home{display:none}
#themebtn{position:fixed;right:16px;top:12px;z-index:41;font:700 14px var(--font);line-height:1.25;color:var(--ink2);background:var(--card);
border:1px solid var(--line2);border-radius:10px;padding:7px 10px;cursor:pointer;opacity:.85;box-shadow:var(--shadow)}
#themebtn:hover,#themebtn:focus-visible{opacity:1}#help{right:68px;top:20px}
:fullscreen #themebtn{opacity:0}:fullscreen #themebtn:hover{opacity:1}
html[data-theme=dark] #home:hover{background:rgba(255,255,255,.06)}
''' + THEME_BTN_CSS

def heading(sl):
    h = re.search(r'<h[12][^>]*>(.*?)</h[12]>', sl, re.S)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h.group(1)))).strip() if h else ''

def build_lecture(course, cdir, ldir, meta, prev):
    src, problems = expand((ldir / 'deck.html').read_text(), meta, ldir, prev)
    num = int(ldir.name.split('-', 1)[0])
    title = f'{course["title"]} · {num} — {meta["title"]}'   # also the BroadcastChannel key: must be unique
    out = OUT / cdir.name / ldir.name
    if problems:
        print(f'  {cdir.name}/{ldir.name}: ⚠ ' + '; '.join(problems))
        return None, problems

    slides = re.findall(r'<section class="slide.*?</section>', src, re.S)
    study = []
    for i, sl in enumerate(slides, 1):
        m = re.search(r'<aside class="study">(.*?)</aside>', sl, re.S)
        sec = re.search(r'data-section="([^"]*)"', sl)
        study.append({'n': i, 'title': heading(sl), 'section': sec.group(1) if sec else '', 'html': md(m.group(1)) if m else None})
        clean = re.sub(r'<aside class="(?:study|notes)">.*?</aside>', '', sl, flags=re.S)
        src = src.replace(sl, clean, 1)
    src = re.sub(r'<aside class="notes">.*?</aside>', '', src, flags=re.S)   # old lecturer notes are never published
    for a, b in LIGHT_MAP:
        src = src.replace(a, b).replace(a.upper(), b)
    src = re.sub(r'<code-block([^>]*)>(.*?)</code-block>', code_block, src, flags=re.S)
    has_study = any(s['html'] for s in study)

    out.mkdir(parents=True, exist_ok=True)
    write_page(out / 'index.html', themeify(f'''<!doctype html>
<html lang="ka"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
{FONTS}{THEME_HEAD}
<style>{CSS}
{HOME_CSS}</style></head>
<body{' data-study="1"' if has_study else ''}>
<a id="home" href="../../" title="ყველა ლექცია">← ლექციები</a>{THEME_BTN.replace('class="themebtn"', 'id="themebtn" class="themebtn"')}
<div id="stage"><div id="deck">
{src}
<div id="hud"><span class="sec"></span><span class="dots"></span><span class="num"></span></div><div id="bar"></div>
</div></div>
<div id="overview"></div>
<div id="help">← → · F</div>
<script>{JS}</script>
</body></html>'''))
    for stale in ('script.html', 'study.html'):
        (out / stale).unlink(missing_ok=True)

    materials = []
    if (ldir / 'materials').is_dir():
        shutil.copytree(ldir / 'materials', out / 'materials', dirs_exist_ok=True)
        materials = sorted(p.name for p in (ldir / 'materials').iterdir() if p.is_file())
    if has_study:
        write_study(out, course, meta, num, title, study, materials)
    print(f'  {cdir.name}/{ldir.name}: {len(slides)} slides' + (f', study {sum(1 for s in study if s["html"])} blocks' if has_study else ''))
    return {'num': num, 'slug': ldir.name, 'title': meta['title'], 'slides': len(slides), 'materials': materials, 'study': has_study}, []

def write_study(out, course, meta, num, deck_title, study, materials):
    blocks = []   # [{slides:[n..], title, section, html}]
    pending = []
    for s in study:
        if s['html']:
            title, body = s['title'], s['html']
            m = re.match(r'\s*<h([23])>(.*?)</h\1>', body, re.S)   # study text's own heading wins over the slide title
            if m:
                title, body = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))), body[m.end():]
            blocks.append({'slides': pending + [s['n']], 'title': title, 'section': s['section'], 'html': body}); pending = []
        elif blocks:
            blocks[-1]['slides'].append(s['n'])
        else:
            pending.append(s['n'])
    body, toc, cur_sec = [], [], None
    for b in blocks:
        if b['section'] != cur_sec:
            cur_sec = b['section']
            sid = f'sec-{len(toc) + 1}'
            toc.append(f'<a href="#{sid}">{esc(cur_sec)}</a>')
            body.append(f'<h2 class="sec" id="{sid}">{esc(cur_sec)}</h2>')
        anchors = ''.join(f'<span class="anchor" id="s-{n}"></span>' for n in b['slides'])
        first = b['slides'][0]
        body.append(f'<article class="blk" data-slides="{",".join(map(str, b["slides"]))}">{anchors}'
                    f'<div class="bh"><h3>{esc(b["title"])}</h3><a class="chip" href="index.html#/{first}" data-go="{first}" title="პრეზენტაციაში გახსნა">სლაიდი {first}</a></div>'
                    f'{b["html"]}</article>')
    mats = ''.join(f'<a href="materials/{esc(m)}" download>📎 {esc(m)}</a>' for m in materials)
    page = (ENGINE / 'study.html').read_text()
    for k, v in {'{{TITLE}}': esc(meta['title']), '{{COURSE}}': esc(course['title']), '{{NUM}}': str(num),
                 '{{DECK_TITLE_JSON}}': json.dumps(deck_title, ensure_ascii=False), '{{TOC}}': ''.join(toc),
                 '{{BODY}}': '\n'.join(body), '{{MATERIALS}}': mats, '{{TOKEN_CSS}}': TOKEN_CSS, '{{FONTS}}': FONTS,
                 '{{THEME_HEAD}}': THEME_HEAD, '{{THEME_BTN_STUDY}}': THEME_BTN.replace('class="themebtn"', 'class="themebtn btn"'), '{{THEME_BTN_CSS}}': THEME_BTN_CSS}.items():
        page = page.replace(k, v)
    write_page(out / 'study.html', themeify(page), encrypt=False)

# ---------- everything ----------

# ---------- LMS-ის კოდის გვერდები: courses/<კურსი>/lms/NN.md → /<კურსი>/lms/NN.html ----------
# NN.md: ჩვეულებრივი markdown + ```lang Path/To/File.cs ბლოკები — ფაილის სრული შიგთავსი ამ ლექციის შემდეგ.
# ფაილების მდგომარეობა იკრიბება 01..NN-ით: ახალი ფაილი → „ახალი“, შეცვლილი → „შეცვლილი“ (ახალი/შეცვლილი ხაზები მონიშნულია).
# "🗑 Path/To/File.cs" — ფაილი წაიშალა.
import difflib
FILE_FENCE = re.compile(r'^```(\w+) +(\S+\.\w+)\n(.*?)^```\s*$', re.M | re.S)

def lms_files(text):
    return [(m.group(1), m.group(2), m.group(3).rstrip('\n')) for m in FILE_FENCE.finditer(text)]

def write_lms_pages(cdir, course, briefs, titles):
    out_dir = OUT / cdir.name / 'lms'
    src_dir = cdir / 'lms'
    state = {}
    nums = sorted(briefs)
    if not nums:
        return
    out_dir.mkdir(parents=True, exist_ok=True)
    for i, num in enumerate(nums):
        f = src_dir / f'{num:02d}.md'
        text = f.read_text() if f.exists() else ''
        if re.search(r'^🆕', text, re.M):   # 🆕 — ცალკე, ახალი პროექტი: წინა ლექციების ფაილები აღარ ითვლება
            state = {}
            text = re.sub(r'^🆕.*\n?', '', text, flags=re.M)
        b = briefs[num]
        parts = [f'<div class="k">{esc(course["title"])} · ლექცია {num:02d}</div><h1>{md_inline(titles.get(num, ""))}</h1>']
        if b.get('learn'):
            parts.append('<div class="box"><h3>🎯 რას ისწავლის სტუდენტი</h3><ul>' + ''.join(f'<li>{md_inline(x)}</li>' for x in b['learn']) + '</ul></div>')
        proj = b.get('project', 'LMS')
        if b.get('build'):
            parts.append(f'<div class="box"><h3>🛠 რას ვწერთ {esc(proj)}-ში</h3><ul>' + ''.join(f'<li>{md_inline(x)}</li>' for x in b['build']) + '</ul></div>')
        files = lms_files(text)
        deleted = re.findall(r'^🗑\s+(\S+)', text, re.M)
        if not files and not deleted:
            parts.append('<div class="empty">კოდი ამ ლექციისთვის ჯერ არ დაწერილა</div>')
        else:
            prose = FILE_FENCE.sub('', re.sub(r'^🗑.*$', '', text, flags=re.M)).strip()
            if prose:
                parts.append('<h2>მიმოხილვა</h2>' + markdown.markdown(prose, extensions=['tables', 'sane_lists', 'fenced_code']))
            parts.append('<h2>ფაილები</h2><p class="legend"><span class="tag new">ახალი</span><span class="tag mod">შეცვლილი</span><span class="tag del">წაშლილი</span> · <i></i>ახალი / შეცვლილი ხაზი</p>')
            toc, boxes = [], []
            for k, (lang, path, body) in enumerate(files):
                prev = state.get(path)
                lines = body.split('\n')
                if prev is None:
                    tag, add = '<span class="tag new">ახალი</span>', set()
                else:
                    tag, add = '<span class="tag mod">შეცვლილი</span>', set()
                    for op, a1, a2, b1, b2 in difflib.SequenceMatcher(None, prev.split('\n'), lines, autojunk=False).get_opcodes():
                        if op in ('replace', 'insert'):
                            add.update(range(b1, b2))
                html_code = highlight(body, lang)
                n = [0]
                def mark(m):
                    idx = n[0]; n[0] += 1
                    return '<span class="ln add">' if idx in add else '<span class="ln">'
                html_code = re.sub(r'<span class="ln">', mark, html_code)
                fid = f'f{k}'
                toc.append(f'<a href="#{fid}">{tag}{esc(path)}</a>')
                boxes.append(f'<div class="codebox" id="{fid}"><div class="ch"><span>{tag}{esc(path)}</span><button class="copy" type="button">კოპირება</button></div><pre class="code"><code>{html_code}</code></pre></div>')
                state[path] = body
            for path in deleted:
                state.pop(path, None)
                toc.append(f'<a><span class="tag del">წაშლილი</span>{esc(path)}</a>')
            parts.append('<div class="toc">' + '<br>'.join(toc) + '</div>' + ''.join(boxes))
        if state:
            parts.append('<h2>პროექტი ამ ლექციის შემდეგ</h2><div class="tree">' + esc('\n'.join(sorted(state))) + '</div>')
        prev_n = nums[i - 1] if i else None
        next_n = nums[i + 1] if i + 1 < len(nums) else None
        nav = (f'<a href="{prev_n:02d}.html">← {prev_n:02d}</a>' if prev_n else '') + (f'<a href="{next_n:02d}.html">{next_n:02d} →</a>' if next_n else '')
        page = (ENGINE / 'lms.html').read_text()
        for key, v in {'{{TITLE}}': f'{num:02d} · ' + esc(titles.get(num, '')), '{{NUM}}': str(num), '{{NAV}}': nav,
                       '{{BODY}}': '\n'.join(parts), '{{FONTS}}': FONTS, '{{TOKEN_CSS}}': TOKEN_CSS,
                       '{{THEME}}': PAGE_THEME, '{{THEME_BTN}}': THEME_BTN}.items():
            page = page.replace(key, v)
        write_page(out_dir / f'{num:02d}.html', themeify(page))

# კურსის სილაბუსი: courses/<კურსი>/syllabus.md → /<კურსი>/syllabus.html
#   "## ნაწილი (N ლექცია)" = ნაწილი; "### 01. სათაური" + აღწერა = ლექცია; აწყობილ ლექციას გვერდით ბმულები უჩნდება
def write_syllabus(cdir, course):
    src = cdir / 'syllabus.md'
    out = OUT / cdir.name / 'syllabus.html'
    if not src.exists():
        out.unlink(missing_ok=True)
        return False
    out.parent.mkdir(parents=True, exist_ok=True)
    # სილაბუსის ლექცია ↔ დეკი: საქაღალდის ნომრით, ან lecture.json-ის "syllabus" ველით (თუ დეკი სხვა ნომერზეა)
    built = {json.loads((d / 'lecture.json').read_text()).get('syllabus', int(d.name.split('-', 1)[0])): d.name
             for d in cdir.iterdir() if (d / 'deck.html').exists() and d.name[:2].isdigit()}
    # "📚 …" = რას ისწავლის სტუდენტი, "🛠 [პროექტი |] …" = რას ვწერთ პროექტში (ერთი ხაზი = ერთი პუნქტი) → ლექციის ⓘ drawer (გვერდზე არ ჩანს)
    briefs, cur, lines = {}, None, []
    for line in src.read_text().splitlines():
        m = re.match(r'### (\d+)\.', line)
        if m:
            cur = int(m.group(1))
        if cur is not None and line.startswith(('📚', '🛠')):
            kind, body = ('learn' if line.startswith('📚') else 'build'), line[1:].strip()
            if kind == 'build' and '|' in body:
                briefs.setdefault(cur, {})['project'], body = [x.strip() for x in body.split('|', 1)]
            briefs.setdefault(cur, {}).setdefault(kind, []).append(body)   # ერთი ხაზი = ერთი პუნქტი
            continue
        lines.append(line)
    h = markdown.markdown('\n'.join(lines), extensions=['tables', 'sane_lists'])
    def lec(m):
        num, title, desc = int(m.group(1)), m.group(2), m.group(3) or ''
        slug, b = built.get(num), briefs.get(num, {})
        proj = b.get('project')
        links = []   # ⋯ მენიუ: მხოლოდ ის, რაც ნამდვილად არსებობს
        if slug:
            links += [f'<a href="{slug}/">▶ პრეზენტაცია</a>', f'<a href="{slug}/study.html">📖 კონსპექტი</a>']
        if (cdir / 'lms' / f'{num:02d}.md').exists():
            links.append(f'<a href="lms/{num:02d}.html">💻 კოდი{f" · {esc(proj)}" if proj else ""}</a>')
        menu = (f'<span class="mw"><button class="more" type="button" title="გახსნა" aria-label="მენიუ">⋯</button>'
                f'<span class="menu">{"".join(links)}</span></span>') if links else ''
        body = desc
        if b.get('learn'):
            body += '<h4>🎯 რას ისწავლის სტუდენტი</h4><ul>' + ''.join(f'<li>{md_inline(x)}</li>' for x in b['learn']) + '</ul>'
        if b.get('build'):
            body += f'<h4>🛠 რას ვწერთ{f" {esc(proj)}-ში" if proj else ""}</h4><ul>' + ''.join(f'<li>{md_inline(x)}</li>' for x in b['build']) + '</ul>'
        tag = f'<span class="pj">{esc(proj)}</span>' if proj else ''
        return (f'<div class="lec{" ready" if slug else ""}" id="l-{num}"><div class="lh" role="button" tabindex="0">'
                f'<span class="chev">›</span><h3>{m.group(1)}. {title}</h3>{tag}{menu}</div>'
                f'<div class="lb">{body}</div></div>')
    h = re.sub(r'<h3>(\d+)\.\s*(.*?)</h3>\s*(<p>.*?</p>)?', lec, h, flags=re.S)
    titles = {int(a): b_ for a, b_ in re.findall(r'^### (\d+)\.\s*(.+)$', src.read_text(), re.M)}
    write_lms_pages(cdir, course, briefs, titles)
    page = (ENGINE / 'syllabus.html').read_text()
    for k, v in {'{{TITLE}}': esc(course['title']), '{{COUNT}}': str(len(re.findall(r'class="lec', h))), '{{BODY}}': h, '{{FONTS}}': FONTS,
                 '{{THEME}}': PAGE_THEME, '{{THEME_BTN}}': THEME_BTN}.items():
        page = page.replace(k, v)
    write_page(out, themeify(page))
    return True

def main(filters):
    OUT.mkdir(parents=True, exist_ok=True)
    marker = OUT / GENERATED
    if not filters and marker.exists():
        for d in marker.read_text().split():
            if (OUT / d).is_dir() and d not in ('courses', 'engine', '.git', '.github'):
                shutil.rmtree(OUT / d)
    catalog, problems = [], []
    for cdir in sorted((ROOT / 'courses').iterdir()):
        if not (cdir / 'course.json').exists():
            continue
        course = json.loads((cdir / 'course.json').read_text())
        if (cdir / 'materials').is_dir():   # კურსის საერთო გვერდები (მაგ. საფინალო პროექტი) — ღია, კოდის გარეშე
            shutil.copytree(cdir / 'materials', OUT / cdir.name / 'materials', dirs_exist_ok=True)
        lectures, prev = [], None
        for ldir in sorted(p for p in cdir.iterdir() if (p / 'deck.html').exists()):
            meta = json.loads((ldir / 'lecture.json').read_text())
            if meta.get('starts_series'):   # e.g. a guest lecture for another group: no review of the previous lecture
                prev = None
            rel = f'{cdir.name}/{ldir.name}'
            if not filters or any(f in rel for f in filters):
                info, errs = build_lecture(course, cdir, ldir, meta, prev)
                problems += errs
                if info: lectures.append(info)
            prev = {'meta': meta, 'num': int(ldir.name.split('-', 1)[0]), 'homework': md_doc(ldir / 'homework.md'),
                    'href': f'../{ldir.name}/'}
        catalog.append({'slug': cdir.name, 'title': course['title'], 'order': course.get('order', 99), 'lectures': lectures,
                        'links': course.get('links', []), 'color': course.get('color'),
                        'syllabus': write_syllabus(cdir, course)})   # extra pages (e.g. a roadmap), href relative to the course folder
    catalog.sort(key=lambda c: c['order'])
    if not filters:
        page = (ENGINE / 'index.html').read_text().replace('/*CATALOG*/[]', json.dumps(catalog, ensure_ascii=False))
        write_page(OUT / 'index.html', page)
        (OUT / '.nojekyll').write_text('')
        marker.write_text('\n'.join(c['slug'] for c in catalog) + '\n')
        print(f'index: {sum(len(c["lectures"]) for c in catalog)} lectures in {len(catalog)} courses')
    if problems:
        sys.exit('⚠ ლექციის სტრუქტურა არასრულია — იხ. ზემოთ')

if __name__ == '__main__':
    main(sys.argv[1:])
