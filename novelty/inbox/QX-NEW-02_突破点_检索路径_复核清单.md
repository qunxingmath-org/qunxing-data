# QX-NEW-02：突破点、检索路径与复核清单

核查截止：**2026-11-26**。本轮按包内《00_先读我》《查新规则与回传格式》做逐题初查；100题均保留原`id / card_rev / batch_id`，没有修改线上题卡、合并题目或发帖。

## 一、覆盖与结论的读法

已完成100题原题对应、每题至少两组不同学术检索词、GitHub/代码及公开AI/社区检索、2469条库内简索引匹配。**38个指定对子**均核双方现版正文；另5个新候选仅有索引，因此待定。两条反向复述已移到审计，主回传只保留指定owner的38条。

结构与覆盖校验通过。共**174项子问/范围判断**、**762条逐题检索或读取记录**。下表统计的是子记录，不是互斥的题卡状态；同一题可以同时有题面订正、部分进展及待核声明。

| 子记录状态 | 数量 |
|---|---:|
| 原题已证 | 2 |
| 完整证明/反例声明待核 | 15 |
| 部分进展 | 47 |
| 题面有误 | 28 |
| 暂未找到可验证结果 | 82 |

“暂未找到可验证结果”只限本次列出的入口和查询，不证明学术界仍开放。“题面有误”包括量词、定义、数值及出处不支撑等不同情况，须看具体说明；例如ES(7)的37上界未核到来源，不等于证明37不可能。

**验证层级：** 没有执行外部论文程序、GAP/Magma/SAT证书或Lean/Coq重跑。取得代码、检查顶层命题、他人报告验证、本轮独立验证分开登记。本轮直接检查了27/7的定理适用代入；另以自编短算术核对Erdős–Moser的平凡解、ES(7)界的113计算、Recamán样例、3003的8个二项式表示及(1,1)subprime周期18。这些有限核对不能作为原猜想的全证明。

## 二、优先改状态或人工复核的项目

| 题号 | 建议 | 依据与限制 |
|---|---|---|
| **001555 / 20.59** | 原题已证，证据强度为预印本 | [Minasyan2603.17596v2](https://arxiv.org/html/2603.17596v2) Theorem1.1完整覆盖；本轮核定理对应，没有独立审完证明，也不记成已刊。 |
| **001618 / 17.25(b)** | 子问已证 | [Kim–Koberda1901.06375v4](https://arxiv.org/abs/1901.06375v4) Theorem1.4(1)，2022已刊；取27/7∈X。(a)全有理数问不关闭。 |
| **001534 / 19.77** | 完整声明待核 | [Kapovich2608.17238](https://arxiv.org/abs/2608.17238) TheoremA、Corollary1.2覆盖原模型；AI协助披露及未独立全证复核须保留。 |
| **001556 / 20.79** | 完整声明待核；先修codegree | [Yang2609.04702镜像](https://borowiecki.dev/pdf/2609.04702) Theorem1.1；官方入口受限；定义须有Kerχ。 |
| **001568 / 20.126(a)(b)** | 同一构造的两个子问待核 | [Gong2611.14972镜像](https://borowiecki.dev/pdf/2611.14972) Theorem1：加法Z²、乘法F∞；镜像/核心构造待复核。 |
| **001581 / 21.55** | 完整否定声明待核 | [ProofForum PF2026.000033](https://www.proofforum.org/abs/PF%3A2026.000033) v1；AI passed不等于人审或形式化。 |
| **001585 / 21.69** | 完整范围的条件算法声明待核 | [2610.25305](https://arxiv.org/abs/2610.25305) Theorem3.8依赖(H)；不得写成无条件已解。 |
| **001598 / 21.123** | 原配方缺陷与修改配方解分别待核 | [Fraga202608.2109](https://www.preprints.org/manuscript/202608.2109)改动实际公式，不能把修正版当原版证明。 |
| **001602 / 21.131** | 直接肯定声明待核 | [Kriebel作者稿](https://aleckriebel.com/research/locally-finite-p-groups-golod-at-section/paper.pdf) Corollary2；仅Golod子群的商，不是整个Golod群为AT。 |
| **001604 / 21.133** | 正对原题的完整反例声明待核 | [2610.05415](https://arxiv.org/abs/2610.05415) Main Theorem；广义次正规交换列定义已对应，旧卡“只是邻近定义”应撤销。 |
| **001633 / Hadwiger–Nelson** | 补≥6声明及精确验证层级 | [OpenAI固定提交论文](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/paper.pdf) Theorem1.1与Five.lean顶层对应任意5染色；未重跑。若成立仍只缩到6或7。 |

### 已发现直接障碍的“完整声明”，须另看

- **001616：** Aydın2016声称反驳17.13，但构造不传递；Asar的totally imprimitive定义预设传递，故当前声明不适用原题。相关Arikan2026论文和勘误另已被出版社撤回。
- **001626：** Singmaster仓库自称Lean完整解决，但固定提交只有定义，无证明链，末命题改成统一坐标界且可直接否定。不能接受为原猜想的形式化证明。
- **001632：** Gnang全证明声明有针对当前v3的Step5缺口报告；另一相关稿已撤回。缺口报告不等于树猜想或Composition Lemma本身被反驳。

因此15条“完整证明/反例声明待核”记录不等于15份可接纳的解答；其中包含已经识别的不适用或不等价声明，具体排除理由已写入证据。

### 明确的订正与部分进展

优先修正：类换位须交换不相交同余类；001544漏阿贝尔直因子；001545将A₅×A₅误扩成任意幂；001547把105读成10⁵；001557的维数子群定义和n≤4背景错误；001571开子群包含方向倒置；001597将profinite误作抽象剩余有限；001623平凡解及素因子计数对象错误；001625引用错指物理arXiv；001629递推下标和素数分支错误；001630“k个相对速度/总k+1跑者”差一。001542的p=2指数冲突涉及原稿本身，应请原作者澄清，不能自行修成奇素数。

部分进展中，001553的EulerSolve证书只覆盖列出的2进赋值范围；001623新增2026-11-21必要下界；001627的SAT仅锚定子类；001630为固定人数的全速度计算辅助声明；001631的4/3上界仍弱于原m≤n。均不得升级为相应一般原题已解。

## 三、查重结论

38个指定对子关系均逐对记在JSONL。最需要避免整卡合并的是**001562与000678仅16.5(a)同题**：p群的局部有限与局部幂零等价，但000678的(b)是另一个问题。001612是000547/17.6(a)的n=3特例；001632的graceful结论比000260的一般Ringel分解存在性更强。001607/001609与001944的关系因1944原源删除、题面猜测而待定。

新增索引候选如下，未取对方现版正文，不认定等价：

| 本题 | 对方 | 对方card_rev |
|---|---|---|
| QX-P-001548 | QX-P-002368 | `04879638b27f7448` |
| QX-P-001551 | QX-P-002372 | `bebcaffd0e6ec3bd` |
| QX-P-001552 | QX-P-002373 | `462eac8ffa9d3475` |
| QX-P-001557 | QX-P-002381 | `b5cf1fe2df813dfb` |
| QX-P-001560 | QX-P-002364 | `33e027da4ba86da1` |

## 四、审计与后续复核顺序

先核上表能改状态的原定理及适用范围，再处理有明确反例/形式化缺口的声明，然后核依赖完整性与计算证书。未经这一复核，不把多篇互相引用、AI平台评分或仓库标签当成独立确认。

压缩包的audit目录保留真实请求、检索返回的题名/URL、逐题检索记录、输入键值、38对配对键值和已取得原稿的哈希。没有再分发第三方论文全文或整段搜索摘要。公共搜索采用合并查询时，返回往往不提供单词条归属；审计按真实批次保存，逐题适用性由evidence说明。原始请求中root:R001的精确词未保全，因此不计入覆盖依据；100题的登记学术/代码/社区搜索词均可在其后实际请求中逐字找到。

下文按题号组展开重要变化；没有逐题复述零命中。

---

## QX-NEW-02 A 片：重要变化与复核清单

检查日期：2026-11-26。范围为QX-P-001528至QX-P-001554中分配的25题；结果与原有 `id / card_rev / batch_id` 一一对应。这里只列影响状态、题面、出处或查重的发现，不逐题复述无命中。

原出处已核为 [Kourovka Notebook arXiv:1401.0300](https://arxiv.org/abs/1401.0300) **v50，2026-11-02**。用原PDF逐题定位；105、Alt₅²、pᵏ、阿贝尔直因子等排版疑点另外核了页图。没有把原题目录无星号、普通搜索无命中或代码目录出现词语等同数学状态结论。

### P0：001534 / 19.77，稳定小消去猜想有完整证明声明

**旧卡 → 变化：** 原先没有具体进展证据；新增 Ilya Kapovich 的预印本 *Small Cancellation Stability and Isomorphism Rigidity for Generic Finitely Presented Groups*，[arXiv:2608.17238](https://arxiv.org/abs/2608.17238)，本轮所见提交史为 v1，2026-08-18。

**原文定位与范围：** [PDF](https://arxiv.org/pdf/2608.17238) Theorem A（pp.3–4）对固定秩 m≥2、元组长 q≥1、任意固定 0<λ<1，声称指数泛型的元组对**每个**自由群自同构都保持循环约化并对称化后的 C′(λ)。Corollary 1.2（p.4）补足自由约化字的球面/球模型；取 λ=1/6 对应原题。不是仅有限多个自同构的实验。

**验证层级：** §12（p.41）披露研究过程大量使用 ChatGPT，作者声明自行检查证明并承担责任。本轮读取了定理、模型推广及披露，未独立审查整个证明、未取得或运行对应形式化代码。回传为 **完整证明/反例声明待核**，不写“本会话已证”。

**实际路径：** 两组 Schupp/Kapovich 名称与 C′(1/6) 特征检索 → system1 精确题名/编号及近180天修订检索 → arXiv 官方PDF、abs提交史。web open 曾 DisabledError，随后只读下载公开官方文件成功；已把失败与成功分开记入审计。优先复核主定理及其外部几何群论依赖。

### P0：001544 / 20.28，漏掉阿贝尔直因子；001545 / 20.29，已知范围误扩大

**001544旧卡 → 变化：** 中文摘要写“无限中心有限群”且结论为 G≅H(L)。原文是任意有限群G，结论 **G≅H(L)×A，A为阿贝尔群**。人话版已经提到这个差异，但标题、题面及形式化尚未修复。仅取非平凡阿贝尔直因子即可说明不能把原结论加强成直接同构 H(L)。

**001545旧卡 → 变化：** “中心化”应改为“中心平凡”；“S=A₅已证”不可理解为所有 n 已证。Gorshkov原稿的Theorem 2仅处理 **A₅×A₅**。Notebook的相关印字为Alt₅平方，应据原论文解释，不扩展为全部直接幂。

**直接证据：** Gorshkov，[arXiv:1912.07206v1](https://arxiv.org/pdf/1912.07206)，Question 1、Theorem 1（p.1）及Question 2、Theorem 2（p.2）。Theorem 1给 L=A₅、H(L)=SL₂(5) 的阿贝尔直因子结论；Theorem 2给 n=2 的无中心识别。Notebook所列已刊版本为 J. Algebra Appl.21(11)(2022),2250226。

**实际路径：** universal perfect central extension / Schur cover / class sizes，以及direct powers / centreless / Alt5两组词检索 → 官方arXiv摘要 → PDF主定理对照。一般L、一般(S,n)未取得完整解；没有对已刊全文做逐步证明复审。

**指定查重：** 001544 与001545为**同源不同问**。一题是中心扩张加阿贝尔因子，另一题是中心平凡的简单群直接幂；保留两卡。

### P0：001547 / 20.36，105被误读为10⁵

**旧卡 → 变化：** 两处“至少10⁵个关系”应为 **至少105个关系**。原PDF p.163（20.36）已经目视核对。这个误读会让“能否少于1000个”的子问被错误地认为已有否定答案。

**范围：** 三个原子问仍分别登记：少于百万、少于千、精确最少数；本轮未取得它们的完整答案。|B(3,4)|=2⁶⁹与旧证明使用超过2³²个四次幂是另外两个数，不能一起改动。

**实际路径：** Havas–Newman/Burnside B(3,4)/fourth power relations与million/thousand两组检索 → Notebook文本提取 → p.163页图。Havas–Newman1980原论文尚未逐字复核；未运行枚举或检查关系证书。

### P0：001542 / 20.18，p=2与导群指数要求冲突

**旧卡 → 变化：** 除简式量词缺 p为素数、k≥2 外，原稿本身还有参数边界冲突。p.160明确写：群指数pᵏ，生成群的导群指数**也是pᵏ**，且p为任意素数。

当 p=2 且群幂零类≤2时，收集公式给

\[
(xy)^{2^k}=x^{2^k}y^{2^k}[y,x]^{2^{k-1}(2^k-1)}.
\]

若 exp(G) 整除2ᵏ，则每个交换子的阶同时整除2ᵏ与2^(k−1)(2ᵏ−1)，所以整除2^(k−1)。导群交换且由交换子生成，故 exp(G′) 也整除2^(k−1)，不可能恰为2ᵏ。

**回传处理：** 记 **题面有误/待原作者澄清**；没有擅自把题目改成奇素数，也没有把奇p情形宣称已解。需要确认应限制p为奇素数，还是群/导群指数条件另有遗漏。

**相邻文献边界：** [Budkin2023官方摘要](https://www.mathnet.ru/php/archive.phtml?jrnid=smj&option_lang=eng&paperid=7742&wshow=paper)涉及奇p、指数p的拟变元簇，不能直接回答本题k≥2及导群同指数的无限族要求。该篇只读了官方摘要，未读全文。

### P1：001553 / 20.52，EulerSolve给有限范围的构造与证书

**旧卡 → 变化：** 新增2026-10-27、v1.0的[公开原稿专页](https://eulersolve.org/papers/kou-20-52/)，DOI [10.5281/zenodo.23685552](https://doi.org/10.5281/zenodo.23685552)。作者Alper Ferudun，站点明确未审稿及AI辅助。

**原文定位：** [PDF](https://eulersolve.org/papers/kou-20-52/paper.pdf?v=9eb72ad6f25c) Theorem 1.2/1.3（p.2）和§1.3（p.3）；另读了[作者验证报告](https://eulersolve.org/papers/kou-20-52/verification_report.md?v=a6868fc29a6f)。

- v₂(m)≤13有手算构造，所以所有m<16384成立；作者把j≤8归于Buckley–MacHale，新增手算范围为9≤j≤13。
- 15≤v₂(m)≤120且不等于34、64给104份计算证书。
- 一般m问题没有决定；j=14、34、64仍不在上述范围。Proposition1.6对若干族的排除不能当作一般反例。

**验证层级：** 已读原稿和作者验证报告，未运行来源ZIP中的GAP/Python或任何外部代码；登记**部分进展**并保留计算部分的独立核验待办。作者报告不是独立审稿或本会话重跑。

**实际路径：** MacHale/conjugate deficiency两组学术检索 → GitHub/社区联合入口命中EulerSolve → 当前目录逐题号find → 专页、PDF、验证报告。A片其余24题在该目录按题号无匹配；所有25题在ProofForum当前公开索引按题号无匹配。两者都只说明所取索引的匹配结果。

### P1：001548 / 20.37，2026年二子集分解充分条件

**旧卡 → 变化：** 补George M. Bergman，[An observation on factorizations of finite groups](https://arxiv.org/pdf/2608.08928)，v2，2026-09-06，Theorem1.1（p.1）。若某子群链各步指数能分成乘积a与乘积b的两组，则|G|=ab可以实现为G=AB、|A|=a、|B|=b。

**范围：** 只是充分条件。§2说明有不能由此子群链方案实现、却另有分解的例子，所以“该方案失败”不是反例。文章开头明确一般k=2尚无已知反例；k>2的反例与本题不同。“每个指定Lagrange子集都能成为因子”也比本题量词更强，不能混同。

**实际路径：** Hooshmand/two subset factorization与prime-index特征检索 → 2026文献 → 官方PDF及abs版本史 → 作者未刊笔记页搜索复核。官方PDF已读；没有把作者网页搜索摘要写成全文核验。

### P1：001531 / 19.54，严格二极大子群的新充分条件

**旧卡 → 变化：** 补Burness–Meng，[On second maximal subgroups of finite groups](https://arxiv.org/pdf/2609.03911)，v1，2026-09-03。Theorem A（p.1）证明素数指数子群的每个极大子群均为严格二极大，去掉既有结果的p-solvable假设。Theorem B还给一类奇合数指数。

**范围：** p.3明确连接19.54的WSM群主因子问题，并说完整分类尚未完成。不能据这篇主定理把整个chief-factor分类置为已解。已读定义和Theorem A/B，未独立检查CFSG依赖及Magma步骤。

**实际路径：** Monakhov/2-maximal与chief-factor特征两组检索 → 2026预印本 → 官方PDF/提交史；web open失败与直接下载成功分别记录。

### P1：001537 / 19.108，旧卡遗漏已刊亚交换子情形

**变化：** [Wilde2019原文](https://www.numdam.org/item/10.4171/RSMUP/12.pdf)，*Zeros of irreducible characters of metabelian p-groups*，Rend. Sem. Mat. Univ. Padova141(2019)9–18，Theorem1.1：奇p的亚交换p群满足所要求的平方分母整除。

**范围：** 不能改为所有奇p群已证。2026年[arXiv:2605.04513](https://arxiv.org/abs/2605.04513)处理一般Wilde猜想的近单群约化，分母与原题不同。另核了[2611.03541](https://arxiv.org/pdf/2611.03541)主定理，它研究两个特征标零点集合的包含与次数，不是本题元素阶结论。

**实际路径：** Wilde/nonzero character与平方次数两组检索 → Numdam已刊全文 → 2026相邻论文范围核对。亚交换结论记部分进展；没有运行特征标计算。

### 题卡定义、形式化及出处的其他实质修正

#### 001528、001529、001549：CT(Z)定义及错误背景

[Kohl原论文](https://stefan-kohl.github.io/articles/simplegp.pdf) Definition1.1要求**不相交的同余类**；三卡人话误写互素模数。互素模数的同余类由中国剩余定理必相交，不能如此定义换位。

001529另写“CT(Z)元均为周期元素已知”，与同文Theorem1.3(2)“所有有限秩自由群可嵌入”矛盾。应删除。001549的第一分支应为轨道**条数**有限，不能写成每条轨道有限。

001528的[MO原问](https://mathoverflow.net/questions/209373/transitivity-on-mathbbn-0-a-42-problem)在2016-11-10给旧版反例后增加了余类并不变条件。现19.45正是修订版；旧反例不能登记为现题反驳。

#### 001535、001539、001541、001550

- **001535 / 19.95：** soluble应为可解，标题“单群”错误。中心化子包含v本身，原稿“adjacent vertices”是否采用闭邻域需澄清，暂不把开邻域字面读法当作新反例。
- **001539 / 19.111：** 形式化和一句话必须保留“除xᵖ=1及其推论”；不能写“没有任何非平凡恒等式”。
- **001541 / 20.12：** 未知方向是u.-2-p.⇒全部u.-n-p.。Mathlib [固定提交的Basic.lean](https://github.com/leanprover-community/mathlib4/blob/bce3fc3a37ff1790b2e3b0ccf8f941053aefde19/Mathlib/Algebra/Group/UniqueProds/Basic.lean)有UniqueProds/TwoUniqueProds相关内容；TwoUniqueProds是至少两个唯一乘积，不能把名字误认作任意n重乘积的证明。未重跑。
- **001550 / 20.45：** 删除“线性群增长率为指数型已知”。高度计数满足e_b≤(2b+1)^(n²)，与字增长不同。[MO220093](https://mathoverflow.net/questions/220093/number-of-matrices-with-small-entries-in-integer-matrix-groups)的原问/评论已读，未见完整一般答案。

#### 001554 / 20.55：1992摘要“2与4”线索排除

[Mattarei1992学位论文](https://wrap.warwick.ac.uk/id/eprint/109415/1/WRAP_Theses_Mattarei_1992.pdf) Summary（PDF p.8）实际写派生长**2与3**，并推广n与n+1。未写2与4。正式 *On character tables of wreath products* 出处是J.Algebra175(1995)157–178；1992年的 *Character tables and metabelian groups* 则在JLMS。旧卡的“1992完整解与Notebook冲突”不成立，应去除。2/4一般问题本轮未取得可核结果。

### 库内查重：三对指定复核与三对新候选

| 本题 | 对方 | 关系 | 正文与量词说明 |
|---|---|---|---|
| 001528 | 000655（4664d11fd09b51fa） | 同源不同问 | 双方正文已读：通用算法判定 vs 特定42阈值传递性。000655把“每条轨道有限”译成“有限条轨道”的错误仅作为附带问题报告。 |
| 001529 | 000617（062e33b54a929465） | 相关但不等价 | 双方正文已读：无限挠子群 vs 中间词增长子群。 |
| 001544 | 001545（f3392570f10cb855） | 同源不同问 | 双方正文及Gorshkov原论文已读：中心扩张加阿贝尔因子 vs 中心平凡直接幂。 |
| 001548 | 002368 | 待定，同题强候选 | 同Kourovka20.37及二子集分解题名；对方全文未提供。双方rev已写JSONL。 |
| 001551 | 002372 | 待定，同题强候选 | 同20.48；对方题名“自同态”需正文核与自同构是否等价。 |
| 001552 | 002373 | 待定，同题强候选 | 同20.49及同指数二生成命题；对方全文未提供。 |

本轮只报告关系，没有线上合并或改卡。

### 分片核查界限

合并回传文件中，本分片对应25题。实际查询和结果范围见逐题JSONL；audit/web_calls.jsonl仅保存请求、返回题名/URL、访问消息及响应哈希。逐题库内匹配记录见audit/queries_by_topic.jsonl，取得原稿的哈希见audit/retrieved_source_hashes.json。摘要、web open失败、后续全文成功与计算未重跑均分开记录。

本轮没有运行外部论文代码、Lean、Coq、GAP或MAGMA。没有发帖、联系作者、修改线上题卡。对未取得完整结果的子问只写本次证据范围，不以零命中或Notebook无注记宣称学术界仍开放。


---

## QX-NEW-02 · B 分片突破点、检索路径与复核清单

核查日期：2026-11-26。范围：QX-P-001555 至 QX-P-001581 中分配的 25 题。各题版本以 `QX-NEW-02_逐题回传.jsonl` 为准。本轮只读初查，没有线上写入、发帖或运行外部证明/计算程序。

原始问题集已从 arXiv 官方摘要核到 **1401.0300v50，2026-11-02**，并将每题与官方 HTML、本地 PDF 对应。页码是该 PDF 中的书面页码。本报告不以“仍在问题目录”或检索无命中独自证明开放状态。

### 一、最可能改变数学状态的四题

#### QX-P-001555 · 20.59 · 原题已证（预印本强度）

**旧卡 → 变化：** 旧卡把 Minasyan 2021 部分结果与所谓已证摘要混在一起，并主张以 Notebook 仍在列为准。新查到的 **2026 新稿**并非那篇旧论文：[arXiv2603.17596v2](https://arxiv.org/html/2603.17596v2)，**Theorem 1.1**直接覆盖 20.59。

**范围：** 定理给所有 virtually free 群的 LR 性质，因而覆盖原题中有限生成 G、有限生成 H 的量词。本轮核对定理对应，未独立审完证明。另有[作者 MPIM 报告摘要](https://www.mpim-bonn.mpg.de/node/15676/index.html)交叉印证；旧目录未更新不是反证。

**修订：** 建议数学状态记“原题已证”，证据强度另记“预印本”。“虚拟收缩核”宜改“虚拟收缩子群”；r:L→H 在 H 上为恒等，不是在说同态核。

**实际路径：** Minasyan + virtually free + virtual retract + 20.59 → 官方 v2 定理 → 作者机构报告；另查特征句及 GitHub、公开 AI/社区限定域。待跟踪发表、勘误和新版。

#### QX-P-001556 · 20.79 · 完整证明声明待核

**旧卡 → 变化：** [Yong Yang 镜像稿](https://borowiecki.dev/pdf/2609.04702)自署 **arXiv2609.04702v2，19 Sep 2026**，50 页，**p.1 Theorem 1.1、§20**宣称所有非交换有限单群由不可约特征标 codegree 集刻画。

**范围与限制：** 是“集合”相等，不含重数。官方 arXiv abs、html v2、pdf v2 都返回 DisabledError；镜像的完整定理可读，但官方版本来源、最新性和核心证明待核，因此不直接记已证。旧稿若只处理若干 Lie 型族或含重数的 multiset，都不能替代本题。

**先修题面：** 正确定义是 cod(χ)=|G:Kerχ|/χ(1)，旧卡的 |G|/χ(1) 漏 kernel，改变定义。

**实际路径：** “20.79 codegrees” → “codegree isomorphism conjecture 2026” → 作者/特征检索 → 官方三种入口失败 → 镜像 Theorem 1.1 与各族覆盖表。待核 §17、§19、§20。

#### QX-P-001568 · 20.126(a)(b) · 两子问共用的完整声明待核

**旧卡 → 变化：** [Lü Gong 镜像稿](https://borowiecki.dev/pdf/2611.14972)《A regular free action on the integral plane and a problem on left braces》，自署 **arXiv2611.14972v1，11 Nov 2026**；**p.1 Theorem 1**宣称加法群 Z²、乘法群可数无限秩自由群的 brace。

**范围：** 若构造正确，(a) 乘法群不可解和 (b) 含非交换自由群同时得到肯定答案。官方 abs/html 不可达，只核到镜像四页稿及检索元数据。

**实际路径：** “20.126 brace” → 新近 Gong 查询 → 官方失败 → 镜像定理、**Lemma 2、§3–4**。待人工核 ping-pong 区域、有限球避让、归纳合并轨道以及 regular/free 的完整性；没有独立运行或形式化通过声明。

#### QX-P-001581 · 21.55 · 完整否定声明待核

**旧卡 → 变化：** [ProofForum PF:2026.000033](https://www.proofforum.org/abs/PF%3A2026.000033)，**v1，2026-11-10**；[八页 PDF](https://www.proofforum.org/server-file.php?disposition=attachment&id=PF%3A2026.000033&type=pdf&version=1) **Theorem 1.1、Corollary 7.1**宣称否定原来的归一化极限 1。

**范围：** p=2,3 时声称极限 log₃2；非 Fermat p≥5 时声称 1/log₂p；Fermat p≥5 时仅给 limsup≤2/log₂p<1。最后一类足以否定“极限为 1”，但没有证明极限存在。

**审查强度：** 页面只有 Full-paper AI passed，**Whole paper: Not reviewed**，**No Palomar formalization linked**。不能当人审或 Lean 验证，更不能写本轮独立通过。搜索摘要曾把 ceil 错显示为 floor，原 PDF/定理索引中上界为 2ceil(logₚn)+1，应以原稿为准。

**实际路径：** p-length + 21.55 新近检索 → PF v1/PDF/定理索引 → 审查和形式化区块。待审 §4 的 3-soluble 归约、§5 高度界及 §6 下界构造。

### 二、新找到的部分进展与代码范围

#### QX-P-001557 · 20.84 · 小阶计算、形式化基础，不是全解

[作者预印本](https://ispacex.github.io/d5/paper/d5.pdf)（Stanislav Vorobev，60 页）摘要与 **§5 Props 5.3、5.10 / Theorem 5.4**列小阶排除和归约，宣称有限 class 3 的 2 群反例阶至少 2¹²。应作为作者计算进展待复核，不能推广到任意群。

[ispacex/group-dimension](https://github.com/ispacex/group-dimension) 的 README **Only stated**明确 `DimensionQuestion5`只是 `def … : Prop`；Lie 环类比已有结果不等于群问题解。可读 `Solution.lean`和主分支说明，但固定提交 `d4a8ddb` 的页面/API均未取到。README自报 **PALOMAR-2026-10-23-000007 v4**、Lean/Mathlib 4.35.0、Mathlib rev `56a0058`；`GroupDimension/Reduction.lean`的`dimensionQuestion5_iff`是归约。Cert1024分支还列出34个 `native_decide` 公理与列表完整性假设；未重跑。

**题面先修：** Dₙ(G)=G∩(1+I(G)ⁿ)，不是只用(g−1)ⁿ生成的理想；普遍 Dₙ=γₙ 只可写 n≤3，第四项已有 Rips 反例。

**路径：** 20.84/Rips → augmentation/fifth dimension 特征 → GitHub命中 → README、Solution、作者PDF → 固定提交访问失败。待锁定完整SHA和依赖、核计算穷尽与证书。索引新候选 **002381@b5cf1fe2df813dfb**待取得正文，不先判同题。

#### QX-P-001560 · 20.100 · 有限群 n=4,5,6 的新声明

[Ma 镜像稿](https://borowiecki.dev/pdf/2611.13582)，自署 **arXiv2611.13582v1，10 Nov 2026**，**Theorems 1.1–1.4**：有限群 n=4,5,6；另有有限群中每个相同循环生成子群等价类最多3元时的任意n情形。n=6剩余有限情况用穷尽计算。

不能省略 **finite**，不能把摘要末句扩成任意群、任意集合。官方 abs 不可达，镜像19页可读；未运行程序。

**路径：** Sun + 20.100 → aᵢⁱ/distinct powers 特征 → 新近题名检索 → 镜像定理。待官方版本、附录程序完备性复核。新索引候选 **002364@33e027da4ba86da1**仅待定。

#### QX-P-001566 · 20.115 · 2026 Wilde 猜想归约

[Malle–Navarro–Tiep arXiv2605.04513 PDF](https://arxiv.org/pdf/2605.04513)，**p.1 Conjecture A、p.2 Theorem B、p.3 Theorems C,D**给近单群归约和众多族验证。Theorem B 有忠实特征标、准单群等条件，一般猜想仍作为 Conjecture A 保留。

**路径：** Wilde nonvanishing/order divisibility → 官方摘要/PDF → 定理条件。建议加“部分进展”，勿写一般已证；跟踪最新版本与剩余近单群情况。

#### QX-P-001573 · 21.26 · 同步 Sylow 交的适用范围扩大

[Lisi–Sabatini v3](https://arxiv.org/html/2505.21222v3) **Conjectures A,B、Theorems 1.1、1.4、1.5**给两素数阶、充分大交错/对称群及奇数阶metanilpotent情形。它明确保留一般同步猜想。

新稿 [arXiv2609.28403](https://arxiv.org/abs/2609.28403)《Sylow synchronization in finite groups: the good case》（2026-09-23）摘要宣称扩到满足 **所有商群** good-case 条件的可解群，包括所有奇数阶群；另处理全部对称/交错群，与先前简单群结果合并。官方 abs/pdf/html均失败，不能假装已读其11页全文。

[作者主页论文11](https://hongyihuang328.github.io/research.html)确认新稿并标AI-assisted，链接 [Zenodo22913983](https://zenodo.org/records/22913983) 的 Lean/Magma 材料；后续访问429，未取得代码、未核声明对应、未重跑。

**路径：** Lisi Sabatini + 编号 → simultaneous minimal intersections → 新题名系统1确认 → 作者主页/Zenodo。待新稿全文定理号、固定代码版本及依赖。必须保留“同一个x”和“按包含极小”；不是最小阶，也不是每个Sylow各选一个x。

### 三、撤回与查重发现

#### QX-P-001562 · 20.105：与16.5(a)等价；相关2026稿撤回

**同题论证：** 对p群，局部有限等价于局部幂零，因为有限生成挠幂零群有限。因此 **001562@a7d1fa7cba6b4850**与 **000678@07c4f10f84a58d8d** 的 **16.5(a)** 在其余perfect/真子群超中心条件相同时等价。16.5(b)问真子群可解，不能整卡合并。

**撤回：** [Arikan原稿出版社页](https://link.springer.com/article/10.1007/s11587-025-01048-7)已标 RETRACTED，说明2026-08-30撤回（10-09更新）。Theorem2.2有致命错误，[corrigendum](https://link.springer.com/article/10.1007/s11587-026-01124-6)的修补又用了错误正规性假设；原稿出版社说明两篇均撤回。纠正文页面仍可读旧内容，不等于已经修复。

该线索也关联 **001570/21.6** 的finitary/minimal non-FC背景；本轮不把相关撤回等同于20.105或21.6本身的开放性证明，也不移植另一论文的非传递例。

**路径：** perfect + locally finite/locally nilpotent + hypercentral → 2026 non-FC新稿 → DOI原稿 → corrigendum与撤回说明；库内16.5(a)正文逐条件比较。

#### 已完成的七个指定对子

| 本题 | 对方及版本 | 分类 | 核心差别 |
|---|---|---|---|
| 001558 | 000962@d31412abb8d08963 | 同源不同问 | 20.94问无限简单例；20.95加对合/无V4条件问Frobenius结构 |
| 001559 | 000668@1bcce0c1392dcb57 | 相关但不等价 | 2群整体局部有限 vs 一般周期群有非平凡局部有限正规子群 |
| 001562 | 000678@07c4f10f84a58d8d | 同题，仅(a) | p群中LF⇔LN；(b)须保留独立 |
| 001563 | 001564@91cdfef47545e1ad | 相关但不等价 | RF2群 vs exponent8；两者在p群内的LF/LN结论等价 |
| 001570 | 001102@8d192682f45a37b6 | 相关但不等价 | 有限Sylow共轭问题 vs 置换作用的cyclic-block |
| 001570 | 001616@de6f1a34428be7e9 | 同源不同问 | 求cyclic-block性质 vs 假设此性质后求minimal non-FC子群 |
| 001579 | 000686@85d14073184f13d9 | 相关但不等价 | 正规于整个P vs 正规于其正规闭包 |

另两条002381、002364只做索引候选，未取正文，分类待定。所有指定对子的版本和关系已记录在逐题JSONL的duplicates及 `audit/assigned_pair_keys.json`，没有合并题卡。

### 四、必须修正的题面与范围

- **001558/20.94：** saturated定义针对“每个有限子群”，不是“每个有限子集”。后者额外强迫局部有限。原稿定义见[Notebook14.101及20.94](https://arxiv.org/html/1401.0300v50)。Frobenius补的共轭也不包含核中全部非单位元。
- **001563–001564/20.106–107：** [Hadjievangelou–Traustason2024](https://doi.org/10.1090/proc/16695)是**strong** left3-Engel的局部幂零根基定理；普通left3-Engel的奇阶结果不能用于2阶。AMS入口及作者PDF下载受限，[作者机构摘要](https://researchportal.bath.ac.uk/en/publications/sandwich-groups-and-strong-left-3-engel-elements-in-groups/)可读。不得把“非整体幂零”例当“非局部有限”例。两题环境不同，p群里的LF/LN结论却等价。
- **001565/20.113：** H(q,c)的指数q、类至多c/相应最大商约束不可丢；只写四生成元的一条换位子关系并未定义原群。拆开H(8,12)和H(7,13)。[Vaughan-Lee2021v3](https://arxiv.org/html/2111.11098v3)的R(2,q;c)界不等于这两个四生成群的精确乘子指数。
- **001570/21.6：** block须对每个g满足 B^g=B 或不交，不能解释为被整个G保持的子集。finitary也不等于finite。
- **001571/21.9：** 严重包含方向误译。[作者2026v3 §12 Question4](https://arxiv.org/html/2507.04120v3)要求 **F的一族开子群，且族中含F这一项**；不是“各个开子群包含F”。Observation6.10的抽象自由群结果未解决pro-p版本。
- **001576/21.41：** self-similar的state-closed作用不自动是finite-state。原题还要求无挠、有限表示、metabelian以及包含Z≀Z，任何一项不可省略。[Intransitive Self-similar Groups v2](https://arxiv.org/abs/2004.08941)只消除Z≀Z自身自相似的障碍。
- **001577/21.42：** [arXiv2509.16947v1](https://arxiv.org/html/2509.16947v1) **Theorem A**二生成情形、**Theorem D**四生成N3,4情形和 **Problem1**三生成缺口须分清；Theorem D连非传递忠实state-closed表示也排除，不应错误缩为仅transitive。
- **001578/21.50：** [Glauberman2024摘要/TheoremA](https://www.sciencedirect.com/science/article/abs/pii/S0021869324000115)是两个特征子群的乘积控制transfer，非单个C。按期刊摘要校正S/T混排；原稿入口403，不能声称已核全文。2026 Flavell稿另外要求Qd(p)-free和characteristic-p，不覆盖所有G。
- **001579/21.51：** [原稿p.186](https://arxiv.org/html/1401.0300v50)子问(b)、p=2时仅n=1，旧卡n≤4错误。p≥5待查范围精确为p=5,n=6；p>5时n=(p+3)/2,(p+5)/2,(p+7)/2。这个清单是原问题集报告，非由本轮零命中推出。
- **001580/21.52：** 要求保留**全部积阶颜色**的D置换延拓到L自同构，可严谨写成Aut(L)的D稳定子的限制像。不要混入21.53的两颜色交集问题。[nilradical21.53成果页](https://nilradical.ai/notes/kourovka-21-53/)的反例不回答21.52。
- **001559/20.97的公开AI命中排除：** [PF2026.000026v1](https://www.proofforum.org/abs/PF%3A2026.000026)明说回答20.56，指数整除4n（n奇、≥665），未提供2群。页面无Palomar且人审Not reviewed，既不能升级为已证，也不能迁移到20.97。

以上各项实际检索词、入口、返回URL及访问强度在逐题JSONL，真实请求与返回题名/URL在 `audit/web_calls.jsonl`；限定域搜索覆盖属于“已执行搜索”，不冒称每站内部入口均逐一访问。后续优先复核三项完整声明、两个新近部分进展的受限官方入口、固定代码版本和两条新查重候选。



---

## QX-NEW-02 第三分片：影响状态、题面与查重的发现

核查日期：2026-11-26。范围为本分片 25 题；逐题记录在 `QX-NEW-02_逐题回传.jsonl`，实际请求与返回题名/URL在 `audit/web_calls.jsonl`，逐题库内匹配记录在 `audit/queries_by_topic.jsonl`。本文件仅列重要变化。以下“待核”均不代表本轮已验证完整证明。没有改线上、发帖、执行第三方代码或重跑形式化系统。

### 1. QX-P-001585：完整范围的条件性算法声明，尚不能写成无条件已解

旧卡“未见专门解决”需要更新。[Kharlampovich–Miasnikov, arXiv:2610.25305](https://arxiv.org/abs/2610.25305) 当前 v1（2026-10-18），PDF p.7 Theorem 3.8 声称判定任意有限单关系表现所定义群是否双曲。输入并不要求预先承诺 BS-free；算法的完备性依赖假设 (H)。作者在 p.3 明说尚未核完其上游 OpenAI 证明，p.39 披露 ChatGPT 6 Pro 协助。

已取得 [OpenAI 上游固定提交 PDF](https://raw.githubusercontent.com/openai/math/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Baumslag-Solitar-free-one-relator-groups-are-hyperbolic-September-25-2026/paper.pdf)，提交为 `adc7f1241b42e322a6451854ab7e4b4c146bf78a`，SHA-256 为 `b57883368214111506c2a050d54f486630c66b36ec467fe9cf746ed133557b93`。p.2 Theorem 1.1 对有限生成元集与任意单关系，声称若不含任何 BS(m,n)（m,n 为非零有符号整数）则双曲；其中包括排除 Z²，没有另加无挠假设。本轮仅核定理范围与依赖，没有独立审完 53 页证明。

固定提交的 `lean/formalization.yaml` 已取得；用 Gersten/Baumslag/relator 检索目录未定位此定理，`lean/docs/258.md` 返回 404。该有界检索不证明仓库全无形式化；本轮没有取得并重跑对应定理代码。

**回传状态：完整证明/反例声明待核。** 待核上游 (H) 全证与下游证书枚举完备性。不要以互相引用或多个 AI 系统的复述替代证明验证。

### 2. QX-P-001598：原配方与修正配方必须分成两个子问

旧卡遗漏 [Fraga, Protected p-Division…](https://www.preprints.org/manuscript/202608.2109)，当前 v1，2026-08-28，未同行评议。文中 Theorem 1、Definition 4、Table 1、§9、Corollary 5 声称公开显示的旧配方有缺项与索引问题，并对明确修正的配方给出群及左 brace 构造。适用条件包括 p>3、有限 p 加法群及 Property 3。

本轮直接对照 [Smoktunowicz 原稿 v2](https://arxiv.org/html/2410.20440v2)（2025-03-29）的 Definition 66、Theorem 67 与 Fraga Table 1。原构造使用 Definitions 60/64 的 Ω、W；Theorem 67 先给 pseudobrace。Fraga 的改动涉及保护指数、分支条件、求和指标、递归幂与除 p 保护，不是可以忽略的排版改写。作者也明确只对照公开显示文本，不替原作者解释所有可能澄清。文末披露 AI 辅助探索、起草和内部检查，没有本轮可执行形式化验证。

**回传状态：原公开配方的缺陷声明、显式修正配方的完整证明声明均待核。** 待逐式核 Table 1 与原 Definitions 60/64/66、唯一性与 BCH 封闭，不能直接把修正版写成原题已证。

### 3. QX-P-001602：发现直接回答 21.131 的完整正面声明

[Alec Kriebel, Locally finite p-groups in Golod groups and an AT section](https://aleckriebel.com/research/locally-finite-p-groups-golod-at-section/paper.pdf)，v1.0.0（2026-10-24），关联 [Zenodo DOI](https://doi.org/10.5281/zenodo.23624706)。p.1 Theorem 1 声称任意可数无限局部有限 p 群可嵌入一种 Golod 群并成为经典齐次、剩余有限 Golod 群的 section；p.2 Corollary 2 据此给无限 AT 群，直接覆盖本题“Golod 群某子群满射到无限 AT 群”。目标及子群允许无限生成。

p.6 §6 明示没有 proof assistant 验证，也没有独立同行评议；有限画像或矩阵检查不证明全称定理。**状态应从无专门结果改为完整证明/反例声明待核。** 需核 AT 定义中无限支撑条件、Lemma 7 标量扩张及所引依赖。

与 QX-P-001002（13.55）的关系为“特例/强化”：13.55 要求整个 Golod 群就是 AT 群，21.131 只要求子群的商。新稿不解决前者，不能并题。

### 4. QX-P-001604：SJ 的可数可识别性存在正对原题的反例声明

[Brescia–Di Siena–Ingrosso–Trombetti, arXiv:2610.05415](https://arxiv.org/abs/2610.05415)，当前 v1（2026-10-04）。PDF p.2 Main Theorem 声称存在不属于 SJ 的群，而其每个可数子群都属于 SJ；这直接否定 21.133。p.4 Definition 2.5 的系列允许一般序型，且各项均以有限次正规深度次正规于整个群（深度可随项变化），并非只要求相邻项次正规，也不是有限可解列。

该定义已与 [de Giovanni–Trombetti 2021 原作者综述](https://www.mdpi.com/2227-7390/9/19/2366) §4 的 SJ 描述及原问题对应。旧卡将结果仅判为“邻近定义”应撤销。**回传为完整反例声明待核**，并非本轮独立验证为已反驳；仍需核长链/可数子群论证与所有次正规条件。

### 5. 已刊或原作者部分成果：保留范围限制

| 题号 | 需要补充或更正的进展 | 精确边界 |
|---|---|---|
| QX-P-001588 | [Busch–Pengitore–Schillewaert–Van Maldeghem, arXiv:2510.06479v1](https://arxiv.org/html/2510.06479v1)，Main Theorem | small Ree 群 ²G₂(3^(2e+1))、e≥1、生成元数 k≥5；不能扩成全部有限单群与全部 k≥3。 |
| QX-P-001597 | [de las Heras–Zozaya，Annali 205 (2026), 749–758](https://link.springer.com/article/10.1007/s10231-025-01622-8)，Theorem 1.1；2025-11-18 在线 | 原题是 profinite 群。有稠密 equationally Noetherian 子群时，字值集若小于连续统则有限。不可去掉额外条件，也不可把有限字值集直接换成有限 verbal subgroup。出版方全文已核。 |
| QX-P-001599 | [Chang–García Mejía–Migliorini，GAFA 36 (2026), 1–58](https://doi.org/10.1007/s00039-026-00731-7)，Theorem 1 | Bestvina–Brady 群的 Dehn 函数分类为 n^d，d∈{1,2,3,4}。只是 RAAG 子群中的特定族，不排除任意有限呈示子群出现原题两种增长。 |
| QX-P-001601 | [Soroko, arXiv:2009.10471v4](https://arxiv.org/abs/2009.10471v4)，p.1 Theorem 1、p.2 首段；Topology Appl. 300 (2021), 107770 | F4、H4 各自不与 D4 可公度，不能删掉 D4 变成 F4 与 H4 彼此不可公度。当前 v4 与官方 PDF 已核，旧 UNT 链接现在重定向首页。 |
| QX-P-001605 | [Vasil’ev, arXiv:2608.12783](https://arxiv.org/abs/2608.12783)，v2，p.6 Problem 3.9(ii) | 当前论文确实重新提出平凡可解根是否由字符次数多重集 cd 保持。相邻 inv=eo 的元素阶反例不回答 cd 问题，不能串项。 |
| QX-P-001606 | [Wilson, arXiv:2209.14753](https://arxiv.org/abs/2209.14753)，v1；Arch. Math. 120 (2023), 557–563 | 有限生成 profinite 情形有更强的有限性结论；一般 profinite 情形没有据此解决。 |

QX-P-001592 另应补 Yong Yang 的一般 23/3 上界（[DOI 10.1017/S0004972720001409](https://doi.org/10.1017/S0004972720001409)），只核到出版方摘要。2026 年元素阶 rho–sigma 新文线索仅有检索摘要且原稿未定位，不用于推断本题 codegree 常数 4 已解决。

### 6. 必须修正的题面、量词或定义

原问题均重新对照 [Kourovka Notebook v50](https://arxiv.org/abs/1401.0300v50)（本轮核版本为 2026-11-02），而非沿用任务卡的版本标签。

| 题号 | 原文定位 | 建议更正及理由 |
|---|---|---|
| QX-P-001582 | p.188，21.61 | 有限生成子群有限呈示的存在性由 coherence 背景保证；待问的是给定生成元求呈示的算法。不要把它拆成两个同等开放子问。[Feighn–Handel 1999](https://annals.math.princeton.edu/articles/12500) 出版方摘要已核。 |
| QX-P-001583 | p.188，21.62 | 原题固定 G=F_n⋊Z，输入子群生成元及 w；不要加强为跨所有 G 的统一算法。submonoid membership 的不可判定结果不自动回答 subgroup membership。 |
| QX-P-001584 | p.188，21.64 | p^e 指 exponent；所问 ⟨A^G⟩ 是正规闭包，不能译成正规化子。 |
| QX-P-001586、001587 | pp.189–190，21.73–74 | class transposition 交换两条互不相交的剩余类，不是“互素模数”；互素模数由 CRT 反而相交。[RCWA 手册 §2.2-3](https://gap-packages.github.io/rcwa/doc/chap2_mj.html) 全文已核。21.74(a) 的 nontrivial 修饰 partition；(b) 只有有限长度的循环，不是循环数量有限；(c) 没有有限循环也不是 (b) 的简单否定。 |
| QX-P-001589、001590 | p.193，21.94–95 | 比较无标记的素图同构，不要求固定素数顶点标签。有限多个已识别简单群例子不能给 21.94 的无限性，也不能给 21.95 的非单 almost simple 例子。 |
| QX-P-001597 | p.197，21.122 | profinite 不能改成抽象剩余有限群。误译版被 G=Z、w=x 的可数无限值集反驳；该例不反驳原 profinite 题。 |
| QX-P-001608 | p.200，21.141 | polycyclic 应为多循环；pro-p coherence 指拓扑有限生成的闭子群均有限 pro-p 呈示，不能改写为有限指标开子群条件。 |

### 7. QX-P-001607 的出处与配对复核

找到 [Witzel 2020 原 MathOverflow 问题](https://mathoverflow.net/questions/363613/infinite-dimensional-torsion-free-f-infty-group-not-containing-f) 和 [Zaremsky 2026-10-08 问题清单](https://zaremsky.github.io/open_problems.pdf)，后者 p.3 §2 Problem 8 精确要求无挠、type F∞、无限上同调维数且不含 Thompson F。本轮已渲染原页，目视确认该条未划线；文本抽取会漏失删除线，因此保留图像检查记录。清单仍列题不构成穷尽文献证明，本轮结论为“暂未找到可验证结果”。

指派配对 7 对均读双方当前正文，版本与内容哈希在审计中。结论如下：

| 配对 | 关系 | 实际差别 |
|---|---|---|
| 001589 / 001590 | 同源不同问 | 可识别群无限性与一个非单 almost simple 群的存在性。 |
| 000153 / 001601 | 相关但不等价 | 一般球型 Artin 拟等距⇒可公度与 F4/H4 的特定可公度问题。 |
| 001002 / 001602 | 特例/强化 | 整个 Golod 群为 AT，与 Golod 子群具有 AT 商。 |
| 001605 / 002395 | 相关但不等价 | 一般平凡可解根的性质识别，与 almost simple 范围的完整同构识别。 |
| 001607 / 001609 | 同源不同问 | 无限维 F∞ 群含 F，与几个 Thompson 直积之间拟等距。 |
| 001607 / 001944 | 待定 | 001944 正文自承来源删除且题面是猜测，不能认证等价或据标题合并。 |
| 001607 / 002499 | 相关但不等价 | 后者是 type F/有限上同调维数的乘积问题，与无限维含 F 不同。 |

### 8. 实际检索路径与复核边界

本分片调用编号对应合并审计中的 c:001 至 c:043；后续文件下载是公开原稿的只读获取，访问和版本见逐题evidence，已取得文件的SHA-256在 `audit/retrieved_source_hashes.json`。实际搜过的入口、检索词、批量结果和访问级别都在逐题 JSONL/合并审计内。批量查询响应不提供逐条归属，不能把整批命中机械分派给某个入口，也没有把未命中推断成仍开放。

下列为重要发现的真实查询路径摘录（不是计划）：

#### QX-P-001585；card_rev dba2063be9e6fa14

- system2_search_query，audit 004：`"one-relator" "hyperbolicity" algorithm Linton`。
- system1_search_query，audit 005：`Gersten conjecture one-relator hyperbolic algorithm OpenAI 2026`。
- system2_search_query，audit 023：`("one-relator" "hyperbolic") site:github.com/openai/math`。
- system2_search_query，audit 024：`"one-relator" "hyperbolic" (site:proofforum.org OR site:zenodo.org OR site:mathoverflow.net OR site:aixiv.science)`。

#### QX-P-001598；card_rev 49b97306caf343b3

- system2_search_query，audit 014：`"Smoktunowicz" "Definition 66" pre-Lie`。
- system2_search_query，audit 015：`"extended Agrachev" "pre-Lie" groups 2026`。
- system2_search_query，audit 029：`"Smoktunowicz" "66" site:github.com`。
- system2_search_query，audit 030：`"Smoktunowicz" "extended" (site:preprints.org OR site:zenodo.org OR site:proofforum.org OR site:eulersolve.org)`。

#### QX-P-001602；card_rev fcb5bb0548df0a67

- system2_search_query，audit 016：`"Golod" "AT-group" homomorphism`。
- system2_search_query，audit 017：`Timofeenko Golod subgroup quotient Rozhkov Aleshin type 21.131`。
- system2_search_query，audit 032：`"Golod" "AT" site:github.com`。
- system2_search_query，audit 033：`"Golod" "AT" (site:zenodo.org OR site:mathoverflow.net OR site:proofforum.org OR site:aixiv.science)`。

#### QX-P-001604；card_rev b2747ae2c7a6b37a

- system2_search_query，audit 004：`"subnormal abelian series" "countable" Trombetti`。
- system1_search_query，audit 005：`"subnormal abelian series" "countably recognizable"`。
- system2_search_query，audit 018：`"subnormal abelian series" "SJ"`。
- system1_search_query，audit 019：`"subnormal abelian series" SJ`。
- system1_search_query，audit 019：`"21.133" "Trombetti" solution`。
- system2_search_query，audit 020：`Trombetti countable recognizability "SN" "SJ"`。
- system2_search_query，audit 020：`de Giovanni Trombetti 2021 compendium countably recognizable subnormal series`。
- system2_search_query，audit 020：`"subnormal abelian" "countably"`。
- system2_search_query，audit 020：`"The group class SJ is not" "21.133"`。
- system2_search_query，audit 034：`"SJ" "countably recognizable" site:github.com`。
- system2_search_query，audit 035：`"subnormal abelian series" (site:mathoverflow.net OR site:zenodo.org OR site:proofforum.org OR site:aixiv.science)`。

#### QX-P-001588；card_rev 3a068e76f733b5ae

- system2_search_query，audit 008：`"Wiegold conjecture" finite simple groups Nielsen equivalence`。
- system2_search_query，audit 009：`"Wiegold" "small Ree" 2026`。
- system2_search_query，audit 025：`"Wiegold" site:github.com`。
- system2_search_query，audit 026：`"Wiegold conjecture" (site:mathoverflow.net OR site:zenodo.org OR site:proofforum.org OR site:eulersolve.org)`。

#### QX-P-001599；card_rev 95d1ebc41d643cad

- system2_search_query，audit 014：`"right-angled Artin" "Dehn functions" "super-exponential"`。
- system2_search_query，audit 015：`finitely presented subgroups RAAG subexponential non polynomial Dehn functions 2026`。
- system2_search_query，audit 032：`"Artin" "Dehn" "super-exponential" site:github.com`。
- system2_search_query，audit 033：`"right-angled Artin" "Dehn" (site:mathoverflow.net OR site:zenodo.org OR site:proofforum.org OR site:eulersolve.org)`。

#### QX-P-001607；card_rev 86741bd645ed05e6

- system2_search_query，audit 016：`"torsion-free" "infinite cohomological dimension" "Thompson"`。
- system2_search_query，audit 017：`Witzel Zaremsky F_infty infinite dimensional without Thompson F counterexample 2026`。
- system2_search_query，audit 034：`"Thompson" "infinite cohomological dimension" site:github.com`。
- system2_search_query，audit 035：`"torsion-free" "F_infty" "Thompson" (site:mathoverflow.net OR site:zenodo.org OR site:proofforum.org OR site:eulersolve.org)`。
- system1_search_query，audit 036：`"infinite dimensional torsion free F infinity group" "Thompson"`。


全库索引实际扫描 2469 条；未指派的新标题相似命中只保留线索，不作正文等价认证。未执行 Lean、Mathlib、GAP、Magma 或任何外部验证代码。各定理的完整性、证明正确性与形式化可运行性仍按上述范围待核。


---

## 第四组：QX-P-001609—001633的重要变化

### QX-P-001615 · 17.11 存在不属于 Hirsch–Plotkin 根的左 3-Engel 元？

修正“正规闭包非幂等”为“非幂零”；非幂零不等于非局部幂零，不能推出元素在HP根外。

- **强条件下已知结论｜部分进展：** Hadjievangelou–Traustason Theorem1.2证明strong left3-Engel元属于HP(G)。
- **原卡术语｜题面有误：** 幂等是误词；应为正规闭包非幂零。

**直接证据与定位：**

- [Sandwich groups and (strong) left 3-Engel elements](https://arxiv.org/abs/2303.16693)；Theorem1.2 p4；引言关于奇数阶与一般左3-Engel的区分。原论文明确强条件；没有证明所有左3-Engel元均在HP根。 核查层级：全文；不适用；未执行外部代码或形式化重跑。

**实际检索路径：**

- system2_search_query：`"left 3-Engel" "radical" sandwich 2026`。
- system2_search_query：`Kourovka 17.11 left three Engel Noce Tracey Traustason normal closure`。

随后核对上述原稿/作者页；GitHub、公开AI/社区和库内查重的逐题词及日期见JSONL，本包审计保留实际批次。

### QX-P-001616 · 17.13 全非本原 finitary p-群含极小非 FC-子群？

发现Aydın2016的直接反例声明，但全文构造不传递，不满足Asar原来使用的totally imprimitive定义；另相关Arikan2026论文及勘误均已撤回，均不能作为原题关闭依据。

- **Aydın2016声称的完整反例｜完整证明/反例声明待核：** 已识别范围不适用：不交3-循环生成直和C3，每个轨道只有3点；Asar的totally imprimitive定义预设传递。此声明不能接受为原题反例。

**直接证据与定位：**

- [Aydın, On a Problem of Minimal Non-FC-Groups](https://ijpam.eu/contents/2016-108-2/16/16.pdf)；pp421–423：§1构造，Corollary3及Corollary5。作者声明否定17.13；构造固定每个三点块，缺传递性。本轮核到此直接范围障碍，未宣称该文所有结论均错误。 核查层级：全文（web不可达；经DOI重定向后本地下载成功）；不适用；未执行外部代码或形式化重跑。
- [Asar, Permutation groups with cyclic-block property and MNFC-groups](https://journals.tubitak.gov.tr/math/vol41/iss4/17/)；p983 §1第一段；PDF https://journals.tubitak.gov.tr/cgi/viewcontent.cgi?article=1908&context=math。totally imprimitive是在传递finitary群中排除primitive/almost primitive后的情形，明确不同于非传递直和构造。 核查层级：全文（网页PDF403，本地原站下载成功）；不适用；未执行外部代码或形式化重跑。
- [Arikan, RETRACTED ARTICLE: Nonexistence of perfect locally finite minimal non-FC and CC-groups](https://link.springer.com/article/10.1007/s11587-025-01048-7)；撤回说明及Change history：2026-08-30撤回，2026-10-09页面更新。Theorem2.2论证错误，勘误错误假设点稳定子正规；出版方明确两篇均撤回。 核查层级：全文网页；不适用；未执行外部代码或形式化重跑。

**实际检索路径：**

- system2_search_query：`"totally imprimitive" "minimal non" "FC" Asar`。
- system2_search_query：`"17.13" "Asar" "problem" FC`。

随后核对上述原稿/作者页；GitHub、公开AI/社区和库内查重的逐题词及日期见JSONL，本包审计保留实际批次。

**待复核：** 如后续追查Aydın更正，须首先核传递性及原作者定义；本轮无联系作者或线上评论。。

### QX-P-001618 · 17.25 Farbman 例外集 X 的有理点问题

17.25(b)可由Kim–Koberda已发表定理直接肯定：27/7本身在X中；(a)所有有理数的总问仍不能关闭。

- **(b) X∩Q∩[27/7,4)是否非空｜原题已证：** Kim–Koberda Theorem1.4(1)覆盖s≤27且s≠24的s/r∈(−4,4)。取s=27,r=7，得到27/7∈X。
- **(a) (−4,4)中全部有理数｜部分进展：** 上述分子范围和密度结论为部分结果；2026 Jang–Yi稿仍把全有理数情形写成Conjecture1.2。

**直接证据与定位：**

- [Kim–Koberda, Non-freeness of groups generated by two parabolic elements with small rational parameters](https://arxiv.org/abs/1901.06375v4)；Theorem1.4(1)，p3；矩阵定义p1。矩阵与原题I+αe12、I+e21一致；代入27/7是本轮推论。论文有Mathematica辅助部分，未重跑。 核查层级：全文；取得论文中计算说明；未执行Mathematica或独立形式化验证。
- [Sang-hyun Kim作者论文目录](https://me.kimsh.kr/research.html)；Published papers第31项。核实2022年Michigan Mathematical Journal刊载信息。 核查层级：全文网页；不适用；未执行外部代码或形式化重跑。
- [Jang–Yi, 关于有理参数两抛物元非自由性的后续论文](https://arxiv.org/abs/2512.20524)；v3 (2026-07-31)，Conjecture1.2及Theorem1.3，p2。沿用Kim–Koberda结果，未把(a)一般情形宣称已解。 核查层级：全文；不适用；未执行外部代码或形式化重跑。

**实际检索路径：**

- system2_search_query：`Farbman nonfree rational "27/7" "4"`。
- system1_search_query：`Farbman Jang Yi rational nonfree parabolic groups 27/7`。

随后核对上述原稿/作者页；GitHub、公开AI/社区和库内查重的逐题词及日期见JSONL，本包审计保留实际批次。

**待复核：** 若要库级结案复核(b)，复查已刊版本Theorem1.4(1)及27/7落区间即可；无需为本次初查重跑全部Mathematica。。

### QX-P-001620 · 17.38 超可解形成" Radical"于饱和遗传形成类的刻画

原题17.38问满足条件的饱和遗传形成集合M是否有最大元；原卡标题泛化成刻画任务，并须校正饱和的定义。

- **题面范围及术语｜题面有误：** 原问是最大元存在性；饱和的标准条件为G/Φ(G)∈F⇒G∈F，不能以扩张封闭代替。

**直接证据与定位：**


**实际检索路径：**

- system2_search_query：`supersoluble formation radical largest saturated hereditary "17.38"`。
- system1_search_query：`"supersoluble" "radical" "largest" formation`。

随后核对上述原稿/作者页；GitHub、公开AI/社区和库内查重的逐题词及日期见JSONL，本包审计保留实际批次。

### QX-P-001621 · 17.52 Eggert 猜想 dim R ≥ p·dim R(p)

17.52原稿限定有限域；短题面若只写特征p会丢失p次幂像作为F子代数所需的域条件。一般问题本轮未关闭。

- **题面域条件｜题面有误：** 恢复有限域F。若另列完美域推广，必须明确是推广且R^(p)指p次幂像。

**直接证据与定位：**

- [Bergman, Thoughts on Eggert’s Conjecture](https://arxiv.org/abs/1206.0326)；摘要、完美域及p次幂像定义。综述的完美域版本可解释为何不能悄然把原题放大为任意特征p域。 核查层级：仅题名/摘要；完整初版未另下载；不适用；未执行外部代码或形式化重跑。
- [Eggert’s Conjecture on Nilpotent Algebras](https://www.tandfonline.com/doi/abs/10.1081/AGB-120027963)；出版社摘要。覆盖某些分次代数和有限阿贝尔群代数的根，非全部有限维交换幂零代数。 核查层级：仅摘要；不适用；未执行外部代码或形式化重跑。

**实际检索路径：**

- system2_search_query：`Eggert conjecture nilpotent algebra dimension p powers 2026`。
- system1_search_query：`"Eggert" conjecture proof nilpotent algebra 2026`。

随后核对上述原稿/作者页；GitHub、公开AI/社区和库内查重的逐题词及日期见JSONL，本包审计保留实际批次。

### QX-P-001623 · Erdős–Moser 方程

更正平凡解、旧下界作者及4,990,906素因子计数对象；新增2026-11-21下界预印本，并单列未验证的SSRN完整证明声明。

- **2026非平凡解下界｜部分进展：** Mehdi-Nezhad–Rahimi Theorem1声称m>6.2612×10^1667658425；已读全文，未独立检查长链计算。
- **SSRN5237097完整证明｜完整证明/反例声明待核：** Bouazad2025摘要声称仅有(m,k)=(3,1)，本轮只有元数据/摘要，不能据此判已证。
- **旧卡数值与出处｜题面有误：** 平凡解是m=3,k=1而非m=1；2.7139×10^1667658416来自Gallot–Moree–Zudilin；4,990,906因子结论指(m²−1)(4m²−1)/12，不是m本身。

**直接证据与定位：**

- [Mehdi-Nezhad–Rahimi, A two-sided continued-fraction criterion for the Erdős–Moser equation and Erdős’s 1949 problem](https://arxiv.org/abs/2611.28637)；v1 (2026-11-21)，Theorem1 p2。下界改进仍是必要条件；未引入全称无解结论。 核查层级：全文（web工具DisabledError，原站PDF本地取得）；不适用；未执行外部代码或形式化重跑。
- [Gallot–Moree–Zudilin, The Erdős–Moser equation revisited](https://arxiv.org/abs/0907.1356)；Theorem3 p5；Math.Comp.80(2011),1221–1237。旧下界的正确作者与定理来源。 核查层级：全文；不适用；未执行外部代码或形式化重跑。
- [Moree, Moser’s Mathemagical Work on the Equation](https://webdoc.sub.gwdg.de/ebook/serien/e/mpi_mathematik/2010/2009_92.pdf)；Theorem2(5)，p2。4,990,906个素因子属于指定四因子乘积/12。 核查层级：全文PDF入口；不适用；未执行外部代码或形式化重跑。
- [Dong–Nguyen–Zaharescu, Erdős-Moser equation in arithmetic progressions](https://arxiv.org/abs/2608.03375)；v1，p1摘要及式(1.2)。原卡把该编号当成长篇综述；实际研究等差数列限制求和的变体，不能当原式全解。 核查层级：全文；不适用；未执行外部代码或形式化重跑。
- [Bouazad, Erdos Moser Equation Proof](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5237097)；Posted7May2025，8页，摘要。完整声明保留待核，未获取可读证明正文。 核查层级：仅题名/摘要；不适用；未执行外部代码或形式化重跑。

**实际检索路径：**

- system2_search_query：`Erdos Moser equation 2608.03375 nontrivial solution bound`。
- system1_search_query：`"Erdos Moser" "odd" "Kellner" 0907.1356`。

随后核对上述原稿/作者页；GitHub、公开AI/社区和库内查重的逐题词及日期见JSONL，本包审计保留实际批次。

**待复核：** 优先复核2611.28637 Theorem1的两侧误差估计及旧continued-fraction数据依赖。；SSRN完整证明须取得全文后再评估，当前不改总体状态。。

### QX-P-001624 · Gilbreath 猜想

Colonna的Proth–Gilbreath计算就是通常素数差分问题，不是“素数幂版本”；2026 Chase–Hunter–Tao结果针对随机模型与条件性推广，不能当原素数序列证明。

- **2026模型与计算进展｜部分进展：** 已核Colonna页面报告素数数值上限1.5×10^15；Chase–Hunter–Tao预印本给Cramér模型结论及条件性路径。
- **题卡出处描述｜题面有误：** 删除“Proth–Gilbreath是素数幂版本”；三位作者应完整列出。

**直接证据与定位：**

- [Colonna, Proth–Gilbreath Conjecture Verification](https://www.lactamme.polytechnique.fr/descripteurs/Proth_Gilbreath_Conjecture.01.Ang.html)；标题、Definition及Results；2026-03-18纪录。1.5×10^15是所用素数的数值上限，不是已验证的行数；本轮未独立重跑。 核查层级：全文网页；他人报告计算；未重跑。
- [Chase–Hunter–Tao, Gilbreath相关预印本](https://arxiv.org/abs/2607.08712)；摘要及引言定理范围。随机Cramér模型不是确定素数序列；条件性inverse theorem亦要保留前提。 核查层级：全文；不适用；未执行外部代码或形式化重跑。
- [michaelmross/Gilbreath](https://github.com/michaelmross/Gilbreath/tree/0e64bed2ba3a27046cd7ac290f9e24395388b94c)；仓库HEAD固定于本次只读git ls-remote。实验/计算仓库命中；未审阅或运行全程序，不能算证明。 核查层级：仓库索引/提交信息；他人代码命中，未重跑。

**实际检索路径：**

- system2_search_query：`Gilbreath conjecture Chase 2607.08712 Colonna 2026`。
- system1_search_query：`"Gilbreath" "Colonna" "1.5" primes verification`。

随后核对上述原稿/作者页；GitHub、公开AI/社区和库内查重的逐题词及日期见JSONL，本包审计保留实际批次。

### QX-P-001625 · Kolakoski 序列密度（Keane 猜想）

原卡给Brent2016的arXiv1605.00224实际是STIRAP物理论文；正确来源是Brent与Osborn相关报告及Brent的UNSW讲义。密度1/2尚未获得本轮可验证的全证明。

- **出处与计算范围｜题面有误：** 1605.00224不属于Kolakoski；正确讲义只说计算various n≤5×10^17的discrepancy。

**直接证据与定位：**

- [Vitanov等, Stimulated Raman adiabatic passage in physics, chemistry and beyond](https://arxiv.org/abs/1605.00224)；题名及作者。核实原卡arXiv编号错配。 核查层级：题名/摘要；不适用；未执行外部代码或形式化重跑。
- [Brent, Fast algorithms for the Kolakoski sequence](https://maths-people.anu.edu.au/~brent/pd/Kolakowski-UNSW.pdf)；2016-11-16，slides1–2。与Judy-anne Osborn合作；若干n≤5×10^17的计算属数值证据，不能推出密度存在。 核查层级：全文PDF；不适用；未执行外部代码或形式化重跑。
- [OEIS A000002](https://oeis.org/A000002/internal)；Nov09 2026条目，Comments。索引明确密度问题未解；直接open403，仅返回缓存全文片段，访问限制保留。 核查层级：检索返回内容；直接入口403；不适用；未执行外部代码或形式化重跑。
- [Formal Conjectures OEIS 2](https://google-deepmind.github.io/formal-conjectures/src/FormalConjectures/OEIS/%C2%AB2%C2%BB/)；Density of ones in the Kolakoski sequence。仅命中题面形式化入口，没有把它当完成证明。 核查层级：题名/摘要；仅形式化题面入口命中；未重跑。

**实际检索路径：**

- system1_search_query：`Kolakoski sequence density half conjecture 2026 bounds`。
- system2_search_query：`Kolakoski density frequency 1 2 Brent fast algorithms 2016 arxiv`。

随后核对上述原稿/作者页；GitHub、公开AI/社区和库内查重的逐题词及日期见JSONL，本包审计保留实际批次。

### QX-P-001626 · Singmaster 猜想

发现声称Lean完整解决的仓库，但固定提交文件仅有def，未证明各转换或终命题；其终命题要求坐标统一有界，既不等价于重数有界且直接为假。

- **2026 Lean完整声明｜完整证明/反例声明待核：** 已核代码不支撑声明：没有theorem/lemma证明链，末尾singmasterConjectureBound只是Prop定义；不能接纳为形式化解。
- **Pascal三角形内区｜部分进展：** Matomäki–Radziwiłł–Shao–Tao–Teräväinen给远离边界区间的重数界，未覆盖全部位置。

**直接证据与定位：**

- [AEjonanonymous, Bounding Singmaster’s Conjecture via Constructive Type Transformation in Lean4](https://github.com/AEjonanonymous/Singmasters-Conjecture/blob/421bb3d8c209ae8f0b2bf62ab614188012fdaaa5/SingmastersConjecture.lean)；全文件；末尾def singmasterConjectureBound。所有14步均为定义，无等式/包含关系的证明。终命题∃M∀t∀(n,k)∈solutionSetSeparated(t),n,k≤M；取任意n≥4，k=2,t=n(n−1)/2即可让n无界，故不是所需重数界。 核查层级：完整5002字节代码已取得并静态阅读；额外公理/占位或不等价：只有定义、目标不等价；未重跑。
- [同一作者Zenodo记录](https://zenodo.org/records/21660302)；标题/摘要及仓库README关联。保留完整形式化解决的声明出处；不把声明当验证。 核查层级：仅题名/摘要；他人声称已形式化验证；本轮代码审查发现不等价。
- [Matomäki–Radziwiłł–Shao–Tao–Teräväinen, Singmaster’s conjecture in the interior of Pascal’s triangle](https://arxiv.org/abs/2106.03335)；主定理；Q.J.Math.73(2022),1137–1177，DOI10.1093/qmath/haac006。只对离边界足够远的大参数位置给上界；非全部Pascal三角形。 核查层级：摘要/主定理入口；不适用；未执行外部代码或形式化重跑。

**实际检索路径：**

- system1_search_query：`Singmaster conjecture 2026 King multiplicity Pascal triangle`。
- system1_search_query：`"Singmaster" "Kane" "log" multiplicity`。

随后核对上述原稿/作者页；GitHub、公开AI/社区和库内查重的逐题词及日期见JSONL，本包审计保留实际批次。

**待复核：** 如作者另给新版本，须查真正的∀t>1重数界定理、各化简证明及完整依赖后才考虑重跑。。

### QX-P-001627 · Erdős–Szekeres g(7) 精确值

旧卡33≤ES(7)≤37未找到可核来源；已核公开定理给33≤ES(7)≤113，2025/26 SAT稿只关闭锚定子类，不能据此宣称ES(7)=33。

- **可核界与SAT部分族｜部分进展：** Mojarrad–Vlachos Theorem1.1代n=7给126−15+2=113；Dumitru只报告锚定子族UNSAT。
- **旧卡上界37｜题面有误：** 所列来源未支撑37，应撤下无可验证出处的上界并保留可核113；不声称证明37不可能。

**直接证据与定位：**

- [Mojarrad–Vlachos, An improved upper bound for the Erdős–Szekeres conjecture](https://arxiv.org/abs/1510.06255v2)；Theorem1.1，p2。n≥6，ES(n)≤C(2n−5,n−2)−C(2n−8,n−3)+2，n7为113；经典下界2^(n−2)+1为33。 核查层级：全文；不适用；未执行外部代码或形式化重跑。
- [Dumitru, ES(7) SAT研究](https://arxiv.org/abs/2512.24061)；引言、锚定实例限制及实验结果。取得7页全文；锚定三/四凸链等子类不是全33点配置。 核查层级：全文；不适用；未执行外部代码或形式化重跑。
- [bogdan27182/esc-paper](https://github.com/bogdan27182/esc-paper/tree/9520ceac1758120124840e0b66b003c559cec4a7)；README；固定提交。已读README及论文，未运行SAT求解器、证书检查器。 核查层级：README代码入口；已取得代码入口未重跑；未核整个证书链。

**实际检索路径：**

- system1_search_query：`Erdos Szekeres seven points 33 37 2512.24061 2026`。
- system1_search_query：`"2512.24061" "113"`。

随后核对上述原稿/作者页；GitHub、公开AI/社区和库内查重的逐题词及日期见JSONL，本包审计保留实际批次。

**待复核：** 若要关闭ES7，需任意33点定向拟阵/可实现性编码的完整覆盖及可检查证书，不能从锚定UNSAT外推。。

### QX-P-001628 · Recamán 序列满射性（Sloane 1991 猜想）

确认Chaffin2026的10^612项计算报告属真实来源：利用连续加减区段跳跃；852655仍未出现不是“永不出现”的证明。

- **计算进展｜部分进展：** Chaffin报告计算至超过10^612项且最小缺项仍852655；本轮未重跑。

**直接证据与定位：**

- [Ben Chaffin, The Recamán Sequence](https://benchaffin.com/recaman/recaman.html)；2026-02-07页面；Results及Computation。作者解释ping-pong区段可整体跳跃。不是逐项储存10^612项，亦不推出无限缺项。 核查层级：全文网页；他人报告计算；未重跑。
- [OEIS A064228](https://oeis.org/A064228)；Extensions，2026-02-08 Chaffin条目。与作者报告的缺项和范围一致。 核查层级：检索条目；不适用；未执行外部代码或形式化重跑。

**实际检索路径：**

- system1_search_query：`Recaman sequence 852655 10 612 Chaffin 2026`。
- system2_search_query：`Recaman 2004.14000 2301.03149 three cousins surjective missing 852655`。

随后核对上述原稿/作者页；GitHub、公开AI/社区和库内查重的逐题词及日期见JSONL，本包审计保留实际批次。

**待复核：** 若找反例，须证明某整数对所有n均不出现；a20=a24=42、a18=a26=43本轮算术核对成立但无关满射性否定。。

### QX-P-001629 · Subprime Fibonacci 序列终归周期

短题面的递推下标及“和为素数时除以该素数”均有错，须恢复原定义；2026已刊广义递推成果不证明所有正初值最终周期。

- **定义和序列引用｜题面有误：** 令s=x_n+x_(n+1)，x_(n+2)=s（s素）或s/spf(s)（s合）。循环长度集合是A214897；A282814是按初值排列的周期长度表。
- **2026广义递推｜部分进展：** Ponomarenko等研究一般二阶subprime递推及小周期分类；不是全部原始Fibonacci参数的有界性证明。

**直接证据与定位：**

- [Guy–Khovanova–Salazar, Conway’s Subprime Fibonacci Sequences](https://arxiv.org/abs/1207.5099)；摘要及递推定义；Math.Mag.87(2014),323–337。正确规则为仅对合数和除最小素因子。 核查层级：摘要/原定义；不适用；未执行外部代码或形式化重跑。
- [Ponomarenko–Rhinehart–Schwarz–Tong, On Subprime Recurrences](https://www.tandfonline.com/doi/full/10.1080/00029890.2025.2594388)；Amer.Math.Monthly133(2026),275–280；作者稿 https://vadim.sdsu.edu/prst-amm.pdf，§1及Theorems1–2。作者稿明确长期行为一般未知；1/2周期分类和广义系数问题不可外推。作者稿有送审模板年份，与最终出版信息分开。 核查层级：出版社摘要及作者稿全文；不适用；未执行外部代码或形式化重跑。
- [OEIS A214897与A282814](https://oeis.org/A214897)；Comments及Crossrefs；https://oeis.org/A282814 的Example。A214897列1,10,11,18,19,56,136；A282814(1,1)=18，本轮小算术核对得到周期18。 核查层级：全文网页；不适用；未执行外部代码或形式化重跑。

**实际检索路径：**

- system1_search_query：`"Subprime Fibonacci" eventual periodicity Conway 2026`。
- system2_search_query：`Conway subprime Fibonacci 1207.5099 bounded eventually periodic smallest factor`。

随后核对上述原稿/作者页；GitHub、公开AI/社区和库内查重的逐题词及日期见JSONL，本包审计保留实际批次。

### QX-P-001630 · Lonely Runner 猜想（一般开放；k≤15 有限情形关闭中）

Allikvere v2覆盖总跑者14和15人的固定人数情形；原卡k表示相对另k人，因此应写k≤14（总人数≤15），不是k≤15。

- **14/15个总跑者｜部分进展：** 2609.02604v2 Theorem1.1声明对这些人数的全部速度组成立，有限证书由约化覆盖无限速度；本轮未重跑。
- **参数与证明范围｜题面有误：** k个非零相对速度对应k+1跑者；修正差一。也不应降格为仅若干有限速度样本的实验。

**直接证据与定位：**

- [Allikvere, Fourteen and fifteen lonely runners](https://arxiv.org/abs/2609.02604v2)；2026-09-24；p1式(1)、Theorem1.1；§5–6证书和验证。原文LRC(k)是k个非零速度、总k+1跑者。v2比v1新增15人；涉及计算证书，未独立重跑。 核查层级：全文；他人报告计算验证；本轮未运行证明/证书。
- [15人证书Zenodo存档](https://zenodo.org/records/22667683)；论文§6及参考文献所指数据集。本轮web直接访问失败；仅核论文中的存档指向，不声称取得或验证全部数据。 核查层级：入口不可达；不适用；未执行外部代码或形式化重跑。

**实际检索路径：**

- system1_search_query：`"lonely runner" "LRC(14)" "fifteen"`。
- system2_search_query：`"Lonely Runner Conjecture" "fourteen" "fifteen" Allikvere`。

随后核对上述原稿/作者页；GitHub、公开AI/社区和库内查重的逐题词及日期见JSONL，本包审计保留实际批次。

**待复核：** 深查时复核§3有限约化与§5–6完整证书；作者提及第三方验证不等于本轮独立验证。。

### QX-P-001631 · Conway Thrackle 猜想

已核Simon v2的4(n−1)/3上界；另Tomar有独立同界计算/Lean声明，形式化接受五条thrackle性质为假设，不能当原猜想m≤n的全证明。

- **2026上界｜部分进展：** Simon2610.31589v2 Theorem1：n≥4时m≤floor(4(n−1)/3)。Tomar给同界及部分形式化路径。
- **图画定义｜题面有误：** “不允许三条边交于同一点”须限定边内部交叉；允许多条边共用同一顶点，否则错误限制顶点度数。

**直接证据与定位：**

- [D.G.Simon, Conway’s thrackle conjecture: a new upper bound of4n/3](https://arxiv.org/abs/2610.31589v2)；2026-11-04；Theorem1 p2；研究方法p5。完整阅读关键定理与计算说明；上界部分进展，无m≤n结论。 核查层级：全文；论文报告计算辅助证明；本轮未重跑。
- [Tomar, A thrackle on n vertices has fewer than4n/3 edges](https://www.mefyi.com/papers/thrackle-bound/)；Formal statement and axioms：Thrackle78.thrackle_bound_4_3_full；Details/Section6。Lean定理显式带ThrackleAxioms和NoSpikeFaces等条件；作者说五条几何性质作为假设，并用编译计算核23个事实。不是全部几何基础已在内核重建。 核查层级：全文页面，仓库v5入口已定位；他人声称已形式化验证；已核页面定理的额外假设，未重跑。

  版本定位：作者首页GitHub指v5，但Formal statement的Source实际指v4/lean/Thrackle78/Main.lean；不把不同tag代码视为已核一致。 v5固定提交为 `a042c1b65730b4a2fa5fa3dfed270d8cb41a0be3`；定理路径为 `lean/Thrackle78/Main.lean :: Thrackle78.thrackle_bound_4_3_full`。只读git ls-remote固定v5；页面陈述对照v4链接，未下载或运行整个仓库。


**实际检索路径：**

- system1_search_query：`"thrackle" "4(n-1)/3" Simon proof GitHub`。
- system2_search_query：`"Conway thrackle conjecture" Simon 2026 upper bound`。

随后核对上述原稿/作者页；GitHub、公开AI/社区和库内查重的逐题词及日期见JSONL，本包审计保留实际批次。

### QX-P-001632 · Graceful Tree 猜想（Gnang 声称证明未获接受）

Gnang v3的全证明声明仍不能接纳；新增针对其Composition Lemma Step5的形式化缺口报告。另一篇2409.01981已明确因相关Lemma4.3错误撤回，不能把该撤回本身等同于原猜想被反驳。

- **Gnang2202.03178v3完整声明｜完整证明/反例声明待核：** KRR仓库明确针对v3的Step5反证步骤指出缺口；本轮静态阅读，未重跑Lean。
- **渐近gracesize｜部分进展：** Letzter–Pokrovskiy–Williams v2：每个充分大的n顶点树可实现至少(1−ε)n种边差，仍非全部n−1差值。

**直接证据与定位：**

- [Gnang, Graceful Tree全证明声明](https://arxiv.org/abs/2202.03178)；v3 (2025-01-31)。完整声明来源保留；未作全证明认可。 核查层级：摘要/版本信息；不适用；未执行外部代码或形式化重跑。
- [Chalise–Clark–Gnang, arXiv2409.01981](https://arxiv.org/abs/2409.01981)；v3 (2026-09-01)撤回注。撤回理由是Lemma4.3 Composition Lemma证明错误，关联2202.03178v2；单凭撤回不自动判Gnang v3全部错误。 核查层级：全文摘要页；不适用；未执行外部代码或形式化重跑。
- [walidelkersh/KRR对Gnang v3 Step5的检查](https://github.com/walidelkersh/KRR/tree/bac4b07d52ef5e81ca1f2e84b522a07dfa202110)；README Scope；KRR/Step5FlawWitness.lean，partB_conclusion_false_canonical。作者明确只指出一条证明的缺口，不主张树猜想或Composition Lemma本身为假。读取固定提交README及关键Lean文件，未审核全部依赖。 核查层级：代码已取得；已取得代码未重跑；命题对应的是证明步骤缺口，不是原猜想反例。
- [Letzter–Pokrovskiy–Williams, On the gracesize of trees](https://arxiv.org/abs/2511.11331v2)；2026-07-31；摘要及Theorem1.2。渐近放宽结果，保留ε和充分大n。 核查层级：全文；不适用；未执行外部代码或形式化重跑。

**实际检索路径：**

- system1_search_query：`"graceful" "gs(T)" "2026" Letzter Pokrovskiy Williams`。
- system2_search_query：`"Graceful Tree Conjecture" Gnang Letzter Pokrovskiy Williams 2026`。

随后核对上述原稿/作者页；GitHub、公开AI/社区和库内查重的逐题词及日期见JSONL，本包审计保留实际批次。

**待复核：** 如要验证KRR报告，须复核原v3符号对应及全部Lean依赖，并在隔离环境重跑；本轮未做。。

### QX-P-001633 · Hadwiger–Nelson 平面色数（5≤χ≤7 未变）

旧卡“5≤χ≤7未变”漏掉公开的无适当5染色证明及Lean声明；已取得固定提交论文与关键文件，命题覆盖无可测性限制的全体染色，但本轮未重跑，因此记录下界6的完整证明声明待核；若该声明成立，精确值仍只限于6与7，尚未由该结果决定。

- **χ(R²)的精确值｜部分进展：** 若公开≥6结果成立，精确值仍在6与7之间；该结果本身不决定精确值。
- **任意5染色必有单位距离同色对｜完整证明/反例声明待核：** OpenAI result158论文Theorem1.1与Five.lean顶层定理对应全部c:ℂ→Fin5，无可测性假设。已静态核对定义与直接导入，未独立运行内核或审完传递依赖。
- **旧卡来源状态｜题面有误：** 应补2026-09-23公开下界6声明，不继续声称没有相关新成果；不能把map-type7色变体混为一般平面定理。

**直接证据与定位：**

- [OpenAI, The Euclidean plane is not five-colorable](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/paper.pdf)；Theorem1.1 p2；Theorems1.3–1.4为全染色到弱可测染色的桥及排除。取得完整论文；不是只证明可测染色版本。χ精确值仍可能6或7。 核查层级：全文PDF；不适用；未执行外部代码或形式化重跑。
- [OpenAI Lean result158关键文件](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Geometry/PlaneColoring/Five.lean)；OAI.EuclideanFiveColor.no_proper_five_coloring；Coloring.lean ProperColoring定义。顶层¬∃c:ℂ→Fin5,ProperColoring5c；Coloring.lean定义单位距离不同色。Five导入BorelTransfer、Mesh；后者进一步依赖Ergodicity/FullApproximation等，未完成全依赖检查。 核查层级：Five、Coloring、BorelTransfer、Mesh完整文件已取得并检查关键位置；已核定理对应、未重跑；全传递依赖/公理审计未完成。
- [Formal Conjectures Erdős508](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/508.lean)；条目标签及所链OpenAI固定提交。作为发现与交叉指向入口；题目库标签不能替代核验证明。 核查层级：源码页面；不适用；未执行外部代码或形式化重跑。

**实际检索路径：**

- system1_search_query：`"Hadwiger Nelson" chromatic plane 2026 5 7`。
- system2_search_query：`Hadwiger Nelson plane unit distance arbitrary coloring five Lean Five.lean`。

随后核对上述原稿/作者页；GitHub、公开AI/社区和库内查重的逐题词及日期见JSONL，本包审计保留实际批次。

**待复核：** 优先独立重跑固定提交158，输出公理依赖并核BorelTransfer和Mesh的传递假设。；不要把其他提交的第三方审计当作本次固定提交已通过。。
