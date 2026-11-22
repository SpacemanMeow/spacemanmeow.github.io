#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全站静态教研门禁（单一权威副本）。

在仓库根目录运行：python3 scripts/site_audit.py
执行前需先完成一次构建，否则产物类维度会跳过。
FAIL 时退出码为 1，供 CI 阻断部署。
"""
# 全站教研静态检查 v3.4 / N 语言版（D18 文章骨架全语言对等：结构 / 目录 / 插图位置）（EN + 所有 _config_<lang>.yml）
# 新增语言无需改脚本：LANGS 自动发现；已完成语言按一一对应检查，
# 分批建设中的语言按「无孤立文件 + 覆盖进度」检查（见 SEO-I18N-PROGRESS.md）。
import os, re, glob, subprocess, collections
BASE = {}
R = []
def add(lv, c, n, d=''): R.append((lv, c, n, d))
def chk(c, n, ok, d=''): add('PASS' if ok else 'FAIL', c, n, d)
def warn(c, n, d=''): add('WARN', c, n, d)
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
    if L == 'en': return dict(posts='_posts', pages='_pages', apps='_apps', gloss='_glossary', rel='_release_notes')
    return dict(posts='_posts/' + L, pages='_pages/' + L,
                apps='_apps_' + L, gloss='_glossary_' + L, rel='_release_notes_' + L)
def lang_of(f):
    for L in LANGS[1:]:
        if any(f.startswith(d + '/') for d in dirs(L).values()): return L
    return 'en'

mds = []
for L in LANGS:
    for d in dirs(L).values(): mds += fs(d + '/**/*.md')
mds = sorted(set(mds))
txt = {f: open(f, encoding='utf-8').read() for f in mds}
fms = {f: fm(t) for f, t in txt.items()}
en_posts = nm('_posts/*.md')
FULL = [L for L in LANGS[1:] if nm(dirs(L)['posts'] + '/*.md') == en_posts]
PARTIAL = [L for L in LANGS[1:] if L not in FULL]
chk('D01', '语言清单与完成度（至少 5 语）', len(LANGS) >= 5,
    f'LANGS={LANGS} 完整={FULL} 分批中={PARTIAL}')
# D01：README 对外语言清单必须与 _data/languages.yml 同步（新增语言最易漏改的公开文案）
_labels = re.findall(r'^\s+label:\s*(.+?)\s*$',
                     open('_data/languages.yml', encoding='utf-8').read(), re.M)
_rm = re.search(r'^## 语言[ \t]*\n(.*?)(?=^## |\Z)',
                open('README.md', encoding='utf-8').read(), re.M | re.S)
_seg = _rm.group(1) if _rm else ''
_miss = [x for x in _labels if x not in _seg]
_CN = {1:'一', 2:'二', 3:'三', 4:'四', 5:'五', 6:'六', 7:'七', 8:'八', 9:'九',
       10:'十', 11:'十一', 12:'十二'}
_num = _CN.get(len(_labels), str(len(_labels)))
chk('D01', 'README 对外语言清单与 languages.yml 一致',
    bool(_labels) and not _miss and (f'{_num}个语言版本' in _seg),
    f'languages.yml {len(_labels)} 语；README 缺失 {_miss}；数量词应为「{_num}个语言版本」')
empty = [(L, k) for L in LANGS[1:] for k in ('apps', 'gloss')
         if not fs(dirs(L)[k] + '/*.md')]
chk('D04', '各语言集合非空（防 site[coll] 静默失败）', not empty, f'空集合 {empty}')
# D03 源对账
for lab, key in [('文章', 'posts'), ('应用', 'apps'), ('页面', 'pages'), ('术语', 'gloss')]:
    B = nm(dirs('en')[key] + '/*.md')
    for L in FULL:
        O = nm(dirs(L)[key] + '/*.md')
        chk('D03', f'{lab} EN/{L} 一一对应', B == O,
            f'EN={len(B)} {L}={len(O)} 差集={len(B ^ O)}')
    for L in PARTIAL:
        O = nm(dirs(L)[key] + '/*.md')
        orphan = O - B
        chk('D03', f'{lab} {L} 无孤立文件', not orphan,
            f'{L} {len(O)}/{len(B)}，孤立 {len(orphan)}；其余按 SEO-I18N-PROGRESS.md 分批补齐')
# D03 结构页硬门禁：每个完整语言必须含 10 个固定结构页（含 Docs / FAQ 中心页；缺页会致 htmlproofer 断链，P0）
STRUCT = ['index', 'meow', 'about', 'privacy', 'terms', 'search', 'tags', 'glossary', 'docs', 'faq']
for L in FULL:
    have = nm(dirs(L)['pages'] + '/*.md')
    miss = [s for s in STRUCT if (s + '.md') not in have]
    chk('D03', f'结构页 10/10 ({L})', not miss,
        f'缺失 {miss}（致 htmlproofer 断链；须与 id 骨架同源补齐，不得标记待补）')
# D06
need0 = {'title', 'description'}
bad = []
for f, d in fms.items():
    if re.match(r'^_release_notes(_[a-z]{2})?/', f): continue  # D20 单独校验其 frontmatter
    n = set(need0)
    if f.startswith('_posts/'): n |= {'date', 'layout', 'tags', 'image'}
    if re.match(r'^_apps(_[a-z]{2})?/', f): n.add('icon')
    if f.startswith('_pages/'): n.add('permalink')
    if n - set(d): bad.append((f, ','.join(sorted(n - set(d)))))
chk('D06', 'frontmatter 必填字段', not bad, f'异常 {len(bad)} {bad[:2]}')
langbad = [f for f, d in fms.items() if d.get('lang') != lang_of(f)]
chk('D06', 'lang 存在且与目录一致', not langbad, f'异常 {len(langbad)} {langbad[:2]}')
long, amp = [], []
for f, d in fms.items():
    v = d.get('description', '')
    if v.startswith(('>-', '>', '|')): continue
    s = v.strip('"')
    if len(s) > 160: long.append((f, len(s)))
    if '&' in s: amp.append(f)
chk('D06', 'description ≤160 字符', not long, f'超长 {len(long)} {long[:2]}')
chk('D06', 'description 无裸 &', not amp, f'{len(amp)} 处')
# D06：App tagline 四语信息量对等（SEO-I18N-PLAYBOOK.md §1 红线 12）
# 只设上限不设下限：中文忠实短句天然只有 EN 的 0.2–0.7 倍字符数，属正常
def _tagline(f):
    for l in open(f, encoding='utf-8').read().split('\n'):
        if l.startswith('tagline:'):
            return re.sub(r'\s+#\s.*$', '', l[len('tagline:'):].strip()).strip()
    return ''
def _nums(s): return set(re.findall(r'\d+', s))
tgl_bad = []
for L in LANGS[1:]:
    for f in fs(dirs(L)['apps'] + '/*.md'):
        en = '_apps/' + os.path.basename(f)
        if not os.path.isfile(en): continue
        a, b = _tagline(en), _tagline(f)
        if not a or not b:
            tgl_bad.append((f, 'tagline 缺失')); continue
        ratio = len(b) / max(len(a), 1)
        extra = _nums(b) - _nums(a)
        if ratio > 1.5 or extra:
            tgl_bad.append((f, f'长度比 {ratio:.2f} 规格数字增补 {sorted(extra)}'))
chk('D06', 'App tagline 信息量与 EN 对等（≤1.5× 且无增补规格数字）', not tgl_bad,
    f'异常 {len(tgl_bad)} {tgl_bad[:2]}')
# D06：站点级 tagline 单行显示宽度（SEO-I18N-PLAYBOOK.md §1 红线 13）
# header .brand__text small 为 nowrap + ellipsis；CJK/全角按 2 单位，泰文/拉丁按 1 单位
import unicodedata
def _w(s):
    return sum(2 if unicodedata.east_asian_width(c) in 'WF' else 1 for c in s)
def _cfg_tagline(f):
    for l in open(f, encoding='utf-8').read().split('\n'):
        if l.startswith('tagline:'):
            return re.sub(r'\s+#\s.*$', '', l[len('tagline:'):].strip()).strip().strip('"')
    return ''
_cfgs = ['_config.yml'] + ['_config_%s.yml' % L for L in LANGS[1:]]
_tw = {f: _w(_cfg_tagline(f)) for f in _cfgs if os.path.isfile(f)}
_enw = _tw.get('_config.yml', 0)
_tw_bad = [(f, w) for f, w in _tw.items() if w > 60 or (f != '_config.yml' and w > _enw)]
chk('D06', '站点级 tagline 单行显示宽度（w≤60，非 EN ≤ EN）', not _tw_bad,
    f'EN w={_enw}，各语 {sorted(_tw.items())}，异常 {_tw_bad}')
# D06：YAML 语法硬门禁（Jekyll 会静默丢弃解析失败的文档，导致空 src / 空链接的连带故障）
RB = r'''require 'yaml'
bad = []
Dir.glob('{_posts,_apps,_apps_*,_pages,_glossary,_glossary_*}/**/*.{md,html}').each do |f|
  t = File.read(f)
  next unless t.start_with?("---\n")
  e = t.index("\n---", 4)
  next unless e
  begin
    YAML.parse(t[4, e - 4])
  rescue StandardError => ex
    bad << f + ': ' + ex.message.lines.first.to_s.strip
  end
end
puts bad.join("\n")
'''
_rb = subprocess.run(['ruby', '-ryaml', '-e', RB], capture_output=True, text=True)
if _rb.returncode != 0:
    warn('D06', 'YAML 校验器不可用', _rb.stderr[:120])
else:
    _bad = [l for l in _rb.stdout.strip().split('\n') if l]
    chk('D06', 'frontmatter YAML 语法有效', not _bad, f'异常 {len(_bad)} {_bad[:2]}')
# D07：完整语言逐篇对齐；分批语言基础结构下限（骨架全语言对等由 D18 硬校验）
h2, sp, weak = [], [], []
for f, t in txt.items():
    if re.search(r'(?<=[\u4e00-\u9fff])[ \t]+(?=[\u4e00-\u9fff])', t): sp.append(f)
for n in en_posts:
    a = len(re.findall(r'^## ', txt['_posts/' + n], re.M))
    for L in FULL:
        z = dirs(L)['posts'] + '/' + n
        if os.path.exists(z):
            b = len(re.findall(r'^## ', txt[z], re.M))
            if a != b: h2.append((n, L, a, b))
chk('D07', '完整语言 H2 数量一致', not h2, f'不一致 {len(h2)} {h2[:2]}')
for L in PARTIAL:
    for f in fs(dirs(L)['posts'] + '/*.md'):
        c = len(re.findall(r'^## ', txt[f], re.M))
        if c < 4 or '{:.faq-q}' not in txt[f]: weak.append((f, c))
chk('D07', '分批语言文章结构完整（H2≥4 且含 FAQ）', not weak,
    f'异常 {len(weak)} {weak[:2]}')
chk('D07', '无汉字间多余空格', not sp, f'残留 {len(sp)} {sp[:2]}')
# D08
IMGRE = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)\s*(\{:[^}]*\})?')
dup, gen, missing, nowidth, total = [], [], [], [], 0
for f, t in txt.items():
    a = IMGRE.findall(t)
    if len(a) != len(set(x[0] for x in a)): dup.append(f)
    if re.search(r'!\[image\]', t, re.I): gen.append(f)
    for alt, p, attr in a:
        if p.startswith('/assets/'):
            total += 1
            if not os.path.exists('.' + p): missing.append((f, p))
            if not attr or not re.search(r'width\s*=', attr): nowidth.append((f, p))
chk('D08', '同文件 alt 唯一', not dup, f'重复 {len(dup)} {dup[:2]}')
chk('D08', '无 ![image] 残留', not gen, f'{len(gen)}')
chk('D08', '引用图片文件存在', not missing, f'缺失 {len(missing)} {missing[:2]}')
chk('D08', '图片 width 覆盖（防 CLS）', total > 0 and not nowidth,
    f'{total} 处引用，缺 width {len(nowidth)} {nowidth[:2]}')
# D17 文章插图跨语言一致性（P0，见 SEO-I18N-PLAYBOOK.md §3.5）
# 只比对「EN 有同名文件」的非 EN 文章；分批建设中的语言不要求 66 篇齐全。
IMGSET = re.compile(r'!\[([^\]]*)\]\((/assets/images/[^)]+)\)')
TOCRE = re.compile(r'^- \[[^\]]+\]\(#[^)]+\)$')
def SKEL(l):
    x = l.strip()
    if x.startswith('### '): return 'H3'
    if x.startswith('## '): return 'H2'
    if x.startswith('!['): return 'IMG'
    if x.startswith('|'): return 'TBL'
    if x.startswith('- '): return 'LI'
    if re.match(r'^\d+\. ', x): return 'NUM'
    if x == '{:.faq-q}': return 'FAQ'
    if x == '---': return 'HR'
    return None
_en_posts = {os.path.basename(f): f for f in fs('_posts/[12]*.md')}
mis, copied, pos = [], [], []
hbad, sbad, tbad = [], [], []
for f, t in txt.items():
    if lang_of(f) == 'en' or not f.startswith('_posts/'): continue
    e = _en_posts.get(os.path.basename(f))
    if not e: continue
    a = collections.Counter(p for _, p in IMGSET.findall(txt[e]))
    b = collections.Counter(p for _, p in IMGSET.findall(t))
    if a != b: mis.append((f, sum(a.values()), sum(b.values())))
    el, tl = txt[e].split('\n'), t.split('\n')
    ea = [i for i, l in enumerate(el) if IMGSET.search(l)]
    ba = [i for i, l in enumerate(tl) if IMGSET.search(l)]
    if ea != ba: pos.append((f, ea[:3], ba[:3]))
    es = [k for k in (SKEL(l) for l in el) if k]
    ts = [k for k in (SKEL(l) for l in tl) if k]
    if es != ts: sbad.append((f, len(es), len(ts)))
    eh = [k for k in es if k in ('H2', 'H3')]
    th = [k for k in ts if k in ('H2', 'H3')]
    if eh != th: hbad.append((f, len(eh), len(th)))
    etoc = [i for i, l in enumerate(el) if TOCRE.match(l)]
    ttoc = [i for i, l in enumerate(tl) if TOCRE.match(l)]
    if etoc != ttoc: tbad.append((f, etoc[:3], ttoc[:3]))
    en_alts = {x[0] for x in IMGSET.findall(txt[e])}
    hit = [x[0] for x in IMGSET.findall(t) if x[0] in en_alts]
    if hit: copied.append((f, hit[0]))
chk('D17', '文章插图集合与 EN 一致', not mis,
    f'{len(mis)} 篇不一致 {mis[:2]}')
chk('D17', '插图行序位置与 EN 一致', not pos,
    f'{len(pos)} 篇不一致 {pos[:2]}')
chk('D17', '插图 alt 已本地化（未照抄 EN）', not copied,
    f'{len(copied)} 篇 {copied[:2]}')
# D18 文章骨架全语言对等：结构 / 目录 / 图片插入（所有非 EN 语言，逐篇比对 EN 同名文章）
chk('D18', '文章 H2/H3 层级序列与 EN 一致', not hbad,
    f'{len(hbad)} 篇不一致 {hbad[:2]}')
chk('D18', '文章结构块序列与 EN 一致', not sbad,
    f'{len(sbad)} 篇不一致 {sbad[:2]}')
chk('D18', '文章目录（TOC）与 EN 一致', not tbad,
    f'{len(tbad)} 篇不一致 {tbad[:2]}')
chk('D18', '图片插入行序与 EN 一致', not pos,
    f'{len(pos)} 篇不一致 {pos[:2]}')
# D09 关键词真实覆盖（词库标「已覆盖」的词必须出现在正文，按语言归一化核对）
K = open('seo/SEO-KEYWORDS.md', encoding='utf-8').read().split('\n')
sec, terms = None, collections.defaultdict(set)
for l in K:
    m = re.match(r'^## (2\.\d+) ', l)
    if m: sec = m.group(1); continue
    if l.startswith('## 3.'): sec = None; continue
    if sec is None or not l.startswith('|') or l.startswith('|---'): continue
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) >= 7 and c[0] != '关键词' and '已覆盖' in c[6]:
        for w in c[0].split('/'): terms[sec].add(w.strip())
    if len(c) == 4 and '已覆盖' in c[3]:
        for w in c[1].split('/'): terms[sec].add(w.strip())
cn = norm('\n'.join(txt.values()))
miss = sorted(w for v in terms.values() for w in v if w and norm(w) not in cn)
chk('D09', '全部关键词真实覆盖', not miss and len(terms) >= 11,
    f'{len(terms)} 组，MISS {len(miss)} {miss[:3]}')
# D19：tags 一致性与相关文章匹配（P0；产品标签变体曾致 related-posts 跨品类，见 §4 D19）
# 规则：① 每篇【_posts/ 文章】至少带 1 个规范产品标签（11 个 App 之一）；
#       ② 不得出现产品标签变体（Meow Mood / Meow Todo List / To Do List / 多余 Meow 前缀等）；
#       ③ related-posts.html 跳过泛标签（Android/Comparison/Best Apps/App Roundup/Alternatives）。
CANON_PRODUCT = {'Meow Todo', 'Meow Habits', 'Meow Money', 'Meow Mood Diary',
                 'Meow FM', 'Only Clock', 'One Widget', 'Crosshair Aim',
                 'System Monitor', 'CPU Monitor', 'Floating Assistant'}
BRAND_PREFIX = ('Meow', 'Only Clock', 'One Widget', 'Crosshair Aim',
                'System Monitor', 'CPU Monitor', 'Floating Assistant')
_badvar, _noprod = [], []
for f, d in fms.items():
    if not f.startswith('_posts/'): continue
    raw = d.get('tags', '')
    m = re.match(r'\[(.*)\]', raw)
    tags = [x.strip() for x in m.group(1).split(',') if x.strip()] if m else []
    for tg in tags:
        if tg in ('Meow Mood', 'Meow Todo List', 'To Do List') or \
           (tg.startswith(BRAND_PREFIX) and tg not in CANON_PRODUCT):
            _badvar.append((f, tg))
    if not (set(tags) & CANON_PRODUCT):
        _noprod.append(f)
chk('D19', 'tags 无产品标签变体', not _badvar, f'异常 {len(_badvar)} {_badvar[:2]}')
chk('D19', '每篇至少带规范产品标签', not _noprod, f'缺失 {len(_noprod)} {_noprod[:2]}')
# D20：Release Note 页面覆盖与内链（P0；见 §4 D20）
# 规则：每语言 11 个 App 均有对应 release note 页；frontmatter 带 layout/app_slug/app_title/google_play；
#       正文有发布记录内容；app 详情页底部有指向 release-notes/ 的内链。
REL_LABEL = {'en': 'Release Notes', 'zh': '更新日志', 'id': 'Catatan Rilis',
             'ms': 'Nota Keluaran', 'th': 'บันทึกการอัปเดต'}
_rel_miss, _rel_badfm, _rel_empty, _rel_badtitle, _rel_badstore = [], [], [], [], []
for L in LANGS:
    app_slugs = nm(dirs(L)['apps'] + '/*.md')
    rel_slugs = nm(dirs(L)['rel'] + '/*.md')
    for s in app_slugs:
        if s not in rel_slugs: _rel_miss.append((L, s))
    for f, d in fms.items():
        if not f.startswith('_%s/' % ('release_notes' if L == 'en' else 'release_notes_' + L)): continue
        need = {'layout', 'app_slug', 'app_title', 'google_play', 'app_store', 'lang', 'title'}
        if need - set(d): _rel_badfm.append((f, ','.join(sorted(need - set(d)))))
        if not re.search(r'^\d+\.\s+\S', txt[f], re.M): _rel_empty.append(f)
        if REL_LABEL.get(L, 'Release Notes') not in d.get('title', ''): _rel_badtitle.append(f)
        # 裸 app_store: 空值会被 YAML 吞掉下一行，破坏 layout/hreflang；单端须写 app_store: ""
        if re.search(r'^app_store:[ \t]*$', txt[f], re.M): _rel_badstore.append(f)
chk('D20', '每 App 均有 Release Note 页（全语言）', not _rel_miss, f'缺失 {len(_rel_miss)} {_rel_miss[:2]}')
chk('D20', 'Release Note frontmatter 完整', not _rel_badfm, f'异常 {len(_rel_badfm)} {_rel_badfm[:2]}')
chk('D20', 'Release Note 正文含发布记录', not _rel_empty, f'空 {len(_rel_empty)} {_rel_empty[:2]}')
chk('D20', 'Release Note 标题含本地化后缀', not _rel_badtitle, f'异常 {len(_rel_badtitle)} {_rel_badtitle[:2]}')
chk('D20', 'Release Note 无裸 app_store 空值行', not _rel_badstore, f'异常 {len(_rel_badstore)} {_rel_badstore[:2]}')
# app 模板须含 release-notes 内链（一处覆盖全语言）
_app_tpl = open('_layouts/app.html', encoding='utf-8').read()
chk('D20', 'app 详情页含 Release Note 内链', 'release-notes/' in _app_tpl, 'app.html 缺内链')
# D11 内链前缀（按语言检查，排除共享资源）
def links(t): return re.findall(r'\]\((/[^)]*)\)', t)
zbad, ebad = [], []
for f, t in txt.items():
    L = lang_of(f)
    for u in links(t):
        if u.startswith(('/assets/', '/pagefind/')): continue
        if L == 'en' and any(u.startswith('/' + x + '/') for x in LANGS[1:]):
            ebad.append((f, u))
        if L != 'en' and not u.startswith('/' + L + '/'):
            zbad.append((f, u))
chk('D11', '内链语言前缀', not zbad and not ebad,
    f'非 EN 缺前缀 {len(zbad)} {zbad[:2]} / EN 误带 {len(ebad)} {ebad[:2]}')
# D11 形态间内链闭合：Docs 形态须在导航与模板中留入口
_nav_txt = open('_data/nav.yml', encoding='utf-8').read()
_tpl_txt = ''.join(open(f, encoding='utf-8').read() for f in
                   fs('_layouts/*.html') + fs('_includes/*.html'))
_hub_ok = ('nav: docs' in _nav_txt and 'docs-hub' in _tpl_txt)
chk('D11', '形态间内链入口闭合', _hub_ok,
    'docs 导航项或 docs-hub 模板入口缺失')
# D14：新增语言源文件属已批准改动，不计入红线告警
st = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True).stdout.split('\n')
def approved(l):
    return any(k in l for L in LANGS[1:] for k in
               ('_posts/' + L + '/', '_pages/' + L + '/', '_apps_' + L + '/',
                '_glossary_' + L + '/', '_config_' + L + '.yml', L + '/blog/'))
risk = [l for l in st if re.match(r'^\s*(R|D|A|\?\?)', l)
        and any(k in l for k in ('_posts/', '_apps', '_pages/', '_glossary'))
        and not approved(l)]
if risk: warn('D14', '文件名增删改（红线）', f'{len(risk)} 条需人工确认 {risk[:2]}')
else: chk('D14', '文件名增删改（红线）', True, f'0 条（已批准语言源 {LANGS[1:]}）')
# 产物维度
if os.path.isdir('_site'):
    hs = fs('_site/**/*.html')
    heads = {h: open(h, encoding='utf-8').read() for h in hs}
    pages = {h: v for h, v in heads.items() if os.path.basename(h) != '404.html'}
    chk('D05', '每页 hreflang 块', all('i18n-hreflang' in v for v in pages.values()),
        f'{len(pages)} 页')
    missxd = [h for h, v in pages.items()
              if 'hreflang="en"' not in v or 'hreflang="x-default"' not in v]
    chk('D05', 'hreflang en + x-default 完整', not missxd, f'异常 {len(missxd)}')
    cnt = collections.Counter(len(re.findall(r'hreflang="[^"]+"', v)) for v in pages.values())
    chk('D05', 'hreflang 条数随组内语言数变化',
        min(cnt) >= 2 and max(cnt) <= len(LANGS) + 1, f'分布 {dict(cnt)}')
    for L in LANGS[1:]:
        lp = '_site/' + L + '/'
        sub = [h for h in pages if h.startswith(lp)]
        bad = [h for h in sub if 'hreflang="' + L + '"' not in heads[h]]
        chk('D05', L + ' 页含自身 alternate', not bad, f'{len(sub)} 页，异常 {len(bad)}')
        chk('D05', L + ' 子 sitemap 已删', not os.path.exists(lp + 'sitemap.xml'), '')
    sm = open('_site/sitemap.xml', encoding='utf-8').read() if os.path.exists('_site/sitemap.xml') else ''
    chk('D05', '合并 sitemap', len(re.findall(r'<loc>', sm)) > 0,
        f'{len(re.findall(r"<loc>", sm))} 条 loc')
    chk('D12', '404 不进 sitemap', '404' not in sm, '')
    ld = [b for v in heads.values() for b in re.findall(
        r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', v, re.S)]
    chk('D10', 'JSON-LD 无 &amp;', not any('&amp;' in b for b in ld), f'{len(ld)} 个块')
    feeds = ['_site/feed.xml'] + ['_site/' + L + '/feed.xml' for L in LANGS[1:]]
    chk('D12', 'feed / robots', all(os.path.exists(x) for x in feeds)
        and os.path.exists('_site/robots.txt'), ','.join(feeds))
    chk('D12', 'Pagefind 索引', os.path.isfile('_site/pagefind/pagefind.js'), '')
    temps = [d for L in LANGS[1:] for d in ('.jekyll-' + L,) if os.path.isdir(d)]
    chk('D15', '无临时目录残留', not temps, f'{temps}')
    chk('D15', '内部 seo/ 未发布', not os.path.isdir('_site/seo'),
        f'存在={os.path.isdir("_site/seo")}')
    leaks = [p for p in fs('_site/**/*') if any(k in p for k in
             ('credentials.json', 'token.json', 'pagefind-bin')
             + tuple('jekyll-' + L for L in LANGS[1:]))]
    chk('D15', '无凭据/缓存文件泄漏', not leaks, f'{len(leaks)} 个')
else:
    warn('DXX', '未构建', '请先运行 bash scripts/build.sh')

# D22 设计令牌与统一样式（P0）：字体/字重/分割线/间距/按钮等禁止硬编码，必须复用统一样式
_css = open('assets/css/main.css', encoding='utf-8').read()
_css_nocomment = re.sub(r'/\*.*?\*/', '', _css, flags=re.S)
# 1) 字号：只能 --fs-sm/base/md/xl/2xl/3xl；无硬编码 px/em/rem/%/clamp/calc
_FS = {'--fs-sm', '--fs-base', '--fs-md', '--fs-xl', '--fs-2xl', '--fs-3xl'}
_fs_def = set(re.findall(r'(--fs-[\w-]+)\s*:', _css))
chk('D22', '字号变量仅保留 6 档标准', _fs_def == _FS,
    f'定义={sorted(_fs_def)} 期望={sorted(_FS)}')
_hard_fs = re.findall(r'font-size\s*:\s*([^;]+)', _css_nocomment)
_hard_fs = [v.strip() for v in _hard_fs if 'var(--fs-' not in v]
chk('D22', '无硬编码字号（font-size 全部用 --fs-* 变量）', not _hard_fs,
    f'硬编码 {len(_hard_fs)} 处 {_hard_fs[:5]}')
# 2) 字重：只能 --fw-head/bold/body；无硬编码数字/关键字
_FW = {'--fw-head', '--fw-bold', '--fw-body'}
_fw_def = set(re.findall(r'(--fw-[\w-]+)\s*:', _css))
chk('D22', '字重变量仅保留 3 档标准', _fw_def == _FW,
    f'定义={sorted(_fw_def)} 期望={sorted(_FW)}')
_hard_fw = re.findall(r'font-weight\s*:\s*([^;]+)', _css_nocomment)
_hard_fw = [v.strip() for v in _hard_fw if 'var(--fw-' not in v]
chk('D22', '无硬编码字重（font-weight 全部用 --fw-* 变量）', not _hard_fw,
    f'硬编码 {len(_hard_fw)} 处 {_hard_fw[:5]}')
# 3) 全仓源文件（排除构建产物/依赖）无硬编码字号字重，含独立 HTML 生成器与内联样式
_srcs = []
for _pat in ('**/*.css', '**/*.html', '**/*.liquid', '**/*.py', '**/*.js'):
    _srcs += [p for p in fs(_pat) if not re.search(
        r'(^|/)(_site|_site_en|_site_zh|\.jekyll-[^/]*|node_modules|\.git|\.pagefind-bin|\.sass-cache)/', p)]
_bad_inline = []
for _p in set(_srcs):
    try: _t = open(_p, encoding='utf-8').read()
    except Exception: continue
    for _m in re.finditer(r'font-size\s*:\s*([^;}"\']+)', _t):
        if 'var(--fs-' not in _m.group(1): _bad_inline.append((_p, 'size', _m.group(1).strip()))
    for _m in re.finditer(r'font-weight\s*:\s*([^;}"\']+)', _t):
        if 'var(--fw-' not in _m.group(1): _bad_inline.append((_p, 'weight', _m.group(1).strip()))
chk('D22', '全仓源文件无硬编码字号/字重（含内联样式与生成器）', not _bad_inline,
    f'{len(_bad_inline)} 处 {_bad_inline[:5]}')
# 4) 统一样式令牌必须齐备（分割线/间距/圆角/阴影），且分割线禁止硬编码颜色
_TOKENS = ['--divider-dashed', '--divider-solid',
           '--space-1', '--space-9', '--radius-sm', '--radius-xl',
           '--shadow-card', '--shadow-soft']
_miss_tok = [t for t in _TOKENS if not re.search(re.escape(t) + r'\s*:', _css)]
chk('D22', '统一令牌齐备（分割线/间距/圆角/阴影）', not _miss_tok,
    f'缺失 {_miss_tok}')
_borders = re.findall(r'border(?:-top|-bottom|-left|-right)?\s*:\s*([^;]+)', _css_nocomment)
_hex_border = [v.strip() for v in _borders if re.search(r'#[0-9a-fA-F]{3,8}\b', v)]
chk('D22', '分割线颜色无硬编码（border 用 var(--line)/--divider-*)', not _hex_border,
    f'硬编码颜色 {len(_hex_border)} 处 {_hex_border[:5]}')
# 5) 共享组件样式只在 _includes/store-buttons.html 定义，页面源码不重复硬编码按钮结构
_btn_inc = fs('_includes/store-buttons.html')
chk('D22', '商店按钮为共享 include（单一来源）', bool(_btn_inc),
    f'_includes/store-buttons.html 存在={bool(_btn_inc)}')
print('=== 全站教研结果 ===')
for lv, c, n, d in R: print(f'{lv:4s} {c:4s} {n:32s} {d}')
print('汇总', dict(collections.Counter(x[0] for x in R)))

# CI gate: any hard-gate failure fails the step.
_fails = [x for x in R if x[0] == "FAIL"]
raise SystemExit(1 if _fails else 0)
