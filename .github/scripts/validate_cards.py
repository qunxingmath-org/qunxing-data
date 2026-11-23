#!/usr/bin/env python3
"""检查题卡：每张 <id>.meta.json 符合 qunxing.problem/2 的 JSON Schema，且有同名的 .text.md。

用法：python3 -I validate_cards.py <schema.json> <题卡目录> [--summary]
依赖：jsonschema（pip install jsonschema）
退出码：0 全部通过；1 有错误。
"""
import json
import pathlib
import re
import sys
from collections import Counter

from jsonschema import Draft202012Validator


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    schema = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    root = pathlib.Path(sys.argv[2])
    validator = Draft202012Validator(schema)
    errors, seen, counter = [], set(), Counter()
    for meta_path in sorted(root.rglob("*.meta.json")):
        cid = meta_path.name[: -len(".meta.json")]
        try:
            card = json.loads(meta_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{meta_path}: JSON 解析失败：{e}")
            continue
        for err in validator.iter_errors(card):
            loc = "/".join(str(p) for p in err.absolute_path) or "(根)"
            errors.append(f"{cid}: {loc}: {err.message[:200]}")
        if card.get("id") != cid:
            errors.append(f"{cid}: 文件名和 id 不一致（{card.get('id')}）")
        if cid in seen:
            errors.append(f"{cid}: 编号重复")
        seen.add(cid)
        text = meta_path.with_name(cid + ".text.md")
        if not text.is_file():
            errors.append(f"{cid}: 缺少 {text.name}")
        elif not re.search(r"^## 题面\s*$", text.read_text(encoding="utf-8"), re.M):
            errors.append(f"{cid}: {text.name} 缺少“## 题面”")
        counter[(card.get("track"), card.get("card_status"))] += 1
    for err in errors[:200]:
        print("错误：" + err)
    if len(errors) > 200:
        print(f"……另有 {len(errors) - 200} 条错误")
    if "--summary" in sys.argv:
        for (track, status), n in sorted(counter.items(), key=lambda x: str(x[0])):
            print(f"  {track}/{status}: {n}")
    print(f"检查了 {len(seen)} 张题卡，错误 {len(errors)} 条。")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
