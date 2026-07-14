# Codex Radar API integration / Codex Radar API 接入

## English

The repository uses the authorized endpoint `GET https://codexradar.com/api/v1/current` with the GitHub Actions repository secret `CODEX_RADAR_API_TOKEN`. The token is never committed, printed by the fetcher, or included in reports.

The endpoint currently exposes model-level summaries under `model_iq.comparisons`. The integration archives only source score, passed/tasks, token counts, wall time, estimated cost, timestamps, and provenance. The raw API response is not published.

The endpoint does **not** currently expose:

- the ten task-level pass/fail outcomes;
- a per-model run ID or per-model update timestamp;
- an explicit full-batch versus partial-rerun marker; or
- a reliable list of models rerun in the latest refresh.

Therefore API snapshots support aggregate trend monitoring, raw score-per-cost analysis, and model-level change alerts, but they cannot independently recompute the project's difficulty-weighted score. A changed aggregate row means the displayed values changed; it is not automatically labeled a confirmed rerun.

The API `observed_at` field may occasionally remain unchanged while comparison values change. The repository preserves both the upstream observation time and the local successful-check time. `data/api/monitor_status.json` records the latest successful API heartbeat, current snapshot ID, model count, and whether that check detected a new snapshot.

The scheduled workflow runs at 17 and 47 minutes past each hour and can also be started manually. Fetching is retried up to three times, and pushes are retried after rebasing on the latest `main` branch. Scheduled GitHub Actions are best-effort and may start later than the exact cron minute, so monitor health should be read from **Last successful check**, not from the nominal schedule alone.

## 简体中文

仓库使用已获授权的接口 `GET https://codexradar.com/api/v1/current`，真实 Token 只保存在 GitHub Actions 仓库 Secret `CODEX_RADAR_API_TOKEN` 中，不提交到仓库、不由抓取脚本输出，也不会写入报告。

当前接口在 `model_iq.comparisons` 下提供模型级摘要。接入程序只归档源站分数、通过数/任务数、Token、耗时、估算费用、时间戳和数据来源，不公开保存完整 API 响应。

当前接口**不提供**：

- 十道任务的逐题通过/失败矩阵；
- 每个模型独立的运行 ID 或更新时间；
- 完整批次与部分重跑的明确标记；
- 最新一次实际重跑模型的可靠列表。

因此 API 快照可用于总分趋势、原始分数/费用和模型级变化提醒，但不能独立重新计算本项目的难度加权分。某行汇总值发生变化，只能说明公开值改变，不能自动写成“已确认重新测试”。

API 的 `observed_at` 字段偶尔可能在汇总值变化后仍保持旧值。仓库同时保留源站观测时间与本地成功检查时间。`data/api/monitor_status.json` 会记录最近成功访问 API 的心跳、当前快照 ID、返回模型数以及本次是否发现新快照。

自动工作流改为每小时第 17 分钟和第 47 分钟运行，也支持手动触发。API 请求最多重试三次，推送前会基于最新 `main` 分支变基并重试推送。GitHub 定时任务属于尽力调度，实际启动时间可能晚于 cron，因此判断监控是否正常应查看“最近成功检查”，而不是只看计划时间。
