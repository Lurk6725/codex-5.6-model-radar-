# Bilingual Publication Policy / 双语发布规范

## 中文

本仓库的公开结果、分析结论和模型推荐必须同时提供简体中文与英文版本。

### 每次测试更新必须包含

1. 原始批次时间与数据来源；
2. 各模型通过数、难度加权分、费用和额度效率；
3. 与上一轮及滚动历史的比较；
4. 异常批次判断及其理由；
5. 推荐是否改变，以及置信度；
6. 中文完整分析；
7. 英文完整分析。

### 文件约定

- `reports/latest.zh-CN.md`：最新中文完整分析；
- `reports/latest.en.md`：最新英文完整分析；
- `reports/latest.md`：中英文合并入口，中文在前、英文在后；
- `reports/latest.generated.zh-CN.md`：脚本生成的中文统计汇总；
- `reports/latest.generated.en.md`：脚本生成的英文统计汇总；
- `reports/latest.generated.md`：脚本生成的双语统计汇总。

历史报告建议使用：

```text
reports/history/YYYY-MM-DD-HHMM.zh-CN.md
reports/history/YYYY-MM-DD-HHMM.en.md
reports/history/YYYY-MM-DD-HHMM.md
```

### 一致性要求

中英文版本必须保持：

- 相同的数据；
- 相同的评分公式；
- 相同的异常状态；
- 相同的推荐；
- 相同的置信度和限制条件。

翻译可以采用自然表达，不要求逐字对应，但不得改变结论或省略重要警告。

### 提交要求

正式数据更新应在同一个提交或同一个 Pull Request 中完成两种语言。若其中一种语言尚未完成，应将报告标记为草稿，而不是覆盖正式 `latest` 文件。

---

## English

Public results, analytical conclusions, and model recommendations in this repository must be available in both Simplified Chinese and English.

### Every benchmark update must include

1. The exact batch timestamp and source provenance;
2. Pass count, difficulty-weighted score, estimated cost, and quota efficiency for each model;
3. Comparison with the previous run and rolling history;
4. An anomaly decision with reasons;
5. Whether recommendations changed, including confidence;
6. A complete Simplified Chinese analysis;
7. A complete English analysis.

### File convention

- `reports/latest.zh-CN.md` — latest complete Chinese analysis;
- `reports/latest.en.md` — latest complete English analysis;
- `reports/latest.md` — combined bilingual entry point, Chinese first and English second;
- `reports/latest.generated.zh-CN.md` — generated Chinese statistical summary;
- `reports/latest.generated.en.md` — generated English statistical summary;
- `reports/latest.generated.md` — generated combined bilingual summary.

Historical reports should preferably use:

```text
reports/history/YYYY-MM-DD-HHMM.zh-CN.md
reports/history/YYYY-MM-DD-HHMM.en.md
reports/history/YYYY-MM-DD-HHMM.md
```

### Consistency requirements

The Chinese and English versions must preserve:

- identical data;
- identical scoring formulas;
- identical anomaly state;
- identical recommendations;
- identical confidence and limitations.

Natural translation is encouraged, but it must not change the conclusion or omit material warnings.

### Commit requirements

A formal data update should include both languages in the same commit or pull request. If one language is incomplete, mark the report as a draft rather than replacing the formal `latest` files.
