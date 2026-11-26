# QX-NEW-03｜突破点、检索路径与复核清单

核查日期：**2026-11-26**。对象严格限于包内 `任务.jsonl` 的 **100题**，按原 `batch_id / id / card_rev` 回传。没有修改群星线上库，没有发帖或执行第三方仓库程序。

## 交付与覆盖

- `QX-NEW-03_逐题回传.jsonl`：100行，每行一题，包含分子问结论、实际查询、直接证据、查重关系、建议修订及待办。
- 本文只汇集影响**状态、题面、出处或查重关系**的发现；没有逐题复制“零命中”。
- 完成 **909条查询/原稿访问/本地索引记录**，收录 **286条证据记录**。这个数量包含打开、查找和本地扫描，不是独立检索式或完整审读论文的数量。
- **55组指定查重对子均已处理**，另报告 **14组新增候选关系**。新增“待定”没有取得双方完整现卡，不视为同题，也没有合并。
- 每题执行至少两组学术检索词，另有代码、公开AI/社区及2469卡本地索引路径。联合域名查询只代表这些域名进入了检索式，**不代表逐站内部全量搜索**；未登录MathSciNet/zbMATH开展穷尽引文追踪。
- 搜索摘要、原始正文、访问失败和作者自报分别记录。**没有运行任何Lean项目**；不得把代码页面可达、Comparator题目模板、AI审核标签或README自报当成本轮独立验证。1693的有限反例是另用自写整数程序核查，1738/1745等短反例属于本轮直接数学推导。

### 阅读统计时的边界

共有 **50题**包含至少一个“题面有误”子记录，**28题**包含至少一个“完整证明/反例声明待核”子记录。各类可重叠；后者**不是新解题数**。同一题可能一个弱子问已证、一个强子问待查，或误混入的另一问题已证，因此不按“任一子问已证”统计整卡解决率。

## 优先复核入口

| 题号 | 本轮关键发现 | 范围与下一步 |
|---|---|---|
| 001693 | 9顶点反例及整数证书已本轮核查 | 反驳δ≥n/3倍增正则版；严格>版另有已知结果。完整数据见附录及JSONL。 |
| 001649 | 11月24日Hadwiger三维完整声明 | 只覆盖d=3；实际Lean项目尚未取得/重跑。 |
| 001635 | 11月24日Overfull渐近完整区间声明 | n充分大、Δ≥(1/4+ε)n；修正障碍必须使用Δ(G)。 |
| 001652、001663 | Artin无穷性与Erdős倒数和的新完整声明 | 主定理范围已定位；强密度/定量界与所选形式化子问分开。 |
| 001667、001735 | 无挠群C*刚性反例、域F≅F(x,y)≇F(x)的新稿 | 分别核Theorem6.2、Corollary6.2；未完成证明审稿。 |
| 001678、001683 | Seymour短证明跟进、Barnette实际Lean入口 | 不能继续写“无人跟进/无代码”；仍未本轮形式化复验。 |
| 001638、001640、001658 | Zaremba、Casas–Alvero、六球复结构的范围边界 | 分别区分M与5、条件假设L、拓扑图册与外置已知光滑桥梁。 |
| 001710、001714 | 撤回稿与族问题状态错误 | 撤回不等于原题被反驳；必须逐子猜想分列。 |
| 001716 | 两个greedy sum-free子猜想出现完整结果声明 | 已定位Conj16原稿与Conj17固定源码，另两个子问不随之解决。 |
| 001738、001745、001748 | 可直接核查的背景反例/教材推论 | 普通提升≠等变提升；a=20推翻特定强常数；有限维CW同伦型区别有限胞腔。 |

下文各条给出旧卡、变化、直接来源、定理/页码/提交、适用范围、实际检索路径和未完成的复核工作。检索无结果不用于推出开放性；所有建议均尚未应用到线上题卡。

## 一、001634—001661

### QX-P-001634｜内接正方形问题（rectifiable 已解；非可求长开放）

- **旧卡 → 变化**：“曲线内部”四点且顺序出现；标题把所有非可求长曲线统称开放。 → 标准内接问题要求顶点在曲线上。Asano–Ike v4涵盖可求长及局部单调等类；其Remark 5.5还覆盖曲线像有正二维测度的情况。因此非可求长不是全体未解类，不能把所有粗糙曲线都写成开放；沿曲线循环次序的额外要求需另核。
- **定位与范围**：[Asano–Ike, The Rectifiable Rectangular Peg Problem](https://arxiv.org/html/2412.21057v4)，Theorem 1.3；Corollary 5.9、5.12；Remark 5.5；v4 2026-11-11（已打开原始来源相关段落）；[Inscribed square problem / ProofAtlas](https://www.proofatlas.ai/collaboration/inscribed-square-problem/)，公开协作页（仅搜索摘要）
- **实际检索路径**：`site.arxiv.org "Asano" "Ike" "rectifiable"` → `rectifiable rectangular peg Asano Ike Theorem 1.1 cyclically ordered 2412.21057`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：核是否需要把沿曲线循环次序作为独立子问；原Toeplitz 1911印本文页尚未取得。

### QX-P-001635｜Overfull 猜想（大 Δ 突破；中间密度开放）

- **旧卡 → 变化**：用Δ(H)定义子图overfull；旧进展只到约n/2的大度区间。 → 子图障碍必须按母图Δ(G)计算。新稿Chen–Shan 2611.32763（11月24日）Theorem 1.1声称对任意ε>0、充分大n且Δ≥(1/4+ε)n给出恰当刻画；这会覆盖原猜想充分大n的全部Δ>n/3区间，但不自动覆盖有限小n。作者明确披露AI协助。
- **定位与范围**：[Chen–Shan, An Asymptotically Sharp Form of the Overfull Conjecture](https://arxiv.org/html/2611.32763v1)，Theorem 1.1；§6；AI statement（已打开原始来源相关段落）；[West, Overfull Conjecture](https://dwest.web.illinois.edu/openp/overfull.html)，问题定义与猜想（检索取得原始页面文字）；[Chen–McDonald–Shan, Towards the Overfull Conjecture II](https://arxiv.org/abs/2607.02270)，摘要，2026-07（搜索摘要可读；HTML入口不可达）
- **实际检索路径**：`overfull conjecture Chen McDonald Shan 2607.02270 maximum degree half` → `"overfull" "Delta(G)" "Delta(H)" subgraph counterexample definition Chetwynd Hilton`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：优先审查新稿主定理；核n0有效性及有限剩余范围；未取得独立Lean验证。

### QX-P-001637｜Erdős–Straus 4/n 猜想（验证至 10^17）

- **旧卡 → 变化**：标题计算核验至10^17。 → M. B. Dumitru的2509.00128报告已核至10^18，应更新为“作者计算报告至10^18，未本轮复算”。这不是所有n的证明；Lean异常集估计与若干分母族也不能替代全题。
- **定位与范围**：[Dumitru, Further verification and empirical evidence for the Erdős–Straus conjecture](https://arxiv.org/html/2509.00128v1)，摘要及§2 computational verification（已打开原始来源相关段落）；[Salez, The Erdős–Straus conjecture: New modular equations and checking up to N=10^17](https://arxiv.org/abs/1406.6307)，题名与摘要（检索摘要）；[Erdős–Straus exceptional set formalization](https://github.com/sushaan-k/erdos-straus-lean)，README：异常集E(N)估计（仅搜索摘要）
- **实际检索路径**：`Erdos Straus conjecture Salez 1406.6307 10^17` → `"4/n" "10^18" "Mihnea" "Dumitru"`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：计算界需锁定作者程序/证书后再独立复算；若引用Erdős #242的distinct分母版本，单独核n>2及与本卡转换。

### QX-P-001638｜Zaremba 猜想（2026-05 Zhang 完全证明声称待验证）

- **旧卡 → 变化**：Zhang 2026完整证明声明与M=5混在一题。 → 2605.02518 v2 Theorem 1.2确实声明每个分母都可用有绝对界的部分商表示，但紧随定理明确其方法只给较大的绝对M，不能给M=5。必须拆分“存在某绝对M”声明和“最强M=5”子问。
- **定位与范围**：[Zhang, Expansion in SL₂(ℤ/qℤ) and Zaremba’s conjecture](https://arxiv.org/html/2605.02518v2)，Theorem 1.2及紧后常数说明；v2 2026-05-08（已打开原始来源相关段落）；[arXiv版本记录2605.02518](https://arxiv.org/abs/2605.02518)，v1/v2修订记录（已打开）
- **实际检索路径**：`site.arxiv.org "Expansion in SL" "Zaremba" Zhang` → `Zaremba Zhang 2605.02518 bounded partial quotients Theorem 1.1 constant 5 correction`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：审查expansion到全分母的覆盖步骤及常数；未找到经本轮核定且重跑的Lean证明。

### QX-P-001639｜Sendov 猜想（RESOLVED 2026=Mazur AI+Lean，Tao 背书）

- **旧卡 → 变化**：已解决，AI及Lean背书；未给本轮可复核固定代码点。 → Tao的作者说明支持Sendov及更强Phelps–Rodriguez结论。已取得teorth/sendov固定提交，核对主定理与原量词相合，记录Lean与Mathlib版本；本轮未运行构建。第三方索引给出的另一哈希在该仓库404，已换用实际可取得的提交。
- **定位与范围**：[Tao, A digestion of the proof of Sendov’s conjecture](https://terrytao.wordpress.com/2026/08/12/a-digestion-of-the-proof-of-sendovs-conjecture/)，Conjectures 1、2及全文说明（已打开原始来源相关段落）；[teorth/sendov pinned main statements](https://github.com/teorth/sendov/blob/1ddea92d89f951a0a7cbbffa6c267cf7e6640b1d/Sendov/Conjecture.lean)，Sendov.sendov；Sendov.phelps_rodriguez（GitHub API已取得源码）；[teorth/sendov dependencies](https://github.com/teorth/sendov/blob/1ddea92d89f951a0a7cbbffa6c267cf7e6640b1d/lake-manifest.json)，mathlib de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11；lean-toolchain v4.34.0-rc1（GitHub API已取得）
- **实际检索路径**：`site.terrytao.wordpress.com "digestion" "Sendov"` → `Sendov conjecture Mazur Tao 2026 Lean github proof Phelps Rodriguez`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：若需更高级别验收，独立检出固定提交，审计导入、证书与#print axioms后再构建。

### QX-P-001640｜Casas-Alvero 猜想（≤12 及 p^e 系已证）

- **旧卡 → 变化**：未假设首一却要求f=(x−a)^d；可能把每阶共有根误读成同一个根。 → 正确特征零题面是f=c(x−a)^d（c≠0），每一阶1≤k<d的导数f^(k)与f各自有公共根，根可随阶数变化。Ghosh 2501.09272 v3明确改为以Hypothesis L为条件的证明，且作者承认此前论证漏洞；不能写成无条件解决。
- **定位与范围**：[Ghosh, A conditional proof of the Casas–Alvero conjecture](https://arxiv.org/html/2501.09272v3)，Hypothesis L；Theorem A；AI说明；v3 2026-11-10（已打开原始来源相关段落）；[Casas–Alvero/resultant formulation article](https://doi.org/10.1007/s44425-026-00047-6)，§3.4（检索取得正文相关段落）
- **实际检索路径**：`Casas Alvero conjecture Ghosh 2501.09272 conditional Lojasiewicz` → `Casas Alvero polynomial common root each derivative monic degree 12 conjecture 2026`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：优先审查Hypothesis L与所需uniform性；不可用旧v1/v2无条件标题替代v3。

### QX-P-001641｜Markov 唯一性猜想（=Frobenius 1913，题面校准）

- **旧卡 → 变化**：把“所有解由(1,1,1)经Vieta变换得到”说成Markov唯一性猜想。 → Vieta下降生成树的可达性是已知事实；Frobenius唯一性是固定最大坐标z时排序后的(x,y)是否唯一。Hu–Tan–Ying–Zhang 2611.01007报告核到z≤10^500000，属于有限计算，不能替代全z唯一性证明。
- **定位与范围**：[Hu–Tan–Ying–Zhang, A Computational Verification of the Markov Uniqueness Conjecture](https://arxiv.org/html/2611.01007v1)，§2.1下降；§2.4计算；题名z≤10^500000（已打开原始来源相关段落）；[Bourgain–Gamburd–Sarnak, Markoff triples and strong approximation](https://www.numdam.org/item/10.1016/j.crma.2015.12.006.pdf)，C. R. Math. 354 (2016), pp.131–135，p.132（检索取得PDF相关段落）；[Markov uniqueness / ProofAtlas](https://www.proofatlas.ai/collaboration/markov-uniqueness-conjecture/)，问题陈述（仅搜索摘要）
- **实际检索路径**：`Frobenius Markov uniqueness conjecture Vieta tree maximum coordinate 2611.01007` → `Markoff equation "maximal coordinate" "Vieta" Frobenius uniqueness conjecture`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：计算审计与保留/删除的数据范围须由复核者确认；不得把遍历树无碰撞外推到无限。

### QX-P-001642｜Erdős–Hajnal 猜想（BNSS23 loglog 下界；五点图收官 NSS VII）

- **旧卡 → 变化**：把n^c齐次集称“超多项式”，仍以较旧五顶点结果概括进展。 → n^c是多项式规模。最新Nguyen 2610.24887 v2声明所有被禁诱导路径P_t都具有Erdős–Hajnal性质，范围超出旧P5/P6记录；一般固定H仍不能据此改为已证。论文声明了ChatGPT参与的具体章节。
- **定位与范围**：[Nguyen, Erdős–Hajnal for excluding paths](https://arxiv.org/html/2610.24887v2)，Theorem 1.2；Declaration of generative AI use；v2 2026-10-20（已打开原始来源相关段落）；[Induced subgraph density. I. A loglog step towards Erdős–Hajnal](https://arxiv.org/abs/2301.10147)，摘要与v3修订记录（已打开摘要）；[Induced subgraph density. VII. The five-vertex path](https://arxiv.org/abs/2312.15333)，摘要；v3 2026-02-23（已打开摘要）
- **实际检索路径**：`Erdos Hajnal homogeneous sets 2301.10147 2312.15333 2026 bound` → `"induced subgraph" "homogeneous" "Erdos Hajnal" 2026 paths`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：新路径定理需后续证明审查；LPBench中的相关形式化线索未取得完整依赖审计。

### QX-P-001643｜Gyárfás–Sumner 猜想（P₅ 多项式 χ-有界 2025 已解决）

- **旧卡 → 变化**：暗示P5的普通χ有界性是2025/2026才解决的特殊情形。 → P5-free图的普通χ有界性不是这次新突破；2512.24907 v4新结果是以团数为变量的多项式χ界。Gyárfás–Sumner的一般树χ有界性与更强的多项式界要分开。
- **定位与范围**：[Polynomial χ-boundedness for excluding P5](https://arxiv.org/abs/2512.24907)，摘要；v4 2026-08-11（已打开摘要与版本记录）；[Graphs with a forbidden induced tree are χ-bounded](https://www.openproblemgarden.org/op/graphs_with_a_forbidden_induced_tree_are_chi_bounded)，原问题和已知树族（检索取得原始页面文字）
- **实际检索路径**：`Gyarfas Sumner "Polynomial" "P_5" "2512.24907"` → `"forbidden induced tree" "chi-bounded" 2026`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：若升级已刊来源，核论文最终期刊版本及定理编号；AI仓库Verified标签未当独立证明。

### QX-P-001644｜R(5,5) 精确值（43≤R(5,5)≤46，界更新）

- **旧卡 → 变化**：43≤R(5,5)≤46；人话版提出寻找46点反例，GitHub可能出现全解标签。 → 2026年JGT正式论文维持R(5,5)≤46。若46点无单色K5会直接反驳已知上界，不能把它当仍兼容界限的候选。另检索到R=43仓库，其固定提交的Reduction.lean明确引入归约公理，未构成原问题无条件形式证明。
- **定位与范围**：[Angeltveit–McKay, R(5,5)≤46](https://onlinelibrary.wiley.com/doi/10.1002/jgt.70029)，JGT 112(3), 198–208，Theorem 1.1；2026-03-20（检索取得出版页与定理摘要）；[motanova84/Ramsey fixed source](https://github.com/motanova84/Ramsey/blob/b31a863fe1249db9b24cec97c098fd9bf34abbb9/src/Ramsey/Reduction.lean)，axiom vibrational_bound_implies_classical；axiom vibrational_implies_classical（GitHub API已取得源码）；[Ramsey testing claims](https://github.com/motanova84/Ramsey/blob/main/TESTING.md)，test/TestReduction.lean及R55宣称（已打开）
- **实际检索路径**：`Ramsey R(5,5) 46 2409.15709 2026 Angeltveit McKay` → `Ramsey "clique" "46" Angeltveit McKay 2409.15709`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：如继续查该仓库，需真正移除归约/SAT公理、核定义等价并独立构建；当前不值得以其标签升级状态。

### QX-P-001645｜~~单位距离问题最优常数~~ 【RESOLVED·被否定·AI 否证】

- **旧卡 → 变化**：“单位距离问题已解/最优常数”容易被理解为精确极值函数已确定。 → 已被反驳的是u(n)=n^{1+o(1)}的预测：存在固定ε,c>0及无穷多个n满足u(n)≥c n^{1+ε}。这个反例不确定u(n)的最优指数或常数。另OpenAI条目167给出n^{4/3−δ}上界完整声明，属另一方向，需单独审查。
- **定位与范围**：[Alon等, Remarks on the disproof of the unit distance conjecture](https://arxiv.org/html/2605.20695v1)，Theorem 1.1（已打开原始来源相关段落）；[OpenAI, Model disproves discrete geometry conjecture](https://openai.com/index/model-disproves-discrete-geometry-conjecture/)，2026-05-20成果说明（已检索原始页面）；[Erdos90 formalization pointer](https://github.com/plby/Erdos90/blob/2062b0e6c9770c81e397bfe41148e90b92ca0567/src/submission/Solution.lean)，固定提交2062b0e6…；FC ErdosProblems/90.lean指向（Formal Conjectures搜索结果中的固定链接）
- **实际检索路径**：`site.openai.com/index/model-disproves-discrete-geometry-conjecture unit distance 0.014` → `"2605.20695" "Theorem 1.1"`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：补核Sawin 2605.20579显式指数细节；条目167的上界须另做主定理/依赖审查；参考卡2485还记录OSVerify的genericity质疑及Naslund新下界声明，这些历史线索本轮未复核，不继承为已反驳或已验证；无独立Lean重跑。

### QX-P-001648｜Moser 蠕虫覆盖问题（Keller 区间 [0.239,0.24633]+Lean 全形式化）

- **旧卡 → 变化**：定义泛称平面区域，使用的上下界却是凸覆盖；刚体运动是否含反射表述不一致。 → Keller 2609.21968及仓库给凸万有覆盖面积下确界0.239≤α≤0.2463322372…，并非最优面积已定。已取得固定提交主定理与Mathlib依赖，作者报告Lean核验证；本轮未重跑。新增2286同题候选的现卡正文不可达，关系保留待定。
- **定位与范围**：[Keller, Improved bounds for universal convex covers of unit arcs](https://arxiv.org/abs/2609.21968)，摘要；v1 2026-09-18（已打开摘要与版本记录）；[MoserWorm main theorem](https://github.com/ethan-keller/moser-worm-improved-bounds/blob/9a3394130fe4f7b1df6ffdeffda16601795d9ce4/MoserWorm/MainTheorem.lean)，MoserWorm.bounds；固定提交9a339413…（GitHub API已取得源码）；[MoserWorm dependencies](https://github.com/ethan-keller/moser-worm-improved-bounds/blob/9a3394130fe4f7b1df6ffdeffda16601795d9ce4/lake-manifest.json)，mathlib 0df444a360eaa60ab8c11dca51a86af692955474；v4.33.1（GitHub API已取得）
- **实际检索路径**：`Moser worm Keller 2609.21968 0.239 0.24633 Lean` → `"universal convex covers" "0.239" "2611.16204"`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：核optimalArea所用覆盖定义和运动群；若要求独立形式验收，再读全依赖/证书并构建；取得2286正文后定查重关系。

### QX-P-001649｜Hadwiger 覆盖猜想（=Boltyanski 照明；d≥3 开放）

- **旧卡 → 变化**：“d≥3开放”；未覆盖11月24日三维完整声明。 → Aiger–Har-Peled–Zuzic 2611.32334 v1 Theorem 1.1声称任意三维凸体可由8个严格较小的正位似副本覆盖，精确覆盖d=3子问，需优先复核。作者称已Lean验证，但本轮只核声明和挑战规格，未取得完整实现/重跑。另2609.23913有分数照明及2^d·poly(d)覆盖声明，仍不是一般d的2^d整数界。
- **定位与范围**：[Aiger–Har-Peled–Zuzic, Hadwiger’s Covering Conjecture in Three Dimensions](https://arxiv.org/html/2611.32334v1)，Theorem 1.1；§1.2/1.3；Appendix A；2026-11-24（已打开原始来源相关段落）；[Fractional illumination and the optimal exponential rate…](https://arxiv.org/abs/2609.23913)，摘要（搜索摘要可读；abs/HTML打开DisabledError）；[照明猜想新增候选494](https://www.qunxingmath.org/p/QX-P-000494/)，card_rev 4ac7ab202441929c（入口不可达）
- **实际检索路径**：`Hadwiger covering illumination conjecture 2404.00547 2026` → `"Hadwiger" "Aiger" "2026" proof`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：优先取得完整Lean项目及固定提交；附录Challenge.lean的sorry是题目模板，不能误当实现有缺口，也不能当验证通过；取494正文后核等价关系。

### QX-P-001650｜Danzer 问题（所有 d≥2 开放）

- **旧卡 → 变化**：英语名及人话版把Danzer稠密击中集误写成antipodal点集最大大小。 → 当前题面串入了另一个已知有限点集问题。Danzer set问在R^d（通常d≥2）是否存在增长O(T^d)且击中每个体积1凸体的集合；有限antipodal点集的2^d上界是Danzer–Grünbaum定理。纠正后171是二维分支，不能沿错误题面直接合并。
- **定位与范围**：[Solomon–Weiss, Dense forests and Danzer sets](https://arxiv.org/abs/1406.3807)，摘要；定义Danzer set与O(T^d)增长（已打开摘要）；[Adiceam, Around the Danzer problem and the construction of dense forests](https://ems.press/journals/lem/articles/5197157)，L’Enseignement Mathématique 68 (2022), pp.25–60（检索取得原始出版页）；[Higher-rank antipodality](https://real.mtak.hu/175280/1/2307.16857.pdf)，Introduction：Danzer–Grünbaum sharp 2^d bound（检索取得PDF相关段落）
- **实际检索路径**：`"Danzer" "antipodal" "2^d" bounded density 1406.3807` → `Danzer problem bounded density Solomon Weiss 1406.3807 2026`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：重新确定维护者欲保留哪一个数学问题；其后再修状态与验收条件；注意O(T^d)全局增长不等于任意局部一致密度假设。

### QX-P-001651｜奇完全数存在性（下界 10^1500）

- **旧卡 → 变化**：仍列N>10^1500等旧计算界；历史撤稿线索需要本轮核。 → Ochem作者页当前报告N>10^2200、Ω(N)≥121及Ω≥2ω+55；Ω计重数，ω不计重数。页面下方仍留115旧汇总，存在未同步文字，回传按位置标明而不静默拼接。Mantovanelli 2607.04365 v2明确因§7缺口撤回，不能用为新证明。
- **定位与范围**：[Ochem, Odd perfect numbers](https://www.lirmm.fr/~ochem/opn/)，条目(1)(2)(4)与下方综合式；2026-11-26访问（已打开当前页面，未复算）；[Mantovanelli, Certified Minimal-Prime Branch Closures for Odd Perfect Numbers](https://arxiv.org/abs/2607.04365)，v2 2026-11-13撤回说明；§7 Lemma 7.3/Definition 7.4（已打开最新版）；[Ochem–Zelinsky odd perfect number result](https://arxiv.org/abs/2607.19746)，摘要，2026-07（仅检索摘要）
- **实际检索路径**：`odd perfect number Ochem Zelinsky 2607.19746 withdrawn Mantovanelli 2607.04365` → `odd perfect number "23000000000" "2026"`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：需要作者版本/证书确认121及+55，并核同页旧汇总差异；本轮未运行其Python、Lean或图灵机代码。

### QX-P-001652｜Artin 原根猜想

- **旧卡 → 变化**：任意指定基数的无条件无穷性仍写成未解决；未列2026-10-04新完整声明。 → OpenAI Math Release 029的固定提交已取得TeX原稿：主定理声称每个a≠−1且非平方整数，在充分大(x,2x)内有至少c_a x/(log x)^2个原根素数。这精确覆盖无穷性子问，但不证明正密度渐近式；按完整证明声明待核登记。
- **定位与范围**：[OpenAI, Primitive roots for every admissible integer base](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/01-introduction.tex)，Theorem 1.1（thm:primitive-root / thm:main）；Theorem 1.2 Hecke零点区域（GitHub API已取得主定理及导论）；[OpenAI Artin manuscript metadata](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/README.md)，Author OpenAI；Date October 4, 2026（GitHub API已取得）；[Murty–Naik, Artin primitive root conditional results](https://arxiv.org/abs/2608.21573)，摘要（仅检索摘要）
- **实际检索路径**：`Artin primitive root conjecture 2502.19601 2608.21573 2026` → `Artin conjecture "2, 3" "5" primitive root Heath Brown Hooley GRH`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：重点审查统一Hecke零点区域、随域变化的常数，以及引用的标记素数估计；形式化镜像声明未本轮核依赖/重跑。

### QX-P-001653｜Collatz 猜想（验证至 2.36×10^21）

- **旧卡 → 变化**：计算上限写约2.36×10^21；Tao结果说成“数密度1轨道几乎有界”。 → Barina作者页当前报告所有n<2075·2^60≈2^71.02已核收敛，属于有限核验。Tao结果是对数密度意义下，轨道能到达随起点缓慢趋∞的界，不是自然密度1的收敛到1证明。一个完整证明仓库自己列出核心收敛/周期结论仍含sorry。
- **定位与范围**：[Barina, Convergence verification of the Collatz problem](https://pcbarina.fit.vut.cz/)，实时页首及2025论文链接；页面生成2026-11-26（已打开）；[Tao, Almost all orbits of the Collatz map attain almost bounded values](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F)，主定理/摘要，Forum of Mathematics, Pi（检索取得原始出版页）；[Khayyam Wakil, Proof Status](https://github.com/iamkhayyam/the-collatz-conjecture/blob/master/PROOF_STATUS.md)，Machine-Verified与Sorried表（已打开相关表格）
- **实际检索路径**：`Collatz Barina verification 2^71 2026 Tao logarithmic density 2602.10466` → `Collatz Tao almost all orbits logarithmic density not natural density`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：动态上限随时间变化；未对Barina程序复算；若继续完整证明声明，先核它的S/T映射定义与缺失推理。

### QX-P-001654｜Landau n²+1 无穷素数（第四问题）

- **旧卡 → 变化**：声称筛法已知道n²+1素数“不太少”却还不能证明无限多。 → 应把筛法给出无穷多至多两个素因子的P2值，与真正素数值无穷性分开。Grimmelt–Merikoski的新大素因子进展亦不等于全值为素数。Zenodo上Frank Vega的v10完整解决声明已记录为待核，不能漏记，也不能当作已解。
- **定位与范围**：[Iwaniec, Almost-primes represented by quadratic polynomials](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0047/PPN356556735_0047.pdf)，1978原刊，p.172起主定理（检索取得原始扫描PDF相关段落）；[Grimmelt–Merikoski, large prime factors of n²+1](https://arxiv.org/abs/2505.00493)，v2 2025-05-30摘要（仅检索摘要）；[Frank Vega, Near-square primes conjecture](https://zenodo.org/records/4283184)，Version v10；Description；manuscript.pdf（已打开元数据/摘要；未审全文）
- **实际检索路径**：`Landau n^2+1 primes 2505.00493 Grimmelt Merikoski 2026` → `"n^2+1" "at most two prime factors" Iwaniec`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：如处理Vega声明，取得并审查manuscript.pdf关键论证；本轮只登记主张，不能凭摘要接受/否定。

### QX-P-001655｜Catalan–Dickson 猜想（276 Lehmer five 之首）

- **旧卡 → 变化**：Lehmer五个未决起点列成276、552、660、966、1074；终止与循环解释混乱。 → 经典Lehmer five是276、552、564、660、966，旧卡把564误换1074。Catalan–Dickson的普遍有界/最终终止或周期，须容许完全数、亲和数及更长循环；固定任意长的增长段也不能证明某一无限逃逸轨道。
- **定位与范围**：[Zimmermann, Aliquot sequences](https://members.loria.fr/pzimmermann/records/aliquot.html)，Lehmer five列表（检索取得原始页面文字）；[Kobayashi–Pollack–Pomerance, aliquot sequences](https://math.dartmouth.edu/~carlp/PDF/kpp16.pdf)，Introduction（检索取得PDF相关段落）；[Erdős–Lenstra, On a problem in the theory of aliquot sequences](https://emis.muni.cz/classics/Erdos/cit/33710005.htm)，Math. Comp. 30 (1976), pp.641–645（检索取得原始索引）
- **实际检索路径**：`Catalan Dickson conjecture Lehmer five 276 552 564 660 966 aliquot` → `"aliquot" "s(n)" "bounded" "Catalan-Dickson"`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：如更新具体序列轨道长度，需要另取带日期的计算项目证书；本轮未复算。

### QX-P-001657｜三角形无关图 Δ≤6 是否 5-可染（Reed 特例）

- **旧卡 → 变化**：把χ≤ceil((Δ+1)/2)当三角自由图已知上界。 → 旧上界被五边形C5直接否定：Δ=2而χ=3>ceil(3/2)=2。原MO37923明确是Reed界χ≤ceil((Δ+1+ω)/2)的特例；问所有三角自由Δ≤6是否5可染（并问girth≥5分支）。本轮没有得到全题解决证据。
- **定位与范围**：[Andrew D. King, Triangle-free maximum degree 6 five-colouring](https://mathoverflow.net/questions/37923/does-every-triangle-free-graph-with-maximum-degree-at-most-6-have-a-5-colouring)，问题正文，2010-09-06；Reed式及末尾两个子问（已打开正文）
- **实际检索路径**：`triangle free graph maximum degree 6 5 colorable 37923 2026` → `"maximum degree at most 6" "5-colouring"`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：需继续追踪精确小度结果，不能用大Δ渐近界代替Δ=6；本轮未发现对应完整形式化。

### QX-P-001658｜S⁶ 复结构（Alpöge–Claude 正向构造声称+Atiyah 反向 DISPUTED）

- **旧卡 → 变化**：六球复结构完整声明及形式化状态较笼统，拓扑/光滑兼容混杂。 → Engel 2609.38442的Theorem 4.1直接声称构造三维复流形微分同胚于S6，应保留完整声明待核。另一HopfProblem形式化明确只在标准拓扑球上建立复图册；其蓝图说明到标准光滑S6使用已知定理Θ6=0；通常数学中的桥梁成立，但尚未纳入该Lean发展。
- **定位与范围**：[Engel, Complex structures on S6](https://arxiv.org/html/2609.38442v1)，Theorem 4.1及其前的monodromy条件（已打开原始来源相关段落）；[Hopf problem blueprint](https://cbirkbeck.github.io/hopf-s6-blueprint/Overview/The-problem/)，Theorem 1.1.1；Mathoverflow1973.mathoverflow_1973；说明段（已打开主陈述与局限）；[HopfProblem pinned source pointer](https://github.com/plby/HopfProblem/blob/9ac8a456b526527837d7082ff775213ca8bc9809/Solution.lean)，固定提交9ac8a456… / Solution.lean（仅文件页面/蓝图陈述可读）
- **实际检索路径**：`"Alpöge" "six" "complex" sphere` → `Alpoge Engel complex structure six sphere 2609.38442 diffeomorphic`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：优先审查Engel Theorem4.1的单值化/拓扑识别；获取Hopf固定源码、依赖及Θ6桥梁后才能独立形式验收。

### QX-P-001660｜是否存在奇异 4-环面（DHHRS 2024 里程碑非 T⁴）

- **旧卡 → 变化**：仅列2024 exotic closed aspherical 4-manifold预印本背景。 → Davis–Hayden–Huang–Ruberman–Sunukjian结果已于2026年正式发表于Annals，证明一般闭非球面四流形有exotic对，但不是四维环面的解。MO原帖旧评论“没有exotic闭非球面四流形”已过时；环面自身仍没有本轮可验解决结果。
- **定位与范围**：[Davis等, Exotic aspherical 4-manifolds](https://annals.math.princeton.edu/2026/204-2/p06)，Annals 204(2), pp.777–794；2026-09-13上线；DOI10.4007/annals.2026.204.2.6（检索取得原始出版页）；[Do there exist exotic 4-tori?](https://mathoverflow.net/questions/133797/do-there-exist-exotic-4-tori)，原问题及2013评论（已打开正文）；[Espinar–Rosenberg, Closed 4-Manifolds Foliated by Hyperplanes](https://arxiv.org/abs/2606.08005)，摘要（搜索摘要可读；abs打开DisabledError）
- **实际检索路径**：`exotic smooth structure 4 torus 2411.19400 Davis Hayden 2026` → `"homeomorphic" "4-torus" smooth 2026`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：若继续查环面，须核π1=Z4或真正同胚T4；叶层定理不排除全部exotic T4。

### QX-P-001661｜TOP(4)/PL(4) 同伦型（2025 专著确认未解决）

- **旧卡 → 变化**：将TOP(4)/PL(4)当普通拓扑群商，高维结论写成若干Eilenberg–MacLane空间乘积。 → MO106971明确PL(n)取PL单纯群的几何实现，TOP/PL定义为BPL(n)→BTOP(n)的同伦纤维；不是按原卡的普通子群商。原问聚焦四维是否不等价于K(Z/2,3)，而n>4是单个K(Z/2,3)。本轮未找到一般四维同伦型的可验新解。
- **定位与范围**：[Homotopy type of TOP(4)/PL(4)](https://mathoverflow.net/questions/106971/homotopy-type-of-top4-pl4)，原问题；Edit各定义条目（已打开正文）；[Kirby problem list](https://people.brandeis.edu/~ruberman/K2.pdf)，Problem 4.126 (Randall)，p.247（搜索取得PDF相关段落）
- **实际检索路径**：`"TOP(4)/PL(4)" "homotopy" 106971` → `"TOP(4)" "PL(4)" Friedl Nagel Orson Powell 2025 5 connected`；其后已执行本题代码/AI联合站点检索，并核本地索引。
- **复核清单**：原卡所引2025书需具体定位其开放声明；本轮未取得足以支持原“152页仍开放”说法的明确页句。

## 二、001662—001694

### QX-P-001662 · 085cbc28b8acf177 · Two-convexity ⇒ Lefschetz？（Petrunin 比较几何，题面校准）

原题应限于单连通开集及二维仿射平面切片。人话版误释二凸性，并把切片维数扩大。原作者 v1 给出光滑边界及 n=3 肯定情形；一般高维问题本次未取得新全解。

**旧卡 → 本次处理**

- 重写人话版：补单连通、开集、二维平面及切片连通分支；替换二凸性定义。
- 将一般仿射子空间扩展版本与原题拆开。

**来源、定位与范围**

- [Petrunin: A gallery of open problems in geometry](https://arxiv.org/html/2510.11908v1)；§1 Two-convexity，L30–55。定义、二维切片原问、两种肯定情形及 R^4 高维切片反例。访问：已读取对应正文。
- [同文版本记录](https://arxiv.org/abs/2510.11908)；Submission history。最新版登记为 v2；此次 v2 HTML 访问失败，正文判断依据明确为 v1。访问：已读摘要/版本栏；最新版正文不可达。
- [Petrunin 原始讨论](https://mathoverflow.net/questions/55788)；问题 55788。用于原问溯源；直接打开失败，只有搜索结果定位。访问：仅搜索条目；直接入口不可达。

**实际检索路径**

- 学术：`Petrunin two convexity Lefschetz Homemade 2510.11908`。
- 学术：`two convex open subset Euclidean affine planes pi1 injective Lefschetz 55788`。
- GitHub/代码：`site:github.com "two-convex" "Lefschetz"`。
- 公开 AI/社区：`"two-convexity" "Lefschetz" (site:mathoverflow.net OR site:math.stackexchange.com OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 取得 2510.11908v2 正文并检查 §1 是否改动；本次已尝试但工具报 DisabledError。

### QX-P-001663 · 79259b3b29b1fb8f · Erdős 等差数列猜想（EP#3，$5000）

旧卡只据 APN 未解记录维持 open，遗漏 OpenAI 2026-09-23 的完整证明声明。已取得固定提交的论文主文件、形式化范围说明及题目声明；定量上界与倒数和推论必须分开，尚未独立重跑。

**旧卡 → 本次处理**

- 登记新的完整证明声明及原稿固定提交；旧 APN 未解只能说明该次尝试，不代表整个研究现状。
- 把倒数和推论与定量上界分开登记；不把题目模板的 sorry 当成已证或反证。

**来源、定位与范围**

- [Quasipolynomial Bounds for Arithmetic Progressions](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/main.tex)；固定提交 3344da59991ed94f9ba711217b29c1d760badfa6；main.tex 摘要。两种结论均有作者原始声明；该文件为含分节引用的主文件，未通读全部分节。访问：已读主文件摘要；全文分节未全部读取。
- [Erdős reciprocal-sum formalization scope](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/docs/159.md)；Scope；Comparator links。只选择倒数和推论，排除定量上界。访问：已读取对应正文。
- [ErdosReciprocal comparator challenge](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/ErdosReciprocal.lean)；OAI.Erdos3.ReciprocalProgressionTheorem；manuscriptReciprocalProgressionTheorem。A⊆ℕ 中 0 的项为 0 不影响正整数版本；这里的 sorry 是题目模板，非解答验证。访问：已读取对应正文。
- [Progressions import surface](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Combinatorics/Progressions/Main.lean)；导入 Results.FullLibrary 等；lean-toolchain=v4.34.1。只读取入口导入，尚未定位最终证书到全部依赖；不能宣称无 sorry/额外公理。访问：已读取对应正文。
- [Erdős Problems #3](https://www.erdosproblems.com/3)；直接访问。入口受限；本次没有读到其当前状态栏。访问：入口不可达。

**实际检索路径**

- 学术：`Erdos problem 3 arithmetic progressions divergent reciprocal sum latest`。
- 学术：`set positive integers sum reciprocals diverges long arithmetic progressions Leng Sah Sawhney Raghavan`。
- GitHub/代码：`site:github.com/google-deepmind/formal-conjectures "ErdosProblems/3.lean"`。
- 公开 AI/社区：`"Erdos" "3" "arithmetic progressions" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 需审阅论文分节和真正解答依赖、comparator 配置、lake-manifest 及公理闭包；当前没有运行 Lean。
- 需直接恢复原题站以核其当前状态；社区/AI 索引不能替代证明。

### QX-P-001664 · 497a69b78f4fb1df · 素数间隔/log n 极限点集（EP#5；Me20 最强后冷冻）

人话版“连一段区间都没有”与原题进展不符。Merikoski 原摘要确认极限点集在 [0,T] 测度至少 T/3，且其间隙有统一界；v3 修复已刊证明两引理但不改结果。不能将这些进展写成所有非负数都是极限点。

**旧卡 → 本次处理**

- 删去“没有连续区间”绝对断言；用已核测度/间隙结论，并将 Pintz 原文列待核。
- 引用 Merikoski 时标明 v3 对已刊证明的修正，不暗示主结论被撤回。

**来源、定位与范围**

- [Merikoski: Limit points of normalized prime gaps](https://arxiv.org/abs/1811.03008)；摘要；Comments v3；2021-03-02 修订。上述部分结论及勘误范围。访问：已读作者摘要和版本说明；未读 §6 证明。
- [Merikoski 已刊论文 DOI](https://doi.org/10.1112/jlms.12314)；arXiv Related DOI。用于准确定位对应已刊版本；本次未直接读出版社全文。访问：由 arXiv 元数据核 DOI。
- [Erdős Problems #5](https://www.erdosproblems.com/5)；名称/编号搜索命中；直接打开 403。Pintz 区间结果为待核原文线索；不可称此次直读当前站点。访问：仅摘要/入口 403。
- [Formal Conjectures #5 固定题目文件](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/ErdosProblems/5.lean)；Erdos5.erdos_5；variants.pintz；import FormalConjecturesUtil。主猜想与多数已知结果以sorry登记；仅题面形式化及文献标签，不是这些定理的Lean证明。。访问：已读取对应正文。

**实际检索路径**

- 学术：`Erdos problem 5 prime gap limit points Merikoski`。
- 学术：`normalized prime gaps limit points one third bounded gaps 1811.03008`。
- GitHub/代码：`site:github.com/google-deepmind/formal-conjectures "ErdosProblems/5.lean"`。
- 公开 AI/社区：`"prime gaps" "limit points" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 补取 Pintz 关于 [0,c] 的原文及精确条件。
- 补读 v3 §6；原题站当前状态未直接获得。

### QX-P-001667 · c01878469e72e9f8 · 无挠群的 C*-刚性

出现直接改变状态的 2026-11 预印本：Curda–Hua–Slutsky 的 Theorem6.2 给无限自由积构造连续统多个不同群、相同约化群 C* 代数，且可保无挠。一般无挠群版本有完整反例声明；有限生成或可均值限制不能顺带认定。

**旧卡 → 本次处理**

- 将旧卡的“没有反例/无后续”更换为已找到 Theorem6.2 完整反例声明，待独立核证。
- 明确研究对象为约化 C* 代数；不要误改为群环或满 C* 代数。

**来源、定位与范围**

- [Curda–Hua–Slutsky: C*-algebras constructed using acyclic groups](https://arxiv.org/html/2611.21817v1)；Theorem6.2，L647–659；§6 证明及 §3 构造。一般无挠群刚性否定；取无限自由积 ℤ 为应用推断。访问：已读取对应正文。
- [原始 C*-rigidity 问题](https://mathoverflow.net/questions/483011/on-c-rigidity-problem-for-torsion-free-groups)；问题主帖。已恢复长 URL；主帖中的 we claim 是原问题的候选构造，不当作新回答证实。访问：已读取对应正文。

**实际检索路径**

- 学术：`torsion free groups C star rigidity Ozawa isomorphic reduced group C algebras 483011`。
- 学术：`nonisomorphic torsion free groups isomorphic reduced group C*-algebras counterexample`。
- GitHub/代码：`site:github.com "torsion-free" "C*-algebras"`。
- 公开 AI/社区：`"torsion-free" "groups" "isomorphic" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 初查未逐行审阅自由积 C* 代数同构及群非同构的全部依赖；没有期刊审稿或形式化核验记录。

### QX-P-001668 · 1080d693e22fb935 · EP#1 子集和互不相同（官方改判 DISPROVED=GPT-6 Astra）

已重新锁定 tadamcz/erdos1 的完整反驳声明及对应形式化命题：不存在绝对 C>0 的 2^n 下界；结论没有给出 ε 到 n 的有效规模。当前仍按完整声明待核，不继承旧“已验证”标签。

**旧卡 → 本次处理**

- 保留 claimed 层级，并更新可复现固定提交及 theorem path。
- 将反驳主命题与有效反例构造要求分开。

**来源、定位与范围**

- [Erdős #1 challenge](https://github.com/tadamcz/erdos1/blob/4b1b079aca49e7fea8ff47cc5a4e95af8285b168/Challenge.lean)；Erdos1.IsSumDistinctSet；Erdos1.erdos_1.disproof。全集子集和映射单射；N≠0；否定绝对 C。题目文件 sorry 是被比较的占位，不是最终证明。访问：已读取对应正文。
- [Erdős #1 solution entry](https://github.com/tadamcz/erdos1/blob/4b1b079aca49e7fea8ff47cc5a4e95af8285b168/Solution.lean)；import Erdos1.Resolutions.Erdos1_219usd_38h；Lean v4.28.0。已核到代码入口；主证全依赖、公理及构建未重跑。访问：已读取对应正文。
- [作者项目说明](https://github.com/tadamcz/erdos1)；README：ineffective；Comparator。作者声称经 comparator 检查，仅作为他人形式化声明。访问：已读取对应正文。
- [Erdős Problems #1](https://www.erdosproblems.com/1)；直接打开。原题入口受限，当前状态栏未直接读到。访问：入口不可达。

**实际检索路径**

- 学术：`Erdos problem 1 distinct subset sums GPT-6 Astra disproved 2026`。
- 学术：`dissociated integer sets N epsilon 2^n Erdős conjecture counterexample 2026`。
- GitHub/代码：`site:github.com "ErdosProblems/1.lean" OR "Erdos" "subset sums"`。
- 公开 AI/社区：`"distinct subset sums" (site:mathoverflow.net OR site:aixiv.science OR site:zenodo.org OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 需审核 imported resolution、lake-manifest、comparator.json 和全部公理闭包；本次未运行 Lean，不能继承第三方“已 build”结论。

### QX-P-001669 · 9d18e43a1b7bebe7 · Lovász 双临界图猜想（k≤5 已证；k=6 前沿）

标准 double-critical 猜想要求图连通。卡面删去连通条件会容许完全图外加孤立点，结论不成立。已刊原摘要支持 k≤5 的背景及部分完全图 minor 结果，未取得一般 k≥6 分类全解。

**旧卡 → 本次处理**

- 在正式题面补 connected，或明确在每个非平凡分支上谈命题。
- 不得把含 K_k minor 的弱结论提升为 G=K_k。

**来源、定位与范围**

- [Double-Critical Graphs and Complete Minors](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v17i1r87)；摘要定义和主要结论。connected 前提；complete minor 不等于图本身完全。访问：已读期刊摘要。
- [Some Cases of the Erdős–Lovász Tihany Conjecture for Claw-free Graphs](https://arxiv.org/abs/2406.15164)；摘要及版本栏。带 claw-free 等范围限制，不能充当 double-critical 全解。访问：仅摘要/版本。

**实际检索路径**

- 学术：`Erdos Lovasz double critical graph conjecture k six latest`。
- 学术：`connected double critical k chromatic graph deleting endpoints every edge k-2 complete`。
- GitHub/代码：`site:github.com "double-critical" "graph"`。
- 公开 AI/社区：`"double-critical" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 需进一步核查最新 k=6 特例与完整分类的区别；本次没有完全证明。

### QX-P-001670 · b1b50747e789f2e6 · Reed 色数上界

Reed 上界的参数解释需要改正：ω 小时猜想接近 (Δ+1)/2，不是接近 Δ+1。已取得 2007.07874 最新 v3 的 0.881/0.119 部分上界及版本说明，未找到可核全部图的 1/2–1/2 全解。

**旧卡 → 本次处理**

- 修正小 ω 的解释，并保留充分大 Δ 的部分结论限制。

**来源、定位与范围**

- [An improved procedure for colouring graphs of bounded local density](https://arxiv.org/abs/2007.07874)；摘要；v2/v3 Comments。0.881/0.119 上界与充分大 Δ 条件；v2 修正 Reed bound、v3 已刊终稿。访问：摘要和版本栏。
- [West: Chromatic number of triangle-free graphs](https://dwest.web.illinois.edu/regs/chitrifree.html)；Reed 关联段落。仅作为背景及三角形自由特例来源，不替代一般猜想最新判定。访问：已读取对应正文。

**实际检索路径**

- 学术：`Reed colouring conjecture 2026 chromatic number`。
- 学术：`chromatic number ceil Delta omega plus one over two Reed Hurley Kang`。
- GitHub/代码：`site:github.com "Reed" "conjecture" "Lean"`。
- 公开 AI/社区：`"Reed" "conjecture" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 全库候选 QX-P-000495 正文线上入口不可达，不能仅凭标题认定同题。

### QX-P-001671 · 4062b7c26ce10e48 · Goldberg–Seymour 猜想（已证+CJZ→JCO 2025→Trellis Lean 闭环）

Goldberg–Seymour 的已刊证明来源可以确认，但卡上 DOI 指向更正通知，且人话版将上界误写成恒等式。应改为 χ′≤max{Δ+1,ceilΓ}；2025-12 的更正仅处理排版。作者页另报告 Lean 完整形式化，本次未重跑。

**旧卡 → 本次处理**

- 主引用改为 DOI 01348-6，01372-6 另列排版更正。
- 将等号改上界，并保留 lower bound max{Δ,ceilΓ} 与实际取值可相差一的区别。

**来源、定位与范围**

- [Chen–Jing–Zang: Proof of the Goldberg–Seymour conjecture on edge-colorings of multigraphs](https://link.springer.com/article/10.1007/s10878-025-01348-6)；主论文 DOI；2025-09-26；摘要定理。正确的主论文入口及上界。访问：已读出版社摘要/出版信息。
- [Publisher Correction](https://link.springer.com/article/10.1007/s10878-025-01372-6)；2025-12-19 更正正文。题卡现 DOI 为更正；页码和脚注格式修改，不是撤回主定理。访问：已读取对应正文。
- [原预印本](https://arxiv.org/abs/1901.10316)；v2，2022-06-07。与已刊结果对应。访问：摘要/版本。
- [Trellis formalization project](https://www.math.cmu.edu/~wes/trellis.php)；项目成果段。作者报告形式化，不作为本次独立通过。访问：已读取对应正文。
- [Goldberg–Seymour 固定主定理](https://github.com/wpegden/goldberg_seymour/blob/88d98c1d1a59d1f1bf7c4eb58e73f3945f6daf12/Tablet/ThmGS.lean)；Tablet/ThmGS.lean；ThmGS；import GeneralHighIndexElementary。有限无环多重图的正确上界；README给Lean v4.33.0、mathlib db584cd6d46c92f209a44c0f1c829460d327499d，作者自报独立构建和标准公理闭包。此次取得主文件但未重跑。。访问：已读取对应正文。

**实际检索路径**

- 学术：`Goldberg Seymour conjecture Chen Jing Zang 2025 journal proof`。
- 学术：`multigraph edge chromatic index max Delta+1 ceiling Gamma Goldberg Seymour proof`。
- 学术：`Goldberg Seymour Trellis Lean github formalization`。
- 公开 AI/社区：`"Goldberg Seymour" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 需审核GeneralHighIndexElementary及全部传递依赖、lake-manifest和公理闭包；本次未运行任何Lean构建。

### QX-P-001672 · 06a98c58e8b21223 · 1-因子分解猜想（充分大 n 已证 CKLOT）

精确 1-factorization 阈值应为偶数 N 的 d≥2ceil(N/4)−1。CKLOT 证明覆盖充分大的 N；卡片泛称“足够高的度”容易与完全图的 perfect 1-factorization 混淆。

**旧卡 → 本次处理**

- 正式题面写明偶数 N、精确阈值、sufficiently large 的范围；2n 顶点时按 n 奇偶区分 n 或 n−1。

**来源、定位与范围**

- [Csaba–Kühn–Lo–Osthus–Treglown: Proof of the 1-factorization and Hamilton Decomposition Conjectures](https://arxiv.org/abs/1401.4159)；摘要；v2，2014-10-22。偶数 N、充分大 N 及精确 d 阈值。访问：作者摘要/版本。
- [West: 1-Factorization Conjecture](https://www.dwest.web.illinois.edu/openp/1fact.html)；原题表达。用于原题阈值映射；旧问题页并非当前完整状态证据。访问：已读取对应正文。

**实际检索路径**

- 学术：`1-factorization conjecture Csaba Kuhn Lo Osthus Treglown sufficiently large`。
- 学术：`regular graph even n D >= 2 ceil n/4 minus 1 one factorization conjecture`。
- GitHub/代码：`site:github.com "1-factorization" "conjecture"`。
- 公开 AI/社区：`"1-factorization conjecture" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 小阶剩余问题及后续是否完全覆盖待专项核查。

### QX-P-001674 · 9e8eaf0835c0f5aa · Erdős–Sós 猜想（RESOLVED 2026=GPT-6 Astra+Lean，$100）

经典 Erdős–Sós 全版本已有 Frederickson v2 的明确 Theorem1.1 与证明框架，且正文引用多个人类后续；旧卡将 Riordan–Scott 一概称幻觉不再可维持。tadamcz/erdos548 形式化仍是略强边数前提，不能单凭它覆盖经典奇偶边界。

**旧卡 → 本次处理**

- 不要以范围略窄的 Lean target 单独认证经典定理全版本；分别登记。
- 将“Riordan–Scott 幻觉”改为已有引用链、原稿本次访问受限待复核。
- 保留完整人类后续预印本的链接、定理及版本，状态不继承历史已核。

**来源、定位与范围**

- [Frederickson: Erdős–Sós via random cyclic orderings](https://arxiv.org/html/2609.21159v2)；Theorem1.1；Theorem1.2；§2.2；2026-10-22 v2。完整经典量词和后续来源链。访问：已读取对应正文。
- [Erdős #548 formalized challenge](https://github.com/tadamcz/erdos548/blob/4d1fc53e731c1bf68538543c47634ee761459ee9/Challenge.lean)；Erdos548.erdos_548。有理数边数阈值与经典严格不等式的范围差异。访问：已读取对应正文。
- [Erdős #548 solution entry](https://github.com/tadamcz/erdos548/blob/4d1fc53e731c1bf68538543c47634ee761459ee9/Solution.lean)；import Erdos548.Resolutions.Erdos548_192usd_21h；Lean v4.28.0。作者声明该模块填充 proof；本次未检查全依赖或运行。访问：已读取对应正文。
- [Riordan–Scott 后续原稿线索](https://people.maths.ox.ac.uk/scott/Papers/erdossos.pdf)；作者 PDF URL。本次访问失败；其存在的引用链与全文正确性分开。访问：全文不可达。

**实际检索路径**

- 学术：`Erdos Sos conjecture 2026 GPT-6 Astra proof 548`。
- 学术：`graphs average degree k-2 every tree k vertices Erdos Sos 2026 proof`。
- GitHub/代码：`site:github.com/tadamcz/erdos548`。
- 公开 AI/社区：`"Erdos Sos" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 需读完 Frederickson §2 关键双射与归纳；如果决定 solved，说明其证据为原稿而非本次重跑。
- 锁定 lake-manifest、公理闭包并核奇数边界是否有另外证书。

### QX-P-001675 · f66c058f0937f37c · Gallai 路径分解猜想（583.lean sorry）

2611.21673 新预印本只覆盖 K5-minor-free 连通图；例外 K3、K5−e 影响 floor(n/2) 加强版，均不否定原 ceil(n/2) 猜想。与 QX-P-000088 正文同题。

**旧卡 → 本次处理**

- 保留 K5-minor-free 范围及 floor/ceil 的区别。
- 报告与 000088 同题，暂不在线合并。

**来源、定位与范围**

- [Gallai’s path decomposition conjecture for K5-minor-free graphs](https://arxiv.org/abs/2611.21673)；摘要；2026-11-14 v1。特类及更强 floor 界例外。访问：作者摘要/版本。
- [Formal Conjectures #583](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/583.lean)；题目文件线索。直接读取失败；存在题目文件不等于证明已完成。访问：入口不可达。
- [Formal Conjectures #583 固定题目文件](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/ErdosProblems/583.lean)；Erdos583.erdos_583；IsPathSubgraph；IsDecomposition。已恢复连接器读取；有限简单连通图、edge-disjoint路径、ceil(n/2)量词明确；主定理仍为sorry占位。。访问：已读取对应正文。

**实际检索路径**

- 学术：`Gallai path decomposition conjecture November 2026 Zhang Liu Hong`。
- 学术：`connected graph edges decomposed at most ceil n/2 paths Erdos 583`。
- GitHub/代码：`site:github.com/google-deepmind/formal-conjectures "ErdosProblems/583.lean"`。
- 公开 AI/社区：`"Gallai" "path decomposition" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 需读新稿定理与证明；原网页583.lean访问失败已由固定提交连接器读取补足，当前文件仅题目占位，不能当解决。

### QX-P-001678 · 69d5401240bc5418 · Seymour 第二邻域猜想（OpenAI 声称+Lean self-reported 双轨登记）

2026-11-24 出现 Bourneuf–Charbit–Coulomb–Thomassé 的短证明预印本，已读核心 Theorem1 与证明段；旧卡“无人跟进、只有自报”过时。OpenAI 的固定提交也含对应完整目标和实际 Main 证明入口，但未独立重跑。

**旧卡 → 本次处理**

- 将旧记录补为有 2026-11-24 专业作者短证明预印本及代码；标完整声明待核。
- 正式题面改非空有限 oriented graph，精确二阶邻域定义。

**来源、定位与范围**

- [A short proof of Seymour’s Second Neighborhood Conjecture](https://arxiv.org/html/2611.32872v1)；2026-11-24 v1；§1 reduction；§2 Theorem1、Lemma2。完整原问证明声明，依赖 OpenAI reduction，非独立历史起源。访问：已读取对应正文。
- [Seymour comparator](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/SeymourSecondNeighborhood.lean)；IsOriented；secondNeighbors；exists_goodVertex。完整假设、距离恰2及 Nonempty；template 的 sorry 不当最终证明。访问：已读取对应正文。
- [SecondNeighborhood Main](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Combinatorics/SecondNeighborhood/Main.lean)；OAI.SeymourSecondNeighborhood.exists_goodVertex；导入 Reduction/Pruning/ExtremalContradiction。已读实际结论证明入口；全依赖和公理未审，Lean v4.34.1。访问：已读取对应正文。

**实际检索路径**

- 学术：`Seymour second neighborhood conjecture OpenAI proof 2026`。
- 学术：`oriented graphs second out neighbourhood 0.715538 Huang Peng proof`。
- GitHub/代码：`site:github.com/openai/math "Seymour"`。
- 公开 AI/社区：`"Seymour" "second" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 核 OpenAI reduction 与新稿 Theorem1 全证明依赖；本次初查只读关键段，没有 Lean 构建或审稿结论。

### QX-P-001680 · 7e56e8395097b9f2 · Caccetta–Häggkvist 猜想（r≥5 开放）

旧卡将 r≥5 全列未解并把 r=4 归给 Hamidoune，均需修正。West 原页明确 r=3 为 Hamidoune、r=4,5 为 Hoàng–Reed；这不解决 r 任意或三角形阈值的一般问题。

**旧卡 → 本次处理**

- 删除“r≥5 未解”，改为 r=5 已覆盖；修正 r=4 归属。
- 区分固定最小出度与有向三角形比例阈值。

**来源、定位与范围**

- [West: Caccetta–Häggkvist Conjecture](https://dwest.web.illinois.edu/openp/cacchagg.html)；L4–5 Partial results；参考文献。直接列 r=3 和 r=4,5 的归属。访问：已读取对应正文。
- [Shen: On the girth of digraphs](https://www.sciencedirect.com/science/article/pii/S0012365X99003234)；作者摘要检索；全文 403。支持 r≤5 背景；直接全文未取得。访问：仅搜索摘要；入口 403。

**实际检索路径**

- 学术：`Caccetta Haggkvist conjecture latest r 5 Hamidoune 2026`。
- 学术：`minimum out degree r directed girth ceil n/r Hladky Kral Norin 0.3465`。
- GitHub/代码：`site:github.com "Caccetta" "Haggkvist"`。
- 公开 AI/社区：`"Caccetta" "Haggkvist" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- GitHub joshp123 等审计/尝试和 wustep 有限计算只作线索，未找到全命题证书；不据搜索空白判断开放。

### QX-P-001682 · 8d08a58a02defe45 · Chvátal 韧性猜想（t₀≥9/4；稠密近正则 t₀=4）

韧性定义的人话版把比例颠倒：应为 min |S|/c(G−S)。新稿 Theorem1.3 对足够大、稠密、近正则的 4-tough 图给 Hamilton 性，只覆盖受限图类。

**旧卡 → 本次处理**

- 纠正韧性比例；保留割集导致至少两个分支的限定。
- 新结果只列为稠密近正则特类，不写 t0=4 普遍成立。

**来源、定位与范围**

- [Chvátal’s Toughness Conjecture for Dense Almost Regular Graphs](https://arxiv.org/html/2611.12519v1)；定义；Conjecture1.1；Theorem1.3。定义校正、主猜想及受限类定理。访问：已读取对应正文。

**实际检索路径**

- 学术：`Chvatal toughness conjecture 2611.12519 Shan`。
- 学术：`4 tough dense nearly regular graph delta alpha n Delta delta epsilon Hamiltonian`。
- GitHub/代码：`site:github.com "toughness" "Chvatal"`。
- 公开 AI/社区：`"Chvatal" "toughness" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 本次未逐行验证新稿证明；全库 000361 候选正文线上不可达，维持待定。

### QX-P-001683 · 8d6e0c38075d84cc · Barnette 猜想（OpenAI 声称+Li 专家解读，SOLVED_CLAIMED 中）

旧卡“没有 Lean”需要更新：固定 openai/math 提交中有 Barnette 的范围文档、完整 comparator 目标和实际 Main 证明。Li 的 2610.30490 是解释原 AI 论证的后续，不能自动当作独立发现或独立验证。

**旧卡 → 本次处理**

- 更新形式化线索为固定提交的实际代码存在，标未重跑。
- 保留 finite/simple/cubic/bipartite/planar/3-vertex-connected 的全部假设。

**来源、定位与范围**

- [Li: A note on the proof of Barnette’s conjecture](https://arxiv.org/abs/2610.30490)；摘要；2026-10-21。原论证解释稿；HTML 直接读取失败。访问：作者摘要/版本；全文不可达。
- [Barnette comparator](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/BarnetteHamiltonian.lean)；PlaneEmbedding；ThreeVertexConnected；MainStatement。全有限图、三正则、二分、平面嵌入和三点连通，结论单个 Hamilton 圈而非2-factor。访问：已读取对应正文。
- [Barnette Main](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Combinatorics/Hamiltonian/Main.lean)；OAI.Barnette.main；import ExactDual。实际主证明入口；Lean v4.34.1；全依赖和公理未审。访问：已读取对应正文。
- [Barnette formalization scope](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/docs/180.md)；Scope。作者明确声明完整覆盖上述图类。访问：已读取对应正文。

**实际检索路径**

- 学术：`Barnette conjecture OpenAI Zhentao Li 2610.30490`。
- 学术：`cubic bipartite planar 3-connected Hamiltonian cycle paired states every edge avoid`。
- GitHub/代码：`site:github.com/openai/math "Paired states"`。
- 公开 AI/社区：`"Barnette" "conjecture" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 下一步审阅 ExactDual 等依赖、comparator 配置及 Mathlib 固定版本；不把模板 sorry 当最后证明，也不把 Main 无 sorry 当整个库无额外公理。

### QX-P-001685 · f5c77bb14719183e · Tutte 3-流猜想（强形式开放）

需要明确 3-flow 的守恒是在 Z/3Z 中；若取整数流，则边值允许绝对值1、2。“±1 且整数守恒”不是标准3-flow。2609.08377 只提供带 essentially41-edge-connected 限制的进展线索。指定查重错配到5-flow，另发现 000581 才为同题。

**旧卡 → 本次处理**

- 补写守恒的群/模数；不要把 Z3 表示混成只有 ±1 的整数流。
- 查重：本题与000581同题，与000117和1686的5-flow相关但不等价。

**来源、定位与范围**

- [Li–Li: nowhere-zero3-flow 的 essentially edge-connected 进展](https://arxiv.org/abs/2609.08377)；作者摘要搜索命中；两次原入口失败。4-edge-connected 且 essentially41-edge-connected，不是所有4-edge-connected。访问：仅搜索摘要；原稿入口不可达。

**实际检索路径**

- 学术：`Tutte 3 flow conjecture Jiaao Xinyuan Li 2609.08377`。
- 学术：`4 edge connected essentially 41 edge connected nowhere zero 3 flow 2026`。
- GitHub/代码：`site:github.com "Tutte" "3-flow"`。
- 公开 AI/社区：`"Tutte" "3-flow" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 补取 2609.08377 全文核 essentially 的精确定义及割大小条件。

### QX-P-001686 · 24a4d4d2b8a41538 · Tutte 5-流猜想

旧卡引用的 oddness≤4 定理遗漏 cyclically6-edge-connected 假设，不能按该引文说所有无桥三正则 oddness≤4 已证。指定配对000581实为3-flow；新增与000117同题。

**旧卡 → 本次处理**

- 恢复 oddness 结果的循环边连通前提。
- 查重：本题与000117同题，000581为不同的3-flow。

**来源、定位与范围**

- [Mazzuoccolo–Steffen: Nowhere-zero5-flows on cubic graphs with oddness4](https://arxiv.org/abs/1412.5398)；原作者摘要；2014-12-17。cyclically6-edge-connected 且 oddness≤4 的结论。访问：作者摘要/版本。
- [作者存档全文](https://iris.univr.it/retrieve/e14ff6e5-5f7a-0209-e053-6605fe0ad24c/18_11_2015_5_Flow_odd_4_revised.pdf)；修订稿 PDF。直接读取403，不把失败当无论文。访问：全文403。

**实际检索路径**

- 学术：`Tutte 5 flow conjecture latest oddness four Mazzuoccolo Steffen`。
- 学术：`bridgeless cubic graphs nowhere zero 5 flow oddness at most 4 1412.5398`。
- GitHub/代码：`site:github.com "Tutte" "5-flow"`。
- 公开 AI/社区：`"Tutte" "5-flow" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 补取修订稿全文，区分约化定理和该特类定理。

### QX-P-001687 · 5bb17e924560187a · Fulkerson 猜想（6-完美匹配双覆盖）

命中的 Lean/AI 代码是受限 spoke C(24) 图类的可枚举证书，并未解决 Berge–Fulkerson 一般猜想。旧卡若笼统标“无AI/无代码”需改为已有特类代码线索。

**旧卡 → 本次处理**

- 记录 AI/Lean 暴露为特类已有，主猜想的量词不变。

**来源、定位与范围**

- [bf-c24 proof scope](https://github.com/frjnn/bf-c24/blob/main/PROOF.md)；PROOF.md 范围与计算说明。有限 C(24) 类及 Lean 自述；固定仓库提交另已取。访问：已读取对应正文。
- [bf-c24 固定版本](https://github.com/frjnn/bf-c24/blob/993b8caa5cd5584460b463311c2028e08198013a/PROOF.md)；2026-09-09 commit993b8caa…。固定提交已由 API 核到，原文读取为 main；未比对该路径版本和全部依赖。访问：固定提交元数据；正文 main 已读。
- [Berge–Fulkerson 后续原稿线索](https://arxiv.org/abs/2607.29511)；作者摘要搜索结果。本次直接原稿打开失败，不能据其标题认定完整解决。访问：仅搜索摘要；入口不可达。
- [2026-11 后续线索](https://arxiv.org/abs/2611.24019)；原稿访问尝试。入口 DisabledError；未核定理范围。访问：入口不可达。

**实际检索路径**

- 学术：`Berge Fulkerson six perfect matchings conjecture 2607.29511`。
- 学术：`bridgeless cubic graph six perfect matchings every edge exactly twice 2611.24019`。
- GitHub/代码：`site:github.com "Fulkerson" "conjecture"`。
- 公开 AI/社区：`"Berge-Fulkerson" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 若引用 C(24) 形式化，需锁定精确定理、工具链和全证书并重跑；本次只做范围核查。
- 全库000268候选正文线上不可达，待定。

### QX-P-001689 · 15cd2c342dadc853 · Frankl 并封闭集猜想（最佳常数 0.38289）

Costa–Sadhu 作者摘要确认0.3828852549667978的部分下界。11月18–19日 Quantavane 另自报0.38317525996679，但页面明确论文尚未投arXiv且未给可读证明，登记为部分改进声明待核。另名为 solved-conjectures 的仓库实际只给特类。

**旧卡 → 本次处理**

- 添加新部分改进声明并明确未公开全文，不把自报纪录写成已确认纪录。
- 主命题补“有非空成员”，避免 F={空集} 边界。
- 库内三个相关加权/数论变体按特例或强化报告，不能仅题名直接合并。

**来源、定位与范围**

- [Costa–Sadhu: Beyond Liu’s0.382709 threshold](https://arxiv.org/abs/2610.02295)；摘要及版本。已核作者声明0.3828852549667978。访问：作者摘要/版本。
- [Quantavane lower-bound announcement](https://quantavane.com/major-results/union-closed-sets-conjecture/)；L5–14；发布日期自报2026-11-18/19。0.38317525996679 的未公开稿声明；页面自报原稿将投，并非已刊纪录核验。访问：成果页全文；未取得证明全文/代码。
- [solved-conjectures README](https://github.com/1337isnot1337/solved-conjectures)；Frankl scope/disclaimers；提交60e47a0419d97deb104e72eb23692232430ce35f。只覆盖特类，不是半数主猜想。访问：README正文与最新提交元数据。

**实际检索路径**

- 学术：`Frankl union closed conjecture Costa Sadhu 2610.02295 0.382885`。
- 学术：`finite union closed family element at least half sets universal lower bound 2026 Demontis`。
- GitHub/代码：`site:github.com "union-closed" "Lean"`。
- 公开 AI/社区：`"union-closed" "conjecture" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 取得 Quantavane 原稿、五个不等式/interval certificates及独立程序；当前页面没有这些可核入口。
- 旧 Demontis 全证明声明如要保留，另核原文与反驳；此次不从自称标题认可。
- 全库000137正文不可达待定。

### QX-P-001690 · 1985f23fa78301de · 1/3–2/3 猜想（Aires–Kahn 2025 一般界）

主命题是存在一对元素的线性扩张先后概率落在[1/3,2/3]，不是所有元素对都不悬殊。2509.11549 的高度条件是 height o(n)，旧卡“大height”反向。新增2609.30888一般界改进线索原入口不可达；有限14阶计算不能解决所有有限偏序。

**旧卡 → 本次处理**

- 重写概率量词为存在一对；修正 height o(n)。
- 与000357同题，报告两卡参考文献差异。

**来源、定位与范围**

- [Aires–Kahn: Balancing Extensions in Posets of Large Width](https://arxiv.org/abs/2509.11549)；原作者摘要。精确的四种渐近条件；小高度而非大高度。访问：作者摘要/版本。
- [Exact verification through14 elements](https://github.com/agupta/gold-partition-conjecture)；README；commitdd1d44610be8cc2576cfeac333e45267ff349cda。有限枚举自报；未遍历数据或运行C程序。访问：已读取对应正文。
- [Breaking the Infinite Barrier in the1/3–2/3 Conjecture](https://arxiv.org/abs/2609.30888)；直接访问及学术名称查询。原入口不可达；二手摘要显示ε改进线索但不据此提升结论。访问：原入口不可达；仅二手摘要线索。

**实际检索路径**

- 学术：`1/3 2/3 conjecture Aires Kahn 2509.11549`。
- 学术：`poset balance constant width omega sqrt n height o n 1/e 2607.23926`。
- GitHub/代码：`site:github.com "poset" "1/3" "2/3"`。
- 公开 AI/社区：`"1/3" "2/3" "conjecture" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 补取2609.30888v2正文及最新版变动；目前搜索摘要日期有差异，不能确定v2改动。
- 若引用14阶计算，锁C程序构建依赖、数据校验与完整枚举范围；此次未运行。

### QX-P-001691 · 6a4c3d55fbd2eb85 · Chvátal 理想猜想（2026 双独立证明，SOLVED_CLAIMED 高）

两份原稿都明确声称证明完整 Chvátal hereditary-family 猜想；已读 Theorem1.1/1。EFF v3 自述受 CLL 启发并借AI得出证明，不能写成两个完全独立的人类起源证明。另已取得固定 boonsuan/chvatal 的主定理代码，未重跑。

**旧卡 → 本次处理**

- 旧“独立证明”改为两个完整稿件、后稿明确依赖前稿启发；分别列证据和AI披露。
- 形式化栏写已取得代码/声明对应、未重跑。

**来源、定位与范围**

- [Chang–Liu–Liu: A proof of Chvátal’s conjecture via a sharp correlation inequality](https://arxiv.org/html/2609.19123v1)；Theorem1.1；Theorem1.2。有限hereditary族D与相交A⊆D，存在坐标i使|A|≤|D(i)|。访问：已读取对应正文。
- [Ellis–Filmus–Friedgut: Chvátal’s conjecture: a proof from The Book](https://arxiv.org/html/2609.28404v3)；Theorem1；§AI disclosure L262–269；2026-10-22v3。完整声明与非独立起源说明。访问：已读取对应正文。
- [Chvatal main formalization](https://github.com/boonsuan/chvatal/blob/c19ed3aaac9e42d446f963a862d39d8a09eddbf9/Chvatal/Main.lean)；Chvatal.chvatal；exists_largest_intersecting_star；sharp_correlation；Lean v4.33.1。Finite且Nonempty坐标；主证明引用Correlation/Spectral；未审全部闭包。访问：已读取对应正文。

**实际检索路径**

- 学术：`Chvatal conjecture hereditary intersecting family Chang Liu Ellis Filmus Friedgut 2026`。
- 学术：`downset largest intersecting star sharp correlation inequality 2026 Chvatal`。
- GitHub/代码：`site:github.com "chvatal" Lean`。
- 公开 AI/社区：`"Chvátal" "2026" (site:gilkalai.wordpress.com OR site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 核Correlation和Spectral的定义、公理及全部依赖；读取lake-manifest后再谈机器通过。
- 一般空坐标/含空集的intersecting约定需在正式合并时统一，勿丢Nonempty条件。

### QX-P-001693 · 8fc2a9a42e1ca370 · Brandt 正则超图猜想

West的δ≥n/3顶点倍增版本存在9顶点反例；本次已用自写整数脚本独立核有限图条件和Farkas证书，未执行外部程序。严格δ>n/3版则已由Brandt–Thomassé Cor4.3(1)给正则权。旧卡“正则版本未被覆盖”与“无AI代码”都需纠正。

**旧卡 → 本次处理**

- ≥边界版登记已反驳，严格>版另列已证；不得继续笼统open。
- 题名改“正则超图/上图（supergraph，顶点倍增）”并解释不是hypergraph。
- 删除“4染色已证但正则本体未动”概括；直接引用Cor4.3(1)。

**来源、定位与范围**

- [West: Regular supergraphs of maximal triangle-free graphs](https://dwest.web.illinois.edu/openp/regsup.html)；Conjecture原文。明确at least n/3及vertex multiplications。访问：已读取对应正文。
- [Brandt–Thomassé: Dense triangle-free graphs are four-colorable](https://perso.ens-lyon.fr/stephan.thomasse/liste/vega11.pdf)；p5，Corollary4.3(1)；权函数定义。严格>n/3正则权结论。访问：已读取对应正文。
- [P02 counterexample data](https://github.com/jzone3/solving-math-problems/blob/4daf2214773f71daefc2c81770a64a3190b87ebd/solutions/P02/verify.py)；WITNESSES首个9顶点图；Farkas证书；commit4daf2214…。只抄录数据用本地自写程序复算；没有运行这个外部脚本。访问：已读取对应正文。
- [brandt9_check_1.json](brandt9_check_1.json)；n=9；14条边；整数Ay和图条件；pass=true。完整边集与证书及初等矛盾可复查；仅验证≥边界版。访问：已实际运行自写脚本。

**实际检索路径**

- 学术：`Brandt regular supergraph conjecture regsup triangle free`。
- 学术：`maximal triangle-free graph minimum degree n/3 vertex multiplication regular supergraph`。
- GitHub/代码：`site:github.com "Brandt" "regular supergraph"`。
- 公开 AI/社区：`"regular supergraph" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 如库内原始Brandt版本本应严格>，需编辑者决定主卡按West转述的≥版或作者原版拆分；本次两版均明确。
- 仓库Lean自报未核；我们的独立检查仅为9顶点数学证书，不继承Lean验证。

### QX-P-001694 · c6ad301484f9fa7a · L(2,1) 标号 Δ² 猜想（Griggs–Yeh；大 Δ 已解决）

Griggs–Yeh Δ²猜想须写Δ≥2。缺此前提时单边K2就有λ=2>1。Havet–Reed–Sereni已刊论文证明充分大Δ等范围，不等于所有Δ≥2已解决。

**旧卡 → 本次处理**

- 正式题面补Δ≥2，明确跨度是最大标签减最小标签而非标签数。
- 保留充分大Δ的部分结果范围。

**来源、定位与范围**

- [Havet–Reed–Sereni: Griggs and Yeh’s Conjecture and L(p,1)-labelings](https://epubs.siam.org/doi/10.1137/090763998)；摘要；2012已刊元数据。猜想Δ≥2及充分大Δ定理。访问：已读出版社摘要/元数据。
- [West:L(2,1)-Labeling](https://www.dwest.web.illinois.edu/openp/L21.html)；原题与背景。旧表述需由论文精确边界补足。访问：已读取对应正文。
- [作者HRS全文](https://lbgi.fr/~sereni/Articles/HRS08.pdf)；原稿PDF访问。访问受限，未读完整证明。访问：全文不可达。

**实际检索路径**

- 学术：`Griggs Yeh L(2,1) delta squared conjecture Havet Reed Sereni 090763998`。
- 学术：`L(2,1) labelling maximum degree span delta squared sufficiently large delta 2012`。
- GitHub/代码：`site:github.com "L(2,1)" "conjecture"`。
- 公开 AI/社区：`"L(2,1)" "conjecture" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.science OR site:eulersolve.com OR site:proofforum.org)`。

**仍需复核**

- 若要记录明确大Δ数值阈值，需要原定理全文；此初查不从摘要推算。

### 新增及易误并的查重结论

指定16对子均已核双方正文；这里突出同题和错配校正，全部关系见JSONL。

- **同题**：QX-P-001675 `f66c058f0937f37c` ↔ QX-P-000088 `af16cefc88b5d19e`。双方均对n顶点连通图要求边集分拆为至多ceil(n/2)条路径，路径的边不重用；不是路径覆盖任意重用边的变体。
- **相关但不等价**：QX-P-001685 `f5c77bb14719183e` ↔ QX-P-000117 `c9f4e5f088817ea5`。参考000117正文实际为Tutte5-flow：任意无桥图非零5流。1685是4边连通图非零3流；两处模数及连通前提均不同，原配对交叉。
- **相关但不等价**：QX-P-001685 `f5c77bb14719183e` ↔ QX-P-001686 `24a4d4d2b8a41538`。1685是4边连通图3流，1686是无桥图5流。较高连通和较小流值不是同一陈述，不能仅Tutte名称合并。
- **同题**：QX-P-001685 `f5c77bb14719183e` ↔ QX-P-000581 `bdf1329917b43115`。新增交叉校正：000581正文与1685均为每个4边连通图有nowhere-zero3-flow。整数流与Z3流按标准等价定义统一后同题。
- **相关但不等价**：QX-P-001686 `24a4d4d2b8a41538` ↔ QX-P-000581 `bdf1329917b43115`。参考000581正文为4边连通图3流，1686为无桥图5流；原配对交叉。
- **同题**：QX-P-001686 `24a4d4d2b8a41538` ↔ QX-P-000117 `c9f4e5f088817ea5`。新增交叉校正：000117正文与1686均为每个无桥图有nowhere-zero5-flow。参考卡所写三正则约化只是等价约化，不是不同命题。
- **同题**：QX-P-001690 `1985f23fa78301de` ↔ QX-P-000357 `a268c4f0cc25a76c`。两卡都对有限非链偏序要求存在x,y使随机均匀线性扩张的先后概率在[1/3,2/3]；参数定义δ(P)只是等价最大化写法。

其余新索引候选（Reed、Erdős–Sós、Seymour、Caccetta–Häggkvist、韧性、Berge–Fulkerson、Frankl相关题）已尝试取正文但受限，统一保留待定；没有按相似标题直接并题。

## 三、001695—001724

### 一、可能影响状态的新证据与冲突

#### QX-P-001696：Nash–Williams 三角分解

原卡已有完整证明线索，本次打开 [Delcourt–Postle 原稿](https://arxiv.org/html/2606.11178v1)，核到 §1.1 Conjecture 1.1 与 §1.2 Theorem 1.8：对充分大的 n，K3-divisible 且最低度至少 3n/4 的图可三角分解。K3-divisible 同时要求所有度数为偶数及边数被 3 整除，不能只保留后一条件。[版本页](https://arxiv.org/abs/2606.11178)本次显示 v1。

实际路径是题名、最低度特征、作者稿和定理定位，再查 GitHub/公开 AI 伴随声明。正确仓库名称的复查与直开均已记录；直开受阻，未取得可审计的固定提交及依赖。结论为“完整证明声明待核”，不把第三方分发页面算作新审计。

#### QX-P-001697：最大最小强定向直径的新上界

[2610.09648](https://arxiv.org/abs/2610.09648)的检索摘要报告八作者合并稿将上界改进为 ⌈d²/2⌉+d+18。原卡的旧 6d 线性项不能继续当作最新已核界。原稿直开失败，现只登记摘要级进展线索。

路径为题名、直径公式、最新稿号、GitHub 与 AI/社区查询。优先复核合并稿的准确函数定义及主定理范围；不能用摘要代替证明审计。

#### QX-P-001699：Harary–Hill 的新增 v2

[Salazar 2611.03515v2](https://arxiv.org/html/2611.03515v2)发表于本轮前一天 2026-11-25，全文可读；核到 Theorems 3、4 及 §1.2 中由奇数阶情形导出一般结论的路线。[OpenAI 项目范围说明](https://github.com/openai/math/blob/main/lean/docs/165.md)和 Comparator 入口亦已查。可以增加“出现另一份完整阐释”的证据，不能只写原项目自述。

“漏检第 13 例”是历史查新编号，不是 n=13 漏证。路径为 Harary–Hill 名称/公式、证明稿版本页、固定源码入口。仍需逐行证明审计和匹配 Lean 提交、依赖、假设；本次未重跑。

#### QX-P-001702：Brocard 的计算界和 AI 归约

[OEIS A146968 作者注记](https://oeis.org/A146968/internal)及 [Epstein–Glickman 代码入口](https://github.com/jhg023/brocard)给出已搜索至 10^15 的报告，原卡模糊的 10^9+ 数值需要更新并注明作者计算报告。

[Cryptids/Semantics/Brocard28.lean](https://github.com/google-deepmind/cryptids/blob/main/Cryptids/Semantics/Brocard28.lean)中 `halts_brocard28_iff_exists_square`、`halts_brocard28_iff_not_brocard` 是 28 态机器停机与额外 Brocard 解存在的语义对应；公开资料报告 Claude 参与。这不是证明额外解不存在。路径为 factorial-plus-one/square 名称和公式、作者代码、GitHub 定理查找及 AI 查询。另有 rxiv 完整声明，仍待全文审计；均未运行。

#### QX-P-001706：Mersenne 无穷性低强度声明

[Zenodo 18323633](https://zenodo.org/records/18323633)出现无穷性及新素数纪录的完整声明，应单列低强度待核证据，不能混同 [GIMPS 已知素数表](https://www.mersenne.org/primes/)的已验证有限记录。名称/公式、GitHub、Zenodo/社区均有实际查询。需要取得并审计声明证明及素性证书；本轮未完成该项。

#### QX-P-001708：准完全数的数值界更新

[Alekseyev 2601.17832v2](https://arxiv.org/html/2601.17832v2)的 2026-10-15 修订版 §5.1 报告排除 n≤10^90。这是比旧卡更近的计算界，原稿全文可读；作者提供代码线索，但本次未复算。

另 [2608.02066](https://arxiv.org/abs/2608.02066)的 ω≥8 仅核到摘要级证明声明，原稿访问受阻。存在性、不同素因子数下界、数值下界必须分别记。路径是 quasiperfect/σ(n)=2n+1、最新稿号、代码、公开 AI 查询及 §5.1 定位。

#### QX-P-001710：三条最长路“可能解”已撤回

[2006.16245](https://arxiv.org/abs/2006.16245)最新 v3（2024-05-06）明确撤回并说明证明错误。Open Problem Garden 中旧“Possible solution”链接不能作为已解证据。[West 原题页](https://dwest.web.illinois.edu/openp/pathtran.html)区分弦图全体最长路共点与一般连通图任三条最长路共点；[2412.20729](https://arxiv.org/abs/2412.20729)的 O(log²n) 路截集界只是部分进展。

路径为 longest paths/common vertex、chordal transversal 两组词、原稿版本和社区旧链接对照。待复核新引用链；不能从旧链接的存在推导一般三路命题成立。

#### QX-P-001711–001712：交叉数题的范围与新声明

1711 的 [Wiley 正式文献](https://onlinelibrary.wiley.com/doi/10.1002/jgt.20016)给出标准公式及参数范围：3≤m≤n 时 conjectural crossing number 是 (m−2)n。卡片写成 m(n−2)，C3□C4 的已知值 4 已反驳该字面版本。[Zenodo 22162315](https://zenodo.org/records/22162315)另有 C8□C8=48 的 AI 辅助声明，检索缓存可见而原记录返回 410，不能采为已核结果。路径为环笛卡尔积名称、公式、C7/C8 参数和代码/AI 检索。

1712 的一般图 iocr=cr 已有反例：已刊 [Odd crossing number and crossing number](https://www.cs.rochester.edu/~stefanko/Publications/DCG%20-%20Odd.pdf) p.2 Remark 2、p.11 Theorem 5.2 连同 iocr≤ocr≤pcr≤cr 区分了这些变体。新稿 [2611.21516v1](https://arxiv.org/html/2611.21516v1) Theorems 1、2 声称在完全图和完全二部图上相关量相等；§10 仍单列一般 pcr=cr 问题。已读全文及其 ChatGPT 5.6 Pro 使用声明，尚未逐行审核。路径为变体名称/符号、odd/independent/pair crossings、原论文与新稿全文；特殊图类结果不能外推到任意图。

#### QX-P-001713：素和图仍须恢复“圈”量词

[West 原帖](https://dwest.web.illinois.edu/openp/primegraph.html)问 m≥2 时的 Hamiltonian cycle，卡片人话版变成 Hamiltonian path，漏掉首尾相接。2021 年 [正式论文](https://doi.org/10.1007/s00373-020-02241-1)给出无限类的部分结果；[She 2609.19114](https://arxiv.org/abs/2609.19114)检索摘要声称充分大的所有参数，但原稿三种入口都未取得可读全文。

路径为 prime-sum graph/prime circles、Hamiltonicity 参数、作者稿和 [有限枚举仓库](https://github.com/matheth/prime-circles)。应登记“充分大参数声明待核”，不能承接旧卡已核标签；有限排列程序也不是一般证明。

#### QX-P-001714：Cohen 定义、撤回稿和 Conjecture 66 反例

[Cohen 正式稿](https://cs.uwaterloo.ca/journals/JIS/VOL28/Cohen/cohen41.pdf) p.2 中 cyclic number 指 gcd(n,φ(n))=1，绝不是十进制 142857 的循环移位。题面需重写。[Le 2509.26138](https://arxiv.org/abs/2509.26138)最新 v3（2025-11-06）仍是 withdrawn；摘要现在报告 16 个证明与 6 个否定，不能沿用旧 17/5 或把撤回稿剩余部分默认为正确。

新稿 [Ibarra 2607.09793](https://arxiv.org/abs/2607.09793)对 Conjecture 66 给出 (31,3928)，涉及 697>696 的反例；原站全文受阻，但 [同篇论文全文副本](https://www.researchgate.net/publication/409444160_A_counterexample_to_a_subadditivity_conjecture_of_Cohen_for_Sophie_Germain_cyclic_numbers) Theorem 1 与 §2 已读。Lean 附件仅作者报告，本次未取得/运行。路径为 Cohen cyclic numbers、conjecture66/subadditivity、两个稿号、撤回记录及全文副本。卡片 B/C 题族成员清单尚未固定，不能给整族统一解答状态；Conj65 原稿反例归属亦需纠正。

#### QX-P-001716：Walnut 四问已有两项新完整声明

[Fokkink 等正式稿](https://cs.uwaterloo.ca/journals/JIS/VOL28/Fokkink/fokkink9.pdf) p.9、p.16、p.18 分别给出一般 p 进数字界、Conj13、Conj16、Conj17。不能把它们继续当成一个全开放题族。

Conj16 的 [Shtrezi 2606.17447](https://arxiv.org/abs/2606.17447)声明已找到，原站失败而 [作者稿全文副本](https://www.researchgate.net/publication/407171605_The_greedy_3-sumfree_sequence_S_1gg1) Theorem 1 已读；其 g≥2 及模 10g+3 的范围与正式问题对应。Conj17 的固定提交 [a857237… / GreedyThreeSumfreeTwoParameter.lean](https://github.com/the-omega-institute/trureturing/blob/a857237bedcc80d56d3b670cd7418bfc91c54199/D5/S1/Words/Sumfree/GreedyThreeSumfreeTwoParameter.lean) 中 `theorem conjecture17` 对应 d≥2、g≥d+1 的正式版本，包含非严格边界 z≥g+d。这里只能记“已核定理对应，未重跑”；没有取得完整 imports、toolchain 与额外公理审计日志。

路径为四问名称/公式、原 PDF 编号、2026 稿号、GitHub 源码和蓝图。一般 Clergyman 与一般 p 数字界仍需分别记未找到可验证完整结果，不能被另外两问的声明覆盖。

#### QX-P-001717：No-three-in-line 的正式 AI 论文与有限纪录

[Voutier 2603.00215v2](https://arxiv.org/html/2603.00215v2)明确承认 Prellberg 对 π/√3 修正启发式的先前推导，并指出独立性假设的疑点；不能称为已证渐近式。[作者资料目录](https://wwwhomes.uni-bielefeld.de/achim/no3in/readme.html)的 2026-10-28 更新与 [QMUL 2026-11-20 报道](https://www.seresearch.qmul.ac.uk/news/5792/a-120-year-old-puzzle-a-new-world-record-and-a-student-project/)记录 n=78 的 156 点构造。

[Frontiers 正式期刊版](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1799444/full)及 [N3L_PatternBoost 作者代码](https://github.com/pranav-ramanathan/N3L_PatternBoost)已打开；Results 是有界实验，GenAI 声明中的 Gemini 用途为架构图等内容，不是一般定理证明。[另一研究笔记](https://github.com/OssaBellator/no-three-in-line-research) README 明确不声称完整证明。路径为 no-three-in-line/2n/π√3、作者纪录目录、AI 比较稿、正式期刊与代码。未独立验证 n=78 全部坐标、未运行 ILP/SAT 或模型训练。

### 二、其他明确题面与出处校正

| 题号 | 旧卡问题 → 本轮可定位的校正 | 直接出处与范围 |
|---|---|---|
| 1695 | “路径条数仅依赖 k” → 每条路径有 2k+1 条边；n 顶点时有 n/2 条路径。2024 的 k=2 部分结果还要求 3 圈与 4 圈不共边。 | [原始期刊摘要](https://onlinelibrary.wiley.com/doi/10.1002/jgt.20413/abstract)；[2024 论文](https://www.sciengine.com/cfs/files/pdfs/view/1674-7216/9A038B7537554B7284033EDD2D967FFB.pdf)全文访问受阻，只核摘要。 |
| 1697 | 对所有定向取最大 → 先对每图取强定向直径最小，再对所有直径 d 的无桥连通图取最大。 | [West 问题目录](https://dwest.web.illinois.edu/openp/)，Maximum oriented diameter。 |
| 1698 | “向集合外有足够出边” → 两个非空块各自诱导子图的最低出度。F(2,2) 的控制作用只是归约。 | [Christoph–Petrova–Steiner 正式全文](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/note-on-digraph-splitting/B377DD1BD9779DFFEE6DA45A43458ACD)，§1.2。 |
| 1700 | 将 196 候选轨迹与十进制 Lychrel 存在性混写 → 拆成两个子问，有限迭代不证明永不回文。 | [p196 作者项目](https://www.p196.org/)，首页及研究入口；[研究稿源码](https://github.com/nkc-daiki/196-carry-asymmetry/blob/main/paper.tex)尚未证明审计。 |
| 1704 | 2307.07894 写 v4 → 最新版本页为 v3（2024-09-09），并给 JNT 261(2024)190–219。 | [原稿版本页](https://arxiv.org/abs/2307.07894)；[FibonacciPrimes.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Wikipedia/FibonacciPrimes.lean)的主无穷性命题仍有 `sorry`，已证等价归约不能替代它。 |
| 1709 | 11+11 个整数全部互异 → 标准 PTE 理想解允许各侧内部重复，要求两整数多重集不相交。全部互异是加强变体。 | [2304.11254 正式论文稿](https://arxiv.org/pdf/2304.11254)，p.1 定义、p.2 尺寸清单；其他数域解不能当整数解。 |
| 1715 | 把 Two Mersenne Prime Conjectures 读成 double Mersenne → 恢复 Wagstaff 两子问。 | [wag14.pdf](https://cs.uwaterloo.ca/journals/JIS/VOL28/Wagstaff/wag14.pdf)，p.2 Conjectures 1、2。第一问的奇正整数 p 条件为 p=2^k±1 或 4^k±3、M_p 素、(2^p+1)/3 素，任二推第三；第二问为 Chen 的最小 Mersenne 素数同余断言。 |
| 1716 | anti-k-nacci 当成前 k 项反号线性递推 → mex/缺失数构造；Clergyman 余项须写 X_n−(k²+1)n。 | [fokkink9.pdf](https://cs.uwaterloo.ca/journals/JIS/VOL28/Fokkink/fokkink9.pdf)，p.16 Conj13。 |
| 1717 | “2n 是下界” → 2n 是每行至多两点得到的上界，只有已构造尺寸知道能达到。 | [Voutier v2](https://arxiv.org/html/2603.00215v2)，§1。 |
| 1718 | 截断和伪歧义 → 每块只需接触最初 T0，允许任意旋转平移；原帖给最多 12 块的说明。 | [MSE 原帖](https://math.stackexchange.com/questions/4932685/placing-triangles-around-a-central-triangle-optimal-strategy)，2024-06-20 作者回复；2024-06-21 SG 评论是条件性框架，不是一般策略。 |
| 1719 | 漏“同构类型”、retract 误作核 → 数实际子群的现卡字面版被 Z² 的 H_n=〈(1,n)〉反驳；原问按同构分类。 | [MSE 4528730](https://math.stackexchange.com/questions/4528730/does-every-finitely-generated-group-have-finitely-many-retracts-up-to-isomorphis)，标题与末段。r_n(x,y)=(x,nx)，所有 H_n 都同构于 Z；也不能沿用原帖“所有有限生成阿贝尔群”都有无穷收缩子群的过强括号。 |
| 1721 | 最小类的伪歧义、阿贝尔成员过窄 → 只用明示的半直积闭包，阿贝尔成员可跨素数作直积。 | [原 MSE](https://math.stackexchange.com/questions/127090/what-groups-are-semidirect-products-of-simple-groups)及新定位 [MO 338374](https://mathoverflow.net/questions/338374/explicit-description-of-the-smallest-class-of-groups-that-contains-all-finite-s)。C6 在内，C4 不在；不额外要求子群/商闭包。 |
| 1724 | 截断后是否有隐藏限制 → 后文只有数表、图像和另题链接；取 n≥1，是否允许 n=0 不改变值域。 | [MSE 5065227 全文](https://math.stackexchange.com/questions/5065227/is-fn-lfloor-n-sin-n-rfloor-an-mathbbn-to-mathbbz-surjection)。m∈Z、弧度、左闭右开区间不变；独立随机模型评论不是确定序列的证明。 |

上述题面校正均由名称/编号和公式/数学特征两类查询进入，并另做代码、公开 AI/社区及全库索引检索；精确查询逐条见 JSONL。未逐站查询的 aiXiv、Zenodo、EulerSolve、ProofForum 等入口不会写成“已无命中”。

### 三、查重的新判断

所有 24 组指派配对均已对照包内双方正文；JSONL 含双方 id、card_rev、关系和量词差异。没有执行任何合并。

- **新增同题**：QX-P-001706 `a047af0d051c4e47` 与 QX-P-001705 `8b406eaf03a07591`。两卡正文均问 2^p−1 为素数的 p 是否无穷；1705 的主栏缺失不改变其人话版的实际命题。
- **子问重叠，不能整卡合并**：QX-P-001715 `66bc1655dcb61c8c` 与 QX-P-000040 `88db22983222d85a`，后者仅含新 Mersenne 第一子问；000040 条件里的 4^k±3 还需校正。QX-P-001716 `c9fa7edee683dc61` 与 QX-P-001806 `15799f797ad9f44b` 仅在 Clergyman 一问重叠；其余三问不同。
- **加强/特例**：1702 与 000002、002321；1706 与 000384。具体参数域、平方根余数限制、幂距离条件和一次素因子条件已逐对写入 JSONL。
- **明确不同命题**：1704 的 10 个候选、1707 的 5 个候选，以及 1696–1198、1697–1681、1716–1238、1718–0836，均不可仅凭 Fibonacci/素数/同名猜想/博弈等词合并。
- **新增待定线索**：QX-P-001710 `08df63cdab56d796` 与 QX-P-000004 `80b48f660aae4c1f`。全库索引显示后者可能对应三路子问，但本包未提供其正文，故仅登记待定，未认定等价。

### 四、优先复核点

优先取得 1697、1713 和 1708 的受阻原稿，核新界或“充分大”定理的完整条件；取得 1711 的失效 Zenodo 声明及证书；固定 1714 题族成员和 Conj66 的附件；对 1716 Conj17 检查完整 toolchain、imports、额外公理及正式题意对应后再考虑运行。1696、1699 等已经取得完整公开证明稿的条目，也仍需独立证明审计才能从“完整声明待核”升级。

原帖无回答、搜索无命中、形式化文件中出现定理名、有限范围计算，均没有被用作一般开放或一般已解的单独证明。

## 四、001725—001750

### 需优先复核的 5 项

#### QX-P-001735（版本 d4329968bea4d7d3）

发现原卡漏掉的MO交叉帖#258647及2026-08-11预印本2608.10381v1。Corollary6.2给精确所求域；MO提供GPT pro辅助证明，预印本致谢说明ChatGPT/Codex完成证明发现与文献导航。作者报告已核，本轮只核定理对应，未独立验证全证明。

**旧卡应变更处：** 升为P0完整肯定解声明待核；补MO#258647及arXiv；删除“十年零进展、AI暴露无”；区分作者验与本轮验。

**按子问的判断：**

- 存在F≅F(x,y)且F≇F(x)：**完整证明/反例声明待核**。Corollary6.2直接构造F=Frac Q[A]，A为Z[√2]中的有界序列加法群；依赖Theorem1.1与Rickard2020。

**直接证据与定位：**

- [Lin–Wang: Reconstruction of Torsion-Free Abelian Groups from Rational Group Fields](https://arxiv.org/html/2608.10381v1)：Theorem1.1，§6 Corollaries6.1、6.2，Acknowledgements。证据：预印本完整证明声明；作者称已独立核验；访问：已取得HTML并核对终端定理范围；未独立验证全证明。
- [版本记录](https://arxiv.org/abs/2608.10381)：v1 2026-08-11，未见后续版本/撤回标记。证据：arXiv版本页；访问：已打开。
- [MO交叉帖回答](https://mathoverflow.net/questions/258647/is-there-a-field-f-which-is-isomorphic-to-fx-y-but-not-to-fx/513970)：Claim、Theorem4、Lemma6、Corollary7；GPT pro归属与作者checked声明。证据：社区完整证明声明；访问：已打开正文。
- [原始MSE帖](https://math.stackexchange.com/questions/2000333/is-there-a-field-f-which-is-isomorphic-to-fx-y-but-not-to-fx)：2017-01-03交叉帖评论。证据：原始题文；访问：已打开。

**实际检索路径：** `field isomorphic F X Y not F X rational functions`；`field stable isomorphism two variables one variable cancellation infinite transcendence`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 优先独立核Theorem4.3/5.1的缺陷群自由性和相对超越次数；核Rickard2020原定理；无形式化复跑。

#### QX-P-001728（版本 c28f9928d4e2594a）

Hill v3 仍是完整不存在声明，已取得 HTML 但未独立审完证明。现卡“有理数域已存在、整数未决”错误：有理平方解可清除平方分母化为整数平方解。Rome–Yamagishi 的 n≥4 结果不覆盖3。

**旧卡应变更处：** 删除“有理数域上已存在”的错误补注；Hill保留待核；n≥4进展与n=3分栏。

**按子问的判断：**

- 3×3 九个相异整数平方魔方的不存在性：**完整证明/反例声明待核**。Hill arXiv:2510.08286v3 声称不存在；本轮未验关键推导。
- 有理平方与整数平方分离：**题面有误**。若各项为r_ij²且r_ij∈Q，取所有分母公倍数D，则乘D²后仍为相异整数平方幻方；反向显然。

**直接证据与定位：**

- [On Arithmetic Progressions and a Proof of the Nonexistence of Magic Squares of Squares](https://arxiv.org/html/2510.08286v3)：§3.2；版本日期2026-04-07。证据：预印本完整声明；访问：已取得HTML；未逐行验证。
- [On the existence of magic squares of powers](https://arxiv.org/abs/2406.09364)：摘要；v2 2024-09-04。证据：预印本；访问：已打开摘要及版本记录。
- [The algebraic geometry of 3-by-3 magic squares of squares](https://arxiv.org/abs/2609.09351)：搜索索引摘要。证据：预印本摘要索引；访问：摘要页及HTML打开失败DisabledError。

**实际检索路径：** `magic square squares Hill 2510.08286 2609.09351`；`3 by 3 distinct rational squares magic square integer denominators proof`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 核验Hill §3.2及关键整除/范围假设；2609.09351本轮未取得正文。

#### QX-P-001738（版本 ae293eb958a473a4）

补全原帖缺失的稳定子相容条件与有限正交作用目标。原帖宣称自由作用下普通提升可选G等变并不成立；本轮构造圆周二重覆盖反例，故原卡不能把普通覆盖提升判据直接当等变判据。

**旧卡应变更处：** 标注背景断言错误；加入本轮反例供独立核算；恢复稳定子条件及有限正交作用版本；不要把反例写成一般判据已完成。

**按子问的判断：**

- 普通提升自动可选G等变的背景断言：**原题已反驳**。本轮直接核算：G=C2反足作用于X=Y=S1，p(z)=z²，fbar(w)=w²。4Z⊂2Z满足π1条件且稳定子平凡；仅两提升f(z)=±z²，均f(-z)=f(z)≠-f(z)。
- 一般非自由作用等变提升的完整判据：**未作判断**。上述反例指出缺失单值化/作用相容条件，并未给所有非自由作用分类。
- 反例图与原假设复核：**题面有误**。本轮再读原文无monodromy/G自同构兼容假设。图：X=Y=S1，G=C2在两者反足作用，pX(z)=pY(z)=z²，底图fbar(w)=w²。提升满足f(z)²=z⁴，所以连续提升仅±z²；均f(−z)=f(z)≠−f(z)。π1条件4Z⊂2Z及平凡稳定子条件成立。父代理亦独立手核此短反例；不解决一般非自由提升准则或有限维向量空间特例。

**直接证据与定位：**

- [Lifting criterion for quotient spaces of non-free group actions](https://math.stackexchange.com/questions/4218457/lifting-criterion-for-quotient-spaces-of-non-free-group-actions)：正文(1)、Moreover句及Compatibility；无monodromy兼容附加假设。证据：原题及作者澄清；访问：已打开完整文字。
- [Hatcher, Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf)：印刷p61 Proposition1.33（PDF页索引69）。证据：教材原文；访问：已取得PDF文字；命题只承诺普通提升。

**实际检索路径：** `lifting criterion quotient spaces non free group actions David Sheard`；`equivariant lift quotient map nonfree discrete action stabilizer fundamental group criterion`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 反例为本轮手工推导，未形式化；一般判据需补单值化/作用群同态相容条件后重述。

#### QX-P-001745（版本 5ce6e480910939ae）

原帖先承认数码和趋无穷已知，真正问f(s)最大指数是否O(s)。原帖Update1强猜想在允许a=20时被尾零不变性直接反驳；这是本会话手核，与未解线性增长问分开。2026版Radcliffe只给特定底数对数下界、一般Stewart型log n/loglog n下界。

**旧卡应变更处：** 题名和主问恢复f(s)的线性界；删“是否趋无穷”开放叙述和未经证实的平均线性已知说法；Update1独立标反例，Update4亦须处理a带10因子的尾零归一化。

**按子问的判断：**

- s10(2^n)→∞：**原题已证**。这只是卡片通俗版子问；原帖与Radcliffe §1/§3明确为已知。非本轮首证。
- 对固定a非10的幂，f(s)=max{k:S10(a^k)≤s}是否O_a(s)：**暂未找到可验证结果**。
- 原帖Update1对所有允许a断言liminf S10(a^k)/k>log2 a：**原题已反驳**。本会话直接推导：a=20时S10(20^k)=S10(2^k)≤9(floor(k log10 2)+1)，故limsup≤9log10 2≈2.7093<log2 20≈4.3219。不反驳存在某正线性下界。

**直接证据与定位：**

- [Sums of digits of powers of integers](https://mathoverflow.net/questions/38971/sums-of-digits-of-powers-of-integers)：正文及Updates1–4；未限定gcd(a,10)=1。证据：原始提问与猜想原量词；访问：已打开正文。
- [Elementary Bounds on Digital Sums of Powers, Factorials, and LCMs](https://arxiv.org/abs/2511.15850)：v2修订2026-01-07，comments明确纠正旧稿错误；HTML自身Date显示2026-08-24，与submission date不同。证据：作者预印本版本记录；访问：已打开摘要版本页。
- [Radcliffe v2全文](https://arxiv.org/html/2511.15850v2)：§4 Theorem4有额外d条件；§6 Theorem6一般logn/(loglogn+C)；c_b统计非零数码，进而下界适用于数码和。证据：预印本，已核定理范围未逐步复证；访问：已打开定理与相关证明。

**实际检索路径：** `"Stolarsky" "digit sums" powers 2026`；`"2511.15850" "38971" OR "sum"`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 线性下界/最优增长未取得证明；未复证Radcliffe全文；本轮反例未形式化。

#### QX-P-001748（版本 10b1900f58fcb0e4）

原问是乘积具有有限维CW同伦型，非本身有限胞腔CW。对两个非空因子，投影-截面给同伦支配，Hatcher A.11的望远镜证明给维数≤n+1的CW模型，故该有限维结论有教材证明支持。空因子是原帖评论的平凡例外。

**旧卡应变更处：** 题名改为非空因子的有限维CW同伦型继承；将教材结论与原误写的有限胞腔版分开；claimed可按修正后有限维子问升级为有定理证明支持。

**按子问的判断：**

- X,Y非空，X×Y≃n维CW⇒各因子有有限维CW同伦型：**原题已证**。本轮核Hatcher A.11 pp.528–529的证明：若h:X×Y→K、g为同伦逆，则X→K取h(x,y0)，K→X取prXg，复合≃idX；将其反向复合做cellular映射望远镜，维数≤n+1。Y同理。教材定理应用已手核，未形式化。
- 原文未排除Y=空集的存在问：**原题已证**。任意非有限维同伦型X乘空集为空CW；原评论已指明。应补非空才能表达本意。
- 有限胞腔/实际CW结构的卡片版本：**题面有误**。不由有限维同伦型定理解决；本次对此另版未作判断，不保留旧备注“Wall障碍未解决”的绝对状态。

**直接证据与定位：**

- [Product finite-dimensional CW homotopy type](https://mathoverflow.net/questions/267669/if-x-times-y-is-homotopy-equivalent-to-a-finite-dimensional-cw-complex-are-x)：原问；Rot空集评论；Goodwillie与Hatcher2017-04-20评论。证据：原题、证明路线及教材作者解释；访问：已打开正文与可见评论。
- [Hatcher Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf)：Appendix Proposition A.11，印刷pp.528–529（PDF536–537）；望远镜证明全文。证据：教材定理和证明；本轮核定应用；访问：已打开PDF并读完整该证明。
- [Wall Finiteness conditions for CW complexes](https://math.uchicago.edu/~shmuel/tom-readings/wall%20finiteness%201.pdf)：原帖指Theorem E p.63；本轮PDF可取但文本层空，仅请求p.63截图。证据：原文补充路线；本结论不依赖此未精读页；访问：PDF可取、无文本提取；未逐行核该定理。
- [UQ152 AI answers](https://uq.stanford.edu/question/152)：多模型相反回答；o3等标UQ Validated同时Needs Human Verification，0humanreviews。证据：公开AI声明，非独立验证；访问：已打开正文。若声称维数总≤n，需低维例外分析；本回传只用≤n+1。

**实际检索路径：** `"product" "finite-dimensional" "CW" "Goodwillie"`；`"267669" "CW"`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 未核维数≤n的所有低维例外；未审独立的有限胞腔/同胚版本；未取得同题形式化代码。

### 其余题面、出处和查重修正

#### QX-P-001725（版本 0dce4665d1c83a1b）

原帖讨论每个圆心的单位圆；现卡草稿写成“对某个 x”将问题大幅弱化。原帖可见评论明确排除仅原点的构造，普通对称度量为前提；未发现可核完整解。

**旧卡应变更处：** 将“对某个 x”改为“对每个圆心 x”；区别所有半径与仅半径1；明确普通对称度量。

**按子问的判断：**

- 所有圆心的单位圆均为通常直边三角形：**暂未找到可验证结果**。
- 草稿仅要求某个圆心：**题面有误**。原帖评论明确说只有原点一个单位圆不能回答原问题。

**直接证据与定位：**

- [Is there a metric on the plane for which (unit) circles are triangles?](https://math.stackexchange.com/questions/4769164/is-there-a-metric-on-the-plane-for-which-unit-circles-are-triangles)：原题及 Kohan 评论（每个单位圆；只有原点不够）。证据：原始提问及评论；访问：已打开正文，部分评论折叠未取。

**实际检索路径：** `metric plane unit circles triangles Mees de Vries`；`metric usual topology all spheres triangular circles 4769164`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 隐藏评论未展开；未对一般度量证明不可行。

#### QX-P-001726（版本 ea876c555ce0fb83）

原帖和交叉帖已核：nontrivial 指非平庸拓扑，并不要求 Hausdorff。MO 唯一回答明确撤回反例。现卡“至少两点”定义不足；不可将该回答作为解答。

**旧卡应变更处：** 将非平凡条件改为拓扑不等于{空集,X}；记录 Hausdorff 为另外的限制版本；保留反例撤回信息。

**按子问的判断：**

- 非平庸拓扑的无限幂积/盒拓扑是否同胚：**暂未找到可验证结果**。
- nontrivial 的定义：**题面有误**。至少两点仍允许反离散拓扑；该情形两拓扑相等，原帖明确排除。

**直接证据与定位：**

- [Product versus box powers](https://mathoverflow.net/questions/431630/can-xi-product-topology-and-xi-box-topology-be-homeomorphic-for-some/431987)：问题 EDIT；回答开头自撤及尾部作者评论。证据：原始交叉帖及撤回回答；访问：已打开正文。

**实际检索路径：** `product box topology homeomorphic nontrivial space 4430813 431630`；`homeomorphic product box infinite power nonmetrizable counterexample`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 检索的代码/AI域组合未取得同题证明；不以此断言问题开放。

#### QX-P-001727（版本 61d90a74083c29b4）

原帖 Edit 已给 κ^ℵ0=κ 的肯定解，存在某个不可数 κ 的字面问题由 κ=c 即解决；余问需重写为指定 κ，尤其 κ^ℵ0>κ。

**旧卡应变更处：** 补全原帖 Edit；分离已肯定的存在版本与剩余逐基数版本；保持拓扑嵌入而非等距嵌入。

**按子问的判断：**

- 存在某个不可数 κ 的字面命题：**原题已证**。原帖 Edit 引 Kowalsky：J(κ)^N 包含权≤κ 的全部可度量空间；κ=c 时基数仍c。此处基数计算为本轮核对。
- κ^ℵ0>κ 的逐基数版本：**暂未找到可验证结果**。

**直接证据与定位：**

- [Universal space of cardinality kappa](https://math.stackexchange.com/questions/4084662/is-there-a-topological-space-of-cardinality-kappa-containing-all-metric-space)：2021-04-07 Edit：κ^ℵ0=κ 的正答案及余问。证据：原始提问的修订；访问：已打开正文。
- [原帖链接的 Kowalsky 简证](https://www.ams.org/journals/proc/1979-075-01/S0002-9939-1979-0529240-7/home.html)：原帖链接17。证据：期刊文献入口；访问：403，未取得全文。

**实际检索路径：** `universal metrizable space cardinality kappa Kowalsky hedgehog 4084662`；`Kowalsky embedding theorem hedgehog countable product cardinality`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 期刊原证明全文403；κ^ℵ0>κ 的现状需要进一步文献核查。

#### QX-P-001729（版本 42047645df169545）

MO 原帖完整正文将五档答案明确写为∞,∞,?,?,18，与旧备注称后四档全部开放冲突。每种至少k份也无上界；2-isohedral 上界18是作者依据分类论文报告，论文访问失败需复核。

**旧卡应变更处：** 补齐五档，不再称至少k份或2-isohedral均开放；18以作者报告待论文复核标注。

**按子问的判断：**

- 每种至少一份；至少任意给定有限k份：**原题已反驳**。原帖给中心N边形/再分k楔构造，边数均无上界。
- 每种无限份；每块邻接异类：**暂未找到可验证结果**。
- 2-isohedral 最大18：**完整证明/反例声明待核**。原作者引用分类论文p109并明确声称最优18；本轮论文入口不可达。

**直接证据与定位：**

- [If two convex polygons tile the plane, how many sides can one of them have?](https://mathoverflow.net/questions/382345/if-two-convex-polygons-tile-the-plane-how-many-sides-can-one-of-them-have)：五档条件及末尾∞,∞,?,?,18；正文两构造与p109。证据：原作者构造及文献声明；访问：已打开正文。
- [原帖2-isohedral分类文献](https://doi.org/10.1007/BF00147644)：原帖链接15；p109待核。证据：已刊论文入口；访问：重定向后不可达。

**实际检索路径：** `two convex polygons tile plane maximum sides 3984049`；`convex two prototile tilings polygon sides infinite copies 382345`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 取得分类文献核p109，确认几何边数与接触次数对应；无限份和异类邻接两档继续初查。

#### QX-P-001730（版本 e3abf8516680a106）

原帖无可核完整论证；可见2020评论直接从erf表达式断言有理值必为0，缺少所需超越性步骤，不能采纳。正确变换是erf(q/√2)，参数不再一般是有理数。

**旧卡应变更处：** 使用精确等价式 erf(q/√2)=2Φ(q)-1；不把未证明的评论升级为解。

**按子问的判断：**

- q∈Q且Φ(q)∈Q是否强制q=0：**暂未找到可验证结果**。
- 将erf参数写为任意非零有理数的等价改写：**题面有误**。q/√2通常无理，必须保留该参数集。

**直接证据与定位：**

- [Rational values of normal CDF](https://math.stackexchange.com/questions/2248589/is-phiq-rational-for-some-q-in-mathbbq-where-phi-is-the-standar)：原式及2020-06-10评论。证据：原始提问/评论；访问：已打开正文。
- [NIST DLMF 7.1](https://dlmf.nist.gov/7.1)：Alternative notations: Φ(z)=erfc(-z/√2)/2。证据：权威函数定义；访问：已打开正文。

**实际检索路径：** `normal CDF rational rational point erf irrational 2248589`；`Gaussian integral rational algebraic point error function Siegel Shidlovsky sqrt pi`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 仍需针对Φ值域的独立超越性来源；搜索命中的AI生成解答不作为证据。

#### QX-P-001731（版本 37078bc4139f5463）

原题确为不加交换律的自由medial magma。取得Ježek–Kepka1981原文，p223所称entropic特指medial cancellation的同态像，另构造交换medial；不能由书名推断已解一般题。

**旧卡应变更处：** 补原文p223、p225的定义和范围定位；不要将entropic历史用法直接等同一般medial。

**按子问的判断：**

- 一般自由medial magma标准形：**暂未找到可验证结果**。
- 交换/可消去或entropic定义下的自由对象：**部分进展**。1981原文明确区分附加性质，不覆盖一般非交换版本。

**直接证据与定位：**

- [Free medial magmas](https://math.stackexchange.com/questions/271611/free-medial-magmas)：问题全文及2013、2025评论。证据：原始提问；访问：已打开正文。
- [Ježek–Kepka, Free entropic groupoids (1981)](https://www.dml.cz/bitstream/handle/10338.dmlcz/106070/CommentatMathUnivCarol_022-1981-2_2.pdf)：p223定义；p225命题1.2、1.3。证据：已刊原文；访问：已取得PDF文字。

**实际检索路径：** `free medial magma explicit description Jezek Kepka`；`free entropic groupoid binary trees normal form medial law`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 未核一般自由medial对象全部后续文献；未进行形式化重跑。

#### QX-P-001732（版本 2b60d79731b79692）

原题为固定六运算签名的等式理论；min或指数扩张的不可有限基结果不直接适用。现卡中文将原文“倒数第二条可由前述推出”误写为“最后一条可由前一条推出”。

**旧卡应变更处：** 更正second last翻译；附加min算子的文献与原签名分开。

**按子问的判断：**

- (N,0,1,+,×,gcd,lcm)有限等式基：**暂未找到可验证结果**。
- 列举恒等式的推导说明：**题面有误**。原文 second last 指gcd(a+b,lcm(a,b))=gcd(a,b)，并非乘积恒等式。

**直接证据与定位：**

- [Finite identities for natural number gcd/lcm algebra](https://math.stackexchange.com/questions/1855226/is-there-a-finite-list-of-identites-in-the-language-of-mathbbn-0-1-times)：恒等式表及其后一句；Makholm的min评论。证据：原始题文；访问：已打开正文，9条评论折叠。

**实际检索路径：** `natural numbers gcd lcm equational theory finitely axiomatizable 1855226`；`identities semiring greatest common divisor least common multiple finite basis`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 折叠评论和2019撤回回答未取；未找到固定签名的完整结论。

#### QX-P-001733（版本 409ea2db1c202aa3）

原帖有限版本是R³中有界集合E内的有限稳定簇；两平板仅是无限版引子。8000构造为作者图片和小扰动说明，本轮未取得坐标或严格锁定证明；36只是评论建议。

**旧卡应变更处：** 恢复有限版bounded E∈R³量词；删除未经原文支持的“只靠平移”；8000注明作者报告，36非已证。

**按子问的判断：**

- 有限全等凸体稳定簇最小个数：**暂未找到可验证结果**。
- 8000个四面体给上界：**完整证明/反例声明待核**。原作者给可视构造说明，未提供可独立复现参数。
- 限定仅平移、限定有限版在平板间：**题面有误**。原文Finite Case用bounded E，移动方式没有只许平移的附加限制。

**直接证据与定位：**

- [8000 congruent convex asteroids](https://math.stackexchange.com/questions/4934035/8000-congruent-convex-asteroids-can-form-a-stable-cluster-how-much-better-can)：The Finite Case及The Question；2024-07-21评论。证据：原始构造声明/评论；访问：已打开完整文字，图片未做三维验证。

**实际检索路径：** `8000 congruent convex asteroids stable cluster Thickland`；`Winkler trapped Thickland finite tetrahedra cluster minimum`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 索取/定位8000构造参数与所有刚体路径阻挡证明；最小个数未核定。

#### QX-P-001734（版本 f54618f37142dac4）

定位到1962 Schweitzer第1题及已出版解答书目，但官方解答正文尚未取得。另同题MSE#4051473有估值/整数值集证明草稿及偶数次数质疑，不能当本轮无缺口验证；原解答链接docdroid现404。

**旧卡应变更处：** 补a,b∈Q及a≠0；官方证明需准确页码；同题社区答案仅作辅助。

**按子问的判断：**

- 有理系数同值集当且仅当有理仿射换元：**完整证明/反例声明待核**。本轮证据仅为原帖的1962 Schweitzer第1题出处说明和解答书目；官方解答正文与准确页码未取得。这里标记本轮核验边界，不将该经典题断言为未解。

**直接证据与定位：**

- [Polynomials with same image on the rationals](https://math.stackexchange.com/questions/2269855/polynomials-with-same-image-on-the-rationals)：2020-02-01评论明确1962年第1题。证据：出处确认；访问：已打开正文。
- [Contests in Higher Mathematics: Miklós Schweitzer Competitions 1962–1991](https://link.springer.com/book/10.1007/978-1-4612-0733-7)：目录：Solutions to the Problems pp55–563；具体本题页码待取得全文。证据：出版社书目；访问：搜索返回出版社正文，未取得解答章全文。
- [Determining a polynomial from rational image](https://math.stackexchange.com/questions/4051473/determining-a-polynomial-p-from-its-image-of-rationals)：原题要求a,b∈Q且a≠0；reuns回答和偶数次数评论。证据：同题社区证明草稿；访问：已打开正文。
- [原官方解答分享链接](https://www.docdroid.net/vyGkcyK/solution.pdf)：MSE原帖链接24。证据：失效分享链接；访问：404。

**实际检索路径：** `polynomials same image rationals Schweitzer 1962 problem 1`；`P Q polynomials rational value sets affine substitution 2269855`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 官方解答正文未取得；实系数到有理系数的化约需单独核对，不由竞赛有理版本自动升级。

#### QX-P-001736（版本 babba2a41bd5d2da）

MO2026-10-22回答确有已列三类部分结果，结尾明确AI辅助；原卡“AI暴露无”错误。本轮取得Yuan–Li PDF p2，正平方判别式的二有理根判据对应准确。其余一般情形未解；D≤0需a|b不能遗漏。

**旧卡应变更处：** 补正AI参与标记；按D及a|b拆子问；勿将一般有理根与整数根差等同。

**按子问的判断：**

- D=k²a²充分性：**原题已证**。原帖有限望远镜和可核；根差为非零整数。
- D>0完全平方时逆命题：**部分进展**。Yuan–Li p2明确二有理根和的超越性当且仅当根差非整数；平移去除有限项可对应。
- D≤0且a|b：**部分进展**。MO回答依Nesterenko及π²公式；已核范围，Nesterenko原证明未重核。
- D>0非平方，或D≤0且a∤b：**暂未找到可验证结果**。

**直接证据与定位：**

- [jvvk部分回答](https://mathoverflow.net/questions/498167/when-is-the-series-sum-n-1-infty-frac1a-n2-b-n-c-rational)：2026-10-22；三编号段；末尾AI辅助声明。证据：社区证明；援引已刊结果；访问：已打开完整文字。
- [Yuan–Li: On the transcendence of some infinite sums](https://arxiv.org/pdf/0909.2387)：p2：α/((qn+s1)(qn+s2))判据。证据：原作者预印本，记载2001判据；访问：已取得PDF并定位p2。
- [原帖](https://math.stackexchange.com/questions/5079671/when-is-the-series-sum-n-1-infty-frac1a-n2-b-n-c-rational)：(a)有限望远镜求和。证据：原始题文；访问：已打开。

**实际检索路径：** `rational series quadratic denominator converse 5079671 498167`；`Adhikari Saradha Shorey Tijdeman rational infinite sums quadratic denominator 2001`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 核Nesterenko Cor6原文；原帖b部分的tan公式与p,q替换可疑，不作依据。

#### QX-P-001737（版本 f7cb67e809ec7458）

原始MSE与MO均已打开。MO主动将“不用一阶模型论”从主问题降为附带偏好；MSE2024评论说明即便允许模型论也未见证明。应先问ZFC存在性，再分方法限制。

**旧卡应变更处：** 区分存在性主问题与证明方法偏好；把两种原文版本同时标明。

**按子问的判断：**

- 每个可数无限结构存在ω上非刚性超幂：**暂未找到可验证结果**。
- 不依赖一阶模型论的限制：**未作判断**。MO新版仅作为偏好，不是主命题假设。

**直接证据与定位：**

- [Non-rigid ultrapowers in ZFC](https://mathoverflow.net/questions/408178/non-rigid-ultrapowers-in-mathsfzfc)：主问题及minor aside/降为side comment段。证据：原作者交叉帖修订；访问：已打开正文。
- [原始提问](https://math.stackexchange.com/questions/4293034/non-rigid-ultrapowers-in-mathsfzfc)：2024-05-12作者评论。证据：原作者状态说明；访问：已打开正文。

**实际检索路径：** `non rigid ultrapowers ZFC Noah Schweber`；`countable structure nontrivial automorphism some ultrafilter omega ZFC Shelah`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** Shelah/Keisler相关定理不等价于本题；未核查所有后续引文。

#### QX-P-001739（版本 22ea84589ec502ac）

发现精确OEIS A369858（2024建），原卡“OEIS无对应序列”错误；OEIS明确固定元素定义、代码及未决猜想。本轮MSE可见正文无答案，新回答样式的搜索摘要未能在已打开正文中定位，故不采纳为突破。

**旧卡应变更处：** 补OEIS A369858并删除无序列备注；n个间隙需n+1个素数；不把随机置换均值公式当实际排序渐近。

**按子问的判断：**

- f(n)~n/log n或~π(n)：**暂未找到可验证结果**。
- 精确序列出处：**未作判断**。新增OEIS A369858是出处补全，不是证明。

**直接证据与定位：**

- [A369858](https://oeis.org/A369858/internal)：%N、%C、%H、PARI/Python程序；2024-04-24创建。证据：作者维护序列数据库；访问：已打开正文与代码；未运行。
- [Sorting of prime gaps](https://math.stackexchange.com/questions/893875/sorting-of-prime-gaps)：原题数据；f(n)≈(1/n)Σc_k(n)²；答案区为空。证据：原始题文；访问：已打开正文，22条评论折叠。

**实际检索路径：** `ordering prime gaps fixed points sorted gaps 893875`；`prime gaps sorting unchanged positions f n asymptotic n log n`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**指定对子正文复核：**

- QX-P-001739（22ea84589ec502ac） ↔ QX-P-002287（77c4f0fd287bc13c）：**相关但不等价**。已读取随包双方正文：1739统计排序后位置和值不变的数量及n/log n渐近；2287量词是所有充分大n的单个间隙上界C(log p_n)^2。统计量、量词、目标均不同，不能合并。

**待复核：** 新搜索摘要与正文不一致，可能缓存/删除内容，不能写有新解；隐藏评论未取得。

#### QX-P-001740（版本 92021a27af9b7614）

原MSE与MO问ZF中c与c^c之间的End(R,+)基数；对c=|R|，ZF中已有c^c=2^c，旧卡该上界写法有效。需修正的是将自同态称为自同构；两端已知情形不解决中间基数的一致性。

**旧卡应变更处：** 保留原标题上界2^c（与c^c在ZF中相等）；纠正通俗句中自同态/自同构混用并分别记录；ZF为模型背景而非只选连续映射。

**按子问的判断：**

- ZF中c<|End(R,+)|<c^c=2^c的一致性：**暂未找到可验证结果**。
- 将End(R,+)自同态称作自同构：**题面有误**；应与另问Aut(R,+)的基数问题分别记录。

ZF中的上界等式可直接核对：c=2^aleph0，显式编码给aleph0×c=c，故c^c=(2^aleph0)^c=2^(aleph0×c)=2^c。这是本会话基数计算，不依赖选择公理，不构成新的中间基数一致性结果。

**直接证据与定位：**

- [Cardinality of endomorphisms of reals](https://math.stackexchange.com/questions/3367572/can-the-set-of-endomorphisms-of-mathbbr-have-cardinality-strictly-betwe)：Question(s)、Edit与Karagila评论。证据：原始提问；访问：已打开正文。
- [MO crosspost](https://mathoverflow.net/questions/342703/can-the-set-of-endomorphisms-of-mathbb-r-have-cardinality-strictly-betwee)：主问题及另问isomorphisms上界c!。证据：原作者交叉帖；访问：已打开正文。

**实际检索路径：** `cardinality endomorphisms real additive group ZF continuum intermediate`；`End R plus cardinality c c^c 342703 choice Solovay`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 中间基数模型或排除定理未取得；未展开所有隐藏评论。

#### QX-P-001741（版本 7e1824e81e1b7be0）

最优函数c(λ)加强问与原TSTST存在c<1不同。原帖实读保留λ=.01时约.9887至.9898的构造/上界，未取得最优函数。已发现原竞赛题进入AI-MO/Numina数据集，不能据此说加强问被AI解决。

**旧卡应变更处：** 把c写成依赖固定λ的最优保证；原竞赛存在性证明与最优常数问题分栏；删去未经系统检索支持的绝对“无MO交叉帖/无AI参与”。

**按子问的判断：**

- 所有单位面积平面可测集、固定λ的最优重叠保证c(λ)：**暂未找到可验证结果**。
- λ=.01的非最优上下界：**部分进展**。原帖Progress：上界约.9898，单位面积圆盘下界约.9887；本轮核题与公式范围，未独立数值优化。
- 原赛题及其可测集版本存在c<1：**原题已证**。Evan Chen解答§3.3明确归BrianLawrence，不是最优c(λ)定理。

**直接证据与定位：**

- [Minimum area contained between measurable set and translate by lambda](https://math.stackexchange.com/questions/2844749/minimum-area-contained-between-measurable-set-and-translate-by-lambda-a-stre)：Question；Progress，尤其λ=.01上下界。证据：原始问题与提问者推导；访问：已打开正文。
- [AI-MO olympiads TSTST2018 solutions](https://huggingface.co/datasets/AI-MO/olympiads/blob/fc1dcb54ac0daa4aaff38dff92e2bfa538588166/USA_TSTST/md/en-sols-TSTST-2018.md)：固定数据提交fc1dcb54ac0daa4aaff38dff92e2bfa538588166；§3.3题9。证据：公开AI数据集；原赛题的再收录；访问：仅搜索摘要。
- [Evan Chen problems and solutions](https://web.evanchen.cc/problems.html)：TSTST2018 sols链接；该网页说明属于个人解答笔记。证据：解答作者官网；访问：已打开索引。
- [Evan Chen USA TSTST2018 solutions](https://web.evanchen.cc/exams/sols-TSTST-2018.pdf)：§3.3 pp.23–24，归Brian Lawrence；证明已适用于可测集，λ=.01存在非最优常数。证据：解答作者原稿；访问：已打开PDF并读此题证明。

**实际检索路径：** `"minimum area" "translate" "lambda" Schildkraut measurable overlap`；`measurable plane unit area fixed distance translation overlap optimal constant TSTST 2018`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** AI-MO数据集仅索引摘要可见；尚未遍历所有AI站点。

#### QX-P-001743（版本 9a9dfb0a7a76ea1d）

原问是ZF下任意PID、任意秩自由模的子模自由是否推出AC；原评论只否定把任意向量空间嵌入自由空间的朴素路线。旧备注“严格弱于每个向量空间有基”未有分离模型支持，应撤回严格性。Alphabeta AI页显式假设AC，只证正向。

**旧卡应变更处：** 保留任意秩、任意PID的阅读，不任意缩成有限秩或固定域。删除“严格弱于”的既定断言；把AI正向定理记为命中不适用。

**按子问的判断：**

- ZF+PID自由模子模自由⇒AC：**暂未找到可验证结果**。
- 旧卡逻辑严格弱于AC的断言：**题面有误**。该严格性断言比目前证据强；没有取得成立子模公理而失败AC的ZF模型。

**直接证据与定位：**

- [PID submodule property implies choice?](https://math.stackexchange.com/questions/4966748/does-every-submodule-of-a-free-module-under-a-pid-is-free-imply-the-axiom-of-c)：提问正文；Brandenburg评论随后将equivalent改成单向implies。证据：原始社区问题；访问：已打开正文。
- [A submodule of an arbitrary-rank free module over a PID is free](https://alphabetamath.cc/item/thm-submodules-of-free-modules-over-a-pid-are-free)：Statement及Facts明确Assume the Axiom of Choice；2026-09-09 codex标签。证据：公开AI改写；额外假设AC；访问：已打开正文。不是反推AC的证明；verified标签不是本轮形式化核验。

**实际检索路径：** `"submodule" "free" "PID" "axiom of choice"`；`"subspaces of free" "choice" modules ZF basis`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 未取得反向推导或ZF分离模型；Blass相关定理不直接替代本问；未逐站检索EulerSolve/ProofForum。

#### QX-P-001744（版本 8ed08bb771bb1347）

存在某个固定非恒定整数多项式、每一步都为素数的无限factonomial序列仍未取得完整结果。旧卡把2,3,7,43,1807归A000945错误；这是Sylvester A000058，A000945逐步取最小素因子。无限多素数项与每项素数也不是同一量词。

**旧卡应变更处：** 更正A000058/A000945混淆；删除“本问至少同难”这种无归约论证的难度断言。保留标准猜想为可接受附加假设，不视作已取得条件定理。

**按子问的判断：**

- 存在无限factonomial序列（允许标准猜想条件）：**暂未找到可验证结果**。
- 旧备注的OEIS号、无限多素数项与全素递推对照：**题面有误**。p(t)=t+1,x1=2在1807=13×139处失败；这不能推出所有p均失败。

**直接证据与定位：**

- [Multiply everything so far, plug into polynomial](https://math.stackexchange.com/questions/4453070/multiply-everything-so-far-plug-into-polynomial-can-these-always-yield-prim)：定义与EDIT；Question存在性；未展开3条折叠评论。证据：原作者问题；访问：已打开正文。
- [Sylvester sequence A000058](https://oeis.org/A000058)：定义a(n+1)=a(n)^2-a(n)+1，初值2。证据：OEIS原条目；访问：搜索内容可见；直接打开403。
- [Euclid–Mullin A000945](https://oeis.org/A000945)：取1+既有项乘积的最小素因子。证据：OEIS原条目；访问：搜索内容可见；直接打开403。
- [UQ358 mismatched AI answer](https://uq.stanford.edu/question/358)：页面题目是nested radical；Gemini2.5Pro段却提factonomial并标Failed UQ Validation/Needs Human Verification。证据：公开AI文本错配，非证明；访问：已打开正文。

**实际检索路径：** `"factonomial" primes sequence polynomial`；`"prime" "product of previous" polynomial infinite sequence`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**指定对子正文复核：**

- QX-P-001744（8ed08bb771bb1347） ↔ QX-P-002458（8b1f1d251f45f4c4）：**相关但不等价**。双方正文已读；1744问∃整数多项式p及素数初值使∀i递推值为素数，2458对∀n与∀Q线性无关复数组断言标准复指数域超越次数≥n。Schanuel在1744仅为愿接受的假设举例，并无已建立蕴含或等价。

**待复核：** 未核任何一般条件性构造/不可能定理；指数增长启发式不是全称否定证明；新索引候选QX-P-001252 rev37f0b597b971ae1a是Euclid–Mullin缺失素数，未获正文，不并题。

#### QX-P-001746（版本 6d93b4572a5e66f6）

符号变化对象是平方自由计数误差Δ(t)=Σ_{n≤t}μ²(n)−t/ζ(2)，不是正整数序列。原帖问实变量t区间内过零次数N(x)及常数1渐近；2026评论质疑常数1。Meng结果还需ζ零点导数矩条件(1.3)，旧备注只写RH不完整。

**旧卡应变更处：** 重写标题与人话版：平方自由计数误差的实变量过零次数。区别~、渐近阶和常数未知；孟文补上(1.3)条件。

**按子问的判断：**

- N(x)~x^(3/4)（常数恰1）：**暂未找到可验证结果**。
- 原卡将平方自由正数本身描述为正负翻转：**题面有误**。
- Meng误差分布/对数均方结果：**部分进展**。仅相关，不推出过零次数；除RH还要求J_{-1}(T)≪ε T^(1+ε)（所有ε>0）。

**直接证据与定位：**

- [Squarefree error sign changes](https://mathoverflow.net/questions/505893/prove-that-the-number-of-sign-changes-sim-x3-4-square-free-integers)：正文定义；2026-05-01评论：朴素局部高斯模型另一常数16/π^(3/2)。证据：原始提问与启发式讨论；访问：已打开正文。
- [Original MSE crosspost](https://math.stackexchange.com/questions/5112713/prove-that-the-number-of-sign-changes-sim-x3-4-square-free-integers)：2025-12-06原帖启发式；M(x)~x^(1/2+ε)只是原帖错误写法，不能当RH定理。证据：原作者启发式，非证明；访问：已打开正文。
- [Meng, The distribution of k-free numbers and the derivative of the Riemann zeta-function](https://arxiv.org/pdf/1408.0429)：v2 2016-05-30；pp.2–3 equation(1.3),Theorems1–3；k=2对应Δ。证据：作者预印本；已核条件和结论；访问：已打开PDF并读相关页。

**实际检索路径：** `"sign changes" "squarefree" "3/4"`；`"squarefree" "505893" OR "sign changes" error term`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 须明确跳跃过零/连续段过零以及整数采样是否同计数；未获严格N(x)渐近；不能将μ随机独立模型当证明。

#### QX-P-001747（版本 a2ee3de54c9bdffe）

原帖是0≤i,j≤n的乘法表多项式，常数项2n+1，非从1开始后除x；还提出k≥2个指标的广义版本。n≤232只有2021评论计算报告，未取得代码/重跑/全体n理论证明。

**旧卡应变更处：** 将两个求和下界均恢复0，去掉“显然有x因子”；增加广义k子问；不把Erdos978、Stäckel乘积加1族合并。

**按子问的判断：**

- f_n=Σ_{0≤i,j≤n}x^(ij)在Q[x]总不可约：**暂未找到可验证结果**。
- k≥2的Σ_{0≤i1,...,ik≤n}x^(i1...ik)不可约：**暂未找到可验证结果**。
- 卡片从1计数、去除x因子的版本：**题面有误**。
- 有限计算范围：**部分进展**。作者n≤20，评论k=2检至n≤232；作者k=3检至n≤8；均报告级，未重跑。

**直接证据与定位：**

- [Are Erdős polynomials irreducible?](https://mathoverflow.net/questions/405593/are-erd%C5%91s-polynomials-irreducible)：Questions1–2；2021-10-07PeterTaylor评论n≤232。证据：原题及计算声明；访问：已打开全文。
- [Erdos978 Lean search hit](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/978.lean)：假设一个给定f不可约，问其值的幂自由性；不是乘法表族不可约。证据：作者仓库搜索内容；不适用；访问：仅搜索摘要/代码片段。未取得本题的形式化定理或固定提交，未执行代码。

**实际检索路径：** `"multiplication table polynomial" irreducibility`；`"405593" polynomial Erdős sum`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 原帖n参数应注明n≥1，n=0为常数1需边界排除；计算代码与可复现固定提交未取得；原题无普遍不可约证明。

#### QX-P-001749（版本 469cde02f5f0c946）

应固定不同素数p,q，研究两个非平凡pq-adic幂等元的无限数码串：是否含每个有限词，及更强的是否正规。原帖只有有限实验，OEIS A018247/A018248与公开Python计算可定位；均不证明这些无限量词。

**旧卡应变更处：** 增加固定pq、非平凡幂等元、所有有限词/正规性两个量词层；引用计算代码只作前缀生成资料。

**按子问的判断：**

- 每个非平凡幂等元展开包含全部有限b=pq数码词：**暂未找到可验证结果**。
- 每个长度k词频趋b^(-k)的正规性：**暂未找到可验证结果**。
- 卡片仅写p,q变化时有限自守数的统计：**题面有误**。

**直接证据与定位：**

- [Distribution of digits of pq-adic idempotents](https://mathoverflow.net/questions/156301/distribution-of-digits-of-pq-adic-idempotents-aka-automorphic-numbers)：正文CRT定义及两个问题；2014-02-03评论：基数10,6,14,15各前500万位、词长1–6卡方实验。证据：原题及作者实验声明；访问：已打开正文与评论。实验未重跑，不给无限正规性认证。
- [10-adic idempotent ending625](https://oeis.org/A018247/internal)：定义与2025-12-06条目修订；PARI/Mathematica算法。证据：OEIS定义与计算资料；访问：已打开正文。
- [10-adic idempotent ending376](https://oeis.org/A018248/internal)：定义，a+b=1，base10构造公式。证据：OEIS定义与计算资料；访问：已打开正文。
- [Computing automorphic numbers Python](https://github.com/angelosalatino/computing-automorphic-numbers/blob/master/ultimate-partial-square.py)：ultimate_partial_square()，digits=[5],limit=20；依赖标准库json/time。证据：公开计算代码，非分布定理；访问：已读代码未运行；历史入口DisabledError，未能固定提交。

**实际检索路径：** `"pq-adic" "digits" automorphic`；`"automorphic numbers" "normal" "digit distribution"`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**待复核：** 未取得可核的正规性/含全词证明；GitHub提交历史访问失败，提交号待锁定；未逐站搜索EulerSolve/ProofForum。

#### QX-P-001750（版本 c80f7ca520864c59）

原题是Grahl/forest-fire序列A229037中1出现无穷次，序列图像等距下标不得形成数值AP，不是递增Stanley集合S(0)。弱递增AP变体A309890已与原序列区分，不能转移其1的指标公式。指定Stanley树题也不是同题。

**旧卡应变更处：** 更名为forest-fire序列中1是否无穷次出现；恢复递推a_m=min positive not equal2a_(m-k)-a_(m-2k)。移除A005836一般Stanley结构叙述。

**按子问的判断：**

- A229037中∀N∃n>N使a(n)=1：**暂未找到可验证结果**。
- 固定9项块1,1,2,1,1,2,2,4,4是否出现无穷次：**暂未找到可验证结果**。
- 原卡的一般Stanley序列结构问：**题面有误**。
- 只排除弱递增AP的变体：**部分进展**。RichardStanley评论自纠：变体1的指标是A003278，原A236246在21项有92而非91；仅变体信息。

**直接证据与定位：**

- [On the first sequence without triple in arithmetic progression](https://mathoverflow.net/questions/338415/on-the-first-sequence-without-triple-in-arithmetic-progression)：主问及附加块问；2019-08-19Stanley纠错；内嵌Sage代码有Li<=Lj即变体。证据：原题与作者代码/评论；访问：已打开正文与可见评论；3条折叠评论未读。
- [Forest fire sequence](https://oeis.org/A229037/internal)：定义a(j),a(j+k),a(j+2k)不成AP；条目修订2026-04-03。证据：OEIS主定义；访问：初次正文可取，随后定点打开403。
- [Indices of ones in A229037](https://oeis.org/A236246/internal)：Greathouse2014问题；n=91区别；Python精确递推与434项表链接。证据：OEIS数据与程序，非无穷性定理；访问：已打开正文，代码未运行。
- [OEIS computation repository](https://github.com/MartinMSPedersen/OEIS)：A229037目录。证据：公开代码索引；访问：根目录可读；A229037目录restricted URL、commit history DisabledError，文件与提交未取得。
- [TheoremDB R1315](https://www.theoremdb.org/records/grahl-sequence-infinitely-many-ones-status-20260801/)：UNKNOWN dated2026-07-27；source-only，無可重播证明。证据：社区状态审查记录；不继承其核验；访问：已打开正文。

**实际检索路径：** `"A229037" "Greathouse"`；`"lexicographically earliest" "3-free" "1"`；再按题逐查 GitHub、公开 AI/社区域组合、原帖/关键原稿与全库索引。详细实际词组及访问失败保留在 JSONL，未执行入口不计完成。

**指定对子正文复核：**

- QX-P-001750（c80f7ca520864c59） ↔ QX-P-000283（dea50a4977553bc3）：**相关但不等价**。双方正文已读：1750应问一个确定正整数值序列中∀N∃n>N,a_n=1；000283问∀非同构树T1,T2，染色对称函数X_T1≠X_T2。Stanley人名为关键词碰撞，数学对象/量词/结论完全不同；无等价证据，不合并。

**待复核：** 无原序列全称无穷性证明；未执行MO/OEIS代码；公开仓库文件及固定提交访问受限；社区状态记录不是证明。

## 五、查重关系总表

下表逐对列出55组指定关系及新增候选；完整双方版本、正文比较和访问边界在JSONL的duplicates字段。此表不是合并指令。

| 来源 | 题号A | 题号B | 判断 |
|---|---|---|---|
| 指定 | QX-P-000002 | QX-P-001702 | 特例/强化 |
| 新增 | QX-P-000004 | QX-P-001710 | 待定 |
| 指定 | QX-P-000040 | QX-P-001715 | 特例/强化 |
| 指定 | QX-P-000088 | QX-P-001675 | 同题 |
| 新增 | QX-P-000109 | QX-P-001678 | 待定 |
| 指定 | QX-P-000117 | QX-P-001685 | 相关但不等价 |
| 新增 | QX-P-000117 | QX-P-001686 | 同题 |
| 新增 | QX-P-000137 | QX-P-001689 | 待定 |
| 指定 | QX-P-000171 | QX-P-001650 | 特例/强化 |
| 新增 | QX-P-000268 | QX-P-001687 | 待定 |
| 指定 | QX-P-000283 | QX-P-001750 | 相关但不等价 |
| 指定 | QX-P-000357 | QX-P-001690 | 同题 |
| 新增 | QX-P-000361 | QX-P-001682 | 待定 |
| 指定 | QX-P-000384 | QX-P-001706 | 特例/强化 |
| 新增 | QX-P-000480 | QX-P-001680 | 待定 |
| 新增 | QX-P-000489 | QX-P-001674 | 待定 |
| 新增 | QX-P-000494 | QX-P-001649 | 待定 |
| 指定 | QX-P-000495 | QX-P-001657 | 特例/强化 |
| 新增 | QX-P-000495 | QX-P-001670 | 待定 |
| 新增 | QX-P-000581 | QX-P-001685 | 同题 |
| 指定 | QX-P-000581 | QX-P-001686 | 相关但不等价 |
| 指定 | QX-P-000598 | QX-P-001654 | 相关但不等价 |
| 指定 | QX-P-000608 | QX-P-001689 | 特例/强化 |
| 指定 | QX-P-000760 | QX-P-001652 | 相关但不等价 |
| 指定 | QX-P-000836 | QX-P-001718 | 相关但不等价 |
| 指定 | QX-P-000863 | QX-P-001704 | 相关但不等价 |
| 指定 | QX-P-000863 | QX-P-001707 | 相关但不等价 |
| 指定 | QX-P-001198 | QX-P-001696 | 相关但不等价 |
| 指定 | QX-P-001238 | QX-P-001716 | 相关但不等价 |
| 指定 | QX-P-001386 | QX-P-001704 | 相关但不等价 |
| 指定 | QX-P-001390 | QX-P-001704 | 相关但不等价 |
| 指定 | QX-P-001635 | QX-P-002490 | 相关但不等价 |
| 指定 | QX-P-001636 | QX-P-002261 | 相关但不等价 |
| 指定 | QX-P-001637 | QX-P-002463 | 相关但不等价 |
| 指定 | QX-P-001638 | QX-P-002120 | 相关但不等价 |
| 指定 | QX-P-001639 | QX-P-001674 | 相关但不等价 |
| 指定 | QX-P-001645 | QX-P-002438 | 相关但不等价 |
| 新增 | QX-P-001645 | QX-P-002485 | 同源不同问 |
| 指定 | QX-P-001646 | QX-P-002485 | 相关但不等价 |
| 新增 | QX-P-001648 | QX-P-002286 | 待定 |
| 指定 | QX-P-001657 | QX-P-002256 | 相关但不等价 |
| 指定 | QX-P-001664 | QX-P-002287 | 相关但不等价 |
| 指定 | QX-P-001669 | QX-P-001837 | 相关但不等价 |
| 指定 | QX-P-001669 | QX-P-002408 | 相关但不等价 |
| 指定 | QX-P-001681 | QX-P-001697 | 相关但不等价 |
| 指定 | QX-P-001683 | QX-P-001684 | 相关但不等价 |
| 指定 | QX-P-001683 | QX-P-001688 | 相关但不等价 |
| 指定 | QX-P-001683 | QX-P-002353 | 相关但不等价 |
| 指定 | QX-P-001685 | QX-P-001686 | 相关但不等价 |
| 指定 | QX-P-001689 | QX-P-002357 | 特例/强化 |
| 指定 | QX-P-001689 | QX-P-002494 | 特例/强化 |
| 指定 | QX-P-001691 | QX-P-001699 | 相关但不等价 |
| 指定 | QX-P-001693 | QX-P-002256 | 相关但不等价 |
| 指定 | QX-P-001702 | QX-P-002321 | 特例/强化 |
| 指定 | QX-P-001704 | QX-P-001707 | 相关但不等价 |
| 指定 | QX-P-001704 | QX-P-001776 | 相关但不等价 |
| 指定 | QX-P-001704 | QX-P-001832 | 相关但不等价 |
| 指定 | QX-P-001704 | QX-P-002070 | 相关但不等价 |
| 指定 | QX-P-001704 | QX-P-002242 | 相关但不等价 |
| 指定 | QX-P-001704 | QX-P-002299 | 相关但不等价 |
| 指定 | QX-P-001704 | QX-P-002320 | 相关但不等价 |
| 新增 | QX-P-001705 | QX-P-001706 | 同题 |
| 指定 | QX-P-001705 | QX-P-001707 | 相关但不等价 |
| 指定 | QX-P-001707 | QX-P-002267 | 相关但不等价 |
| 指定 | QX-P-001707 | QX-P-002299 | 相关但不等价 |
| 指定 | QX-P-001707 | QX-P-002320 | 相关但不等价 |
| 指定 | QX-P-001716 | QX-P-001806 | 特例/强化 |
| 指定 | QX-P-001739 | QX-P-002287 | 相关但不等价 |
| 指定 | QX-P-001744 | QX-P-002458 | 相关但不等价 |

## 六、1693的可复现有限证书

数据来源为[jzone3/solving-math-problems固定提交](https://github.com/jzone3/solving-math-problems/blob/4daf2214773f71daefc2c81770a64a3190b87ebd/solutions/P02/verify.py)。本轮只取边集和证书作为数据，另写标准库脚本枚举核对；没有执行原仓库程序。ZIP内提供 `复核证书/verify_brandt9.py` 和 `复核证书/brandt9_check.json`，JSONL的1693行也内嵌完整数据。

顶点为0到8，14条边为：

`(0,4), (0,5), (0,8), (1,4), (1,7), (1,8), (2,5), (2,6), (2,8), (3,6), (3,7), (3,8), (4,6), (5,7)`

度数为 `(3,3,3,3,3,3,3,3,4)`，故δ=3=n/3。对全部84个顶点三元组检查无三角形；对全部36对顶点检查，每条缺边的端点有公共邻点，所以图是极大无三角形图。令A为邻接矩阵，并取

\[
y=(2,-1,-1,2,-1,-1,-1,-1,2)^\mathsf T,
\qquad Ay=(0,0,0,0,0,0,0,0,2)^\mathsf T,
\qquad \sum_i y_i=0.
\]

若对各顶点作正整数倍增x，使所得图d正则，则Ax=d·1。因此

\[
0=d\sum_i y_i=y^\mathsf T Ax=(Ay)^\mathsf T x=2x_8>0,
\]

矛盾。这是针对West所写 **δ≥n/3** 版本的有限反例；不否定严格 **δ>n/3** 的已知结论，也不是Lean编译验证。脚本仅需Python标准库，运行 `python verify_brandt9.py` 可再核边集、矩阵乘法及上述有限条件。

## 七、交付校验

- 100行可解析UTF-8 JSONL，无重复题号；顺序、题号、card_rev、batch_id与输入逐项相同。
- 所有题均保留实际查询与证据/访问边界；全部55个指定pair_id已覆盖，双方版本与包内索引一致。
- 数学状态按子问记录；形式化状态与数学状态分离，独立Lean运行次数为0。
- 没有修改群星线上库。候选修订、潜在同题与深查任务均以建议回传。
- 未将完整网页检索响应打包；避免把索引文字和第三方全文误作本轮原创研究报告。
