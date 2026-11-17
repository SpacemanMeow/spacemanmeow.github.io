# SEO 核心指标月度报告

> 本文件**独立维护**，专门记录每月核心 SEO 指标的趋势与详细分析。
> **更新方式**：每月初用 `../skills/seo-research/scripts/gsc_export.py` 拉取上月全量 GSC 数据（用法见 `SEO-PLAYBOOK.md` §7.1），然后：① 在下方趋势表加一行数字；② 在「每月详细分析」新增一个 `#### YYYY-MM` 小节说明变化原因与后续动作。**数据未拉到就留空并标注，不臆造数字。**
> **口径**：收录页数 / 点击 / 展现 / CTR / 排名来自 **GSC（Google 搜索）**；全站访问来自 **GoatCounter**（含所有来源，口径不同，仅作辅助参考）。导出的 CSV/JSON 落在 `../skills/seo-research/scripts/gsc/`（已 gitignore），本文件不引用会被 gitignore 的 `seo/data/` 路径。

## 核心指标趋势（跨月对比）

表内只放可横向对比的核心数字；每月变化原因见下方各月详细分析。

| 月份 | 收录页数 | GSC 点击 | GSC 展现 | CTR | 平均排名 | 全站访问 |
|---|---|---|---|---|---|---|
| 2026-10 | 见 GSC Indexing | 57 | 1789 | 3.19% | 10.3 | 515 |
| 2026-11 | 待回填（本月 5 语全量 + 3 批对比文发布，收录应显著上升） | | | | | |

> **回填提醒**：2026-11 发生了 5 语全量交付与 3 篇 5 语深度对比文发布（见 `SITE-AUDIT.md` §8），是当前最重要的观测窗；数据到位后必须补齐 11 月行并写明发布对收录/流量的影响，不得长期留空。

## 每月详细分析

#### 2026-10（基线月）

- **Google 搜索（GSC）**：展现 1789 / 点击 57 / CTR 3.19% / 平均排名 10.3。
- **真实搜索词**：`meow money`(3击/23现)、`meow manager`(2)、`meow money manager`(2)、`phone cpu temperature check`(1)、`android cpu temperature`(0/5)、`alternative ccleaner android`(0/1)、`aesthetic clock app`(0/1)。品牌词（meow*）已起量；长尾硬件词（cpu temperature / android）有展现无点击，是后续内容优化重点。
- **Top 页面**：`meow-money-manager`(21击/191现)、`pillar-flip-clock-apps-android`(6/77)、`pillar-cpu-temperature-monitor`(5/257)、`alternatives-to-widgetsmith`(3/123)。
- **国家（GSC）**：菲律宾 13 / 印尼 6 / 美国 5 / 马来 4 / 泰国 4 —— 英语区与东南亚并重。
- **设备**：Mobile 45 / Desktop 11 / Tablet 1（移动为主）。
- **GoatCounter 全站 515 访问**：来源 Google 50% / Email 13% / chatgpt 2% / bing 1% / DDG 1%；位置 US 26%·ID 7%·MY 6%·PH 5%·CN 4%·IN 4%；系统 Android 56%·iOS 12%·macOS 20%；手机 64%。
- **解读**：10 月为内容集群首月 + 中英双语优化落库，流量基数小属正常。CPU/Flip 集群已起量，移动端 + 东南亚特征明显；AI 引荐（chatgpt 2%）初现。后续重点：把「有展现无点击」的长尾硬件词补成深度内容，并用 Release Note 抬升新鲜度。

---

### 新增月份模板（复制后改日期填充）

```markdown
#### YYYY-MM

- **Google 搜索（GSC）**：展现 / 点击 / CTR / 平均排名。
- **真实搜索词**：`词1`(x击/y现)、`词2`(...)……（原始导出见 skills/seo-research/scripts/gsc/）
- **Top 页面**：`页面1`(x击/y现)、`页面2`(...)……
- **国家（GSC）**：国家1 / 国家2 / ……
- **设备**：Mobile / Desktop / Tablet。
- **GoatCounter 全站 N 访问**：来源 ……；位置 ……；系统 ……；手机 …%。
- **解读**：本月做了什么、指标环比变化原因、后续重点。
```
