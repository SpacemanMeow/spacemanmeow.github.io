#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全站校验门禁 — 单一权威副本（按维度分类）。

用法（仓库根目录）：python3 scripts/site_audit.py
执行前需先完成构建，否则产物类规则会跳过；CI 的 `Audit site` 步骤调用本脚本。
FAIL 退出码 1；WARN 不阻断但会在报告中单列。

扩展规则：在对应维度的 check_*() 函数内新增 a.chk(...)，并同步
seo/SITE-AUDIT.md §3/§4 的同一维度小节。禁止在维度外散落 chk 调用。
"""
import os, re, glob, subprocess, collections, unicodedata

# ---------------------------------------------------------------------------
# 维度注册表：新增维度须同时在此登记 + 写 check_*() + 更新文档 §3/§4
# ---------------------------------------------------------------------------
DIMS = [
    ('BLD',     '构建与产物'),
    ('I18N',    '多语言一致性'),
    ('META',    '元数据与结构化数据'),
    ('CONTENT', '内容质量与 SEO'),
    ('LINK',    '链接与导航'),
    ('A11Y',    '可访问性与媒体'),
    ('DESIGN',  '设计系统与样式一致性'),
    ('HYGIENE', '运维与清洁度'),
]

BASE = {}  # 已知欠账登记；当前为空表示所有规则均为硬门禁


class Auditor:
    def __init__(self):
        self.rows = []
        self.counts = collections.defaultdict(collections.Counter)

    def add(self, level, dim, rid, name, detail=''):
        self.rows.append((dim, rid, level, name, detail))
        self.counts[dim][level] += 1

    def chk(self, dim, rid, name, ok, detail=''):
        self.add('PASS' if ok else 'FAIL', dim, rid, name, detail)

    def warn(self, dim, rid, name, detail=''):
        self.add('WARN', dim, rid, name, detail)

    def total(self):
        c = collections.Counter(r[2] for r in self.rows)
        return dict(c)

    def report(self):
        print('=' * 78)
        print(' 全站校验报告  /  Site Audit')
        print(f' 语言 {LANGS}   完整 {FULL}   分批中 {PARTIAL}')
        print('=' * 78)
        for code, title in DIMS:
            c = self.counts[code]
            if not c:
                continue
            print(f'\n[{code}] {title}   PASS {c["PASS"]} / FAIL {c["FAIL"]} / WARN {c["WARN"]}')
            for dim, rid, lv, name, detail in self.rows:
                if dim == code:
                    print(f'  {rid:16s} {lv:4s}  {name}' + (f'  — {detail}' if detail else ''))
        t = self.total()
        n = sum(t.values())
        print('\n' + '=' * 78)
        print(f' 汇总  PASS {t.get("PASS", 0)} / FAIL {t.get("FAIL", 0)} / WARN {t.get("WARN", 0)}  '
              f'(共 {n} 项 / {len([d for d, _ in DIMS if self.counts[d]])} 维度)')
        print('=' * 78)


# ---------------------------------------------------------------------------
# 共享上下文：一次加载，所有维度函数复用
# ---------------------------------------------------------------------------
def fs(p): return sorted(glob.glob(p, recursive=True))
def nm(p): return {os.path.basename(x) for x in fs(p)}
def fm(t):
    if not t.startswith('---'): return {}
    e = t.find('\n---', 3)
    if e < 0: return {}
    d = {}
    for l in t[3:e].split('\n'):
        m = re.match(r'^([A-Za-z_][A-Za-z_0-9]*):\s*(.*)$', l)
        if m: d[m.group(1)] = m.group(2).strip()
    return d
def norm(s): return s.lower().replace(' ', '').replace('\t', '').replace('**', '').replace('　', '')

LANGS = ['en']
for _f in sorted(glob.glob('_config_*.yml')):
    _m = re.match(r'_config_([a-z]{2})\.yml$', os.path.basename(_f))
    if _m and _m.group(1) not in LANGS: LANGS.append(_m.group(1))
LANGS = ['en'] + sorted(LANGS[1:])

def dirs(L):
    if L == 'en':
        return dict(posts='_posts', pages='_pages', apps='_apps',
                    gloss='_glossary', rel='_release_notes')
    return dict(posts='_posts/' + L, pages='_pages/' + L,
                apps='_apps_' + L, gloss='_glossary_' + L, rel='_release_notes_' + L)

def lang_of(f):
    for L in LANGS[1:]:
        if any(f.startswith(d + '/') for d in dirs(L).values()): return L
    return 'en'

MDS = sorted(set(sum((fs(d + '/**/*.md') for L in LANGS
                      for d in dirs(L).values()), [])))
TXT = {f: open(f, encoding='utf-8').read() for f in MDS}
FMS = {f: fm(t) for f, t in TXT.items()}
EN_POSTS = nm('_posts/*.md')
FULL = [L for L in LANGS[1:] if nm(dirs(L)['posts'] + '/*.md') == EN_POSTS]
PARTIAL = [L for L in LANGS[1:] if L not in FULL]
HAS_SITE = os.path.isdir('_site')

STRUCT = ['index', 'meow', 'about', 'privacy', 'terms',
          'search', 'tags', 'glossary', 'docs', 'faq']
CANON_PRODUCT = {'Meow Todo', 'Meow Habits', 'Meow Money', 'Meow Mood Diary',
                 'Meow FM', 'Only Clock', 'One Widget', 'Crosshair Aim',
                 'System Monitor', 'CPU Monitor', 'Floating Assistant'}
BRAND_PREFIX = ('Meow', 'Only Clock', 'One Widget', 'Crosshair Aim',
                'System Monitor', 'CPU Monitor', 'Floating Assistant')
REL_LABEL = {'en': 'Release Notes', 'zh': '更新日志', 'id': 'Catatan Rilis',
             'ms': 'Nota Keluaran', 'th': 'บันทึกการอัปเดต'}


# ---------------------------------------------------------------------------
# BLD 构建与产物
# ---------------------------------------------------------------------------
def check_bld(a):
    a.chk('BLD', 'BLD-01', '语言清单与完成度（至少 5 语）', len(LANGS) >= 5,
          f'LANGS={LANGS} 完整={FULL} 分批中={PARTIAL}')
    if not HAS_SITE:
        a.warn('BLD', 'BLD-02', '产物未构建', '请先运行 bash scripts/build.sh；产物类规则已跳过')
        return
    feeds = ['_site/feed.xml'] + ['_site/' + L + '/feed.xml' for L in LANGS[1:]]
    a.chk('BLD', 'BLD-03', 'feed / robots 存在',
          all(os.path.exists(x) for x in feeds) and os.path.exists('_site/robots.txt'),
          ','.join(feeds))
    a.chk('BLD', 'BLD-04', 'Pagefind 索引存在',
          os.path.isfile('_site/pagefind/pagefind.js'), '')
    temps = ['.jekyll-' + L for L in LANGS[1:] if os.path.isdir('.jekyll-' + L)]
    a.chk('BLD', 'BLD-05', '无临时目录残留', not temps, f'{temps}')


# ---------------------------------------------------------------------------
# I18N 多语言一致性
# ---------------------------------------------------------------------------
def check_i18n(a):
    labels = re.findall(r'^\s+label:\s*(.+?)\s*$',
                        open('_data/languages.yml', encoding='utf-8').read(), re.M)
    rm = re.search(r'^## 语言[ \t]*\n(.*?)(?=^## |\Z)',
                   open('README.md', encoding='utf-8').read(), re.M | re.S)
    seg = rm.group(1) if rm else ''
    miss = [x for x in labels if x not in seg]
    cn = {1:'一',2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九',10:'十',11:'十一',12:'十二'}
    num = cn.get(len(labels), str(len(labels)))
    a.chk('I18N', 'I18N-01', 'README 语言清单与 languages.yml 一致',
          bool(labels) and not miss and (f'{num}个语言版本' in seg),
          f' languages.yml {len(labels)} 语；README 缺失 {miss}；应为「{num}个语言版本」')

    empty = [(L, k) for L in LANGS[1:] for k in ('apps', 'gloss')
             if not fs(dirs(L)[k] + '/*.md')]
    a.chk('I18N', 'I18N-02', '各语言集合非空（防 site[coll] 静默失败）', not empty, f'空集合 {empty}')

    for lab, key in [('文章','posts'), ('应用','apps'), ('页面','pages'), ('术语','gloss')]:
        base = nm(dirs('en')[key] + '/*.md')
        for L in FULL:
            other = nm(dirs(L)[key] + '/*.md')
            a.chk('I18N', f'I18N-03/{key}/{L}', f'{lab} EN/{L} 一一对应', base == other,
                  f'EN={len(base)} {L}={len(other)} 差集={len(base ^ other)}')
        for L in PARTIAL:
            other = nm(dirs(L)[key] + '/*.md')
            orphan = other - base
            a.chk('I18N', f'I18N-04/{key}/{L}', f'{lab} {L} 无孤立文件', not orphan,
                  f'{L} {len(other)}/{len(base)}，孤立 {len(orphan)}')

    for L in FULL:
        have = nm(dirs(L)['pages'] + '/*.md')
        m = [s for s in STRUCT if (s + '.md') not in have]
        a.chk('I18N', f'I18N-05/{L}', f'结构页 {len(STRUCT)}/{len(STRUCT)} ({L})', not m,
              f'缺失 {m}（致 htmlproofer 断链；须同源补齐）')

    if not HAS_SITE: return
    htmls = {h: open(h, encoding='utf-8').read() for h in fs('_site/**/*.html')}
    pages = {h:v for h,v in htmls.items() if os.path.basename(h) != '404.html'}
    a.chk('I18N', 'I18N-06', '每页 hreflang 块',
          all('i18n-hreflang' in v for v in pages.values()), f'{len(pages)} 页')
    missxd = [h for h,v in pages.items()
              if 'hreflang="en"' not in v or 'hreflang="x-default"' not in v]
    a.chk('I18N', 'I18N-07', 'hreflang en + x-default 完整', not missxd, f'异常 {len(missxd)}')
    cnt = collections.Counter(len(re.findall(r'hreflang="[^"]+"', v)) for v in pages.values())
    a.chk('I18N', 'I18N-08', 'hreflang 条数随组内语言数变化',
          min(cnt) >= 2 and max(cnt) <= len(LANGS) + 1, f'分布 {dict(cnt)}')
    for L in LANGS[1:]:
        lp = '_site/' + L + '/'
        sub = [h for h in pages if h.startswith(lp)]
        bad = [h for h in sub if 'hreflang="' + L + '"' not in htmls[h]]
        a.chk('I18N', f'I18N-09/{L}', f'{L} 页含自身 alternate', not bad,
              f'{len(sub)} 页，异常 {len(bad)}')
        a.chk('I18N', f'I18N-10/{L}', f'{L} 子 sitemap 已删',
              not os.path.exists(lp + 'sitemap.xml'), '')
    sm = open('_site/sitemap.xml', encoding='utf-8').read() if os.path.exists('_site/sitemap.xml') else ''
    a.chk('I18N', 'I18N-11', '合并 sitemap 非空', len(re.findall(r'<loc>', sm)) > 0,
          f'{len(re.findall(r"<loc>", sm))} 条 loc')

    # 骨架与插图跨语言对等（原 D17/D18）
    IMGSET = re.compile(r'!\[([^\]]*)\]\((/assets/images/[^)]+)\)')
    TOCRE = re.compile(r'^- \[[^\]]+\]\(#[^)]+\)$')
    def skel(l):
        x = l.strip()
        for p, k in (('### ','H3'),('## ','H2'),('![','IMG'),('|','TBL'),('- ','LI')):
            if x.startswith(p): return k
        if re.match(r'^\d+\. ', x): return 'NUM'
        if x == '{:.faq-q}': return 'FAQ'
        if x == '---': return 'HR'
        return None
    enmap = {os.path.basename(f): f for f in fs('_posts/[12]*.md')}
    mis, copied, pos, hbad, sbad, tbad = [], [], [], [], [], []
    for f, t in TXT.items():
        if lang_of(f) == 'en' or not f.startswith('_posts/'): continue
        e = enmap.get(os.path.basename(f))
        if not e: continue
        ec = collections.Counter(p for _,p in IMGSET.findall(TXT[e]))
        tc = collections.Counter(p for _,p in IMGSET.findall(t))
        if ec != tc: mis.append((f, sum(ec.values()), sum(tc.values())))
        el, tl = TXT[e].split('\n'), t.split('\n')
        ea = [i for i,l in enumerate(el) if IMGSET.search(l)]
        ba = [i for i,l in enumerate(tl) if IMGSET.search(l)]
        if ea != ba: pos.append((f, ea[:3], ba[:3]))
        es = [k for k in (skel(l) for l in el) if k]
        ts = [k for k in (skel(l) for l in tl) if k]
        if es != ts: sbad.append((f, len(es), len(ts)))
        eh = [k for k in es if k in ('H2','H3')]
        th = [k for k in ts if k in ('H2','H3')]
        if eh != th: hbad.append((f, len(eh), len(th)))
        etoc = [i for i,l in enumerate(el) if TOCRE.match(l)]
        ttoc = [i for i,l in enumerate(tl) if TOCRE.match(l)]
        if etoc != ttoc: tbad.append((f, etoc[:3], ttoc[:3]))
        alts = {x[0] for x in IMGSET.findall(TXT[e])}
        hit = [x[0] for x in IMGSET.findall(t) if x[0] in alts]
        if hit: copied.append((f, hit[0]))
    a.chk('I18N', 'I18N-12', '文章插图集合与 EN 一致', not mis, f'{len(mis)} 篇 {mis[:2]}')
    a.chk('I18N', 'I18N-13', '插图行序位置与 EN 一致', not pos, f'{len(pos)} 篇 {pos[:2]}')
    a.chk('I18N', 'I18N-14', '插图 alt 已本地化（未照抄 EN）', not copied, f'{len(copied)} 篇 {copied[:2]}')
    a.chk('I18N', 'I18N-15', '文章 H2/H3 层级序列与 EN 一致', not hbad, f'{len(hbad)} 篇 {hbad[:2]}')
    a.chk('I18N', 'I18N-16', '文章结构块序列与 EN 一致', not sbad, f'{len(sbad)} 篇 {sbad[:2]}')
    a.chk('I18N', 'I18N-17', '文章目录（TOC）与 EN 一致', not tbad, f'{len(tbad)} 篇 {tbad[:2]}')
    a.chk('I18N', 'I18N-18', '图片插入行序与 EN 一致', not pos, f'{len(pos)} 篇 {pos[:2]}')

    # tagline 信息量与显示宽度
    def tagline(f):
        for l in open(f, encoding='utf-8').read().split('\n'):
            if l.startswith('tagline:'):
                return re.sub(r'\s+#\s.*$', '', l[len('tagline:'):].strip()).strip()
        return ''
    tbad2 = []
    for L in LANGS[1:]:
        for f in fs(dirs(L)['apps'] + '/*.md'):
            en = '_apps/' + os.path.basename(f)
            if not os.path.isfile(en): continue
            x, y = tagline(en), tagline(f)
            if not x or not y:
                tbad2.append((f, 'tagline 缺失')); continue
            ratio = len(y) / max(len(x), 1)
            extra = set(re.findall(r'\d+', y)) - set(re.findall(r'\d+', x))
            if ratio > 1.5 or extra:
                tbad2.append((f, f'长度比 {ratio:.2f} 规格数字增补 {sorted(extra)}'))
    a.chk('I18N', 'I18N-19', 'App tagline 信息量与 EN 对等', not tbad2,
          f'异常 {len(tbad2)} {tbad2[:2]}')
    def w(s): return sum(2 if unicodedata.east_asian_width(c) in 'WF' else 1 for c in s)
    def cfg_tag(f):
        for l in open(f, encoding='utf-8').read().split('\n'):
            if l.startswith('tagline:'):
                return re.sub(r'\s+#\s.*$', '', l[len('tagline:'):].strip()).strip().strip('"')
        return ''
    cfgs = ['_config.yml'] + ['_config_%s.yml' % L for L in LANGS[1:]]
    widths = {f: w(cfg_tag(f)) for f in cfgs if os.path.isfile(f)}
    enw = widths.get('_config.yml', 0)
    twbad = [(f, v) for f,v in widths.items() if v > 60 or (f != '_config.yml' and v > enw)]
    a.chk('I18N', 'I18N-20', '站点 tagline 宽度（w≤60，非 EN ≤ EN）', not twbad,
          f'EN w={enw}，异常 {twbad}')


# ---------------------------------------------------------------------------
# META 元数据与结构化数据
# ---------------------------------------------------------------------------
def check_meta(a):
    need = {'title','description'}
    bad = []
    for f, d in FMS.items():
        if re.match(r'^_release_notes(_[a-z]{2})?/', f): continue
        n = set(need)
        if f.startswith('_posts/'): n |= {'date','layout','tags','image'}
        if re.match(r'^_apps(_[a-z]{2})?/', f): n.add('icon')
        if f.startswith('_pages/'): n.add('permalink')
        if n - set(d): bad.append((f, ','.join(sorted(n - set(d)))))
    a.chk('META', 'META-01', 'frontmatter 必填字段', not bad, f'异常 {len(bad)} {bad[:2]}')
    langbad = [f for f,d in FMS.items() if d.get('lang') != lang_of(f)]
    a.chk('META', 'META-02', 'lang 存在且与目录一致', not langbad, f'异常 {len(langbad)} {langbad[:2]}')
    longs, amps = [], []
    for f, d in FMS.items():
        v = d.get('description','')
        if v.startswith(('>-','>','|')): continue
        s = v.strip('"')
        if len(s) > 160: longs.append((f, len(s)))
        if '&' in s: amps.append(f)
    a.chk('META', 'META-03', 'description ≤160 字符', not longs, f'超长 {len(longs)} {longs[:2]}')
    a.chk('META', 'META-04', 'description 无裸 &', not amps, f'{len(amps)} 处')

    rb = '''require 'yaml'
bad=[]
Dir.glob('{_posts,_apps,_apps_*,_pages,_glossary,_glossary_*}/**/*.{md,html}').each do |f|
 t=File.read(f); next unless t.start_with?("---\\n"); e=t.index("\\n---",4); next unless e
 begin; YAML.parse(t[4,e-4]); rescue StandardError=>ex; bad << f+': '+ex.message.lines.first.to_s.strip; end
end
puts bad.join("\\n")
'''
    r = subprocess.run(['ruby','-ryaml','-e',rb], capture_output=True, text=True)
    if r.returncode != 0:
        a.warn('META', 'META-05', 'YAML 校验器不可用', r.stderr[:120])
    else:
        badyaml = [l for l in r.stdout.strip().split('\n') if l]
        a.chk('META', 'META-05', 'frontmatter YAML 语法有效', not badyaml,
              f'异常 {len(badyaml)} {badyaml[:2]}')

    if HAS_SITE:
        htmls = [open(h, encoding='utf-8').read() for h in fs('_site/**/*.html')]
        ld = [b for v in htmls for b in re.findall(
            r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', v, re.S)]
        a.chk('META', 'META-06', 'JSON-LD 无 &amp; 污染',
              not any('&amp;' in b for b in ld), f'{len(ld)} 个块')


# ---------------------------------------------------------------------------
# CONTENT 内容质量与 SEO
# ---------------------------------------------------------------------------
def check_content(a):
    h2, sp, weak = [], [], []
    for f, t in TXT.items():
        if re.search(r'(?<=[\u4e00-\u9fff])[ \t]+(?=[\u4e00-\u9fff])', t): sp.append(f)
    for n in EN_POSTS:
        x = len(re.findall(r'^## ', TXT['_posts/' + n], re.M))
        for L in FULL:
            z = dirs(L)['posts'] + '/' + n
            if os.path.exists(z):
                y = len(re.findall(r'^## ', TXT[z], re.M))
                if x != y: h2.append((n, L, x, y))
    a.chk('CONTENT', 'CONTENT-01', '完整语言 H2 数量一致', not h2, f'不一致 {len(h2)} {h2[:2]}')
    for L in PARTIAL:
        for f in fs(dirs(L)['posts'] + '/*.md'):
            c = len(re.findall(r'^## ', TXT[f], re.M))
            if c < 4 or '{:.faq-q}' not in TXT[f]: weak.append((f, c))
    a.chk('CONTENT', 'CONTENT-02', '分批语言文章结构完整（H2≥4 且含 FAQ）', not weak,
          f'异常 {len(weak)} {weak[:2]}')
    a.chk('CONTENT', 'CONTENT-03', '无汉字间多余空格', not sp, f'残留 {len(sp)} {sp[:2]}')

    kw = open('seo/SEO-KEYWORDS.md', encoding='utf-8').read().split('\n')
    sec, terms = None, collections.defaultdict(set)
    for l in kw:
        m = re.match(r'^## (2\.\d+) ', l)
        if m: sec = m.group(1); continue
        if l.startswith('## 3.'): sec = None; continue
        if sec is None or not l.startswith('|') or l.startswith('|---'): continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) >= 7 and c[0] != '关键词' and '已覆盖' in c[6]:
            for word in c[0].split('/'): terms[sec].add(word.strip())
        if len(c) == 4 and '已覆盖' in c[3]:
            for word in c[1].split('/'): terms[sec].add(word.strip())
    blob = norm('\n'.join(TXT.values()))
    miss = sorted(w for v in terms.values() for w in v if w and norm(w) not in blob)
    a.chk('CONTENT', 'CONTENT-04', '全部关键词真实覆盖',
          not miss and len(terms) >= 11, f'{len(terms)} 组，MISS {len(miss)} {miss[:3]}')

    badvar, noprod = [], []
    for f, d in FMS.items():
        if not f.startswith('_posts/'): continue
        raw = d.get('tags','')
        m = re.match(r'\[(.*)\]', raw)
        tags = [x.strip() for x in m.group(1).split(',') if x.strip()] if m else []
        for tg in tags:
            if tg in ('Meow Mood','Meow Todo List','To Do List') or \
               (tg.startswith(BRAND_PREFIX) and tg not in CANON_PRODUCT):
                badvar.append((f, tg))
        if not (set(tags) & CANON_PRODUCT): noprod.append(f)
    a.chk('CONTENT', 'CONTENT-05', 'tags 无产品标签变体', not badvar, f'异常 {len(badvar)} {badvar[:2]}')
    a.chk('CONTENT', 'CONTENT-06', '每篇至少带规范产品标签', not noprod, f'缺失 {len(noprod)} {noprod[:2]}')

    rmiss, rbad, rempty, rtitle, rstore = [], [], [], [], []
    for L in LANGS:
        apps = nm(dirs(L)['apps'] + '/*.md')
        rels = nm(dirs(L)['rel'] + '/*.md')
        for s in apps:
            if s not in rels: rmiss.append((L, s))
        prefix = '_release_notes' if L == 'en' else '_release_notes_' + L
        for f, d in FMS.items():
            if not f.startswith(prefix + '/'): continue
            need = {'layout','app_slug','app_title','google_play','app_store','lang','title'}
            if need - set(d): rbad.append((f, ','.join(sorted(need - set(d)))))
            if not re.search(r'^\d+\.\s+\S', TXT[f], re.M): rempty.append(f)
            if REL_LABEL.get(L, 'Release Notes') not in d.get('title',''): rtitle.append(f)
            if re.search(r'^app_store:[ \t]*$', TXT[f], re.M): rstore.append(f)
    a.chk('CONTENT', 'CONTENT-07', '每 App 均有 Release Note 页（全语言）', not rmiss, f'缺失 {len(rmiss)} {rmiss[:2]}')
    a.chk('CONTENT', 'CONTENT-08', 'Release Note frontmatter 完整', not rbad, f'异常 {len(rbad)} {rbad[:2]}')
    a.chk('CONTENT', 'CONTENT-09', 'Release Note 正文含发布记录', not rempty, f'空 {len(rempty)} {rempty[:2]}')
    a.chk('CONTENT', 'CONTENT-10', 'Release Note 标题含本地化后缀', not rtitle, f'异常 {len(rtitle)} {rtitle[:2]}')
    a.chk('CONTENT', 'CONTENT-11', 'Release Note 无裸 app_store 空值行', not rstore, f'异常 {len(rstore)} {rstore[:2]}')


# ---------------------------------------------------------------------------
# LINK 链接与导航
# ---------------------------------------------------------------------------
def check_link(a):
    def links(t): return re.findall(r'\]\((/[^)]*)\)', t)
    zbad, ebad = [], []
    for f, t in TXT.items():
        L = lang_of(f)
        for u in links(t):
            if u.startswith(('/assets/','/pagefind/')): continue
            if L == 'en' and any(u.startswith('/' + x + '/') for x in LANGS[1:]): ebad.append((f,u))
            if L != 'en' and not u.startswith('/' + L + '/'): zbad.append((f,u))
    a.chk('LINK', 'LINK-01', '内链语言前缀', not zbad and not ebad,
          f'非 EN 缺前缀 {len(zbad)} {zbad[:2]} / EN 误带 {len(ebad)} {ebad[:2]}')
    nav = open('_data/nav.yml', encoding='utf-8').read()
    tpl = ''.join(open(f, encoding='utf-8').read() for f in fs('_layouts/*.html') + fs('_includes/*.html'))
    a.chk('LINK', 'LINK-02', '形态间内链入口闭合',
          'nav: docs' in nav and 'docs-hub' in tpl, 'docs 导航项或 docs-hub 模板入口缺失')
    app_tpl = open('_layouts/app.html', encoding='utf-8').read()
    a.chk('LINK', 'LINK-03', 'App 详情页含 Release Note 内链',
          'release-notes/' in app_tpl, 'app.html 缺内链')


# ---------------------------------------------------------------------------
# A11Y 可访问性与媒体
# ---------------------------------------------------------------------------
def check_a11y(a):
    IMGRE = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)\s*(\{:[^}]*\})?')
    dup, gen, missing, nowidth, total = [], [], [], [], 0
    for f, t in TXT.items():
        imgs = IMGRE.findall(t)
        if len(imgs) != len(set(x[0] for x in imgs)): dup.append(f)
        if re.search(r'!\[image\]', t, re.I): gen.append(f)
        for alt, p, attr in imgs:
            if p.startswith('/assets/'):
                total += 1
                if not os.path.exists('.' + p): missing.append((f, p))
                if not attr or not re.search(r'width\s*=', attr): nowidth.append((f, p))
    a.chk('A11Y', 'A11Y-01', '同文件 alt 唯一', not dup, f'重复 {len(dup)} {dup[:2]}')
    a.chk('A11Y', 'A11Y-02', '无 ![image] 残留', not gen, f'{len(gen)}')
    a.chk('A11Y', 'A11Y-03', '引用图片文件存在', not missing, f'缺失 {len(missing)} {missing[:2]}')
    a.chk('A11Y', 'A11Y-04', '图片 width 覆盖（防 CLS）', total > 0 and not nowidth,
          f'{total} 处引用，缺 width {len(nowidth)} {nowidth[:2]}')


# ---------------------------------------------------------------------------
# DESIGN 设计系统与样式一致性
# ---------------------------------------------------------------------------
def check_design(a):
    css = open('assets/css/main.css', encoding='utf-8').read()
    clean = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    fs_set = {'--fs-sm','--fs-base','--fs-md','--fs-xl','--fs-2xl','--fs-3xl'}
    defined_fs = set(re.findall(r'(--fs-[\w-]+)\s*:', css))
    a.chk('DESIGN', 'DESIGN-01', '字号变量仅保留 6 档标准', defined_fs == fs_set,
          f'定义={sorted(defined_fs)} 期望={sorted(fs_set)}')
    hard_fs = [v.strip() for v in re.findall(r'font-size\s*:\s*([^;]+)', clean)
               if 'var(--fs-' not in v]
    a.chk('DESIGN', 'DESIGN-02', '无硬编码字号', not hard_fs, f'{len(hard_fs)} 处 {hard_fs[:5]}')
    fw_set = {'--fw-head','--fw-bold','--fw-body'}
    defined_fw = set(re.findall(r'(--fw-[\w-]+)\s*:', css))
    a.chk('DESIGN', 'DESIGN-03', '字重变量仅保留 3 档标准', defined_fw == fw_set,
          f'定义={sorted(defined_fw)} 期望={sorted(fw_set)}')
    hard_fw = [v.strip() for v in re.findall(r'font-weight\s*:\s*([^;]+)', clean)
               if 'var(--fw-' not in v]
    a.chk('DESIGN', 'DESIGN-04', '无硬编码字重', not hard_fw, f'{len(hard_fw)} 处 {hard_fw[:5]}')

    srcs = []
    for pat in ('**/*.css','**/*.html','**/*.liquid','**/*.py','**/*.js'):
        srcs += [p for p in fs(pat) if not re.search(
            r'(^|/)(_site|_site_en|_site_zh|\.jekyll-[^/]*|node_modules|\.git|\.pagefind-bin|\.sass-cache)/', p)]
    inline = []
    for p in set(srcs):
        try: t = open(p, encoding='utf-8').read()
        except Exception: continue
        for m in re.finditer(r'font-size\s*:\s*([^;}"\']+)', t):
            if 'var(--fs-' not in m.group(1): inline.append((p, 'size', m.group(1).strip()))
        for m in re.finditer(r'font-weight\s*:\s*([^;}"\']+)', t):
            if 'var(--fw-' not in m.group(1): inline.append((p, 'weight', m.group(1).strip()))
    a.chk('DESIGN', 'DESIGN-05', '全仓源文件无硬编码字号/字重', not inline,
          f'{len(inline)} 处 {inline[:5]}')
    tokens = ['--divider-dashed','--divider-solid','--space-1','--space-9',
              '--radius-sm','--radius-xl','--shadow-card','--shadow-soft']
    mt = [t for t in tokens if not re.search(re.escape(t) + r'\s*:', css)]
    a.chk('DESIGN', 'DESIGN-06', '统一令牌齐备（分割线/间距/圆角/阴影）', not mt, f'缺失 {mt}')
    borders = re.findall(r'border(?:-top|-bottom|-left|-right)?\s*:\s*([^;]+)', clean)
    hexb = [v.strip() for v in borders if re.search(r'#[0-9a-fA-F]{3,8}\b', v)]
    a.chk('DESIGN', 'DESIGN-07', '分割线颜色无硬编码', not hexb, f'{len(hexb)} 处 {hexb[:5]}')
    a.chk('DESIGN', 'DESIGN-08', '商店按钮为共享 include（单一来源）',
          bool(fs('_includes/store-buttons.html')), '_includes/store-buttons.html')


# ---------------------------------------------------------------------------
# HYGIENE 运维与清洁度
# ---------------------------------------------------------------------------
def check_hygiene(a):
    if HAS_SITE:
        sm = open('_site/sitemap.xml', encoding='utf-8').read() if os.path.exists('_site/sitemap.xml') else ''
        a.chk('HYGIENE', 'HYGIENE-01', '404 不进 sitemap', '404' not in sm, '')
        a.chk('HYGIENE', 'HYGIENE-02', '内部 seo/ 未发布', not os.path.isdir('_site/seo'), '')
        leaks = [p for p in fs('_site/**/*') if any(k in p for k in
                 ('credentials.json','token.json','pagefind-bin')
                 + tuple('jekyll-' + L for L in LANGS[1:]))]
        a.chk('HYGIENE', 'HYGIENE-03', '无凭据/缓存文件泄漏', not leaks, f'{len(leaks)} 个')
    st = subprocess.run(['git','status','--short'], capture_output=True, text=True).stdout.split('\n')
    def approved(l):
        return any(k in l for L in LANGS[1:] for k in
                   ('_posts/'+L+'/', '_pages/'+L+'/', '_apps_'+L+'/',
                    '_glossary_'+L+'/', '_config_'+L+'.yml', L+'/blog/'))
    risk = [l for l in st if re.match(r'^\s*(R|D|A|\?\?)', l)
            and any(k in l for k in ('_posts/','_apps','_pages/','_glossary'))
            and not approved(l)]
    if risk:
        a.warn('HYGIENE', 'HYGIENE-04', '文件名增删改（红线）', f'{len(risk)} 条需人工确认 {risk[:2]}')
    else:
        a.chk('HYGIENE', 'HYGIENE-04', '文件名增删改（红线）', True,
              f'0 条（已批准语言源 {LANGS[1:]}）')


# ---------------------------------------------------------------------------
# 执行入口
# ---------------------------------------------------------------------------
CHECKS = [
    ('BLD', check_bld), ('I18N', check_i18n), ('META', check_meta),
    ('CONTENT', check_content), ('LINK', check_link), ('A11Y', check_a11y),
    ('DESIGN', check_design), ('HYGIENE', check_hygiene),
]

def main():
    a = Auditor()
    for _, fn in CHECKS:
        fn(a)
    a.report()
    return 1 if a.total().get('FAIL', 0) else 0

if __name__ == '__main__':
    raise SystemExit(main())
