# 群星题库与统计 · qunxing-data

群星的公开数据：

- **题卡**：开放数学问题的题面（自然语言和 Lean）、出处、分类和状态；
- **统计**：按周汇总的用量和成功率。延迟两周发布，不含安装 ID；
- **贡献者名单**：审核过的昵称。

> 状态：首批 2262 张题卡已导入，全部是**草稿**（card_status = draft）：题面、来源和查新记录齐全，题型、MSC 分类等判断类字段待补。

## 目录

| 路径 | 内容 |
|---|---|
| `problems/000/QX-P-000001.meta.json` | 题卡的结构化部分（CC0 1.0） |
| `problems/000/QX-P-000001.text.md` | 题卡正文：题面、原文摘录、已知结果、边界与约定、证据（CC BY-SA 4.0） |
| `schema/qunxing.problem-2.schema.json` | 题卡格式（qunxing.problem/2，v2.2），每个字段带中英文说明 |
| `import/` | 每次批量导入的报告：数量、疑似重复、题面过短、核对不通过 |

每 1000 张题卡放一个目录。提交题卡的 PR 会自动检查格式（`cards` 工作流）。

## 首批导入（2026-11-23）

来自两个按 SOL 标准整理的题包，由脚本转换，没有经过 AI 改写：

- 包 B（群星问题池）：1622 张，开放 1443、部分解决 179。
- 包 A（群星开放题池查新交付包）：640 张，开放 481、部分解决 75、未知 17、有争议 3。另有 64 张在验证轨道：别人声称已解或已解，等待核对或形式化。

已知的待办：
- 258 张的题面只有一句话；
- 20 组疑似重复；
- 5 张题面与出处核对不通过。

清单见 `import/2026-11-23-report.json`。

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
- 题卡的改动请走 PR，`cards` 和 `checks` 两项检查都要通过。
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
