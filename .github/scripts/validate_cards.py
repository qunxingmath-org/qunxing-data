#!/usr/bin/env python3
"""检查题卡目录。题库更新包、CI 和桌面端更新题库前都用它；有任何错误就退出码 1，调用方应保留旧版。

用法：python3 -I validate_cards.py <schema.json> <题卡目录> [--summary] [--allow-empty]
依赖：jsonschema（4.18 以上）

检查内容：
1. 目录存在，且至少有一张题卡（--allow-empty 时可以为空，只用于测试）。
2. 每张 <id>.meta.json 符合 qunxing.problem/2 的 Schema，文件名和 id 一致，编号不重复。
3. 文件成对：每个 .meta.json 有同名的 .text.md，每个 .text.md 也有同名的 .meta.json。
4. 正文有"## 题面"一节，内容不为空；内容是"（待补）"时，statement_fidelity 必须是 unknown。
5. card_rev 与内容一致：按 tools/cardrev.py 重算，结果要相同。
退出码：0 全部通过；1 有错误；2 用法错误。
"""
import json
import pathlib
import sys
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import cardrev  # noqa: E402

from jsonschema import Draft202012Validator  # noqa: E402

PLACEHOLDER = "（待补）"


def check(schema_path, root, allow_empty=False):
    """返回 (错误列表, 题卡数, 按 轨道/状态 的计数)。"""
    errors, counter = [], Counter()
    root = pathlib.Path(root)
    if not root.is_dir():
        return [f"{root}: 目录不存在"], 0, counter
    schema = json.loads(pathlib.Path(schema_path).read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    metas = {p.name[: -len(".meta.json")]: p for p in root.rglob("*.meta.json")}
    texts = {p.name[: -len(".text.md")]: p for p in root.rglob("*.text.md")}
    for cid in sorted(set(texts) - set(metas)):
        errors.append(f"{cid}: 只有 {texts[cid].name}，缺少 .meta.json")
    if not metas and not allow_empty:
        errors.append(f"{root}: 没有任何题卡")
    seen = set()
    for meta_path in sorted(root.rglob("*.meta.json")):
        cid = meta_path.name[: -len(".meta.json")]
        if cid in seen:
            errors.append(f"{cid}: 编号重复（{meta_path}）")
            continue
        seen.add(cid)
        try:
            card = json.loads(meta_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            errors.append(f"{meta_path}: JSON 解析失败：{e}")
            continue
        if not isinstance(card, dict):
            errors.append(f"{cid}: meta 不是对象")
            continue
        for err in validator.iter_errors(card):
            loc = "/".join(str(p) for p in err.absolute_path) or "(根)"
            errors.append(f"{cid}: {loc}: {err.message[:200]}")
        if card.get("id") != cid:
            errors.append(f"{cid}: 文件名和 id 不一致（{card.get('id')}）")
        text_path = meta_path.with_name(cid + ".text.md")
        if not text_path.is_file():
            errors.append(f"{cid}: 缺少 {text_path.name}")
        else:
            text = text_path.read_text(encoding="utf-8")
            statement = cardrev.statement_of(text)
            if not statement:
                errors.append(f"{cid}: {text_path.name} 缺少“## 题面”，或这一节是空的")
            elif statement == PLACEHOLDER and card.get("statement_fidelity") != "unknown":
                errors.append(f"{cid}: 题面是“{PLACEHOLDER}”，statement_fidelity 应为 unknown")
            try:
                expected = cardrev.card_rev(card, text)
                if card.get("card_rev") != expected:
                    errors.append(f"{cid}: card_rev 与内容不符（记的是 {card.get('card_rev')}，按内容算是 {expected}）")
            except TypeError as e:
                errors.append(f"{cid}: card_rev 无法计算：{e}")
        counter[(card.get("track"), card.get("card_status"))] += 1
    return errors, len(seen), counter


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if len(args) < 2:
        print(__doc__)
        return 2
    errors, n, counter = check(args[0], args[1], allow_empty="--allow-empty" in argv)
    for err in errors[:200]:
        print("错误：" + err)
    if len(errors) > 200:
        print(f"……另有 {len(errors) - 200} 条错误")
    if "--summary" in argv:
        for (track, status), k in sorted(counter.items(), key=lambda x: str(x[0])):
            print(f"  {track}/{status}: {k}")
    print(f"检查了 {n} 张题卡，错误 {len(errors)} 条。")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
