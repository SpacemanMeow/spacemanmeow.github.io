# SpacemanMeow SEO 关键词库（Keyword Bank）

> **用途**：所有 App 跨语言关键词的**权威库**。按「语言 × 词层 × 优先级」分组排序，作为**新文章撰写、现有文章更新**的文案优化依据；并随 Google Play Console / Search Console 真实数据持续维护。
> **最后更新**：2026-11-04
> **语言范围**：英文站（默认 `en`）+ `/zh/` 中文站（已上线）+ 后续可扩展 `id` / `ms` / `tl` / `hi` 等（试点见 `SEO-PROGRESS.md` T-31）。关键词须**本地化**而非直译（见 `SEO-PLAYBOOK.md` §6.1）。
> **关联文档**：本库是 `SEO-PLAYBOOK.md` §2.1.1 关键词库的**详细展开与持续维护版**；内容集群模型见 §2.2，度量回填见 `SEO-METRICS.md`。

---

## 0. 使用规范（编辑 SOP）

1. **新文章**：先查本库 §1 索引 → 选目标词（优先 P0/P1）→ 文案围绕目标词展开（title/description/H1/首段/Glossary 内链）→ 填 `tags`（app/品类/类型/竞品四层，见 §3.5）→ 确认与 Pillar/App 互链 → 改完后回写本库「当前覆盖」列 + 标 `last_modified_at`（见 `SEO-PLAYBOOK.md` §2.4）。
2. **改文章**：用 GSC 实际点击词（`tools/gsc_export.py`）回填本库「搜索量(实测)/排名」列，并据低 CTR 词重写 title/description（`SEO-PLAYBOOK.md` §2.3）。
3. **每月维护**：结合 Google Play Console「获客 → 商店列表 → 搜索关键字/来源」+ GSC 实际词，新增/调整/降权关键词，并在 §2.4 维护日志登记。
4. **防自相残杀（cannibalization）**：同词只由一篇主吃，其余内链导流，不两篇抢同一词（见 `SEO-PLAYBOOK.md` §3 / §7.2）。

### 0.1 词层定义
| 词层 | 含义 | 难度 | 流量 | 转化 | 主吃页型 |
|---|---|---|---|---|---|
| **Head** | 品类大词（品类名本身） | 高 | 高 | 低 | Pillar 品类落地页 |
| **Middle** | 带修饰/场景的中词 | 中 | 中 | 中 | vs / Best / Alternatives |
| **Long-tail** | 精准长尾（功能/场景/意图明确） | 低 | 低–中 | 高 | App 详情页 / How-to |

### 0.2 优先级定义
| 优先级 | 含义 | 动作 |
|---|---|---|
| **P0** | 品牌词 + 高意图长尾（直接转化） | App 详情页必吃；全文高频自然出现 |
| **P1** | 中难度 + 中意图（vs/Best/Alternatives 主攻） | 对应集群页主标题/对比表覆盖 |
| **P2** | 高难度 Head 大词（长期积累） | Pillar 页逐步沉淀，不急于排名 |

### 0.3 字段说明（每条关键词一行）
`关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注`
- **预估流量**：相对值 高/中/低（绝对量待 GSC/Play Console 回填至「搜索量(实测)」）。
- **购买意图**：高/中/低（是否接近下载/付费决策）。
- **当前覆盖**：`已覆盖(文件名)` 或 `待覆盖`。
- **数据来源**：`站内已覆盖` / `竞品调研` / `GSC实测(待回填)` / `Play Console(待回填)`。

---

## 1. 全 App 关键词索引（种子总览）

> 完整展开见各 App 小节；本表给全站词源地图。种子词取自 `SEO-PLAYBOOK.md` §2.1.1，其余 App 待按 §2 模板展开。

| App（英） | 中文名 | 核心 Head 词（en） | 核心 Head 词（zh） | 关键词状态 |
|---|---|---|---|---|
| **Meow Money Manager** | 喵窝记账 | expense tracker / budget app / money manager | 记账软件 / 记账应用 / 预算管理 | ✅ 已完整展开（§2） |
| Meow Todo | — | to-do list / task manager / schedule planner | 待办 / 任务管理 | ☐ 待展开（种子见 §2.1.1） |
| Meow Mood Diary | — | mood diary / journal / safe place | 心情日记 / 日记本 | ☐ 待展开 |
| Meow Habits | — | habit tracker / habit building / routine | 习惯养成 / 打卡 | ☐ 待展开 |
| One Widget | — | home screen widgets / Material You / clock widget | 桌面小组件 | ☐ 待展开 |
| Only Clock | — | full-screen clock / flip animation / nightstand clock | 翻页时钟 / 整点钟 | ☐ 待展开 |
| CPU Monitor | — | cpu temperature / cpu frequency / ram widget | CPU 温度 / 手机降温 | ☐ 待展开 |
| System Monitor | — | cpu monitor / storage cleaner / memory booster | 系统清理 / 内存加速 | ☐ 待展开 |
| Floating Assistant | — | assistive touch / floating clock / floating monitor | 悬浮球 / 悬浮窗 | ☐ 待展开 |
| Meow FM | — | white noise / sleep / relax / concentrate | 白噪音 / 助眠 | ☐ 待展开 |
| Crosshair Aim | — | crosshair / FPS games / aim / overlay | 准星 / 射击辅助 | ☐ 待展开 |

---

## 2. Meow Money Manager（喵窝记账）关键词记录

**品牌**：Meow Money Manager（英）/ 喵窝记账（中，品牌中文名）
**品类**：记账 / 预算管理 / 报销管理（Expense Tracker / Budget Management / Reimbursement）
**核心卖点（用于长尾词构造）**：无账号、本地存储、隐私、多币种符号、离线记账、主屏小组件、指纹锁、CSV 导出、报销追踪、可爱猫主题、免费核心。

### 2.1 英文（en）

#### 2.1.1 Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| expense tracker app | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 站内已覆盖 | 品类根词 |
| budget app | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 站内已覆盖 | 与上为双根词 |
| money manager app | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar/app) | 站内已覆盖 | 品牌名含此词 |
| expense tracker | Head | P2 | 高 | 低 | Pillar | 已覆盖(glossary) | 站内已覆盖 | Glossary 命中 AI |
| budgeting app | Head | P2 | 中 | 中 | Pillar | 待覆盖 | 竞品调研 | 同义变体 |

#### 2.1.2 Middle（中词，P1，vs/Best/Alternatives 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| free budget app | Middle | P1 | 高 | 中 | Best/App | 已覆盖(android/students/app) | 站内已覆盖 | 高量转化词 |
| private expense tracker | Middle | P1 | 中 | 高 | vs/App | 已覆盖(vs/app) | 站内已覆盖 | 隐私卖点 |
| cute budget app | Middle | P1 | 中 | 中 | App | 已覆盖(app) | 站内已覆盖 | 差异化猫主题 |
| multi-currency budget app | Middle | P1 | 中 | 高 | App/Pillar | 已覆盖(pillar/app) | 站内已覆盖 | 多币种符号 |
| offline budget app | Middle | P1 | 中 | 高 | App/Android | 已覆盖(android/app) | 站内已覆盖 | 离线记账 |
| budget app for Android | Middle | P1 | 高 | 中 | Android/Best | 已覆盖(android/pillar) | 站内已覆盖 | 平台限定 |
| budget app for students | Middle | P1 | 中 | 中 | Students | 已覆盖(students) | 站内已覆盖 | 场景限定 |
| best budget app 2026 | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/title) | 站内已覆盖 | 年度词（年度刷新） |
| YNAB alternative | Middle | P1 | 中 | 高 | vs/Mint替代 | 已覆盖(vs/mint) | 竞品调研 | 抢竞品流量 |
| Mint alternative | Middle | P1 | 高 | 高 | Mint替代 | 已覆盖(mint) | 竞品调研 | Mint 关停红利 |

#### 2.1.3 Long-tail（精准长尾，P0，App 详情页主吃）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| budget app no account required | Long-tail | P0 | 中 | 高 | App | 已覆盖(app/FAQ) | 站内已覆盖 | 无账号卖点 |
| expense tracker private no cloud | Long-tail | P0 | 中 | 高 | App/vs | 已覆盖(vs/app) | 站内已覆盖 | 本地存储 |
| expense tracker with fingerprint lock | Long-tail | P0 | 低 | 高 | App | 已覆盖(app) | 站内已覆盖 | 指纹锁 |
| multi-currency expense tracker app | Long-tail | P0 | 中 | 高 | App/Pillar | 已覆盖(pillar/app) | 站内已覆盖 | 多币种 |
| budget app for couples | Long-tail | P0 | 中 | 高 | App/vs | 已覆盖(vs) | 竞品调研 | 跨境伴侣场景 |
| expense tracker with CSV export | Long-tail | P0 | 中 | 高 | App/Tutorial | 已覆盖(tutorial/app) | 站内已覆盖 | 导出 |
| reimbursement tracker app | Long-tail | P0 | 中 | 高 | App/Tutorial | 已覆盖(tutorial/app) | 站内已覆盖 | 报销管理 |
| offline expense tracker Android | Long-tail | P0 | 中 | 高 | Android/App | 已覆盖(android/app) | 站内已覆盖 | 离线+平台 |
| cute expense tracker cat | Long-tail | P0 | 低 | 中 | App | 已覆盖(app) | 站内已覆盖 | 猫主题差异化 |
| expense tracker local storage | Long-tail | P0 | 中 | 高 | App/vs | 已覆盖(vs/app) | 站内已覆盖 | 本地优先 |
| budget app Android widget | Long-tail | P0 | 中 | 中 | Android/App | 已覆盖(android/app) | 站内已覆盖 | 小组件 |
| subscription tracker app | Long-tail | P1 | 中 | 高 | App | 待覆盖 | 竞品调研 | 循环交易场景 |
| best private budget app | Long-tail | P1 | 中 | 高 | vs/App | 已覆盖(vs) | 竞品调研 | 隐私+best |

#### 2.1.4 品牌词 & 竞品替代词
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| Meow Money Manager | 品牌 | P0 | 中 | 高 | App | 已覆盖(app/全站) | 站内已覆盖 | 自有品牌，必守 |
| Meow Money | 品牌 | P0 | 低 | 高 | App | 已覆盖(app) | 站内已覆盖 | 简称 |
| YNAB vs Meow Money Manager | 竞品对比 | P0 | 中 | 高 | vs | 已覆盖(vs) | 竞品调研 | 对比拦截 |
| best Mint alternative 2026 | 竞品替代 | P1 | 高 | 高 | Mint替代 | 已覆盖(mint) | 竞品调研 | Mint 红利 |
| PocketGuard alternative | 竞品替代 | P1 | 低 | 高 | Pillar | 已覆盖(pillar) | 竞品调研 | 待强化 |

### 2.2 中文（zh）

> 本地化选词（非英文直译）：中文用户搜「记账软件/记账应用」而非 "expense tracker"；「喵窝记账」为品牌中文名。

#### 2.2.1 Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 记账软件 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 站内已覆盖 | 品类根词 |
| 记账应用 | Head | P2 | 高 | 中 | Pillar/Glossary | 已覆盖(pillar-zh/glossary) | 站内已覆盖 | 同义根词 |
| 记账app | Head | P2 | 高 | 中 | App/Pillar | 已覆盖(app-zh) | 站内已覆盖 | 移动场景 |
| 预算管理 | Head | P2 | 中 | 中 | Pillar/Glossary | 已覆盖(pillar-zh/glossary) | 站内已覆盖 | 第二品类 |
| 记账 | Head | P2 | 高 | 低 | Pillar | 已覆盖(pillar-zh) | 站内已覆盖 | 极短根词 |

#### 2.2.2 Middle（中词，P1，vs/Best/Alternatives 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 安卓记账 | Middle | P1 | 高 | 中 | Android/Best | 已覆盖(android-zh) | 站内已覆盖 | 平台限定 |
| 免费记账软件 | Middle | P1 | 高 | 中 | Best/App | 已覆盖(android/students-zh) | 站内已覆盖 | 高量转化 |
| 隐私记账 | Middle | P1 | 中 | 高 | vs/App | 已覆盖(vs-zh/app) | 站内已覆盖 | 隐私卖点 |
| 多币种记账 | Middle | P1 | 中 | 高 | App/Pillar | 已覆盖(pillar-zh/app) | 站内已覆盖 | 多币种符号 |
| 离线记账 | Middle | P1 | 中 | 高 | App/Android | 已覆盖(android-zh/app) | 站内已覆盖 | 离线 |
| 学生记账 | Middle | P1 | 中 | 中 | Students | 已覆盖(students-zh) | 站内已覆盖 | 场景限定 |
| 记账软件推荐 | Middle | P1 | 高 | 中 | Best/Pillar | 已覆盖(pillar-zh) | 站内已覆盖 | 清单词 |
| 最好用的记账app | Middle | P1 | 高 | 中 | Best/Pillar | 已覆盖(pillar-zh/title) | 站内已覆盖 | 年度词 |
| 猫主题记账 | Middle | P1 | 低 | 中 | App | 已覆盖(app-zh) | 站内已覆盖 | 差异化 |
| YNAB 替代 | Middle | P1 | 中 | 高 | vs/Mint替代 | 已覆盖(vs-zh/mint-zh) | 竞品调研 | 抢竞品 |
| Mint 替代 | Middle | P1 | 高 | 高 | Mint替代 | 已覆盖(mint-zh) | 竞品调研 | Mint 红利 |
| 报销记账 | Middle | P1 | 中 | 高 | App/Tutorial | 已覆盖(tutorial-zh/app) | 站内已覆盖 | 报销管理 |

#### 2.2.3 Long-tail（精准长尾，P0，App 详情页主吃）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 不用注册账号的记账软件 | Long-tail | P0 | 中 | 高 | App | 已覆盖(app-zh/FAQ) | 站内已覆盖 | 无账号 |
| 本地存储记账 app | Long-tail | P0 | 中 | 高 | App/vs | 已覆盖(vs-zh/app) | 站内已覆盖 | 本地优先 |
| 多币种记账软件 | Long-tail | P0 | 中 | 高 | App/Pillar | 已覆盖(pillar-zh/app) | 站内已覆盖 | 多币种 |
| 学生免费记账 | Long-tail | P0 | 中 | 高 | Students/App | 已覆盖(students-zh/app) | 站内已覆盖 | 场景 |
| 报销记账 app | Long-tail | P0 | 中 | 高 | App/Tutorial | 已覆盖(tutorial-zh/app) | 站内已覆盖 | 报销 |
| 带指纹锁的记账 | Long-tail | P0 | 低 | 高 | App | 已覆盖(app-zh) | 站内已覆盖 | 指纹锁 |
| 记账软件 导出 csv | Long-tail | P0 | 中 | 高 | App/Tutorial | 已覆盖(tutorial-zh/app) | 站内已覆盖 | 导出 |
| 隐私记账 不用云账号 | Long-tail | P0 | 中 | 高 | App/vs | 已覆盖(vs-zh/app) | 站内已覆盖 | 隐私+本地 |
| 安卓 记账 小组件 | Long-tail | P0 | 中 | 中 | Android/App | 已覆盖(android-zh/app) | 站内已覆盖 | 小组件 |
| 喵窝记账 | 品牌 | P0 | 中 | 高 | App | 已覆盖(app-zh/全站) | 站内已覆盖 | 品牌中文名必守 |

#### 2.2.4 品牌词 & 竞品替代词（zh）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 喵窝记账 | 品牌 | P0 | 中 | 高 | App | 已覆盖(app-zh/全站) | 站内已覆盖 | 品牌中文名 |
| Meow Money Manager 对比 YNAB | 竞品对比 | P0 | 中 | 高 | vs | 已覆盖(vs-zh) | 竞品调研 | 对比拦截 |
| 最好用的记账应用 2026 | 竞品替代 | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh/title) | 站内已覆盖 | 年度词 |
| 最佳 Mint 替代 | 竞品替代 | P1 | 高 | 高 | Mint替代 | 已覆盖(mint-zh) | 竞品调研 | Mint 红利 |

### 2.3 竞品拦截词（抢竞品品牌流量）
| 竞品 | 拦截词（en） | 拦截词（zh） | 目标页型 | 当前覆盖 |
|---|---|---|---|---|
| Mint（已关停） | Mint alternative / best Mint alternative 2026 | Mint 替代 / 最佳 Mint 替代 | Mint替代页 | ✅ 已覆盖(mint/mint-zh) |
| YNAB | YNAB alternative / YNAB vs Meow Money Manager | YNAB 替代 / Meow Money Manager 对比 YNAB | vs页 | ✅ 已覆盖(vs/vs-zh) |
| PocketGuard | PocketGuard alternative | PocketGuard 替代 | Pillar | 🟡 已提及，待强化 |
| Goodbudget | Goodbudget alternative | Goodbudget 替代 | Students | 🟡 已提及，待强化 |
| EveryDollar | EveryDollar alternative | EveryDollar 替代 | Pillar | 🟡 已并入对比段 |
| Expensify | Expensify alternative（报销场景） | Expensify 替代 | App/报销 | ☐ 待覆盖 |

### 2.4 维护日志 & Google Play 数据回填区

> **每月动作**：从 Google Play Console（获客 → 商店列表 → 搜索关键字 / 搜索来源）与 GSC（`tools/gsc_export.py`）导出真实词，回填下表并调整 §2.1/§2.2 的「搜索量(实测)/排名/优先级」。

| 月份 | 数据来源 | 新增/升权关键词 | 降权/删除关键词 | 备注 |
|---|---|---|---|---|
| 2026-11 | 站内已覆盖 + 竞品调研（初版） | （建库） | — | 首版基于站内内容+竞品调研；绝对量待 Play Console/GSC 回填 |
| _待填_ | Google Play Console | | | |
| _待填_ | GSC 实际点击词 | | | |

**回填字段模板**（每条关键词补充两列，月度更新）：
`搜索量(实测)`（来自 Play Console/GSC，绝对数）｜ `当前平均排名`（GSC）。

---

## 2.5 Meow Todo（待办清单）关键词记录

**品牌**：Meow Todo List（en/zh 同，无独立中文品牌名，正文统一用 "Meow Todo List"）
**品类**：待办清单 / 任务管理 / 子任务（To-Do List / Task Manager / Subtask）
**核心卖点（长尾词构造）**：日历视图、子任务、提醒、Google Drive/WebDav 同步、离线、指纹锁、400+ 可爱图标、免费核心、学生友好、简单不订阅、可爱 UI。

### 2.5.1 英文（en）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| to-do list app | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 品类根词 |
| task manager app | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 双根词 |
| task management app | Head | P2 | 中 | 中 | Pillar | 待覆盖 | 竞品调研 | 同义 |
| checklist app | Head | P2 | 中 | 低 | Pillar | 待覆盖 | 竞品调研 | 同义变体 |

#### Middle（中词，P1，vs/Best/Alternatives 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| best to-do list app for Android | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | 年度词 |
| best task manager Android | Middle | P1 | 高 | 中 | Best | 已覆盖(best-android) | 竞品调研 | |
| free task management app | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best/pillar) | 竞品调研 | |
| offline to-do app | Middle | P1 | 中 | 高 | App/Pillar | 已覆盖(pillar/app) | 竞品调研 | 离线卖点 |
| simple to-do app | Middle | P1 | 中 | 中 | App | 已覆盖(app) | 竞品调研 | 简单卖点 |
| cute to-do app | Middle | P1 | 中 | 中 | App | 已覆盖(app) | 竞品调研 | 差异化 |
| to-do app with calendar | Middle | P1 | 中 | 高 | App/Pillar | 已覆盖(pillar/app) | 竞品调研 | 日历视图 |
| to-do app with subtasks | Middle | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 子任务 |
| to-do app with reminders | Middle | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 提醒 |

#### Long-tail（精准长尾，P0，App 详情页主吃）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| free todoist alternative | Long-tail | P0 | 高 | 高 | vs/Alternatives | 已覆盖(vs/alt) | 竞品调研 | 抢竞品 |
| best free to-do list app | Long-tail | P0 | 高 | 高 | Best/Pillar | 已覆盖(pillar/best) | 竞品调研 | |
| offline to-do list app android | Long-tail | P0 | 中 | 高 | Android/App | 已覆盖(android/app) | 竞品调研 | |
| to-do app for students | Long-tail | P0 | 中 | 高 | Students/App | 已覆盖(students/app) | 竞品调研 | |
| cute task manager android | Long-tail | P0 | 中 | 中 | App | 已覆盖(app) | 竞品调研 | |
| to-do app with fingerprint lock | Long-tail | P0 | 低 | 高 | App | 已覆盖(app) | 竞品调研 | 指纹锁 |
| to-do app google drive sync | Long-tail | P0 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 同步 |
| simple offline task manager | Long-tail | P0 | 中 | 高 | App/Pillar | 已覆盖(pillar/app) | 竞品调研 | |
| task manager with subtasks free | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | |

#### 品牌词 & 竞品替代词（en）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| Meow Todo List | 品牌 | P0 | 中 | 高 | App | 已覆盖(app/全站) | 站内已覆盖 | 自有品牌 |
| Todoist alternative | 竞品 | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 Todoist |
| TickTick alternative | 竞品 | P1 | 中 | 高 | Pillar | 已覆盖(pillar) | 竞品调研 | 抢 TickTick |
| Microsoft To Do alternative | 竞品 | P1 | 中 | 高 | Pillar | 待覆盖 | 竞品调研 | 抢 MS To Do |
| Google Tasks alternative | 竞品 | P1 | 中 | 高 | Pillar | 待覆盖 | 竞品调研 | 抢 Google Tasks |

### 2.5.2 中文（zh）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 待办清单 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | 品类根词 |
| 待办清单app | Head | P2 | 高 | 中 | Pillar/App | 已覆盖(pillar-zh/app) | 竞品调研 | |
| 任务管理 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | 双根词 |
| 任务管理软件 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 日程管理app | Head | P2 | 中 | 中 | Pillar | 待覆盖 | 竞品调研 | 同义 |

#### Middle（中词，P1）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 最佳安卓待办清单 | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh) | 竞品调研 | 年度词 |
| 待办清单 应用 推荐 | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh) | 竞品调研 | |
| 学生 待办清单 | Middle | P1 | 中 | 中 | Students | 已覆盖(students-zh) | 竞品调研 | |
| 免费 待办清单 | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 可爱 待办app | Middle | P1 | 中 | 中 | App | 已覆盖(app-zh) | 竞品调研 | 差异化 |
| 离线 待办 | Middle | P1 | 中 | 高 | App/Pillar | 已覆盖(pillar-zh/app) | 竞品调研 | |
| 待办清单 子任务 | Middle | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | |
| 待办清单 日历视图 | Middle | P1 | 中 | 高 | App/Pillar | 已覆盖(pillar-zh/app) | 竞品调研 | |
| 待办清单 排行榜 | Middle | P1 | 中 | 中 | Pillar | 待覆盖 | 竞品调研 | 榜单词 |

#### Long-tail（精准长尾，P0）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 待办清单 app 哪个好 | Long-tail | P0 | 高 | 高 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | |
| 安卓 待办清单 推荐 | Long-tail | P0 | 中 | 高 | Android/App | 已覆盖(android-zh/app) | 竞品调研 | |
| 学生 免费 待办 | Long-tail | P0 | 中 | 高 | Students/App | 已覆盖(students-zh/app) | 竞品调研 | |
| 待办清单 指纹锁 | Long-tail | P0 | 低 | 高 | App | 已覆盖(app-zh) | 竞品调研 | |
| 待办清单 子任务 免费 | Long-tail | P0 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | |
| 滴答清单 替代 | Long-tail | P0 | 中 | 高 | vs/Alt | 🟡 待强化 | 竞品调研 | 抢 TickTick(滴答清单) |
| 微软待办 替代 | Long-tail | P0 | 中 | 高 | Pillar | 🟡 待强化 | 竞品调研 | 抢 Microsoft To Do |
| 待办清单 谷歌同步 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | |

### 2.5.3 竞品拦截词（zh 重点）
| 竞品（中文） | 拦截词 | 目标页型 | 当前覆盖 |
|---|---|---|---|
| 滴答清单（TickTick） | 滴答清单 替代 / 滴答清单 哪个好 | vs/Pillar | 🟡 待强化 |
| 微软待办（Microsoft To Do） | 微软待办 替代 | Pillar | 🟡 待强化 |
| 番茄ToDo | 番茄ToDo 替代 | Pillar | ☐ 待覆盖 |
| Todoist（待办事项） | Todoist 替代 | vs/Alt | ✅ 已覆盖(vs/alt-zh) |

### 2.5.4 维护日志
| 月份 | 数据来源 | 新增/升权 | 降权/删除 | 备注 |
|---|---|---|---|---|
| 2026-11 | 竞品调研（web）+ 站内已覆盖 | （初版建库） | — | 绝对量待 Play Console/GSC 回填；中文竞品 滴答清单/微软待办 拦截词待在 vs/pillar 强化 |

---

## 2.6 Meow Habits（习惯打卡）关键词记录

**品牌**：Meow Habits（en/zh 同，无独立中文品牌名，正文统一用 "Meow Habits"）
**品类**：习惯打卡 / 习惯养成 / 自律 / 连续打卡（Habit Tracker / Habit Tracking / Streak）
**核心卖点（长尾词构造）**：猫主题可爱 UI、400+ 分类图标、连续天数(streak)、提醒、完成率/完美周进度图、日历、习惯分类、免账号、数据留本机、CSV 导出、WebDav/Google Drive 备份、免费核心、小组件。

### 2.6.1 英文（en）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| habit tracker app | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 品类根词 |
| habit tracking app | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| daily habit tracker | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| streak app | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 连续打卡 |
| habit tracker | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 双根词 |

#### Middle（中词，P1，Best/vs/Alternatives 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| best habit tracker app for Android | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | 年度词 |
| free habit tracker app | Middle | P1 | 高 | 高 | Best/App | 已覆盖(best/app) | 竞品调研 | 免费卖点 |
| habit tracker with reminders | Middle | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 提醒 |
| habit tracker with widgets | Middle | P1 | 中 | 中 | App | 已覆盖(app) | 竞品调研 | 小组件 |
| offline habit tracker | Middle | P1 | 中 | 高 | App/Pillar | 已覆盖(pillar/app) | 竞品调研 | 离线 |
| habit tracker no account | Middle | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 免账号 |
| cute habit tracker | Middle | P1 | 中 | 中 | App | 已覆盖(app) | 竞品调研 | 差异化 |
| habit tracker with calendar | Middle | P1 | 中 | 高 | App/Pillar | 已覆盖(pillar/app) | 竞品调研 | 日历 |

#### Long-tail（精准长尾，P0，App/Alternatives 主吃）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| free habit tracker app no subscription | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app) | 竞品调研 | 无订阅 |
| best free habit tracker Android | Long-tail | P0 | 中 | 高 | Android/App | 已覆盖(android/app) | 竞品调研 | |
| habit tracker offline no account | Long-tail | P0 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | |
| Streaks alternative | Long-tail | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 Streaks |
| Loop Habit Tracker alternative | Long-tail | P1 | 中 | 高 | vs/Alt | 🟡 待强化 | 竞品调研 | 抢 Loop |
| Habitica alternative | Long-tail | P1 | 中 | 高 | vs/Alt | 🟡 待强化 | 竞品调研 | 抢 Habitica |
| habit tracker with csv export | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | CSV |
| habit tracker with webdav backup | Long-tail | P1 | 低 | 高 | App | 已覆盖(app) | 竞品调研 | 备份 |

#### 品牌词 & 竞品替代词（en）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| Meow Habits | 品牌 | P0 | 中 | 高 | App | 已覆盖(app/全站) | 站内已覆盖 | 自有品牌 |
| Streaks alternative | 竞品 | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 Streaks |
| Habitica alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 🟡 待强化 | 竞品调研 | 抢 Habitica |
| Habitify alternative | 竞品 | P1 | 中 | 高 | Pillar | 待覆盖 | 竞品调研 | 抢 Habitify |
| Fabulous alternative | 竞品 | P1 | 中 | 高 | Pillar | 待覆盖 | 竞品调研 | 抢 Fabulous |

### 2.6.2 中文（zh）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 习惯打卡 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | 品类根词 |
| 习惯养成 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 习惯追踪 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 自律 app | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 打卡软件 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | 同义 |

#### Middle（中词，P1）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 习惯打卡 应用 推荐 | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh) | 竞品调研 | 年度词 |
| 安卓 习惯打卡 | Middle | P1 | 高 | 中 | Android/App | 已覆盖(android-zh/app) | 竞品调研 | |
| 免费 习惯打卡 | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 自律 软件 推荐 | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh) | 竞品调研 | |
| 习惯养成 app | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 习惯打卡 小部件 | Middle | P1 | 中 | 中 | App | 已覆盖(app-zh) | 竞品调研 | 小组件 |

#### Long-tail（精准长尾，P0）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 习惯打卡 app 哪个好 | Long-tail | P0 | 高 | 高 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | |
| 小日常 替代 | Long-tail | P0 | 中 | 高 | vs/Alt | 🟡 待强化 | 竞品调研 | 抢 小日常 |
| 习惯打卡 免费 | Long-tail | P0 | 中 | 高 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 自律 打卡 软件 | Long-tail | P0 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | |
| 习惯养成 安卓 | Long-tail | P0 | 中 | 高 | Android/App | 已覆盖(android-zh/app) | 竞品调研 | |
| 不订阅 习惯打卡 | Long-tail | P0 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 无订阅 |
| 打卡 小日常 类似 | Long-tail | P1 | 中 | 高 | Pillar | 🟡 待强化 | 竞品调研 | 抢 小日常 |

#### 竞品拦截词（zh 重点）
| 竞品（中文） | 拦截词 | 目标页型 | 当前覆盖 |
|---|---|---|---|
| 小日常（打卡小日常/小日常生活） | 小日常 替代 / 小日常 哪个好 | vs/Pillar | 🟡 待强化 |
| 小习惯 app | 小习惯 替代 | vs/Pillar | ☐ 待覆盖 |
| 种子习惯 | 种子习惯 替代 | vs/Pillar | ☐ 待覆盖 |
| 自律树 | 自律树 替代 | vs/Pillar | ☐ 待覆盖 |
| 习惯足迹 | 习惯足迹 替代 | vs/Pillar | ☐ 待覆盖 |

### 2.6.3 维护日志
| 月份 | 数据来源 | 新增/升权 | 降权/删除 | 备注 |
|---|---|---|---|---|
| 2026-11 | 竞品调研（web）+ 站内已覆盖 | （初版建库） | — | 绝对量待 Play Console/GSC 回填；中文竞品 小日常/小习惯 拦截词待在 vs/pillar 强化 |

---

## 2.7 Meow Mood Diary（心情日记）关键词记录

**品牌**：Meow Mood Diary（en/zh 同，中文品牌名待确认；正文统一用 "Meow Mood Diary"）
**品类**：心情日记 / 情绪记录 / 情绪追踪 / 心情树洞 / 每日打卡（Mood Tracker / Mood Diary / Journal）
**核心卖点（长尾词构造）**：猫主题可爱 UI、两步打卡（选心情+活动）、表情/评分量表、活动标签、文字与照片笔记、图表与相关分析、日历热力图、免账号、数据留本机、CSV 导出、WebDav/Google 备份、免费核心。

### 2.7.1 英文（en）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| mood tracker app | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 品类根词 |
| mood tracker | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| mood diary | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| journal app | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 双根词 |
| daily mood log | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| emotion tracker | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |

#### Middle（中词，P1，Best/vs/Alternatives 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| best mood tracker app | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | 年度词 |
| mood tracker Android | Middle | P1 | 高 | 中 | Pillar/App | 已覆盖(pillar/app) | 竞品调研 | |
| mood journal app | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | |
| free mood tracker | Middle | P1 | 高 | 高 | Best/App | 已覆盖(best/app) | 竞品调研 | 免费卖点 |
| mood diary app | Middle | P1 | 中 | 中 | App | 已覆盖(app) | 竞品调研 | |
| mood tracker with charts | Middle | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 图表 |
| daily check-in app | Middle | P1 | 中 | 中 | App | 已覆盖(app) | 竞品调研 | |

#### Long-tail（精准长尾，P0，App/Alternatives 主吃）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| best free mood tracker | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app) | 竞品调研 | 无订阅 |
| Daylio alternative | Long-tail | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 Daylio |
| mood tracker no subscription | Long-tail | P0 | 中 | 高 | Best/App | 已覆盖(app) | 竞品调研 | |
| mood tracker offline | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | |
| mood tracker with export | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | CSV |
| mood tracker private no account | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 免账号 |
| mood and habit tracker | Long-tail | P1 | 中 | 中 | App | 已覆盖(app) | 竞品调研 | 与 Habits 联动 |

#### 品牌词 & 竞品替代词（en）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| Meow Mood Diary | 品牌 | P0 | 中 | 高 | App | 已覆盖(app/全站) | 站内已覆盖 | 自有品牌 |
| Daylio alternative | 竞品 | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 Daylio |
| MoodKit alternative | 竞品 | P1 | 中 | 高 | Pillar | 待覆盖 | 竞品调研 | 抢 MoodKit |
| Bearable alternative | 竞品 | P1 | 中 | 高 | Pillar | 待覆盖 | 竞品调研 | 抢 Bearable |
| Journey alternative | 竞品 | P1 | 中 | 高 | Pillar | 待覆盖 | 竞品调研 | 抢 Journey |
| Reflectly alternative | 竞品 | P1 | 中 | 高 | Pillar | 待覆盖 | 竞品调研 | 抢 Reflectly |

### 2.7.2 中文（zh）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 心情日记 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | 品类根词 |
| 情绪记录 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 心情追踪 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 情绪追踪 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 日记 app | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | 双根词 |
| 心情笔记 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |

#### Middle（中词，P1）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 心情日记 app 推荐 | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh) | 竞品调研 | 年度词 |
| 情绪记录 安卓 | Middle | P1 | 高 | 中 | Android/App | 已覆盖(android-zh/app) | 竞品调研 | |
| 心情追踪 应用 | Middle | P1 | 中 | 中 | Pillar/App | 已覆盖(pillar-zh/app) | 竞品调研 | |
| 免费 心情日记 | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 心情日记 隐私 | Middle | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | |

#### Long-tail（精准长尾，P0）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 心情日记 app 哪个好 | Long-tail | P0 | 高 | 高 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | |
| Daylio 替代 | Long-tail | P0 | 中 | 高 | vs/Alt | 🟡 待强化 | 竞品调研 | 抢 Daylio |
| 心情日记 免费 | Long-tail | P0 | 中 | 高 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 情绪记录 安卓 | Long-tail | P0 | 中 | 高 | Android/App | 已覆盖(android-zh/app) | 竞品调研 | |
| 心情日记 不订阅 | Long-tail | P0 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 无订阅 |
| 卡片日记 替代 | Long-tail | P1 | 中 | 高 | Pillar | 🟡 待强化 | 竞品调研 | 抢 格志/卡片日记 |

#### 竞品拦截词（zh 重点）
| 竞品（中文） | 拦截词 | 目标页型 | 当前覆盖 |
|---|---|---|---|
| Daylio（日记/心情） | Daylio 替代 / Daylio 哪个好 | vs/Pillar | 🟡 待强化 |
| MOODA心情日记 | MOODA 替代 | vs/Pillar | ☐ 待覆盖 |
| moo日记 | moo日记 替代 | vs/Pillar | ☐ 待覆盖 |
| 情绪指压心情日记（Moodpress） | 情绪指压 替代 | vs/Pillar | ☐ 待覆盖 |
| 格志 / 卡片日记 | 卡片日记 替代 | vs/Pillar | ☐ 待覆盖 |
| 心岛日记 | 心岛日记 替代 | vs/Pillar | ☐ 待覆盖 |

### 2.7.3 维护日志
| 月份 | 数据来源 | 新增/升权 | 降权/删除 | 备注 |
|---|---|---|---|---|
| 2026-11 | 竞品调研（web）+ 站内已覆盖 | （初版建库） | — | 绝对量待 Play Console/GSC 回填；中文竞品 Daylio/MOODA/moo日记 拦截词待在 vs/pillar 强化 |

---

## 2.8 Meow FM（白噪音 / 专注 / 助眠）关键词记录

**品牌**：Meow FM（en/zh 同，中文品牌名待确认；正文统一用 "Meow FM"）
**品类**：白噪音 / 环境音 / 助眠声音 / 专注音乐 / 放松音景（White Noise / Ambient Sound / Sleep Sounds / Focus Sounds）
**核心卖点（长尾词构造）**：猫主题可爱 UI、高保真音源库（雨声/海浪/篝火/森林/风扇/白噪音/棕噪音/粉红噪音）、声音自由混音、定时关闭/睡眠定时、离线播放、免订阅/免费核心、专注模式、睡眠模式、遮噪助眠。

### 2.8.1 英文（en）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| white noise | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 品类根词 |
| white noise app | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| sleep sounds | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| focus sounds | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| ambient noise | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| noise generator | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |

#### Middle（中词，P1，Best/vs/Alternatives 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| white noise for sleep | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | |
| white noise for focus | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | |
| white noise app Android | Middle | P1 | 高 | 中 | Pillar/App | 已覆盖(pillar/app) | 竞品调研 | |
| sleep sounds app | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | |
| brown noise app | Middle | P1 | 中 | 中 | App | 已覆盖(app) | 竞品调研 | 棕噪音 |
| rain sounds app | Middle | P1 | 高 | 中 | App | 已覆盖(app) | 竞品调研 | |
| focus music | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | |

#### Long-tail（精准长尾，P0，App/Alternatives 主吃）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| best free white noise app | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app) | 竞品调研 | 无订阅 |
| white noise app no subscription | Long-tail | P0 | 中 | 高 | Best/App | 已覆盖(app) | 竞品调研 | |
| white noise offline | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | |
| white noise with timer | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 定时关闭 |
| white noise to block noise | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 遮噪 |
| cat white noise app | Long-tail | P1 | 中 | 中 | App | 已覆盖(app) | 竞品调研 | 品牌特色 |

#### 品牌词 & 竞品替代词（en）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| Meow FM | 品牌 | P0 | 中 | 高 | App | 已覆盖(app/全站) | 站内已覆盖 | 自有品牌 |
| Calm alternative | 竞品 | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 Calm |
| Headspace alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 Headspace |
| Noisli alternative | 竞品 | P1 | 中 | 高 | Pillar/Alt | 待覆盖 | 竞品调研 | 抢 Noisli |
| Brain.fm alternative | 竞品 | P1 | 中 | 高 | Pillar/Alt | 待覆盖 | 竞品调研 | 抢 Brain.fm |
| myNoise alternative | 竞品 | P1 | 中 | 高 | Pillar/Alt | 待覆盖 | 竞品调研 | 抢 myNoise |
| BetterSleep alternative | 竞品 | P1 | 中 | 高 | Pillar/Alt | 待覆盖 | 竞品调研 | 抢 BetterSleep |

### 2.8.2 中文（zh）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 白噪音 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | 品类根词 |
| 白噪音 app | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 助眠 声音 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 专注 音乐 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 睡眠 白噪音 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |

#### Middle（中词，P1）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 白噪音 app 推荐 | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh) | 竞品调研 | 年度词 |
| 助眠 白噪音 | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 专注 白噪音 | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 白噪音 安卓 | Middle | P1 | 高 | 中 | Android/App | 已覆盖(android-zh/app) | 竞品调研 | |
| 睡眠 声音 app | Middle | P1 | 中 | 中 | Pillar/App | 已覆盖(pillar-zh/app) | 竞品调研 | |

#### Long-tail（精准长尾，P0）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 白噪音 app 哪个好 | Long-tail | P0 | 高 | 高 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | |
| 免费 白噪音 app | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 白噪音 不订阅 | Long-tail | P0 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 无订阅 |
| 白噪音 定时关闭 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 睡眠定时 |
| 雨声 白噪音 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | |

#### 竞品拦截词（zh 重点）
| 竞品（中文） | 拦截词 | 目标页型 | 当前覆盖 |
|---|---|---|---|
| 潮汐 (Tide) | 潮汐 替代 / 潮汐 哪个好 | vs/Pillar | 🟡 待强化 |
| 小睡眠 | 小睡眠 替代 | vs/Pillar | ☐ 待覆盖 |
| MUJI to Relax | MUJI to Relax 替代 | vs/Pillar | ☐ 待覆盖 |
| Noisli | Noisli 替代 | vs/Pillar | ☐ 待覆盖 |
| Brain.fm | Brain.fm 替代 | vs/Pillar | ☐ 待覆盖 |
| 白噪音（通用） | 白噪音 替代 | vs/Pillar | 🟡 待强化 |

### 2.8.3 维护日志
| 月份 | 数据来源 | 新增/升权 | 降权/删除 | 备注 |
|---|---|---|---|---|
| 2026-11 | 竞品调研（web）+ 站内已覆盖 | （初版建库） | — | 绝对量待 Play Console/GSC 回填；中文竞品 潮汐/小睡眠 拦截词待在 vs/pillar 强化 |

---

## 2.9 One Widget（安卓桌面小组件）关键词记录

**品牌**：One Widget（en/zh 同；中文品牌名待确认；正文统一用 "One Widget"）
**品类**：安卓桌面小组件 / 自定义小组件 / Material You 小组件 / 玻璃风格小组件 / Nothing 风格小组件 / 组件制作（Android Home Screen Widgets / Custom Widgets / Widget Maker）
**核心卖点（长尾词构造）**：500+ 可定制组件、四大风格（Glass iOS / Material You / Galaxy One UI / Nothing 极简）、应用快捷方式、系统快捷开关（Wi-Fi/蓝牙/手电）、时钟与日历组件、电量/内存组件、设备信息组件、尺寸与背景色/圆角自由自定义、覆盖三星/Pixel/Nothing 等所有安卓、付费（免费含 One UI 主题组件）。

### 2.9.1 英文（en）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| android widgets | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 品类根词 |
| custom widgets | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| home screen widgets | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| widget app | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| android widget maker | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |

#### Middle（中词，P1，Best/vs/Alternatives 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| best android widget app | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | 年度词 |
| android widgets 2026 | Middle | P1 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| material you widgets | Middle | P1 | 高 | 中 | Best/Pillar | 已覆盖(best-zh/pillar) | 竞品调研 | |
| glass widgets android | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | 玻璃风格 |
| nothing widgets | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | Nothing 风格 |
| samsung one ui widgets | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | 三星 |
| ios style widgets android | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | 仿 iOS |

#### Long-tail（精准长尾，P0，App/Best 主吃）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| best widget app for android | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(best/app) | 竞品调研 | |
| custom home screen widgets android | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(best/app) | 竞品调研 | |
| material you widget maker | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(best/app) | 竞品调研 | |
| android clock widget app | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 时钟 |
| android calendar widget app | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 日历 |
| glass style widgets android | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 玻璃风 |
| nothing phone widgets | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | Nothing |
| 500+ widgets android | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 数量卖点 |
| widget with app shortcuts android | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 快捷方式 |
| android widget no subscription | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 无订阅 |

#### 品牌词 & 竞品替代词（en）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| One Widget | 品牌 | P0 | 中 | 高 | App | 已覆盖(app/全站) | 站内已覆盖 | 自有品牌 |
| KWGT alternative | 竞品 | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 KWGT |
| best KWGT alternative android | 竞品 | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | |
| Kustom Widget Maker alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 Kustom |
| Widgetsmith alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 Widgetsmith |
| Chronus alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 Chronus |
| Widgetopia alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Widgetopia |
| Zooper Widget alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Zooper |

### 2.9.2 中文（zh）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 安卓小组件 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | 品类根词 |
| 桌面小组件 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 小组件 app | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 安卓 桌面组件 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 自定义小组件 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |

#### Middle（中词，P1）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 安卓小组件 app 推荐 | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | 年度词 |
| 安卓小组件 制作 | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| Material You 小组件 | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 透明小组件 | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 灵动岛 小组件 | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | 动态岛风 |
| 三星 One UI 小组件 | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 玻璃风格 小组件 | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| Nothing 风格 小组件 | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |

#### Long-tail（精准长尾，P0）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 安卓 桌面小组件 哪个好 | Long-tail | P0 | 高 | 高 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | |
| 安卓 自定义小组件 app | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 安卓 透明小组件 app | Long-tail | P1 | 高 | 高 | App | 已覆盖(app-zh) | 竞品调研 | |
| 安卓 玻璃风格 小组件 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | |
| 安卓 时钟 小组件 app | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 时钟 |
| 安卓 日历 小组件 app | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 日历 |
| 500+ 小组件 安卓 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 数量卖点 |
| 安卓 小组件 不订阅 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 无订阅 |

#### 竞品拦截词（zh 重点）
| 竞品（中文） | 拦截词 | 目标页型 | 当前覆盖 |
|---|---|---|---|
| 小组件盒子 | 小组件盒子 替代 / 小组件盒子 哪个好 | vs/Pillar | 🟡 待强化 |
| 灵动坞 | 灵动坞 替代 | vs/Pillar | 🟡 待强化 |
| 万能小组件 (Top Widgets) | 万能小组件 替代 | vs/Pillar | ☐ 待覆盖 |
| 魔力小组件 | 魔力小组件 替代 | vs/Pillar | ☐ 待覆盖 |
| 元气小组件 | 元气小组件 替代 | vs/Pillar | ☐ 待覆盖 |
| iScreen / 米写 | iScreen 替代 / 米写 替代 | vs/Pillar | ☐ 待覆盖 |
| KWGT 中文 (KustomWidget) | KWGT 中文 替代 | vs/Pillar | ☐ 待覆盖 |

### 2.9.3 维护日志
| 月份 | 数据来源 | 新增/升权 | 降权/删除 | 备注 |
|---|---|---|---|---|
| 2026-11 | 竞品调研（web）+ 站内已覆盖 | （初版建库） | — | 绝对量待 Play Console/GSC 回填；中文竞品 小组件盒子/灵动坞 拦截词待在 vs/pillar 强化 |

---

## 2.10 Only Clock（翻页钟/全屏时钟/床头钟）关键词记录

**品牌**：Only Clock（en/zh 同；中文品牌名待确认；正文统一用 "Only Clock"）
**品类**：翻页钟 / 全屏时钟 / 床头钟 / 桌面钟 / 大字号时钟（Flip Clock / Full Screen Clock / Nightstand Clock / Desk Clock / Big Digital Clock）
**核心卖点（长尾词构造）**：全屏翻页动画、桌面钟/床头钟、学习工作专注计时、时钟小组件、白噪音助专注、12/24 小时与日期显示、黑白主题、闲置手机/iPad 当钟表摆件、极简风格。

### 2.10.1 英文（en）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| flip clock | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 品类根词 |
| full screen clock | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| nightstand clock | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 床头钟 |
| desk clock | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 桌面钟 |
| big digital clock | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 大字号 |
| clock widget | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 与 One Widget 同根 |

#### Middle（中词，P1，Best/vs 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| flip clock app | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | |
| best flip clock app | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | 年度词 |
| android flip clock | Middle | P1 | 高 | 中 | Pillar/App | 已覆盖(pillar/app) | 竞品调研 | |
| nightstand clock app | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | |
| full screen clock android | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | |
| bedside clock app | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | |
| retro flip clock | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | 复古风 |
| flip clock widget | Middle | P1 | 中 | 中 | App | 已覆盖(app) | 竞品调研 | |

#### Long-tail（精准长尾，P0，App/Best 主吃）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| best flip clock app for android | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app) | 竞品调研 | |
| full screen flip clock android | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app) | 竞品调研 | |
| flip clock for desk | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 桌面钟 |
| nightstand clock no ads | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 无广告 |
| flip clock with white noise | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 白噪音 |
| flip clock with focus timer | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 专注计时 |
| use old phone as clock | Long-tail | P1 | 中 | 中 | App/Pillar | 已覆盖(app/pillar) | 竞品调研 | 闲置机当钟 |
| minimalist flip clock | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 极简 |

#### 品牌词 & 竞品替代词（en）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| Only Clock | 品牌 | P0 | 中 | 高 | App | 已覆盖(app/全站) | 站内已覆盖 | 自有品牌 |
| Retroflip Clock alternative | 竞品 | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 Retroflip（主对比） |
| best Retroflip Clock alternative | 竞品 | P0 | 中 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | |
| Flip Clock (Soosu) alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Soosu Flip Clock |
| Fliqlo alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Fliqlo（桌面） |
| Nightdream alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Nightdream（开源） |
| ClockLab alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 ClockLab |
| Google Clock alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Google Clock |
| Digital Clock Widget alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 DCW |

### 2.10.2 中文（zh）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 翻页钟 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | 品类根词 |
| 翻页时钟 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 全屏时钟 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 床头钟 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 大字时钟 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 桌面钟 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |

#### Middle（中词，P1）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 翻页时钟 app | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | |
| 翻页时钟 安卓 | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 床头钟 app | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 全屏时钟 安卓 | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 翻页电子钟 | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 极简时钟 | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 桌面翻页时钟 | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 翻页时钟 哪个好 | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | 年度词 |

#### Long-tail（精准长尾，P0）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 安卓 翻页时钟 哪个好 | Long-tail | P0 | 高 | 高 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | |
| 全屏 翻页时钟 安卓 | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 翻页时钟 无广告 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | |
| 翻页时钟 白噪音 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | |
| 翻页时钟 专注计时 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | |
| 旧手机 当 时钟 | Long-tail | P1 | 中 | 中 | App/Pillar | 已覆盖(app-zh/pillar-zh) | 竞品调研 | 闲置机当钟 |
| 翻页时钟 小组件 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | |
| 大字 极简 时钟 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | |

#### 竞品拦截词（zh 重点）
| 竞品（中文） | 拦截词 | 目标页型 | 当前覆盖 |
|---|---|---|---|
| 翻页时钟 (com.charm) | 翻页时钟 替代 / 翻页时钟 哪个好 | vs/Pillar | 🟡 待强化 |
| 翻页桌面时钟 (com.deepaso) | 翻页桌面时钟 替代 | vs/Pillar | ☐ 待覆盖 |
| 大字时钟 | 大字时钟 替代 | vs/Pillar | ☐ 待覆盖 |
| 翻页时钟24H | 翻页时钟24H 替代 | vs/Pillar | ☐ 待覆盖 |
| 极简时钟 | 极简时钟 替代 | vs/Pillar | ☐ 待覆盖 |
| 谷歌时钟 (Google Clock) | 谷歌时钟 替代 | vs/Pillar | ☐ 待覆盖 |
| Fliqlo | Fliqlo 替代 | vs/Pillar | ☐ 待覆盖 |

### 2.10.3 维护日志
| 月份 | 数据来源 | 新增/升权 | 降权/删除 | 备注 |
|---|---|---|---|---|
| 2026-11 | 竞品调研（web）+ 站内已覆盖 | （初版建库） | — | 绝对量待 Play Console/GSC 回填；中文竞品 翻页时钟(com.charm)/极简时钟 拦截词待在 vs/pillar 强化 |

---

## 2.11 CPU Monitor（CPU/温度/电池监控）关键词记录

**品牌**：CPU Monitor（en/zh 同；中文品牌名"CPU 监测"；正文统一用 "CPU Monitor"）
**品类**：CPU 温度监控 / 手机温度监控 / 系统监测 / 性能监测 / 多核 CPU 监控（CPU Temperature Monitor / CPU Monitor / System Monitor / Phone Temperature Monitor / Performance Monitor）
**核心卖点（长尾词构造）**：实时监控 CPU 温度与频率、RAM、电池与多核占用、状态栏+桌面浮窗、RAM/CPU/电池小组件、一键加速、过热报警、温度/频率历史分析、多主题；Pro 升级为 Powerful System Monitor 全家桶（无 iOS）。

### 2.11.1 英文（en）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| cpu temperature monitor | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 品类根词 |
| cpu monitor | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 品牌/品类 |
| cpu temp | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| android cpu monitor | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| phone temperature monitor | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| cpu usage monitor | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |

#### Middle（中词，P1，Best/vs/Alternatives 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| best cpu temperature monitor app | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | 年度词 |
| best cpu monitor for android | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | |
| cpu temperature monitor android | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | |
| cpu-z alternative | Middle | P1 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 CPU-Z（主对比） |
| phone cpu temp monitor | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | |
| android system monitor | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | |
| cpu monitor with floating window | Middle | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 浮窗 |
| battery temperature monitor | Middle | P1 | 中 | 中 | App | 已覆盖(app) | 竞品调研 | 电池 |

#### Long-tail（精准长尾，P0，App/Best 主吃）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| best cpu temperature monitor app for android | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app) | 竞品调研 | |
| monitor cpu temperature and frequency android | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app) | 竞品调研 | 温度+频率 |
| cpu monitor with floating window android | Long-tail | P0 | 高 | 高 | App | 已覆盖(app) | 竞品调研 | 浮窗 |
| cpu overheat alarm app | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 过热报警 |
| cpu ram battery widget android | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 小组件 |
| multicore cpu monitor android | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 多核 |
| phone cooling app with temperature | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 降温 |
| cpu frequency history monitor | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 历史分析 |

#### 品牌词 & 竞品替代词（en）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| CPU Monitor | 品牌 | P0 | 中 | 高 | App | 已覆盖(app/全站) | 站内已覆盖 | 自有品牌 |
| CPU-Z alternative | 竞品 | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 CPU-Z（主对比） |
| best CPU-Z alternative android | 竞品 | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | |
| DevCheck alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 DevCheck |
| AIDA64 alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 AIDA64 |
| Simple System Monitor alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Simple System Monitor |
| CPU Float alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 CPU Float |
| Cooler Master alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Cooler Master |

### 2.11.2 中文（zh）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 手机cpu温度 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | 品类根词 |
| cpu温度监控 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 手机温度监控 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 安卓cpu监控 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| cpu监测 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 系统监测 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |

#### Middle（中词，P1）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 手机cpu温度监控 app | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | |
| 安卓cpu温度监控 | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 最好的cpu温度监控软件 | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | 年度词 |
| cpu-z 中文 替代 | Middle | P1 | 高 | 高 | vs/Pillar | 已覆盖(vs/pillar-zh) | 竞品调研 | 抢 CPU-Z（主对比） |
| 手机降温软件 | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| cpu监控悬浮窗 | Middle | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 浮窗 |
| 电池温度监控 | Middle | P1 | 中 | 中 | App | 已覆盖(app-zh) | 竞品调研 | 电池 |
| 多核cpu监控 | Middle | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 多核 |

#### Long-tail（精准长尾，P0）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 安卓 手机cpu温度监控 哪个好 | Long-tail | P0 | 高 | 高 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | |
| 监控cpu温度频率 安卓 | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | 温度+频率 |
| cpu监控 悬浮窗 安卓 | Long-tail | P0 | 高 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 浮窗 |
| cpu过热报警 app | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 过热报警 |
| cpu内存电池 小组件 安卓 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 小组件 |
| 手机降温 cpu监控 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 降温 |
| 多核cpu频率监控 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 历史分析 |

#### 竞品拦截词（zh 重点）
| 竞品（中文） | 拦截词 | 目标页型 | 当前覆盖 |
|---|---|---|---|
| CPU-Z 中文 | cpu-z 中文 替代 / cpu-z 中文 哪个好 | vs/Pillar | 🟡 待强化 |
| 鲁大师 | 鲁大师 替代 / 鲁大师 降温 | vs/Pillar | ☐ 待覆盖 |
| 安兔兔 | 安兔兔 替代 / 安兔兔 温度监控 | vs/Pillar | ☐ 待覆盖 |
| CPU监控大师 | CPU监控大师 替代 | vs/Pillar | ☐ 待覆盖 |
| 强力监测 (Powerful Monitor) | 强力监测 替代 | vs/Pillar | ☐ 待覆盖 |
| 手机降温/Cooler Master | 手机降温 替代 | vs/Pillar | ☐ 待覆盖 |
| Device Info HW | Device Info HW 替代 | vs/Pillar | ☐ 待覆盖 |
| AIDA64 中文 | AIDA64 中文 替代 | vs/Pillar | ☐ 待覆盖 |

### 2.11.3 维护日志
| 月份 | 数据来源 | 新增/升权 | 降权/删除 | 备注 |
|---|---|---|---|---|
| 2026-11 | 竞品调研（web）+ 站内已覆盖 | （初版建库） | — | 绝对量待 Play Console/GSC 回填；中文竞品 CPU-Z 中文/鲁大师 拦截词待在 vs/pillar 强化 |

---

## 2.12 System Monitor（系统监控/手机清理/RAM 加速/存储清理）关键词记录

**品牌**：System Monitor（en/zh 同；中文品牌名"系统监控"/"系统管家"；正文统一用 "System Monitor"）
**品类**：系统监控 / 手机清理 / 内存加速 / 存储清理 / 电池医生（System Monitor / Phone Cleaner / RAM Booster / Storage Cleaner / Battery Monitor）
**核心卖点（长尾词构造）**：CPU 温度/频率监控+历史+多核；存储清理（垃圾/缓存）；内存分析+一键加速；电池医生（健康/电压/温度曲线）；过热报警与保护；浮窗+小组件；多主题；免费核心+Pro。同开发者家族（com.glgjing），也是 CPU Monitor Pro 解锁的"Powerful System Monitor"全家桶。

### 2.12.1 英文（en）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| system monitor | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 品类根词 |
| android system monitor | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| phone cleaner | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| ram booster | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| storage cleaner | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| android cleaner | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| battery monitor | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 电池医生 |
| android optimizer | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 一体优化 |

#### Middle（中词，P1，Best/vs/Alternatives 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| best system monitor app | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | 年度词 |
| best phone cleaner for android | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | |
| best ram booster android | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | |
| best storage cleaner android | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | |
| android cleaner app | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | |
| ccleaner alternative | Middle | P1 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 CCleaner（主对比） |
| system monitor with floating window | Middle | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 浮窗 |
| all in one tool android | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | 一体机 |

#### Long-tail（精准长尾，P0，App/Best 主吃）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| best phone cleaner app for android | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app) | 竞品调研 | |
| android system monitor with cleaner and booster | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app) | 竞品调研 | 监控+清理+加速 |
| system monitor cpu ram battery cleaner | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app) | 竞品调研 | 一体 |
| ccleaner alternative for android | Long-tail | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | |
| ram booster with one tap | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 一键加速 |
| storage cleaner junk files android | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | |
| battery monitor with temperature curve | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 电池曲线 |
| floating window system monitor android | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 浮窗 |

#### 品牌词 & 竞品替代词（en）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| System Monitor | 品牌 | P0 | 中 | 高 | App | 已覆盖(app/全站) | 站内已覆盖 | 自有品牌 |
| CCleaner alternative | 竞品 | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 CCleaner（主对比） |
| best CCleaner alternative android | 竞品 | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | |
| AVG Cleaner alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 AVG Cleaner |
| Files by Google alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Files by Google |
| SD Maid alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 SD Maid |
| Clean Master alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Clean Master |
| 3C Toolbox alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 3C Toolbox |

### 2.12.2 中文（zh）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 系统监控 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | 品类根词 |
| 安卓系统监控 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 手机清理 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 内存加速 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 存储清理 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 安卓清理 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 电池医生 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 手机管家 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | 高量泛词 |

#### Middle（中词，P1）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 系统监控 app | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | |
| 最佳手机清理 安卓 | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | |
| 最好用的内存加速 | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 存储清理 哪个好 | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | 年度词 |
| 安卓清理 软件 | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| ccleaner 替代 安卓 | Middle | P1 | 高 | 高 | vs/Pillar | 已覆盖(vs/pillar-zh) | 竞品调研 | 抢 CCleaner（主对比） |
| 系统监控 悬浮窗 | Middle | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 浮窗 |
| 一键加速 清理 | Middle | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | |

#### Long-tail（精准长尾，P0）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 安卓 系统监控 清理 加速 | Long-tail | P0 | 高 | 高 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | 监控+清理+加速 |
| 最好的 手机清理 app 安卓 | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 内存加速 一键清理 安卓 | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| ccleaner 替代 安卓 清理 | Long-tail | P0 | 高 | 高 | vs/Pillar | 已覆盖(vs/pillar-zh) | 竞品调研 | |
| 存储清理 垃圾文件 安卓 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | |
| 电池监控 温度曲线 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 电池曲线 |
| 悬浮窗 系统监控 安卓 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 浮窗 |

#### 竞品拦截词（zh 重点）
| 竞品（中文） | 拦截词 | 目标页型 | 当前覆盖 |
|---|---|---|---|
| CCleaner | ccleaner 替代 / ccleaner 安卓 替代 | vs/Pillar | 🟡 待强化 |
| 360清理大师 | 360清理大师 替代 | vs/Pillar | ☐ 待覆盖 |
| 鲁大师 | 鲁大师 替代 / 鲁大师 清理 | vs/Pillar | ☐ 待覆盖 |
| 腾讯手机管家 | 手机管家 替代 / 腾讯手机管家 替代 | vs/Pillar | ☐ 待覆盖 |
| 百度手机卫士 | 百度手机卫士 替代 | vs/Pillar | ☐ 待覆盖 |
| 猎豹清理大师 | 猎豹清理大师 替代 | vs/Pillar | ☐ 待覆盖 |
| 清浊 | 清浊 替代 | vs/Pillar | ☐ 待覆盖 |
| SD Maid | SD Maid 替代 | vs/Pillar | ☐ 待覆盖 |
| 安卓清理君 | 安卓清理君 替代 | vs/Pillar | ☐ 待覆盖 |

### 2.12.3 维护日志
| 月份 | 数据来源 | 新增/升权 | 降权/删除 | 备注 |
|---|---|---|---|---|
| 2026-11 | 竞品调研（web）+ 站内已覆盖 | （初版建库） | — | 绝对量待 Play Console/GSC 回填；中文竞品 CCleaner/360清理大师/鲁大师/手机管家 拦截词待在 vs/pillar 强化 |

---

## 2.13 Floating Assistant（悬浮助手/悬浮球/辅助触控/单手助手）关键词记录

**品牌**：Floating Assistant（en/zh 同；中文品牌名"浮动助手"/"悬浮助手"；正文统一用 "Floating Assistant"）
**品类**：悬浮助手 / 悬浮球 / 辅助触控 / 单手助手 / 边缘浮动球（Floating Assistant / Assistive Touch / Floating Ball / One-Hand Helper）
**核心卖点（长尾词构造）**：边缘浮动球 + 自定义快捷（应用/联系人/系统开关）；动作集（返回/主页/多任务/锁屏/截屏/分屏）；按钮+手势；单手控制；轻量稳定；核心免费 + VIP。同开发者家族（com.glgjing），与 CPU Monitor / System Monitor 共享品牌体系。

### 2.13.1 英文（en）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| floating assistant | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 品类根词 |
| android floating assistant | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| assistive touch | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 借 iOS 词 |
| floating ball | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| floating button | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| edge floating ball | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |

#### Middle（中词，P1，Best/vs/Alternatives 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| best floating assistant app | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | 年度词 |
| best assistive touch app android | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | |
| best floating ball android | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | |
| floating assistant vs assistive touch | Middle | P1 | 高 | 高 | vs | 已覆盖(vs) | 竞品调研 | 抢 Assistive Touch（主对比） |
| floating button for one hand | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | |
| assistive touch alternative | Middle | P1 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 Assistive Touch（主对比） |
| customizable floating ball android | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | |

#### Long-tail（精准长尾，P0，App/Best 主吃）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| best floating assistant app for android | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app) | 竞品调研 | |
| best assistive touch app for android 2026 | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app) | 竞品调研 | |
| floating button app for one hand android | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app) | 竞品调研 | |
| assistive touch alternative android | Long-tail | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | |
| floating ball with custom shortcuts | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | |
| edge floating ball with gestures | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | |
| floating assistant back home recent button | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 动作集 |

#### 品牌词 & 竞品替代词（en）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| Floating Assistant | 品牌 | P0 | 中 | 高 | App | 已覆盖(app/全站) | 站内已覆盖 | 自有品牌 |
| Assistive Touch alternative | 竞品 | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 Assistive Touch（主对比） |
| best Assistive Touch alternative android | 竞品 | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | |
| Easy Touch alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Easy Touch |
| Floatify alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Floatify |
| Button Mapper alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Button Mapper |
| Simple Control alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Simple Control |

### 2.13.2 中文（zh）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 悬浮助手 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | 品类根词 |
| 安卓悬浮助手 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 悬浮球 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 辅助触控 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | 借 iOS 词 |
| 悬浮按钮 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 单手助手 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 边缘悬浮球 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |

#### Middle（中词，P1）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 最佳悬浮助手 安卓 | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | |
| 最佳辅助触控 安卓 | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | |
| 最好用的悬浮球 | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 悬浮助手 对比 辅助触控 | Middle | P1 | 高 | 高 | vs | 已覆盖(vs) | 竞品调研 | 抢 Assistive Touch（主对比） |
| 单手操作 悬浮球 | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 辅助触控 替代 | Middle | P1 | 高 | 高 | vs/Pillar | 已覆盖(vs/pillar-zh) | 竞品调研 | 抢 Assistive Touch（主对比） |
| 可自定义 悬浮球 安卓 | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |

#### Long-tail（精准长尾，P0）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 最好的 悬浮助手 app 安卓 | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app-zh) | 竞品调研 | |
| 最佳 辅助触控 app 安卓 2026 | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app-zh) | 竞品调研 | |
| 单手操作 悬浮球 安卓 | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app-zh) | 竞品调研 | |
| 辅助触控 替代 安卓 | Long-tail | P0 | 高 | 高 | vs/Pillar | 已覆盖(vs/pillar-zh) | 竞品调研 | |
| 自定义 悬浮球 快捷方式 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | |
| 边缘悬浮球 手势 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | |
| 悬浮助手 返回 主页 最近键 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 动作集 |

#### 竞品拦截词（zh 重点）
| 竞品（中文） | 拦截词 | 目标页型 | 当前覆盖 |
|---|---|---|---|
| Assistive Touch（辅助触摸小白点） | 辅助触控 替代 / assistive touch 中文 替代 | vs/Pillar | 🟡 待强化 |
| 小米悬浮球 | 小米悬浮球 替代 | vs/Pillar | ☐ 待覆盖 |
| 苹果辅助触控 | 苹果辅助触控 替代 | vs/Pillar | ☐ 待覆盖 |
| 小白点 / 安卓小白点 | 小白点 替代 | vs/Pillar | ☐ 待覆盖 |
| 按钮大师 | 按钮大师 替代 | vs/Pillar | ☐ 待覆盖 |
| 悬浮助手SoftCircle | 悬浮助手SoftCircle 替代 | vs/Pillar | ☐ 待覆盖 |
| 白开水悬浮助手 | 白开水悬浮助手 替代 | vs/Pillar | ☐ 待覆盖 |
| fooview悬浮球 | fooview悬浮球 替代 | vs/Pillar | ☐ 待覆盖 |
| 龙珠悬浮窗 | 龙珠悬浮窗 替代 | vs/Pillar | ☐ 待覆盖 |

### 2.13.3 维护日志
| 月份 | 数据来源 | 新增/升权 | 降权/删除 | 备注 |
|---|---|---|---|---|
| 2026-11 | 竞品调研（web）+ 站内已覆盖 | （初版建库） | — | 绝对量待 Play Console/GSC 回填；中文竞品 小米悬浮球/辅助触控 拦截词待在 vs/pillar 强化 |

---

## 2.14 Crosshair Aim（准星 / 射击游戏辅助 / FPS 叠层 / 屏幕准星）关键词记录

**品牌**：Crosshair Aim（en/zh 同；中文品牌名"准星瞄准"/"十字准星"；正文统一用 "Crosshair Aim"）
**品类**：准星 / 射击游戏辅助 / FPS 叠层 / 屏幕准星（Crosshair / FPS Crosshair / Crosshair Overlay / Screen Crosshair）
**核心卖点（长尾词构造）**：80+ 样式准星叠层；完全可自定义（大小/颜色/位置/透明度）；全射击游戏支持（含无原生准星的武器）；每游戏预设；轻量叠层不卡帧；核心免费 + Pro。合规卖点（必须强调）：纯视觉辅助、不修改游戏数据、不触发反作弊、免 root。同开发者家族（com.glgjing）。
**竞品主对比**：全站统一以 **Crosshair Hero** 为主对比（原 pillar/alternatives 曾用 Crosshair Hero，已统一）。其余竞品（EN：Crosshair X / Crosshair Pro / Custom Crosshair / Custom Aim / CrossAim / Crosshair PRO；ZH：准星大师 / 准星精灵 / 准星助手 / TapAim / 吃鸡准星助手 / 准心助手 / 准星实验室 等）统一拦截。

### 2.14.1 英文（en）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| crosshair | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | 品类根词 |
| crosshair overlay | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| fps crosshair | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| crosshair app | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| screen crosshair | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| android crosshair | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |
| crosshair for games | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar) | 竞品调研 | |

#### Middle（中词，P1，Best/vs/Alternatives 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| best crosshair app for android | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | 年度词 |
| best crosshair overlay app | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | |
| fps crosshair android | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar/best) | 竞品调研 | |
| crosshair for pubg mobile | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | 热门游戏词 |
| crosshair hero alternative | Middle | P1 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 Crosshair Hero（alternatives 页主对比） |
| crosshair hero alternative | Middle | P1 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 Crosshair Hero（vs 页主对比） |
| crosshair x alternative | Middle | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Crosshair X（iOS） |
| custom crosshair android | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best/app) | 竞品调研 | |

#### Long-tail（精准长尾，P0，App/Best 主吃）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| best crosshair app for android 2026 | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app) | 竞品调研 | |
| best crosshair overlay app for fps games | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app) | 竞品调研 | |
| crosshair hero alternative android | Long-tail | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | |
| custom crosshair overlay android no root | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 免 root |
| crosshair for shooting games android free | Long-tail | P1 | 中 | 高 | App | 已覆盖(app) | 竞品调研 | 免费 |

#### 品牌词 & 竞品替代词（en）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| Crosshair Aim | 品牌 | P0 | 中 | 高 | App | 已覆盖(app/全站) | 站内已覆盖 | 自有品牌 |
| Crosshair Hero alternative | 竞品 | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 Crosshair Hero（alternatives 页主对比） |
| best Crosshair Hero alternative android | 竞品 | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | |
| Crosshair Hero alternative | 竞品 | P0 | 高 | 高 | vs/Alt | 已覆盖(vs/alt) | 竞品调研 | 抢 Crosshair Hero（vs 页主对比） |
| Crosshair X alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Crosshair X（iOS） |
| Crosshair Pro alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Crosshair Pro |
| Custom Crosshair alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Custom Crosshair |
| Custom Aim alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Custom Aim |
| CrossAim alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 CrossAim |
| Crosshair PRO alternative | 竞品 | P1 | 中 | 高 | vs/Alt | 待覆盖 | 竞品调研 | 抢 Crosshair PRO |

### 2.14.2 中文（zh）
#### Head（大词，P2，Pillar 抢）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 准星 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | 品类根词 |
| 准星叠层 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 游戏准星 | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 准星 app | Head | P2 | 高 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 屏幕准星 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 安卓准星 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |
| 射击游戏准星 | Head | P2 | 中 | 中 | Pillar | 已覆盖(pillar-zh) | 竞品调研 | |

#### Middle（中词，P1）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 最佳准星 app 安卓 | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | |
| 最佳准星叠层 应用 | Middle | P1 | 高 | 中 | Pillar/Best | 已覆盖(pillar-zh/best-zh) | 竞品调研 | |
| 游戏准星 安卓 | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |
| 和平精英 准星 | Middle | P1 | 高 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | 热门游戏词 |
| 准星大师 替代 | Middle | P1 | 高 | 高 | vs/Pillar | 已覆盖(vs/pillar-zh) | 竞品调研 | 抢 准星大师（=Crosshair Hero，主对比） |
| Crosshair Hero 替代 | Middle | P1 | 中 | 高 | vs/Pillar | 已覆盖(vs/pillar-zh) | 竞品调研 | 抢 Crosshair Hero（vs zh 页主对比） |
| 准星精灵 替代 | Middle | P1 | 中 | 高 | vs/Pillar | 待覆盖 | 竞品调研 | 抢 准星精灵 |
| 自定义 准星 安卓 | Middle | P1 | 中 | 中 | Best/App | 已覆盖(best-zh/app) | 竞品调研 | |

#### Long-tail（精准长尾，P0）
| 关键词 | 词层 | 优先级 | 预估流量 | 购买意图 | 目标页型 | 当前覆盖 | 数据来源 | 备注 |
|---|---|---|---|---|---|---|---|---|
| 最好的 准星 app 安卓 2026 | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app-zh) | 竞品调研 | |
| 最佳 准星叠层 fps 游戏 | Long-tail | P0 | 高 | 高 | Best/App | 已覆盖(app-zh) | 竞品调研 | |
| 准星大师 替代 安卓 | Long-tail | P0 | 高 | 高 | vs/Pillar | 已覆盖(vs/pillar-zh) | 竞品调研 | |
| 自定义 准星叠层 安卓 免root | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 免 root |
| 射击游戏 准星 安卓 免费 | Long-tail | P1 | 中 | 高 | App | 已覆盖(app-zh) | 竞品调研 | 免费 |

#### 竞品拦截词（zh 重点）
| 竞品（中文） | 拦截词 | 目标页型 | 当前覆盖 |
|---|---|---|---|
| 准星大师（Crosshair Hero） | 准星大师 替代 / 准星大师 安卓 替代 | vs/Pillar | 🟡 待强化 |
| 准星精灵 / 准星精灵大师（Crosshair Pro） | 准星精灵 替代 | vs/Pillar | ☐ 待覆盖 |
| 准星助手（FPSTool） | 准星助手 替代 | vs/Pillar | ☐ 待覆盖 |
| TapAim 瞄准镜助手 | TapAim 替代 | vs/Pillar | ☐ 待覆盖 |
| 吃鸡准星助手 | 吃鸡准星助手 替代 | vs/Pillar | ☐ 待覆盖 |
| 准心助手 / 准心精灵助手 | 准心助手 替代 | vs/Pillar | ☐ 待覆盖 |
| 准星实验室 | 准星实验室 替代 | vs/Pillar | ☐ 待覆盖 |
| 多功能准星助手 | 多功能准星助手 替代 | vs/Pillar | ☐ 待覆盖 |
| Crosshair Pro 高级版 | crosshair pro 替代 | vs/Pillar | ☐ 待覆盖 |

### 2.14.3 维护日志
| 月份 | 数据来源 | 新增/升权 | 降权/删除 | 备注 |
|---|---|---|---|---|
| 2026-11 | 竞品调研（web）+ 站内已覆盖 | （初版建库） | — | 绝对量待 Play Console/GSC 回填；中文竞品 准星大师/准星精灵 拦截词待在 vs/pillar 强化 |

---

## 4. 编辑落地检查（与红线对齐）

- 每篇新/改内容：**差异化 title + description（含目标词）+ 关键词化 alt**（§2.3 / §1.6）。
- 目标词须来自本库；写前查重避免 cannibalization（§7.2）。
- 财务类属 YMYL：表述用事实/数字，避免空泛「最好」类绝对词（见此前审计结论），保 E-E-A-T。
- 所有改动**中英同步**（§6.1 红线）；新增语言走 `/<lang>/` 子路径。
- 改完真实更新正文 + `last_modified_at`，并回写本库覆盖状态（§2.4 纪律）。
