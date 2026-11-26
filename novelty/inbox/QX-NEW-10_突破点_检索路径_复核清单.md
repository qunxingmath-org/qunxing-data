# QX-NEW-10｜突破点、检索路径与复核清单

核查日期：**2026-11-26（北京时间）**。任务范围严格取随包《任务.jsonl》的100张卡；参考题卡和全库索引没有扩充为额外任务。逐题回传保留原 `batch_id`、`id` 与 `card_rev`。本轮没有修改线上库、合并题卡或发帖。

## 执行与证据边界

| 项目 | 本轮结果 |
|---|---:|
| 逐题回传 | 100 / 100 |
| 实际查询、读取及本地查重记录 | 1153 |
| 按题登记的证据条目 | 278 |
| 指定配对双方正文复核 | 71 / 71 |
| 新增双方正文已读的关系（按无向对子去重） | 3 |
| 新增仅简索引候选、仍待正文复核 | 12 |
| 有修订建议的题卡 / 建议条数 | 70 / 103 |
| 本轮独立重跑第三方 Lean / Isabelle 工程 | 0 |

“查询、读取记录”包括搜索词、打开原稿、读取代码和本地题面配对，**不是独立搜索引擎调用次数**。同一批请求的聚合返回不归因给某个单独检索词。每题已列实际入口、词句、日期、结果、URL/定位与访问层级；不可达、只摘要和主张未核分别记录。“暂未找到可验证结果”不等于已证明仍开放。

数学结论按子问记录；证明声明、证据强度和形式化状态分开。四份本地脚本只验证小算例、有限证书或转录问题，不冒充外部完整证明重跑。第一子问的标签统计仅供审计，不应取代各题量词与子问范围。

## 优先处理的变化

| 题号 | 旧卡需要改变的内容 | 本轮建议与关键边界 |
|---|---|---|
| 002413、002454 | RH依赖链只列弱声明 | [Lean FRO / Mathlib 11月21日认证](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)支持标准RH；据此推得密度假设，并结合[Saito v3 Theorem1.8](https://arxiv.org/html/2508.16068v3)推得最小Mills常数超越。列已证推论，同时保留本轮未重跑。 |
| 002432 | 用图覆盖模型宣称Petersen反例独立核实 | 边星染色与局部双射顶点图同态不等价，撤销旧独立验证标签。K4正例已自写复算；文献52顶点反例另列，未重新认证。 |
| 002436 | 未列Pierce–Birkhoff完整反例 | 新增[Lai–Lim–Ren 2609.10420](https://arxiv.org/abs/2609.10420)与30维定理端点；仍为完整反例声明待核。有限闭拼接已保证连续，旧背景也须改。 |
| 002443 | 未列完美域全维消解声明 | 新增Tian声明；摘要中的global replacement certificate与无条件全解之间的桥梁待审，798页正文未成功取得。 |
| 002431、002455 | 泛称Lean全证明 | 完美长方体端点不含原题必要桥梁；六阶矩端点保留Watt41前提且41.007/41.008不同，均不能作原题无假设全证。 |
| 002494 | 当前题面全称成立 | F={∅}退化例直接否定现有字面版本；先补非平凡性。通常Frankl猜想不受此反例否定。 |
| 002467、002477、002482、002484、002500 | 需细分全声明与证书覆盖 | 分别核小CM候选环、Thompson F、Chowla、Navier–Stokes、ζ(5)的真实终点、依赖或访问失败；没有统一标“形式化已通过”。 |
| 002469 ↔ 002470 | 两卡关系不清 | 标准流形约定下是同一光滑四维Poincaré核心命题；保留Davis声明来源差别，只报告，不合并。 |

下文只纳入影响状态、题面、出处或查重判断的重要变化。所有100题的完整记录在 `QX-NEW-10_逐题回传.jsonl`；71个指定对子及新增候选另汇入 `QX-NEW-10_查重回传.jsonl`。


## 第一部分：群论、数论、几何与题面校正

### QX-P-002397｜Kourovka 21.78：pro-p 群各阶上同调有限是否推出上同调环有限生成

**现版**：`95dbcacdf8acdccf`。完成本轮初查；主问题未找到可验证的一般解决。旧卡把非交换自由 pro-p 群的上同调环写成外代数，需要纠正。

- **P1 · 修正已知结果**：旧卡“自由 pro-p 群上同调环为外代数” → 改为 F_p⊕H^1 且所有正次数乘积为0；外代数描述属于适当的自由阿贝尔 pro-p 情形。

**直接证据与范围**：

- [Kourovka Notebook v50](https://arxiv.org/pdf/1401.0300v50) — 21.78，印刷页190–191；问题集／原出处，全文定位。原题是各 H^n(G,F_p) 有限是否推出 H*(G,F_p) 作为代数有限生成；本版本仍列题，编目不能替代全面开放性证明。
- [Castellano–Zalesskii, Subgroups of pro-p PD3-groups](https://www.boa.unimib.it/retrieve/e39773b7-6571-35a3-e053-3a05fe0aac26/Pro_p%20subgroups%20_%20IRIS.pdf) — Proposition 1.1(3)，印刷页3；作者论文，全文定位。非平凡自由 pro-p 群的 cd_p=1；故 H^n=0 (n≥2)，秩d有限时正次数部分是平方零的 F_p^d，而非d≥2时的外代数。
- [Cook, Bieri–Eckmann criteria for profinite groups](https://arxiv.org/abs/1412.1703) — v2 摘要；预印本，仅摘要。讨论 profinite FP_n 判据；此轮只核摘要，不把 FP∞ 同上同调环有限生成等同。

**本轮实际搜索路径**：

- `web.system2_search_query`：`"Kourovka" "21.78" cohomology`（2026-11-26）。
- `web.system1_search_query`：`pro p group cohomology ring FP infinity finitely generated Kropholler`（2026-11-26）。
- `web.system2_search_query`：`"pro-p" "cohomology" "finite generation" (site:github.com OR site:mathoverflow.net OR site:zenodo.org)`（2026-11-26）。
- `web.system1_search_query`：`"free pro-p" "cohomological dimension" "one"`（2026-11-26）。

**量词及复核边界**：一般 pro-p 群：检索范围内仅核到原问题与有限性/同调维数背景；不由零命中断言开放。；自由 pro-p 群背景描述：d≥2 时 cd=1 与外代数有非零二次部分不相容。

**待复核**：一般无限同调维数的 FP∞ pro-p 情形仍需追踪作者文献；本轮未做环生成元分类或证明搜索。


### QX-P-002398｜Kourovka 21.79：是否存在所有非平凡元素都被扭曲的有限生成左序群

**现版**：`0840f0ce4999e63a`。主研究问题未找到一般解；补上非平凡群条件。与000978为强化关系，不能按同题合并。

- **P1 · 补全量词**：旧卡“未显式要求群非平凡” → 写明 G≠1；左序性随后保证非平凡元素为无限阶。

**查重正文比较**：

- `QX-P-000978`（`5f10cf0070ad14d3`）：**特例/强化**。000978恰有一个非平凡共轭类的性质强于本题全元素扭曲。在非平凡左序群中g无限阶；若tgt⁻¹=g²，用二进制递推写g^n可得词长O(log n)，所以每个g扭曲；反向未建立。

**直接证据与范围**：

- [Kourovka Notebook v50](https://arxiv.org/pdf/1401.0300v50) — 21.79–21.80，印刷页191；问题集／原出处，全文定位。21.79 问有限生成左序群所有非平凡元素扭曲；21.80 问仅一个非平凡共轭类。非有限生成群的扭曲在某个有限生成子群内定义。
- [Fedorynski–Lodha](https://arxiv.org/abs/2509.09856) — v1 摘要；预印本，仅摘要。G_rho 的不可有限呈示、均匀单性等性质不等于每个非平凡元素扭曲。
- [本包题面的量词核对](https://www.qunxingmath.org/p/QX-P-002398/) — 随包 card_rev 0840f0ce4999e63a；题面；本次数学核对，本包正文。按未排除 G=1 的字面存在量词，平凡群真空满足；应明确 G≠1，避免把退化例视为研究解。

**本轮实际搜索路径**：

- `web.system2_search_query`：`"Kourovka" "21.79" distorted`（2026-11-26）。
- `web.system1_search_query`：`finitely generated left orderable group every nontrivial element distorted Lodha Navas`（2026-11-26）。
- `web.system2_search_query`：`"left orderable" "distorted" (site:github.com OR site:mathoverflow.net OR site:aixiv.org)`（2026-11-26）。

**量词及复核边界**：按研究意图的非平凡有限生成左序群：原题在最新问题集中列出，现有构造性质不足以推出全元素扭曲。；未排除平凡群的字面题面：G=1 有限生成且左可序，非平凡元素全称条件真空。

**待复核**：核查21.80所印“推出21.78”是否原问题集交叉编号笔误；本轮直接证明的关系是21.80⇒21.79，不修改原引用。


### QX-P-002400｜Kourovka 21.84：SL_n(Z) 是否具有柔性置换稳定性

**现版**：`1668a1326d75e566`。核对 Kourovka 21.84 及 Bowen–Burton 条件结果；未见可验证的 SL_n(Z) 全范围柔性置换稳定性结论。

- **P1 · 查重附带纠错**：旧卡“参考000979把 flexible 解释为放宽生成集大小” → 参考卡应改为允许扩大置换集合/作用载体，具体归一化及n到m的量词以原定义为准。

**查重正文比较**：

- `QX-P-000979`（`0b36acdd552f0d7a`）：**相关但不等价**。SL_n(Z)这一具体群族是否flexible P-stable，与任意群从flexible推出严格P-stable不同。参考卡flexible的生成集解释有误，应是置换作用载体可扩大。

**直接证据与范围**：

- [Kourovka Notebook v50](https://arxiv.org/pdf/1401.0300v50) — 21.84–21.85，印刷页191；问题集／原出处，全文定位。柔性稳定允许扩大有限置换作用的载体；不是改变有限生成集大小。
- [Bowen–Burton](https://arxiv.org/pdf/1906.02172) — v3，引言主结果；预印本，全文定位。PSL_d(Z)、d≥5 的特定 flexible sofic-approximation 假设导向非sofic群；不能倒推 SL_n(Z) 的普通柔性 P-stability。

**本轮实际搜索路径**：

- `web.system2_search_query`：`"SL_n" "flexible" "stability"`（2026-11-26）。
- `web.system1_search_query`：`SL integer flexible permutation stability Bowen Burton 2026`（2026-11-26）。
- `web.system2_search_query`：`"flexible" "SL" "permutation stability" (site:github.com OR site:mathoverflow.net OR site:zenodo.org)`（2026-11-26）。

**量词及复核边界**：SL_n(Z) 柔性 P-stability：所核条件定理对象和近似范畴不同，不支持原题全解。

**待复核**：需分n核查已知低秩特例；本轮不把PSL条件结论改写成SL全称结论。


### QX-P-002401｜Lang–Trotter 猜想：非 CM 椭圆曲线固定 Frobenius 迹的精确素数计数

**现版**：`cc7b055d8b8f9e1b`。固定迹 Lang–Trotter 主问题未找到可验证的全面解决；旧卡 Sato–Tate 密度归一化差4倍。

- **P1 · 修正公式**：旧卡“密度(2/π)√(4-u²)du” → 改为(1/(2π))√(4-u²)du；对应二阶矩1。

**直接证据与范围**：

- [Akbary–Parks, On the Lang–Trotter conjecture for two elliptic curves](https://arxiv.org/pdf/1711.00176) — v2，Conjecture1.1，页1；预印本／原题标准重述，全文定位。先重述单条非CM曲线固定迹计数及常数；其平均/双曲线进展不能替代每条固定曲线的精确渐近。
- [Serre, Sato–Tate 讲义](https://www.college-de-france.fr/media/professeurs-honoraires/UPL47720_cours_Taiwan_avril__10juin_2011_.pdf) — §8.1.5.2及§8.2；检索提取公式；作者讲义，检索定位公式。u=a_p/√p∈[-2,2] 的概率密度是 (1/(2π))√(4-u²) du。
- [本包归一化核对](https://www.qunxingmath.org/p/QX-P-002401/) — 随包 card_rev cc7b055d8b8f9e1b；已知结果 Sato–Tate 段；本次数学核对，本包正文。旧系数2/π使总质量与二阶矩都为4；正确系数使二者为1。
- [2026 Lang–Trotter 相关论文线索](https://arxiv.org/abs/2608.17639) — 检索命中v2(2026-11-09)，摘要入口DisabledError；预印本线索，仅检索摘要／入口不可达。处理固定Frobenius域的上下界，区别于固定迹精确渐近；本轮未取正文，不采作原题解决。

**本轮实际搜索路径**：

- `web.system1_search_query`：`"Lang Trotter" "Frobenius" 2026 non CM`（2026-11-26）。
- `web.system1_search_query`：`"Lang Trotter" "sqrt" "constant" non CM`（2026-11-26）。
- `web.system1_search_query`：`"Sato Tate" "1/2" "pi" "sqrt" Sutherland`（2026-11-26）。
- `web.system2_search_query`：`"Lang Trotter" site:github.com OR site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science 2026`（2026-11-26）。
- `web.system1_search_query`：`Sutherland Sato Tate distribution trace [-2,2] 1/(2pi)`（2026-11-26）。
- `web.system1_search_query`：`"Lang Trotter" conjecture 2026 non CM fixed trace`（2026-11-26）。
- `web.system1_search_query`：`"Lang-Trotter conjecture" "2026" non-CM`（2026-11-26）。

**量词及复核边界**：非CM固定曲线固定迹精确渐近：查到条件上界、平均和其他Lang–Trotter变体，未覆盖原量词。；Sato–Tate背景公式：[-2,2]上需用1/(2π)，而非2/π。

**待复核**：最新固定迹主问题的期刊引文链未穷尽；2608.17639完整正文未取得。


### QX-P-002403｜构造点数少于 200 且覆盖参数大于 5 的斯坦纳系统

**现版**：`1fc78d1336f5797c`。原题是n<200且6≤t≤9的显式Steiner系统。新检出S(6,7,23)若干对称性类的排除声明，但不解一般构造题。

- **P1 · 补充部分进展**：旧卡“未列2026 issue3700的排除计算” → 补充自同构类排除线索并明确未独立复算；QX-P-001821的S(6,9,45)仍是候选特例。

**查重正文比较**：

- `QX-P-001821`（`da08ab950acc2591`）：**特例/强化**。S(6,9,45)符合本题n<200、6≤t≤9要求；构造它可给本题一个解，但证明此参数不存在并不排除所有参数，不能合并。

**直接证据与范围**：

- [Epoch Large Steiner Systems](https://epoch.ai/frontiermath/open-problems/large-steiner-systems) — 题面 n>q>r>5,r<10,n<200；状态栏目；原题页面，全文定位。要求列出全部区组并可检验，不是只给必要可除性。
- [Keevash, The existence of designs](https://arxiv.org/html/1401.3665v4) — 引言存在性定理；预印本，全文定位。固定t,k、充分大v的渐近存在性，未给满足本题v<200的具体系统。
- [Formal Conjectures issue3700](https://github.com/google-deepmind/formal-conjectures/issues/3700) — 2026-04-06 issue正文；本次API读取；作者社区／计算声明，已取issue正文。报告S(6,7,23)对M23、AGL(1,23)、Z23⋊Z11、D23若干自同构类的排除，Z23分支仍未闭；这是计算声明，未独立运行。
- [Formal Conjectures SteinerSystem.lean](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/Wikipedia/SteinerSystem.lean) — large_steiner_systems；blob e57ff36f646eb3cc71a522ec6bfaf9956b04a2c3；作者仓库，已取代码未重跑。目标仍为sorry；已有小t样例不是t≥6构造。

**本轮实际搜索路径**：

- `web.system2_search_query`：`"Large Steiner Systems" "200"`（2026-11-26）。
- `web.system1_search_query`：`"Steiner" "6" "200" "construction" 2026`（2026-11-26）。
- `web.system2_search_query`：`"large Steiner" (site:github.com OR site:mathoverflow.net OR site:aixiv.org)`（2026-11-26）。

**量词及复核边界**：所要求有限范围的显式系统：未取得可验证的完整区组表。；S(6,7,23)对称性限制：新增计算排除声称；范围仅指定自同构类，尚未复现。

**待复核**：取得排除程序、精确版本和机器证书；不能把某些自同构类不存在等同无设计。


### QX-P-002404｜随机稳定婚配的稳定匹配数是否集中到期望

**现版**：`bcd84f273a2e5197`。题面随机模型与原Lennon–Pittel下尾猜想对应；修正样本空间、强弱关系和“集中到期望”的标题。

- **P1 · 修正定义与标题**：旧卡“|Ω_n|=(n!)²，单点概率(n!)^-2；题名集中到期望” → 改为(n!)^(2n)、(n!)^(-2n)；题名写为稳定匹配数的趋零比例下尾界。
- **P1 · 修正逻辑**：旧卡“固定正比例高概率下界较弱” → 固定c下界⇒每个ε_n→0下界，反向不成立。

**查重正文比较**：

- `QX-P-000438`（`70083a2be2d0bec8`）：**相关但不等价**。000438讨论带d_n参数模型的二阶矩及双曲曲面阈值，本题是完整iid偏好模型的每个ε_n→0下尾猜想；有界二阶矩只给正概率下界，不给高概率集中。

**直接证据与范围**：

- [Lennon博士论文](https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1194991095&disposition=inline) — 摘要ii及式(6.0.1)，印刷页117（PDF第126页）；原作者论文，全文定位。n男n女的2n张独立均匀排名表共有(n!)^(2n)个剖面；猜想为任意ε_n↓0有P(S_n≥ε_n E S_n)→1。
- [Formal Conjectures LennonPittelStableMatchings](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/Paper/LennonPittelStableMatchings.lean) — uniformProfile、positive/antitone epsilon及主定理；作者仓库，已核定理对应、未重跑。编码逐人偏好均匀独立，主问题sorry；未运行Lean。
- [本轮有限模型核验](https://www.qunxingmath.org/p/QX-P-002404/) — 本包数学段及local_checks.py；n=2；本次数学／有限计算核对，独立有限算例通过。自写程序枚举2^4=16种剖面；旧(n!)²给4。固定c>0的高概率下界强于每个趋0系数的下界；均不等价S_n/E S_n→1。

**本轮实际搜索路径**：

- `web.system2_search_query`：`"Lennon" "Pittel" "stable" "number" conjecture`（2026-11-26）。
- `web.system1_search_query`：`"random stable matchings" "epsilon" "expectation" conjecture`（2026-11-26）。
- `web.system2_search_query`：`"Lennon Pittel" (site:github.com OR site:mathoverflow.net OR site:zenodo.org)`（2026-11-26）。

**量词及复核边界**：Lennon–Pittel下尾猜想：本次原式与代码一致，无全解证明。；样本空间与强弱关系：2n个独立排列；旧卡还把固定正比例与趋0比例的蕴含方向写反。

**待复核**：本轮未重做高阶矩估计；000438的参数d_n/双曲线阈值模型应另核原文，不合并。


### QX-P-002405｜Leopoldt 猜想：任意数域和素数的 p 进调节子非零

**现版**：`17d409def4c8a40d`。Leopoldt一般猜想未判解决；题卡整数线性独立和按局部迹组成的调节子均不忠实，需要重写。

- **P1 · 重写等价表述**：旧卡“基本单位的对数对整数系数独立；用各局部迹做方阵行列式” → 先定义λ_Qp: Q_p⊗_Z O_K^×→∏_{v|p}K_v，再要求其单射/像的Q_p维数为r；或先对E/μ(K)作Z_p完备化。原λ定义域尚非Z_p模，不能直接写rank_Zp imλ或Q_p⊗_Zp λ；逐局部域迹矩阵也不能替代此映射。

**直接证据与范围**：

- [Ferri–Johnston](https://arxiv.org/html/2301.05700v2) — §1定义λ与Λ、Theorem1.1，2026-03-23 v2；预印本／已刊版本线索，全文定位。正确条件是Z_p⊗O_K×到主单位群的单射，或Q_p线性秩等于r1+r2−1。阿贝尔Q或虚二次扩张已知成立。
- [本次单位与局部迹核对](https://www.qunxingmath.org/p/QX-P-002405/) — 随包card_rev 17d409def4c8a40d；调节子和线性独立段；本次数学核对，反例核对（针对错误表述）。整数系数独立不能替代Q_p独立。K=Q(√5),p=3惰性，ε=(1+√5)/2的范数−1，Tr(log_3 ε)=log_3(−1)=0；按旧单局部迹矩阵会得0，而该阿贝尔域已满足Leopoldt。

**本轮实际搜索路径**：

- `web.system2_search_query`：`"Leopoldt" "conjecture" 2026`（2026-11-26）。
- `web.system1_search_query`：`"Leopoldt" "p-adic logarithms" "linearly independent"`（2026-11-26）。
- `web.system2_search_query`：`"Leopoldt" (site:github.com/google-deepmind OR site:aixiv.org OR site:zenodo.org)`（2026-11-26）。
- `web.system2_search_query`：`"Leopoldt" "counterexample" "2026"`（2026-11-26）。

**量词及复核边界**：Leopoldt原猜想：Ferri–Johnston给群表示与显式单位的子类进展，不是任意数域/素数。；题卡等价式：缺Q_p/Z_p系数与适当扩张的定义域；根单位被对数杀掉，逐局部域取迹还可丢失独立方向。

**待复核**：对旧Mihăilescu声明的完整证明不做认可；需另核修订/撤稿与专家意见。此轮重点已落在可确认的题面错误。


### QX-P-002407｜Littlewood 多项式在单位圆上的渐近平坦性（2026 直接解声称待独立核验）

**现版**：`a76282546b61e321`。保留完整超平坦声称待核。取得官方076范围说明，确认现有形式化终点只覆盖上界/有限p的Lp平坦性，不能充当双边一致超平坦证明。

- **P0 · 细化形式化覆盖**：旧卡“有Lean或Comparator容易被误读为完整超平坦已核” → 分别登记上界、有限p的Lp、单位圆一致下界；最后一项仍需独立证据。

**直接证据与范围**：

- [OpenAI Ultraflat real Littlewood polynomials](https://github.com/openai/math/blob/main/preprints/Ultraflat-real-Littlewood-polynomials-October-5-2026/ultraflat-real-littlewood-polynomials.pdf) — 2026-10-05稿；本轮只取得GitHub文件页与摘要；作者预印本，文件元数据／检索摘要。原题需要对所有充分大N、同一±1多项式在整个单位圆上同时满足上下1±ε界；PDF全文本轮未审。
- [OpenAI形式化范围说明076](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/076.md) — Lean scope；commit adc7f1241b42e322a6451854ab7e4b4c146bf78a 已重新读取；blob dcd69b52ed11c3e254e47d2f8f784a76b42344fd；作者仓库，已取得范围说明。明确形式化是渐近最小上界及每个有限p的Lp结果，不包括uniform lower bound。
- [OpenAI Comparator挑战](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/AsymptoticallyMinimalLittlewood.lean) — 上界主定理；blob7323fc6a4121e0c3686e312bb6e5c7720490c56d；作者仓库，已核定理对应、未重跑。已核挑战所陈述的是上界；Challenge的sorry属于目标占位，本身不是对Solution有漏洞的证明。
- [El Abdalaoui 的相冲突声明](https://arxiv.org/abs/2504.21499) — v1,2025-04-30；并查2509.04212v1；预印本声明，摘要与版本核对。宣称排除某些Lα平坦性，从而与2026超平坦声称发生冲突；本轮未裁判两套完整论证。
- [Mathcommunity复核记录](https://mathcommunity.github.io/oai-math-revised/papers/Ultraflat-real-Littlewood-polynomials-October-5-2026/) — 2026-10-26 comparator记录与评审限制；外部社区验证报告，已读搜索返回的报告文本；未独立打开全文。第三方报告的是上界/Lp核验；仍明确缺定理翻译的人类专家审查。

**本轮实际搜索路径**：

- `web.system1_search_query`：`"Ultraflat real Littlewood polynomials" OpenAI`（2026-11-26）。
- `web.system2_search_query`：`"Littlewood" "1-epsilon" "ultraflat" review`（2026-11-26）。
- `web.system2_search_query`：`"Littlewood" "ultraflat" (site:mathoverflow.net OR site:aixiv.org OR site:zenodo.org OR site:eulersolve.com)`（2026-11-26）。

**量词及复核边界**：双边一致超平坦主问题：存在直接正面声称与相反声明，官方形式化范围不足以消解冲突。；上界与有限p的Lp变体：取得官方代码/说明及外部验证报告；本次未重跑。

**待复核**：核完整PDF中的下界定理与量词；审El Abdalaoui反向论证；若复现只报告实际验证终点。


### QX-P-002408｜每个有限连通顶点传递简单图是否都有哈密顿路

**现版**：`c555ff1c2eb98a8a`。新增2026年多对数度数Cayley图Hamilton圈进展及Lean验证报告；全体连通顶点传递图Hamilton路尚不能据此晋级。

- **P0 · 补充遗漏进展**：旧卡“旧卡主要前沿为d>n^(1−c)” → 增加C(log n)^13/loglog n的Cayley特例及精确验证级别；不改全题已解决。
- **P2 · 修复公式乱码**：旧卡“全称量词附近含“本机文件 quad”” → 恢复标准LaTeX空白命令并核正文渲染。

**直接证据与范围**：

- [Bedert–Draganić–Müyesser–Pavez-Signé](https://arxiv.org/html/2603.08675v2) — Theorem1.2，2026-04-20 v2；预印本，全文定位。充分大n、Cayley、d>n^(1−c)，c≥1/200，有Hamilton圈。
- [Shengtong Zhang, lovasz-opus](https://github.com/shengtongz/lovasz-opus/blob/ee0085ddec79996279c7b52044659032e5cf8431/Solution.lean) — Lovasz.hamiltonian_of_polylog_degree；commit ee0085ddec79996279c7b52044659032e5cf8431；作者仓库，已核定理对应、未重跑。存在绝对C,n0，连通Cayley图n≥n0且d≥C(log n)^13/loglog n时Hamiltonian；Solution由main_proof给出，已核声明与Mathlib对象对应。
- [lovasz-opus验证记录](https://github.com/shengtongz/lovasz-opus/blob/ee0085ddec79996279c7b52044659032e5cf8431/VERIFICATION.md) — 2026-09-25记录；Lean v4.35.0-rc2；他人形式化验证报告，已取文档。作者报告49模块编译、Comparator及独立内核接受，仅propext/choice/Quot.sound；本次未运行。
- [Matija Bucić作者研究页](https://sites.google.com/view/matija-bucic/research) — Working Drafts 2026+；作者页面，检索摘要。作者确认Cayley log^13 Lean进展，并列vertex-transitive推广与asymptotic草稿；后两者未在本轮逐定理核查。

**本轮实际搜索路径**：

- `web.system1_search_query`：`Lovasz Hamiltonian vertex transitive conjecture 2026 Bedert Draganić`（2026-11-26）。
- `web.system2_search_query`：`"Hamilton" "Cayley" "1/200" Lovasz`（2026-11-26）。
- `web.system2_search_query`：`"Lovasz" "Hamiltonian" site:github.com OR site:mathoverflow.net OR site:zenodo.org`（2026-11-26）。
- `web.system1_search_query`：`"Hamilton cycles" "polylogarithmic degree" "2026"`（2026-11-26）。

**量词及复核边界**：全部有限连通顶点传递图Hamilton路：度数门槛和Cayley假设仍限制范围；almost-Hamiltonian也不是spanning Hamilton路。；多对数度数Cayley特例：已取得真实终点代码与外部验证记录；未独立复现。

**待复核**：独立重跑固定提交及全依赖；核作者新vertex-transitive工作稿的最终量词，不从网页摘要升级。


### QX-P-002410｜曼德博集合是否局部连通

**现版**：`3d08e1dcc15e5154`。修正旧卡把“非局部连通”误列已知的标题，并补2026 parabolically bounded primitive组合类型的MLC进展。

- **P1 · 修正错误状态文字**：旧卡“[KNOWN] 全局连通但非局部连通” → 改为已知全局连通；局部连通全称命题未由此推出。
- **P1 · 补充论文**：旧卡“漏2606.27272” → 加入TheoremC精确组合范围；更新Feigenbaum论文发表信息并注明本轮正文403。
- **P2 · 修复公式**：旧卡“复数集符号含“本机文件 C:”” → 恢复\mathbb C。

**直接证据与范围**：

- [Kahn–Kapiamba–Lyubich](https://arxiv.org/html/2606.27272v1) — §1.1 TheoremsA–C，2026-06-25；预印本，全文定位。prime primitive types组成的parabolically bounded族有beau bounds；再加puzzle Teichmüller控制导出该族rigid，见TheoremC。不覆盖所有参数。
- [Dudko–Lyubich, MLC at Feigenbaum points](https://pmihes.centre-mersenne.org/articles/10.5802/pmihes.2/) — PMIHES143(2026),97–141；2026-06-02在线；已刊元数据，摘要可达／正文403。检索可见已发表元数据和bounded-type结论；实际打开403，未复读发表版。
- [Formal Conjectures Mandelbrot](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/Wikipedia/Mandelbrot.lean) — MLC；固定提交9097e2f90e66d2f6244209cb1c07f7120d17ec53；作者仓库，已核定理对应、未重跑。原目标为LocallyConnectedSpace mandelbrotSet，仍sorry；density of hyperbolicity是另一个声明。
- [本包题面检查](https://www.qunxingmath.org/p/QX-P-002410/) — 随包定义与[KNOWN]小标题；本次正文核对，本包正文。“全局连通但非局部连通”字面上声称反例；实际下文只说明不能从连通推出局部连通，标题错误且公式有本机文件乱码。

**本轮实际搜索路径**：

- `web.system1_search_query`：`Mandelbrot local connectivity conjecture 2026 Dudko Lyubich`（2026-11-26）。
- `web.system2_search_query`：`"Mandelbrot" "local connectivity" "bounded type" 2026`（2026-11-26）。
- `web.system2_search_query`：`"Mandelbrot" "local connectivity" site:github.com OR site:aixiv.science OR site:mathoverflow.net OR site:prove2.me`（2026-11-26）。
- `web.system1_search_query`：`"MLC for parabolically bounded primitive renormalization"`（2026-11-26）。

**量词及复核边界**：MLC全称问题：2026 TheoremC仍是真子类，公开社区任务页面不等于证明。；新组合类型：parabolically bounded prime primitive类型的rigidity已定位原定理。；旧卡标题：不能把一般拓扑蕴含不成立写为Mandelbrot已非局部连通。

**待复核**：新稿依赖的parabolic-tail Teichmüller控制证明可续查；未重证全部73页。


### QX-P-002411｜能否在流形上的层范畴上建立还原 de Rham 上同调的模型结构

**现版**：`ba9abc439dc441c3`。现题把普通层范畴和复形层范畴混用，公式失去类型意义。修正到Ch(Sh(M,R))后的基本模型结构已有Hovey定理，不能继续作为未解的存在性缺口。

- **P1 · 重写并拆分题面**：旧卡“在Sh(M,Ab)上以准同构为弱等价，Hom(underline Z,Ω^n[n])还原deRham” → 将核心基本版本改为Ch(Sh(M,R))与Ω^•；注明已知定理，若保留开放研究题须明确额外几何要求。

**直接证据与范围**：

- [Hovey原问题列表](https://www-users.cse.umn.edu/~tlawson/hovey/model.html) — Problem2；原作者问题页，全文定位。原问题是探索manifold sheaves、deRham、Floer、quantum cohomology的宽泛纲领，没有题卡自行添加的Sh(M,Ab)准同构和Ω^n[n]公式。
- [Hovey, Model category structures on chain complexes of sheaves](https://arxiv.org/pdf/math/9909024) — Theorem2.2、Corollary2.3(a)，印刷页5；作者论文，全文定位。Grothendieck阿贝尔范畴A的Ch(A)有injective模型结构，弱等价为准同构，同伦范畴为D(A)；环化空间的模层适用。
- [David White对Hovey问题的更新](https://mathoverflow.net/questions/424613/mark-hoveys-open-problems-in-the-theory-of-model-categories) — 2022回答Problem2部分；专家社区说明，已读对应回答。仍讨论更宽的几何/物理方向；不能把这段解读成否认标准复形层模型结构。
- [本包类型核对](https://www.qunxingmath.org/p/QX-P-002411/) — Sh(M,Ab)、准同构、Hom及Ω^n[n]段；本次数学核对，本包正文。普通层无复形度数/平移；正确deRham对象是整个Ω_M^•，可写HdR^n(M)=H^n RΓ(M,Ω_M^•)=Hom_D(underline R,Ω_M^•[n])。

**本轮实际搜索路径**：

- `web.system1_search_query`：`"Hovey" "sheaves over a manifold" model structure de Rham`（2026-11-26）。
- `web.system1_search_query`：`"injective model structure" "Grothendieck" "complexes" Hovey sheaves`（2026-11-26）。
- `web.system2_search_query`：`"model category structures on chain complexes of sheaves" Hovey`（2026-11-26）。
- `web.system2_search_query`：`"de Rham" "sheaves" "model structure" site:github.com OR site:mathoverflow.net OR site:zenodo.org`（2026-11-26）。

**量词及复核边界**：当前题面：使用普通层范畴却要求准同构及移位复形，表达式不成立。；修正后的标准复形层模型结构：该基本版本由Hovey Thm2.2/Cor2.3(a)解决；不等于回答全部Floer/quantum纲领。

**待复核**：确定题卡真正希望保留的额外结构（如单体兼容、自然几何对象或Floer/quantum），不把修正文法后已知定理重新包装成开放问题。


### QX-P-002412｜Meyniel 猜想：每个连通 n 顶点图的警察数 c(G)=O(√n)

**现版**：`8467d5c86666f951`。补到2026以vertex-cover数为参数的上界；不改变n顶点一般Meyniel猜想。

- **P1 · 补充部分结果**：旧卡“未列2602.07435” → 增加以vc(G)替代n的次线性上界；不宣传soft Meyniel已解。

**直接证据与范围**：

- [Baird–Bonato survey](https://arxiv.org/abs/1308.3385) — v1摘要与原题重述；作者综述，仅摘要。主问题c(G)=O(√n)，量化所有连通图。
- [Bose等，Cops and robber in graphs with bounded vertex cover number](https://arxiv.org/html/2602.07435v1) — Theorem1及Theorem2，2026-02-07；预印本，全文定位。得到cop(G)≤vc(G)/2^((1−o(1))√log vc(G))，及更一般移除集参数化；不是普遍√n上界。
- [Formal Conjectures Meyniel](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/Wikipedia/MeynielConjecture.lean) — meyniel_conjecture及variants.soft；作者仓库，已核定理对应、未重跑。两主目标均sorry；有限图游戏定义含每轮可停留。

**本轮实际搜索路径**：

- `web.system1_search_query`：`"Meyniel conjecture" 2026 cop number general upper bound`（2026-11-26）。
- `web.system2_search_query`：`"Meyniel" "cop number" "sqrt" site:github.com OR site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science`（2026-11-26）。
- `web.system2_search_query`：`"cop number" "n/2" "vertex cover" 2026`（2026-11-26）。

**量词及复核边界**：一般Meyniel上界：已核2026论文仍把一般最优界描述为n的次线性界；本轮未见完整证明。；vertex-cover参数化：新增主定理精确适用范围已核。

**待复核**：本轮未复现图游戏算法或全称形式化；所有顶点传递特例不能代替任意连通图。


### QX-P-002413｜验证最小 Mills 常数的超越性：Saito 条件定理与 Alpöge RH 证明的组合

**现版**：`773adf4b6cb5a72f`。本轮核到11月21日RH外部联合认证及11月26日短版多内核记录；结合Saito Thm1.8，最小Mills常数超越性可列为依外部认证定理所得的已证推论。本次未独立重跑Lean或形式化组合。

- **P0 · 更新证据和状态建议**：旧卡“claimed/weak，仅待核RH链” → 可改为原题已证（依外部RH认证与Saito条件定理）；单独保留本次未重跑、组合形式化未执行。

**查重正文比较**：

- `QX-P-000181`（`c5975162cfb2d07f`）：**相关但不等价**。000181量化所有有理r>1，问floor(r^n)无穷多次为素数；本题最小实数A使floor(A^(3^k))每次为素数且问A超越，不存在已核等价。

**直接证据与范围**：

- [Saito, Transcendency of variants of Mills’ constant](https://arxiv.org/html/2508.16068v3) — 2025-12-07 v3；§1定义ξ(3^k)、Theorem1.8及其前DH定义；与旧摘要区分；作者预印本，已核定理与定义对应。定理直接为DH⇒最小Mills常数超越，并明确RH⇒DH；不是只证明存在某个造素数常数。
- [Lean FRO / Mathlib联合声明](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) — 2026-11-21认证声明；独立形式化认证报告，已读全文。声明核对标准Mathlib RH陈述，编译/Comparator及独立内核检查通过。此为他人认证，本轮没有重跑。
- [Michael Rubinstein验证页](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/) — 2026-11-25/26 compact proof verification；独立数学家验证报告，已读记录。短版794模块，五个声明，六内核与Comparator的通过记录；是新的外部复核证据。
- [Formal Conjectures Mills](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/Wikipedia/Mills.lean) — 本轮取得文件；最小值/无理性等目标；作者仓库，已取得代码未重跑。该文件未给完整Mills超越性组合；不能用目录缺项否定外部认证后的数学推论。

**本轮实际搜索路径**：

- `web.system1_search_query`：`"Alpöge" "Riemann Hypothesis" Lean`（2026-11-26）。
- `web.system2_search_query`：`"Mills constant" "Saito" transcendental 2026`（2026-11-26）。
- `web.system2_search_query`：`"Mills" "transcendental" (site:mathoverflow.net OR site:zenodo.org OR site:github.com)`（2026-11-26）。
- `web.system2_search_query`：`Mills constant least A floor A^(3^n) transcendental Saito Theorem 1.8 Riemann Hypothesis`（2026-11-26）。

**量词及复核边界**：最小Mills常数的超越性：基于本轮可读的外部RH认证，应用已核对定义的Saito Thm1.8；这一数学分类不声称本会话重验RH内核或重证Saito全文。明确逻辑链：已认证RH⇒DH（σ>1/2无零点，σ=1/2由N(T)=O(T log T)）⇒Saito v3 Theorem1.8，且ξ(3^k)与卡中最小Mills常数同定义。；端到端Lean组合验证：本轮未编译、未运行Comparator，也未提交Mills超越性组合定理。

**待复核**：若验收要求本机端到端形式化，应固定RH短版、核#print axioms，并实现Saito定理到最小Mills定义的组合；本轮范围为初查，未执行此复现。；历史论文包括2025-12-07 v3摘要仍写无条件超越性开放，那是2025发表时状态；本轮推论由v3条件定理与2026外部RH认证组合得到，不能只凭摘要状态或库内旧标签判断。


### QX-P-002417｜有限 Morley 秩连通群在有限 Morley 秩单群上的忠实不可约作用是否只能是共轭作用

**现版**：`6b404c29b20fe8de`。旧卡把“单”仅定义为无真非平凡可定义正规子群，漏掉研究语境的非交换限制；其字面版本有标量作用反例，不能当作反驳作者原意。

- **P1 · 补全假设**：旧卡“simple仅指无非平凡真可定义正规子群” → 明确S为无限非交换单群，作用为群自同构作用，并对照原稿语境；保留字面反例作为修订理由。
- **P1 · 新增查重关系**：旧卡“仅提21.20/21.21，遗漏000968” → 增加000968 rev4d79ee91ef784476为加幂零真子群条件的特例，暂不合并。

**查重正文比较**：

- `QX-P-000968`（`4d79ee91ef784476`）：**特例/强化**。000968另加S无限、M非平凡及每个真可定义子群幂零；修复simple非交换语境后是本题限制子类，不能合并。

**直接证据与范围**：

- [Berkman–Borovik](https://arxiv.org/html/2405.07307v2) — §1.5定义、§1.10仿射/regular类型、§1.12 Conjecture4；作者预印本，全文定位。原研究语境把交换目标与simple目标分开；猜想要求忠实不可约作用为共轭。题卡独立摘录的定义未保留这一排除。
- [本次定义反例](https://www.qunxingmath.org/p/QX-P-002417/) — 随包card_rev 6b404c29b20fe8de；单群定义；本次数学核对，字面反例／双人逻辑复核。在ACF0中S=(K,+)，M=K×标量作用；S无真非零可定义子群，M连通，作用忠实不可约，却非内共轭（S交换，内共轭均平凡）。有限Cp与M=1也暴露退化遗漏。
- [新增库内候选000968](https://github.com/qunxingmath-org/qunxing-data/blob/main/problems/000/QX-P-000968.text.md) — current card_rev4d79ee91ef784476；Kourovka21.19摘录；库内正文，已取得双方正文。已读正文与meta：在正确simple语境下加每个真可定义子群幂零的限制，是Conjecture4的真子类，不同题。

**本轮实际搜索路径**：

- `web.system1_search_query`：`"Berkman" "Borovik" "Conjecture 4" simple irreducible`（2026-11-26）。
- `web.system2_search_query`：`"Morley rank" "faithfully" "irreducibly" "simple" 2026`（2026-11-26）。
- `web.system2_search_query`：`"Morley rank" "Conjecture 4" site:github.com OR site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science`（2026-11-26）。

**量词及复核边界**：按题卡显式定义的全称命题：标量作用提供字面反例；需加非交换（并明示无限等研究约定）。；修正后的Berkman–Borovik猜想：2026相关代数识别和高传递结果不覆盖该全称作用分类。

**待复核**：核作者对simple的全局惯例并修订卡中独立定义；不能宣传已反驳作者猜想。


### QX-P-002422｜Nagell–Ljunggren 猜想：哪些多重几何级数是整数完全幂？

**现版**：`cf05a35301ad2332`。重要版本更新：本轮已读Wang v1的Nagell–Ljunggren全解声明；当前v2已不含该节，不能把v1结论当作最新稿明确主张。一般问题保留声明待核。

- **P0 · 修正版本与声称范围**：旧卡“旧卡v1正文不可达，v2删除情况待核” → 现已读v1§4 Theorem8，并确认v2正文没有该分类节；保留历史声称，不等同正式撤回。

**查重正文比较**：

- `QX-P-001190`（`557e8d6dada61c5c`）：**相关但不等价**。0001190是x²−2=y^p指数丢番图方程；本题是几何级数和等于完美幂，不因同用指数方程方法等价。
- `QX-P-001244`（`4c02f293288f290e`）：**相关但不等价**。0001244 Goormaghtigh是两种底数的repunit相等；本题Nagell–Ljunggren是repunit等于完美幂，量词不同。

**直接证据与范围**：

- [Wang, On ABC Triples v1](https://www.preprints.org/manuscript/202512.0286/v1) — §4 Theorem8；前置Theorem7；未经同行评审预印本，全文定位。v1直接声明Nagell–Ljunggren全部解，依赖所宣称的统一abc根式界；本轮成功读到旧卡先前403的正文。
- [Wang, On ABC Triples v2](https://www.preprints.org/manuscript/202512.0286/v2) — 最新v2，2025-12-05；正文结构、References前末段；未经同行评审预印本，版本全文对照。本轮读当前页面全文结构并查Nagell无匹配；v2保留abc主界但不含v1的§4/Theorem8分类节。并无明确撤回说明，不能擅称撤稿或已证伪。
- [Chen–Mihăilescu 2026](https://doi.org/10.1007/s11401-026-0018-7) — 检索摘要；奇素数指数与类数限制；已刊线索，仅检索摘要。只在额外素数、类数条件下排除解；不是原题全参数分类。

**本轮实际搜索路径**：

- `web.system1_search_query`：`"Nagell" "Ljunggren" 2026 proof`（2026-11-26）。
- `web.system2_search_query`：`"Nagell-Ljunggren" "x^n" "complete" Wang`（2026-11-26）。
- `web.system2_search_query`：`"Nagell-Ljunggren" (site:github.com OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net)`（2026-11-26）。

**量词及复核边界**：Nagell–Ljunggren全分类：历史v1有直接声明，最新版不再明确列此节；未核统一abc界及推导。；当前v2的出处描述：旧卡对v1/v2访问及目标所处版本应更新。

**待复核**：审统一abc根式界及v1分类推导；向发表/修订链追踪而不把仓库或预印本标题当认可。


### QX-P-002423｜附近拉格朗日猜想：核验 2026-09-23 的高维反例声称

**现版**：`b745d1e8b093b2e3`。取得官方主定理TeX，确认高维反例声称确覆盖附近拉格朗日原题；OSVerify报告不等于独立全证明或内核验证。

- **P0 · 细化原稿可达性**：旧卡“raw网页失败可能误作原稿未取得” → 已通过GitHub读取引言TeX并核定原题对应；审查级别仍为完整反例声明待核。

**查重正文比较**：

- `QX-P-001279`（`7a68cc579955d802`）：**相关但不等价**。0001279研究Euler–Chow级数与Cox环；本题是余切丛中的紧exact Lagrangian Hamilton同位。
- `QX-P-001293`（`bcb49189d73f47a5`）：**相关但不等价**。0001293是有限域三次超曲面单有理参数化次数；不存在所核的与附近拉格朗日猜想等价关系。
- `QX-P-002482`（`027084c83a40140b`）：**相关但不等价**。002482为Liouville两点相关Chowla问题；两题共同出现OpenAI成果来源不构成数学同题。

**直接证据与范围**：

- [OpenAI nearby Lagrangian counterexample](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-counterexample-to-the-nearby-Lagrangian-conjecture-September-23-2026/build/sections/introduction.tex) — 主定理Theorem main；取得blob ad83cfd73490e10560a387e00ae49ec4e6ac9773；作者预印本源码，已取得并核主定理。Q=S9×S^(N−1)，某充分大偶N，紧exact embedded L与Q微分同胚但不Hamilton同位零截面；这是真正原题反例范围。
- [OSVerify case report](https://osverify.github.io/cases/nearby-lagrangian.html) — 0 major／1 minor及Porcelli–Smith引用备注；AI审查报告，已读报告。该自动审查未报重大问题，不是学术同行完整复核；其引用定位建议为Theorem1.17,p8。
- [本包原卡形式化背景](https://www.qunxingmath.org/p/QX-P-002423/) — 随包card_rev b745d1e8b093b2e3；形式化范围段；本包线索，未独立重跑。旧卡描述main_reduction依赖拓扑输入；本轮未取得并编译全工程，不把条件规约或文件数量当无假设反例验证。

**本轮实际搜索路径**：

- `web.system1_search_query`：`"A counterexample to the nearby Lagrangian conjecture" 2026`（2026-11-26）。
- `web.system2_search_query`：`"nearby Lagrangian" "S^9" "Lean" counterexample`（2026-11-26）。
- `web.system2_search_query`：`"nearby Lagrangian" (site:osverify.github.io OR site:mathoverflow.net OR site:proofweave.org)`（2026-11-26）。

**量词及复核边界**：附近拉格朗日猜想：官方主定理确称反例，但本轮没有完整独立数学审查或等价无额外假设形式化验证。

**待复核**：复核非Hamilton同位障碍与所用稳定化/拓扑输入；运行固定提交需先审脚本，此轮未执行。


### QX-P-002425｜是否存在不能表示为 Grothendieck site 上层的 ∞-topos

**现版**：`f457b08cfe1d9901`。原问题仍只核到条件性归约；新发现出处作者错配：MO#345680提问者是Charles Rezk，Francesco Polizzi为编辑者。

- **P1 · 更正出处**：旧卡“原作者Francesco Polizzi，2019-11-10” → 改为Charles Rezk于2019-11-10提问；Polizzi为2021编辑，Campion为回答者。

**直接证据与范围**：

- [MathOverflow #345680](https://mathoverflow.net/questions/345680/whats-an-example-of-an-infty-topos-not-equivalent-to-sheaves-on-a-grothendie) — 问题署名区、原题及两回答；2019-11-10提问；原始题源，全文定位。Asked署名Charles Rezk，edited署名Francesco Polizzi；题目允许更换任意小∞-site，非当前site不拓扑即可反例。
- [Tim Campion条件性归约](https://mathoverflow.net/questions/345680/whats-an-example-of-an-infty-topos-not-equivalent-to-sheaves-on-a-grothendie#437226) — 2022-12-25回答Hypothesis/Claim；原始专家回答，全文定位。小满子范畴可容纳任意给定对象集且重新作sheaf呈现的假设⇒所有∞topos是sheaf；假设本身未证，连Spaces也待定。
- [Anel–Biedermann–Finster–Joyal II](https://arxiv.org/html/2201.01236v2) — 旧卡分类定理线索；本轮入口DisabledError；预印本线索，正文不可达。未复读全文，不将extended topology分类当任意∞topos可在小site表示的证明。

**本轮实际搜索路径**：

- `web.system1_search_query`：`"infinity-topos" "not" "Grothendieck site" 2026`（2026-11-26）。
- `web.system2_search_query`：`"non-sheaf" "topos" "cotopological"`（2026-11-26）。
- `web.system2_search_query`：`"infinity-topos" "Grothendieck" site:github.com OR site:zenodo.org OR site:aixiv.science OR site:mathoverflow.net`（2026-11-26）。

**量词及复核边界**：存在不能在任何小∞site表示的∞topos：本轮读原题与条件归约，未取得真正反例或全称否定证明。；原出处署名：旧卡把编辑者当作提问者。

**待复核**：需补2201.01236v2全文以及后续引文；不能由当前呈现的cotopological局部化推断不存在别的site。


## 第二部分：证明端点、反例声明及量词修正

### P0：Petersen 旧“独立核实”检查用错了数学模型

**题号与版本：** QX-P-002432，`d8cc649895d0600f`。

**旧卡 → 本轮变化：** 旧卡声称 Petersen 边星染色等价于局部双射顶点图同态，并用后者的弧一致和 Hall 检查宣布两张 52 顶点图已独立核实不可染。这一等价式错误，因此旧检查不能支撑“独立复算通过”的标签。

直接读取 [六作者原稿 v4](https://arxiv.org/html/2608.10028v4) 的 §1 定义、Theorem 6、Observation 10、Problem 11 和 §5.3，确认目标是边映射保持每个顶点星。取 K4 的三组完美匹配，把每组映到 Petersen 图中同一个固定顶点星的一条边，四个源顶点的星均合法。相反，有限连通图到 Petersen 图的局部双射顶点同态是图覆盖：沿目标任意一条边，各端点纤维之间都是双射，目标连通迫使全部 10 个纤维等大。因此源顶点数必须是 10 的倍数；K4 和任何 52 顶点图都不可能有这种覆盖。这个覆盖失败不能证明 Petersen 边染色失败。

本组的 `petersen_semantic_check.py` / `petersen_semantic_check.json` 已实际运行，列出 K4 六条边的映射并逐星核对。它没有读取或求解 52 图，也没有运行外部 SAT、DRAT 或 Lean。

**状态建议：** 撤销旧卡“本次独立核实”及错误等价式。原稿 Theorem 6 的 52 顶点反例、Observation 10 的作者枚举界 \(40\le n_{\min}\le52\) 作为独立的文献证据保留；本轮只完成初查，未重跑证明。循环 5 边连通反例也应另问。此外，正常 5 边染色的 3/5 颜色数须数两端星的并集，包括该边自身；旧文若只数四条旁边，最多只能有四色。

**实际路径：** `"Petersen coloring" "2608.10028"`；`"Petersen coloring" "smallest" 2026`；边映射/normal/locally bijective 特征查询；GitHub CAOS_RESEARCH；Zenodo 与 MO。取得 [Zenodo 22836612](https://zenodo.org/records/22836612) 的 v0.04 入口；最新版转跳返回 429，本轮没有重新取得旧卡所称 v0.07 完整证书。

**下一步：** 采用真正的边星映射或正常 5 边染色模型，加入 K4 正例控制，再对固定图哈希与证书做独立检查；只有该过程完成才能恢复独立验证标签。


### P0：Pierce–Birkhoff 存在完整反例声明，且覆盖当前题面

**题号与版本：** QX-P-002436，`f82709c7712af81d`。

旧卡“没有找到完整反例”已被本轮实际检索改变。[Lai–Lim–Ren, arXiv:2609.10420v1](https://arxiv.org/abs/2609.10420)（2026-09-09）明确声称反驳猜想。arXiv HTML 不可达，但取得作者仓库 `paper.tex` 全文、30 维 README、Lean 说明、主定理及关键定义。

主稿的 “The 30-dimensional lattice obstruction” 定理在 (\mathrm{Sym}_5(\mathbb R)\times\mathrm{Sym}_5(\mathbb R)\cong\mathbb R^{30}) 上给连续、二次齐次、分片二次函数；其不可能表示为任意次数实多项式的有限 max/min 组合。作者 README 称 30 维证明经人类专家检查，低维分支的检查情况不同；这是作者说明，不等于本轮独立审核或期刊接受。

已取得仓库提交 **`b8d342ab889845e7efcb9c29d964baab2250aa53`**，并按该提交重新读取 [Collaborator30Main.lean](https://github.com/7pocheR/Pierce-Birkhoff/blob/b8d342ab889845e7efcb9c29d964baab2250aa53/n=30_d=5_k=2/lean/PBCounterexample/Collaborator30Main.lean)。主端点为 `PBCounterexample.Collaborator30Main.pierce_birkhoff_counterexample30`，以及 `no_finite_max_min_representation`；显式函数的闭覆盖有 41 片。端点文件 blob SHA 为 `a2ff45ea39f40c5b3ef5d42701a1c335f9d2f3f2`，这是文件哈希，与前述仓库提交号区分。

另读的 `Basic.lean` 使用真实 `MvPolynomial` 叶子和实数 `max` / `min`，不限制次数、叶数或深度；`Semialgebraic.lean` 定义有限布尔组合的多项式不等式、闭片、全空间覆盖及片上多项式一致。因此在本次读到的定义和端点层面，确实对应题面，而非只反驳有限次数变体。尚未读取完整传递依赖或运行 `verify.sh`。

**另一题面错误：** 旧卡说“有限闭半代数覆盖上的分片多项式”可能不连续，从而比通常猜想更宽。有限闭拼接已经自动给连续性；仓库也有相应 `FiniteClosedPolynomialCover.continuous`。这不能作为排除新反例的理由。

**实际路径：** Pierce–Birkhoff 名称/有限 max-min 特征查询；system1 完整反例与 error 查询；arXiv 记录；GitHub connector 读取作者 TeX、README 和 Lean，再锁定提交。建议改为“完整反例声明待核”，并优先审核 41 片函数、符号障碍和全依赖。仓库另有四维分支，提交说明写 human expert review pending；本轮不判最小反例维数。


### P0：正特征消解新增全维声称，证书假设需要逐字核实

**题号与版本：** QX-P-002443，`bd949f050a4cc60c`；关联 QX-P-002442，`a7f4542312f61607`。

本轮检出 Chenxiao Tian 的 [arXiv:2608.20066](https://arxiv.org/abs/2608.20066)、[SSRN 7317598](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7317598) 及 [作者项目页](https://sites.google.com/view/positive-char-resolution)。作者页面声称在**完美正特征域、任意维数**上获得 canonical strong embedded resolution、principalization 和 intrinsic resolution，所列合订稿为 Parts I–IX、798 页。旧卡“未见完整证明声称”应更新为存在完整声明。

但原 arXiv 搜索摘要把终止性写为：complete state **equipped with** global replacement certificate；之后仅说进一步 formulate object-level realization。无条件存在该证书，正是必须核验的核心。作者页面和 SSRN 登记较强的全称主张，不能代替这一步证明。arXiv abs / HTML / PDF 均不可达，SSRN 直取 403，公开 Drive 只返回文件页，尚未取得 798 页正文。当前仅支持“完整证明声明待核”。

此声称即使成立，直接范围也只包含完美域。002442 允许任意正特征基域且要求不改变原函数域；不能把完美域全局消解或 [Temkin 的纯不可分扩张局部一致化](https://math.huji.ac.il/~temkin/papers/Inseparable_Local_Uniformization.pdf) 直接当作 002442 的全解。

**实际路径：** resolution / Frobenius-Hasse / 2608.20066 的名称、review/error 查询；作者站、SSRN、arXiv；打开 Drive 主稿入口。建议优先核证书全称构造、permissible 中心、终止与全局拼接。初轮曾误开 arXiv:2412.16592，返回计算机视觉论文，已明确排除，没有计作数学证据。


### P0：完美长方体“Lean 全证明”实际没有编码原题

**题号与版本：** QX-P-002431，`09f2d8ae239d4dc3`。

新增 [Jonathan Reed, Zenodo 19074228 v2](https://zenodo.org/records/19074228)（2026-03-11）完整不存在性声称。归档说使用 Lean 4，本轮实际打开其 [No Perfect Cuboids.lean](https://zenodo.org/records/19074228/files/No%20Perfect%20Cuboids.lean?download=1)，74 行，归档 MD5 `23acb5c145d377414acbe222117aeb89`。

最终 `no_perfect_cuboid_final` 仅从 (u\in\{0,1,-1\}) 和 (2(u-1)^2+1=0) 推出矛盾。代码没有长方体的四个平方方程，也没有从假设完美长方体推出这两条件的桥梁。另一个 `parity_wall_consistency` 直接假定三个边长平方模 8 分别为 4、0、1；它只证明这组假设与体对角线平方不相容。由此可明确标“已取得代码、未重跑、最终命题不等价”，不能标为全问题的独立机器证明。PDF 附件解析失败，所以还不能对整篇非形式化论证作最终裁决。

另实际读取 [nkc-daiki/perfect-cuboid-chabauty 的 PROOF_FINAL.md](https://github.com/nkc-daiki/perfect-cuboid-chabauty/blob/main/PROOF_FINAL.md)。标题和正文已明确为 partial results，仅列整数参数 (r=2,\ldots,500)；其 §4.1–4.2 用有限多个特化值反驳“只有有限例外”的逻辑也缺失统一例外数界。不能因为文件名为 PROOF_FINAL 就认作全解。对于 [2609.14526](https://arxiv.org/abs/2609.14526) 则仅取得摘要，作者自己明确限定 (m\le100) 的 2040 个纤维。

**实际路径：** perfect cuboid 名称、968 fibers 特征、GitHub、Zenodo；归档附件直接读取与作者库 connector 回退。下一步应审核真正的全体有理参数约化，以及 torsion/φ 条件的来源。


### P0/P1：量词、定义和公式错误可直接修复

| 题号 / card_rev | 旧卡问题 | 建议修复及证据 |
|---|---|---|
| 002446 / `b0efc838304f2474` | 主问是“存在步长 C”，所谓等价段却写“每个 C>0” | 改回存在 C。Hurwitz 格中不同点距离至少 1，故 0<C<1 无边，字面全称版本为假。[MO74544 原题](https://mathoverflow.net/questions/74544/the-quaternion-moat-problem)。 |
| 002449 / `228c695b0d0c14a3` | “某个 r 正则 ⇒ B(n) 正则”不是 Rado 有界性的等价式；d 的最大值可能取空集；c/d 混用 | 用“存在 B(n)，B(n)-正则 ⇒ 对所有有限色正则”，或直接用非 Rado 系数的最小避解色数 c(a)≤B(n)。若 d 为最大正则度，约定 d=0 后 d=c−1。公式中的“本机文件”须删除。[Green Problem21](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf)，本轮还直接读了 `FormalConjectures/GreensOpenProblems/21.lean`。 |
| 002428 / `5226bca9b562b944` | 位移适当的公式损坏，正文以紧集返还条件解释 metrically proper | 明确写对任意 R≥0，{g:‖α(g)ξ−ξ‖≤R} 有限；无限维 Hilbert 空间不能直接把紧集和有界集互换。[MO218145](https://mathoverflow.net/questions/218145/do-one-relator-groups-satisfy-haagerup-property)。 |
| 002441 / `d55463e53663bdff` | 标题“至少损失2”反向；最小正整数维数定义和单点维数0冲突 | 标题改“至多损失2”；采用允许0的约定，或在 Baker 可加性中排除单点因子。反链维数2需 n≥2。[Bergman Question3.2](https://arxiv.org/html/2312.12615v4)。 |
| 002448 / `bb2751222a18110a` | 将无限群 VR1 一概说成不可缩 | 无边 Γ 给自由群，标准 Cayley 图是树且 VR1 已可缩；删掉全称注释。[Zaremsky §4.5](https://zaremsky.github.io/open_problems.pdf)。 |
| 002434 / `8aeaa7bcd2d91d9d` | p(K) 定义含“本机文件”破坏 | 恢复“使每个有限平方和可写成 r 个平方的最小 r”，没有有限 r 时定义∞；上界形式化不能当等号已证。 |
| 002444 / `eb09b549b965e1c8` | 条带集合公式含“本机文件”破坏 | 恢复 \(P_\varepsilon=\{z\in\mathbb C:\operatorname{dist}(\operatorname{Re}z,\mathbb Z)\le\varepsilon\}\)。 |


### P1：睡衣覆盖已有更强定理声称，直接覆盖双指数目标

**002444 / `eb09b549b965e1c8`。** 已打开 [Sida Li, Quasipolynomial pyjamas, 2611.26622v1](https://arxiv.org/html/2611.26622v1) 的 Theorem 1.2：充分小 ε 时，以至多 

\[
\exp((\log\varepsilon^{-1})^{50000})
\]

个旋转覆盖全平面。这比卡片的双指数目标强，且原稿开条带覆盖可用于相同宽度的闭条带。该量词和蕴含已核；本轮没有审完技术证明，仍按预印本完整声明记录。旧 [Kravitz–Leng Theorem1.1](https://arxiv.org/html/2510.17744v1) 的三指数界也已读取，不能把新进展仅描述成可能节省一层的计划。


### P1：Falconer 与反射 Banach FPP 的主端点已固定读取

- **002438 / `1698e8d5bdea4962`：** 在 OpenAI/math 提交 `3344da59991ed94f9ba711217b29c1d760badfa6` 按 ref 读取 [Falconer/Main.lean](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/MeasureTheory/Falconer/Main.lean)，`manuscript_main` 明确量化紧平面集、Hausdorff 维数>1、距离集正测度。主文件没有占位不能推出全依赖已核。[Burstein–Iosevich–Yavicoli v1](https://arxiv.org/html/2611.14867v1) 的 Theorem1.1/1.2 也直接定位：未锚定全维结论及更强距离测度正则性，不能外推成锚定版本。仍标完整证明声明待核。
- **002452 / `b6fa41e98860e6b3`：** 同一提交读取 [Nonexpansive/Main.lean](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Analysis/Nonexpansive/Main.lean) 的 `exists_fixedPoint_of_canonicallyReflexive`，端点确是原范数、任意实反射 Banach 空间、非空闭有界凸集及非扩张自映射。还读了实际导入 Model 中的反射性、原范数非扩张性和不动点性质定义，以及 OriginalNorm 与 Basic 部分接口，未重建 Reduction / NormalizedContradiction 的完整链。

两者的 `ComparatorChallenges` 文件均保留 `sorry` 作为待比对模板；已另读真实主模块，故既不能以模板占位认定作者主证明失败，也不能以端点类型匹配宣布独立核验成功。没有执行任何构建或公理闭包扫描。


### P1：分拆奇偶 v2 与谱几何期刊版本

**002430 / `1a94efc8fc0161c6`：** 查询发现 [Wang 2611.10899v2 的索引](https://www.arxiv.symmetricfunctions.com/paper/2611.10899v2) 标记 2026-11-18 更新，并新增 AxiomProver 已形式化声明。原 arXiv abs / HTML / PDF 读取均失败，故这里只标二级索引线索。(X^{3/4}/(\log X\log\log X)) 下界仍不足以推出密度 1/2。早期 Zheng 的 √X 级形式化不能混作 Wang 新界代码，需下一轮取得对应固定提交。

**002451 / `f21d2b511dbde834`：** 已取得 [EMS 正式 PDF](https://ems.press/content/serial-article-files/51291)：Hanna N. Kim，*J. Spectral Theory* 15 (2025), 963–993，DOI `10.4171/JST/572`。旧卡应补已刊信息。Conjecture3 的高维锐常数 (A_n) 与 Theorem4 已证的较大 (B_n) 仍明确分开；后者渐近比趋近1不能代替精确锐界。


### 查重结论与继续复核的边界

本组 16 个指定对子均判为相关但不等价或词面误配，未合并。特别是 002445 / 002484（勾股染色 / Navier–Stokes）和 002452 / 002481（Banach 不动点 / 截角八面体等积最优）没有同题关系，仅泛化标题或存在性措辞相似。002451 与三个图 Laplacian 猜想也不能因算子名称相同而合并。

新增 002442 / 002443 关联已保留双方版本：全局消解与逐赋值局部模型有联系，但基域与全局量词不同，尚未核可逆归约。其余全库宽词命中只列入实际检索记录，不依据标题作等价判定。

优先下一轮复核的顺序：Petersen 正确语义证书 → Pierce–Birkhoff 全依赖与人工论证 → Tian 全局证书存在性 → Reed 长方体约化桥梁 → Falconer / Banach 原范数证明链。原稿访问受限的项目（Wang、部分三维消解/HAL、Pfister 大扫描、Rado/Pillai 旧 Zenodo 声称）均在逐题 `pending` 中按事实列明，不能复用旧卡“已读”“已核”的完成状态。


## 第三部分：新界、条件推论及重复题

### 交付与实际执行范围

- 25题均实际执行名称/原出处、公式或特征、GitHub/形式化、公开AI/社区查询，并记录查询原文、日期、返回引用、直接链接与访问层级；合并响应没有伪装成逐词零命中。
- 全库索引逐题执行25次 rg 检索，15组指定对子均读双方当前全文。指定对子判断为12组相关但不等价、3组特例/强化；另新增2469与2470的同题关系。
- 主问题结论：21题暂未找到可验证结果、1题原题已证的数学推论、3题完整证明/反例声明待核。另列有限范围进展及题面错误，未用“没有搜到”证明“仍开放”。
- 311条实际请求或本地检索记录、68条证据、85个原始工具批次。原始第三方全文仅留内部审计 raw，不并入面向用户的成品包。
- 本轮实际执行的是自写整数/证书检查；未运行任何未经审查的外部代码，未编译 Lean，未运行 comparator 或独立内核。所有线上写入标记为 false。
- 主文件：results.jsonl。辅助可复核文件：validation.json、local_index_audit.json、local_checks.json、local_checks.py。查询与证据附对应原始响应 SHA-256；GitHub blob SHA 与 commit 分开记录。


### 1. QX-P-002454：标准RH的外部认证使均匀密度命题成为已证推论

当前 rev：cd6f7b99319cdf4f。旧卡的待核推论状态，建议更新为“原题已证（外部认证基础上的数学推论）”，把本轮未重跑形式化单列。

实际打开：

- [Lean FRO / Mathlib联合声明](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)，2026-11-21，正文认证标准Mathlib RH陈述及证明检查。
- [Rubinstein原页](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/)，2026-11-26更新报告短版794模块与多内核检查。同页仍有13个经典假设的人类指南，是另一材料，不能混同。
- [DensityHypothesis.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Wikipedia/DensityHypothesis.lean)，实际 blob 为 de3df7705ba189811eeebdc1c296ceef84206a7a；量词为先ε、后同一Cε、再所有σ和T。

目标是对每个ε>0存在Cε，使全部1/2≤σ≤1、T≥2同时满足 N(σ,T)≤Cε T^{2(1−σ)+ε}。标准RH给σ>1/2时计数为0；σ=1/2时经典Riemann–von Mangoldt给N(T)=O(T log T)，再用log T≪ε T^ε。相同常数覆盖整个σ区间，含σ=1，无需依赖σ的常数。

本轮直接核到的是外部认证原页、目标量词与数学推导，没有重跑RH或组合Lean。DLMF §25.10(i)只作零点定义与边界核对，不冒充该页已经给出本次所需计数渐近公式；额外大学PDF抓取超时记录在queries。形式化目录仍标open/sorry不能否定已认证的外部结果。


### 2. QX-P-002455：六阶矩41.008声明与41.007形式化目标必须分开

当前 rev：25d77dbea6171317。原问是精确首项42a₃/9!，本轮取得的新界和声明都没有给这个等式。

- [de Faveri–Pandey原稿](https://arxiv.org/html/2610.01035v1)，Theorem1.1：未归一化六阶矩上界T^{37/30+ε}。
- [Durkan–Page作者机构记录](https://research.manchester.ac.uk/en/publications/amplified-moments-of-the-riemann-zeta-function/)，摘要给34.4的归一化下界；PDF请求403，c₃全文归一化仍待逐式核对，未声称读完全文。
- [Fraccaro Hexagon v3](https://hexagonmath.org/2610.00634v3)，Abstract、Provenance、Version history，当前版本史日期2026-11-21：作者声称41.008，并披露AI曾纠正Lemma4。此站点不是arXiv，页面顶部日期与版本史不同也已保留。
- [固定commit的README](https://github.com/Niklas-Fraccaro/sixth-moment-lean/blob/950bfaff8724d4adb1c37535634a139b70228df0/README.md)：实际目标liminf>41.007，最终类型为 DivisorProof.Watt41 → SixthMoment.FullGoal。Watt41并未在该交付中无条件完成；其统一常数形式与原Watt定理的对应仍须复核。本轮未跑Lean，不把作者CI报告记成本轮通过。
- [Harper原摘要](https://arxiv.org/abs/1305.4618)：RH下的正确阶上界，结合本轮所采用的RH外部认证成为数学推论，但仍不能确定首项42。

建议补进展与声明层级，不把41.008、41.007或正确阶上界合并成精确渐近证明。


### 3. QX-P-002467：小Cohen–Macaulay反例声明有部分Lean，范围只到候选环

当前 rev：62252e4add374e5c。旧卡“只有TeX、没有Lean”须改，但主反例仍列完整声明待核。

实际读到[paper.tex](https://github.com/openai/math/blob/main/preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/build/paper.tex)的 thm:main、thm:obstruction 与 cor:affine-local，和[surface.tex](https://github.com/openai/math/blob/main/preprints/A-Complete-Local-Domain-Without-a-Small-Cohen-Macaulay-Module-September-23-2026/build/surface.tex)的构造。主声明确实排除任意非零有限生成MCM模，不只是分次模或有限代数。原始路径是paper.tex，不应继续泛称不存在的main.tex。

[官方lean/docs/195.md](https://github.com/openai/math/blob/main/lean/docs/195.md)的Scope and limitations明确：Lean支持候选环的三维、完备、Noetherian、整闭及剩余域等结构，不认证“没有非零有限MCM模”。因此“存在Lean”也不能升级主反例。

本轮独立算术复算n=7：H²=1715，K²−2c₂=13377，6H²=10290，确有13377>10290。没有借算术正确替代曲面几何、正规性或任意非分次模到数值障碍的证明。优先待审的是后者完整链条。


### 4. QX-P-002469 / 002470：同一数学命题，Davis全称声明未取得全文

当前 rev分别为cc4ede605134dba2、eebd978e25d7b85a。两卡都问标准光滑四维Poincaré。2470的通常Hausdorff无边界流形约定下，同伦等价S⁴给连通性和非零顶维同调，从而强迫闭；2469显式写闭连通。2469多的是Davis声明追踪，不构成新的数学问题。

建议标“同题”，以2470作为主问题候选、2469作为声明追踪子记录，由维护方决定；本轮未执行合并。

- [Davis Zenodo18987788](https://zenodo.org/records/18987788)：搜索返回2026-03-12 v1、完整SPC4声称和作者摘要；本轮记录页429、PDF请求失败，仅摘要级。旧卡过去全文审稿的说法不算本轮已经重做。重点待核干净finger move、不新增双点与终止性。
- [Oliveira–Smith原稿](https://arxiv.org/html/2603.23717v1)：Theorem1.1只证特定Dunfield–Gong同伦四球面X_DG标准，Corollary1.1.1是相应结的slice性，不覆盖全称。
- [正确的Poincare.lean路径](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Millennium/Poincare.lean)：blob212db258d04823771044d5ed7de6bcecf591d84a，四维smooth项是研究占位。此前猜测Wikipedia路径404已由正确目录修复，未把抓取失败误判为不存在。

2469维持完整声明待核；2470全称为本轮暂未找到可验证结果，并单列Davis声称。不能把该声称作为大奇异4球等关联题的已证前提。


### 5. QX-P-002477：非可均证明的可读重写和固定源码支持，复现层级独立

当前 rev：45caaca857ed42f7。主问题是标准dyadic PL群F非可均。题面均值函数域有“本机文件”乱码，应恢复M:ℓ∞(F;R)→R及线性、正、归一、左不变条件。

实际读取[Kim–Lodha 2610.18360v1](https://arxiv.org/html/2610.18360v1)的Theorem0.1、Theorem2.1与Lemma2.5。其人类重写给Hilbert球上L<√2的位移映射与均值距离q≤L²q/2，再和位移矛盾；本轮没有把能复述结构当作全部分析依赖已独立审核。

形式化实际路径：

- [官方248范围说明](https://github.com/openai/math/blob/main/lean/docs/248.md)：标准F无不变均值；不额外认证指定生成集及精确边界常数。
- [固定Main.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/GroupTheory/Thompson/Main.lean)：有 thompson_F_not_amenable 与 thompson_F_nonamenable_composition。
- [固定ComparatorChallenges配置](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ThompsonNonamenability.json)：精确目标为OAI.ThompsonNonamenability.thompson_F_nonamenable_composition，允许三个标准公理，enable_nanoda=false。读取配置不是通过检查。

本轮只静态核Main、配置和范围文档，没有重跑完整依赖，也没有重做旧卡所谓12文件审核。保留完整证明声明待核，同时注明人类证明与代码支持；不把期刊是否接收当作唯一验收门槛。


### 6. 可以直接修正的题面或说明

| 题号与当前rev | 旧卡问题 → 建议修正 | 本轮证据与定位 |
|---|---|---|
| 2457 · 73911c340745c208 | 用“辛同胚”定义逼近序列本身，循环；改为光滑辛微分同胚的C⁰极限，S⁴称四维球面 | [原MO问题](https://mathoverflow.net/questions/179898/does-s4-have-a-symplecto-homeomorphic-structure)；[2026原稿](https://arxiv.org/html/2603.07731v1) Remark1.5、Question1.6仍将辛bi-Lipschitz加细作为问题 |
| 2458 · 8b1f1d251f45f4c4 | “所有非零复数z的e^z由Hermite–Lindemann超越”错误；需z为非零代数数，n=1按z代数/超越分支说明 | [实际Schanuel定义](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Wikipedia/Schanuel.lean)；例如z=2πi时e^z=1即可排除旧措辞 |
| 2462 · fc73e9927a3c3681 | 某个正比例下界不推出始终>0.8；恢复计数式中的X和存在素数p | [原讨论](https://mathoverflow.net/questions/470539/probability-of-finding-a-prime-number-between-x-lnx-and-x-lnx)专家评论/答案；[Jha v2](https://arxiv.org/html/2605.23014v2)仍有强Hardy–Littlewood条件 |
| 2464 · 1a0806f4091ce302 | S=H−I不能“零对角且全±1”；改为非对角元±1 | [2610.27175v2](https://arxiv.org/pdf/2610.27175v2) p10 §5.1 Problem4及表；版本已到2026-11-03 v2，skew最小未决阶仍列356，普通Hadamard更新不等于skew更新 |
| 2471 · 6a19322796118183 | S³在S⁴的两个闭侧目标是B⁴，不是S⁴“光滑四球面” | [Cha–Kim](https://arxiv.org/html/2411.10051v1) Theorem A/B及Schoenflies balls说明；标准双倍不推出球本身标准 |
| 2472 · 8a9b26c700122695 | 本题是处处Ric>0，不是“一点处”；无限π₁、近非负Ric结果不构成本题更强假设的直接子情形 | [Chen–Ge–Han摘要](https://arxiv.org/abs/2209.11951)；紧致Ric>0由Myers给有限π₁。[Wiemeler已刊全文](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.70295) Thm1.1/1.2、Cor1.3仍含额外完全交/群作用条件 |
| 2473 · 5a3385feeb15e3fa | 120n+49前五项不是全平方，409不是；实际4个平方仍大于24n+1的3个，N=5反例仍有效 | 本轮自写isqrt逐项检查；[作者摘要](https://arxiv.org/abs/1301.5122)仅确认6≤N≤52，唯一性另有限制 |
| 2474 · 8d20475f4e575dae | 完整理论不对否定封闭；若完整T_exp有递归可枚举公理化，就足以用双路证明枚举判定 | [Berarducci–Gallinaro PDF](https://arxiv.org/pdf/2603.08365) p2、Thm12.4/14.4；全exp结论仍以实Schanuel为前提。abs v3日期9月25日，但可读PDF日期6月24日，未确认两者同版 |
| 2476 · fbec873dce41630f | 固定4连通无爪版本才与本题等价；000894的∃f(3)不保证f(3)=4 | [Ozeki–Zhang](https://arxiv.org/html/2603.03361v1) Conjecture1.1；指定对子完整题面比对 |

这些纠错不等于对应数学主问题被反驳；原始意图与卡片表述分开记录。


### 7. QX-P-002460：真正重做了538证书检查，仍不是精确S(6)

当前 rev：88cd24e058bed3ea。实际从[作者仓库字串](https://github.com/mysticflounder/schur-538/blob/main/schur6-538.word)取得538位证书，blob d3447d860a196d35a10e07be31669a3897228337。包括尾换行的SHA-256为9e149c007b778655afd199685ebcc76260604a44f4c322d8aa9a1d96afb71d20。

自写遍历覆盖72,361对1≤x≤y、x+y≤538，包含x=y；没有同色冲突。六类大小依次131、85、58、67、63、134，与包内字符串一致。由有限证书可确认S(6)≥538，不能得精确值。未运行作者外部程序或Lean。


### 8. 其余需要保留的范围区别

- **2463 · f918500be94ac157：**[Ghermoul原稿](https://arxiv.org/html/2508.07367v1) Theorem2.1后及Conjecture2仍留下n=5q+1且q≡0 mod252的分支；摘要说全部不能覆盖正文缺口。Zenodo17714682只到搜索线索，不判其不存在。
- **2465 · 31743300a9485b05：**[Banff问题集](https://math.dartmouth.edu/~auel/papers/docs/Banff_2022_arithmetic_groups_problem_session.pdf) p2 Question1/1′明确区分SL₂=E₂和有限生成。与000566（90c5e59af99380c9）是强化关系；非FP₂不推出非有限生成。
- **2466 · 59d2c0d76219185e：**[Ye–Zhang](https://arxiv.org/html/2605.25080v1) Theorem1.1证明SL₃(Z)非Howson，未给有限生成但非有限表现子群，不能解决coherence。
- **2468 · fa6363c1cba53878：**[Ma–Ning–Zhao](https://arxiv.org/html/2609.20724v1) Theorem1.2的k/600不等于目标k。2611.07145摘要的min{k,10k−n−30}仅在相应参数范围给全k，正文三入口不可达。
- **2475 · b149d08145660f3d：**[OEIS A393643](https://oeis.org/A393643)的四参数主序列不是对角x^^y+y^^x。评论只说43为已知对角素数，不是唯一性定理。


### 9. 查重与复核优先级

15组指定对子完整记录在results.jsonl，每组包含双方当前rev及理由。尤其001900使用当前20a387a5da315568，没有采用历史候选中的fa5b702e827f8dcc。

三组强化关系为2464↔001202（限d(4k)达界子问）、2465↔000566、2476↔000894（限k=3且固定阈值）。其余12组没有同题等价。新增2469↔2470是本轮最明确的同题发现，尚未合并。2459↔000366、2464↔000483、2477↔002051/002151只做索引候选标记，没读这些额外卡的全文，故标待定，不冒充完成配对。

下一步按证据价值优先：固定版本重跑及语义核对2454/2477；审2467任意有限模的几何障碍；取得Davis全文；核2455的Watt41依赖及两个常数；修正上述题面、量词和算例。未取得全文与未编译项均已留在各题pending中。



## 第四部分：退化反例、有限进展及其适用范围

### 1. 当前题面已被退化例否定：QX-P-002494，09de741e122c26f8

**旧卡 → 新发现。** 旧卡允许所有并闭族，并认为没有反例。取 \(n=1,m=0,\mathcal F=\{\varnothing\},x_1=0\)。这族非空且并闭，满足全部当前前提。唯一候选 \(k=1\) 的左侧为空和 \(0\)，右侧是 \(e_0(\varnothing)=1\)，故要求 \(0\ge1\)，错误。自写标准库脚本已作精确检查，见 `counterexample_2494.py`、`counterexample_2494.json`。

[MO #514705 原题](https://mathoverflow.net/questions/514705/further-algebraic-strengthening-of-frankls-union-closed-sets-conjecture) 本次全文可读，其定义同样未明确排除这一族。所谓“非空集族”仍不足，建议要求 \(\bigcup\mathcal F\ne\varnothing\)，或明确单独排除 \(\{\varnothing\}\)。空集族本身是平凡真例。

**量词与边界。** 这只否定当前字面题面，不否定通常的 Frankl 猜想。修订后 \(m=0\) 才与通常非平凡 Frankl 对应；一般加权修订题仍需研究。旧卡 \(m=n-1\) 端点证明也应修补 \(n=1\) 边界。

**实际路径。** 原 MO 全文；题名与“union-closed / elementary symmetric / nonnegative”学术查询；GitHub 查询；全库索引；000137、000457 指定正文对照。**待复核：** 作者 intended scope；000457 的同类假设遗漏。报告、修订与查重关系应保留版本，不直接合并。


### 2. 万有偏序上界明显过时：QX-P-002487，75824ebb1f6b3c1d

**旧卡 → 新证据。** 旧上界指数为 \(2/3\)。Balogh–Garcia–Sales 的 [Even smaller universal posets，arXiv:2607.12980](https://arxiv.org/abs/2607.12980) 摘要及 [Rényi 作者研讨页](https://www.renyi.hu/en/node/5077) 声明：每个 \(\eta>0\)，充分大 \(n\) 存在大小至多 \(2^{(1+\eta)n/2}\) 的偏序，作为**诱导子偏序**包含所有 \(n\) 元偏序。上界应更新为 \(2^{n/2+o(n)}\)，不是精确规模已确定。

**访问与路径。** 名称和指数特征两组检索，system1 交叉验证，原 arXiv 摘要、机构报告全文；arXiv abs / html / pdf 多次打开失败。GitHub 和 MO 入口已查询。**待复核：** 取最新证明全文及定理编号；下界指数 \(1/4\) 与新上界仍有间隙。


### 3. 新有限称重矩阵覆盖：QX-P-002493，8fb63b84335a4eaf

**旧卡 → 新证据。** [arXiv:2610.33976](https://arxiv.org/abs/2610.33976) 及 [作者仓库 README](https://github.com/adrianmaciasquintero/weighing-matrices/blob/main/README.md) 声称覆盖 \(n=4,8,\ldots,108\)、所有 \(1\le w\le n\)，总计 1512 个 \(W(n,w)\)。\(w=0\) 可直接取零矩阵。

README 给出整数条目、每行列重量及 \(WW^T=wI\) 的精确验证流程；本次没有读取全部矩阵数据或运行验证器。文件 blob SHA 为 `4ef54ca9c1064d3167f71530ba5412a052e24924`，不是仓库 commit。

**实际路径。** 原 1974 Cambridge 四页论文已打开；名称、全重量/2026 特征学术检索；代码入口；AI/社区检索；与 Hadamard、Williamson 两卡正文对照。**待复核：** 全数据与验证器、最新稿版本。有限覆盖不能推出所有 \(4m\)；Hadamard 是 \(w=n\) 端点，Williamson 是受结构限制的构造路线。


### 4. ζ(7) 两处逻辑错误及新声明：QX-P-002501，2de6f072c562ab87

**题面修订。** “ζ(7) 无理”等价于**不存在**整数 \(a,b\)、\(b\ne0\) 使其等于 \(a/b\)，旧卡“是否存在”漏掉否定。若四个数中至少一个无理，而另外三个都已知有理，则确能推出 ζ(7) 无理；旧卡反向说法错误。已知集合结论本身不能确定另外三个是否有理，才是无法选出 ζ(7) 的原因。

**新声明范围。** [gmDevi README](https://github.com/gmDevi/zeta-7-21-lean/blob/master/README.md) 声称八个**实** ζ 值 \(7,9,\ldots,21\) 不全有理；尽管目录名含 Zeta2Lean，不能解释成 2-adic 结论。声明固定 commit `a3b69fc43aea3dd140540f6e8380c7d0fecce028`、端点 `Zeta2Lean/Window/Main.lean::ZetaWindow.zeta_7_to_21_not_all_rational`。本次只核 README，未取得全部证明。

**Anand 单值声明。** [Issue #1 及评论](https://github.com/gmDevi/zeta-7-21-lean/issues/1) 指 v1 式 (54)、(58)、(59)、(62) 所给积分应为 \(453803/288000>0\)，不是 Table 5 / (122) 的负数，并给出末区间和最终 margin 的精确质疑。两份公开核算都是他人报告，本会话未运行；Anand Zenodo 及 PDF 访问失败，不能把旧卡作者勘误记载说成本次重新读到。

**实际路径。** ζ7、集合无理性两组学术查询；Zenodo/MO/AI 查询；Formal Conjectures 文件；README、issue、评论全文。**待复核：** 最新 Anand 稿及修改；八值定理完整依赖。当前证据不决定单值 ζ7 的有理性。


### 5. ζ(5) 新测度 ≤87 声明：QX-P-002500，18f9bcef315b745a

**旧卡 → 新证据。** Sean Litsey 的 [An irrationality measure for zeta(5)](https://hexagonmath.org/pdf/2611.00841v1)，Theorem 1.1（页 2），声称存在 \(q_0\)，对所有整数 \(p\)、\(q\ge q_0\)，有 \(|\zeta(5)-p/q|>q^{-87}\)，即测度至多 87。§10（页 19–20）指向 `CatalanCore/Zeta5/SolutionZeta5.lean` 端点。请求 URL 含 v1，实际 PDF 页眉为 v2；应保留该版本差异。

**已有路线重核。** [mo271 固定提交顶层定理](https://github.com/mo271/Zeta5/blob/2c80b320d06b4395605edbd413649d19094507af/Apery/Main.lean) 与 ζ5 无理目标对应，未审全依赖。[Dan Romik README](https://github.com/danromik/zeta5-irrationality/blob/main/README.md) 明列 PNT 公理 `chebyshev_theta_asymptotic`。[AFP](https://isa-afp.org/entries/Zeta_5_Irrational.html) 入口已在旧卡中，本次重核不计新发现；它公开使用区间不等式的 `holds` oracle，不能与其他路线公理表混用。

**实际路径。** Fauzan 名称与 Hankel/多项式特征；Zenodo 记录、MO 讨论、AFP、作者仓库、Hexagon 全文。直接请求论文所指 SolutionZeta5.lean 返回 404，尚需定位真实目录。**待复核：** Litsey 完整代码和固定提交，全部解析假设、公理与比较器；本次没有独立 Lean/Isabelle 重跑，保持完整声明待核。


### 6. RH 新审计与 dyadic 障碍：QX-P-002502，059ab51433981178

[Rubinstein 官方报告](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/) 的 11 月 25–26 日更新报告短版 794 模块、五项 RH/GRH 定理、六内核及 paranoid comparator 全部通过，并链接 Sutherland 独立检查。本会话已读报告，未重跑。

**量词不能跳过。** 本卡数 \((T,2T]\) 内**简单且在临界线上**的零点。已读 [Bui–Heath-Brown 原稿](https://arxiv.org/pdf/1302.5018) 页 1，其 RH 条件下 \(19/27\) 比例采用累计 \(0<\gamma\le T\)。两条累计下界不能直接相减得到 dyadic 下界；需核对局部化证明或另引合适定理。即使 RH 路线通过，也不能略掉这一连接。

[Yang–Yang Zenodo](https://zenodo.org/records/21975237) 与 [仓库 README](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/main/README.md) 仍明确为候选，解析层未形式化；部分有理证书和 Lean 定理不能替代整个 .7962 证明。

**实际路径。** 原比例/区间特征、Yang 复核查询、RH 官方页、Bui–Heath-Brown PDF、Zenodo 和两个形式化入口。**待复核：** RH 最终语义/依赖；dyadic 版本；.6725 基准与后续改进的同一区间约定。


### 7. 紧空间“例子”的摘要自相矛盾：QX-P-002503，c087ed109c76035e

**旧卡 → 新线索。** [Guedes 2023 公开摘要](https://www.researchgate.net/publication/370979087_Examples_of_Weakly_First-Countable_Compact_Spaces_in_ZFC) 提出 \([0,\omega_1)\) 序拓扑，声称紧而非第一可数且 \(\omega_1>\mathfrak c\)。

该具体例子不合格：开初始段构成无有限子覆盖的开覆盖；每个小于 \(\omega_1\) 的序数可数，从而各点有可数局部基；ZFC 中 \(\aleph_1\le\mathfrak c\)。这只驳倒摘要中的构造，不是否定所问 ZFC 存在命题。全文需要申请，本次未取得。

**实际路径。** 精确名称、ZFC/compact、Jakovlev/b=c 查询；2013 原论文入口与 MathNet 书目；Guedes 摘要；当前 Formal Conjectures 精确目标。**待复核：** 原 2013 PDF 本次不可达；CH 下结果不得当无条件证明。题面索引 \(n\in\mathbb N\) 的文件残留字样应清除。


### 8. 原引文指数误抄：QX-P-002491，2f62d791f1150edf

[Waldschmidt Cetraro 稿](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/Cetraro.pdf) §4.1、印刷页 301、式 (4.1) 是 \(|e^b-a|\ge b^{-\kappa}\)，有限计算取 \(\kappa=2.25\)、\(2\le b\le100\)。旧卡写成 \(b^{1-\eta}\)、\(\eta=2.25\)，相差一个幂次；原文摘录字母也应改。

**实际路径。** 名称/最近整数与 \(n^{-c}\) 两组查询、原稿全文、形式化文件及社区入口。**范围：** 有限数值范围并不解决所有 \(n\ge2\) 的统一常数问题。**待复核：** 2026 讲义本次只查得索引，不沿用旧卡“全文已读”记录。


### 9. 图论背景错误，非主猜想反例：QX-P-002498，f78681e3aae9ba54

旧卡说一般星形树有哈密尔顿路。\(K_{1,3}\) 的三个叶子都必须是路径端点，故没有哈密尔顿路；它不满足 \(\operatorname{tree}(G)-2\le\kappa(G)\)，所以不是 WOWII 199 反例。作为有路无圈的例子应改用路径。

“任意独立集加一个相邻顶点成为诱导星”也不成立：\(P_6\) 的独立集 \(\{1,3,5\}\) 没有共同邻点。这里只否定该论证，不据此宣布 \(\alpha(G)\le\operatorname{tree}(G)\) 本身真假。

**定位与路径。** [当前 GraphConjecture199.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/WrittenOnTheWallII/GraphConjecture199.lean) 全文取得、目标 open/sorry；官方 WOWII 索引原句可检，PDF/存档直接打开失败。名称、诱导树/连通度特征和 AI 社区已检。**待复核：** 相关不变量关系另找正确证明；不要用相邻 141–143 号结果替代 199。


### 10. 单位距离评审应保留人工修补评价：QX-P-002485，3d39c86a8db8a489

[OSVerify 案例页](https://osverify.github.io/cases/planar-unit-distances.html) 对 §8.2 扩大系数域后的 genericity 提出错误；同页 human expert feedback 认为提出的修补解决该处过强表述，并保留所需下游结论。旧卡若只写“大问题”而省略修补评价，会误导为整篇已被否定。这里既不认证整篇，也不宣布主定理反驳。

[Sawin 原稿](https://arxiv.org/pdf/2605.20579) Theorem 1 明确是任意大的 \(n\)、\(n^{1.014114}/C\) 下界；不是精确 limsup。修复 \(\nu(P)\) 的乱码为无序单位距离点对数，另定义 \(u(n)\)。

**实际路径。** limsup/数值指数、power saving/genericity 查询；Sawin PDF、OSVerify 全文、GitHub 与社区。**待复核：** 更高优化指数、条件 zeta 数值界及整篇依赖；新索引候选 001645 尚未读正文。


### 11. 截角八面体的对象译名过窄：QX-P-002481，fc07504db6fcaea6

旧卡将 parallelohedra 译为“平行六面体”。该类包含五类三维凸平移铺砌体，截角八面体自身有 14 个面；应使用“平行多面体”并说明铺砌条件。

[Hales–Song v2](https://arxiv.org/pdf/2609.00997) Theorem 1.1、§6.5 与 Appendix A 本次已核，覆盖全五类及等号唯一性；[Cesaroni–Novaga v2](https://arxiv.org/pdf/2609.02384) §6.3 也给全局比较。[CVGMT 作者页](https://cvgmt.sns.it/paper/7958/) 11 月 13 日仍列 preprint，不能用另一篇局部最优文章的 DOI 冒充全局结果发表。

**实际路径。** 名称和常数/对象检索、两份原稿全文、作者书目、代码/社区入口。**待复核：** 全部精确证书及退化边界；本次核定理范围，未独立重跑证书。


### 12. 必须防止误归类的新增结果

| 题号与当前版本 | 实际读到的变化及范围 | 证据与下一步 |
|---|---|---|
| 002480 / c4afd61c87b5c064 | 三臂蜘蛛及方向翻转受控的长路径；一般树未覆盖。任意有向宿主的 relative anti-Sidorenko 与竞赛图版本不同。 | [2605.14138 全文](https://arxiv.org/pdf/2605.14138)，Theorems 1.4/1.5/1.7；[2609.14655 摘要](https://arxiv.org/abs/2609.14655)，全文待取。 |
| 002488 / 25dd981b16eaa8f4 | 新 Hadamard 矩阵下界在 \(\mathbb F_3\)、秩约 \(\log^2N/80\)，远低于 \(N/\log\log N\)。 | [2608.06592 摘要页](https://arxiv.org/abs/2608.06592)；[Alman–Liang 全文](https://arxiv.org/html/2502.19580v1)。 |
| 002489 / bcb0c4ce7909768e | 新 Vaught 反例仓库明言只适用 \(L_{\omega_1,\omega}\)，不处理一阶完备理论。 | [SOURCE-ALIGNMENT](https://github.com/cameronfreer/vaught-conjecture-palomar/blob/main/docs/SOURCE-ALIGNMENT.md)；完整代码与 Knight 原稿待核。 |
| 002490 / 01b130b79767f561 | WG2026 算法针对 \(\Delta\ge8\)，不解决 \(\Delta=6\)。Huang 记录本次不可达。 | [出版页](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.WG.2026.27)；旧声明版本仍待重核。 |
| 002492 / af794ebb98d9c1f2 | 两个新仓库分别为弱铺砌 Problems 4.1、4.3；四区间反例集合自身真铺砌，不能否定 4.2。 | [原稿 §4](https://arxiv.org/html/2506.23631v2)、[4.3 README](https://github.com/KitaKen1/weak-tiling-counterexample/blob/main/README.md)、[4.1 README](https://github.com/KitaKen1/weak-tiling-bounded-density/blob/main/README.md)。未重跑。 |
| 002496 / ecce293f09f6877d | PR 7792 合并的是三个 open/sorry 目标；不是三种断言已获机器证明。 | [PR 7792](https://github.com/google-deepmind/formal-conjectures/pull/7792)，merge commit `5c783f7227e86c989fd592da04915f377dc6cb23`；双路径原稿不可达，证明待核。 |
| 002482 / 027084c83a40140b | OpenAI 范围文件声明普通平均和定量节省；Elliott 版本要求 uniform nonpretentiousness。挑战目标的 sorry 不是解答文件缺口。 | [docs/007](https://github.com/openai/math/blob/main/lean/docs/007.md)、[挑战文件](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/OrdinaryElliott.lean)；另已读 [原稿 Introduction](https://github.com/openai/math/blob/main/preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/introduction.tex) 与定量挑战，系数固定、隐常数不要求有效；完整依赖与固定提交待核。 |
| 002484 / fa9a27eef52a2449 | NS 形式化链仍有剖面/区间证书/cell layer 输入条件；公告及 CI 不等于本会话独立核实反例。 | [lean README](https://github.com/tristanbuckmaster/navier-stokes/blob/main/lean/README.md)、[Clay 精确题面](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf)；原仓库 PDF 返回不支持的内容类型，未取得全文；实际实例化证书和 11月20日补丁后全链运行待核。 |

以上各题均执行了名称与公式/特征学术查询、相应 GitHub 或形式化入口、公开 AI/社区入口及本地逐题索引；具体实际查询以 JSONL 为准，不把计划入口冒充已查。


### 13. 查重结论与下一轮候选

20 个指定对子均读取双方正文，记录两侧版本、比较理由及对方正文 SHA-256。没有建议直接合并的同题。四指数条件、Hadamard 端点、Frankl 的 \(m=0\) 是有方向的特殊/强化关系；列表边着色、ordinary Sidorenko、谱集、Williamson 结构等不应凭名称合并。

新索引命中只作为**待定**：u=13 与本组 u=15、旧单位距离猜想与本组精确指数、其他加权 Frankl、WOWII 40/133、type F 相关卡。新候选未读正文，不计入 20 个指定对子完成数；具体两侧题号和版本见逐题 `duplicates` 字段。


### 交接与审计

- `results.jsonl`：25 行，保留模板全部键；本次 225 条查询/打开/代码读取/库内检索记录、65 条证据。
- `index_checks.jsonl`：实际逐题 rg 查询、源索引 hash、命中与两侧版本。
- `audit_ledger.jsonl`：原始工具请求及文件 hash；不复制整页第三方文本。
- `counterexample_2494.py/.json`：自写精确反例复核。
- 全部 GitHub `sha` 字段按文件 `blob_sha` 记录；只有来源实际提供或指定的值才称 commit/merge commit。



## 查重与后续复核的统一说明

71组指定配对均比较了双方当前版本的数学题面。记录给出双方题号和card_rev，关系采用包内要求的分类；没有按标题相似直接认同题，也没有线上合并。新增索引候选只有取得双方正文后才列为已复核。

新增的完整正文关系包括：002417与000968的额外幂零假设特例；002442与002443在基域假设上的范围关系；002469与002470的同一核心命题。其余仅索引候选继续待定。经典Littlewood与p进版本、Nagell–Ljunggren与Goormaghtigh、不相交NP对与coNP对，均不能按同题合并。

下一轮优先顺序：先修复可直接确认的定义、量词、公式和出处；再审核已找到的全证明/反例声明的关键桥梁；最后对固定提交与明确终点安排独立形式化重跑。遇到额外公理、未实例化的数值证书、只证明候选对象存在或只覆盖特殊参数的代码，应保持对应范围，不扩大到全称原题。

## 文件与复现说明

- `QX-NEW-10_逐题回传.jsonl`：正式逐题回传，恰100行。
- `QX-NEW-10_实际检索索引.jsonl`：从逐题记录展平的实际路径，便于按题号查阅。
- `QX-NEW-10_查重回传.jsonl`：所有指定配对判断与新增候选；双向记录保留，但统计按无向对子去重。
- `QX-NEW-10_执行校验.json`：输入与输出哈希、题号/版本/字段/引用/71配对覆盖及本地脚本结果。
- `本地有限核验/`：四个自写可复现小检查及对应结果，含538字符数学证书。

审计字段中的原始记录标识和响应哈希用于追溯；原始网页整页文本、第三方论文全文与下载的证明工程不随包重复分发。需要复核时按已列原始URL、论文版本、定理定位和真实提交号访问。GitHub的文件blob SHA与仓库commit分栏保留，不互相替代。
