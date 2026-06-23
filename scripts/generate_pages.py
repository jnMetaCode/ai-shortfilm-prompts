#!/usr/bin/env python3
"""Static page generator for the prompt-library showcase (SEO SSG).

Reads the repo's Markdown sources and emits one static, fully-crawlable HTML
page per file under ``docs/p/`` — content rendered into the HTML at build time
(so Google/Baidu index it), each with its own <title>/description/canonical/
hreflang/JSON-LD and a copy-prompt button. Also rewrites ``docs/sitemap.xml``.

stdlib only — no third-party deps. The DEPLOYED site stays 100% static; run
this locally and commit the output (keeps the repo's "zero build to serve"
convention intact). Usage:

    python3 scripts/generate_pages.py
"""
import os, re, glob, html as _html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
OUT  = os.path.join(DOCS, "p")
SITE = "https://prompts.aiolaola.com"
REPO = "https://github.com/jnMetaCode/ai-shortfilm-prompts"
BUILD_DATE = os.environ.get("BUILD_DATE", "2026-06-23")
PAGE_SLUGS = set()  # populated in build(); lets in-content .md links resolve to generated pages

# ── which sources become public pages ───────────────────────────────────────
PATTERNS = [
    "templates/*.md", "prompts/*.md",
    "methodology.md", "methodology.zh.md", "cases.md", "cases.zh.md",
    "faq.md", "faq.zh.md", "cheatsheet.md", "cheatsheet.zh.md",
    "skills/shortfilm-prompt/SKILL.md", "skills/shortfilm-prompt/SKILL.zh.md",
]

def sources():
    seen, out = set(), []
    for pat in PATTERNS:
        for f in sorted(glob.glob(os.path.join(ROOT, pat))):
            rel = os.path.relpath(f, ROOT)
            if os.path.basename(rel).lower().startswith("readme"):
                continue
            if rel not in seen:
                seen.add(rel); out.append(rel)
    return out

def slug_of(rel):
    base = os.path.basename(rel)
    if base.endswith(".md"):
        base = base[:-3]
    return base.lower()

def is_zh(slug):
    return slug.endswith(".zh")

def sibling_slug(slug):
    return slug[:-3] if is_zh(slug) else slug + ".zh"

# ── minimal, dependency-free Markdown → HTML (covers what our files use) ──────
def esc(s):
    return _html.escape(s, quote=False)

def inline(text):
    codes = []
    text = re.sub(r"`([^`]+)`", lambda m: codes.append(m.group(1)) or f"\x00{len(codes)-1}\x00", text)
    text = esc(text)
    def linkrepl(m):
        txt, url = m.group(1), m.group(2)
        if re.match(r"^(https?:|#|mailto:)", url):
            href = url
        elif url.endswith(".md"):
            s = os.path.basename(url)[:-3].lower()
            href = f"{s}.html" if s in PAGE_SLUGS else REPO
        else:
            href = url
        ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
        return f'<a href="{href}"{ext}>{txt}</a>'
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", linkrepl, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: "<code>" + esc(codes[int(m.group(1))]) + "</code>", text)
    return text

def render_list(buf):
    parsed = []
    for l in buf:
        if not l.strip():
            continue
        m = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", l)
        if m:
            parsed.append([len(m.group(1)), bool(re.match(r"\d+\.", m.group(2))), m.group(3)])
        elif parsed:
            parsed[-1][2] += " " + l.strip()
    if not parsed:
        return ""
    def build(i, indent):
        out = []
        ordered = None
        while i < len(parsed):
            ind, od, txt = parsed[i]
            if ind < indent:
                break
            if ind > indent:
                sub, i = build(i, ind)
                if out:
                    out[-1] = out[-1][:-5] + sub + "</li>"
                continue
            if ordered is None:
                ordered = od
            out.append("<li>" + inline(txt) + "</li>")
            i += 1
        tag = "ol" if ordered else "ul"
        return f"<{tag}>" + "".join(out) + f"</{tag}>", i
    base = min(p[0] for p in parsed)
    htmlstr, _ = build(0, base)
    return htmlstr

def convert(md):
    lines = md.split("\n")
    out, para, i, n = [], [], 0, len(md.split("\n"))
    def flush():
        if para:
            out.append("<p>" + inline(" ".join(para).strip()) + "</p>")
            para.clear()
    while i < n:
        line = lines[i]
        if line.startswith("```"):
            flush(); buf = []; i += 1
            while i < n and not lines[i].startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            out.append("<pre><code>" + esc("\n".join(buf)) + "</code></pre>")
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            flush(); lvl = len(m.group(1))
            out.append(f"<h{lvl}>" + inline(m.group(2).strip()) + f"</h{lvl}>"); i += 1; continue
        if re.match(r"^\s*([-*_])\1\1+\s*$", line):
            flush(); out.append("<hr>"); i += 1; continue
        if line.startswith(">"):
            flush(); buf = []
            while i < n and lines[i].startswith(">"):
                buf.append(lines[i][1:].lstrip()); i += 1
            out.append("<blockquote>" + convert("\n".join(buf)) + "</blockquote>"); continue
        if line.lstrip().startswith("|") and i + 1 < n and "-" in lines[i+1] \
           and re.match(r"^\s*\|?[\s:|-]+\|?\s*$", lines[i+1]):
            flush()
            def cells(r):
                r = r.strip()
                r = r[1:] if r.startswith("|") else r
                r = r[:-1] if r.endswith("|") else r
                return [c.strip() for c in r.split("|")]
            header = cells(line); i += 2; rows = []
            while i < n and lines[i].lstrip().startswith("|"):
                rows.append(cells(lines[i])); i += 1
            t = "<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in header) + "</tr></thead><tbody>"
            for r in rows:
                t += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
            out.append(t + "</tbody></table>"); continue
        if re.match(r"^\s*([-*+]|\d+\.)\s+", line):
            flush(); buf = []
            while i < n and (re.match(r"^\s*([-*+]|\d+\.)\s+", lines[i]) or
                             (lines[i].startswith((" ", "\t")) and lines[i].strip())):
                buf.append(lines[i]); i += 1
            out.append(render_list(buf)); continue
        if not line.strip():
            flush(); i += 1; continue
        para.append(line); i += 1
    flush()
    return "\n".join(out)

# ── metadata extraction ──────────────────────────────────────────────────────
def first_h1(md):
    m = re.search(r"^#\s+(.*)$", md, re.M)
    return re.sub(r"[`*]", "", m.group(1)).strip() if m else "AI 视频提示词"

def make_desc(md):
    for block in re.split(r"\n\s*\n", md):
        b = block.strip()
        if not b or b.startswith("#") or b.startswith("|") or b.startswith("```"):
            continue
        b = re.sub(r"^>\s?", "", b, flags=re.M)
        b = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", b)
        b = re.sub(r"[`*>#]", "", b)
        b = re.sub(r"\s+", " ", b).strip()
        if len(b) >= 24:
            return (b[:152] + "…") if len(b) > 153 else b
    return "电影感 AI 视频提示词模板,5 段式结构,适用 Seedance/可灵/Sora/Veo,点开即看一键复制。"

def license_of(rel):
    if rel.startswith("prompts/"):
        return ("© Mx-Shell · 保留所有权利(教育存档参考)", "")
    return ("MIT · 可自由使用", "https://opensource.org/licenses/MIT")

# ── page template ────────────────────────────────────────────────────────────
PAGE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_seo}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{site}/p/{slug}.html">
<meta name="robots" content="index, follow">
{hreflang}
<meta property="og:type" content="article">
<meta property="og:site_name" content="电影感 AI 视频提示词库">
<meta property="og:title" content="{title_og}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{site}/p/{slug}.html">
<meta property="og:locale" content="{locale}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{title_og}">
<meta name="twitter:description" content="{desc}">
<link rel="stylesheet" href="./page.css">
<script type="application/ld+json">
{jsonld}
</script>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-7LBJRDWYYW"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-7LBJRDWYYW');</script>
</head>
<body>
<header class="topbar">
  <a class="back" href="../">← 提示词库</a>
  <a class="ghlink" href="{repo}/blob/main/{src}" target="_blank" rel="noopener">在 GitHub 查看源文件 ↗</a>
</header>
<main class="doc">
  <div class="doc-actions">
    <button id="copyPrompt">⧉ 复制提示词</button>
    <button id="copyAll">复制全文</button>
    {langswitch}
  </div>
  <article class="md">
{article}
  </article>
  <footer class="doc-foot">
    <p>许可 · <a href="{license_url}" target="_blank" rel="noopener">{license_label}</a></p>
    <p><a href="../">← 回提示词库</a> · <a href="https://www.aiolaola.com/?utm_source=prompts.aiolaola.com&amp;utm_medium=referral&amp;utm_campaign=docpage" target="_blank" rel="noopener">aiOlaOla 学 AI 编程</a></p>
  </footer>
</main>
<div class="toast" id="toast"></div>
<script>
const RAW = {raw_json};
function extractPrompt(md){{
  const lines=md.split("\\n");
  const re=/^#{{1,4}}\\s.*(完整提示词|complete prompt|copy-paste|可直接复制)/i;
  let s=-1; for(let i=0;i<lines.length;i++){{if(re.test(lines[i])){{s=i+1;break;}}}}
  if(s>=0){{let e=lines.length;for(let i=s;i<lines.length;i++){{if(/^##\\s/.test(lines[i])){{e=i;break;}}}}
    const r=lines.slice(s,e).join("\\n").replace(/^\\s*-{{3,}}\\s*$/gm,"").trim();if(r)return r;}}
  const b=[...md.matchAll(/```[^\\n]*\\n([\\s\\S]*?)```/g)].map(m=>m[1].trim());
  return b.length?b.join("\\n\\n"):md.trim();
}}
function toast(t){{const e=document.getElementById('toast');e.textContent=t;e.classList.add('show');
  clearTimeout(toast._t);toast._t=setTimeout(()=>e.classList.remove('show'),1700);}}
async function cp(t,msg){{try{{await navigator.clipboard.writeText(t);toast(msg);}}catch(e){{toast('复制失败');}}}}
document.getElementById('copyPrompt').onclick=()=>cp(extractPrompt(RAW),'提示词已复制 · 可直接粘进视频模型');
document.getElementById('copyAll').onclick=()=>cp(RAW,'全文已复制');
</script>
</body>
</html>
"""

def jsonld_for(rel, title, desc, slug, lang, lic_url):
    import json
    obj = {
        "@context": "https://schema.org",
        "@type": "HowTo" if "methodology" in rel else "CreativeWork",
        "name": title,
        "description": desc,
        "inLanguage": lang,
        "url": f"{SITE}/p/{slug}.html",
        "isPartOf": {"@type": "WebSite", "name": "电影感 AI 视频提示词库", "url": SITE + "/"},
        "author": {"@type": "Person", "name": "jnMetaCode", "url": "https://github.com/jnMetaCode"},
    }
    if lic_url:
        obj["license"] = lic_url
    return json.dumps(obj, ensure_ascii=False, indent=2)

def build():
    import json
    os.makedirs(OUT, exist_ok=True)
    srcs = sources()
    slugs = {slug_of(s) for s in srcs}
    global PAGE_SLUGS
    PAGE_SLUGS = slugs
    pages = []
    meta = []
    for rel in srcs:
        with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
            md = f.read()
        slug = slug_of(rel)
        zh = is_zh(slug)
        lang = "zh-CN" if zh else "en"
        locale = "zh_CN" if zh else "en_US"
        title = first_h1(md)
        desc = make_desc(md).replace('"', "'")
        title_seo = f"{title}｜电影感 AI 视频提示词库" if zh else f"{title} | Cinematic AI Video Prompt Library"
        lic_label, lic_url = license_of(rel)
        sib = sibling_slug(slug)
        hreflang = ""
        if sib in slugs:
            other = "en" if zh else "zh-CN"
            hreflang = (f'<link rel="alternate" hreflang="{lang}" href="{SITE}/p/{slug}.html">\n'
                        f'<link rel="alternate" hreflang="{other}" href="{SITE}/p/{sib}.html">')
        langswitch = (f'<a class="langsw" href="./{sib}.html">{"EN" if zh else "中文"}</a>'
                      if sib in slugs else "")
        article = convert(md)
        page = PAGE.format(
            lang=lang, locale=locale, title_seo=esc(title_seo), title_og=esc(title),
            desc=esc(desc), site=SITE, slug=slug, hreflang=hreflang,
            jsonld=jsonld_for(rel, title, desc, slug, lang, lic_url),
            repo="https://github.com/jnMetaCode/ai-shortfilm-prompts", src=rel,
            langswitch=langswitch, article=article,
            license_label=esc(lic_label), license_url=lic_url or (SITE + "/"),
            raw_json=json.dumps(md, ensure_ascii=False),
        )
        with open(os.path.join(OUT, slug + ".html"), "w", encoding="utf-8") as f:
            f.write(page)
        pages.append(slug)
        meta.append((slug, title, rel))
    write_index(meta)
    write_sitemap(pages)
    print(f"✓ generated {len(pages)} pages → docs/p/  + index.html + sitemap.xml")
    return pages

def write_index(meta):
    groups = [("模板库", lambda r: r.startswith("templates/")),
              ("Mx-Shell 原始提示词(存档)", lambda r: r.startswith("prompts/")),
              ("方法论 · 案例 · FAQ · Skill", lambda r: True)]
    used = set()
    sections = []
    for gtitle, pred in groups:
        items = []
        for slug, title, rel in meta:
            if slug in used or not pred(rel):
                continue
            used.add(slug)
            items.append(f'      <li><a href="./{slug}.html">{esc(title)}</a></li>')
        if items:
            sections.append(f"    <h2>{gtitle}</h2>\n    <ul class=\"idx\">\n" + "\n".join(items) + "\n    </ul>")
    body = "\n".join(sections)
    doc = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>全部提示词索引｜电影感 AI 视频提示词库</title>
<meta name="description" content="电影感 AI 视频提示词库的全部模板、方法论与存档提示词索引,适用 Seedance/可灵/Sora/Veo,点开即看一键复制。">
<link rel="canonical" href="{SITE}/p/">
<meta name="robots" content="index, follow">
<link rel="stylesheet" href="./page.css">
</head>
<body>
<header class="topbar"><a class="back" href="../">← 提示词库首页</a>
  <a class="ghlink" href="{REPO}" target="_blank" rel="noopener">GitHub ↗</a></header>
<main class="doc">
  <article class="md">
    <h1>全部提示词 · 索引</h1>
    <p>电影感 AI 视频提示词库的完整清单。点任意一条看全文、一键复制。</p>
{body}
  </article>
</main>
</body>
</html>
"""
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)

def write_sitemap(pages):
    urls = [f"  <url><loc>{SITE}/</loc><lastmod>{BUILD_DATE}</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>",
            f"  <url><loc>{SITE}/p/</loc><lastmod>{BUILD_DATE}</lastmod><changefreq>weekly</changefreq><priority>0.9</priority></url>"]
    for slug in pages:
        urls.append(f"  <url><loc>{SITE}/p/{slug}.html</loc><lastmod>{BUILD_DATE}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(urls) + "\n</urlset>\n")
    with open(os.path.join(DOCS, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)

if __name__ == "__main__":
    build()
