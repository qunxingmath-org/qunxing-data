# 查新回传

查新 GPT 按《查新、证据核验与回填规范 v2》交来的结果，格式是 `qunxing.novelty-handoff/2`，每题一行 JSONL。

| 目录 | 内容 |
|---|---|
| `inbox/` | 原样交来的回传和《突破点、检索路径与复核清单》。只追加，不修改；同名但内容不同的另起一个名字 |
| `quarantine/` | 没通过接收检查的行，原样保留，写明原因 |
| `reviews/` | 每批的待复核清单：提议结案、题卡改动建议、查重、降级说明、隔离的行 |

导入以后的结果在 `evidence/` 里，每题一个文件。四个摘要状态（数学结论、形式化、查新覆盖、最强声明）由回传记录算出来，取值见 `schema/qunxing.vocab-1.json`。

## 导入

```bash
python3 .github/scripts/evidence.py import --data . 回传.jsonl --check
```

试导：什么都不写，只报收下多少、隔离多少、哪些取值不认识。

```bash
python3 .github/scripts/evidence.py import --data . 回传.jsonl 清单.md
```

正式导入。同一批导两次，结果不变。

## 二审

`原题已证明`、`原题已推翻` 这类闭合状态，导入时只记成提议，二审以后才算数：

```bash
python3 .github/scripts/evidence.py review --data .
```

```bash
python3 .github/scripts/evidence.py review --data . QX-P-000123 accept --by 名字 --note "对照了当前题面和原文定理 3"
```

更多用法（人工改状态、加状态、加分类）见协作仓库的 `projects/qunxing/contracts/evidence/README.md`。
