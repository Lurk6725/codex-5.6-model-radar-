# Codex Radar API integration / Codex Radar API 接入

## English

The repository uses the authorized endpoint `GET https://codexradar.com/api/v1/current` with the GitHub Actions repository secret `CODEX_RADAR_API_TOKEN`. The token is never committed, printed by the fetcher, or included in reports.

The endpoint currently exposes model-level summaries under `model_iq.comparisons`. The integration archives only source score, passed/tasks, token counts, wall time, estimated cost, timestamps, and provenance. The raw API response is not published.

The endpoint does not currently expose the ten task-level outcomes used by the project's difficulty-weighted score. API snapshots are therefore reported separately and are not silently treated as task-weighted observations.

The scheduled workflow runs at 5 and 35 minutes past each hour and can also be started manually. Identical snapshots are deduplicated by a content hash.

## 简体中文

仓库使用已获授权的接口 `GET https://codexradar.com/api/v1/current`，真实 Token 只保存在 GitHub Actions 仓库 Secret `CODEX_RADAR_API_TOKEN` 中，不提交到仓库、不由抓取脚本输出，也不会写入报告。

当前接口在 `model_iq.comparisons` 下提供模型级摘要。接入程序只归档源站分数、通过数/任务数、Token、耗时、估算费用、时间戳和数据来源，不会公开保存完整 API 响应。

当前接口没有返回本项目使用的十道题逐题结果，因此 API 数据会单独展示，不能直接冒充本项目的难度加权分。

自动工作流每小时的第 5 分钟和第 35 分钟运行，也支持手动触发。内容完全相同的快照会通过内容哈希去重。
