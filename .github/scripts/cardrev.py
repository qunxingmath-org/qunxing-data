"""题卡版本号 card_rev 的唯一实现（规格 v2.1 第 2 条、v2.2 第 11 条）。

导入（import_pools.py）、合并（llm/merge_results.py）、检查（validate_cards.py）、迁移（migrate_card_rev.py）都调这里，
桌面端和网站重算时也按这里的写法。

card_rev = sha256(JCS(输入)) 的前 16 位十六进制。输入是一个对象，五个键：

| 键 | 取自 | 缺省 |
|---|---|---|
| statement | 正文"## 题面"一节（含其下的"### 形式化表述"），到下一个二级标题为止 | "" |
| conventions | meta.conventions（记号约定） | [] |
| ambiguity | meta.ambiguity（已知的歧义点和本卡采用的解释） | [] |
| acceptance | meta.acceptance 整个对象 | null |
| challenge_sha256 | meta.formal_challenge.sha256 | null |

题面的规范化：Unicode NFC；换行统一为 \\n；去掉每行行尾空白；去掉首尾空行。

JCS（RFC 8785）：这里的输入只有字符串、整数、布尔、null、数组和对象，键都是 ASCII，
所以等同于 json.dumps(sort_keys=True, separators=(",", ":"), ensure_ascii=False) 的 UTF-8 编码。
遇到浮点数直接报错，因为 Python 和 JCS 写浮点数的方式不完全一致。
"""
import hashlib
import json
import re
import unicodedata

_HEADING = re.compile(r"^## 题面[ \t]*$", re.M)
_NEXT_H2 = re.compile(r"^## ", re.M)


def normalize(text):
    text = unicodedata.normalize("NFC", text).replace("\r\n", "\n").replace("\r", "\n")
    return "\n".join(line.rstrip() for line in text.split("\n")).strip("\n")


def statement_of(text):
    """正文"## 题面"一节的内容（规范化后）。没有这一节返回空串。"""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    m = _HEADING.search(text)
    if not m:
        return ""
    body = text[m.end():]
    nxt = _NEXT_H2.search(body)
    return normalize(body[: nxt.start()] if nxt else body)


def _no_floats(value):
    if isinstance(value, float):
        raise TypeError("card_rev 的输入里不能有浮点数")
    if isinstance(value, dict):
        for v in value.values():
            _no_floats(v)
    elif isinstance(value, list):
        for v in value:
            _no_floats(v)


def jcs(value):
    _no_floats(value)
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def rev_input(meta, text):
    return {
        "statement": statement_of(text),
        "conventions": meta.get("conventions") or [],
        "ambiguity": meta.get("ambiguity") or [],
        "acceptance": meta.get("acceptance"),
        "challenge_sha256": (meta.get("formal_challenge") or {}).get("sha256"),
    }


def card_rev(meta, text):
    return hashlib.sha256(jcs(rev_input(meta, text))).hexdigest()[:16]
