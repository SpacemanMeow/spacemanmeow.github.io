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

## 3. 其他 App 关键词（待展开）

按 §2 同样模板逐项展开；种子词见 `SEO-PLAYBOOK.md` §2.1.1。展开顺序建议：先高转化品类（CPU Monitor / Only Clock 已在非英语区有起量信号，见 T-31），再铺其余。

- [ ] Meow Todo（to-do / task manager）
- [ ] Meow Mood Diary（mood diary / journal）
- [ ] Meow Habits（habit tracker）
- [ ] One Widget（home screen widgets）
- [ ] Only Clock（flip clock）
- [ ] CPU Monitor（cpu temperature）
- [ ] System Monitor（storage cleaner）
- [ ] Floating Assistant（assistive touch）
- [ ] Meow FM（white noise）
- [ ] Crosshair Aim（crosshair / FPS）

---

## 4. 编辑落地检查（与红线对齐）

- 每篇新/改内容：**差异化 title + description（含目标词）+ 关键词化 alt**（§2.3 / §1.6）。
- 目标词须来自本库；写前查重避免 cannibalization（§7.2）。
- 财务类属 YMYL：表述用事实/数字，避免空泛「最好」类绝对词（见此前审计结论），保 E-E-A-T。
- 所有改动**中英同步**（§6.1 红线）；新增语言走 `/<lang>/` 子路径。
- 改完真实更新正文 + `last_modified_at`，并回写本库覆盖状态（§2.4 纪律）。
