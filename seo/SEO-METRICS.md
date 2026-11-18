# SEO 核心指标月度报告

> 本文件**独立维护**，专门记录每月核心 SEO 指标的趋势与详细分析。
> **更新方式**：每月初用 `../skills/seo-research/scripts/gsc_export.py` 拉取上月全量 GSC 数据（用法见 `SEO-PLAYBOOK.md` §7.1），然后：① 在下方趋势表加一行数字；② 在「每月详细分析」新增一个 `#### YYYY-MM` 小节说明变化原因与后续动作。**数据未拉到就留空并标注，不臆造数字。**
> **口径**：收录页数 / 点击 / 展现 / CTR / 排名来自 **GSC（Google 搜索）**；全站访问来自 **GoatCounter**（含所有来源，口径不同，仅作辅助参考）。导出的 CSV/JSON 统一落在 `seo/data/`（已 gitignore，凭据仍固定在 `skills/seo-research/scripts/gsc/`）；本文件只引用汇总数字，不直接引用被 gitignore 的导出明细。

## 核心指标趋势（跨月对比）

表内只放可横向对比的核心数字；每月变化原因见下方各月详细分析。

| 月份 | 收录页数 | GSC 点击 | GSC 展现 | CTR | 平均排名 | 全站访问 |
|---|---|---|---|---|---|---|
| 2026-10 | 见 GSC Indexing | 57 | 1789 | 3.19% | 10.3 | 515（整月） |
| 2026-11 | 340 页有展现 | 182 | 8280 | 2.20% | 15.7 | 929（1–18 日） |

> **口径**：2026-11 GSC 为 11/1–11/15（API 实际返回 15 天，导出时延迟约 3 天），GoatCounter 为 11/1–11/18；10 月为整月。因此**环比必须用日均**：GSC 点击 12.1/天 vs 10 月 1.8/天（约 6.6×）、展现 552/天 vs 58/天（约 9.6×）；GoatCounter 51.6/天 vs 16.6/天（约 3.1×）。绝对值不可直接相减。
> **回填说明**：2026-11 发生 5 语全量交付与 3 批 5 语深度对比文发布（见 `SITE-AUDIT.md` §8）；340 页有展现、仅 114 EN + 61 zh + 71 id + 69 th + 25 ms 页产生展现，说明发布已带来大范围曝光，但点击高度集中。

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

#### 2026-11（5 语全量 + 3 批深对比文发布后的首个观测窗）

- **Google 搜索（GSC，11/1–11/15）**：展现 8280 / 点击 182 / CTR 2.20% / 平均排名 15.7，340 页有展现。环比 10 月：日均点击 12.1 vs 1.8（6.6×）、日均展现 552 vs 58（9.6×），但 CTR 3.19%→2.20%（−0.99pp）、平均排名 10.3→15.7（退 5.4 位）。
- **真实搜索词**：品牌词 `meow manager`(8击/47现/CTR 17%)、`meow money`(8/62/12.9%)、`meow money manager`(3/41/7.3%) 共 19 击、CTR 最高；品类/替代词 `cpu-z alternative android`(1/5)、`ccleaner alternative android`(1/3)、`best widget apps for android`(1/3) 长尾化明显，单query >2 击的极少。高展现低点击词集中在 Glossary 占位词：`budget management`(0/595/pos 60.2)、`floating window`(0/130/pos 10)、`crosshair`(1/96/pos 37.8)、`one ui`(0/84/pos 41)、`nothing ui`(0/61/pos 9.3)、`jendela mengambang`(1/97/pos 7.7)。
- **Top 页面**：`apps/meow-money-manager`(30击/465现)、`alternatives-to-widgetsmith`(14/342)、`pillar-cpu-temperature-monitor-apps-android`(13/622/CTR 2.1%)、`pillar-android-home-screen-widgets`(12/237/pos 29.5 异常)、`pillar-flip-clock-apps-android`(12/307)、`tutorial-meow-money`(11/127/CTR 8.7%)、`pillar-crosshair-apps-fps-android`(9/231)。
- **术语页吞噬曝光**：`glossary/what-is-budget-management`(0击/640现/pos 59.5)、`what-is-a-floating-window`(0/356/pos 8.5)、`what-is-a-crosshair`(1/324/pos 18.7)、`what-is-galaxy-one-ui`(0/241/pos 35.7)、印尼语 `id/glossary/what-is-a-floating-window`(1/175)。仅这 5 页合计约 1736 展现、2 点击。
- **国家（GSC）**：泰国 19、美国 19、印尼 17、印度 17、马来 11、菲律宾 10 —— 东南亚 + 印度崛起，美国展现 1524 但 CTR 仅 1.2%（pos 21.5）。
- **设备**：Mobile 138击/4472现（CTR 3.1%、pos 9.5）、Desktop 36/3580（CTR 1.0%、pos 23.5）、Tablet 8/228。
- **按语言页面聚合**：EN 155击/7012现、zh 12/400、id 8/714、th 6/451、ms 2/65 —— 非英语页有曝光但 CTR 偏低（id 1.1%）。
- **GoatCounter 全站 929 访问（11/1–11/18）**：来源 Google 41%(377) / 未知 26%(241) / chatgpt.com 3%(26) / Bing 约 1.1%(11) / Email 0.4%(4)；位置 US 11%·ID 10%·IN 9%·CN 8%·TH 5%·MY 5%；系统 Android 67%·macOS 10%·Windows 10%·iOS 9%；手机 73%·桌面 14%·高 HD 桌面 8%·平板 5%；浏览器 Chrome 88%·Safari 10%。
- **增长页面（GoatCounter vs 10 月同期）**：首页 329(+68%)、`meow-money-manager` 52(+53%)、`alternatives-to-widgetsmith` 27(+350%)、`pillar-cpu-temperature` 26(+100%)、`pillar-android-home-screen-widgets` 22(+1000%)、`pillar-flip-clock` 16(+78%)、`pillar-floating-assistant` 14(+600%)、`alternatives-to-assistive-touch` 12(+500%)、`pillar-crosshair` 12(+300%)、`only-clock` 9(+800%)、`/zh` 21(+600%)、`/id` 18(新)、`/th` 9(新)、`/search` 11(+1000%)。
- **解读与方向**：内容扩张已成功把曝光放大约 10 倍，但点击增长主要靠品牌词与少数强页；排名与 CTR 下滑是「新页大量进入 20–60 位 + Glossary 抢到不相关 Head 词」的结构性问题，不是旧页崩塌。下一步优先级：① 把 Glossary 的高曝光零点击词（budget management / floating window / crosshair / one ui）改为导流页或让 Pillar/App 主吃，标题/描述补解决方案词；② 重写 `pillar-cpu-temperature`（622 现 / 2.1% CTR，10 月同样 1.95%）与 `pillar-android-home-screen-widgets`（pos 29.5）的 title/description；③ 复制「竞品替代 + 平台限定 + 2026」高增长内容模式，但停止用 Glossary 硬打 Head 大词；④ 非英语 CTR 优化优先 id/th（GSC 点击第 1 的泰国与第 3 的印尼，对应本地页仅 6/8 击），核对 hreflang 与本地化标题；⑤ 移动端占 73%、GSC mobile CTR 3.1% vs desktop 1.0%，新内容与内链一律移动优先；⑥ chatgpt.com 引荐升至 3%（10 月 2%），定义型 Glossary 已成 AI 引用资产，继续用结构化数据 + 清晰 CTA 承接；⑦ T-29 性能、T-22b / T-36 / T-41 本批处理；新语言扩张已删除，不再排期。

---

### 新增月份模板（复制后改日期填充）

```markdown
#### YYYY-MM

- **Google 搜索（GSC）**：展现 / 点击 / CTR / 平均排名。
- **真实搜索词**：`词1`(x击/y现)、`词2`(...)……（原始导出见 `seo/data/`）
- **Top 页面**：`页面1`(x击/y现)、`页面2`(...)……
- **国家（GSC）**：国家1 / 国家2 / ……
- **设备**：Mobile / Desktop / Tablet。
- **GoatCounter 全站 N 访问**：来源 ……；位置 ……；系统 ……；手机 …%。
- **解读**：本月做了什么、指标环比变化原因、后续重点。
```
