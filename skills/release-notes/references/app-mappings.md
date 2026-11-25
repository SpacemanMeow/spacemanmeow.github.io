# App slug 映射与当前 Release Note 覆盖情况

## Slug 别名（日志文件名 → _apps slug）

`skills/release-notes/scripts/update_release_notes.py` 默认把下划线转换为连字符。以下四个需要在脚本里配置显式 `SLUG_ALIASES`：

| 日志 key | App slug |
|---|---|
| `meow_habit` | `meow-habits` |
| `meow_todo` | `meow-todo-list` |
| `meow_mood` | `meow-mood-diary` |
| `crosshair` | `cross-hair` |

其余所有日志遵循默认规则（`only_clock` → `only-clock`、`cpu_monitor` → `cpu-monitor`、`system_monitor` → `system-monitor`、`floating_assistant` → `floating-assistant`、`meow_fm` → `meow-fm`、`one_widget` → `one-widget`、`meow_money_manager` → `meow-money-manager`）。

## 版本数（英文，2026-11-25 核实）

| App | 版本数 |
|---|---|
| meow-money-manager | 31 |
| cpu-monitor | 19 |
| only-clock | 12 |
| meow-habits | 10 |
| system-monitor | 11 |
| floating-assistant | 9 |
| meow-todo-list | 8 |
| cross-hair | 8 |
| meow-fm | 5 |
| meow-mood-diary | 3 |
| one-widget | 3 |

## 日志位置与生命周期

日志位于 `seo/data/<app_slug>_release_note`（被 gitignore）。该目录还存放 GSC 的 CSV/JSON 导出 — 忽略它们，与本流程无关。处理完成后可以删除日志；从旧日志重新生成只需再次运行脚本（生成的页面才是持久产物）。
