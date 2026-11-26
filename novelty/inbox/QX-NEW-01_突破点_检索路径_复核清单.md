# QX-NEW-01｜突破点、检索路径与复核清单

**查核日期：2026-11-26（Asia/Shanghai）。范围：包内唯一任务清单的100张题卡。**

本轮完成100/100逐题联网初查，按输入顺序保留全部原始 `id`、`card_rev`、`batch_id`；30/30指定查重对子均对照双方包内当前正文。参考卡只用于比较，没有扩张成额外任务。100张卡的输入待办均为P1；发现可能改状态、题面或冲突声明后，优先核查这些证据。线上改卡、合并和发帖均为零。

逐题回传共有 **868条实际检索、来源访问或本地核对记录，242项证据，182条修改建议**。这些是记录数，不是独立网页数；批量检索的同一回执可以供不同题目使用。每题均记录原题/出处、至少两套学术检索、GitHub/代码、公开AI/社区、库内查重五路。入口报错、仅摘要、后续普通HTTPS补取与命中不适用分别登记。零命中从未被当成开放性证明。

## 1. 优先处理的实质发现

| 题号 | 本轮变化与建议 | 证据定位和适用边界 |
|---|---|---|
| 001432 | 原存在性子问可改为否定 | Lazar–Somerset已刊论文Corollary5.3；无需CH，按非空目标空间解释。 |
| 001516 | 小规模距离集目标已有旧结果 | Erdős–Fishburn(1996), Theorem1及印刷p.117 Fig.1；给出n=6,7,8,9最少距离数3,3,4,4与不等价最优构型。一般n问题未因此解决。 |
| 001445、001438 | 分别修正已解子问 | 1445原帖Edit2解决Q3，Q1另保留；1438的2017定理覆盖实对称4×4，并非任意复Hermitian。 |
| 001472 | 当前全称题式被反驳 | 4×4二维马图删中心4顶点后有6个分量，违反Hamilton路径必要条件。附自写DP与可手核割集证书；不把该反例扩张到原意k≥3。 |
| 001486 | 当前左支撑断言被反驳 | 标准单边移位及秩一投影的显式解析反例；推导在本报告，经过本轮另核，非发表结果、非形式化运行。 |
| 001431 | 得到完整解析推导，保留待外部复核 | 有限角色筛法与Chebyshev整数多项式构造；本轮主审解析二审通过。须恢复满秩条件，不宣称文献优先权或形式化通过。 |
| 001471 | 新完整证明声明需按系数版本登记 | Ottem arXiv:2611.31152v1，Theorem1.1；原稿是整系数对角线问题，不能直接关闭当前加入有理系数的版本。 |
| 001483 | 有限反例已核；无限族有精确匹配的新声明 | 本轮穷尽核验两个六顶点图；Hexagon新稿与固定提交定理`NWDigraph.counterexample_all`已核对应，未运行Lean。Hexagon编号不能替换成同号arXiv。 |
| 001485 | 新稿直接覆盖矩形微分分类；旧题“极大”含义有误 | arXiv:2608.23871v2，Corollary1.3 pp.17–18；完整证明声明待核。255页全文只核关键命题与范围，未完成全证明审查。 |
| 001495、001496 | 排除错误或范围不足的新声明 | 1495新稿否认周期1轨道，但代入可得两个不动点；这不反驳原mild-dissipation问题。1496新稿限于特定primary kneading pair，局部非退化不足以推出原问的全局唯一。 |
| 001521、001522 | 错误追溯到上游原始条目 | 1521混写EGZ、Davenport与Gao常数，且普遍等式不成立；1522的标准模量型Jackson式多除一次n^r，用高频余弦即矛盾。应先重建正确题面。 |
| 001508、001511–001515、001523–001527 | 校正问题范围、来源编号与定义 | 分别涉及CI/DCI、固定朝向EPG、树宽/树深、完整强积、树同构计数、合法落子规则以及Kourovka原题条件；具体修改见逐项记录。 |

上述每条的原文链接、定理或页码、实际检索词与待复核点均在后文对应题号下。优先表只帮助安排人工复核，不能作为整卡状态的批量替换表。

## 2. 数学结论的计数口径

以下按**子问**计数；同一题卡可以同时包含“题面有误”“部分进展”和“暂未找到可验证结果”。因此不能把各行相加解释成已解决题卡数。

| 子问判断 | 子问条数 | 涉及题卡数（可重叠） |
|---|---:|---:|
| 原题已证 | 13 | 12 |
| 原题已反驳 | 5 | 5 |
| 已知独立 | 0 | 0 |
| 部分进展 | 41 | 39 |
| 完整证明/反例声明待核 | 13 | 13 |
| 题面有误 | 46 | 44 |
| 暂未找到可验证结果 | 83 | 78 |
| 未作判断 | 12 | 11 |

数学状态、文献强度和形式化程度是三件事。没有任何条目声称本轮独立重跑外部形式化系统通过。001483记录为“已核定理对应、未重跑”；其他作者声明、不可达固定提交和占位定理分别标注。本轮实际运行的是自写有限核验程序；解析推导另行给出证明，不冒充Lean验证。

## 3. 查重结果

30个指定对子全部有双方版本及比较理由。对方卡自身正文信息不足时也明确保留这一限制，未将标题相似直接判断为等价。新增6个候选关系如下；其中5个补取并比较了对方现版全文，1个仍待取得全文。

| 本任务题号/版本 | 对方题号/版本 | 关系 | 判定范围 |
|---|---|---|---|
| QX-P-001428 / 7679dcabbf4a7dfd | QX-P-000727 / 7274e6c984870d08 | 同源不同问 | 000727 正是每条边连接异度顶点时 M_G graphic 的正边猜想，与001428所引正边子问同题且同源 MO140819。001428当前主目标还包括一般图 graphic 失衡的结构刻画，因此不判整卡同题，不合并。 |
| QX-P-001445 / 0428162da116ee8e | QX-P-000322 / d7fe3a812162c2a6 | 待定 | 索引是整个平面稠密有理距离集，题面线索与本题 toy good 集相关；未取得当前全文，不能判重复。 |
| QX-P-001468 / 98d1be205e208076 | QX-P-000738 / 38dc6dfbd7c18427 | 相关但不等价 | 新线索已补取官网现版全文，页脚card_rev与索引38dc6dfbd7c18427一致。000738是对每个n>1、P为前n素数积，存在p_n<p<P使P+p素数；本题是对同一素数p检查(p−1)!+p并问无穷性，变量/乘积/量词均不同。 |
| QX-P-001469 / 772cfab02d631b92 | QX-P-001246 / 9e6c3f68818d8ac9 | 同题 | 补取官网现版完整题面、形式化及人话版，页脚card_rev9e6c3f68818d8ac9与索引一致。双方主问均为∀n∈Z∃x1,…,x4∈Z，n=Σxi³，允许负数；001246附带五立方/非负子问题不改变主命题。该卡所写五立方等式右侧实际为6m−1，另留修订提示。 |
| QX-P-001517 / c78e7840f7960032 | QX-P-000211 / 55b33e37dcfa461a | 同题 | 补齐1517的渐近量词后等价：若无5共线集合的4-rich线数不是o(n²)，则某固定c>0有任意大n违反1517；反向由同一逆否推理。原卡“有限目标”须先修正；不是把Erdős102一般增长率全问与101合并。 |
| QX-P-001518 / f4ed19afedaf12ea | QX-P-001289 / 3d0c777f5ae41623 | 特例/强化 | 同一猜想来源但当前题面不等价：001289漏monic，其全称断言被a=2,b=(1+x)/2反驳；1518含monic是受限版本。先修正001289归一化后才可按同题处理。 |

## 4. 回传文件与审计约定

- `QX-NEW-01_逐题回传.jsonl`：100行，顺序与输入一致。顶层必需字段完整；新增统一的`math_results[].status/conclusion/formal_status`、`duplicates[].relation/pair_id/assigned`及路径前缀，保留原分组的细分字段。
- `QX-NEW-01_突破点_检索路径_复核清单.md`：完整实质发现及解析证明；不逐题复述零命中。
- `QX-NEW-01_校验报告.json`：身份、路线、30个指定对子、版本与文件引用校验，以及统计口径。
- `group_*/receipts/`：实际请求、来源URL/引用号、入口错误及原始回执SHA256。为避免重复分发论文或网页全文，附件为回执索引；逐题结论和访问层级保存在JSONL。原始正文成功读取不等于本包附带原文全文。
- `group_02/receipts/1472_knight4x4.py`及JSON：本轮自写有限图核验；`group_03/verify_finite_examples.py`及`finite_verification.json`：六顶点图与模幂核验。`group_03/formalization_review.json`仅为作者代码的静态对应与依赖记录。
- `input/`保留用户给定的原包文本，供版本和指定对子复核。新增候选卡只记录读取事实、版本、来源和摘要，不增加逐题回传行。

本文之后是四组实质发现的完整合编。回传包内同时保留分组报告以支持本地证明锚点。各组记录中的早期入口失败属于实际路径；若后续补取成功，以该来源的最终访问层级及补取说明为准。

## 5. 逐项实质发现与复核清单


### QX-NEW-01｜group_01 突破点、检索路径与复核清单

查核日期：2026-11-26，Asia/Shanghai。范围为 group_01 的 25 张卡；所有输入优先级为 P1。此文件只列影响状态、题面、出处或查重的发现；逐题完整记录及真实查询见 QX-NEW-01_逐题回传.jsonl，实际请求与来源索引见 group_01/receipts/（原始正文不重复打包）。未改线上、未发帖、未运行外部代码，也没有独立形式化通过记录。

#### 优先复核项

| 题号 | 建议处理 | 证据强度与界限 |
|---|---|---|
| 001432 | 原存在性问否定 | 已刊论文 Cor.5.3；无需 CH，按非空空间解释 |
| 001445 | Q3 改已证，Q1 单独保留 | 原帖 Edit2 与明确构造 |
| 001438 | 实对称 4×4 子问改已证 | 2017 已刊论文；一般复 Hermitian 未直接覆盖 |
| 001428 | 撤销错误的正边反例；新证明待核 | 原反例可直接核范围；新稿/Lean 是作者声明 |
| 001421 | 增完整证明声明待核 | 纸面 Theorem1.1 对应；固定提交访问失败 |
| 001431 | 本轮解析二审通过，仍待外部复核 | 显式多项式构造，不冒称文献解决或形式化验证 |
| 001444 | 记新有限参数结果待核 | 预印本；finite exclusions 使用 native reflection |

下面每项的“暂未找到可验证结果”只描述已列入口；无 accepted、零答案、零检索命中均不构成开放性证明。

#### QX-P-001419

**旧卡 → 变化：**只有旧综述与一般开放标记 → 补入 2026 年算法进展，并排除一篇已撤回的改进界稿。

**本轮结论：**查到 2026 年局部/全局邮票算法进展，但不是所有 n(h,k) 的闭式或完全分类；另有已撤回预印本不能作为新界证据。

**证据与适用范围：**

- [原始问题综述](https://people.math.wisc.edu/~awmille1/res/fun-maa.pdf) — Guy, Unsolved Problems, AMM 94 (1987), 印刷 p.963 / PDF p.3。邮票问题的参数及 at most h stamps 口径。 访问层级：全文已访问。
- [预印本作者原稿](https://membres-ljk.imag.fr/Bruno.Grenet/publis/CDGGM26.pdf) — Colisson Palais 等, Algorithms for the local and the global postage stamp problem, §2–3；Theorem 3.2 p.10。局部范围计算及全局近似/构造；不能把近似算法改写成一般精确解。 访问层级：正文及关键定理已访问。
- [撤回预印本](https://arxiv.org/abs/2507.23627) — v2, 2025-11-11，撤回说明。下界证明存在缺口；排除相应未经修复的界。 访问层级：版本页已访问。
- [作者代码仓库](https://github.com/jgdumas/GStamps) — 程序 alba、bala 由原稿 §3.1 指认。算法实现命中，不是一般 n(h,k) 已解的证明。 访问层级：搜索命中；未固定提交、未运行。

**实际检索路径：**

- system1_search："global postage stamp problem" "2601.21423"；回执 group_01/receipts/academic_01.json。
- system1_search：postage stamp problem optimal basis n(h,k) algorithm 2025 2026；回执 group_01/receipts/academic_01.json。
- system2_search：site:github.com "postage stamp" "global"；回执 group_01/receipts/code_community_01.json。
- system2_search："postage stamp problem" (site:aixiv.online OR site:zenodo.org OR site:mathoverflow.net OR site:hexagonmath.org)；回执 group_01/receipts/code_community_01.json。

**待复核：**

- GStamps 固定提交及输出范围尚未审计。
- 最新精确数表与 h、k 固定分支未作深查。

#### QX-P-001421

**旧卡 → 变化：**未记解决声明 → 新增覆盖原不等式的 2026 年完整证明声明，仍待独立核查。

**本轮结论：**定位到 2026 年完整解决声明，纸面 Theorem 1.1 覆盖原题偶数维比较；作者称 Lean 验证通过，本轮未取得固定提交内容也未重跑，状态应为完整证明声明待核。

**证据与适用范围：**

- [原始题源](https://mathoverflow.net/questions/477402/poisson-binomial-conjecture) — 题目正文式（尾阈值 n/2）；2024-08-22。n 为偶数、坐标逐项 p≥q、独立 Bernoulli；原线程回答只给损失因子的进展。 访问层级：全文已访问。
- [作者完整证明声明](https://hexagonmath.org/pdf/2611.00708v1) — Christopher D. Long, The exact Poisson–binomial comparison in every dimension, Theorem 1.1, pp.1–2。纸面声明覆盖偶数 n 的原不等式，并处理全维数及等号结构；作者说明使用 Lean，未亲自检查全部细节。 访问层级：PDF 关键定理及核验说明已访问。
- [作者代码固定提交](https://github.com/long-mathematics/poisson-binomial-comparison/tree/b34cde620016c85e5c7d5461630c0fde3f098d4b) — SHA b34cde620016c85e5c7d5461630c0fde3f098d4b；论文所述 CI 提交。只核到论文列出的提交及 CI 声明，未核定理文件、依赖闭包或重跑。 访问层级：全文入口不可达：DisabledError。
- [原作者后续预印本](https://arxiv.org/abs/2601.04079v3) — Kontorovich, v3, 2026-02-25。常数因子进展与精确猜想分开。 访问层级：摘要与版本已访问。
- [公开 AI 成果页](https://aixiv.online/problems/kontorovichs-poisson-binomial-comparison-problem) — 问题页关联 2611.02285 等解决声明。页面的 proved 标签是平台/作者声明，不能升级成本轮独立验证。 访问层级：页面已访问。

**实际检索路径：**

- system1_search："477402" Bernoulli Kontorovich tail；回执 group_01/receipts/academic_01.json。
- system1_search："Bernoulli" "tail" "Kontorovich" "gamma" inequality binomial；回执 group_01/receipts/academic_01.json。
- system2_search：site:github.com ("477402" OR "Poisson binomial conjecture")；回执 group_01/receipts/code_community_01.json。
- system2_search："Poisson binomial conjecture" (site:aixiv.online OR site:zenodo.org OR site:mathoverflow.net OR site:hexagonmath.org)；回执 group_01/receipts/code_community_01.json。

**待复核：**

- 核对 n=2 及 γ=0,1 端点与所引用 B_n 的定义。
- 取得上述 SHA 的完整源文件、lean-toolchain、lake-manifest 和公理依赖，之后才可考虑重跑。
- 核清 aiXiv 各记录号与 Hexagon 版本之间的同稿关系。

#### QX-P-001424

**旧卡 → 变化：**主猜想、固定底特例和同余方法混在一项 → 拆问，并确认指定对子是特例/方法关系。

**本轮结论：**原题应拆为固定模数方法与特定偶数底 B 的三连 powerful；Entin 回答只阻断某类固定模数路线，不能当成 Erdős–Mollin–Walsh 主猜想的证明。指定对子属特例/方法细化。

**证据与适用范围：**

- [原始题源](https://mathoverflow.net/questions/468771/congruence-obstructions-for-three-consecutive-powerful-numbers) — 原帖两问、Wieferich 讨论。三连 powerful 主猜想、固定 B 的特例、有限模方法必须拆分。 访问层级：全文已访问。
- [社区数学论证](https://mathoverflow.net/questions/468771/congruence-obstructions-for-three-consecutive-powerful-numbers/477149) — Ofir Entin 答案，指数 φ(n²) 构造。固定 n 且相应互素条件下可消去拟议的同余阻碍。 访问层级：答案已访问。
- [形式化邻题仓库](https://github.com/golfyx/jsp-000301-lean) — 两相邻 powerful 非平方数 12167、12168。仅是两连续数，命中不适用于三连不存在命题。 访问层级：仅搜索摘要。

**查重：**

- QX-P-000491（rev 83c5f3ec3f35e73c）：特例/强化；双方随包全文已复核。000491 排除所有三连续 powerful；本题的偶数底幂分支是其特例，固定模数方法问题另有量词，不能当同题。

**实际检索路径：**

- system1_search："468771" powerful numbers；回执 group_01/receipts/academic_03.json。
- system1_search："consecutive powerful" "B" "Puccioni" "Entin"；回执 group_01/receipts/academic_03.json。
- system2_search：site:github.com "consecutive powerful" numbers；回执 group_01/receipts/code_community_03.json。
- system2_search："congruence obstructions" "powerful" (site:aixiv.online OR site:zenodo.org OR site:mathoverflow.net OR site:hexagonmath.org)；回执 group_01/receipts/code_community_03.json。

**待复核：**

- Wieferich 条件是否已被无条件替代未检出。
- 需澄清 powerful 是否包含 1，避免把 2^1−1=1 误说成非 powerful。

#### QX-P-001425

**旧卡 → 变化：**无重叠被简写成 a_n≥2^n → 该长度下界本身不足；最新稿仍只声称两极端已证。

**本轮结论：**已打开 Neunhäuserer 2026 预印本最新 v2，摘要仍明确把一般熵凹性列为猜想，已证两极端情形；共同参数 p 与异参数 Bernoulli 的凹性问题不能混同。

**证据与适用范围：**

- [原始题源](https://mathoverflow.net/questions/514729/a-recursive-overlap-construction-of-finite-bernoulli-sum-laws-and-an-entropy-con) — 递归定义、权重 Bernoulli 等价形式及评论。所有 Bernoulli 共享 p；不能用异参数反例冒充本题反例。 访问层级：全文已访问。
- [原作者预印本](https://arxiv.org/abs/2609.05546v2) — 2026-09-22 v2，Abstract。两极端已证，一般命题仍在稿中作为猜想；这是作者状态证据而非本轮开放性证明。 访问层级：摘要及版本已访问；正文未深核。

**实际检索路径：**

- system1_search："514729" entropy concave；回执 group_01/receipts/academic_03.json。
- system1_search："Bernoulli" "entropy" "Neunhäuserer" concavity weighted sums；回执 group_01/receipts/academic_03.json。
- system2_search：site:github.com "overlap" "Bernoulli" entropy；回执 group_01/receipts/code_community_03.json。
- system2_search："Bernoulli" "entropy concavity" (site:aixiv.online OR site:zenodo.org OR site:mathoverflow.net OR site:hexagonmath.org)；回执 group_01/receipts/code_community_03.json。

**待复核：**

- 最新正文中递归长度条件与加权表示的严格等价尚需逐式复核。
- 没有执行符号计算或外部代码。

本轮定义检查：令 a₁=2、a₂=8、a₃=9，此后可取 aₙ=2ⁿ。它满足逐项 aₙ≥2ⁿ。对 0<p<1，P₂ 支撑为 {0,1,6,7}；第三步右移量为 1，所以左右支撑在 {1,7} 相交。这只纠正“无重叠”的充分条件，不是熵凹性反例。

#### QX-P-001428

**旧卡 → 变化：**正边失衡猜想被 9 顶点反例否定 → 引用错位；原反例只否定允许零失衡版本，正边版另有新证明声明。

**本轮结论：**发现实质题面/状态错误：2013 反例含零边失衡，否定无前提版本，不能否定所有边失衡正的版本；后者另出现 2026 证明及 Lean 仓库声明，需单列待核。

**证据与适用范围：**

- [原始反例](https://mathoverflow.net/questions/140198/a-question-on-graphic-sequences) — Douglas S. Stones 答案；Kozerenko 2013-08-24 评论。反例序列含六个零与两个 2；后续评论提出严格正边失衡猜想。 访问层级：全文已访问。
- [原始题源](https://mathoverflow.net/questions/140819/graphs-with-graphic-imbalance-sequences) — 2013-08-30，Imbalance Conjecture 明确 imb(e)>0。无条件反例和有条件猜想分开。 访问层级：全文已访问。
- [完整证明预印本声明](https://arxiv.org/abs/2608.09191) — A Proof of the Imbalance Conjecture；James Alexander Schreib、Yousof Yavari。数学稿尚未取得可读全文，不据摘要宣告定理已核。 访问层级：仅搜索摘要；abs/html 多入口不可达。
- [作者形式化仓库](https://github.com/jamesschreib/imbalance-conjecture) — ImbalanceConjecture.lean；VerificationAudit.lean 的 Imbalance.imbalanceConjecture / imbalanceMultiset_graphic；Lean 4.30.0；mathlib c5ea00351c28e24afc9f0f84379aa41082b1188f。README 声称无自定义公理；审计文件列 choice/propext/Quot.sound。它是作者可运行断言，本轮未重跑，也未核完整定理假设链。 访问层级：README、主文件页、审计页与依赖页已访问；固定仓库 SHA 未取得。
- [查重对方当前题卡](https://www.qunxingmath.org/p/QX-P-000727/) — HTML 题面、原文摘录、已知进展及引用区；card_rev 7274e6c984870d08。每边异度的正边猜想，与001428正边子问同题；更广结构刻画不是整卡同题。 访问层级：先前 web.open 失败；后普通 HTTPS GET 200，全文已读取。

**查重：**

- QX-P-000727（rev 7274e6c984870d08）：同源不同问；双方当前全文已复核；对方线上 rev 与索引一致。000727 正是每条边连接异度顶点时 M_G graphic 的正边猜想，与001428所引正边子问同题且同源 MO140819。001428当前主目标还包括一般图 graphic 失衡的结构刻画，因此不判整卡同题，不合并。

**实际检索路径：**

- system1_search："graphic imbalance" Kozerenko；回执 group_01/receipts/academic_04.json。
- system1_search："imbalance conjecture" graph degree sequence counterexample；回执 group_01/receipts/academic_04.json。
- system2_search：site:github.com "imbalance conjecture"；回执 group_01/receipts/code_community_04.json。
- system2_search："graphic imbalance" (site:aixiv.online OR site:zenodo.org OR site:mathoverflow.net OR site:hexagonmath.org)；回执 group_01/receipts/code_community_04.json。

**待复核：**

- 取得 arXiv 稿完整正文与固定仓库 SHA，核定理假设和证明依赖。
- 核对 Raoui 的早期 Zenodo 声明、Schreib/Yavari 版本和优先权；本轮没有裁定先后。

#### QX-P-001429

**旧卡 → 变化：**环版本缺少后续定理 → 补入带 real 等附加假设的定理，禁止把假设当结论。

**本轮结论：**Capco 的广义 Artin–Schreier 原稿给带 Baer、real 和整闭等附加假设的定理；其前提已经要求 real，不能回答卡片试图由有限闭包推出 real 的一般约化环问题。

**证据与适用范围：**

- [原始题源](https://mathoverflow.net/questions/10449/artin-schreier-theorem-for-rings) — Capco 2010-01-02，问题及添加条件讨论。totally integral closure 与普通整闭包及域代数闭包不可互换。 访问层级：全文已访问。
- [作者论文原稿](https://www3.risc.jku.at/publications/download/risc_5375/generalized_field_theory_for_rings.pdf) — Capco, Theorem 1, p.1。Baer real 环等额外前提；部分进展不能推出任意约化环必 real。 访问层级：关键定理已访问。

**实际检索路径：**

- system1_search："Artin-Schreier" "ring" "Capco"；回执 group_01/receipts/academic_05.json。
- system1_search："totally integrally closed" "finite" "real" rings Artin Schreier；回执 group_01/receipts/academic_05.json。
- system2_search：site:github.com "Artin Schreier" "rings"；回执 group_01/receipts/code_community_05.json。
- system2_search："Artin-Schreier" "ring" (site:aixiv.online OR site:zenodo.org OR site:mathoverflow.net OR site:hexagonmath.org)；回执 group_01/receipts/code_community_05.json。

**待复核：**

- 一般约化环分支、K=L 退化分支及是否已有反例需要后续专查。

#### QX-P-001431

**旧卡 → 变化：**Poisson 路线未完成，因无 accepted 仍开放 → 本轮给出显式整数多项式推导，经本轮解析二审，仍待外部复核；补满秩。

**本轮结论：**联网未找到已发表完整代数收尾；本轮有限角色筛法与 Chebyshev 显式整数多项式推导已获主审解析二审通过。仍保守列完整推导待核，未外部审稿、未形式化；须补满秩 det V≠0。

**证据与适用范围：**

- [原始题源](https://mathoverflow.net/questions/484639/conjecture-closed-form-of-summation-over-an-integer-lattice) — 题目闭式及 answer 484726 的 Poisson 路线。已有回答只给指数格点和；不能把无 accepted 作为开放性证明。 访问层级：全文已访问。

**实际检索路径：**

- system1_search："484639" lattice closed form；回执 group_01/receipts/academic_06.json。
- system1_search："lattice" "sinh" "cosh" "integer polynomial" sum reciprocals；回执 group_01/receipts/academic_06.json。
- system2_search：site:github.com "integer lattice" "cosh" sum conjecture；回执 group_01/receipts/code_community_06.json。
- system2_search："summation over an integer lattice" (site:aixiv.online OR site:zenodo.org OR site:mathoverflow.net OR site:hexagonmath.org)；回执 group_01/receipts/code_community_06.json。

**待复核：**

- 外部数学审阅与可能已有同等文献的优先权检索未完成。
- 若拟改为正式已证卡，保留满秩、P∈Z[x] 无额外符号/次数限制的精确范围。

#### QX-P-001432

**旧卡 → 变化：**要求构造处处非第一可数商且标开放 → 已刊 Corollary 5.3 给非空情形否定答案。

**本轮结论：**已刊定理给出无条件否定答案：这类 Hausdorff Fréchet–Urysohn 商在稠密开集上第一可数，因此不可能处处非第一可数。不是依赖 CH 的结论。

**证据与适用范围：**

- [原始题源](https://mathoverflow.net/questions/364611/frechet-urysohn-quotient-of-second-countable-locally-compact-hausdorff-space) — 问题正文。源为第二可数局部紧 Hausdorff，目标 Hausdorff/FU；所加 Tychonoff 更强。 访问层级：全文已访问。
- [原始问题集](https://cmuc.karlin.mff.cuni.cz/pdf/cmuc1001/arhangav.pdf) — Arhangelskii 2010, Problems 5.14–5.15, 印刷 p.111。对照原始存在性问。 访问层级：全文已访问。
- [已刊论文](https://doi.org/10.4153/S0008439521000515) — Lazar–Somerset, Pure quotients and Morita’s theorem for kω-spaces, Corollary 5.3 与紧接的 Arkhangelskii’s question 段；在线 2021-07-15。无 CH 的 Cor.5.3 已排除；文中另追溯 Siwiec 1976。Theorem 5.4 的 CH 是更广命题，不能倒加到本题。 访问层级：全文与关键推论已访问。

**查重：**

- QX-P-002284（rev 53e30ff5507d6b2b）：相关但不等价；双方随包全文已复核。2284 问任意紧 Hausdorff 是否为齐性紧空间连续像；本题固定第二可数局部紧源并要求 FU、处处非第一可数目标，既不同问也无直接等价。
- QX-P-002503（rev c087ed109c76035e）：相关但不等价；双方随包全文已复核。2503 是 ZFC 弱第一可数但非第一可数的紧 Hausdorff 构造；不要求第二可数局部紧商表示，也不要求处处非第一可数或 FU。

**实际检索路径：**

- system1_search："364611" quotient Frechet Urysohn；回执 group_01/receipts/academic_06.json。
- system1_search："quotient" "locally compact" "nowhere first countable"；回执 group_01/receipts/academic_06.json。
- system2_search：site:github.com "Frechet Urysohn" "quotient"；回执 group_01/receipts/code_community_06.json。
- system2_search："quotient" "nowhere first countable" (site:aixiv.online OR site:zenodo.org OR site:mathoverflow.net OR site:hexagonmath.org)；回执 group_01/receipts/code_community_06.json。

**待复核：**

- Siwiec 1976 原文可再追溯；但当前已刊 Cor.5.3 足以给本题结论。

#### QX-P-001434

**旧卡 → 变化：**笼统询问 analytic Zariski 的 stable → 补入一维不可约、关联 AEC 的明确进展，保留逻辑口径。

**本轮结论：**查到 Zilber 2016 对一维不可约 analytic Zariski 结构关联 AEC 的稳定性/范畴性结果；这不是任意维、原语言下一阶稳定性的无条件证明。

**证据与适用范围：**

- [原始题源](https://mathoverflow.net/questions/153047/stability-of-analytic-zariski-structures) — 2013 问题正文。所问 stable 的逻辑语言和模型类需明确。 访问层级：全文已访问。
- [原作者预印本](https://arxiv.org/pdf/1601.02961) — Boris Zilber, pp.1–2，主结果 (1)–(3)；v1 2016-01-12。假设 one-dimensional、irreducible；关联 AEC 的结论不能直接改写成所有 analytic Zariski 结构一阶稳定。 访问层级：导言及主结论说明已访问。

**实际检索路径：**

- system1_search："analytic Zariski structures" stable Peatfield Zilber；回执 group_01/receipts/academic_07.json。
- system1_search："analytic Zariski" "stability" quasiminimal；回执 group_01/receipts/academic_07.json。
- system2_search：site:github.com "analytic Zariski"；回执 group_01/receipts/code_community_07.json。
- system2_search："analytic Zariski" "stable" (site:aixiv.online OR site:zenodo.org OR site:mathoverflow.net OR site:hexagonmath.org)；回执 group_01/receipts/code_community_07.json。

**待复核：**

- 待以原文定理号、语言约化与 closure 定义逐项对应卡片中 stable 的口径。

#### QX-P-001435

**旧卡 → 变化：**只列连通稳定子已知 → 原题还列阿贝尔稳定子的正分支。

**本轮结论：**原问题不只连通 H 有正结果；原帖说明 H 连通或阿贝尔时的实局部化满射。任意非连通非阿贝尔 H 的普遍实逼近未取得完整答案。

**证据与适用范围：**

- [原始题源](https://mathoverflow.net/questions/50570/real-approximation-for-homogeneous-spaces-of-linear-algebraic-groups) — Borovoi 2010，loc∞ 讨论。连通或阿贝尔 H 分支已知，非连通不能一律视为未解。 访问层级：全文已访问。
- [相关作者论文](https://pure.mpg.de/pubman/item/item_3122278_1/component/file_3122279/borovoi_vanishing_oa_2011.pdf) — Vanishing of algebraic Brauer–Manin obstructions, Corollary 2.3 与 Question 2.4。搜索摘要显示连通或阿贝尔稳定子分支；全文受阻，未作完全定理适用核对。 访问层级：仅搜索定位 Cor.2.3 / Q.2.4；PDF 打开 403。

**实际检索路径：**

- system1_search："Borovoi" "real approximation" homogeneous spaces；回执 group_01/receipts/academic_08.json。
- system1_search："50570" "G/H" rational points；回执 group_01/receipts/academic_08.json。
- system2_search：site:github.com "real approximation" "homogeneous"；回执 group_01/receipts/code_community_08.json。
- system2_search："real approximation" "homogeneous" (site:aixiv.online OR site:zenodo.org OR site:mathoverflow.net OR site:hexagonmath.org)；回执 group_01/receipts/code_community_08.json。

**待复核：**

- 需取得 Cor.2.3 全文并核从 quasi-trivial G 到卡片一般 G 的步骤。
- 非连通非阿贝尔分支另查。

#### QX-P-001437

**旧卡 → 变化：**笼统说二维非方窗口存在性仍不确定 → 需按参数限定；相关构造进展不等于指定多重集计数。

**本轮结论：**计数给定局部子阵数据的二维环面问题未找到完整公式；新 de Bruijn 构造/存在论文与代码不能替代该计数问题。旧卡概括二维存在仍不清楚过宽。

**证据与适用范围：**

- [原始题源](https://mathoverflow.net/questions/10752/enumerating-generalized-de-bruijn-tori) — 2010-01-05 问题正文，二维枚举。需要保留周期矩形大小、窗口及是否模平移同构的计数口径。 访问层级：全文已访问。
- [相关作者论文](https://www-2.dc.uba.ar/staff/becher/papers/array.pdf) — 2024 nested perfect arrays，DOI 10.1109/TIT.2024.3445122。相关构造说明存在性文献已发展；不能推出本题任意多重集的计数。 访问层级：仅搜索摘要/引言命中；正文未深核。
- [代码仓库](https://github.com/man4/debruijn-torus) — 特定 rectangular torus 生成。生成一个例子不等于枚举全部或计数定理。 访问层级：仅搜索摘要。

**实际检索路径：**

- system1_search："generalized de Bruijn tori" count；回执 group_01/receipts/academic_09.json。
- system1_search："same multiset" "subarrays" torus de Bruijn；回执 group_01/receipts/academic_09.json。
- system2_search：site:github.com "generalized de Bruijn" tori；回执 group_01/receipts/code_community_09.json。
- system2_search："de Bruijn tori" "enumerating" (site:aixiv.online OR site:zenodo.org OR site:mathoverflow.net OR site:hexagonmath.org)；回执 group_01/receipts/code_community_09.json。

**待复核：**

- 未核全体 admissible 参数的存在定理；不以相关构造冒充该题解决。

#### QX-P-001438

**旧卡 → 变化：**连 4×4 都未证且所有角固定 ±45° → 实对称 4×4 已刊解决；固定角的误译需改。

**本轮结论：**4×4 实对称矩阵的并行 Jacobi 收敛已被 2017 已刊论文证明，且给定量 sweep 收缩；原卡不能继续笼统写连 4×4 都没证明。一般复 Hermitian 的对应仍需核查。

**证据与适用范围：**

- [原始题源](https://mathoverflow.net/questions/77434/convergence-speed-of-jacobi-eigenvalue-algorithm-for-parallel-orderingbrent-luk) — Chervov 2011，原题及 ±45° 歧义评论。原题是消去 pivot 的 Jacobi 旋转，不能将每次角都设 ±45°。 访问层级：规范题名网页正文已访问；短链部分失败。
- [已刊论文对应作者稿](https://arxiv.org/pdf/1701.02334) — v2 2017-03-27；LAA 524 (2017),199–234，DOI 10.1016/j.laa.2017.03.003。4 阶实对称、全并行策略及定量收缩结果。 访问层级：正文入口、摘要及主范围已访问。

**实际检索路径：**

- system1_search："Brent" "Luk" "Jacobi" "convergence" "4"；回执 group_01/receipts/academic_09.json。
- system1_search："Jacobi" "parallel ordering" "Hermitian" convergence；回执 group_01/receipts/academic_09.json。
- system2_search：site:github.com "Jacobi" "Brent" "convergence"；回执 group_01/receipts/code_community_09.json。
- system2_search："Jacobi" "parallel ordering" (site:aixiv.online OR site:zenodo.org OR site:mathoverflow.net OR site:hexagonmath.org)；回执 group_01/receipts/code_community_09.json。

**待复核：**

- 精确对照主定理中角区间/对角相等规则与 MO 所指定单侧约定。
- 复 Hermitian 版本及一般维数不得凭实对称结果推断。

#### QX-P-001441

**旧卡 → 变化：**未列近期搜索线索 → 有有限直径排除声明的镜像摘要，但原仓库不可达，不采纳其界。

**本轮结论：**原始八点问题与七点已知构造已对应；检索到有限直径排除的仓库线索，但原仓库入口失败，仅有镜像搜索摘要，不能作为新界已核。未取得八点构造或全局不存在证明。

**证据与适用范围：**

- [原始题源转述](https://mathoverflow.net/questions/53797/open-problems-in-euclidean-geometry) — answer 202871，Kreisel–Kurz 2008 引文。明确八点、无三共线、无四共圆、全距离整数；七点结果不是八点解。 访问层级：网页已访问。
- [代码声明线索](https://github.com/jaredwilder/integral-point-sets) — 摘要称 d(2,8)>30000、有限证书。缺固定提交、证书全文和独立审计，暂不采纳数值。 访问层级：镜像仅摘要；原仓库打开 DisabledError。

**实际检索路径：**

- system1_search："eight" "integer distances" "general position" points；回执 group_01/receipts/academic_10.json。
- system1_search："integral octagon" "no three" collinear；回执 group_01/receipts/academic_10.json。
- system2_search：site:github.com "integral octagon"；回执 group_01/receipts/code_community_10.json。
- system2_search："eight" "integer distances" (site:aixiv.online OR site:zenodo.org OR site:mathoverflow.net OR site:hexagonmath.org)；回执 group_01/receipts/code_community_10.json。

**待复核：**

- 取得 Kreisel–Kurz 原文与新仓库证书，核一般位置及尺度约定。

#### QX-P-001442

**旧卡 → 变化：**45 点与圆盘边界版本可能混列 → 45 点是浮点线索，44 点新结果明确为开圆盘版本。

**本轮结论：**已查到 2026 年 44 点不可覆盖声明及精确算术说明，但原文明确开圆盘；本卡是闭圆盘、内部不交。45 点旧上界也只是浮点实验。需要先核边界版本才能更新卡片界。

**证据与适用范围：**

- [原始题源](https://mathoverflow.net/questions/53797/open-problems-in-euclidean-geometry) — answer 202867，原句 pairwise-disjoint interior；另链 MO20558。本卡最大 k 与最小不可覆盖点数 m 满足 k=m−1。 访问层级：对应答案已访问。
- [相关作者预印本](https://arxiv.org/html/2611.13535v1) — Kittipassorn–Phetmak–Sriamorn 2026, §1。区分已知 50 点、45 点浮点搜索、44 点开圆盘精确结果；论文主结果针对无限三角格，非本题 k 的精确值。 访问层级：导言已访问。
- [作者会议摘要](https://eurocg26.fernuni-hagen.de/program-thursday.html) — Nakai–Bundo, A 44-Point Configuration Not Coverable by Disjoint Unit Disks, EuroCG26 Paper5。明确定义 pairwise disjoint open unit disks，声明以精确整数算术验证。 访问层级：摘要检索命中；论文全文未取得。

**实际检索路径：**

- system1_search："covering points" "disjoint unit disks" largest；回执 group_01/receipts/academic_11.json。
- system1_search："unit disks" "13" "45" covering points；回执 group_01/receipts/academic_11.json。
- system2_search：site:github.com "disjoint unit disks" covering；回执 group_01/receipts/code_community_11.json。
- system2_search："covering points" "disjoint unit disks" (site:aixiv.online OR site:zenodo.org OR site:mathoverflow.net OR site:hexagonmath.org)；回执 group_01/receipts/code_community_11.json。

**待复核：**

- 取得 Paper5 全文、配置与精确验证代码。
- 核开圆盘反例是否有正余量或扰动论证可转成本卡闭圆盘口径。

#### QX-P-001443

**旧卡 → 变化：**仅一般环面禁子式问题 → 新稿分类无 K5 minor 子类，并区分 minor 与 topological 数量。

**本轮结论：**定位到 2026 年排除 K5 minor 的环面障碍分类预印本：Theorem1.1 列 74 个 minor 障碍、Theorem8.1 列381个拓扑障碍；这是受限子类，不是全部环面 forbidden minors。

**证据与适用范围：**

- [原始题源](https://mathoverflow.net/questions/358385/list-of-long-open-elementary-problems-which-are-computational-in-nature/358414) — 对应 toroidal obstruction 答案。原目标是全部最小不可嵌入环面的 minor。 访问层级：网页已访问。
- [预印本原稿镜像](https://borowiecki.dev/pdf/2611.22089) — Toroidal Obstructions with No K5 Minor, Theorem1.1 p.2，Theorem8.1 与 §9 p.71。74 是无 K5 minor 子类；381 是同子类拓扑障碍。导言列 17535 个旧搜集及未收录图，需核历史数据版本。 访问层级：关键定理及结尾已访问；arXiv abs 入口失败。

**实际检索路径：**

- system1_search："toroidal" "forbidden minors" "complete" Myrvold Woodcock；回执 group_01/receipts/academic_11.json。
- system1_search："torus" "obstructions" "17523" graphs；回执 group_01/receipts/academic_11.json。
- system2_search：site:github.com "toroidal" "obstructions"；回执 group_01/receipts/code_community_11.json。
- system2_search："toroidal" "forbidden minors" (site:aixiv.online OR site:zenodo.org OR site:mathoverflow.net OR site:hexagonmath.org)；回执 group_01/receipts/code_community_11.json。

**待复核：**

- 74 图附录 O1/O4、完备性证明和镜像对应正式 arXiv 版本需二审。
- 17523/17535 历史计数差异需核 Myrvold–Woodcock 数据版本，不直接覆盖旧数。

#### QX-P-001444

**旧卡 → 变化：**只列旧公式及上界 → 新稿声称 h(4,3)=23、h(5,3)≥32，并明确不同形式化可信链。

**本轮结论：**新预印本给 h(4,3)=23、h(5,3)≥32 和一般容量下界；关键定理纸面已对应，算法/形式化可信链尚未独立验证。一般 h(n,k) 未完全解决。

**证据与适用范围：**

- [原始题源](https://mathoverflow.net/questions/462557/optimal-covering-trails-for-every-k-dimensional-cubic-lattice-mathbbnk) — Ripà 2024，H(n,k) 与 upper bounds。允许格外转折点的 covering trail，不能偷换为只能沿网格边行走。 访问层级：全文已访问。
- [预印本作者完整声明](https://arxiv.org/pdf/2611.28108) — Pessolano–Ripà, Theorem1.3 p.2；Theorem1.4、Table1 p.3；§形式化说明 pp.14–15。h(4,3)=23 和 h(5,3)≥32；一般实顶点、任意方向。作者明确有限排除依赖 native 编译器/运行时。 访问层级：主定理及形式化说明已访问。
- [论文所引证明工件](https://doi.org/10.5281/zenodo.24145830) — technical note and Lean proof artifacts v1.2, 2026-11-11。源论文列工件，但本轮没有取得固定代码、核依赖或运行。 访问层级：仅核论文引文；该 DOI 工件本轮未打开。

**实际检索路径：**

- system1_search："Ripà" "minimum-link" "H(n,k)"；回执 group_01/receipts/academic_12.json。
- system1_search："grid" "covering trail" "3" "2" Ripa 2026；回执 group_01/receipts/academic_12.json。
- system2_search：site:github.com "covering" "hypercubic" "trail"；回执 group_01/receipts/code_community_12.json。
- system2_search："covering trails" "Ripà" (site:aixiv.online OR site:zenodo.org OR site:mathoverflow.net OR site:hexagonmath.org)；回执 group_01/receipts/code_community_12.json。

**待复核：**

- 取得 Zenodo v1.2 工件和固定文件哈希，核有限枚举、退化段与 trail/chain 口径。
- 核原稿一般公式受新结果影响的具体参数，勿误报 h(2,k) 或 h(3,k) 已被推翻。

#### QX-P-001445

**旧卡 → 变化：**第3问仍作为开放题 → 原帖 Edit2 已给肯定解；第1问独立保留。

**本轮结论：**原帖 Edit2 已在 2021 年解决第3问：存在无限非共线 good 集。卡片应保留单位线段第1问而移出第3问的开放标记。

**证据与适用范围：**

- [原始题源与直接解答](https://mathoverflow.net/questions/381214/dense-sets-in-bbbr2-with-rational-distance) — 2021-01-14，Edit2 与 Wojowu 19:10 评论。原定义 S⊂R²\closure(X)；圆上稠密 S 的补集含无限闭 X，得到 Q3 正答。 访问层级：正文 Edit2、评论已访问。

**查重：**

- QX-P-000322（rev d7fe3a812162c2a6）：待定；仅索引候选；对方正文未取得。索引是整个平面稠密有理距离集，题面线索与本题 toy good 集相关；未取得当前全文，不能判重复。

**实际检索路径：**

- system1_search："Dense sets" "rational distance" "381214"；回执 group_01/receipts/academic_12.json。
- system1_search："good" "rationally distanced" "Hunter" circle；回执 group_01/receipts/academic_12.json。
- system2_search：site:github.com "rationally distanced"；回执 group_01/receipts/code_community_12.json。
- system2_search："good" "rationally distanced" (site:aixiv.online OR site:zenodo.org OR site:mathoverflow.net OR site:hexagonmath.org)；回执 group_01/receipts/code_community_12.json。

**待复核：**

- 如要可独立阅读的卡片，补写圆幂集有理弦长与密度的短验证。

#### QX-P-001446

**旧卡 → 变化：**负系数 Pell 即产生无穷解 → 必须排除平方 D 等退化；原主猜想不因此被反驳。

**本轮结论：**未检出三立方可解推出无穷四立方解的完整答案；原帖 Pell 路线及卡片说明漏了 D=−(a+b)c 必须为非平方数等条件，负号本身不足。

**证据与适用范围：**

- [原始题源](https://mathoverflow.net/questions/289554/if-a3b3c3-n-then-x3y3z3t3-n-in-infinitely-many-ways) — Tito Piezas III 2017，Part I 恒等式、Part II 与附问。原文把负系数作为关键条件；本轮代数检查指出平方 D 的退化遗漏。 访问层级：全文已访问。

**实际检索路径：**

- system1_search："289554" "cubes"；回执 group_01/receipts/academic_13.json。
- system1_search："three cubes" "four cubes" "infinitely" "Piezas"；回执 group_01/receipts/academic_13.json。
- system2_search：site:github.com "three cubes" "four cubes" infinite；回执 group_01/receipts/code_community_13.json。
- system2_search："289554" cubes (site:aixiv.online OR site:zenodo.org OR site:mathoverflow.net OR site:hexagonmath.org)；回执 group_01/receipts/code_community_13.json。

**待复核：**

- 对每个已知三立方可解 N 能否选到非平方 D 的表示仍需证明。
- 无穷参数是否给不同四元组，尤其 N=0 与退化 a,b,c 分支，尚需统一核。

本轮代数检查：a=1,b=3,c=−1 给 N=27 且 (a+b)c=−4。Pell 式为 (p−2q)(p+2q)=1，整数解只有 q=0、p=±1。故负号单独不足以产生无穷参数；本例不否定 N 的四立方主猜想。

<a id="q1431-proof"></a>

#### Q1431：本轮解析推导，主审解析二审通过

**来源性质。**以下是本轮根据题面给出的独立纸面推导，不是联网检索到的论文，不宣称优先权，也不是形式化验证。本次经主审独立核对归一化、角色分母、绝对收敛与 Chebyshev 整系数步骤通过；仍保守记录为“完整证明/反例声明待核”，未外部审稿、未形式化。

设 \(\Lambda\subseteq\mathbb Z^n\) 满秩，\(d=[\mathbb Z^n:\Lambda]\ge1\)。原题要求

\[
S(\Lambda)=\sum_{k\in\Lambda}\prod_{j=1}^n\frac1{1+k_j^2}
=\frac{\pi^n}{d\,\sinh^n\pi}\,
P\!\left(\cosh\frac{\pi}{d}\right),
\qquad P\in\mathbb Z[x].
\]

取有限角色群
\[
H=\Lambda^*/\mathbb Z^n,\qquad |H|=d.
\]
因为 \(\mathbb Z^n/\Lambda\) 的阶为 \(d\)，每个角色的各坐标都可取为
\(\chi_j=r_j(\chi)/d\)，其中 \(r_j(\chi)\in\{0,\ldots,d-1\}\)。
角色正交给出
\[
\mathbf1_\Lambda(k)=\frac1d\sum_{\chi\in H}
e^{2\pi i\langle\chi,k\rangle}.
\]
全格上乘积级数绝对收敛，因此可交换有限角色和及各坐标求和：
\[
S(\Lambda)=\frac1d\sum_{\chi\in H}\prod_{j=1}^n
F\!\left(\frac{r_j(\chi)}d\right),
\qquad
F(t)=\sum_{m\in\mathbb Z}\frac{e^{2\pi imt}}{1+m^2}.
\]

对 \(0\le t\le1\)，一维 Fourier 级数恒等式为
\[
F(t)=\frac{\pi\cosh(\pi(1-2t))}{\sinh\pi}.
\]
这个恒等式也可不依赖外部表格验证：直接积分右侧在 \([0,1]\) 的第 \(m\) 个 Fourier 系数，得到 \(1/(1+m^2)\)；系数绝对可和，周期端点值一致，故等式成立。

令 \(x=\cosh(\pi/d)\)。由第一类 Chebyshev 多项式
\(T_\ell(\cosh u)=\cosh(\ell u)\)、\(T_\ell\in\mathbb Z[x]\)，以及 cosh 的偶性，
\[
F(r/d)=\frac{\pi}{\sinh\pi}\,
T_{|d-2r|}(x).
\]
于是直接得到整数多项式
\[
\boxed{P(x)=\sum_{\chi\in H}\prod_{j=1}^n
T_{|d-2r_j(\chi)|}(x)\in\mathbb Z[x].}
\]
代回即为题目要求的等式，前因子准确为 \(1/d\)，没有额外 \(d^n\)。

**边界自检。**当 \(d=1\) 时只有平凡角色，得到 \(P=x^n\)，从而
\(S(\mathbb Z^n)=(\pi\coth\pi)^n\)。当 \(n=1,d=2\) 时，
\(P=T_2+T_0=2x^2\)，得到
\(\frac\pi2\coth(\pi/2)\)，与 \(\sum_m(1+4m^2)^{-1}\) 相符。
这里是符号核对，没有运行数值或 Lean。

**已完成的解析二审重点。**角色分母只需整除 \(d\)、Fourier 恒等式的 \(2\pi\) 归一化、满秩条件、绝对收敛换和，以及原题是否另有未写出的 \(P\) 次数或系数符号限制。当前题面没有这些额外限制。


---

### QX-NEW-01 第2组：突破点、实际检索路径与复核清单

检索日：2026-11-26（按本任务指定 Asia/Shanghai 日期登记）。本文件只收影响状态、题面、出处或查重的新发现；25题完整五路记录见 `QX-NEW-01_逐题回传.jsonl`。未进行线上改卡、合并或发帖。

证据分层：原刊/作者稿、预印本、社区推导、公开AI声明分别记录；摘要和受阻入口明确标注。没有零命中推开放结论，也没有外部代码或形式化系统独立通过的声明。1472的本轮自写有限DP另附可手核割集证书。

#### 优先复核项

- **1471：新完整证明声明。** 2026-11-23 Ottem arXiv:2611.31152v1 给出整系数对角线问题构造；原卡系数及定义需先修。原稿5页已读，依赖与作者计算未独立核实。
- **1472：现全称式有明确反例。** 4×4二维马图不存在Hamilton路径，割集证书可直接复核；高维原意须另列。
- **1467、1454、1463：原卡将缺条件/已可直接给式/已证明的子问继续标为未解。** 分别补多因子条件、分布及期望积分、临界轨道发散结论。
- **1449、1462、1464、1466、1473：对象、引用、归一化、操作规则或λ参数发生实质错配。** 下文给旧→新、适用范围和直接来源。

#### QX-P-001447（版本 `df445ef09a7aa8bf`）

原题与 ±C 平移族/全刚体旋转族的比较一致。核得 Bárány–Matoušek 原文只是给平移族密度的统一非平凡上界，并未证明其等于旋转装填密度；原卡将 Imre 误作第三作者。本轮未取得主比较问题的可验证完整解答。

##### 旧卡 → 变化

- **出处作者**：Barány–Imre–Matoušek 2007 → Imre Bárány 与 Jiří Matoušek（两位作者）
- **已知进展**：论文被概括为本题最密性开放问题依据 → 补列 Theorem1.1 的 ±C 平移装填密度上界，并明确不解决旋转比较。

##### 证据、定位与范围

- [已刊论文作者稿](https://www.renyi.hu/~barany/cikkek/kuper.pdf)，**作者预印本PDF p.2，Theorem 1.1；首页作者**。访问程度：全文已取得、关键定理已读。只许C及−C平移的锥装填密度有统一小于1的上界；作者是Imre Bárány、Jiří Matoušek。 适用性：适用于±C平移，不涵盖任意转动族最密性。
- [社区原题](https://mathoverflow.net/questions/171803/packing-space-by-cones-translates-best?noredirect=1)，**题面与Kuperberg评论**。访问程度：全文/评论已取得。询问圆锥及其点反射的平移是否达到所有全等拷贝的最密装填。 适用性：与本题量词对照见 claim

##### 实际检索路径

- 学术 / `system2_search_query`：`"Packing cones and their negatives" densest rotations`（group_02/receipts/s02.json，条目0，2026-11-26）。
- 学术 / `system2_search_query`：`"right circular cone" packing density rotations conjecture`（group_02/receipts/s02.json，条目1，2026-11-26）。
- GitHub/代码 / `system2_search_query`：`site:github.com "cone" "packing" "Kuperberg"`（group_02/receipts/s04.json，条目0，2026-11-26）。
- 公开AI/社区 / `system2_search_query`：`("Packing cones" OR "171803") (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR site:eulersolve.org OR site:proofforum.org)`（group_02/receipts/s04.json，条目1，2026-11-26）。
- 查重：全库2469条索引正则 `cone|圆锥`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 沿2007论文后续引用查特定高径比/一般旋转装填比较；未穷尽引文网络。

#### QX-P-001449（版本 `3b78b2e11987398a`）

原答的虚自由分解属于另建的辅助群H，不能归给原卡四生成元七关系群G。作者明言仍不知G是否无挠甚至非平凡；其因式分解只排除指定消去模型的无挠零因子路线。与000353为特定例子对一般猜想，不能合并。

##### 旧卡 → 变化

- **已知结果对象**：该表现为虚自由群 → 明确为用消去关系另定义的H；G本身是否无挠/非平凡仍未定。
- **题名**：2-生成4-符号7-关系 → 依显式表现为4个生成符号、7条关系；如声称2生成需另给等价变换。

##### 证据、定位与范围

- [社区推导](https://mathoverflow.net/questions/513707/checking-one-group-for-torsion)，**Henrik Rüping答案；辅助H定义、t与AB分解**。访问程度：全文及关键等式已读。H≅⟨t,w4,w5,w6,w7,w12|t³⟩；原答明确未判定G。 适用性：只针对给出的消去路线；最后关系的w12修正是前提。
- [公开完整解声明线索](https://www.academia.edu/181666134/Kaplanskys_conjectures_fail_for_torsion_free_hyperbolic_groups_in_positive_characteristic)，**搜索结果题名/摘要**。访问程度：仅检索摘要，原证明未核。出现广义无挠群代数零因子新声明；尚不能用于这张具体G题卡。 适用性：相关更广问题，非本题G的直接证明。

##### 查重关系

- QX-P-001449 `3b78b2e11987398a` ↔ QX-P-000353 `df7c1799f3b293c8`：**相关但不等价**。指定对子两卡全文已读；000353是所有无挠群/域的Kaplansky零因子猜想，001449只问特定表现群及给定路线。

##### 实际检索路径

- 学术 / `system1_search_query`：`"513707" "group"`（group_02/receipts/s03.json，条目3，2026-11-26）。
- 学术 / `system1_search_query`：`"Maximka123" "torsion" group relations Rüping`（group_02/receipts/s05.json，条目0，2026-11-26）。
- GitHub/代码 / `system2_search_query`：`site:github.com "torsion" "513707"`（group_02/receipts/s06.json，条目0，2026-11-26）。
- 公开AI/社区 / `system2_search_query`：`"513707" (site:zenodo.org OR site:aixiv.org OR site:eulersolve.org OR site:proofforum.org)`（group_02/receipts/s06.json，条目1，2026-11-26）。
- 查重：全库2469条索引正则 `Kaplansky|卡普兰斯基|零因子`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 复核原帖w1/w12笔误与H→G映射每条关系；未执行群计算软件。
- 检索到2026广义Kaplansky零因子声明，但本轮未取得并核对其完整证明，也未建立对这个G的适用性；不得借此改G结论。

#### QX-P-001453（版本 `782084ba8b635583`）

原帖确问去掉可度量性后的l.s.c.非空闭凸值映射不动点。Ky Fan型u.s.c.定理不能替代。检索命中若干较强假设/可度量情形，未取得满足现量词的完整证明或反例；Xian Wu原论文未取得。

##### 旧卡 → 变化

- **定义边界**：闭凸值而未明写非空 → 补X≠∅、F(x)非空，维持l.s.c.而非u.s.c.。

##### 证据、定位与范围

- [社区原题](https://mathoverflow.net/questions/61309/fixed-point-theorem-for-convex-closed-multivalued-mapping)，**题面与Xian Wu线索**。访问程度：全文已取得。问题主轴是非可度量局部凸Hausdorff背景中的l.s.c.闭凸值自映射。 适用性：与本题量词对照见 claim

##### 实际检索路径

- 学术 / `system1_search_query`：`"fixed point" "lower semicontinuous" "nonmetrizable" compact convex`（group_02/receipts/s07.json，条目0，2026-11-26）。
- 学术 / `system1_search_query`：`"61309" fixed points lower semicontinuous maps`（group_02/receipts/s07.json，条目1，2026-11-26）。
- GitHub/代码 / `system2_search_query`：`site:github.com "lower semicontinuous" "fixed point" nonmetrizable`（group_02/receipts/s08.json，条目0，2026-11-26）。
- 公开AI/社区 / `system2_search_query`：`"lower semicontinuous" "nonmetrizable" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org)`（group_02/receipts/s08.json，条目1，2026-11-26）。
- 查重：全库2469条索引正则 `fixed point|不动点`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 取得Xian Wu A new fixed point theorem and its application原稿，核其可度量性用途及后续引用。

#### QX-P-001454（版本 `1a00f432636eb450`）

期望子问已有精确积分式；一般CDF可由次序统计量联合分布直接积分得到，不能因未化简为初等闭式而称一般公式未解。一般F可能含原子，PDF甚至不存在。需将未指定“闭式”标准的开放表述撤回或改为具体计算要求。

##### 旧卡 → 变化

- **人话版与状态**：一般公式仍未解决；一般CDF开放 → 移除该断言；给精确积分式，并明确若要求某类闭式须另行定义。
- **支撑/可积性**：∫₀∞期望公式用于一般F → 限定非负样本；含负值时用分位数期望并声明可积性。

##### 证据、定位与范围

- [社区原始推导](https://mathoverflow.net/questions/15346/distribution-of-the-sum-of-the-m-smallest-values-in-a-sample-of-size-n)，**Zare答案，2010-02-15**。访问程度：全文与公式已读。非负时E S_m=∫₀∞Σ_{k=0}^{m−1}(m−k)binom(n,k)F(x)^k(1−F(x))^{n−k}dx。 适用性：与本题量词对照见 claim
- [作者教学原稿](https://healy.econ.ohio-state.edu/kcb/Ma103/Notes/Lecture15.pdf)，**KC Border Lecture15 §15.3.1、§15.4.1，pp.1–2**。访问程度：全文已取得、关键密度命题已读。联合次序密度为n!∏f(x_i)于有序区域；为CDF直接积分与分位数推导提供标准基础。 适用性：与本题量词对照见 claim

**附加论证：** 令Q(u)=inf{x:F(x)≥u}。F_{S_m}(t)=n!/(n−m)! ∫_{0<u1<…<um<1} 1{ΣQ(ui)≤t}(1−um)^(n−m) du1…dum，任意F成立。若可积，E S_m=Σ_{i=1}^m n!/[(i−1)!(n−i)!]∫₀¹Q(u)u^(i−1)(1−u)^(n−i)du。绝对连续时可换成x域密度积分。此为本轮依据均匀次序统计量作的直接推导，未称形式化验证。

##### 实际检索路径

- 学术 / `system1_search_query`：`"sum" "smallest order statistics" distribution general density`（group_02/receipts/s07.json，条目2，2026-11-26）。
- 学术 / `system1_search_query`：`"15346" "order statistics"`（group_02/receipts/s07.json，条目3，2026-11-26）。
- GitHub/代码 / `system2_search_query`：`site:github.com "smallest order statistics" sum`（group_02/receipts/s08.json，条目2，2026-11-26）。
- 公开AI/社区 / `system2_search_query`：`"sum" "smallest order statistics" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR site:eulersolve.org OR site:proofforum.org)`（group_02/receipts/s08.json，条目3，2026-11-26）。
- 查重：全库2469条索引正则 `order statistic|次序统计`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 若保留研究题，指定F家族、闭式类型或有效算法/复杂度目标；本轮不把任意积分再化简设为开放猜想。

#### QX-P-001455（版本 `bd90f553cd167f6d`）

已核原题，并取得Smith综述对Hansen固定维数分量同伦分类的明确结论，部分子问是经典已知结果。卡把度0称恒等分量错误，恒等映射度1。跨维整体同胚问题与各分量同伦类型必须分别登记。

##### 旧卡 → 变化

- **边界**：k=0恒等分量 → 恒等分量k=1；k=0为零伦分量。
- **题名**：C(S^m,S^n)各自之间 → C(S^m,S^m)与C(S^n,S^n)；固定n分量同伦分类单独列出。

##### 证据、定位与范围

- [社区原题](https://mathoverflow.net/questions/8729/are-the-csn-sns-homeomorphic)，**原问及Igor Belegradek答案、Reid Barton评论**。访问程度：全文已取得。整体空间与单一恒等分量不能混同。 适用性：与本题量词对照见 claim
- [作者综述预印本](https://arxiv.org/pdf/1009.0804)，**Samuel Bruce Smith, The homotopy theory of function spaces: a survey；v2，§2.1.1 PDF p.5**。访问程度：关键分类及参考文献已读。偶数球分量由Whitehead积相差正负决定；奇数球n=1,3,7所有分量同伦等价，其他奇数维度按度奇偶分两类。 适用性：仅同维非基点映射空间的同伦类型。

##### 实际检索路径

- 学术 / `system1_search_query`：`"C(S^n,S^n)" homeomorphic Hansen Lupton Smith components`（group_02/receipts/s09.json，条目1，2026-11-26）。
- 学术 / `system1_search_query`：`"8729" "homeomorphic"`（group_02/receipts/s09.json，条目2，2026-11-26）。
- GitHub/代码 / `system2_search_query`：`site:github.com "sphere" "Hansen" "homotopy" components`（group_02/receipts/s11.json，条目0，2026-11-26）。
- 公开AI/社区 / `system2_search_query`：`"self maps spheres" "components" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR site:eulersolve.org)`（group_02/receipts/s11.json，条目1，2026-11-26）。
- 查重：全库2469条索引正则 `C\(S|self.map|函数空间|球面.*同胚`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 取得Hansen1974原刊并核所有分量分类假设；若用无限维流形同伦⇒同胚需另核流形类型和分类定理。

#### QX-P-001458（版本 `4045a00f0b025063`）

已取得Counting Groups: Gnus原稿，§10明确使用group-perfect并把gnu(n)=n、n>1的不存在性列为Conjecture10.1，平方自由n属于已知group-deficient分支。未取得一般n新解决。

##### 旧卡 → 变化

- **术语待核**：group-perfect名称待原文核实 → Conway等Counting Groups: Gnus §10（PDF p.11）已明确定义，关联Conjecture10.1。

##### 证据、定位与范围

- [作者原稿](https://www.math.auckland.ac.nz/~obrien/research/gnu.pdf)，**§10，Conjecture10.1，PDF p.11**。访问程度：全文已取得、§10已读。将gnu(n)=n称group-perfect；猜想没有n>1满足，平方自由n>1已为group-deficient。 适用性：与本题量词对照见 claim
- [社区原题](https://mathoverflow.net/questions/46444/natural-numbers-n-which-satisfy-gnun-n?r=31)，**问题正文**。访问程度：全文已取得。原问排除n=1，问组数恰等于阶数。 适用性：与本题量词对照见 claim

##### 实际检索路径

- 学术 / `system1_search_query`：`"Counting Groups: Gnus" "Conjecture 10.1"`（group_02/receipts/s12.json，条目2，2026-11-26）。
- 学术 / `system1_search_query`：`"gnu(n)=n" "group"`（group_02/receipts/s12.json，条目3，2026-11-26）。
- GitHub/代码 / `system2_search_query`：`site:github.com "group-perfect" gnu`（group_02/receipts/s13.json，条目2，2026-11-26）。
- 公开AI/社区 / `system2_search_query`：`"group-perfect" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR site:proofforum.org)`（group_02/receipts/s13.json，条目3，2026-11-26）。
- 查重：全库2469条索引正则 `gnu\(|群完全|group.perfect`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 继续核Conjecture10.1后续引文、计算范围和原文正式期刊版本；本轮未重跑gnu计数。

#### QX-P-001459（版本 `81ca4420f49ce43d`）

已有2008文献声称否定不加regular限定的星紧致Gδ对角线可度量性；2011 Song全文例子明确不正则且可数，不能反驳本卡正则空间的基数界。加强对角线条件的2014定理也不直接覆盖。

##### 旧卡 → 变化

- **文献范围**：可度量性问与基数问笼统并列 → 标注Yang–Shi2008负答的分离公理待全文核；Song2011反例非regular且可数，不适用于主问。

##### 证据、定位与范围

- [社区原题](https://mathoverflow.net/questions/120922/an-open-problem-on-general-topology)，**正文及regular/Tychonoff限定**。访问程度：全文已取得。本卡保留分离公理并问不超过连续统的基数。 适用性：与本题量词对照见 claim
- [已刊论文](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/an-answer-to-van-mills-question/C96F1A96227340F99F507EC5A60D6F5C)，**Yang–Shi2008，摘要，DOI10.1017/S000497270800066X**。访问程度：仅摘要，PDF未取得。摘要只表明一般星紧致Gδ对角线可度量性有负答。 适用性：不能据摘要补上regular。
- [已刊论文](https://www.vesnik.math.rs/vol/mv11105.pdf)，**Song2011 Example2.1与Remark2.2，p.42**。访问程度：全文已取得、例与remark已读。所给Hausdorff星紧致非可度量例可数且明确非正则。 适用性：不反驳regular主问，也不反驳|X|≤c。

##### 实际检索路径

- 学术 / `system1_search_query`：`"star compact" "G_delta" cardinality regular`（group_02/receipts/s14.json，条目0，2026-11-26）。
- 学术 / `system1_search_query`：`"star-compact" "diagonal" metrizable problem 4.8`（group_02/receipts/s14.json，条目1，2026-11-26）。
- GitHub/代码 / `system2_search_query`：`site:github.com "star-compact" "diagonal"`（group_02/receipts/s15.json，条目0，2026-11-26）。
- 公开AI/社区 / `system2_search_query`：`"star compact" "diagonal" (site:zenodo.org OR site:aixiv.org OR site:mathoverflow.net OR site:proofforum.org)`（group_02/receipts/s15.json，条目1，2026-11-26）。
- 查重：全库2469条索引正则 `star.compact|星紧致|star compact`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 取得Yang–Shi2008 pp353–355全文核其正则性与基数；目前Cambridge只回摘要。

#### QX-P-001462（版本 `f0c38084455e87f2`）

Rassias素数线性配对猜想及10^9范围的社区计算已核（未重跑）。原卡引用1606.03845作为相关条件进展不适用：该文是一个素数加两个孤立素数的三元Goldbach问题，不是∀p∃q使(p−1)q−1为素数。

##### 旧卡 → 变化

- **相关进展引用**：arXiv:1606.03845可能为本题条件成果 → 删除作为本题支持；可列命中不适用，明确三元Goldbach不同量词。
- **计算范围**：已验证至10^9 → 标为Peter社区报告，q≤1709；本轮未独立重跑。

##### 证据、定位与范围

- [社区计算声明](https://math.stackexchange.com/questions/1464339/up-to-which-value-is-rassias-conjecture-verified?r=31)，**原问及Peter计算评论/答案**。访问程度：全文已取得、未重跑。报告有限p范围和q上界，不能用作一般证明。 适用性：与本题量词对照见 claim
- [预印本](https://arxiv.org/abs/1606.03845)，**Maier–Rassias，v1 2016-06-13，题名与摘要**。访问程度：摘要和版本历史已核；未逐页全文。题目是三元Goldbach表示含孤立素数，在GRH下的充分大奇数结果。 适用性：与本题线性素数配对不同。

##### 实际检索路径

- 学术 / `system1_search_query`：`Rassias conjecture prime "(p-1)q-1" progress`（group_02/receipts/s16.json，条目0，2026-11-26）。
- 学术 / `system1_search_query`：`Rassias Maier Rassias "1606.03845" conjecture primes`（group_02/receipts/s16.json，条目1，2026-11-26）。
- GitHub/代码 / `system2_search_query`：`"Rassias conjecture" site:github.com`（group_02/receipts/s17.json，条目2，2026-11-26）。
- 公开AI/社区 / `system2_search_query`：`"Rassias conjecture" (site:zenodo.org OR site:aixiv.org OR site:eulersolve.org OR site:proofforum.org OR site:math.stackexchange.com)`（group_02/receipts/s17.json，条目3，2026-11-26）。
- 查重：全库2469条索引正则 `Rassias`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 取得最初Rassias出处与2007相关刊文；doiserbia PDF本轮超时。

#### QX-P-001463（版本 `00fd0b510f2802e7`）

端点行为已由原帖第三答证明u_n(δ)严格递增趋+∞，不应仍写成开放子问。阈值的数值与LambertW递推是另一个子问；OEIS编号的数值匹配未构成所写嵌套乘积恒等式证明。

##### 旧卡 → 变化

- **开放子问**：u_n(δ)是收敛、有界或发散仍未知 → 拆出已证明u_n(δ)→+∞；保留δ表达式/更强界待核。
- **OEIS匹配**：δ=ln(嵌套乘积)作为已知式 → 降为社区数值识别线索；A278812本轮403，等式未核。

##### 证据、定位与范围

- [社区完整推导](https://math.stackexchange.com/questions/3831702/u-n1-fraceu-nn1)，**dan_fulea第三答，Lemma2、Result与Proof；SimplyBeautifulArt数值答案**。访问程度：全文及端点论证已读。c_n严格递增到δ，δ>c_n令临界轨道严格递增；有界增长轨道会由递推趋0产生矛盾，故发散。 适用性：与本题量词对照见 claim
- [序列线索](https://oeis.org/A278812)，**OEIS入口**。访问程度：403不可达。本轮未验证定义，更没有验证其与δ相等。 适用性：与本题量词对照见 claim

**附加论证：** 若某项u_{n+1}≤u_n，则下一步严格下降，此后单调下降且极限由递推为0。反之从未下降的正轨道严格递增，若有界则递推右侧趋0而矛盾。收敛到0等价于某有限步严格下降，故其初值集合由有限迭代连续性为开集；边界δ不在该集合，因而u_n(δ)→+∞。这是普通数学复核，非形式化工具验证。

##### 实际检索路径

- 学术 / `system1_search_query`：`"3831702" "delta" sequence`（group_02/receipts/s16.json，条目2，2026-11-26）。
- 学术 / `system1_search_query`：`"0.3132776395465558" recurrence exponential`（group_02/receipts/s16.json，条目3，2026-11-26）。
- GitHub/代码 / `system2_search_query`：`site:github.com "A278812"`（group_02/receipts/s18.json，条目2，2026-11-26）。
- 公开AI/社区 / `system2_search_query`：`"A278812" (site:math.stackexchange.com OR site:zenodo.org OR site:aixiv.org OR site:eulersolve.org OR site:proofforum.org)`（group_02/receipts/s18.json，条目3，2026-11-26）。
- 查重：全库2469条索引正则 `bifurcation.*threshold|递推.*阈值|u_.*e`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 审定LambertW界的下标与渐近误差；取得A278812原记录、原始定义和真正等价证明。

#### QX-P-001464（版本 `c0bf794b963138e8`）

Γ归一化在原卡叙述中混淆：A=√πV^{1/2}，1.48–1.55是A的原帖界而非归一化V的界。且||A||²才等于A*A最大特征值。2026检索命中的Bochner–Lebesgue映射论文与核L2范数代码不等于精确Lp算子范数解。

##### 旧卡 → 变化

- **人话版数值范围**：V^{1/2}核为1/√(x−y)、范数1.48至1.55 → 归一化核为1/(√π√(x−y))，相应界除以√π。
- **形式化归约**：||Vhalf||等价A*A最大特征值 → ||Vhalf||=√(λmax(A*A)/π)，避免省略平方根与π。

##### 证据、定位与范围

- [社区原题](https://math.stackexchange.com/questions/5091826/riemann-liouville-fractional-integral-operator-norm-and-related-singular-value-p?r=31)，**V^s与A定义、min-max说明、1.48–1.55**。访问程度：全文已取得。原作者明说A是归一化Vhalf去掉常数；A最大奇异值是A*A最大特征值平方根。 适用性：与本题量词对照见 claim
- [已刊论文线索](https://link.springer.com/article/10.1007/s13540-026-00480-2)，**The Riemann-Liouville fractional integral in Bochner-Lebesgue spaces IV，2026**。访问程度：本轮仅搜索摘要。命中映射/正则性系列，不据摘要认定给出了本题精确范数。 适用性：全文定理尚未核。

##### 实际检索路径

- 学术 / `system1_search_query`：`Riemann Liouville fractional integral "operator norm" Lp exact 2026`（group_02/receipts/s19.json，条目0，2026-11-26）。
- 学术 / `system1_search_query`：`"5091826" fractional integral norm`（group_02/receipts/s19.json，条目1，2026-11-26）。
- GitHub/代码 / `system2_search_query`：`site:github.com "Riemann-Liouville" "norm"`（group_02/receipts/s20.json，条目1，2026-11-26）。
- 公开AI/社区 / `system2_search_query`：`"Riemann Liouville" "operator norm" (site:zenodo.org OR site:aixiv.org OR site:eulersolve.org OR site:math.stackexchange.com OR site:proofforum.org)`（group_02/receipts/s20.json，条目2，2026-11-26）。
- 查重：全库2469条索引正则 `Riemann.Liouville|分数积分`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 追踪Carvalho-Neto–Fehlberg系列中范数定理，并严格区分已证明界与原帖声称的数值界。

#### QX-P-001465（版本 `6f3e0125401e89c3`）

原猜想仍无本轮可验证一般证明；旧卡复制原帖算术笔误，正确改写是q+3=3p1+p2。Chen定理的半素数没有指定因子3，不能推出该式。10^10计算仍仅为Peter社区声明。

##### 旧卡 → 变化

- **已知进展代数式**：q−3为素数+3p1 → q+3为p2+3p1；限定半素数因子3仍是额外限制。
- **计算证据**：11≤q≤10^10、p1≤797 → 保留为Peter 2022-11-09报告，明确未独立重跑。

##### 证据、定位与范围

- [社区原题/计算报告](https://math.stackexchange.com/questions/4571438/comans-last-conjecture-stating-that-every-prime-q-geq-11-can-be-written-as)，**题面、P.S.与Peter2022-11-09评论**。访问程度：全文及评论已读。P.S.确有q−3笔误；主式明确q=3(p1−1)+p2，有限验证报告10^10、797。 适用性：与本题量词对照见 claim

##### 实际检索路径

- 学术 / `system1_search_query`：`"Coman" "last conjecture" primes`（group_02/receipts/s19.json，条目2，2026-11-26）。
- 学术 / `system1_search_query`：`"q" "3(p" "Coman" primes`（group_02/receipts/s19.json，条目3，2026-11-26）。
- GitHub/代码 / `system2_search_query`：`site:github.com "Coman" "conjecture" primes`（group_02/receipts/s20.json，条目3，2026-11-26）。
- 公开AI/社区 / `system1_search_query`：`"Coman" "last conjecture" AI discussion proof`（group_02/receipts/s21.json，条目2，2026-11-26）。
- 查重：全库2469条索引正则 `Coman`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 取得Coman原书p81核原始猜想；不把未固定p1的量词改成某一个p1对所有q有效。

#### QX-P-001466（版本 `793c7c0d0f3ef1a6`）

已取得2019官方题目与解答。每步是在左端或右端添一个比特；旧卡人话版同时两端各添一位改变了整个生成过程。官方(a)还给出明确下界底数φ与上界底数ψ（x³−x²−x−1唯一实根），不是只有笼统1.6/1.9。

##### 旧卡 → 变化

- **人话规则**：左右两端各添一个0/1 → 分别允许在左端或右端添一个0/1，长度每次增加1。
- **已知指数界**：1.6<λ1,λ2<1.9 → 可补φ=(1+√5)/2和ψ为x³−x²−x−1唯一实根；不把有限nth根当极限。
- **OEIS状态**：序列不在OEIS → 限为2020评论的历史观察，本轮未验证当前OEIS收录状态。

##### 证据、定位与范围

- [竞赛原题](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf)，**官方2019 SessionB，B4，p.2**。访问程度：正文已取得。归纳规则为左右任选一端添一位，(b)在2019明示未知。 适用性：与本题量词对照见 claim
- [官方证明](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-solutions_1.pdf)，**官方解答B4，pp.10–12**。访问程度：PDF全文与(a)证明已读。给Fibonacci型下界φ、避免RRLL动作串上界ψ。 适用性：与本题量词对照见 claim
- [社区原题/代码线索](https://math.stackexchange.com/questions/3706460/reference-request-the-number-of-binary-string-with-some-special-condition-ope)，**题面与joriki数值评论**。访问程度：正文评论已取得；链接Java代码未执行。有限序列数值只是实验。 适用性：与本题量词对照见 claim

##### 实际检索路径

- 学术 / `system1_search_query`：`"Simon Marais" "2019" "B4" binary`（group_02/receipts/s21.json，条目0，2026-11-26）。
- 学术 / `system1_search_query`：`"1,2,3,5,9,16,29,52,94" binary`（group_02/receipts/s21.json，条目1，2026-11-26）。
- GitHub/代码 / `system2_search_query`：`"binary strings" "Simon Marais" github`（group_02/receipts/s22.json，条目0，2026-11-26）。
- 公开AI/社区 / `system2_search_query`：`"Simon Marais" "B4" "AI" 2019`（group_02/receipts/s22.json，条目1，2026-11-26）。
- 查重：全库2469条索引正则 `binary string|二进串`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 沿官方B4(b)和精确数列查后续论文/序列登记；本轮未重跑外部Java枚举。

#### QX-P-001467（版本 `767346bf3d37a347`）

形式化漏掉j−k≥2，因此按现式每个m≥3都取j=m!,k=m!−1成立，稀疏解集断言错误。修正后对应Surányi两阶乘乘积问题；Habsieger2019 Theorem4已给极强排除界，旧卡未收。

##### 旧卡 → 变化

- **形式化**：j>k>1 → 补j−k≥2；并明确是否排除C=B+1产生的m=x!−1平凡族。
- **边界**：j−k=0为单因子 → 改j−k=1为单因子。
- **已知结果**：无其它例子已知，仅OEIS联系 → 补Habsieger2019 Theorem4的B≥10^3000与明确变量对应，不能误写m≥10^3000。

##### 证据、定位与范围

- [社区原题](https://math.stackexchange.com/questions/2148523/find-all-numbers-whose-factorial-equals-the-product-of-more-than-1-consecutive)，**题名、3答案与OEIS关联**。访问程度：全文已取得。原问greater-than-number与回答一般阶乘乘积的范围混杂。 适用性：与本题量词对照见 claim
- [已刊论文预印本](https://arxiv.org/pdf/1903.08370)，**Habsieger v1 2019-03-20，Theorem4，PDF p.3（期刊对应Theorem1.4）**。访问程度：关键定义、Theorems1–4及适用范围已读。非平凡A!B!=C!且(A,B,C)≠(6,7,10)⇒B≥10^3000并有显式C−B上界。 适用性：先排序A=min(m,k),B=max(m,k)，且需C≥B+2。
- [序列数据库](https://oeis.org/A109095)，**Comments与参考文献，2023-01-19注**。访问程度：全文已读、PARI代码未重跑。A109095收的是C，而非m；提供Surányi名称与Habsieger线索。 适用性：与本题量词对照见 claim

##### 实际检索路径

- 学术 / `system2_search_query`：`"factorials" "A109095" equation`（group_02/receipts/s22.json，条目2，2026-11-26）。
- 学术 / `system2_search_query`：`"m!" "j!/k!" consecutive integers factorial`（group_02/receipts/s22.json，条目3，2026-11-26）。
- GitHub/代码 / `system1_search_query`：`site:github.com "factorial" "A109095"`（group_02/receipts/s23.json，条目1，2026-11-26）。
- 公开AI/社区 / `system1_search_query`：`"factorial equation" "A!B!" AI proof`（group_02/receipts/s23.json，条目2，2026-11-26）。
- 查重：全库2469条索引正则 `factorial|阶乘`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 原帖greater than m子情形与现一般式仍需编辑选择；已列两版本不可混写。
- Habsieger原文方法/§5计算没有独立重跑；后续2019—2026引文尚未穷尽。

#### QX-P-001468（版本 `98d1be205e208076`）

原帖明确加p≡2 mod3，现正式题面删掉该限制，成为较弱的不同版本；应拆问。mercio收敛级数是社区启发式，并未给卡中所写精细概率模型推导。三个指定对子全文已核均不等价；新000738经官网全文补核也是primorial问题，属相关但不等价；正常HTTP恢复了此前受阻入口。

##### 旧卡 → 变化

- **题面范围**：省略同余条件 → 明确原帖是p≡2(mod3)；无此限制另作变体。
- **概率结论**：概率~1/[p(logp)^2]等归因mercio → 仅准确记mercio给收敛级数的启发判断；删无出处的细化概率公式，不按其改有限/无限结论。

##### 证据、定位与范围

- [社区原题](https://math.stackexchange.com/questions/403786/are-there-infinitely-many-primes-p-k-such-that-p-k-1p-k-is-a-also-prime?r=31)，**题面同余条件；mercio、Aguirre评论**。访问程度：全文/可见评论已取得。原帖有p≡2mod3；收敛级数只是一条启发评论，Aguirre只证因子大于p。 适用性：与本题量词对照见 claim
- [问题原始公开数据库](https://www.erdosproblems.com/forum/thread/779)，**Erdős779原题描述**。访问程度：搜索全文片段已取得，直接打开受限。该题用P=首n素数乘积，寻另一个素数p使P+p素数；不等于(p−1)!+p。 适用性：只有用于排除结构混淆；该次访问未取得卡全文；后续已补取000738现版全文，见查重记录。
- [新查重候选现版题卡](https://www.qunxingmath.org/p/QX-P-000738/)，**题面、形式化、人话版及页脚card_rev38dc6dfbd7c18427**。访问程度：正常HTTP取得完整HTML并解析可见全文；此前搜索工具入口受阻已恢复。∀n>1存在区间素数p使primorial P+p为素数，与阶乘(p−1)!+p无穷素值不是同题。 适用性：只用于查重，不采纳卡中旧状态为本题文献结论。

##### 查重关系

- QX-P-001468 `98d1be205e208076` ↔ QX-P-000429 `de18bdf5a9f0707e`：**相关但不等价**。指定两卡全文已读；000429是Ω(p−2)奇偶的素数问题，无阶乘表达式。
- QX-P-001468 `98d1be205e208076` ↔ QX-P-000863 `e756fc8b96c6c4ec`：**相关但不等价**。指定两卡全文已读；000863是幸运素数无穷性，不是固定阶乘+同一素数。
- QX-P-001468 `98d1be205e208076` ↔ QX-P-001707 `223391beabc965fc`：**相关但不等价**。指定两卡全文已读；Wilson素数条件p² | (p−1)!+1，与(p−1)!+p素性不同。
- QX-P-001468 `98d1be205e208076` ↔ QX-P-000738 `38dc6dfbd7c18427`：**相关但不等价**。新线索已补取官网现版全文，页脚card_rev与索引38dc6dfbd7c18427一致。000738是对每个n>1、P为前n素数积，存在p_n<p<P使P+p素数；本题是对同一素数p检查(p−1)!+p并问无穷性，变量/乘积/量词均不同。

##### 实际检索路径

- 学术 / `system1_search_query`：`"Deaconescu" "779" factorial prime`（group_02/receipts/s23.json，条目3，2026-11-26）。
- 学术 / `system1_search_query`：`"779" "Erdős" "Deaconescu"`（group_02/receipts/s24.json，条目0，2026-11-26）。
- GitHub/代码 / `system1_search_query`：`site:github.com "(p-1)!+p"`（group_02/receipts/s24.json，条目2，2026-11-26）。
- 公开AI/社区 / `system1_search_query`：`"factorial" "Deaconescu" "AI"`（group_02/receipts/s24.json，条目3，2026-11-26）。
- 查重：全库2469条索引正则 `factorial|Wilson|幸运素数|Omega`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 针对固定阶乘偏移的筛因子修正与独立文献作进一步核查；任何随机模型都不是原题证明。

#### QX-P-001469（版本 `772cfab02d631b92`）

四个带符号整数立方主问未获可验证完整解；原卡缺少经典非±4模9分支的文献层次。公开AI汇编出现“Linnik已解”元数据但同页承认无原证明且混用七正立方；不能据此改已解。新001246经正常HTTP取得现版全文及匹配页脚版本，确认主问同题；只报告，不合并。

##### 旧卡 → 变化

- **已知成果层次**：只列有限计算和MO怀疑 → 补非±4mod9的经典四立方分支线索，保持与所有整数主问的差别。
- **状态证据**：无相关已解声明 → 补录公开AI汇编的冲突元数据并标无原始证明，不升为已解。
- **查重**：仅有001469自身的MSE来源 → 新增与QX-P-001246（rev9e6c3f68818d8ac9）主命题同题关系；双方全文已核，只报告不合并。

##### 证据、定位与范围

- [社区原题/计算](https://math.stackexchange.com/questions/2751881/why-9k-pm-4-cant-be-written-as-sum-of-four-cubes)，**qwr原问及Oleg567答案**。访问程度：正文与可见答复已取得；数据未重算。问题的9k±4是尚需证明分支，不是四立方同余不可能。 适用性：与本题量词对照见 claim
- [作者教材原稿](https://swc-math.github.io/aws/2006/06CohenExtract.pdf)，**Cohen Theorem6.4.25，印刷p.370**。访问程度：定理搜索摘要已取得；PDF文本乱码，证明未完整核验。载Dem’janenko关于n≢±4mod9可为四整数立方和的定理。 适用性：仅部分同余类。
- [公开AI/社区汇编](https://we-solve.github.io/problems/can-every-integer-be-written-as-a-sum-of-four-perfect-cubes/)，**Status与Sources说明**。访问程度：页面检索正文已取得。同页承认Linnik已解标签缺原证明，并与七正立方资料混用。 适用性：不是独立证明。
- [作者代码仓库](https://github.com/akp2003/sum-of-four-cubes)，**README与目录**。访问程度：README已读；未取得固定提交、未运行。暴力寻找四立方算法的项目目标，不是全称定理。 适用性：与本题量词对照见 claim
- [新查重候选现版题卡](https://www.qunxingmath.org/p/QX-P-001246/)，**形式化∀n∈Z∃x1..x4∈Z；页脚card_rev9e6c3f68818d8ac9**。访问程度：正常HTTP取得完整HTML并解析可见全文；此前搜索工具入口受阻已恢复。主命题与001469完全相同，允许负整数立方。附带五立方等式中右侧展开为6m−1而非所写6m，应另修。 适用性：同题关系据全文量词判定；库卡旧文献状态不作为独立新证明。

##### 查重关系

- QX-P-001469 `772cfab02d631b92` ↔ QX-P-001246 `9e6c3f68818d8ac9`：**同题**。补取官网现版完整题面、形式化及人话版，页脚card_rev9e6c3f68818d8ac9与索引一致。双方主问均为∀n∈Z∃x1,…,x4∈Z，n=Σxi³，允许负数；001246附带五立方/非负子问题不改变主命题。该卡所写五立方等式右侧实际为6m−1，另留修订提示。

##### 实际检索路径

- 学术 / `system1_search_query`：`"four cubes" "every integer" identity 9`（group_02/receipts/s25.json，条目0，2026-11-26）。
- 学术 / `system1_search_query`：`"a^3+b^3+c^3+d^3" "9" integers`（group_02/receipts/s25.json，条目1，2026-11-26）。
- GitHub/代码 / `system1_search_query`：`site:github.com "four cubes" integers`（group_02/receipts/s26.json，条目2，2026-11-26）。
- 公开AI/社区 / `system1_search_query`：`"four cubes" "AI" proof integer`（group_02/receipts/s26.json，条目3，2026-11-26）。
- 查重：全库2469条索引正则 `four cubes|四.*立方`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 取得Dem’janenko1966原文；Cohen PDF文本乱码，本轮仅检索摘要/目标页定位，未逐页完整证明核查。
- 新同题卡001246还把6m−1的五立方恒等式写成6m：右侧展开或取m=0即可核；在其下一轮编辑复核中修正，本轮不改该卡。

#### QX-P-001471（版本 `5f47918cc234fae6`）

发现2026-11-23新预印本Ottem arXiv:2611.31152v1完整解决声明：整系数版本给出10节点quartic double solid的消解例。原卡把Q系数硬加到主问题且把对角线分解误释为一般Künneth拆块，需先修题面。新结论不自动解决Q系数版本。

##### 旧卡 → 变化

- **正式题面系数**：Q系数，除非否认Bloch猜想 → 恢复原帖与Voisin Question3.27的整系数主问；Q系数作为单独变体，不宣称被Ottem解决。
- **人话定义**：按Künneth分量拆块 → 使用Δ=X×p+Γ、Γ支撑真闭子集D×X的支撑型分解。
- **相关声明**：无公认解决记录且无声明 → 加入2026-11-23 Ottem完整预印本声明待核及AI辅助披露，不能把aiXiv转载计作独立验证。

##### 证据、定位与范围

- [社区原题](https://math.stackexchange.com/questions/5115069/a-variety-admitting-a-cohomological-decomposition-of-the-diagonal-but-not-a-chow?r=31)，**主问与Q系数背景句**。访问程度：全文已取得。Q系数出现在背景条件句；主问并未限定为Q系数。 适用性：与本题量词对照见 claim
- [作者预印本](https://arxiv.org/abs/2611.31152)，**v1，2026-11-23 18:19:37UTC；提交历史**。访问程度：摘要与提交历史已核。当前可见v1完整解决整系数Voisin问题的声明。 适用性：新预印本，非已刊/独立验证。
- [作者预印本完整证明声明](https://arxiv.org/pdf/2611.31152)，**Theorem1.1 p.1；Proposition2.1 p.2；(2.2)–(2.3) pp.3–4；AI disclosure p.4**。访问程度：5页全文已读；关键假设已对照，计算/依赖未独立复核。构造10节点quartic double solid消解，整系数上同调分解存在、Chow分解不存在；作者披露ChatGPT-6辅助。 适用性：仅整系数，不能直接回答Q系数版本。
- [公开AI索引](https://aixiv.online/abs/2611.02648)，**aiXiv转载、Source链接与AI use**。访问程度：全文已取得。2026-11-24转载前述arXiv，不是第二个独立证明。 适用性：与本题量词对照见 claim
- [作者代码](https://www.mn.uio.no/math/personer/vit/johnco/papers/10nodes.m2)，**原文p.4所列Macaulay2文件**。访问程度：入口不可达；未取得代码/未重跑。作者称验证部分计算；本轮不能核文件、依赖或固定版本。 适用性：与本题量词对照见 claim

**代码证据：** GitHub检索只命中另一份pg=q=0曲面Bloch猜想仓库，范围不同，未据此认定本三维主问解决。Ottem实际作者代码链接不可达；没有任何独立形式化/计算验证声明。

##### 实际检索路径

- 学术 / `system1_search_query`：`"cohomological" "not" "Chow" "decomposition" diagonal`（group_02/receipts/s25.json，条目2，2026-11-26）。
- 学术 / `system1_search_query`：`"Bloch" "rational coefficients" "cohomological decomposition"`（group_02/receipts/s25.json，条目3，2026-11-26）。
- GitHub/代码 / `system2_search_query`：`site:github.com "cohomological" "Chow" "diagonal" Ottem`（group_02/receipts/s27.json，条目0，2026-11-26）。
- 公开AI/社区 / `system2_search_query`：`site:zenodo.org "cohomological" "Chow" "decomposition"`（group_02/receipts/s27.json，条目1，2026-11-26）。
- 查重：全库2469条索引正则 `diagonal.*decomposition|对角.*分解`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- P0：独立核§2显式节点、判别曲线不可约/9节点及特征2专化的全部假设；作者Macaulay2文件本轮不可达。
- 确认有无v2/勘误/撤稿及同行反馈；本轮arXiv摘要显示只有v1，无后续版本信息。
- 若维护Q版，另核广义Bloch猜想与所需系数下的精确定义，不能照用整系数结论。

#### QX-P-001472（版本 `2f6e12c0ff38196c`）

字面全称∀k≥2,n≥4被4×4二维马图反例否定：删中心4顶点得到6连通分量，超过哈密顿路径允许的5。本轮自写DP独立复核并保存割集证书。原意k≥3仍须分偶边长已知闭巡、奇边长及严格open定义，不能笼统无已知结果。

##### 旧卡 → 变化

- **形式化范围**：∀k≥2,n≥4 → 若保留存在性全称须排除(2,4)并分别声明所指是Hamilton路径还是首尾不相邻open巡；原帖研究重点为k≥3。
- **已知进展**：k≥3开情形无已知解/文献 → 对允许闭的路径版：偶n≥4由EGG已解决；剩余奇n与严格open另列。

##### 证据、定位与范围

- [社区原题](https://math.stackexchange.com/questions/4752687/open-knights-tours-on-n-times-n-times-cdots-times-n-subseteq-mathbbzk?r=31)，**主问possibly open、最后段k≥3与link-length**。访问程度：全文已取得。源题没有要求对所有k=2,n=4成立；其主要提问是高维存在判据。 适用性：与本题量词对照见 claim
- [已刊论文作者稿](https://www.math.u-bordeaux.fr/~sgolenia/Fichiers/chess.pdf)，**EGG2012，定义p.1、Theorem1.3 p.3、§2步法**。访问程度：关键定义及定理已读。k≥3且各边≥4时，闭巡充要条件为至少一边偶数；strict open要求末点不攻击初点。 适用性：与本题量词对照见 claim
- [本轮独立有限计算+初等论证](group_02/receipts/1472_knight4x4.json)，**割集及整数位集DP证书；脚本1472_knight4x4.py**。访问程度：实际运行成功；非形式化工具验证。4×4删中心4点后6分量。Hamilton路径删s点最多s+1段，故不可能存在。 适用性：精确处理k=2,n=4，不外推到k≥3。

**附加论证：** 顶点为{0,1,2,3}²，马步为一轴±1另一轴±2。移除S={(1,1),(1,2),(2,1),(2,2)}后：四角各独立，其他8点分为两组4点连通分量，总数6。若原图有Hamilton路径，删S仅能将它切成至多5条路径段，且每个剩余连通分量至少需一段，矛盾。自写完整子集DP也复核无16点路径（最大15点），未使用外部代码。

##### 实际检索路径

- 学术 / `system2_search_query`：`"open knight tour" "higher dimensions"`（group_02/receipts/s27.json，条目3，2026-11-26）。
- 学术 / `system1_search_query`：`"Erde" "Golenia" "knight" higher dimensions open`（group_02/receipts/s28.json，条目2，2026-11-26）。
- GitHub/代码 / `system1_search_query`：`site:github.com "knight" "higher dimensions" tour`（group_02/receipts/s29.json，条目2，2026-11-26）。
- 公开AI/社区 / `system1_search_query`：`"knight tour" "higher dimensions" "AI"`（group_02/receipts/s29.json，条目3，2026-11-26）。
- 查重：全库2469条索引正则 `knight.*tour|马巡`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 核奇边长高维Hamilton路径完整分类及首尾不相邻版本；现有代码搜索未获得可采纳一般证明。

#### QX-P-001473（版本 `d919538dab93bf18`）

已核原帖两份作者PDF。λ为目标λR1+R2的速率权重，不是信道干扰参数。VWIC Proposition2仅算HK内界的和速率；另一方面CZI子类的λ=1已由HK-sub Proposition2证明达容量，不能写这一子类未知。一般VWIC仍无本轮完整解决。

##### 旧卡 → 变化

- **人话版**：干扰参数λ>1，λ=1临界 → 改为加权速率目标λR1+R2中的权重；λ=1为和速率方向。
- **已知子类**：λ=1无结果 → 明确CZI子类λ=1已有最优定理，一般VWIC主问另列。

##### 证据、定位与范围

- [社区原题](https://math.stackexchange.com/questions/4690736/does-han-kobayashi-attain-the-maximal-rate-sum-of-a-discrete-memoryless-very-wea?r=31)，**两条互信息定义及两篇原文链接**。访问程度：全文已取得。原题固定very weak定义并单问R1+R2最优性。 适用性：与本题量词对照见 claim
- [作者论文稿](https://chandra.ie.cuhk.edu.hk/pub/papers/manuscripts/VWIC.pdf)，**Liu–Nair–Xia，§III，Proposition2，pp.4–5**。访问程度：定义及Proposition2已读。SR_HK=max_{p1p2}[I(X1;Y1)+I(X2;Y2)]；一般容量等式未在该命题建立。 适用性：与本题量词对照见 claim
- [作者论文稿](https://staff.ie.cuhk.edu.hk/~cnair/pub/papers/IC/HK-sub.pdf)，**Nair–Xia–Yazdanpanah，p.2脚注1、Proposition2 p.3**。访问程度：关键命题、范围与证明已读。CZI是very weak子类；λ≤1支持函数相等，λ>1才有严格HK次优例。 适用性：仅CZI子类的λ=1已解，不推广全类。

##### 实际检索路径

- 学术 / `system1_search_query`：`"very weak interference" "Han-Kobayashi" lambda sum capacity`（group_02/receipts/s30.json，条目2，2026-11-26）。
- 学术 / `system1_search_query`：`"Han-Kobayashi" "λ" "Proposition 2" very weak`（group_02/receipts/s30.json，条目3，2026-11-26）。
- GitHub/代码 / `system2_search_query`：`site:github.com "very weak interference" "Han"`（group_02/receipts/s31.json，条目0，2026-11-26）。
- 公开AI/社区 / `system2_search_query`：`"very weak interference" "Han" (site:zenodo.org OR site:aixiv.online OR site:math.stackexchange.com)`（group_02/receipts/s31.json，条目1，2026-11-26）。
- 查重：全库2469条索引正则 `Han.Kobayashi|干扰信道`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 核最新VWIC和容量外界论文及两稿正式发表版本/修订；不把强干扰、Gaussian或CZI特例套到全类。

#### QX-P-001474（版本 `62f88c03948a2293`）

原帖、定理编号和页码已对应到Simon1982 Bull.AMS综述论文，卡称“书”应改。AMS PDF403、Euclid安全页导致关键原文未取得；因此势类、x量词与严格正性的精确定义尚未核，不能以一般唯一延拓结果或热核严格正性代替。

##### 旧卡 → 变化

- **出处类型**：Simon书 → Barry Simon, Schrödinger semigroups, Bull.AMS7(1982),447–526，DOI10.1090/S0273-0979-1982-15041-8。
- **正式题面**：a.e.λ但x与势类不全 → 待原文补ρ、x的量词和V假设；当前不适宜视作无歧义全称题。

##### 证据、定位与范围

- [社区原题](https://math.stackexchange.com/questions/191023/strict-positivity-on-the-diagonal-of-a-particular-integral-kernel-a-question-fr?r=31)，**题面C.5.2、p504及p510引用**。访问程度：全文已取得。原帖只重提Simon问题，没有给当前解决。 适用性：与本题量词对照见 claim
- [作者书目](https://math.caltech.edu/simon/biblio.html)，**综述书目[xxi]**。访问程度：书目已取得。确认为Bull.AMS7(1982)447–526论文，不是单行本。 适用性：与本题量词对照见 claim
- [期刊原文](https://www.ams.org/bull/1982-07-03/S0273-0979-1982-15041-8/S0273-0979-1982-15041-8.pdf)，**Simon原文全文入口**。访问程度：403不可达；Euclid另入口为安全页。本轮未读到p504/p510，不能核所有假设。 适用性：与本题量词对照见 claim

##### 实际检索路径

- 学术 / `system2_search_query`：`"Schrodinger semigroups" "C.5.2" "positive"`（group_02/receipts/s31.json，条目2，2026-11-26）。
- 学术 / `system2_search_query`：`"F(x,x" "Simon" "unique continuation"`（group_02/receipts/s31.json，条目3，2026-11-26）。
- GitHub/代码 / `system2_search_query`：`site:github.com "Schrodinger semigroups" "spectral" kernel`（group_02/receipts/s33.json，条目0，2026-11-26）。
- 公开AI/社区 / `system2_search_query`：`"Simon" "spectral kernel" (site:zenodo.org OR site:aixiv.online OR site:mathoverflow.net)`（group_02/receipts/s33.json，条目1，2026-11-26）。
- 查重：全库2469条索引正则 `spectral.*kernel|谱.*核|Radon`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 取得Simon原文pp504、510、唯一延拓节并核x为每点/几乎处处/函数非零的语义；本轮入口受阻。
- 核Kato势类UCP后续成果是否足够推出目标谱核命题；文献题名“Simon's problem”有不同问题，不得直接合并。

#### QX-P-001475（版本 `f2c65cf4da1f21d6`）

原帖用g_n表示普通相邻素数间隔又用相邻指标谈纪录，卡继续混用；应定义纪录指标n_j及G_j=g_{n_j}。Kourbatov2018提供启发式/数值研究，普通间隔无界和纪录表均不能证明纪录增量无界，本轮未取得该命题完整证明。

##### 旧卡 → 变化

- **符号**：g_n同时指第n普通间隔与第n纪录 → 先设d_n=p_{n+1}−p_n，再设纪录指标n_j及G_j=d_{n_j}；正式极限与等差尾部全部使用G_j。
- **历史数据**：83个已知纪录作为不带日期事实 → 注明2025原帖数据截点；当前表仅作有限证据，不支撑渐近证明。

##### 证据、定位与范围

- [社区原题](https://math.stackexchange.com/questions/5094186/on-the-difference-between-consecutive-maximal-prime-gaps)，**题面g_n与gnasher729启发式答案**。访问程度：全文与答案已读。题面指标有歧义；回答2/logn是概率模型启发，不是素数独立性定理。 适用性：与本题量词对照见 claim
- [已刊论文预印本](https://arxiv.org/pdf/1709.05508)，**Kourbatov v3 2018-02-24，p.1摘要、p.2 Introduction**。访问程度：版本、摘要和研究范围已核。研究第n纪录间隔的数值分布与猜想，明确以heuristic/statistical evidence为目标。 适用性：并未提供本卡纪录差limsup无穷的证明。
- [数据项目](https://primegap-list-project.github.io/lists/)，**Tables更新2026-11-17**。访问程度：索引表说明已取得、未重算数据。提供当前数据入口，纪录长度与有限记录不构成无穷性证明。 适用性：与本题量词对照见 claim

**代码证据：** 命中Numerisect文档的有限区间maximal-gaps计算接口，未取得固定提交/未执行；有限搜索不等于纪录差无界证明。

##### 实际检索路径

- 学术 / `system1_search_query`：`"record prime gaps" "increments" unbounded`（group_02/receipts/s32.json，条目2，2026-11-26）。
- 学术 / `system1_search_query`：`"maximal prime gaps" "g_n+2"`（group_02/receipts/s32.json，条目3，2026-11-26）。
- GitHub/代码 / `system2_search_query`：`site:github.com "record prime gaps" increments`（group_02/receipts/s33.json，条目2，2026-11-26）。
- 公开AI/社区 / `system2_search_query`：`"maximal prime gaps" "limsup" (site:math.stackexchange.com OR site:zenodo.org OR site:aixiv.online)`（group_02/receipts/s33.json，条目3，2026-11-26）。
- 查重：全库2469条索引正则 `maximal prime gap|极大.*间隔|记录.*间隔`；完整命中表在 `index_search_log.json`。指定对子从包内全文复核，新线索缺全文的保持“待定”。

##### 尚待复核

- 查纪录增量无界的专门无条件文献；另查普通相邻间隔差结果，不能借其直接解决纪录子序列。

#### 留存与边界

- `QX-NEW-01_逐题回传.jsonl`：25题逐题回传，保留id/card_rev/batch_id；含五路实际查询、数学分问、证据访问程度、建议修订及余留任务。
- `group_02/receipts/s01.json`—`group_02/receipts/s39.json`：39个实际网络请求及返回回执；s39图像二进制以元数据代替，未因此声称读到Cohen证明。
- `index_search_log.json`：25次全库索引检索及候选；4个指定对子均完成双方全文核对，均为相关但不等价。新候选2个也补齐当前官网全文：001468↔000738相关但不等价，001469↔001246同题；页脚版本均匹配索引。
- `group_02/receipts/QX-P-000738.*`、`group_02/receipts/QX-P-001246.*`：新候选正常HTTP获取的完整HTML、解析可见全文及抓取回执；此前搜索工具受阻不再作为“尚未读全文”的最终结论。
- `group_02/receipts/1472_knight4x4.py`、`group_02/receipts/1472_knight4x4.json`：本轮自写并实际执行的有限DP及割集证书；非形式化系统证明。
- 未穷尽全部引文、版本历史及所有社区平台；每题具体未执行/受阻点保留，不能将初查覆盖等同深查完结。


---

### QX-NEW-01 · group_03 初查发现与复核清单

检索日期：2026-11-26（Asia/Shanghai）。范围：分配的 25 张任务卡；13 个指定对子。本文为本轮可复核发现的工作记录，线上写入为零。逐题完整记录见 `QX-NEW-01_逐题回传.jsonl`；实际请求和来源索引见 `group_03/receipts/`（原始正文不重复打包）。零命中只表示已列入口内未取得可验证结果，不证明数学问题仍开放。外部代码一律未执行。

#### 1. QX-P-001486：按当前左支撑定义，原断言有显式反例

**旧卡 → 变化。** 旧卡称 von Neumann 代数中显然成立，并询问 Baer*-环是否成立。该断言按原帖和当前卡片共同采用的左投影定义已经为假，且反例就在 von Neumann 代数中。

原题：[MathOverflow 301691](https://mathoverflow.net/questions/301691/algebraic-version-of-unilateral-shift)，正文的左投影定义及问题式；本轮读取 ref `turn243834880view0`，主代理另行读取并复核 ref `turn434354799view0`。实际路径：`academic_03` 名称检索 → `verify_03` 特征检索 → `source_03` 原帖正文。GitHub 与公开 AI 查询分别在 `code_03`、`ai_03`。

**完整反例。** 令 \(H=\ell^2(\mathbb N_0)\)，\(A=B(H)\)。这是 von Neumann 代数，因而是 Baer*-环。令 \(Se_j=e_{j+1}\)，\(p\) 是投影到 \(\mathbb C e_0\) 的秩一投影。则 \(S\) 是等距算子，\(p\perp[S^n p]\) 对每个 \(n\ge1\) 成立，并且这些左支撑是投影到各坐标轴的投影，其格上确界为 \(I\)。因此 \(S\) 确实是题目定义的单边移位。

取

\[
v=\frac{\sqrt3}{2}(1,\tfrac12,\tfrac14,\ldots),\qquad q=\operatorname{proj}_{\mathbb C v}.
\]

由于 \(\|v\|^2=\tfrac34\sum_{j\ge0}4^{-j}=1\)，\(q\) 是非零秩一投影，特别是有限投影。直接计算得 \(S^*v=\tfrac12v\)，从而对每个 \(n\ge1\)，

\[
(S^*)^n q=2^{-n}q.
\]

非零标量倍 \(2^{-n}q\) 的值域仍为 \(\mathbb C v\)，所以按最小投影 \([y]y=y\) 的定义，\([(S^*)^nq]=q\)。于是

\[
\inf_{n\ge1}[(S^*)^nq]=q\ne0.
\]

同时 \(\|(S^*)^nq\|=2^{-n}\to0\)。这说明算子本身趋零与左支撑投影的下确界为零不能混用。原帖 wandering 定义一行的变量笔误不影响上述标准移位对正确条件的验证。

**建议回传。** `原题已反驳`；证据性质为本会话给出的解析反例，经主代理另核；不是已发表文献，不是形式化验证，不声称独立运行 Lean/Mathlib。删除“von Neumann 代数中显然成立”及相应人话解释。若作者想问另一种投影式，应另立经过核对的变体，不能静默换题。

#### 2. QX-P-001483：有限图子问已核；无限族有新的完整声明待核

原题：[MathOverflow 369168](https://mathoverflow.net/questions/369168/two-more-counterexamples-to-a-conjecture-from-1975-about-hamiltonicity-of-digrap)，两份边集及评论；ref `turn609355588view2`。

本轮用自己编写、可阅读的 Python 标准库脚本 `verify_finite_examples.py` 对原帖精确边集作有限枚举。两图均为 6 顶点无环强连通有向图；分别排序的入度和出度满足所问 Nash-Williams 条件。g2 有 19 条边，排序度序列为 (2,2,2,4,4,5)；g3 有 18 条边，序列为 (2,2,2,4,4,4)。对每图固定起点枚举全部 120 个候选顶点排列，均无 Hamilton 圈。g2 删去边 (5,4) 后，由置换 (2,3,4,5,1,0) 与 g3 同构。原始数值记录见 `finite_verification.json`。这是有限计算复核；未检验平面嵌入，也未运行外部或形式化代码。

新命中：[Peter Graham，Hexagon 2611.00844v1 PDF](https://hexagonmath.org/pdf/2611.00844v1)，以及 [aiXiv 索引 2611.02496](https://aixiv.online/abs/2611.02496)。PDF Theorem 1、Corollary 2（第 2 页）声称所有 n≥7 均有反例，合并 n=6 得任意 n≥6；Theorem 3（第 3 页）给加强性质的族。§4 声称提供 Lean 4/Mathlib 验证，归档为 [Zenodo 23969956](https://zenodo.org/records/23969956)。网页工具不能取得归档后，**通过普通HTTPS/API补取成功**，获得 v2 元数据、ZIP 和 GitHub tag 指向。

固定提交为 [`e9dd9382f179e38d76daaf4ed621eda6bd18c7b2`](https://github.com/6/clank-lab/tree/e9dd9382f179e38d76daaf4ed621eda6bd18c7b2/results/hamiltonian-degree-sequences)。已静态阅读 `lean/Statement.lean`、`Main.lean`、`Check.lean`：`NWDigraph.counterexample_all` 的类型为所有 n≥6 存在满足强连通、Nash-Williams 条件且无 Hamilton 圈的无环有向图。分别排序的出入度、可双向弧、强连通和圈的定义已与原题核对。工具链为 Lean 4.34.0；Mathlib 固定为 `5ed2965256430c3649e86755f9576b54eca72435`，其余8依赖也在锁文件固定。ZIP MD5 与 Zenodo 声明一致；SHA256 为 `4289cb23c65f2f124aee9a6d0d1176768e23bcde56d67b72b68fefa8b30f7fde`。

7个 Lean 文件的静态词法扫描没有 `sorry`、`admit`、新 `axiom`、`unsafe` 或 `native_decide`。但这**不是编译或内核验证**：`Check.lean` 的标准公理检查没有执行，作者写出的预期输出不是本轮实测。Theorem 1(b) 的小阶穷尽明确不在 Lean 中。无限族数学状态仍记 `完整证明/反例声明待核`；形式化证据已升级为 **`已核定理对应、未重跑`**，详见 `formalization_review.json`。没有执行归档内任何外部程序。

**出处风险。** Hexagon 的 2611.00844 不是同号 arXiv 论文；[arXiv:2611.00844](https://arxiv.org/abs/2611.00844) 实为另一篇微分几何论文。不能写成 arXiv 反例论文。PDF 文件名 v1、页首自报 Nov 5 v2、平台发布时间之间亦有差别；Zenodo API 确认其归档版本为 v2（发布2026-11-05，updated2026-11-21）。实际搜索路径：`academic_02` → `verify_02` → `ai_02` → `source_02`、`source_02_extra`、`source_02_details` → `primary_pdfs/hamiltonian_download_receipt.json`。现有完整声明与本轮有限枚举须分开，不将有限枚举推广到无限族。

#### 3. QX-P-001485：“包含意义极大”需纠正

原题：[MathOverflow 316075](https://mathoverflow.net/questions/316075/is-a-maximal-set-of-rectangles-known-for-which-lebesgue-s-differentiation-theore)，正文第 2–4 段；ref `turn249429376view1`。原帖把平面矩形作为一般 \(\mathbb R^n\) 管问题的特例；当前卡正式式 \(\Theta\subset S^1\) 也是平面问题，不能用“高维方向集”替换。

若将“极大”严格解释为卡片边界所说的集合包含极大，则这样的可行极大方向集不存在：给任意可行 \(\Theta\) 添一个方向 \(\theta\)，新增的固定方向矩形族经旋转也微分所有 \(L^p\)，\(p>1\)。对每个函数取两个满测集的交，就知两个微分族的有限并仍微分该函数。全部方向的族已知失败，因此任何可行集都不是全集，能严格添加一个方向而仍可行。此为本轮对当前形式化解释的直接推导，不是所搜文献的新定理。应将任务改为可行方向族的必要充分刻画，或明确另一种“极大”含义。

**重要后续补取。** Kroc–Lee–Pramanik [Directional maximal operators in the plane](https://arxiv.org/pdf/2608.23871) 已通过普通 HTTPS 下载取得。实际为 v2（2026-10-09），255 页；搜索索引还显示 v1、195 页。Theorem 1.1（p.14）给 admissible finite-order lacunarity 与方向/矩形极大算子有界性的刻画；**Corollary 1.3（pp.17–18）直接给矩形平均的 \(L^p\) 微分正反结论**。其正向覆盖每个 \(p>1\) 和每个 \(f\in L^p\)；反向为非 admissible finite-order lacunary 时，每个 \(p>1\) 存在非负 \(L^p\) 函数使平均几乎处处发散。Lemma 15.1（pp.183–184）核对了线段与矩形极大算子之间的控制，§1 四扇区归约处理一般方向。

因此，这已是准确匹配平面分类问题的**完整证明声明**，不是只有相邻线段问题的摘要。由于新稿专门修复旧证明缺口，且本轮并未审完 255 页构造，回传为 `完整证明/反例声明待核`；下步核 Definition 3.3 与主证明及独立评议，不继续沿用“未取原稿”的旧限制。原始 web 失败和后续下载成功均保留。实际路径：`academic_03`、`verify_03`、`source_gap_retry`、`focused_confirm`、`final_locators`，再 `primary_pdfs/download_receipt.json`。作者[论文页](https://sites.google.com/view/juyoungleehomepage/papers)也确认预印本。

#### 4. QX-P-001495 / 001496：新工作稿需作范围核验，且一稿已有显式错误

两题原来源是 [Hénon maps: a list of open problems](https://arxiv.org/html/2312.03907v1)，分别为 §3.1 Question 6 与 §4 Question 12。实际路径为 `academic_05`、`verify_05`、`ai_05`，再 `source_05`、`source_05_details`、`detail_remaining`。网页工具曾不能读 PDF；随后普通 HTTPS 补取成功，见 `primary_pdfs/zenodo_download_receipt.json`。**最终判断以已取得原稿为准。**

##### 001495：定义错误与新稿的周期一反例

旧卡把 mild dissipation 定义为非逃逸集面积有界，需改成清单 Definition 2 的稳定曲线条件：对非 sink 的遍历不变测度，几乎处处稳定曲线去基点的两分支无界。面积压缩本身不是该定义。

新稿：[G. de Azevedo Silveira，Computational evidence for mild dissipation of the Hénon map at (1.4,0.3)](https://zenodo.org/records/18824095)，[PDF](https://zenodo.org/records/18824095/files/paper.pdf?download=1)，2026-03-01。Theorem 1.1（p.2）给有限周期计算声明；Theorem 1.2 声称高熵测度结论；Theorem 1.3 附加全部周期轨道满足某 Lyapunov 下界的假设。即便这些都成立，也不是所有 \(|b|<1\) 参数的结论。

但原稿 Theorem 1.1 还有明确错误：它断言该参数下周期 1–12 均无周期轨道。对该稿自己定义的

\[
H(x,y)=(1-1.4x^2+y,\,0.3x),
\]

不动点方程为 \(y=3x/10\)、\(14x^2+7x-10=0\)，故存在两个实不动点

\[
\left(\frac{-7\pm\sqrt{609}}{28},\ \frac{3(-7\pm\sqrt{609})}{280}\right).
\]

直接代入即可验证，已反驳其“周期 1–12 无轨道”的书面断言。**此处反驳的是新稿内部断言，绝不意味着原 mild-dissipation 问题被反驳。** 回传保留新稿为有明确缺陷的待核声明，不能写成计算已验证的可靠进展。其从有限周期到全测度的推论也需另外审查，未运行作者所称 CAPD/Julia 验证。原稿引文多处显示“[?]”，只是需完善的文献定位问题，不作为数学反驳理由。

##### 001496：任意两条与 primary pair 不等价

新稿：[Kneading sequences determine parameters for the Lozi family](https://zenodo.org/records/18829061)，[PDF](https://zenodo.org/records/18829061/files/paper.pdf?download=1)，记录发布 2026-03-02、PDF 日期 2026-03-01。Theorem 1.1（p.2）写的是 primary pair \((k_0,k_{-1})\)，参数 \(a>1+b,0<b<1\)，且至少一条序列无限换号；不是原 Q12 在 \(\mathcal M\) 内“任意两个不同 kneading 序列”的全称陈述。Theorem 1.4 的 79 种最终周期模式只给各解处 Jacobian 非零；这种局部非退化本身不等于全局唯一参数。

卡片“参数到全部 kneading 数据单射”的口语改写也弱于任意两条即可恢复参数，应恢复原量词。此稿记受限完整声明待核；没有运行其 Sturm/区间代码，没有把作者自称回答 Q12 当成范围等价证据。

#### 5. QX-P-001500 / 001501：定义修正与严格凸范围的新结果

原文 [Bracci–Ökten 2507.19967v2](https://arxiv.org/html/2507.19967v2) 的 Definition 3.1 将 essentially visible 与 visible 区分为连接测地线的存在量词和全称量词，共同要求经过域内紧集。旧卡说“两条线不要交得太厉害”不准确。Question 3.3 首句要求无边界解析圆盘；第二句问光滑有界凸域，并未重复无圆盘条件。若卡希望同时要求两个条件，应明确这是强化问法。

Q3.10 保留凸性与所有射线着陆。作者预期否定不等于证明；非凸单连通平面例子不适用。若不存在所问反例，才可从已知正向推出 ray-landing 刻画 visibility；卡首段“否则”逻辑应纠正。

新取得 [Nikolov–Sarkar, Kobayashi visibility of strictly convex domains](https://arxiv.org/pdf/2610.12502)，**v2（2026-11-04）**。3 页原稿已读。Theorem 1（p.1）处理欧氏严格凸域上符合条件的 proper geodesic 度量；Corollary 3（p.2）给每边界点可局部严格凸化的有界复域的 Kobayashi 可见性，且不要求边界光滑。因此严格凸域不能作为这两问所求非可见例；一般凸域仍未被覆盖。v1 搜索摘要不能代替这次已取得的 v2。

路径：`academic_06`、`verify_06`、`academic_07`、`verify_07` → 原文 `source_detail_final` / `final_locators` → 普通 PDF 补取 `primary_pdfs/download_receipt.json`。GitHub 与公开社区只获得无关同词项；未取得本题形式化证明。

#### 6. QX-P-001498 / 001499：准确正则性范围与消解量词

原出处 [Dinew–Guedj–Zeriahi 1511.00705 PDF](https://arxiv.org/pdf/1511.00705) 已取得：Q19 在 p.11，Q34 在 p.17。旧 HTML 入口失败不表示原稿不可得。

001498 的目标是**整个 X** 上 Hölder 连续；ample locus 上的正则性不够。[Dang 2603.25520v2](https://arxiv.org/html/2603.25520v2)（2026-10-02）Theorem A 仅在 Zariski 开集上给 Hölder，Theorem B 在特殊 log resolution 拉回形式下给全局连续，不能提升成原问的一般全局 Hölder。[Guo–Song–Sturm 2609.28978v1](https://arxiv.org/html/2609.28978v1) §2 的 (2.2) 后也明确区别 Kähler 与 big semipositive 障碍；有曲率假设的结论不是只有 \(L^p\) 数据的版本。应替换卡片无明确出处的“2025连续模工作”占位，写入这些实际主定理与范围。

001499 要补齐 \(\forall\varepsilon>0\) 量词：每个 ε 可选择自己的有限 blow-up 复合 \(\pi_\varepsilon\)，拉回流分解为 SNC 正实系数除子流与正余流，后者**所有点** Lelong 数都小于 ε。这不是一次修改后余流 Lelong 数全零，也不是仅对解析奇点应用 Hironaka。GitHub 的解析消解挑战以及某仓库有限 Lelong 算术审计都不覆盖此问。尚未取得高维完整消解声明。

路径：`academic_06`、`verify_06` → `source_07`、`source_detail_final`、`source_final_new`、`detail_remaining`；GitHub `code_06`、公开索引 `ai_06`。

#### 7. 其余会影响题面或状态的纠正

| 题号 | 旧卡 → 建议变化 | 已核直接出处与定位 | 实际路径与待核点 |
|---|---|---|---|
| 001476 | 加 CH、aleph₁-calibre 的 submetrizability 不能覆盖仅 ccc 的问题 | [Xuan–Shi 2016](https://www.dml.cz/manakin/handle/10338.dmlcz/144922)，摘要、pp.131–134 | academic_01 / verify_01 / source_01_retry；更强假设的已刊变体，只作相关进展 |
| 001477 | “Carathéodory 至少四个脐点”改正；多面体定义要求仍分别保留 | [原帖](https://mathoverflow.net/questions/283626/what-is-an-umbilic-point-of-a-convex-polyhedron)要求列表；[Ghomi官方讲座](https://math.gatech.edu/seminars-colloquia/series/geometry-topology-seminar/mohammad-ghomi-20110124)写至少两个 | academic_01 / verify_01 / source_01_retry；光滑结果不解决多面体定义 |
| 001479 | 有限排除不能否定素数存在性；只确认两个给定数不满足 p³ | [原帖](https://mathoverflow.net/questions/516909/can-a-mirimanoff-prime-p-satisfy-3p-1-equiv1-pmodp3)；finite_verification.json | 两组搜索后自写模幂实算；11、1006003的模p³余数分别485、717092505034537041；GitHub条目不是p³已证定理 |
| 001480 | 去掉未经原帖支持的左端>0；恢复严格不等式为主问，非Wieferich只为后果 | [MO470571](https://mathoverflow.net/questions/470571/conjecture-x41-is-never-wieferich-prime?noredirect=1)，J定义与Conjecture1 | academic_01 / verify_01 / source_01_retry；J特殊定义和n起点仍按原文；未独立重跑OP的大范围计算 |
| 001481 | “非平凡单位不是±1”改为不是λg；F₂时为不是群元g；10种三维Bieberbach群不能直接当10种同商扩张 | [MO454329](https://mathoverflow.net/questions/454329/a-question-on-giles-gardam-counter-example-to-the-unit-conjecture-of-kaplansky)及[Craven–Pappas p.1](https://arxiv.org/pdf/1010.1144) | academic_02 / verify_02 / source_02；完整群分类与局部可指标应用尚待核；Gardam原GAP仓库不回答其他群 |
| 001482 | Q1已有2002文献；Q3一般n/常内存复杂度独立保留 | [MO392994](https://mathoverflow.net/questions/392994/factoring-integers-of-the-form-n-p-q2-using-elliptic-curves?r=31)，Q1更新与Q3；[Waterloo2002报告目录](https://uwaterloo.ca/combinatorics-and-optimization/research-combinatorics-and-optimization/technical-reports/technical-reports-2002)，CORR2002-02 | academic_02 / verify_02 / source_focused / original_1482_and_biseparating；官方1页摘要PDF提取乱码，未称完整算法已审 |
| 001484 | 保留正整数符号；2019三立方新大解一正两负，不是本题两正一负 | [MO337954](https://mathoverflow.net/questions/337954/how-many-solutions-of-x3-y3-z33-are-known?noredirect=1)，KConrad评论 | academic_02 / verify_02；Sutherland signed-cubes代码未运行；固定参数椭圆曲线纤维不穷尽三变量曲面 |
| 001487 | “支集不交”改为cozero不交；四问分开；一般非线性新定义不可混用 | [Araujo作者版](https://personales.unican.es/araujoj/autcontinref86.pdf) pp.1–4；[Feng–Leung2009.11570](https://arxiv.org/pdf/2009.11570) pp.1–3 | academic_03 / verify_03 / original_1482_and_biseparating；Feng–Leung修订定义更强，未直接覆盖原Q1 |
| 001488 | 添加已核更早MO203396；原卡239355与该帖关系尚未核，星号不能未经定义写成join | [MO203396](https://mathoverflow.net/questions/203396/pro-g-pg-q-topology-profinite-topology)正文 | academic_03 / verify_03 / source_06_extra；239355直接入口及多次检索受阻，待核原引用与*运算 |
| 001489 | 临界区间改为pc(Z³)<p<pc(Z²)；补概率量词 | [MO189431](https://mathoverflow.net/questions/189431/long-paths-in-the-supercritical-percolation?r=31)正文与讨论 | academic_04 / verify_04 / source_04_extra；固定维数格点模型与维数增长随机图不同 |
| 001490 | 文献版本补记v4（2015-02-25）；两问使用特定积分定义 | [1403.5209 PDF](https://arxiv.org/pdf/1403.5209)，§7 Q1 PDF p.13、Q2 PDF p.15 | academic_04 / verify_04 / source_04_extra / final_locators；Pettis/另一网积分不自动回答本问 |
| 001491 | 保留加并σ(T)与去并版区别、m=1子问；不以出版社ensemble摘要代替固定K定理 | [MO431810](https://mathoverflow.net/questions/431810/approximating-spectra-of-finite-rank-pertubations-of-laurent-operators-by-spec)；[DOI10.1007/BF01275512](https://link.springer.com/article/10.1007/BF01275512) | academic_04 / verify_04 / source_04_extra；期刊全文未取，Conj7.3精确范围仍待核 |
| 001492 | 任意极大理想交不等于X上点消失理想；2020同题名strongly-z文献不能只按名称套用 | [MO104812](https://mathoverflow.net/questions/104812/sums-of-strongly-z-ideals)；[2020论文DOI](https://doi.org/10.21859/IJMSI.15.1.23) | academic_04 / verify_04 / source_gaps / source_gap_retry；2020pointfree定义与本题极大交的等价待核，官方全文入口受阻 |
| 001493 | “经验熵”改成商半群n步分布Shannon熵；一般对称半群类须明确定义 | [MO96347](https://mathoverflow.net/questions/96347/entropy-of-bernoulli-walks-on-semi-groups)正文 | academic_05 / verify_05 / source_05_details；L/R对称本身不推出单峰 |
| 001494 | 保持已改正some degree和严格含于transitive set；补齐旧短引文 | [2312.03907v1](https://arxiv.org/html/2312.03907v1)，§2.1 Q1 | academic_05 / verify_05 / source_05；Newhouse wild sets与本问不同 |
| 001497 | 最大熵端点与所有α分开；全参数面及b=0约定需写明 | [2312.03907v1](https://arxiv.org/html/2312.03907v1)，§7.2.1 Q28；[Arai–Ishii1501.01368](https://arxiv.org/abs/1501.01368)摘要 | academic_06 / verify_06；后者仅摘要按b符号分区，未核完整原证明，数值等高线不证明任意α |

#### 8. 查重结果：13 个指定对子均不合并

已遍历全库 2469 条简索引，实际正则与命中保存在 `local_index_search.json`。已逐对读所给全文；若对方在本100题内，使用 `input/任务.jsonl`，外部分配卡使用 `查重参考题卡.jsonl`。参考卡不是任务。

| 指定关系 | 判断 | 正文差别 |
|---|---|---|
| 001491—002169、001491—002177 | 相关但不等价 | 谱的Hausdorff距离与Hausdorff测度/维数不同；后两卡本身只提供有限题面，不能做等价合并 |
| 001494—001495、001494—001496、001494—001497、001495—001496、001495—001497、001496—001497 | 同源不同问 | 同清单Q1/Q6/Q12/Q28：野吸引子、mild dissipation、Lozi编码恢复参数、Hénon等熵集 |
| 001494—002278 | 相关但不等价 | Hénon野吸引子与高维Fourier球形截断Carleson问题；名字重叠 |
| 001498—001499 | 同源不同问 | Q19全局Hölder与Q34任意qpsh的小Lelong消解 |
| 001498—002096 | 相关但不等价 | 方程解正则与Hölder函数球度量熵 |
| 001500—001502、001501—001502 | 同源不同问 | Q3.3弱强可见性分离、Q3.10射线着陆与Conj4.9 Denjoy–Wolff不同 |

每对双方题号、card_rev 与理由均在 JSONL。未用标题相似判同题，也没有执行合并。

#### 9. 复核优先级与可复现边界

优先处理：001486短解析反例的编辑复核；001483完整新族及已声称形式化的源文件核验；001485新修复性刻画的独立评议；001495新稿内部错误；001496受限声明的量词与局部/全局区分。其余以修正定义、来源和子问边界为先。

`QX-NEW-01_逐题回传.jsonl` 每题保留输入的 id、card_rev、batch_id；含原出处、两组学术、GitHub、公开AI/社区与本地查重共6条结构化路线记录。搜索入口具体是 system1/system2 网页索引，不宣称曾逐一登录每个论文数据库或每个AI站点作全库扫描。`search_manifest.json`列出原始调用及sha256；普通PDF/归档下载的只读回执另在 `primary_pdfs/`。网页全文不可达、抽取失败、只有摘要、命中不适用和已补取成功分别标记。

本轮只运行自己写的两个有限数学检查：6顶点图的穷尽与两个数的精确模幂。所有外部源代码只读，未执行，未把作者日志当独立通过。所有一般问题的“暂未找到可验证结果”只针对已列入口；没有从未发现新结果推出普通开放状态。


---

### 第四组实质发现（25题）

日期：2026-11-26（Asia/Shanghai）。这里只列题面、状态、出处或查重变化；全部实际查询见逐题JSONL。

#### QX-P-001502 · 题面有误

原稿 Conjecture 4.9 对应有界凸域的 visibility 与 Denjoy–Wolff 性质；题卡把后者误写成所有全纯自映射的轨道都趋边界，遗漏无内不动点条件。已知正向结果和反向猜想应分开；2026 平面 intrinsic visibility 文献不能直接覆盖一般 C^N 凸域。

**旧卡 → 建议变化**

- 在 DW 性质中恢复“无内不动点的全纯自映射”。
- 把定理方向、猜想方向和单个例子分开；注明 strong/essential/intrinsic visibility 的定义。

**证据与范围**

- [Bracci–Ökten 原稿](https://arxiv.org/html/2507.19967v2)；Definition 4.1、Theorem 4.5、Conjecture 4.9；访问：全文。无内不动点假设及可见性定义可直接定位。
- [An intrinsic notion of visibility and classification of planar Denjoy-Wolff domains](https://arxiv.org/abs/2610.25815)；检索摘要；abs/html 入口失败；访问：仅摘要。平面域、intrinsic visibility；不能越过维数和定义差异。

**实际搜索路径**：`"Denjoy-Wolff property" visibility "convex" conjecture` → `Bracci Okten bounded convex domains visibility Denjoy Wolff 4.9` → `site:github.com "Denjoy-Wolff" visibility` → `"Denjoy-Wolff" "visibility" site:aixiv.online`。

**待复核**：取得 2610.25815 全文并核其平面分类与本卡定义的关系。

#### QX-P-001503 · 题面有误

精确对应 Mnich–van Bevern §3.1 Open Problem 1。最大加工时间有界、所有加工时间相等、附加结构参数是不同条件；原卡把 pmax=O(1) 的多项式可解性称为平凡，没有该来源支持。

**旧卡 → 建议变化**

- 保留 pmax 的单参数问题；删除无依据的固定 pmax 多项式断言。
- 附加 release dates 或 pathwidth/overlap 参数的进展单列。

**证据与范围**

- [Mnich–van Bevern, Parameterized complexity of machine scheduling: 15 open problems](https://arxiv.org/pdf/1709.01670)；§3.1，Open Problem 1，PDF p4；v3；访问：全文。原问题及特殊情形。
- [带释放时间的等加工时间总拖期进展](https://arxiv.org/abs/2609.28751)；检索摘要；访问：仅摘要。包含 release dates，不适用无释放时间主问。

**实际搜索路径**：`"total weighted tardiness" "maximum processing time" parameterized` → `"1||" "pmax" tardiness FPT` → `site:github.com "total weighted tardiness" parameterized` → `"total weighted tardiness" "pmax" site:aixiv.online`。

**待复核**：若补入最新参数算法，需逐项核参数表，不能把附加参数省掉。

**查重**：QX-P-001504（同源不同问）：同为调度综述，前者单机加权拖期、pmax参数；后者job-shop makespan近似、(m,ε)参数。

#### QX-P-001504 · 题面有误

对应同一调度综述 §5.2 Open Problem 13。已知算法含每个作业最大操作数 nmax；本题要去掉该参数。原卡用 ε 依赖超多项式来否定 FPT-AS，误解了 f(m,ε) 可任意可计算增长的定义。

**旧卡 → 建议变化**

- 重写缺口为消除每个作业最大操作数 nmax。
- 保留机器数 m、精度 ε 与输入长度的分别量化。

**证据与范围**

- [Mnich–van Bevern 调度综述](https://arxiv.org/pdf/1709.01670)；§5.2 Open Problem 13，PDF p7；访问：全文。明确比较 (m,nmax,ε) 与 (m,ε)。

**实际搜索路径**：`"job shop" "FPT" "approximation scheme" machines` → `Mnich van Bevern "Open Problem 13" job shop` → `site:github.com "job shop" "FPT" approximation` → `"job shop" approximation site:aixiv.online`。

**待复核**：后续若出现近似算法，需核其是否仍依赖最大操作数或重入限制。

#### QX-P-001505 · 部分进展

原出处是 Wang–Salmaniw 综述模型 (2.10)、Open Problem 1。原文已经记录 detailed-balance 条件下的 top-hat 弱解；2025 Giunta 等结果针对光滑核，不能直接宣布一般 top-hat 多物种问题解决。

**旧卡 → 建议变化**

- 补记 detailed balance 下已知 top-hat 弱解。
- 不要把密度耦合模型 (2.10) 与动态认知图 PDE–ODE 模型 (2.11) 混用。

**证据与范围**

- [Wang–Salmaniw 原综述](https://www.math.ualberta.ca/~hwang/WangSalmaniwReview.pdf)；模型 (2.10)、Open Problem 1，PDF p13；访问：全文。综述已提 Jüngel 等 detailed balance 的 top-hat 弱解。
- [Giunta–Hillen–Lewis–Potts, Positivity and global existence for nonlocal advection-diffusion models of interacting populations](https://www.aimspress.com/article/doi/10.3934/math.2025949)；2025-09-16；10(9):21254–21272；访问：期刊入口。已刊；并非一般 top-hat 核定理。
- [同文预印本](https://arxiv.org/html/2312.09692v2)；Theorems 2、5、6；访问：全文。光滑核全局弱解及一维经典解的范围。

**实际搜索路径**：`"cognitive" "top-hat" "existence" Wang Salmaniw` → `"2201.09150" "2.10" "solutions"` → `site:github.com Giunta nonlocal existence top-hat` → `"top-hat" "existence" site:aixiv.online`。

**待复核**：对一般 top-hat 核还需明确弱解/经典解、维数及交互矩阵假设。

**查重**：QX-P-001506（同源不同问）：模型(2.10)的固定核适定性与非恒定稳态存在性不同。；QX-P-001507（同源不同问）：固定核存在性与R→0局部极限不同；后者还须R一致估计。

#### QX-P-001506 · 部分进展

对应 (2.10) 的 Open Problem 2；存在性须按系数、核、维数及周期/零通量/Neumann 条件拆分，不能把某组参数分岔或数值稳态升成任意参数的非恒定稳态定理。

**旧卡 → 建议变化**

- 按边界、参数及核划分子问，明确常数稳态与非恒定稳态。
- 将动态记忆变量模型的结果列为相关而不等价。

**证据与范围**

- [Wang–Salmaniw 原综述](https://www.math.ualberta.ca/~hwang/WangSalmaniwReview.pdf)；模型 (2.10)、Open Problem 2，PDF p13；访问：全文。三种边界和 steady state 问法。
- [Giunta 等 minimum energy states 工作](https://pmc.ncbi.nlm.nih.gov/articles/PMC9585017/)；入口出现验证页；本轮只核到摘要线索；访问：全文不可达。不能从摘要声称完整稳态分类。
- [Biological aggregations from spatial memory and nonlocal advection](https://jxshix.people.wm.edu/shi/Liu-Potts-Salmaniw-Shi-Wang-2025-PhyD.pdf)；检索摘要/作者 PDF 线索；访问：仅摘要。一维特定模型存在/分岔；需核模型差异。

**实际搜索路径**：`"nonlocal" "top-hat" "steady states" Giunta bifurcation` → `"Wang" "Salmaniw" "spatially non-constant" steady` → `site:github.com "nonlocal" "steady" "Giunta"` → `"nonlocal" "Giunta" "steady" (site:mathoverflow.net OR site:zenodo.org OR aiXiv)`。

**待复核**：对拟采用的分岔定理，逐项比对模型和参数。

**查重**：QX-P-001507（同源不同问）：非恒定稳态与非局部到局部极限的量词和待证目标不同。

#### QX-P-001507 · 题面有误

对应综述 (2.10) Open Problem 4，问 R→0 的局部极限；不能把固定 R 的非局部全局存在或局部系统某些系数下爆破误作所有参数的收敛/不收敛结论。

**旧卡 → 建议变化**

- 把解空间、时间区间、核缩放、相互作用系数与收敛意义补入待澄清项。
- 分离固定 R 的存在性与 R→0 极限。

**证据与范围**

- [Wang–Salmaniw 原综述](https://www.math.ualberta.ca/~hwang/WangSalmaniwReview.pdf)；Open Problem 4，PDF p13；访问：全文。原问题是指定模型的局部极限。
- [Giunta 等存在性论文](https://arxiv.org/html/2312.09692v2)；§4 local case；访问：全文。局部模型讨论不能替代 R-一致估计与收敛证明。

**实际搜索路径**：`"cognitive" "nonlocal-to-local" limit movement` → `"Giunta" "detection radius" zero blow up 2025` → `site:github.com "Giunta" "local" "blow"` → `"Giunta" "local" "blow-up" (site:mathoverflow.net OR site:zenodo.org OR aiXiv)`。

**待复核**：需要明确哪一类参数/初值下要求 R-一致控制。

#### QX-P-001508 · 题面有误

已补取 Pálfy v1 全文：Problem 1 位于 p2，是最大 DCI 秩随 p 的问题；p=3 的 r=6,7 在该页明确仍开放。原卡 DCI⇒CI“不必然”错误，DCI 确实蕴含 CI；生成集量词也应恢复为任意连接集。

**旧卡 → 建议变化**

- 改正 DCI⇒CI，并使用任意连接集 S,T。
- 区分“存在某个 p”与“逐 p 判定/最大秩是否一致有界”。
- 高秩 AI 辅助改进只按原文转述记录。

**证据与范围**

- [Pálfy, On the isomorphism problem of Cayley digraphs](https://arxiv.org/pdf/2610.33692v1)；p1 定义；p2 Problem 1 及前段；访问：全文。web 入口失败后经普通 PDF 下载取得全文；当前版本 v1。
- [Feng–Kovács rank-five 工作](https://arxiv.org/abs/1705.02929)；摘要；JCTA 2018；访问：摘要/出版信息。odd p 的 rank 5；Pálfy 原稿汇总全部 r≤5 已知。

**实际搜索路径**：`"C_p" "DCI" "six" "seven"` → `Palfy elementary abelian p groups DCI rank 6 7 2026` → `"DCI" "rank" "Cayley" site:github.com` → `"DCI" "rank" (site:aixiv.online OR site:mathoverflow.net OR site:zenodo.org)`。

**待复核**：若要采用 2p+2 构造，需要取得 Somlai 的原构造/修改细节与验证资料。

**查重**：QX-P-002279（相关但不等价）：DCI是Cayley图同构是否由群自同构实现；2279是连通无向Cayley图的Hamilton圈存在性。

#### QX-P-001510 · 题面有误

已取得 Sun–Xu–Yang v1：p19 §5 明确 k=2 仍开放，并说明可推进的端点装置条件。原卡关于 k=0,1 的限制类 NP 难却一般类未知的表述逻辑不成立。

**旧卡 → 建议变化**

- 修正 k=0,1 状态与 NP 难的限制类/一般类逻辑。
- 把 CPG 定义写为 internally disjoint grid paths，接触产生邻接。

**证据与范围**

- [Sun–Xu–Yang, Resolving Two Open Problems of Planar B_k-CPG Recognition](https://arxiv.org/pdf/2610.05838v1)；§5 Conclusion，p19；访问：全文。k=2 的端点装置 F2 仍为障碍。
- [Champseix–Galby–Munaro–Ries, CPG graphs: Some structural and hardness results](https://pureadmin.qub.ac.uk/ws/portalfiles/portal/228484347/Results.pdf)；2021；引言和 recognition 结果；访问：已刊全文。一般 Bk-CPG 与平面 k≥3 的已知 NP 完全边界。

**实际搜索路径**：`"Resolving Two Open Problems of Planar" CPG` → `"planar" "B_2-CPG" recognition complexity` → `"B_2" "CPG" site:github.com` → `"B_2" "CPG" (site:aixiv.online OR site:mathoverflow.net OR site:zenodo.org)`。

**待复核**：若进一步推进，核 F2 的所有 B2 表示中无自由端点且有暴露内点的要求。

**查重**：QX-P-001180（相关但不等价）：1510为内部不交格路径接触图识别；1180为平面点集无遮挡线段可见图识别，表示与邻接规则不同。

#### QX-P-001511 · 题面有误

取得原稿后确认引文和范围均需重建：2610.09443 研究固定 ⌞ 朝向的弦图，不能写成 ⟂ 或任意 B1-EPG。§7 留下的是寻找合适团树的多项式识别问题，未出现题卡声称的 k≥2 原句。

**旧卡 → 建议变化**

- 删除伪作逐字引文的 k≥2 英文句。
- ⌞、⟂、B1 不可互换；恢复原论文准确题名。
- 可按原稿重建弦 ⌞-EPG 多项式识别子问，或另行补证 k≥2 问题出处。

**证据与范围**

- [Sun–Xu–Yang, Characterizing chordal ⌞-EPG graphs via admissible clique tree orientations](https://arxiv.org/pdf/2610.09443v1)；p1–2 定义/摘要；§7 p21；访问：全文。固定朝向；指定 clique tree 的算法；总体 polynomial recognition 仍开放。

**实际搜索路径**：`"chordal" "EPG" "k" characterization` → `"admissible clique tree orientations" chordal EPG` → `"chordal" "EPG" site:github.com` → `"chordal" "EPG" (site:aixiv.online OR site:mathoverflow.net OR site:zenodo.org)`。

**待复核**：确认用户题库希望保留一般 k≥2 研究方向还是改为有确切原文的识别问题。

#### QX-P-001512 · 题面有误

已取得 Kühn v1，§5 p13 三个问题与卡的主要目标对应；已知 NP 难采用 Turing 归约，不能写成 Karp 归约。卡内“大 treedepth 强制大 treewidth”方向错误，长路径即反例。

**旧卡 → 建议变化**

- 修正 td 与 tw 的蕴含方向。
- Karp 归约、精确墙算法、可构造图族分为独立子问，保留度条件。

**证据与范围**

- [Kühn, Treedepth is NP-Hard on Planar Graphs of Maximum Degree 3](https://arxiv.org/pdf/2610.42033v1)；Theorem 1 p2；§5 Questions 1–3 p13；访问：全文。Turing 归约及墙/精确深度/平面 treewidth 三个不同目标。

**实际搜索路径**：`"Treedepth is NP-Hard on Planar Graphs of Maximum Degree 3"` → `"treedepth" "wall" "Karp" reduction` → `"treedepth" "wall" site:github.com` → `"treedepth" "Karp" (site:aixiv.online OR site:mathoverflow.net OR site:zenodo.org)`。

**待复核**：若找到新构造，必须检查 anchor 性质，不能仅有 td=k。

#### QX-P-001513 · 题面有误

已取得 2611.13917v1：当前编号是 §7 Question 7.2（p20），cactus 缺口在引言 p3。完整 G⊠Pℓ 与其诱导子图的复杂度不同；主问不能由诱导子图 NP 完全结果结案。

**旧卡 → 建议变化**

- 更新定位为 Question 7.2，保留题目版本。
- 不要把同文 Edge Coloring 或诱导子图结论移到完整强积 Max Cut。

**证据与范围**

- [Diester–Kühn–Rapp–Schneider–Ueckerdt](https://arxiv.org/pdf/2611.13917v1)；p3；Theorem 5.10；§7 Question 7.2 p20；访问：全文。当前下载 v1；完整强积为本卡目标。

**实际搜索路径**：`"Max Cut" "strong product" "cactus"` → `"2611.13917" "Question 37"` → `site:github.com "Max Cut" "strong product"` → `"Max Cut" "cactus" (site:aixiv.online OR site:mathoverflow.net OR site:zenodo.org)`。

**待复核**：未来算法须说明输入给的是 G 与 ℓ，还是强积表示，及运行时间对 ℓ 的依赖。

**查重**：QX-P-000515（同源不同问）：同文中Max Cut完整强积问题与平面3-edge-coloring问题；目标、输入类和问题编号不同。

#### QX-P-001514 · 题面有误

全文确认定义必须要求换边后连通。原卡把渐近目标写成“是否趋0”，但原文按无标号同构类计数，Open Problem 6.3 猜测极限 1−ρ≈0.661，并问 liminf>0；另已有 limsup≤1−ρ²≈0.885。

**旧卡 → 建议变化**

- 在形式化中加入换边后连通/仍为树。
- 将目标 B 改成存在极限及是否等于 1−ρ，另列 liminf>0 的较弱问法。
- 补录已证 limsup≤1−ρ²，并明确有限枚举不证明极限。

**证据与范围**

- [Bencs–van Dijk–Guo, Sustainable trees](https://arxiv.org/pdf/2610.17078v1)；定义 p1；Open Problems 6.1、6.3，Proposition 6.2，pp25–26；访问：全文。原文 αn=sn/tn 的无标号计数和具体未决极限。

**实际搜索路径**：`"Sustainable trees" Bencs Dijk Guo` → `"sustainable" "trees" "proportion"` → `site:github.com "sustainable trees" spectral` → `"Sustainable trees" (site:aixiv.online OR site:mathoverflow.net OR site:zenodo.org)`。

**待复核**：仍需一般分类与渐近极限证明。

#### QX-P-001515 · 题面有误

已取得 v5：CIG 的合法步是在已选集合 S 的一次 interval IC(S) 之外选点，不是“每步保持 S 凸”。ℓk 使用至多 k 条边的诱导路径。v5 §8 明确保留 geodesic、monophonic、ℓk 的 interval-game 复杂度。

**旧卡 → 建议变化**

- 重写合法步规则，区分 CIG 与 CHG。
- ℓk 改为长度至多 k 的诱导路径；注明正常/逆规则及优化/胜负判定版本。

**证据与范围**

- [Costa–Almeida–Sampaio, Hull Games of Induced Path Convexities in Graphs](https://arxiv.org/pdf/2609.30302v5)；pp1–2 定义；§8 p21；Acknowledgments pp21–22；访问：全文。v5 2026-11-16；作者披露 Claude 辅助的是其他证明/计算工作，非 CIG 完整解。

**实际搜索路径**：`"Hull Games of Induced Path Convexities" interval` → `"CIG" "monophonic" "geodesic" complexity` → `site:github.com "Hull Games" "convexities"` → `"interval game" "convexity" (site:aixiv.online OR site:mathoverflow.net OR site:zenodo.org)`。

**待复核**：三种凸性仍需分别追踪，不因 hull-game 已解结案。

#### QX-P-001516 · 原题已证

n=6,7,8,9 的至少两种非相似最少距离配置已被 Erdős–Fishburn 1996 Theorem 1 覆盖：最小距离数依次为3,3,4,4。不能继续把这四个有限目标作为未解；一般大 n 问题不在本卡结案范围。

**旧卡 → 建议变化**

- 将本卡四个有限存在性子问改为已解决，列出构造与最优性依据。
- 不要由此更改 Erdős91 一般版本。
- 正式证据优先用1996已刊定理；Lean 路径单记核验边界。

**证据与范围**

- [Erdős–Fishburn, Maximum planar sets that determine k distances](https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Erdos2.pdf)；Theorem 1 p116；Fig.1 p117；Discrete Math.160(1996)115–125；DOI 10.1016/0012-365X(95)00153-N；访问：已刊全文；原页图像已核。g(2)=5,g(3)=7,g(4)=9，及9点四距离配置。
- [Formal Conjectures Erdős 91](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/91.lean)；variants.six / seven / eight / nine；外部 proof 链接；访问：代码网页。registry 内 theorem 使用 sorry；research solved 标签不是本次内核验证。
- [外部 Lean 证明线索](https://github.com/linrock/math-proofs/blob/cd3cf0b176e95209584bf35555a7c0e501255f6e/erdos-91/Solution.lean)；固定提交 cd3cf0b176e95209584bf35555a7c0e501255f6e；L165/L168；访问：入口不可达。他人提供固定提交；本轮未取得/重跑，不能称独立形式化通过。

**本轮解析核对**

记 Rm 为正 m 边形顶点。n=6 用 R6 与 R5 加圆心，均3距离；n=7 用 R7 与 R6 加圆心，均3距离；n=8 用 R8 与 R7 加圆心，均4距离，三对由凸包顶点数不同知不相似。n=9 用 R9 与 Erdős–Fishburn Fig.1 任一9点4距离配置；后者非正9边形。g(2)=5排除6、7点的≤2距离，g(3)=7排除8、9点的≤3距离。

**实际搜索路径**：`"Erdos" "91" "Kovács" "distances"` → `"six" "seven" "eight" "nine" "distinct distances" non similar` → `site:github.com "ErdosProblems/91.lean"` → `"Erdős" "91" "non-similar" (site:aixiv.online OR site:mathoverflow.net OR site:zenodo.org)`。

**待复核**：若题库要求坐标证书，可将 Fig.1 对应配置转录后另行精确验算。

#### QX-P-001517 · 题面有误

h_c(n)≥5 的正确量词是每个固定 c>0，存在 N(c)，所有 n≥N(c)。这是无限渐近子问而非有限目标；用 no-five-collinear 集合的4-rich线数 o(n²) 可作等价改写。

**旧卡 → 建议变化**

- 恢复 ∀c>0 ∃N(c) ∀n≥N(c) 的次序。
- 将至少4点写清，删除“有限验证足以解决”的暗示。
- 新增与QX-P-000211（55b33e37dcfa461a）的同题关系：两者是渐近命题的逆否改写。

**证据与范围**

- [Erdős Problems 102](https://www.erdosproblems.com/102)；原入口失败；检索摘要；访问：入口不可达/摘要。需以精确 h_c 定义复核所有常数范围。
- [Erdős 原始问题论文](https://lematematiche.dmi.unict.it/index.php/lematematiche/article/download/587/555/)；p236，Problem 17；检索返回该页正文；访问：原 PDF 可取得；正文由检索定位。no five collinear ⇒ 4-rich lines=o(n²)，是本卡 h_c≥5 子目标的等价方向。
- [Erdős102 Hunter 变体 Lean 线索](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/eee8e904a0eb8511302bc809b9486116ec079e69/Proofs/T_Erdos102_erdos_102_variants_hunter.lean#L1113)；固定提交 eee8e904a0eb8511302bc809b9486116ec079e69，hunter variant；访问：检索线索。Hunter 上界变体不等于本题五点共线下界；未取得并重跑。

**实际搜索路径**：`"Erdos" "Purdy" "five" "lines" conjecture` → `"h_c(n)" "5" lines Hunter` → `site:github.com "Erdos" "102" "four"` → `("Erdős 102" OR "Erdos 102") (AI OR Lean OR "proof")`。

**待复核**：同题关系以补齐“每个c>0、充分大n”的量词为前提；只对应101，不对应102全部增长率目标。

**查重**：QX-P-000211（同题）：补齐1517的渐近量词后等价：若无5共线集合的4-rich线数不是o(n²)，则某固定c>0有任意大n违反1517；反向由同一逆否推理。原卡“有限目标”须先修正；不是把Erdős102一般增长率全问与101合并。

#### QX-P-001518 · 部分进展

MO 原问与 monic、实系数非负、乘积0/1的表述对应。新 Hexagon v2 声称完整解决一因子恰为三项式的子情形，未解决一般因子；另作者代码仓库声称验证总次数≤45，未在本轮重跑。

**旧卡 → 建议变化**

- 增加三项式子情形的完整证明声明待核，保持一般问题独立。
- 新查重：001289（3d0c777f5ae41623）当前正文漏monic，a=2,b=(1+x)/2即反例；其意图与1518同源，但须先修复再考虑同题。

**证据与范围**

- [MO339137 原帖](https://mathoverflow.net/questions/339137)；问题及回答；访问：全文。monic 与非负系数都是必要版本条件。
- [Baravelli, The Unfair 0–1 Polynomial Conjecture for Trinomial Factors](https://hexagonmath.org/2611.00674v2)；v2 2026-11-20；PDF Theorem 1 p1；Provenance；访问：全文。AI 生成证明/稿件/Lean 的作者自述；三项式特例。最初v1链接返回v2内容，已按v2重新核对。
- [ZeroOnePolynomials 作者仓库](https://github.com/dzhang314/ZeroOnePolynomials)；README；solver 与 Lean 项目目录；访问：代码入口。作者称总次数≤45的计算验证；本轮未取得固定提交及依赖复现。
- [Formal Conjectures MO339137](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Mathoverflow/339137.lean)；mathoverflow_339137 与概率等价定理；访问：代码网页。两处均有 sorry；不能视为已形式化证明。
- [Palomar 形式化注册](https://palomar-registry.org/entry?id=PALOMAR-2026-11-20-000022&version=1)；Hexagon 链接；页面仅 JS shell；访问：入口仅壳页。只能记他人声称已形式化验证，未核定理/依赖。

**实际搜索路径**：`"0,1" "monic" "nonnegative" polynomial factors` → `"339137" polynomials factors` → `site:github.com "339137" polynomial` → `"unfair 0-1" (AI OR Lean OR aiXiv)`。

**待复核**：取得新稿关联 Lean 仓库固定提交、定理路径、依赖、公理报告并按原题核对应。；001289全文已取得且版本一致；仅报告归一化错误和特例关系，不自动合并。

**查重**：QX-P-001289（特例/强化）：同一猜想来源但当前题面不等价：001289漏monic，其全称断言被a=2,b=(1+x)/2反驳；1518含monic是受限版本。先修正001289归一化后才可按同题处理。

#### QX-P-001519 · 部分进展

f(137) 的精确极值未取得可验证结果；2026 Chaffin 已给 f(20)=249、f(21)=282 的作者计算结果，明显超出原卡旧进展，但不能外推至137。来源具体为TAOCP预分册旧版题号。

**旧卡 → 建议变化**

- 补入20/21的新计算结果并注明作者计算、未独立复跑。
- 任何137下界起始牌列不得当作最优精确值。

**证据与范围**

- [TAOCP 数据集](https://huggingface.co/datasets/sytelus/taocp_open_problems)；taocp-v4a-7.2.1.2-107；Vol.4 Pre-Fascicle2B rev12，2004-12-10，printed p36；访问：数据行全文。须区分旧预分册与最终4A页码。
- [2021 Topswops 最大步数计算](https://arxiv.org/abs/2103.08346)；摘要；访问：摘要。18与19的结果。
- [Ben Chaffin 作者计算说明](https://benchaffin.com/topswops/topswops.html)；2026-04-14，Results 与 search algorithm；访问：作者全文。20/21的最大步数及起始牌列；不是137结果。

**实际搜索路径**：`"topswops" "137"` → `"topswops" "maximum" "2026"` → `site:github.com topswops 137` → `"topswops" (AI OR "formal proof" OR "f(137)")`。

**待复核**：137仍需匹配的全局上界/最优性证书。

**查重**：QX-P-000053（同源不同问）：同为TAOCP；1519问TopSwops137最长步数，53问10阶三个MOLS存在。；QX-P-000477（同源不同问）：同为TAOCP；477为模立方根与分解复杂度，1519为前缀反转极值。；QX-P-000478（同源不同问）：同为TAOCP；478为Scholz–Brauer加法链，1519为TopSwops。

#### QX-P-001520 · 未作判断

回源数据行 current_status=not-applicable、is_still_open=null；卡将历史 source-marked-open 沿用成当前二元开放状态不妥。练习要求尝试自动补断言，没有规定完备性、语言范围和验收标准。

**旧卡 → 建议变化**

- 改成任务规格待定义/非二元开放分类。
- 明确程序语言、允许断言、目标正确性、是否要求完备以及成功判据后再立题。

**证据与范围**

- [sytelus TAOCP 数据集](https://huggingface.co/datasets/sytelus/taocp_open_problems)；taocp-v1-1.2.1-14，current_status_as_of=2026-08-03；访问：数据行全文。current_status not-applicable；is_still_open null；不赋二元解决状态。
- [同数据源代码展示](https://github.com/sytelus/taocp/blob/main/knuth_open_problems_viewer.html)；相应练习与状态字段；访问：检索/代码入口。不是独立数学证明。

**实际搜索路径**：`Knuth "1.2.1" "14" assertions program` → `"Algorithm E" "assertions" "Knuth"` → `site:github.com Knuth "1.2.1" "14" assertions` → `"Knuth" "assertions" "1.2.1" automated`。

**待复核**：没有上述规格，不能用现有自动验证器成功或不可判定性口号直接结案。

#### QX-P-001521 · 题面有误

已取得atlas原始行：标题写EGZ，canonical实际写有限交换群Davenport常数D(G)，且误称全群D(G)=1+Σ(n_i−1)、循环群D(Cn)=2n−1；来源内部不一致。现卡又改成|G|项Gao常数E(G)并混入非交换群，必须重建题源。Qu新稿只为E(G)的上界与取等分类声明。

**旧卡 → 建议变化**

- 先修源内错配：保留一般E(G)问题需另建精确文献锚点；不能把atlas中Davenport公式当其出处。
- 统一常数记号、序列/子集及非交换乘积重排条件。
- 加入新上界预印本声明并保留其未评审/未独立验证边界。

**证据与范围**

- [Tommysha atlas精确数据行](https://huggingface.co/datasets/Tommysha/open-problem-atlas)；row_idx794；opa.mathematics.combinatorics.erdos-ginzburg-ziv-generalization；statement_canonical及why_it_matters；访问：数据API原始行已取得。标题EGZ、canonical Davenport；常数与命题发生源内错配。
- [Yongke Qu, The Erdős–Ginzburg–Ziv theorem for finite groups](https://arxiv.org/pdf/2610.26122)；v1 2026-10-19；定义p1；Theorem1.4、Corollary1.5 p2；Lemma2.2 p4；访问：全文。88页新预印本已取得并核主定理范围，未逐行审证明/运行计算。
- [Caro–Gao 定理参考](https://math.colgate.edu/~integers/w102/w102.pdf)；Theorem2；检索摘要；访问：仅摘要。交换群固定群阶子序列的常数公式，不等同exp(G)版本。
- [Geroldinger–Liebmann–Philipp, On the Davenport constant and on the structure of extremal zero-sum free sequences](https://arxiv.org/abs/1009.5835)；摘要；2010-09-29；访问：作者预印本摘要。明确给C2⊕C(2n)^r（n≥3奇数,r≥4）的d>d*反例族，反驳atlas的全群普适等式。

**实际搜索路径**：`"Erdos Ginzburg Ziv constant" "exponent" "Gao"` → `"E(G)" "D(G)" "|G|" Gao theorem` → `site:github.com "Erdos Ginzburg Ziv" "finite groups"` → `"Erdős Ginzburg Ziv" "finite groups" (Lean OR aiXiv OR "AI proof")`。

**待复核**：完整复核 Qu 稿的非可解群部分及计算表；查公开勘误/后续版本。；若保留一般Davenport研究方向须用正确已知反例和未解群类重建；若保留E(G)则用明确的product-one文献定义。

#### QX-P-001522 · 题面有误

已从atlas数据API取得原始完整条目。它写E_n(f)_p≤C(r,p)ω_r(f,1/n)_p/n^r，在标准光滑模定义下多了n^−r，存在立即反例；不能将该错式直接补入原占位题卡，也不能为它寻找有限尖锐常数。

**旧卡 → 建议变化**

- 记录题卡原先缺失规格，以及上游补回公式本身错误。
- 不要沿用“来源标human_verified/high”作为数学正确性凭据。
- 先选正确的标准光滑模型或导数型Jackson估计，再定义尖锐常数问题；本轮不擅自替换成另一个猜想。

**证据与范围**

- [Tommysha atlas精确数据行](https://huggingface.co/datasets/Tommysha/open-problem-atlas)；row_idx565；opa.mathematics.approximation-theory.approximation-jackson-bernstein-sharp；statement_canonical；访问：数据API原始行已取得。明确给L^p[0,2π]、次数≤n、标准r阶光滑模以及额外n^−r因子。
- [Balaganskii 尖锐 Jackson–Stechkin 常数工作](https://www.mathnet.ru/php/archive.phtml?jrnid=mzm&option_lang=eng&paperid=8575&wshow=paper)；2013；L2 特定设定，检索摘要；访问：仅摘要。不同函数空间/光滑模的常数不能互换。

**本轮解析核对**

固定r=1,p=2。对每个n≥1取实函数f_n(x)=cos((n+1)x)，它与所有次数≤n的三角多项式L²正交，故最佳逼近误差E_n(f_n)₂=||f_n||₂>0。周期平移保持L²范数，由三角不等式ω₁(f_n,1/n)₂≤2||f_n||₂。因此atlas所写估计会要求1≤2C(1,2)/n，对任意大n不可能。故该规范下不存在统一有限常数。此为本轮显式解析反例，针对上游具体公式，不否定标准Jackson定理。

**实际搜索路径**：`"approximation-jackson-bernstein-sharp"` → `"Jackson Bernstein" "sharp constant" approximation` → `site:github.com "Jackson Bernstein" "sharp"` → `"Jackson" "Bernstein" "sharp" (Lean OR aiXiv OR "AI proof")`。

**待复核**：须从Jackson/逼近论原始文献选定一个正确规范化及明确常数目标。

#### QX-P-001524 · 题面有误

最新 Kourovka19.14 的量词是所有 Sylow 子群共同生成的拟簇。卡内“Sylow=G 当且仅当幂零”错误：Sylow等于G需G为p群；幂零群的平凡性来自G是各Sylow的直积。

**旧卡 → 建议变化**

- 更正幂零群的说明和共同生成量词。
- 保留一般有限G问题，与19.15分开。

**证据与范围**

- [Kourovka Notebook](https://arxiv.org/pdf/1401.0300v50)；19.14，PDF p142；访问：全文。有限G及共同生成的拟簇。
- [Budkin 2025, On the quasivariety generated by a 3-nilpotent group](https://math-semr.ru/en/content/22-1)；卷22(1) pp110–124，目录/摘要；访问：仅书目/摘要。相关拟簇结果，未核其覆盖19.14，不作主问解决证据。

**实际搜索路径**：`"Kourovka" "19.14"` → `"quasivariety" "Sylow" "finitely" Budkin` → `site:github.com "Kourovka" "19.14"` → `"Kourovka" "19.14" (AI OR Lean OR proof)`。

**待复核**：Budkin 2025全文若要引用为进展，需核其定理与19.14关系。

#### QX-P-001525 · 题面有误

Kourovka19.15明确 A 为有限幂零群；卡的形式化遗漏有限性。L(qA) 要求每个单元素的正常闭包属于 qA，不能与全群属于 qA 或普通局部幂零性互换。

**旧卡 → 建议变化**

- 在形式化中加 finite A，并保持G不要求有限/有限生成。
- 避免把qA的有界幂零类结论直接套给L(qA)整个G。

**证据与范围**

- [Kourovka Notebook](https://arxiv.org/pdf/1401.0300v50)；19.15，PDF p142；访问：全文。有限nilpotent A；∀a∈G 正常闭包属于qA。

**实际搜索路径**：`"Kourovka" "19.15"` → `"L(qA)" "nilpotent"` → `site:github.com "Kourovka" "19.15"` → `"Kourovka" "19.15" (AI OR Lean OR proof)`。

**待复核**：后续候选反例应核每一个单元素正常闭包，而非只核生成元。

#### QX-P-001526 · 部分进展

Kourovka19.33的“至少p”必须计不同线性不可约成分，不能计重数。对称、交错、p可解与散在单群已在题集列为已验证，Rossi–Sambale仅推广p可解范围，且其v1猜想后来修改，不能误当原问反例。

**旧卡 → 建议变化**

- 把“至少p个”改成“至少p个不同线性成分”。
- 将p可解定理、blockwise变体与一般Giannelli问分别登记。

**证据与范围**

- [Kourovka Notebook](https://arxiv.org/pdf/1401.0300v50)；19.33，PDF p145；访问：全文。完整量词、distinct及已验证群类。
- [Rossi–Sambale, Restrictions of characters in p-solvable groups](https://arxiv.org/abs/2106.04818v2)；v2 2021-07-22；Abstract及Comments；访问：摘要/版本信息。其自身原猜想曾错误并修改，不能说Giannelli原问被反驳。
- [Giannelli–Sambale, On restriction of characters to defect groups](https://benjaminsambale.github.io/pdfs/GS.pdf)；摘要与Introduction，作者PDF检索；访问：检索摘要。blockwise变体改变P为defect group并加height条件，非直接全群解决。

**实际搜索路径**：`"Kourovka" "19.33"` → `Giannelli "p" "different linear constituents" restriction` → `site:github.com "Kourovka" "19.33"` → `"Kourovka" "19.33" (AI OR Lean OR proof)`。

**待复核**：需要一般非可解群的同范围证据才能改主问状态。

#### QX-P-001527 · 题面有误

Kourovka19.34限定有限生成G，卡主式遗漏。有限G肯定已知；要求对每个内自同构的交换子集成子群，不可与“所有自同构的扭共轭单位类成子群”的更强假设混同。

**旧卡 → 建议变化**

- 在主式恢复有限生成。
- 区分inner/all automorphisms；删去无法定位或不对应的Nasybullov–Novikov泛称进展。

**证据与范围**

- [Kourovka Notebook](https://arxiv.org/pdf/1401.0300v50)；19.34，PDF p145；访问：全文。有限生成和有限群已知肯定。
- [Gonçalves–Nasybullov, On groups where the twisted conjugacy class of the unit element is a subgroup](https://www.tandfonline.com/doi/full/10.1080/00927872.2018.1498873)；Communications in Algebra47(2019)930–944，摘要；访问：出版摘要。对所有自同构的性质及DCC等额外假设下结论；非原问一般解。
- [原卡所列预印本入口](https://arxiv.org/abs/1705.06842)；abs重复访问失败；访问：入口不可达。仅作为待核原卡引文，不当成已读全文。

**实际搜索路径**：`"Kourovka" "19.34"` → `Nasybullov Goncalves "commutators" "residually nilpotent"` → `site:github.com "Kourovka" "19.34"` → `"Kourovka" "19.34" (AI OR Lean OR proof)`。

**待复核**：原卡2024相关文献需给准确题名、编号并核假设；本轮命中的是brace分类，不足采用。


---
