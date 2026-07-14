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

The API `observed_at` field may occasionally remain unchanged while comparison values change. The repository preserves both `observed_at` and `retrieved_at` and treats such snapshots as freshness-metadata inconsistencies rather than silently correcting the source timestamp.

The scheduled workflow runs at 5 and 35 minutes past each hour and can also be started manually. Identical normalized snapshots are deduplicated by a content hash.

## 简体中文

仓库使用已获授权的接口 `GET https://codexradar.com/api/v1/current`，真实 Token 只保存在 GitHub Actions 仓库 Secret `CODEX_RADAR_API_TOKEN` 中，不提交到仓库、不由抓取脚本输出，也不会写入报告。

当前接口在 `model_iq.comparisons` 下提供模型级摘要。接入程序只归档源站分数、通过数/任务数、Token、耗时、估算费用、时间戳和数据来源，不公开保存完整 API 响应。

当前接口**不提供**：

- 十道任务的逐题通过/失败矩阵；
- 每个模型独立的运行 ID 或更新时间；
- 完整批次与部分重跑的明确标记；
- 最新一次实际重跑模型的可靠列表。

因此 API 快照可用于总分趋势、原始分数/费用和模型级变化提醒，但不能独立重新计算本项目的难度加权分。某行汇总值发生变化，只能说明公开值改变，不能自动写成“已确认重新测试”。

API 的 `observed_at` 字段偶尔可能在汇总值变化后仍保持旧值。仓库同时保留 `observed_at` 与 `retrieved_at`，并将这种情况标记为时间元数据不一致，不擅自修正来源时间。

自动工作流每小时的第 5 分钟和第 35 分钟运行，也支持手动触发。规范化内容完全相同的快照会通过内容哈希去重。
