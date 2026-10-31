# SEO 核心指标月度报告

> 本文件**独立维护**，专门记录每月核心 SEO 指标的趋势与详细分析。
> **更新方式**：每月初用 `../tools/gsc_export.py` 拉取上月全量 GSC 数据（用法见 `SEO-PLAYBOOK.md` §7.1），然后：
> 1. 在下方「核心指标趋势表」加一行数字；
> 2. 在「每月详细分析」新增一个 `#### YYYY-MM` 小节，说明变化原因与后续动作。
> **口径**：收录页数 / 点击 / 展现 / CTR / 排名来自 **GSC（Google 搜索）**；全站访问来自 **GoatCounter**（含所有来源，口径不同，仅作辅助参考）。

## 核心指标趋势（跨月对比）

表内只放可横向对比的核心数字；每月变化原因见下方各月详细分析。

| 月份 | 收录页数 | GSC 点击 | GSC 展现 | CTR | 平均排名 | 全站访问 |
|---|---|---|---|---|---|----------|
| 2026-10 | 见 GSC Indexing（sitemap 提交 228） | 57 | 1789 | 3.19% | 10.3 | 515      |
| 2026-11 | | | | | |          |
| 2026-12 | | | | | |          |
| 2027-01 | | | | | |          |
| 2027-02 | | | | | |          |
| 2027-03 | | | | | |          |
| 2027-04 | | | | | |          |

收录页数 / 点击 / 展现 / CTR / 排名来自 **GSC（Google 搜索口径）**；全站访问来自 **GoatCounter**（含所有来源，口径不同，仅作辅助参考）。每月用 `../tools/gsc_export.py` 拉取后回填本表 + 下方分析。

## 每月详细分析

#### 2026-10（基线月）

- **Google 搜索（GSC）**：展现 1789 / 点击 57 / CTR 3.19% / 平均排名 10.3。
- **真实搜索词（全 147 词，见 `data/oct2026_query.csv`）**：`meow money`(3击/23现)、`meow manager`(2)、`meow money manager`(2)、`phone cpu temperature check`(1)、`android cpu temperature`(0/5)、`alternative ccleaner android`(0/1)、`aesthetic clock app`(0/1)。品牌词（meow*）已起量；长尾硬件词（cpu temperature / android）有展现但无点击，是后续内容优化的重点。
- **Top 页面**：`meow-money-manager`(21击/191现)、`pillar-flip-clock-apps-android`(6/77)、`pillar-cpu-temperature-monitor`(5/257)、`alternatives-to-widgetsmith`(3/123)。
- **国家（GSC）**：菲律宾 13 / 印尼 6 / 美国 5 / 马来 4 / 泰国 4 —— 英语区与东南亚并重。
- **设备**：Mobile 45 / Desktop 11 / Tablet 1（移动为主）。
- **GoatCounter 全站 515 访问**：来源 Google 50% / Email 13% / chatgpt 2% / bing 1% / DDG 1%；位置 US 26%·ID 7%·MY 6%·PH 5%·CN 4%·IN 4%；系统 Android 56%·iOS 12%·macOS 20%；手机 64%。
- **解读**：10 月为内容集群 66 篇首月 + 中英双语优化落库，流量基数小属正常。CPU/Flip 集群已起量，移动端 + 东南亚特征明显，与 `SEO-PROGRESS.md` T-31 语种试点（id/ms/tl/hi）方向吻合；AI 引荐（chatgpt 2%）初现，印证 AI 搜索专项开始见效。后续重点：把「有展现无点击」的长尾硬件词补成深度内容，并借 changelog 常态化抬升新鲜度。

---

### 新增月份模板（复制后改日期填充）

```markdown
#### YYYY-MM

- **Google 搜索（GSC）**：展现 / 点击 / CTR / 平均排名。
- **真实搜索词（全 N 词，见 `data/yyyymm_query.csv`）**：`词1`(x击/y现)、`词2`(...)……
- **Top 页面**：`页面1`(x击/y现)、`页面2`(...)……
- **国家（GSC）**：国家1 / 国家2 / ……
- **设备**：Mobile / Desktop / Tablet。
- **GoatCounter 全站 N 访问**：来源 ……；位置 ……；系统 ……；手机 …%。
- **解读**：本月做了什么、指标环比变化原因、后续重点。
```
