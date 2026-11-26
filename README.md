# 群星题库与统计 · qunxing-data

群星的公开数据：

- **题卡**：开放数学问题的题面（自然语言和 Lean）、出处、分类和状态；
- **统计**：按周汇总的用量和成功率。延迟两周发布，不含安装 ID；
- **贡献者名单**：审核过的昵称。

> 状态：
> - 2469 张题卡，全部是**草稿**（card_status = draft）。首批导入 2262 张，2026-11-24 删除了题面有异议的 34 张；2026-11-25 加入 Agent 出的 241 张。
> - 题面、来源和查新记录来自原包。
> - 题型、答案形式、MSC 分类、人话版和验收条件由 AI（DeepSeek）补出，经过机器检查，但**未经人工审校**。
> - 每题有一个证据文件（`evidence/`），记数学结论、形式化、查新覆盖和最强声明四个状态。现在都是由题卡旧字段映射的初值，查新 GPT 的 v2 回传导入以后更新。

## 目录

| 路径 | 内容 |
|---|---|
| `problems/000/QX-P-000001.meta.json` | 题卡的结构化部分（CC0 1.0） |
| `problems/000/QX-P-000001.text.md` | 题卡正文：题面、原文摘录、已知结果、边界与约定、证据（CC BY-SA 4.0） |
| `schema/qunxing.problem-2.schema.json` | 题卡格式（qunxing.problem/2，v2.2），每个字段带中英文说明 |
| `import/` | 每次批量导入的报告：数量、疑似重复、题面过短、核对不通过 |
| `evidence/000/QX-P-000001.json` | 每题的证据文件：四个摘要状态、查新记录、人工决定和分类（CC0 1.0）。由脚本生成，不要手改 |
| `schema/qunxing.vocab-1.json` | 状态和分类的取值表：中英文名、颜色、强弱顺序、查新回传的各种写法 |
| `schema/qunxing.evidence-1.schema.json` | 证据文件格式（qunxing.evidence/1） |
| `novelty/` | 查新回传原件、隔离区、待复核清单，见 `novelty/README.md` |
| `batches/` | 批次一等研究批次的公开承诺（抽题规则、题库快照、题单的哈希），见 `batches/batch-1/README.md` |

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

## 补字段与复核标记（2026-11-24）

- 2262 张全部补上了题型、答案形式、可检验性、MSC 分类号（`msc2020.source = agent`）、关键词、英文标题、人话版和验收条件。
  - 52 张原来只有一句话题面，DeepSeek 照原文起草了题面，放在正文的"题面草稿（AI 起草，待核）"一节，原题面没动。
- 补了验收条件，按规格题卡版本（card_rev）重算，修订号升到 2。查新结论是在旧版本上做的，开题前要重新查新。
- 复核清单里的问题已经处理：
  - **题面有异议的 34 张已删除**（用户决定），其中 8 张是原包的占位条目。这些编号作废、不再复用，清单和原因见 `import/2026-11-24-removed.json`。
  - 268 张题面待补全（`statement_fidelity = unknown`），具体说明写在各卡的 `novelty.statement_issues` 里；
  - 43 张可能与别的卡重复（`provenance.possible_duplicates`）。
- 首批导入时记为"核对不通过"的 5 张，原包其实写的是"FAIL（……已补全／已修正）"，已改记为修正后通过（`pass_with_fixes`）。其中 QX-P-000040 还有一个条件待核，已写进说明。

标记清单见 `import/2026-11-24-review-flags.json`，统计见 `import/2026-11-24-merge-report.json`。

## 题卡版本号统一算法（2026-11-24）

- **原因**：复核发现旧的合并脚本只把验收条件的文字算进 `card_rev`，没有用整个验收条件对象，和规格不一致（协作仓库 Issue #9）。
- **新算法**：`card_rev` 统一按 `.github/scripts/cardrev.py` 计算，输入是：
  - 题面一节；
  - 记号约定；
  - 歧义点；
  - 整个验收条件对象；
  - 锁定的 Challenge 哈希。
- **迁移结果**：
  - 2228 张的 `card_rev` 全部重算。**修订号不变**，因为内容没有改，变的只是算法。
  - `novelty.card_rev` 按同一算法换算，仍然指向查新时的那一版，也就是还没有验收条件的第 1 版。
  - 新旧值的对照见 `import/2026-11-24-card-rev-migration.json`。
- **检查**：从这一版起，题卡检查会核对每张卡的 `card_rev` 是否与内容一致；目录为空、文件不成对、题面为空，都算不通过。

## 第二批：Agent 出的题卡（2026-11-25）

- **来源**：Agent 按协作仓库的《找题、查新和出题卡说明》写的 245 份草稿（`qunxing.card-draft/1`），用 `make_cards.py` 转成正式题卡。
  - 同一道题有两份的去掉 4 份，生成 241 张：QX-P-002263 到 QX-P-002503。
  - 开放轨道 208 张（开放 57、部分解决 151）；验证轨道 33 张，都是"有人声称证明了，需要核对"。
- **难度**：中等 8 张、高等 190 张、**传奇 43 张**。
  - 从这一批起，难度 5 只给"传奇"：提出 30 年以上仍未解决、在本领域之外也有名、公认极难。例如 Schinzel 假设 H、Whitehead 猜想、光滑四维庞加莱猜想；验证轨道上有 abc 猜想、三维 Navier–Stokes、ζ(5) 无理性等证明声明。
  - 草稿里其余自评 5 分的改为 4，原估计写在 `difficulty.note` 里。每张传奇题的 `difficulty.note` 开头写了一句理由：谁在哪一年提出、有名在哪里。
- **整理**（逐份记在 `import/2026-11-25-normalize.json`，原稿不入库）：
  - 取值写错的改成规定取值：题型、答案形式、来源角色、线索关系等；
  - 不加引号的 arXiv 编号恢复原样（`0807.3404` 曾被读成 `807.3404`）；
  - Erdős problems 网站的原文摘录删掉，只留链接；
  - **删去了草稿里作者电脑上的本机路径**（共约 390 处，其中有带用户名的），换成公开仓库里的相对路径或"本机文件"。
- **待人工复核**（清单见 `import/2026-11-25-report.json`）：
  - 1 对确实重复：QX-P-002331 与 QX-P-002385（Kourovka 21.138），已互相标上疑似重复；
  - 21 张开放题的查新里有"有人声称解决、尚未核实"的线索，作者判断不影响开放状态，是否改到验证轨道要人工决定；
  - 108 张有打不开的关键原文；36 张的原文摘录缺出处行。

## 证据文件（2026-11-26）

- **为什么单独放**：已装好的桌面端按打包时的题卡格式校验题库，题卡加字段会让它们更新失败。所以状态和证据放在每题的证据文件里，题卡不动，`card_rev` 不变。
- **四个状态分开记**：
  - 数学结论；
  - 形式化，其中"他人声称已形式化验证"单独一级，和"复跑通过"分开；
  - 查新覆盖；
  - 最强声明及其复核情况。
- **初值**：由题卡的旧字段映射。数学结论：本次范围未发现确证 1930、有部分进展 426、有人声称已证明 98、现有材料无法判定 15；形式化全部是"未检索形式化"；查新覆盖全部是"旧版记录，仅供参考"。
- **取值都在取值表里**：加状态、改名、加分类，改 `schema/qunxing.vocab-1.json`，再运行 `python3 .github/scripts/evidence.py sync --data .`。
- **检查**：`cards` 工作流会重算全部证据文件，和文件不一致就报错。

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
- 证据文件由 `.github/scripts/evidence.py` 生成，请不要直接改；查新结果走 `novelty/`，人工二审和改状态用脚本的 `review`、`set`。

---

**English.** Public data of Qunxing:

- problem cards: natural-language and Lean statements, sources, classification and status;
- weekly aggregated statistics, published with a two-week delay and without installation IDs;
- one evidence file per problem (`evidence/`): mathematical status, formal verification, search coverage and the strongest claim, with the underlying search records. Allowed values live in `schema/qunxing.vocab-1.json`.

Licenses:

- structured metadata, per-run records and statistics: CC0 1.0;
- card texts and novelty reports: CC BY-SA 4.0;
- Lean statements: Apache-2.0;
- third-party content keeps its original license.

Per-file licensing is in REUSE.toml.
