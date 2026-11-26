#!/usr/bin/env python3
"""群星证据文件工具（CON-040）。设计见 docs/specs/查新与证据状态-设计.md，用法见 contracts/evidence/README.md。

状态和分类的取值都写在取值表 qunxing.vocab-1.json 里。加状态、改名、补中文写法、加分类都只改那张表，
再运行 sync 重算全部证据文件，不用改这个脚本。

  python3 evidence.py sync   --data <qunxing-data> [--check]
  python3 evidence.py import --data <qunxing-data> <回传.jsonl 或 清单.md>... [--ids <题号清单>] [--replace] [--check]
  python3 evidence.py review --data <qunxing-data> [<题号> accept|reject --by <谁> [--note <说明>]]
  python3 evidence.py set    --data <qunxing-data> (<题号> <状态或分类> <取值> | --file <表格>) --by <谁> [--note …] [--check]
  python3 evidence.py check  --data <qunxing-data>
  都可以加 --vocab <取值表>；不加时用 <qunxing-data>/schema/qunxing.vocab-1.json。

导入时：原样存档到 novelty/inbox/；没通过检查的行放进 novelty/quarantine/；合并进 evidence/<分片>/<题号>.json
并重算摘要；要人看的写进 novelty/reviews/<批号>.md；改动清单写进 import/。题卡一个字都不动。
"""
import argparse
import csv
import datetime
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
HANDOFF = 'qunxing.novelty-handoff/2'
LISTS = ('math_results', 'queries', 'evidence', 'duplicates', 'card_actions', 'pending')
PER_BATCH = ('math_results', 'card_actions', 'pending')  # 每批各自的判断，不跨批去重
SETTABLE = ('math_status', 'formal_evidence', 'search_coverage')  # 摘要里可以人工改的状态；新分类放 facets
NEEDED = ('math_status', 'formal_evidence', 'search_coverage', 'claim_state', 'claim_review', 'scope_match', 'route', 'query_outcome')
CODE = re.compile(r'[a-z][a-z0-9_]*')
CLEAR = {'', 'auto', '自动', '清除'}


def norm(s):
    """去掉空白和括号里的补充说明，统一斜杠：'不适用（纯组合题）' → '不适用'。"""
    return re.sub(r'[（(][^）)]*[）)]|\s+', '', str(s or '')).replace('／', '/')


def head(s):
    """冒号、逗号前的部分：'仅特例：n≤10' → '仅特例'。"""
    return re.split(r'[：:，,；;。]', norm(s), maxsplit=1)[0]


def day(s):
    m = re.match(r'\s*(\d{4})[-/.年](\d{1,2})[-/.月](\d{1,2})', str(s or ''))
    return f'{int(m[1]):04d}-{int(m[2]):02d}-{int(m[3]):02d}' if m else ''


def today():
    return datetime.date.today().isoformat()


def pick(d, *keys):
    for k in keys:
        if d.get(k) not in (None, '', []):
            return d[k]
    return None


def dig(obj, path):
    for k in (path or '').split('.'):
        obj = obj.get(k) if isinstance(obj, dict) else None
    return obj


def dumps(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2) + '\n'


def put(path, content):
    """内容有变才写；返回是否写了。"""
    data = content.encode('utf-8') if isinstance(content, str) else content
    if path.exists() and path.read_bytes() == data:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return True


def ev_path(data, pid):
    return data / 'evidence' / pid[5:8] / f'{pid}.json'


class Vocab:
    """取值表 qunxing.vocab/1：dimensions 是摘要和记录里用到的状态，facets 是以后加的分类。"""

    def __init__(self, path):
        self.path = Path(path)
        raw = json.loads(self.path.read_text(encoding='utf-8'))
        if raw.get('schema') != 'qunxing.vocab/1':
            sys.exit(f'{self.path} 不是 qunxing.vocab/1 取值表')
        self.facets = set(raw.get('facets') or {})
        self.dims = {**(raw.get('dimensions') or {}), **(raw.get('facets') or {})}
        self.values, self.alias, errs = {}, {}, []
        for name, d in self.dims.items():
            if not CODE.fullmatch(name):
                errs.append(f'{name}：名字只能用小写字母、数字和下划线')
            vals, amap = {}, {}
            for i, v in enumerate(d.get('values') or []):
                c = v.get('code', '')
                if not CODE.fullmatch(c) or c in vals:
                    errs.append(f'{name}：代号 {c!r} 重复，或者用了小写字母、数字和下划线以外的字符')
                vals[c] = dict(v, rank=v.get('rank', i * 10))
            for c, v in vals.items():
                for a in [c, v.get('zh')] + list(v.get('aliases') or []) + list(v.get('replaces') or []):
                    k = norm(a)
                    if k and amap.setdefault(k, c) != c:
                        errs.append(f'{name}：写法"{a}"同时对应 {amap[k]} 和 {c}')
            self.values[name], self.alias[name] = vals, amap
            fc = d.get('from_card') or {}
            refs = [v.get('pending_as') for v in vals.values()] + list((d.get('rules') or {}).values()) + list((fc.get('map') or {}).values())
            refs += [d.get('default'), d.get('item_default'), fc.get('default'), fc.get('ai_claim_lean_checked')]
            refs += [d['unknown']] if d.get('unknown') not in (None, 'quarantine', 'ignore') else []
            errs += [f'{name}：用到了取值表里没有的代号 {r}' for r in refs if r and r not in vals]
        errs += [f'缺少 {n}' for n in NEEDED if n not in self.dims or n in self.facets]
        if errs:
            sys.exit(f'取值表 {self.path} 有错：\n  ' + '\n  '.join(errs))

    def code(self, dim, value):
        """中文写法、别名、旧代号或代号 → 现在的代号；认不出返回 None。"""
        if value is None or dim not in self.dims:
            return None
        for k in (norm(value), head(value)):
            if k in self.alias[dim]:
                return self.alias[dim][k]
        if self.dims[dim].get('match') == 'contains':
            v = norm(value)
            for c, entry in self.values[dim].items():
                if any(norm(kw) and norm(kw) in v for kw in entry.get('keywords') or []):
                    return c
        return None

    def raw(self, dim, item):
        return pick(item, *(self.dims[dim].get('fields') or [dim])) if dim in self.dims else None

    def lookup(self, dim, item):
        """按 fields 的顺序逐个字段找，第一个认得出的取值算数。返回 (代号, 写了的原文列表)。"""
        found = []
        for f in (self.dims[dim].get('fields') or [dim]) if dim in self.dims else []:
            v = item.get(f)
            if v in (None, '', []) or isinstance(v, dict):
                continue
            for x in (v if isinstance(v, list) else [v]):
                found.append(x)
                c = self.code(dim, x)
                if c:
                    return c, found
        return None, found

    def item_code(self, dim, item):
        """一条记录在这个维度上的代号：没写用 item_default；认不出时 unknown 是代号就用它。"""
        c, found = self.lookup(dim, item)
        if c:
            return c
        if not found:
            return (self.dims.get(dim) or {}).get('item_default')
        u = self.dims[dim].get('unknown', 'quarantine')
        return u if u in self.values[dim] else None

    def get(self, dim, code, key, default=None):
        return self.values.get(dim, {}).get(code, {}).get(key, default)

    def label(self, dim, code):
        return self.get(dim, code, 'zh') or str(code)

    def rank(self, dim, code):
        return self.get(dim, code, 'rank', -1)

    def flagged(self, dim, key):
        return {c for c, v in self.values.get(dim, {}).items() if v.get(key)}

    def rule(self, dim, key):
        return self.dims[dim]['rules'][key]

    def default(self, dim):
        return self.dims[dim].get('default')

    def facet_value(self, dim, value):
        """分类的取值：multi 的可以写多个（顿号、分号或竖线隔开）；open 的不查取值表。认不出返回 None。"""
        d = self.dims[dim]
        items = value if isinstance(value, list) else (re.split(r'[、;；|]', str(value)) if d.get('multi') else [value])
        items = [str(x).strip() for x in items if str(x).strip()]
        out = items if d.get('open') else [self.code(dim, x) for x in items]
        if not out or None in out:
            return None
        return list(dict.fromkeys(out)) if d.get('multi') else out[0]

    def per_version(self, dim):
        return dim in SETTABLE or bool(self.dims[dim].get('per_version'))


class Bank:
    """一份 qunxing-data：取值表、题卡、记录过的旧版本号、已删除的题号，以及读进内存的证据文件。"""

    def __init__(self, data, vocab=None):
        self.data = Path(data)
        path = Path(vocab) if vocab else next((p for p in (self.data / 'schema' / 'qunxing.vocab-1.json',
                                                           HERE.parent / 'qunxing.vocab-1.json') if p.exists()), None)
        if not path:
            sys.exit('找不到取值表 qunxing.vocab-1.json，用 --vocab 指定')
        self.vc = Vocab(path)
        self.cards, self.old_revs, self.alias, self.removed = {}, {}, {}, {}
        for p in sorted((self.data / 'problems').glob('*/*.meta.json')):
            m = json.loads(p.read_text(encoding='utf-8'))
            self.cards[m['id']] = m
            old = (m.get('novelty') or {}).get('card_rev')
            if old and old != m['card_rev']:
                self.old_revs[m['id']] = {old}
        for p in sorted((self.data / 'import').glob('*card-rev-migration*.json')):
            mig = json.loads(p.read_text(encoding='utf-8'))
            # 只认"题面没变、只换了哈希算法"的迁移：旧写法和新值是同一个版本
            if mig.get('changed') and mig.get('old_values_explained_by_legacy_algorithm') == mig.get('changed'):
                for ch in mig.get('changes', []):
                    self.alias[(ch['id'], ch['card_rev'][0])] = ch['card_rev'][1]
        for p in sorted((self.data / 'import').glob('*removed*.json')):
            rm = json.loads(p.read_text(encoding='utf-8'))
            for x in rm.get('removed', []):
                self.removed[x['id']] = f'这张题卡 {rm.get("date", "")} 已删除：{rm.get("decision", "")}'
        self.docs, self.orig, self.unknown = {}, {}, Counter()
        self.assume_schema = False

    def doc(self, pid):
        if pid not in self.docs:
            p = ev_path(self.data, pid)
            self.orig[pid] = p.read_text(encoding='utf-8') if p.exists() else None
            self.docs[pid] = json.loads(self.orig[pid]) if self.orig[pid] else \
                {'schema': 'qunxing.evidence/1', 'id': pid, 'card_rev': self.cards[pid]['card_rev'], 'summary': {},
                 'batches': [], **{k: [] for k in LISTS}}
        return self.docs[pid]

    def save(self):
        changed = [pid for pid, doc in self.docs.items() if dumps(doc) != self.orig[pid]]
        for pid in changed:
            put(ev_path(self.data, pid), dumps(self.docs[pid]))
        return len(changed)


# ---------- 重算摘要（设计第 2、4、6 节）：同样的输入总是得到同样的结果 ----------
def has_source(e):
    return bool(pick(e, 'url', 'link') and pick(e, 'locator', 'location'))


def has_rerun(e):
    rr = e['rerun'] if isinstance(e.get('rerun'), dict) else e
    return bool(pick(rr, 'commit') and pick(rr, 'command', 'log', 'log_url'))


def annotate(it, vc, where):
    """按取值表给一条记录算代号（codes）：来源是 where 的维度都算。evidence 有问题时写 issue。"""
    it['codes'] = {dim: c for dim, d in vc.dims.items()
                   if d.get('from') == where and dim not in vc.facets and (c := vc.item_code(dim, it))}
    if where != 'evidence':
        return
    it.pop('issue', None)
    c = it['codes']
    if not has_source(it):
        it['issue'] = '缺直接链接或原文定位，不进摘要'
    elif c.get('formal_evidence') in vc.flagged('formal_evidence', 'pass') and not has_rerun(it):
        c['formal_evidence'] = vc.rule('formal_evidence', 'pass_without_record')
        it['issue'] = f'标了复跑通过，但缺固定 commit、命令或日志，按"{vc.label("formal_evidence", c["formal_evidence"])}"记'


def legacy_summary(card, vc):
    """还没有 v2 回传时的初值，由题卡旧字段映射。"""
    fallback = day((card.get('informal_status') or {}).get('as_of'))
    s = {}
    for dim in ('math_status', 'formal_evidence'):
        fc = vc.dims[dim].get('from_card') or {}
        v = (fc.get('map') or {}).get(dig(card, fc.get('field'))) or fc.get('default') or vc.default(dim)
        if fc.get('ai_claim_lean_checked') and v == fc.get('default') and any(a.get('lean_checked') for a in card.get('ai_claims') or []):
            v = fc['ai_claim_lean_checked']
        date = day(dig(card, fc.get('as_of_field'))) or fallback
        s[dim] = {'value': vc.get(dim, v, 'pending_as', v), **({'as_of': date} if date else {}), 'basis': [f'card:{fc.get("field")}']}
    checked = day(dig(card, 'novelty.last_checked_at'))
    s['search_coverage'] = {'value': vc.rule('search_coverage', 'legacy'), 'checked_at': checked} if checked \
        else {'value': vc.default('search_coverage')}
    s['legacy'] = True
    return s


def decided(doc, vc, rev, v, batch):
    return any(d.get('dimension') == 'math_status' and d.get('action') in ('accept', 'reject') and d.get('card_rev') == rev
               and d.get('batch_id') == batch and vc.code('math_status', d.get('value')) == v for d in doc.get('decisions') or [])


def compute(doc, card, vc, batch=None):
    """按题卡、回传记录、人工决定和取值表重算 summary、facets 和每条记录的代号；返回要人看的说明。"""
    rev, notes = card['card_rev'], []
    doc['card_rev'] = rev
    bat = {b['batch_id']: b for b in doc['batches']}
    when = {k: b.get('checked_at') or b['imported_at'] for k, b in bat.items()}
    order = {k: (when[k], i) for i, k in enumerate(bat)}
    for b in doc['batches']:
        annotate(b, vc, 'row')
    for k in LISTS:
        for it in doc[k]:
            annotate(it, vc, k)
            if k == 'evidence' and it['batch_id'] == batch and it.get('issue'):
                notes.append(f'证据 {pick(it, "url", "link", "title", "text") or "（无链接）"}：{it["issue"]}')
    s = legacy_summary(card, vc)
    cur = [b for b in doc['batches'] if b['card_rev'] == rev]
    # 当前版本没有回传时，用最近一批的旧版本记录作参考
    use = rev if cur else (max(doc['batches'], key=lambda b: order[b['batch_id']])['card_rev'] if doc['batches'] else None)
    legacy, latest = use != rev, {}
    if use:
        recs = {k: [x for x in doc[k] if x['card_rev'] == use] for k in LISTS}
        bs = [b for b in doc['batches'] if b['card_rev'] == use]
        last = max(bs, key=lambda b: order[b['batch_id']])

        # 查新覆盖：本版本各批里最高的一级；要求核心路线的，缺一路真实记录就降级
        routes = dict.fromkeys(sorted(vc.flagged('route', 'core')), False)
        for q in recs['queries']:
            r, o = q['codes'].get('route'), q['codes'].get('query_outcome')
            if r in routes and q.get('query') and o and vc.get('query_outcome', o, 'record', True):
                routes[r] = True
        if legacy:
            dates = [b['checked_at'] for b in bs if b.get('checked_at')]
            s['search_coverage'] = {'value': vc.rule('search_coverage', 'legacy'), **({'checked_at': max(dates)} if dates else {})}
        else:
            cov = lambda b: b['codes'].get('search_coverage') or vc.default('search_coverage')  # noqa: E731
            best = max(bs, key=lambda b: (vc.rank('search_coverage', cov(b)), order[b['batch_id']]))
            value = cov(best)
            if vc.get('search_coverage', value, 'needs_core_routes') and not all(routes.values()):
                lower = vc.rule('search_coverage', 'missing_core_routes')
                if best['batch_id'] == batch:
                    gaps = '、'.join(vc.label('route', k) for k, ok in routes.items() if not ok)
                    notes.append(f'回传写的是"{vc.label("search_coverage", value)}"，但{gaps}没有真实检索记录，'
                                 f'按"{vc.label("search_coverage", lower)}"记')
                value = lower
            s['search_coverage'] = {'value': value, **({'checked_at': best['checked_at']} if best.get('checked_at') else {}),
                                    'routes': routes}

        # 数学结论：每个子问取最近一批的说法；闭合状态先当"提议"，二审后才算数
        msd = vc.dims['math_status']
        main = {norm(x) for x in msd.get('main_subquestion') or []} | {''}
        patterns = [re.compile(x) for x in msd.get('main_patterns') or []]
        closed = vc.flagged('math_status', 'closed')
        mains = {}
        for m in sorted(recs['math_results'], key=lambda m: order[m['batch_id']]):
            sub = str(pick(m, *(msd.get('subquestion_fields') or ['subquestion'])) or '').strip()
            compact = re.sub(r'\s+', '', sub)
            k = '' if compact in main or (norm(sub) and norm(sub) in main) or any(p.search(compact) for p in patterns) else sub
            v = m['codes'].get('math_status') or vc.default('math_status')
            prev = latest.get(k)
            if prev and prev[0]['batch_id'] == m['batch_id'] and vc.rank('math_status', prev[1]) >= vc.rank('math_status', v):
                continue
            latest[k] = (m, v)
            if not k:
                mains[m['batch_id']] = v
        if '' not in latest and latest:
            # 没有单独的主问题结论：按子问保守推出，只会排除、不会结案（取值表 math_status 的 note）
            codes = [v for _, v in latest.values()]
            stmt, claims = vc.flagged('math_status', 'statement_problem'), vc.flagged('math_status', 'claim') | closed
            if any(c in stmt for c in codes):
                derived = vc.rule('math_status', 'derive_statement')
            elif any(c in claims for c in codes):
                derived = vc.rule('math_status', 'derive_pending')
            else:
                derived = max(codes, key=lambda c: vc.rank('math_status', c))
            newest = max((m for m, _ in latest.values()), key=lambda m: order[m['batch_id']])
            s['math_status'] = {'value': derived, 'as_of': when[newest['batch_id']], 'basis': ['derived:subquestions'],
                                'note': '没有单独的主问题结论，按子问保守推出'}
        if '' in latest:
            m, v = latest['']
            s['math_status'] = {'value': vc.get('math_status', v, 'pending_as', v), 'as_of': when[m['batch_id']],
                                'basis': [f'batch:{m["batch_id"]}']}
            if v in closed and legacy:
                if m['batch_id'] == batch:
                    notes.append(f'主问题：旧版本上提议"{vc.label("math_status", v)}"，题卡已换版本，不能直接结案')
            elif v in closed and not decided(doc, vc, rev, v, m['batch_id']):
                s['math_status_proposed'] = {'value': v, 'batch_id': m['batch_id'], 'basis': [f'batch:{b}' for b in bat if mains.get(b) == v],
                                             **({'note': str(m['scope_note'])} if m.get('scope_note') else {})}
        parts = []
        for k, (m, v) in latest.items():
            if k:
                note = str(m.get('scope_note') or '')
                if v in closed:
                    note = f'提议"{vc.label("math_status", v)}"，待二审' + (f'；{note}' if note else '')
                    if m['batch_id'] == batch:
                        notes.append(f'子问 {k}：提议"{vc.label("math_status", v)}"，待二审')
                parts.append({'subquestion': k, 'value': vc.get('math_status', v, 'pending_as', v), **({'note': note} if note else {})})
        if parts:
            s['math_status']['parts'] = parts

        # 形式化、最强声明：同一条证据（链接 + 定位 + 版本 + 子问）只看最近一批的记录
        seen = {}
        for e in sorted((e for e in recs['evidence'] if has_source(e)), key=lambda e: order[e['batch_id']]):
            seen[json.dumps([pick(e, 'url', 'link'), pick(e, 'locator', 'location'), pick(e, 'version', 'evidence_version'),
                             pick(e, 'subquestions', 'subquestion', 'covers')], ensure_ascii=False, sort_keys=True)] = e
        evs = list(seen.values())
        passes, full = vc.flagged('formal_evidence', 'pass'), vc.flagged('scope_match', 'full')

        def level(e):
            v = e['codes']['formal_evidence']
            return vc.rule('formal_evidence', 'pass_partial_scope') if v in passes and e['codes'].get('scope_match') not in full else v
        formals = [e for e in evs if e['codes'].get('formal_evidence')]
        if formals:
            top = max(formals, key=lambda e: vc.rank('formal_evidence', level(e)))
            s['formal_evidence'] = {'value': level(top), 'as_of': when[top['batch_id']], 'basis': [str(pick(top, 'url', 'link'))]}
            if top['codes'].get('scope_match') not in full:
                s['formal_evidence']['note'] = f'只覆盖：{vc.raw("scope_match", top) or vc.label("scope_match", top["codes"].get("scope_match"))}'
        elif any(routes.get(r) for r in vc.flagged('route', 'formal_search')) and s['formal_evidence']['value'] == vc.default('formal_evidence') \
                and not any(e['codes'].get('role') in vc.flagged('role', 'formal') for e in recs['evidence']):
            s['formal_evidence'] = {'value': vc.rule('formal_evidence', 'formal_route_no_hits'), 'as_of': when[last['batch_id']]}
        no_claim, demote = vc.flagged('claim_state', 'not_a_claim'), vc.flagged('claim_review', 'demotes_claim')
        claims = [e for e in evs if e['codes'].get('claim_state') not in (None, *no_claim) and e['codes'].get('scope_match') in full]
        if claims:
            def strength(e):
                rv = e['codes'].get('claim_review') or vc.default('claim_review')
                return (-10 ** 6 if rv in demote else vc.rank('claim_state', e['codes']['claim_state']), vc.rank('claim_review', rv))
            c = max(claims, key=strength)
            s['claim'] = {'state': c['codes']['claim_state'], 'url': str(pick(c, 'url', 'link'))}
            if c['codes'].get('claim_review'):
                s['claim']['review'] = c['codes']['claim_review']
            for k, names in (('by', ('claimant', 'claim_by', 'by', 'authors', 'author')), ('date', ('claim_date', 'date'))):
                v = pick(c, *names)
                if v:
                    s['claim'][k] = '、'.join(map(str, v)) if isinstance(v, list) else str(v)
        if not legacy:
            s.pop('legacy')

    # 人工决定（二审、set）：每个状态或分类取最后一条；摘要状态只认当前版本的
    eff = {}
    for d in doc.get('decisions') or []:
        dim = d.get('dimension')
        if dim in vc.dims and d.get('action') in ('set', 'clear', 'accept') and (not vc.per_version(dim) or d.get('card_rev') == rev):
            eff[dim] = d
    facets = {}
    for dim, d in eff.items():
        v = None if d['action'] == 'clear' else (vc.facet_value(dim, d.get('value')) if dim in vc.facets else vc.code(dim, d.get('value')))
        if v is None:
            continue
        who = {'by': d['by'], 'at': d['at'], **({'note': d['note']} if d.get('note') else {})}
        if dim in vc.facets:
            facets[dim] = {'value': v, **who, **({'basis': d['basis']} if d.get('basis') else {})}
            continue
        if dim == 'math_status' and '' in latest and latest[''][0]['batch_id'] == batch and latest[''][1] != v:
            notes.append(f'主问题：这批写的是"{vc.label(dim, latest[""][1])}"，和人工确认的"{vc.label(dim, v)}"不同，请复核')
        keep = {'parts': s[dim]['parts']} if s[dim].get('parts') else {}
        s[dim] = {'value': v, 'as_of': d['at'], **({'basis': d['basis']} if d.get('basis') else {}), 'reviewed': who, **keep}
        if dim == 'math_status' and (s.get('math_status_proposed') or {}).get('value') == v:
            del s['math_status_proposed']
    doc['summary'] = s
    if facets:
        doc['facets'] = facets
    else:
        doc.pop('facets', None)
    return notes


# ---------- 读一行回传、合并 ----------
def parse_row(raw, bank):
    """返回 (行, 问题列表)。有问题的行整行隔离；认不出的取值记进 bank.unknown，方便补取值表。"""
    vc = bank.vc
    try:
        r = json.loads(raw)
    except json.JSONDecodeError as e:
        return None, [f'不是合法的 JSON（{e.msg}）']
    if not isinstance(r, dict):
        return None, ['不是 JSON 对象']
    errs = []
    if r.get('schema') is None and bank.assume_schema:
        r['schema'] = HANDOFF
    if r.get('schema') != HANDOFF:
        errs.append(f'schema 不是 {HANDOFF}')
    for k in ('batch_id', 'id', 'card_rev'):
        if not isinstance(r.get(k), str) or not r[k].strip():
            errs.append(f'缺 {k}')
    if isinstance(r.get('search_summary'), dict):  # 有的回传把覆盖写成对象，级别在 depth 里；原样另存
        r['search_summary_detail'], r['search_summary'] = r['search_summary'], r['search_summary'].get('depth') or ''
    for k in LISTS:
        v = r.get(k) or []
        if not isinstance(v, list):
            errs.append(f'{k} 应是数组')
            continue
        r[k] = [x if isinstance(x, dict) else {'text': str(x)} for x in v]
    if errs:
        return r, errs
    pid = r['id']
    if pid not in bank.cards:
        errs.append(bank.removed.get(pid) or '题库里没有这个题号')
    else:
        r['_rev'] = bank.alias.get((pid, r['card_rev']), r['card_rev'])
        if r['_rev'] != bank.cards[pid]['card_rev'] and r['_rev'] not in bank.old_revs.get(pid, ()):
            errs.append(f'card_rev {r["card_rev"]} 不认识：既不是当前版本，也不是记录过的旧版本')
    if r.get('checked_at') and not day(r['checked_at']):
        errs.append(f'checked_at 不是日期：{r["checked_at"]}')
    for dim, d in vc.dims.items():
        if dim in vc.facets or not d.get('from'):
            continue
        for it in [r] if d['from'] == 'row' else r.get(d['from']) or []:
            c, found = vc.lookup(dim, it)
            if found and c is None:
                bank.unknown[(dim, str(found[0])[:60])] += 1
                if d.get('unknown', 'quarantine') == 'quarantine':
                    errs.append(f'{d.get("zh", dim)}的取值不认识：{str(found[0])[:60]}')
    for e in r['evidence']:
        if vc.raw('scope_match', e) is None and (vc.raw('formal_evidence', e) or vc.raw('claim_state', e)):
            bank.unknown[('scope_match', '（没写）')] += 1
    return r, errs


def raw_key(it):
    return json.dumps({k: v for k, v in it.items() if k not in ('batch_id', 'codes', 'issue')}, ensure_ascii=False, sort_keys=True)


def merge(doc, r, replace):
    """把一行原样并进证据文件。同一批已经导过就跳过（--replace 时先删掉这批原来的记录）。"""
    b = r['batch_id']
    if any(x['batch_id'] == b for x in doc['batches']):
        if not replace:
            return False
        doc['batches'] = [x for x in doc['batches'] if x['batch_id'] != b]
        for k in LISTS:
            doc[k] = [x for x in doc[k] if x['batch_id'] != b]
    doc['batches'].append({'batch_id': b, 'card_rev': r['_rev'], **({'card_rev_sent': r['card_rev']} if r['card_rev'] != r['_rev'] else {}),
                           'checked_at': day(r.get('checked_at')), 'imported_at': today(), 'search_summary': str(r.get('search_summary') or '')})
    for k in LISTS:
        have = set() if k in PER_BATCH else {raw_key(x) for x in doc[k]}
        for it in r[k]:
            it = dict(it, batch_id=b, card_rev=r['_rev'])
            if raw_key(it) not in have:
                doc[k].append(it)
                have.add(raw_key(it))
    return True


# ---------- 命令 ----------
def cmd_sync(args):
    bank, made, changed = Bank(args.data, args.vocab), 0, 0
    for pid, card in bank.cards.items():
        doc = bank.doc(pid)
        made += bank.orig[pid] is None
        compute(doc, card, bank.vc)
        changed += bank.orig[pid] is not None and dumps(doc) != bank.orig[pid]
    if not args.check:
        bank.save()
    orphans = [p.stem for p in (bank.data / 'evidence').glob('*/*.json') if p.stem not in bank.cards]
    print(f'题卡 {len(bank.cards)} 张；新生成证据文件 {made} 个，按取值表或题卡新版本重算后有变化的 {changed} 个'
          + (f'；没有对应题卡的证据文件 {len(orphans)} 个（不自动删）：{" ".join(orphans[:10])}' if orphans else '')
          + ('（只检查，没有写）' if args.check else ''))


def archive(data, src):
    """原样存进 novelty/inbox/，只追加：同名不同内容时另起一个名字。"""
    inbox, raw = data / 'novelty' / 'inbox', src.read_bytes()
    for n in range(1, 1000):
        p = inbox / (src.name if n == 1 else f'{src.stem}-{n}{src.suffix}')
        if not p.exists():
            put(p, raw)
            return p
        if p.read_bytes() == raw:
            return p
    sys.exit(f'{src.name}：inbox 里同名文件太多')


def import_file(bank, src, expected, replace, dry):
    vc = bank.vc
    lines = [(i, ln) for i, ln in enumerate(src.read_text(encoding='utf-8-sig').splitlines(), 1) if ln.strip()]
    rows, bad = [], []
    for i, ln in lines:
        r, errs = parse_row(ln, bank)
        if errs:
            bad.append({'line': i, 'reason': '；'.join(errs), 'raw': ln})
        else:
            rows.append((i, ln, r))
    count = Counter(r['id'] for _, _, r in rows)
    missing = sorted(expected - set(count)) if expected is not None else []
    good = []
    for i, ln, r in rows:
        if count[r['id']] > 1:
            bad.append({'line': i, 'reason': '同一题号出现多行', 'raw': ln})
        elif expected is not None and r['id'] not in expected:
            bad.append({'line': i, 'reason': '不在这批的题号清单里', 'raw': ln})
        else:
            good.append(r)
    bad.sort(key=lambda b: b['line'])
    batches = sorted({r['batch_id'] for _, _, r in rows}) or [src.stem]
    tag = re.sub(r'[\\/:*?"<>|\s]+', '_', batches[0] if len(batches) == 1 else src.stem)[:80]
    rep = {'updated': [], 'skipped': [], 'legacy': [], 'proposed': [], 'notes': [], 'actions': [], 'dups': []}
    no_change = vc.flagged('card_action', 'no_change')
    for r in good:
        doc = bank.doc(r['id'])
        if not merge(doc, r, replace):
            rep['skipped'].append(r['id'])
            continue
        rep['updated'].append(r['id'])
        rep['notes'] += [(r['id'], n) for n in compute(doc, bank.cards[r['id']], vc, r['batch_id'])]
        if r['_rev'] != doc['card_rev']:
            rep['legacy'].append((r['id'], r['card_rev'], doc['card_rev']))
        pr = doc['summary'].get('math_status_proposed')
        if pr and pr['batch_id'] == r['batch_id']:
            rep['proposed'].append((r['id'], vc.label('math_status', pr['value']), pr.get('note', '')))
        rep['actions'] += [(r['id'], a) for a in r['card_actions'] if vc.item_code('card_action', a) not in no_change]
        rep['dups'] += [(r['id'], d) for d in r['duplicates']]
    if not dry:
        archive(bank.data, src)
        qfile = bank.data / 'novelty' / 'quarantine' / f'{tag}.jsonl'
        changed = put(qfile, ''.join(json.dumps(b, ensure_ascii=False) + '\n' for b in bad)) if bad else False
        if rep['updated']:
            put(bank.data / 'novelty' / 'reviews' / f'{tag}.md', review_md(tag, rep, bad, missing))
        if rep['updated'] or changed:
            put(bank.data / 'import' / f'{today()}-novelty-{tag}.json', dumps(
                {'source': src.name, 'batches': batches, 'vocab': bank.vc.path.name, 'rows': len(lines), 'accepted': len(good),
                 'updated': len(rep['updated']), 'already_imported': len(rep['skipped']), 'quarantined': len(bad),
                 'legacy_version': len(rep['legacy']), 'proposed_closures': len(rep['proposed']), 'card_actions': len(rep['actions']),
                 'duplicates': len(rep['dups']), 'notes': len(rep['notes']), 'missing_ids': missing, 'updated_ids': rep['updated']}))
    print(f'{src.name}：{len(lines)} 行，收下 {len(good)}（更新 {len(rep["updated"])}，以前导过 {len(rep["skipped"])}），'
          f'隔离 {len(bad)}，题卡版本不符 {len(rep["legacy"])}，提议结案 {len(rep["proposed"])}，'
          f'题卡改动建议 {len(rep["actions"])}，查重 {len(rep["dups"])}，降级说明 {len(rep["notes"])}'
          + (f'，清单里缺 {len(missing)} 题' if missing else ''))
    for b in bad[:10]:
        print(f'  隔离 第 {b["line"]} 行：{b["reason"]}')
    if len(bad) > 10:
        print(f'  ……隔离的行共 {len(bad)} 行')
    return len(lines), len(good), len(bad)


def review_md(tag, rep, bad, missing):
    out = [f'# 待复核清单 · {tag}', '', '由 `evidence.py import` 生成。提议结案用 `evidence.py review` 记二审结论；'
           '题卡改动走题卡修订流程；查重的合并要二审。', '']

    def cell(c):
        return (c if isinstance(c, str) else json.dumps(c, ensure_ascii=False)).replace('|', '\\|').replace('\n', ' ')

    def table(title, cols, rows):
        if rows:
            out.extend([f'## {title}（{len(rows)}）', '', '| ' + ' | '.join(cols) + ' |', '|' + '---|' * len(cols)]
                       + ['| ' + ' | '.join(cell(c) for c in row) + ' |' for row in rows] + [''])
    table('提议结案（要二审）', ['题号', '提议', '说明'], rep['proposed'])
    table('题卡改动建议', ['题号', '建议'], rep['actions'])
    table('查重', ['题号', '关系'], rep['dups'])
    table('降级和冲突说明', ['题号', '说明'], rep['notes'])
    table('题卡版本不符，只记成旧版参考', ['题号', '回传的 card_rev', '当前 card_rev'], rep['legacy'])
    table('隔离的行', ['行', '原因'], [(str(b['line']), b['reason']) for b in bad])
    table('清单里有、回传里没有', ['题号'], [(i,) for i in missing])
    return '\n'.join(out) + '\n'


def cmd_import(args):
    if args.ids and sum(not f.lower().endswith('.md') for f in args.files) > 1:
        sys.exit('--ids 只配一个回传文件')
    bank = Bank(args.data, args.vocab)
    bank.assume_schema = args.assume_schema
    expected = set(Path(args.ids).read_text(encoding='utf-8').split()) if args.ids else None
    total = Counter()
    for src in map(Path, args.files):
        if src.suffix.lower() == '.md':
            if not args.check:
                archive(bank.data, src)
            print(f'{src.name}：清单，原样存档')
            continue
        n, ok, bad = import_file(bank, src, expected, args.replace, args.check)
        total.update(rows=n, accepted=ok, quarantined=bad)
    written = 0 if args.check else bank.save()
    print(f'合计 {total["rows"]} 行，收下 {total["accepted"]}，隔离 {total["quarantined"]}；'
          + ('试导，没有写任何文件' if args.check else f'写了 {written} 个证据文件'))
    if bank.unknown:
        print('不认识的取值（补进取值表的 aliases，或者请查新 GPT 改成规范里的写法）：')
        for (dim, value), n in bank.unknown.most_common(30):
            print(f'  {dim}：{value}（{n} 次）')


def cmd_review(args):
    bank = Bank(args.data, args.vocab)
    if not args.id:
        rows = []
        for p in sorted((bank.data / 'evidence').glob('*/*.json')):
            pr = json.loads(p.read_text(encoding='utf-8'))['summary'].get('math_status_proposed')
            if pr:
                rows.append(f'{p.stem}\t{pr["value"]}\t{pr["batch_id"]}\t{pr.get("note", "")}')
        print('\n'.join(rows) if rows else '没有待二审的结案提议')
        return
    if not (args.decision and args.by):
        sys.exit('记二审结论要写 accept 或 reject，并用 --by 写明是谁审的')
    if args.id not in bank.cards:
        sys.exit(f'题库里没有 {args.id}')
    doc = bank.doc(args.id)
    pr = doc['summary'].get('math_status_proposed')
    if not pr:
        sys.exit(f'{args.id} 没有待二审的结案提议')
    doc.setdefault('decisions', []).append({'dimension': 'math_status', 'action': args.decision, 'value': pr['value'],
                                            'batch_id': pr['batch_id'], 'card_rev': doc['card_rev'], 'by': args.by, 'at': today(),
                                            **({'note': args.note} if args.note else {})})
    compute(doc, bank.cards[args.id], bank.vc)
    bank.save()
    print(f'{args.id}：{bank.vc.label("math_status", pr["value"])} {"二审确认" if args.decision == "accept" else "二审驳回"}')


def read_table(path, dimension):
    """人工改状态、批量加分类用的表：CSV/TSV（表头 id,dimension,value,note,basis）或 JSONL。"""
    text = path.read_text(encoding='utf-8-sig')
    if path.suffix.lower() == '.jsonl':
        rows = [(i, json.loads(ln)) for i, ln in enumerate(text.splitlines(), 1) if ln.strip()]
    else:
        rows = list(enumerate(csv.DictReader(text.splitlines(), delimiter='\t' if path.suffix.lower() == '.tsv' else ','), 2))
    return [(i, {**r, 'dimension': r.get('dimension') or dimension}) for i, r in rows]


def cmd_set(args):
    bank = Bank(args.data, args.vocab)
    vc = bank.vc
    if args.file:
        rows = read_table(Path(args.file), args.dimension)
    elif args.id and args.dimension and args.value is not None:
        rows = [(0, {'id': args.id, 'dimension': args.dimension, 'value': args.value})]
    else:
        sys.exit('写 <题号> <状态或分类> <取值>，或者用 --file 给一张表')
    allowed = '、'.join(list(SETTABLE) + sorted(vc.facets)) or '无'
    done, same, bad = 0, 0, []
    for line, r in rows:
        pid, dim, val = str(r.get('id') or '').strip(), str(r.get('dimension') or '').strip(), r.get('value')
        clear = not isinstance(val, list) and str(val or '').strip() in CLEAR
        v = None if clear or dim not in vc.dims else vc.facet_value(dim, val) if dim in vc.facets else vc.code(dim, val)
        basis = r.get('basis') or args.basis or []
        basis = basis.split() if isinstance(basis, str) else list(basis)
        err = ('题库里没有这个题号' if pid not in bank.cards else
               f'{dim} 不能人工改（能改的：{allowed}）' if dim not in SETTABLE and dim not in vc.facets else
               f'{dim} 的取值不认识：{val}' if not clear and v is None else
               '复跑通过要用 --basis 写明依据（commit、日志链接）' if isinstance(v, str) and v in vc.flagged(dim, 'pass') and not basis else '')
        if err:
            bad.append((line, err))
            continue
        doc = bank.doc(pid)
        rec = {'dimension': dim, 'action': 'clear' if clear else 'set', **({} if clear else {'value': v}),
               **({'card_rev': bank.cards[pid]['card_rev']} if vc.per_version(dim) else {}), 'by': args.by, 'at': today(),
               **({'note': r.get('note') or args.note} if r.get('note') or args.note else {}), **({'basis': basis} if basis else {})}
        prev = [d for d in doc.get('decisions') or [] if d.get('dimension') == dim and d.get('action') in ('set', 'clear', 'accept')
                and (not vc.per_version(dim) or d.get('card_rev') == rec.get('card_rev'))]
        if (prev and (prev[-1]['action'] == 'clear') == clear and prev[-1].get('value') == rec.get('value')) or (clear and not prev):
            same += 1
            continue
        doc.setdefault('decisions', []).append(rec)
        compute(doc, bank.cards[pid], vc)
        done += 1
    if not args.check:
        bank.save()
    print(f'改了 {done} 条，和现在一样的 {same} 条，有问题的 {len(bad)} 条' + ('（只检查，没有写）' if args.check else ''))
    for line, err in bad[:20]:
        print(f'  第 {line} 行：{err}')
    if bad:
        sys.exit(1)


def cmd_check(args):
    bank = Bank(args.data, args.vocab)
    errors, validator = [], None
    if not args.skip_schema:
        schema = next((p for p in (bank.data / 'schema' / 'qunxing.evidence-1.schema.json', HERE.parent / 'qunxing.evidence-1.schema.json')
                       if p.exists()), None)
        if not schema:
            sys.exit('找不到 qunxing.evidence-1.schema.json')
        try:
            from jsonschema import Draft202012Validator
        except ImportError:
            sys.exit('检查证据文件要装 jsonschema（4.18 以上），或者加 --skip-schema')
        validator = Draft202012Validator(json.loads(schema.read_text(encoding='utf-8')))
    seen = set()
    for p in sorted((bank.data / 'evidence').rglob('*.json')):
        rel = p.relative_to(bank.data)
        try:
            text = p.read_text(encoding='utf-8')
            doc = json.loads(text)
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            errors.append(f'{rel}: JSON 解析失败：{e}')
            continue
        if validator:
            errs = [f'{rel}: {"/".join(map(str, e.absolute_path)) or "(根)"}: {e.message[:200]}' for e in validator.iter_errors(doc)]
            if errs:
                errors += errs
                continue
        pid = doc.get('id') if isinstance(doc, dict) else None
        if not isinstance(pid, str) or pid not in bank.cards:
            errors.append(f'{rel}: 题库里没有 {pid}')
            continue
        seen.add(pid)
        if p != ev_path(bank.data, pid):
            errors.append(f'{rel}: 位置不对，应在 {ev_path(bank.data, pid).relative_to(bank.data)}')
        ms = (doc.get('summary') or {}).get('math_status') or {}
        if ms.get('value') in bank.vc.flagged('math_status', 'closed') and not ms.get('reviewed'):
            errors.append(f'{rel}: 数学结论是闭合状态 {ms["value"]}，但没有二审记录')
        again = json.loads(text)
        compute(again, bank.cards[pid], bank.vc)
        if dumps(again) != text:
            errors.append(f'{rel}: 和题卡、记录、取值表算出来的不一致（题卡换了版本、取值表改了，或者手改过？运行 evidence.py sync）')
    for pid in sorted(set(bank.cards) - seen):
        errors.append(f'{pid}: 缺证据文件（运行 evidence.py sync）')
    for e in errors[:200]:
        print(e)
    print(f'证据文件 {len(seen)} 个，题卡 {len(bank.cards)} 张，错误 {len(errors)} 条')
    sys.exit(1 if errors else 0)


def labels(vc, dim):
    """取值表里一类取值能用的写法：中文名和别名。"""
    return sorted({v['zh'] for v in vc.values[dim].values() if v.get('zh')} |
                  {a for v in vc.values[dim].values() for a in v.get('aliases') or []})


def handoff_schema(vc):
    """查新回传的固定结构（经验总结第 7 条）。取值都从取值表来，取值表改了重新生成。"""
    S = lambda **k: {'type': 'string', **k}  # noqa: E731
    E = lambda dim: {'enum': labels(vc, dim)}  # noqa: E731
    obj = lambda props, req: {'type': 'object', 'additionalProperties': False, 'required': req, 'properties': props}  # noqa: E731
    date, rev, pid = S(pattern=r'^\d{4}-\d{2}-\d{2}$'), S(pattern='^[0-9a-f]{16}$'), S(pattern=r'^QX-P-\d{6}$')
    route = {'anyOf': [E('route'), S(pattern='^其他：.+')]}
    strs = {'type': 'array', 'items': {'type': 'string'}}
    return {
        '$schema': 'https://json-schema.org/draft/2020-12/schema',
        '$id': 'https://www.qunxingmath.org/schema/qunxing.novelty-handoff-2.schema.json',
        'title': '查新回传 qunxing.novelty-handoff/2（固定结构，由取值表生成）',
        'description': '每题一行。标签字段只写取值表里的写法，细节写进 note / scope_note。字段名固定，不要换成 status、verdict、result、actual_request 之类。',
        **obj({
            'schema': {'const': HANDOFF}, 'batch_id': S(minLength=1), 'id': pid, 'card_rev': rev,
            'checked_at': {'anyOf': [date, {'const': ''}]}, 'search_summary': E('search_coverage'),
            'summary': S(maxLength=400, description='一两句话的人读总结'),
            'math_results': {'type': 'array', 'minItems': 1,
                             'contains': {'type': 'object', 'properties': {'subquestion': {'const': '主问题'}}, 'required': ['subquestion']},
                             'items': obj({'subquestion': S(minLength=1, description='主问题必须单独一行，写"主问题"'),
                                           'math_status': E('math_status'), 'scope_note': S(), 'evidence_ids': strs},
                                          ['subquestion', 'math_status'])},
            'queries': {'type': 'array', 'items': obj({
                'request_id': S(description='同一次请求给多道题共用时，各题写同一个编号'), 'route': route, 'site': S(), 'query': S(),
                'date': date, 'outcome': E('query_outcome'), 'url': S(), 'locator': S(), 'result_count': {'type': 'integer', 'minimum': 0},
                'shared_with': {'type': 'array', 'items': pid}, 'match_reason': S(description='共用请求时，这道题的命中理由'), 'note': S()},
                ['route', 'site', 'query', 'date', 'outcome'])},
            'evidence': {'type': 'array', 'items': obj({
                'evidence_id': S(), 'url': S(minLength=1), 'locator': S(minLength=1), 'version': S(minLength=1, description='arXiv 版本、日期或提交号'),
                'subquestions': strs, 'role': E('role'), 'publication': E('publication'), 'scope_match': E('scope_match'),
                'claim_state': E('claim_state'), 'review_status': E('claim_review'), 'formal_status': E('formal_evidence'),
                'claimant': S(), 'claim_date': S(), 'rerun': obj({'commit': S(), 'theorem': S(), 'toolchain': S(), 'command': S(),
                                                                  'log_url': S(), 'cache': S(), 'axioms': S()}, []),
                'note': S()}, ['url', 'locator', 'version', 'subquestions', 'scope_match'])},
            'duplicates': {'type': 'array', 'items': obj({
                'other_id': pid, 'other_card_rev': rev, 'relation': E('duplicate_relation'), 'reason': S(minLength=1),
                'positions': obj({'self': S(), 'other': S()}, []), 'note': S()}, ['other_id', 'other_card_rev', 'relation', 'reason'])},
            'card_actions': {'type': 'array', 'items': obj({
                'action': E('card_action'), 'field': S(), 'old': S(), 'new': S(), 'reason': S(), 'evidence_ids': strs,
                'small_case_check': S(description='改题面时：用小例或空对象试过的结果')}, ['action'])},
            'pending': {'type': 'array', 'items': obj({'route': route, 'reason': S(), 'next_step': S(minLength=1)}, ['next_step'])},
        }, ['schema', 'batch_id', 'id', 'card_rev', 'checked_at', 'search_summary', 'math_results', 'queries', 'evidence',
            'duplicates', 'card_actions', 'pending']),
    }


def cmd_handoff_schema(args):
    vc = Bank(args.data, args.vocab).vc if args.data else Vocab(args.vocab or HERE.parent / 'qunxing.vocab-1.json')
    text = json.dumps(handoff_schema(vc), ensure_ascii=False, indent=2) + '\n'
    if args.out:
        put(Path(args.out), text)
        print(f'已写入 {args.out}')
    else:
        print(text, end='')


def main(argv=None):
    ap = argparse.ArgumentParser(description='群星证据文件：生成和重算、导入查新回传、二审、人工改状态和分类、检查')
    sub = ap.add_subparsers(dest='cmd', required=True)

    def cmd(name, help_text):
        a = sub.add_parser(name, help=help_text)
        a.add_argument('--data', required=True, help='qunxing-data 的目录')
        a.add_argument('--vocab', help='取值表；默认 <data>/schema/qunxing.vocab-1.json')
        return a
    a = cmd('sync', '给每张题卡生成证据文件；按取值表和题卡的当前版本重算全部摘要')
    a.add_argument('--check', action='store_true', help='只检查，不写')
    a = cmd('import', '导入查新回传（.jsonl）；清单（.md）原样存档')
    a.add_argument('files', nargs='+')
    a.add_argument('--ids', help='这批应有的题号清单，空白分隔')
    a.add_argument('--replace', action='store_true', help='同一批改过以后重新导入：先删掉这批原来的记录')
    a.add_argument('--assume-schema', action='store_true', help='回传行没写 schema 时当作 qunxing.novelty-handoff/2（旧交付用）')
    a.add_argument('--check', action='store_true', help='试导：只报结果，不写')
    a = cmd('review', '列出待二审的结案提议；或记一条二审结论')
    a.add_argument('id', nargs='?')
    a.add_argument('decision', nargs='?', choices=('accept', 'reject'))
    a.add_argument('--by')
    a.add_argument('--note')
    a = cmd('set', '人工改一个摘要状态，或者给题目加分类（facets）；取值写 auto 表示撤销人工改动')
    a.add_argument('id', nargs='?')
    a.add_argument('dimension', nargs='?')
    a.add_argument('value', nargs='?')
    a.add_argument('--file', help='批量：CSV/TSV（表头 id,dimension,value,note,basis）或 JSONL')
    a.add_argument('--dimension', dest='dimension_opt', help='表里没有 dimension 列时，统一用这个')
    a.add_argument('--by', required=True)
    a.add_argument('--note')
    a.add_argument('--basis', nargs='*', help='依据：链接、commit 等')
    a.add_argument('--check', action='store_true', help='只检查，不写')
    a = sub.add_parser('handoff-schema', help='按取值表生成查新回传的 JSON Schema（交给查新 GPT 用）')
    a.add_argument('--data', help='qunxing-data 的目录；不写就用 --vocab 或契约里的取值表')
    a.add_argument('--vocab')
    a.add_argument('--out')
    a = cmd('check', '检查全部证据文件：格式、取值、和重算结果是否一致')
    a.add_argument('--skip-schema', action='store_true')
    args = ap.parse_args(argv)
    if args.cmd == 'set':
        args.dimension = args.dimension or args.dimension_opt
    {'sync': cmd_sync, 'import': cmd_import, 'review': cmd_review, 'set': cmd_set, 'check': cmd_check,
     'handoff-schema': cmd_handoff_schema}[args.cmd](args)


if __name__ == '__main__':
    main()
