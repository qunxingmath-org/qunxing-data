# 群星题库与统计 · qunxing-data

群星的公开数据：

- **题卡**：开放数学问题的题面（自然语言和 Lean）、出处、分类和状态；
- **统计**：按周汇总的用量和成功率。延迟两周发布，不含安装 ID；
- **贡献者名单**：审核过的昵称。

> 状态：搭建中。目录结构和字段以群星的题卡格式和数据格式规范为准，定稿后补在这里。

## 许可

| 内容 | 许可 |
|---|---|
| 题卡的结构化元数据（`*.meta.json`：编号、星域、分类号、状态、日期、链接） | [CC0 1.0](LICENSES/CC0-1.0.txt) |
| 匿名的逐次记录、汇总统计 | [CC0 1.0](LICENSES/CC0-1.0.txt) |
| 题卡文字（`*.text.md`）、查新报告、说明文档 | [CC BY-SA 4.0](LICENSES/CC-BY-SA-4.0.txt) |
| Lean 题面（`*.lean`） | [Apache-2.0](LICENSES/Apache-2.0.txt) |

- 每个文件的许可，按 [REUSE](https://reuse.software/) 规范写在 `REUSE.toml` 里。
- 从第三方导入的内容保持原许可，在 `REUSE.toml` 里单独标注，并列在网站的"致谢与许可"页。

## 怎么改

- 题面有错：开 Issue，选"题面异议"。
- 统计由群星的自动流程生成，请不要直接改。

---

**English.** Public data of Qunxing:

- problem cards: natural-language and Lean statements, sources, classification and status;
- weekly aggregated statistics, published with a two-week delay and without installation IDs.

Licenses:

- structured metadata, per-run records and statistics: CC0 1.0;
- card texts and novelty reports: CC BY-SA 4.0;
- Lean statements: Apache-2.0;
- third-party content keeps its original license.

Per-file licensing is in REUSE.toml.
