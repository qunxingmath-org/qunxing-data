# QX-NEW-06：突破点、检索路径与复核清单

**检查日期：2026-11-26（Asia/Shanghai）。范围：任务文件中的100题。** 全部题号、`card_rev`、`batch_id`按原包保留；未修改线上题卡、合并题目或发帖。本轮为初查，不是100题的完整证明审计。

## 交付与阅读方法

- `QX-NEW-06_逐题回传.jsonl`：100行，按任务原顺序；逐子问给出数学结论，分别记录证据强度、读取范围、形式化状态、查询、查重、修卡建议和待核事项。
- 本清单：只列影响题面、状态、出处或查重的变化，并给旧卡→变化→来源定位→量词范围→实际检索词→待复核点。旧结论的重新补证不当作新定理。
- 压缩包中的 `审计附件/QX-NEW-06_实际检索审计.jsonl`：工具调用参数、返回来源链接和本地复核记录；使用 `trace_id`与逐题记录对应。合并搜索的返回清单不逐项强归因给某一条检索词。
- 形式化运行次数为0。取得的代码、他人测试输出、定理对应和完整依赖审计分开；自写的有限整数/图枚举核算仅支持其明确的有限范围。

## 验收摘要

|项目|本轮结果|
|---|---|
|逐题记录及版本匹配|100/100|
|两组学术查询、代码、公开AI/社区、库内索引路线|100/100；具体入口以每题记录为准|
|逐题查询、读取及本地复核记录|1017条|
|证据条目|222条，强度和读取程度逐条说明|
|指定查重对子|25/25；23对相关但不等价，2对待定|
|新增查重关系|001986↔002015同题；001979↔001024特例/强化，后者实时正文与索引版本对应尚待复核|
|线上写入、发帖、合并|0|
|独立形式化重跑|0|

三个指定原帖未完整恢复：001975（MSE255834/MO104889）、001984（MSE4753404/MO452567）、001989（MSE4075536）。001975另取得已刊非表示证明及原作者交叉说明；001984、001989不从旧备注擅自补全原题。001982取得搜索返回的原题正文，直接入口有失败记录。其余访问失败、仅摘要和不可用的新稿也逐条记录；没有将这些情况写作零命中。

## 优先处理的变化

|题号|旧卡需改变的内容|本轮处理|
|---|---|---|
|001985|把`x+z=2y`漏成乘法，并据此排除无解|恢复加号；明确样例和无穷Pell构造；全体解的穷尽性未证。|
|002016|把A126776立方体对称轨道数当欧氏全等类数|五维已刊作者材料有全等而非同一立方体轨道的单纯形；撤回错误序列识别，未计算正确五、六维确值。|
|002033|TOP与smooth两套分类被写成冲突|按Hillman Thm5.2及后页光滑说明，原题光滑清单只有S³、S³/Q₈；S³/I*只属于TOP变体。|
|002031|三维只知数值非消失、线性有效性未解|Müller2025 Cor.B已给三维实际非消失；一般维数和更强半正定假设另列。|
|001976|把C¹存在性列残余开放|公开连续构造可验证；同一支撑区间论证给C∞推广，短证明附下，标本轮推论。|
|001979|指定七元格仍未解决|取得2026 L₇群区间完整稿与固定提交GAP复算材料；本轮未跑，保留声明待核；Lean206不验证该构造或普遍群区间结论。|
|002018、002051|旧卡仍以早期未解评论为依据|同步2026自由群因子同构、Thompson F非amenability的完整声明；核作者原稿和代码端点，未独立重跑或审完整依赖闭包。|
|002059|无理论上界、无AI进展|补已刊/作者幂次界及2026更强幂次界声明；幂界并不推出原O(log P)。|
|002069|只记录姐妹初值已解决|最新版通用面积引理能推出原初值永不共线；完整缺失面积谱另保留。|
|002071|新出现完整否定证明|定位viXra§3.3无依据引入`x=z−x`的缺口；不能据此关题。Zenodo新版本是部分约束。|
|002007|残数上界仅需RH/单性；1/ζ为整函数|补最新v10推论的额外负性条件，删除错误整函数描述。|
|002046、002049|新完整稿的精确适用范围待补|取得原稿定理；分别核对对称多项式特化和有向/无向路径计数，仍保留预印本声明待核层级。|

## 查重汇总

指定对子中的待定项为002036↔002169、002036↔002177：已读所给现版参考卡，但其完整公式/量词缺失，不能完成严格等价性判断。其余23个指定对子相关但不等价，不建议合并。

新增同题001986↔002015已读双方现版正文及Sawin同一原答，只报告不合并。新增001979↔001024为小格问题与普遍有限格问题的特例/强化关系；001024实时仓库正文已读，包内索引版本是否对应该正文尚未确认。完整双方版本、理由及来源均在JSONL的`duplicates`中。

下列逐项结论均作用于写明的子问。辅助识别被反驳、邻题反例或特殊情形已证，不代表整个原题相应改变状态。


## 第1部分：分题证据与复核事项


检查日期：2026-11-26（Asia/Shanghai）。本节仅列影响题面、状态、出处或查重的变化；逐题实际查询和读取程度见逐题 JSONL。完整声明与本轮验证程度分开，不把未检出当开放证明。

#### QX-P-001985 · xz=2y 型方程组（恒空解，排除） · P0

**旧卡 → 变化：** 旧卡把 x+z 误写为 xz，继而把原题排除为无解；原帖标题和正文都含加号。 → 必须撤销对原题的‘恒空解’排除。样例(2,4,12;3,5,7)及 Pell 无限族满足原式；族的穷尽性本轮未找到可验证证明。

**原题范围：** 正整数 0<a<b<c，ab+1=x²、ac+1=y²、bc+1=z²，且 x+z=2y；问是否所有解都来自给定 Pell 递推族。

**直接证据与定位：**

- [MSE4481833 原题](https://math.stackexchange.com/questions/4481833/positive-integer-solutions-of-ab1-x2-ac1-y2-bc1-z2-xz-2y)；标题、方程第四式与 Somos 回答的两个方向。社区原题/构造；全文已读。URL slug 吞掉加号，正文为 x+z=2y，不能从slug恢复乘法。
- [MO88220 相邻等差三元组问题](https://mathoverflow.net/questions/88220/special-arithmetic-progressions-involving-perfect-squares/88263)；主问与三元组评论。社区邻题；全文相关段已读。该帖要求 a,b,c 自身等差；本题是三个平方根 x,y,z 等差，不可套用其 Pell 穷尽性。

**实际检索词：** 学术名称 `"ab+1" "ac+1" "x+z" "2y"`；公式/特征 `Diophantine triples square roots arithmetic progression Pell Somos`；代码 `site:github.com "x+z=2y" Diophantine`；公开AI/社区 `"x+z" "2y" "Diophantine" (site:mathoverflow.net OR site:zenodo.org OR "EulerSolve")`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**本轮可复核核算：** 原式最后一项是 $x+z=2y$。取 $(a,b,c;x,y,z)=(2,4,12;3,5,7)$，得到 $ab+1=9$、$ac+1=25$、$bc+1=49$ 且 $3+7=2\cdot5$。

一般取 $x^2-2a^2=1$、$b=2a$、$c=3a+2x$、$y=x+a$、$z=x+2a$，则 $ac+1=(x+a)^2$、$bc+1=(x+2a)^2$、$x+z=2y$。由 $(x,a)=(3,2)$ 以及递推 $(x,a)\mapsto(3x+4a,2x+3a)$ 得到无穷族。以上是代数构造；另用自写 Python 的精确整数运算核对前10项，四式均成立。没有枚举全体解，也没有验证所有解都属于此族。

**待复核：** P0 恢复加号与原题的族穷尽性问句；撤销 solved/excluded 标记，仅保留已验构造方向。

#### QX-P-001976 · 自含积分方程非常数解 · P0

**旧卡 → 变化：** 人话版换成了 f(x)=∫_0^x f(x−f(t))dt；零函数也不满足严格正条件。旧记录把 C1 存在性列为残余开放，需修正。 → 原帖 Simd 的连续构造可直接验算。相同支撑间隔论证允许取零均值光滑小扰动，因此 C∞ 非常数解亦存在；这是本轮对旧构造的明确推论，不是新文献声明。

**原题范围：** 存在非常数、全局连续、严格正的 f:R→(0,∞)，使 f(x)=∫_(x−f(x))^(x+f(x)) f(t)dt 吗。

**直接证据与定位：**

- [原题与 Simd 评论](https://math.stackexchange.com/questions/5142615/existence-of-non-constant-solutions-to-the-self-bounding-integral-equation-fx?r=31)；原文 Problem；Simd 2026-07-03 18:16 评论。社区构造；全文及构造已读。周期局部正弦构造已按原式检查。

**实际检索词：** 学术名称 `self bounding integral equation nonconstant solutions Simd`；公式/特征 `"f(x)" "x-f(x)" "x+f(x)" integral periodic`；代码 `site:github.com "self-bounding" integral Lean`；公开AI/社区 `"self-bounding integral" (site:mathoverflow.net OR site:zenodo.org OR "aiXiv" OR "EulerSolve")`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**本轮短证明（包括光滑推广）：** 令 $g$ 为1周期函数，在每周期仅支撑于 $[1/8,3/8]$，满足 $\int_0^1g=0$、$\|g\|_\infty\le1/16$，置 $f=1/2+g$。若 $g(x)=0$，积分窗长1，故窗内 $g$ 的积分为0。若 $g(x)\ne0$，$x$ 模1落在支撑内；未扰动端点 $x\pm1/2$ 模1在 $[5/8,7/8]$，加入至多 $1/16$ 的端点扰动后仍在 $[9/16,15/16]$。该区域与 $g$ 的支撑不交，移动端点不改变 $g$ 的积分，因此窗内 $g$ 的积分仍为0。常数部分的积分为 $(1/2)\cdot2f(x)=f(x)$，且 $f\ge7/16>0$。

取非零光滑函数 $h$ 紧支撑于 $(1/8,3/8)$，取非零且足够小的 $\varepsilon$，令 $g=\varepsilon h'$ 并周期延拓至上述幅度，得到非常数 $C^\infty$ 解。此光滑推广是本轮从已公开构造作出的明确推论，未标作新论文或Lean结果；完整解分类不在本题初查范围。

**待复核：** 人工复核回传中的短证明并修正旧残余 C1 标签；完整分类不在原问验收范围。

#### QX-P-001979 · n 元格实现为有限群子群格？ · P0

**旧卡 → 变化：** 人话版把子群区间换成整个子群格；Palfy–Pudlak 是普遍量词等价，不能直接逐格互推。 → 发现指定例 L7 的 2026 完整群表示稿和 DeMeo 作者仓库复算，旧‘此例未解决’已过时。广义否定/不可判定论文另有声明，但公开 Lean 206 只覆盖图刻画；不据此判整题全解。

**原题范围：** 小有限格（特别七/八元及指定七元例）能否作为有限群的完整子群区间 [H,G]；与有限代数的整个同余格表示须分开。

**直接证据与定位：**

- [MO85724 原题](https://mathoverflow.net/questions/85724/given-a-lattice-l-with-n-elements-are-there-finite-groups-h-g-such-that-l-c)；主问及更正评论，指定七元格图。社区原题；全文已读。完整区间 [H,G]，不是整个子群格。
- [Tian, The exceptional seven-element lattice as a subgroup interval in PSL2(64)](https://www.researchgate.net/publication/414130064_THE_EXCEPTIONAL_SEVEN-ELEMENT_LATTICE_AS_A_SUBGROUP_INTERVAL_IN_PSL_2_64)；稿内日期2026-08-28；上传2026-09-10；Theorem1.1/1.2、Corollary1.3，pp.1–2；§2。预印本；作者上传全文已读相关定理及证明结构。L7 指定覆盖关系被明确实现；七元同余格结论与所有群区间问题区分。
- [DeMeo 仓库的 L10/L7 复核与 GAP 代码](https://github.com/UniversalAlgebra/fin-lat-rep-gap/pull/2)；merge e891783487eaaea9efe3c3e57f9c848cafba1a58；docs/L10-is-representable.md；L10/verifyPSL264.g、latticeTests.g、results/verifyPSL264.txt。作者仓库/他人计算复核；代码、输出、报告及合并元数据已取得。他人环境 GAP4.15.1/TomLib1.2.11；报告称复算通过并披露 Claude 辅助。本轮未运行，非形式化独立通过。
- [OpenAI Lean 206 范围声明](https://github.com/openai/math/blob/main/lean/docs/206.md)；Scope；ComparatorChallenges/FiniteCongruenceGraph.lean。作者仓库；范围文档与定理页已读。明确只证明 colored-graph criterion，不包括 undecidability 和 subgroup-interval conclusions。 同样不验证本题指定L7群区间构造。
- [OpenAI 有限格稿固定版本](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Finite-Congruence-Lattices-Characterization-and-Undecidability-September-24-2026/paper.pdf)；固定提交的论文入口；主结论由作者 lean/docs 交叉定位。预印本声明；作者PDF文件入口已确认，未取得可读原PDF全文。第三方TeX转录仅作为导航，不以其全文作为已核原稿；广义负解仍须取回原PDF并核正文。

**实际检索词：** 学术名称 `DeMeo seven element lattice subgroup interval finite group representation`；公式/特征 `finite lattice representation seven eight elements Aschbacher Palfy Pudlak`；代码 `site:github.com DeMeo subgroup interval lattice GAP Lean`；公开AI/社区 `"finite lattice representation" (site:zenodo.org OR "aiXiv" OR site:mathoverflow.net)`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**查重：** `QX-P-001979|QX-P-001024`，双方版本 `22150e30c616758a` / `ec089c286914f879`，结论 **特例/强化**。1979 的小规模格及指定 L7 群区间问题是1024所有有限格量词下的特例；不得以有限代数整个同余格的逐例表示替代群区间表示。

**待复核：** 先专家复核 Tian 定理和本轮未跑的 GAP；另行取回广义稿原文审范围，禁止把图刻画 Lean 证书覆盖到未形式化结论。

#### QX-P-001971 · 开集≅闭包内部刻划 · P0

**旧卡 → 变化：** 同胚和作为 X 的子集相等是不同子问；半正则空间不能定义为每个开集都正则开。 → 第二子问在 X=R 已有显式反例，旧卡的 R 情形判断需纠正；一般条件刻画未找到全解。

**原题范围：** 对开 U⊂X，何种条件保证 U 同胚于 int(cl U)；又在何种条件下同胚能推出二者相等。X 可假定局部紧可度量。

**直接证据与定位：**

- [原题与 Govc 反例评论](https://math.stackexchange.com/questions/1791701/when-is-an-open-set-homeomorphic-to-the-interior-of-its-closure?r=31)；两个问句；Dejan Govc 2016-05-22 评论。社区原题/反例；全文及反例已读。本轮核对区间分量可一一线性配对；只反驳上述相等性子问。

**实际检索词：** 学术名称 `open set homeomorphic interior closure regular open`；公式/特征 `locally compact metrizable open U homeomorphic int closure U counterexample`；代码 `site:github.com regular open homeomorphic closure Lean`；公开AI/社区 `"homeomorphic" "interior" "closure" (site:mathoverflow.net OR site:zenodo.org OR "ProofForum")`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**明确反例：** 取 $U=\bigcup_{k\in\mathbb Z}((4k,4k+1)\cup(4k+1,4k+2))$，则 $\operatorname{int}\overline U=\bigcup_{k\in\mathbb Z}(4k,4k+2)$，二者不同，但都是可数无穷个互不相交开区间的拓扑和。把第一类区间上的点映为 $2x$，第二类映为 $2x+2$，即得到两者间同胚。它否定“同胚必相等”，不完成一般空间/开集的分类。

**待复核：** 保留一般条件刻画；将 R 情形反例正式写入回传，不能因第二问否定而删除第一问。

#### QX-P-001974 · ℓ¹ 等距点集 · P0

**旧卡 → 变化：** 不是无限维 l1 的另问；坐标轴上的四点是 l1 等距构型，普通轴对齐正方形的顶点不是。 → 具体三、四维子问由旧文献已知最大 6、8 排除；一般 d 的 2d 猜想仍未取得全解。旧卡把 p=1 的 O(d log d) 称为 2026 新界不准确，2020 原稿已归于 Alon–Pudlak。

**原题范围：** 固定有限维 l1 度量，最多能有多少两两等距点；原帖具体问 R³ 能否放 8 点、R⁴ 能否放 16 点，并问 ±e_i/2 的 2d 构型是否最优。

**直接证据与定位：**

- [原题 MSE 1341076](https://math.stackexchange.com/questions/1341076/point-set-where-each-point-has-unity-distance-to-all-other-points-l-1-metric?noredirect=1)；正文具体 8/16 点问句。社区原题；全文已读。明确有限维和 l1 metric。
- [Chen–Gui–Tang–Xiong, Few distance sets](https://math.mit.edu/research/highschool/primes/materials/2020/Chen-Gui-Tang-Xiong.pdf)；印刷 p.2 §1.3，Conjecture 1 后；p.3 上界讨论。作者研究稿；全文相关段已读。2020 稿即记 p=1 的 O(n log n) 为 Alon–Pudlak 旧界，并引 BCL98/KLS00 的 d=3,4。
- [Ge–Xu–Zhou, Kusner's conjecture: Exact values and linear bounds](https://arxiv.org/abs/2606.03987)；v1，2026-06-02，摘要。预印本；官方摘要及版本表已读。2≤p≤4 等区间的新精确值不解决 p=1 的精确 2d。
- [Xiong, Kusner's conjecture is false for p>4](https://arxiv.org/abs/2609.14794)；检索题名/摘要；abs/html/pdf 多次不可达。预印本线索；仅摘要；全文入口不可达。p>4 非 p=1。旧卡关于 GPT-6 Astra 的归属本轮未取得原稿核实，保留为旧线索。

**实际检索词：** 学术名称 `Kusner conjecture l1 equilateral sets Ge Xu Zhou 2606.03987`；公式/特征 `Xiong 2609.14794 equilateral sets l_p counterexample p=1`；代码 `site:github.com Kusner equilateral l1 Lean`；公开AI/社区 `"Kusner" (site:zenodo.org OR "aiXiv" OR "EulerSolve" OR site:uq.stanford.edu)`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**查重：** `QX-P-001974|QX-P-002433`，双方版本 `1373906686a7095d` / `598219f36b33f8d5`，结论 **相关但不等价**。1974 固定 ℓ¹ 范数，问最大等距集是否为 2d；2433 量化所有六维实赋范空间，问至少七个等距点。上界/下界、固定范数/全部范数均不同。

**待复核：** 取回 Xiong 全文核 AI 声明和版本；若需升级低维证据，打开 BCL98/KLS00 原刊。

#### QX-P-001983 · 多米诺唯一可铺判定算法 · P0

**旧卡 → 变化：** 不是唯一铺砌是否可判定这一宽问；按面积 n 的线性算法已是背景，所求是周长复杂度。 → Pak–Sheffer–Tassy Theorem1.2 只给 tileability；Theorem1.3 给极大铺砌的点查询。它们不直接宣布唯一性判定达到原复杂度。

**原题范围：** 以边界/周长 p 为输入，能否在 O(p log p) 或更好时间判定单连通格区域的多米诺铺砌唯一性。

**直接证据与定位：**

- [MSE4940528 原题](https://math.stackexchange.com/questions/4940528/what-is-the-current-best-algorithm-to-find-if-a-simply-connected-region-is-uniqu)；最后的 O(p log p) 问句与 Fournier 背景。社区原题；全文已读。输入参数是周长 p，而 n 是面积。
- [Pak–Sheffer–Tassy, Fast Domino Tileability](https://www.math.ucla.edu/~pak/papers/tileability.pdf)；pp.1–2 Theorems1.2/1.3；§1 输入编码。已刊论文作者稿；全文关键定理已读。O(p log p) 决定可铺；极大铺砌点查询 O(log²p)。未见原复杂度唯一性定理。
- [Caltech 原作者存档](https://authors.library.caltech.edu/records/jkye5-bab17)；期刊元数据：DCG56(2016),377–394，DOI10.1007/s00454-016-9807-1。机构原稿存档；元数据已读。确认论文版本与刊物，保存的附件是提交稿v1。

**实际检索词：** 学术名称 `unique domino tiling perimeter algorithm O(p log p) Fournier Pak Sheffer Tassy`；公式/特征 `uniquely tileable simply connected domino region fastest algorithm boundary complexity`；代码 `site:github.com domino unique tiling perimeter algorithm`；公开AI/社区 `"unique tiling" "domino" (site:mathoverflow.net OR site:zenodo.org OR "aiXiv" OR "EulerSolve")`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**待复核：** 查唯一性检测是否能利用压缩表示，不把必须枚举面积 n 的算法说成按周长近线性。

#### QX-P-001986 · 稠密代数点⇒Q̄ 定义（=C402 同题；MO#428384 Sawin 已答） · P1

**旧卡 → 变化：** 是固定坐标下的定义域下降，不是仅存在某个抽象同构模型；不可把旧无回答标记压过交叉帖证明。 → 已重新读到 Sawin 完整基展开证明，结论更一般，对任意域扩张成立。与2015同源同题，双方当前正文已复核。

**原题范围：** 在固定仿射嵌入下，复代数集含 Zariski 稠密的代数坐标点，是否能由 Qbar 系数方程定义；一般化为域扩张 K/F。

**直接证据与定位：**

- [MO428384 / Sawin 回答428394](https://mathoverflow.net/questions/428384/is-a-complex-algebraic-set-with-a-zariski-dense-subset-of-algebraic-points-alrea/428394)；Will Sawin 2022-08-12 回答。社区证明；完整证明已读。一般域扩张；本轮核论证与原题，无形式化重跑。
- [本包2015当前正文](package:任务.jsonl#QX-P-002015)；card_rev 0f78ce001d7fc0e8；题面与来源。包内指定任务卡对照；全文已读。与1986同一固定坐标定义域下降问题。

**实际检索词：** 学术名称 `Zariski dense algebraic points defined over field Sawin`；公式/特征 `Milne algebraic geometry Proposition 16.8 field of definition dense rational points`；代码 `site:github.com Zariski dense field definition Lean`；公开AI/社区 `"Zariski dense" "algebraic points" (site:zenodo.org OR "aiXiv" OR site:mathoverflow.net)`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**查重：** `QX-P-001986|QX-P-002015`，双方版本 `00b8701da1d461f7` / `0f78ce001d7fc0e8`，结论 **同题**。两卡当前正文均为固定坐标中代数点 Zariski 稠密推出在代数数域上定义，追溯到同一MO428384及Sawin回答；一般域下降为同一证明的强化。

**待复核：** 只报告同题关系，不合并；去除与已证结论冲突的人话版疑问式暗示。

#### QX-P-001978 · 下半连续像 Borel 性（MO#494998 已答） · P1

**旧卡 → 变化：** 原问是整个紧定义域的像，不能换成任意 Borel 子集之像。 → 已读 MSE 的已解决更新和 MO Gro-Tsen 完整反例；旧卡已解结论可保留，但应明确否定回答的对象。

**原题范围：** 紧伪度量空间 X 上的下半连续实函数 f，整个像 f(X) 是否一定 Borel。

**直接证据与定位：**

- [MSE 5066507 原题](https://math.stackexchange.com/questions/5066507/are-lower-semi-continuous-images-of-compact-sets-borel)；原问与2025-05-29链接 MO 的解决更新。社区原题；全文已读。确认对象为整个像 f(X)。
- [MO 494998 Gro-Tsen 反例](https://mathoverflow.net/questions/494998/are-lower-semi-continuous-images-of-compact-sets-borel?noredirect=1)；Gro-Tsen 2025-05-28 回答。社区证明；完整证明已读。从非Borel解析集的连续参数化作下半连续延拓；只添加可数像值不使其变成Borel。未形式化重跑。

**实际检索词：** 学术名称 `lower semicontinuous image compact metric non Borel Gro Tsen`；公式/特征 `Baire class one graph G delta image analytic non Borel compact interval`；代码 `site:github.com lower semicontinuous image Borel Lean`；公开AI/社区 `"lower semicontinuous" "Borel" (site:zenodo.org OR "aiXiv" OR "EulerSolve" OR site:mathoverflow.net)`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**待复核：** 将反例定位写入卡片；无需因 MSE 回答数为0重新标开放。

#### QX-P-001968 · 图的子类偏序自同构自由？ · P1

**旧卡 → 变化：** 不是任意图类的集合包含偏序；顶点数固定，元素是图同构类。 → 未找到所有 n≥5 的证明或反例。新增直接同题的 UQ/GPT-5 公开回答，但页面要求人工验证，不能作为已解或确认开放的依据。

**原题范围：** P_n 为 n 个顶点的无标号图同构类，按子图关系排序；问每个 n≥5 时 Aut(P_n) 是否只有恒等。

**直接证据与定位：**

- [原题 MO 153208](https://mathoverflow.net/questions/153208/is-the-poset-of-graphs-automorphism-free)；问题正文 P_n 定义、n≥5 问句及小 n 讨论。社区原题；全文已读。固定 n 的无标号图子图偏序。
- [UQ Project 的 GPT-5 同题回答](https://uq.stanford.edu/answer/9a46a339-0962-4103-8640-02a2e477483a)；2025-09-02；Model Answer；Human Verification。公开 AI 回答；全文已读。标为 UQ Validated，同时 Needs Human Verification，0 人工评审；本轮只确认 AI 暴露与回答范围，不接受其开放性断言或邻题推论为证明。

**实际检索词：** 学术名称 `poset isomorphism classes n vertex graphs automorphism rigid reconstruction`；公式/特征 `set edge reconstruction graph poset automorphism n vertices`；代码 `site:github.com graph poset rigidity reconstruction Lean`；公开AI/社区 `"poset of graphs" (site:uq.stanford.edu OR site:zenodo.org OR "aiXiv" OR "EulerSolve")`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**待复核：** 复核边删除集合与偏序自同构之间的逻辑；UQ 标签不能替代专家证明。

#### QX-P-001966 · 素数两完美幂表示个数 · P1

**旧卡 → 变化：** 人话版把表示数问题泛化成研究方法，并未保留无界性和满射性两个子问。 → 两个子问均未找到可验证全解。新检出的 arXiv:2509.11558 已撤回，且其目标整数不要求为素数，不能用于本题。

**原题范围：** 对素数 p，以原文的完全幂约定计数 p=a+b、0<a<b 的表示数 f(p)；问 f(p) 是否无界，以及若无界是否取遍所有自然数。

**直接证据与定位：**

- [原题 MSE 2767018](https://math.stackexchange.com/questions/2767018/can-a-prime-have-arbitary-many-representations-as-a-sum-of-two-perfect-powers)；问题正文的 f(p)、两个问句。社区原题；全文已读。确认量词和计数对象；原作者列举的高计数样本未独立枚举。
- [Aggarwal, On integers with many representations as the sum of kth powers of primes](https://arxiv.org/abs/2509.11558v2)；arXiv v2，2025-09-16；Comments/Submission history。已撤回预印本；摘要及撤回记录已读。官方页面明确为鸽巢论证错误而撤回；目标为一般 n，原题目标为素数 p。

**实际检索词：** 学术名称 `prime sum two perfect powers number representations unbounded`；公式/特征 `primes a^m+b^n number representations arbitrary many powers`；代码 `site:github.com prime perfect powers representations Lean`；公开AI/社区 `"prime" "perfect powers" (site:mathoverflow.net OR site:zenodo.org OR "aiXiv" OR "EulerSolve")`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**待复核：** 寻找针对素数目标且允许不同完全幂的无界性或逐值构造。

#### QX-P-001967 · Ω 常数素数前缀无穷性 · P1

**旧卡 → 变化：** Ω 是停机概率，不是 Lambert W 的常数；一般正规数、Martin-Löf 随机数和某台机器的 Ω 不可混同。 → 原帖没有给出全解。发现十进制正规数全部前缀合数的 Lean 仓库，但它不涉及二进制 Chaitin Ω，不能反驳原题。

**原题范围：** Chaitin Ω 的二进制前缀整数 floor(2^n Ω) 是否有无穷多个为素数；须保留通用前缀机及其 Ω 的约定。

**直接证据与定位：**

- [原题 MSE 2285471](https://math.stackexchange.com/questions/2285471/does-chaitins-constant-have-infinitely-many-prime-prefixes)；问题正文及机器依赖性的评论。社区原题；全文已读。原问是 Chaitin Ω 的二进制前缀。
- [Normal Composite Prefixes 作者仓库](https://github.com/slavanaprienko/normal-composite-prefixes)；README Result；lean/NormalCompositePrefixes/Main.lean 中 exists_normal_with_no_prime_prefix 的展示。作者仓库；README 和展示的定理已读；未拉取完整依赖。只声称存在十进制正规实数使所有十进制前缀非素数；不能升级为 Ω 的反例。未固定此邻题代码版本，未运行。

**实际检索词：** 学术名称 `Chaitin Omega infinitely many prime binary prefixes`；公式/特征 `Martin Lof random binary sequences prime prefixes floor 2^n`；代码 `site:github.com Chaitin prime prefixes Lean`；公开AI/社区 `"prime prefixes" (site:mathoverflow.net OR site:zenodo.org OR "aiXiv" OR "EulerSolve")`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**待复核：** 核 Ω 的量词后查随机性与素数前缀的精确连接；邻题代码无须代替原题验收。

#### QX-P-001975 · 4x²+2xy+7y²−z³ 表示集 · P1

**旧卡 → 变化：** z 可取任意整数时 +z³ 和 −z³ 给同一表示集，不构成数学勘误；正定并不表示沿每个坐标绝对值逐项单调。 → 重新定位 AMM 11539 已刊非表示证明，印刷 pp.884–885。它仅证明例外族不表示，未证明族外全部可表示；原两帖未取回，改用作者2014交叉说明校准。

**原题范围：** 整数多项式 Q(x,y)−z³，Q=4x²+2xy+7y²，是否恰好漏掉指定 ±2m³、±32m³ 例外族；x,y,z∈Z。

**直接证据与定位：**

- [AMM Problem 11539 与 Chapman 解答](https://lupucezar.wordpress.com/wp-content/uploads/2010/04/amer-math-monthly-119-10-880.pdf)；印刷 pp.884–885；PDF索引5–6，Quadratic form plus a cube。已刊论文/原刊扫描；全文相关证明已读。明确 E 定义与单向不可表示结论。
- [Jagy 对问题族的原作者补充说明](https://mathoverflow.net/questions/12486/integers-not-represented-by-2-x2-x-y-3-y2-z3-z/13369)；问题正文 EDIT 9 March 2014，提及 Q−z³ 和11539。原作者社区说明；全文相关段已读。该帖主式不同；仅用其明确讨论 Q−z³ 的段落校准单向/双向。
- [指定原出处 MSE255834 / MO104889](https://math.stackexchange.com/questions/255834)；数字链接、问号参数和 StackPrinter 尝试。原题入口；原帖全文不可达。MO https://mathoverflow.net/questions/104889 同样未取回；不声称本轮读过九族恒等式原文。

**实际检索词：** 学术名称 `Jagy Chapman quadratic form plus a cube 11539 2012`；公式/特征 `"4x^2+2xy+7y^2" cube integers`；代码 `site:github.com Jagy quadratic cube 11539`；公开AI/社区 `"quadratic form" "cube" (site:mathoverflow.net OR site:zenodo.org OR "EulerSolve")`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**待复核：** 恢复指定双帖并核九族恒等式；族外可表示性继续初查，不把作者别式的采纳答案套回本式。

#### QX-P-001973 · 特征函数非带状域延拓（题面校准） · P0

**旧卡 → 变化：** 人话版若要求延拓域包含整条实轴便加入原点，改变问题；原帖用稳定分布解释这个区别。 → 关键变化是补回原点排除和具体域。检出的大量条带解析/指数矩结果不自动回答该非带状延拓问题。

**原题范围：** 求概率特征函数/Levy 特征指数在原点之外延拓到非带状复域（如扇形）的充分条件；原文允许实轴非零点附近，特意排除在 0 邻域全纯的要求。

**直接证据与定位：**

- [原题 MSE 1478352](https://math.stackexchange.com/questions/1478352/holomorphic-extensions-of-characteristic-functions)；问题正文的域、Levy 例子和稳定特征函数说明。社区原题；全文已读。原点与非原点解析的假设差异已核。

**实际检索词：** 学术名称 `holomorphic extension characteristic functions Levy processes non strip sectors`；公式/特征 `Cuppens Lukacs Norvidas analytic characteristic functions exponential moments sector`；代码 `site:github.com characteristic function analytic continuation Lean Levy`；公开AI/社区 `"holomorphic extensions of characteristic functions" (site:mathoverflow.net OR site:zenodo.org OR "aiXiv")`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**待复核：** 按指定扇形/去虚轴域重新核 Levy 测度充分条件；相邻文献仍需全文对应。

#### QX-P-001980 · 和集条件逼出 2 幂集 · P0

**旧卡 → 变化：** 不是小倍增和集基数是否为2的幂；核心是最短表示唯一性及两项间隔条件。 → MSE/MO 同源主问已核。作者局部检验到128与附加引理没有替代全称证明；未找到后续完整解。

**原题范围：** 正整数真子集 S={a1<a2<…} 满足 a_(n+1)≤2a_n、相邻差无界、每个正整数都有按加数最少且忽略排列唯一的 S 表示（允许重复），是否必为2的幂集。

**直接证据与定位：**

- [MSE5044047 原题](https://math.stackexchange.com/questions/5044047/set-s-satisfies-several-conditions-about-the-sumset-is-s-the-set-of-powers)；SSR 定义与三项条件。社区原题；全文已读。人话版的加法组合对象需恢复。
- [MO489584 交叉帖](https://mathoverflow.net/questions/489584/set-s-satisfies-several-conditions-about-the-sumset-is-s-the-set-of-powers?r=31)；2025-03-17 主问及3月评论。同源社区原题；全文已读。局部计算/引理为作者报告，本轮未复算；不将普通二进制唯一性作为逆向刻画证明。

**实际检索词：** 学术名称 `simplest sum representation unique powers of two JetfiRex`；公式/特征 `"unique" "sum representation" "unbounded" powers two`；代码 `site:github.com unique simplest sum powers two Lean`；公开AI/社区 `"simplest sum representation" (site:mathoverflow.net OR site:zenodo.org OR "aiXiv" OR "EulerSolve")`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**待复核：** 精确核 SSR 逆向刻画；普通 Sidon 集、二进制编码与 Euler169 均不是原题。

#### QX-P-001981 · Meas 有限表现对象（范畴论口径） · P0

**旧卡 → 变化：** finitely presentable 是范畴论性质，不是有限生成 sigma 代数、sigma 有限性或标准 Borel 性。 → 原帖给出有限离散的充分方向；一般逆向未找到可验证证明。相邻滤过余极限不交换有限极限的反例不能直接完成分类。

**原题范围：** 在可测空间及可测映射构成的 Meas 中，哪些对象 X 的 Hom(X,−) 保持滤过余极限；是否仅有限离散可测空间。

**直接证据与定位：**

- [MSE5024471 原题](https://math.stackexchange.com/questions/5024471/which-measurable-spaces-are-finitely-presentable)；Hom 保持滤过余极限的定义及有限离散方向。社区原题；全文已读。需保留 Meas 与范畴量词。
- [滤过余极限相邻帖](https://math.stackexchange.com/questions/5027218/filtered-colimits-of-measurable-spaces-do-not-commute-with-finite-limits)；2025 帖及回答摘要。社区邻题；检索摘要已读。反例针对交换性质，不自动分类全部有限表现对象。
- [Mathlib 有限表现概念](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Presentable/Finite.html)；isFinitelyPresentable_iff_preservesFilteredColimitsOfSize。形式化基础库；检索文档摘要。只有一般定义命中；无本题等价定理命中，未重跑。

**实际检索词：** 学术名称 `measurable spaces finitely presentable finite discrete Brandenburg`；公式/特征 `category Meas filtered colimits finite presentable objects sigma algebra`；代码 `site:github.com "Meas" "FinitelyPresentable"`；公开AI/社区 `"measurable spaces" "finitely presentable" (site:mathoverflow.net OR site:zenodo.org OR "aiXiv")`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**待复核：** 区分可测结构与底集合的滤过余极限，专查分类的必要方向。

#### QX-P-001987 · Trappist-1（无限象棋变体）mate-in-n 可判定性 · P0

**旧卡 → 变化：** 棋盘和合法步集合无限；‘固定深度逐层枚举’不能直接给终止算法。普通无限象棋的 Presburger 证明不覆盖素数跳跃。 → 已核原问和普通无限棋邻题；未取得该变体的可判定/不可判定证明。新搜索命中支持 Huygens 的棋引擎，但有限机器坐标/启发搜索不是判定定理。

**原题范围：** Trappist-1 无限棋含 Huygens 以任意素数格数正交跳跃；问 mate-in-1 或固定 n 的 mate-in-n 是否不可判定。

**直接证据与定位：**

- [MSE4464503 原题](https://math.stackexchange.com/questions/4464503/is-mate-in-n-problem-for-trappist-1-undecidable)；Huygens 定义、mate-in-1 示例及一般问句。社区原题；全文已读。素数距离是与普通无限棋的关键差别。
- [Brumleve–Hamkins–Schlicht 普通无限棋](https://arxiv.org/abs/1201.5597)；摘要与作者公开说明。论文邻题；检索返回摘要已读，未通读论文。Presburger 可定义走法的证明；不宣称已覆盖本变体。
- [infinite-chess-engine](https://github.com/FirePlank/infinite-chess-engine/blob/main/docs/ARCHITECTURE.md)；检索返回 i64 坐标与 Huygens 原坐标素数关系说明。软件邻题；仅搜索摘要，未审完整代码。功能支持不是无限输入的可判定性证书；没有运行。

**实际检索词：** 学术名称 `Trappist-1 infinite chess mate in n decidability Huygens`；公式/特征 `prime leaper infinite chess Presburger arithmetic Brumleve Hamkins Schlicht`；代码 `site:github.com infinitechess Trappist Huygens`；公开AI/社区 `"Trappist-1" "mate" (site:mathoverflow.net OR site:zenodo.org OR "aiXiv" OR "EulerSolve")`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**待复核：** 查实际不可判定归约或有效素数距离决策法，禁止将引擎搜索成功当数学判定。

#### QX-P-001990 · 任意 3 维凸体能否被四面体笼困住 · P0

**旧卡 → 变化：** 笼是四面体1-骨架六根杆，不是四个支撑平面组成的外切四面体；可外切不等于不能逃逸。 → 原作者定义已核。Schramm 的 midscribing 与二维圆盘的 cage 结果不能直接当作任意三维凸体的动态困笼定理。

**原题范围：** 任意 R³ 的凸紧体（有非空内部），能否被某四面体的六条棱组成的固定笼困住，无法经允许旋转的连续刚体运动逃到远处而不让棱穿入体内部。

**直接证据与定位：**

- [MO379560 原题](https://mathoverflow.net/questions/379560/can-every-3-dimensional-convex-body-be-trapped-in-a-tetrahedral-cage)；Kuperberg 问题正文的四条定义、2020-12-23。社区原题；全文已读。明确六棱、允许旋转、杆不进入内部的逃逸路径。
- [Schramm, How to cage an egg](https://link.springer.com/article/10.1007/BF01231901)；出版商 Summary，Invent. Math. 107 (1992), 543–560；DOI10.1007/BF01231901。已刊邻题；出版商摘要已读；全文未取得。midscribing 是相邻但不同结论，不能代替运动困笼性质。
- [Tetrahedral and pentahedral cages for discs](https://www.dlib.si/stream/URN%3ANBN%3ASI%3ADOC-IPWVXVGV/918ccb87-8c1b-4027-a406-8b5a0f401da1/PDF)；题名与摘要。已刊邻题；仅搜索摘要。研究圆盘及特定笼，不能覆盖具有非空三维内部的全部凸体。

**实际检索词：** 学术名称 `Kuperberg convex body tetrahedral cage Schramm egg`；公式/特征 `convex body trapped tetrahedron one skeleton rigid motion cages`；代码 `site:github.com tetrahedral cage convex body`；公开AI/社区 `"tetrahedral cage" (site:mathoverflow.net OR site:zenodo.org OR "aiXiv" OR "EulerSolve")`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**查重：** `QX-P-001990|QX-P-002038`，双方版本 `431df874aac63e3f` / `f90af92266bbd252`，结论 **相关但不等价**。1990 固定三维、以六条杆的连续刚体逃逸定义困笼；2038 是高维凸体的投影面积数量级，原帖固定二阶矩归一化。维数、动力学条件及目标量完全不同。

**待复核：** 对静态边切与动态不能逃逸建立精确对应前，不将相邻定理认作全解；指定2038仅作不同问查重。

#### QX-P-001984 · Ruelle 算子谱单性通有性（题面修正） · P0

**旧卡 → 变化：** 当前人话版在主特征值简单、全谱简单、开稠和稠密Gδ间混用；必须回到原文后决定。 → 已实际执行原址、API、StackPrinter、题名及公式查询，指定两帖未恢复。相邻 Ruelle 文献不据标题套用；原题数学状态暂不判断。

**原题范围：** 旧卡声称原问题为 Ruelle 算子谱单性的 C1 通有性；本轮未取回 MSE4753404/MO452567，故不确认其精确函数空间、势函数、主特征值/全谱及开稠/剩余量词。

**直接证据与定位：**

- [MSE4753404 原入口](https://math.stackexchange.com/questions/4753404)；数字链接、q/、尾斜杠、StackPrinter 与官方API尝试。原题入口；全文不可达。多种读法未恢复原文；并非零命中证明开放。
- [MO452567 旧卡交叉入口](https://mathoverflow.net/questions/452567)；数字链接与定向检索。旧出处线索；全文不可达。未确认与原MSE的完整对应。
- [The Ruelle spectrum of generic transfer operators](https://www.aimsciences.org/article/doi/10.3934/dcds.2012.32.2521)；学术摘要。已刊邻题；仅检索摘要。摘要为特征值序列上界在稠密算子族最优，不等价于本卡所述 C1 简单性。

**实际检索词：** 学术名称 `Ruelle transfer operator spectral simplicity C1 generic Axiom A conjecture`；公式/特征 `"dim" "ker" "Ruelle" "generic"`；代码 `site:github.com Ruelle spectral simplicity Lean`；公开AI/社区 `"Ruelle" "simplicity" (site:mathoverflow.net OR site:zenodo.org OR "aiXiv")`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**待复核：** P0：优先取得指定原题正文，核 C1 拓扑、AxiomA 假设、谱空间与 r 的意义，再谈结果状态。

#### QX-P-001989 · PTE 型均衡剖分集合刻画 · P0

**旧卡 → 变化：** 人话版却讨论多边形等面积三角剖分和 Monsky，和同卡历史的幂和/Thue–Morse内容冲突。 → 必须先恢复原题后修复人话版。已检索到 Littlewood 多项式/等幂分拆文献，但不能在未知 s_n 精确定义时宣称覆盖原题。

**原题范围：** 包内历史线索指 Prouhet–Tarry–Escott 型整数分拆最大等幂指数 s_n；指定 MSE4075536 本轮未恢复，故不补造其精确定义和端点约定。

**直接证据与定位：**

- [MSE4075536 指定入口](https://math.stackexchange.com/questions/4075536)；数字链接直接打开；PTE、s_n、Littlewood关键词恢复检索。原题入口；全文不可达。仅凭历史卡无法确认 s_n 的全定义。
- [Littlewood polynomials, spectral-null codes, and equipowerful partitions](https://cris.bgu.ac.il/en/publications/littlewood-polynomials-spectral-null-codes-and-equipowerful-parti/)；机构文献页摘要。学术邻题；仅检索摘要。联系多项式在1的零点阶与等幂分拆；暂不判与原题完全等价。

**实际检索词：** 学术名称 `Prouhet Tarry Escott equitable partition s_n maximum exponent`；公式/特征 `Littlewood polynomial vanishing order one partition first n integers equal power sums`；代码 `site:github.com Prouhet equitable partition Lean`；公开AI/社区 `"Prouhet" "partition" (site:mathoverflow.net OR site:zenodo.org OR "aiXiv" OR "EulerSolve")`。这些查询已执行，批次结果和后续读取层级见逐题记录。

**待复核：** P0 取得原帖正文并核 {0,…,n−1}/{1,…,n}、次数起点及量词；之后再决定 Thue–Morse 的特例覆盖。

### 其余必须保留的题面校准

|题号|校准|
|---|---|
|001966|原题分别问表示数无界与取遍自然数，不是泛问计数方法。|
|001967|Ω 为停机概率的二进制展开，非 Lambert W 常数；机器量词待明确。|
|001968|$P_n$ 的元素为 n 顶点图的同构类，序为子图关系，不是全部图类的包含格。|
|001969|输入为整数系数实多项式，问四类 Sharkovskii 截断参数；不是随意给定有限初始段。|
|001970|噪声为独立均匀分布；已核局部密度评论，未得全局显式密度。|
|001977|原问是复数域的唯一性；排除离散域，且“所有 C¹ 函数”的量词不能省。|
|001982|要求各类型测地线的全局完备，n≥3 的穿孔球面是剩余主问。|
|001988|对象为可分叉、总长2的树；单位弧 Moser 文献不能直接覆盖。|


## 第2部分：分题证据与复核事项


检查日期：2026-11-26（Asia/Shanghai）。仅负责任务文件中的 25 题，版本逐项保留。全部操作只读；没有线上改卡、发帖或合并，没有执行外部证明程序。

本文件只收影响题面、数学声明范围、出处或查重的发现。已存在于旧卡的结果，只在范围纠错或来源复核必要时提及，不列为新定理。逐题完整记录在 QX-NEW-06_逐题回传.jsonl；89 个原始工具返回在 检索审计文件；审计索引含原始参数和 SHA-256。

### 优先复核顺序

1. **002016**：A126776 的立方体对称轨道数不等于任意欧氏全等计数，五维已有原文反例。撤回错误序列识别和据此产生的 AI 错误判断。
2. **002018**：新取得直接声称 L(F₂)≅L(F₃) 的作者原稿及固定提交 Lean 代码；保持完整声明待核，未独立运行。
3. **002007**：最新 v10 的残数上界推论另需负性条件；旧卡遗漏，且把 1/ζ 写成整函数。
4. **002013**：一般坏生成集声明与 S_{p,q} 特定族分开；预印本元数据冲突和最新版不可达须保留。

### 具体变化

#### QX-P-002016 · 版本 41eada573b749cb1

**分项结论**：旧卡 S(n)=A126776(n) 的识别：原题已反驳；真实欧氏全等计数 S(n)：暂未找到可验证结果；以边长多重集作为全等判据：题面有误。

**旧卡 → 本轮发现**：关键新发现：原评论与旧卡混用了立方体对称轨道和任意欧氏全等。两个不同五维对称轨道可全等，因此现卡的 237 不能是原题的五维计数。这是根据已读原文反例与表格作出的明确推论。

- P0 · S(4)=17、S(5)=237、S(6)=9892 是全等类计数；已独立验证 → 保留它们为立方体对称轨道数据，撤回 n≥5 时与欧氏全等计数等同；不得沿用旧“独立验证”。

- P0 · AI 说不在 OEIS 已被 A126776 推翻 → 撤回基于错误等价关系的 AI 错误判定，真实欧氏全等序列是否另在 OEIS 待核。

- P1 · 枚举边长多重集即可核类别 → 比较带顶点关联的完整距离矩阵，并对顶点置换取等价类。

**量词与适用范围**：对单位 n-立方体的顶点选 n+1 个仿射独立点，按任意欧氏等距下的全等分类，求 n-单纯形的类别数；原题还问该序列是否已知。这里的等价关系并非必须延拓为整个立方体的对称。

**直接证据与定位**：

- [How many non-congruent n-simplices can be formed from vertices of the n-cube?](https://mathoverflow.net/questions/495937/how-many-non-congruent-n-simplices-can-be-formed-from-the-vertices-of-the-n)：原问的 non-congruent；评论对 A126776 的链接。欧氏全等计数；评论的序列链接必须另核等价关系。 获取状态：已打开并读取正文。审计：trace_id=`part_1/015_sources`。
- [OEIS A126776](https://oeis.org/A126776)：序列 1,1,4,17,237,9892…；定义为基的对称轨道计数与参考论文。按立方体对称计数的更细等价关系；并非所有欧氏全等。 获取状态：已打开定义及参考链接。审计：trace_id=`part_1/018_primary_papers`。
- [Bremner–Dutour Sikirić–Schürmann: Polyhedral representation conversion up to symmetries](https://arxiv.org/pdf/math/0702239)：Table 1 印刷 p.14（PDF 第 14 页）；cube 的 bases orbits，锥维数 n+1。237、9892 是立方体对称群下基轨道的计数；不能自动改为欧氏全等数。 获取状态：已打开全文并核表与对称群口径。审计：trace_id=`part_1/021_cube_toric_scope`。
- [Günter M. Ziegler: Lectures on 0/1-Polytopes](https://www.mi.fu-berlin.de/math/groups/discgeom/ziegler/Preprintfiles/067PREPRINT.pdf)：2001-11-06；Proposition 7，印刷 pp.9–10；p.10（PDF 第 10 页）两组 6 个顶点的五维全维单纯形。两单纯形欧氏全等但不 0/1-equivalent；反证通过配对距离与列 1 数量不变量。来源同时注明 d≤4 的全维情形不存在这类差别。 获取状态：已打开并逐项核反例和命题适用范围。审计：trace_id=`part_1/024_cube_counterexample`。
- [Brandts–Cihangir: On the combinatorial structure of 0/1-matrices representing nonobtuse simplices](https://dml.cz/bitstream/handle/10338.dmlcz/147590/AplMat_64-2019-1_1.pdf)：Applications of Mathematics 64 (2019),1–31；印刷 p.6 图 3 附近（PDF 第 7 页）。明确说明维数 5 及以上存在全等但不在同一 B_n 轨道的单纯形，为同一等价关系差别的独立原文佐证。 获取状态：已打开相关段落。审计：trace_id=`part_1/023_cube_primary`。

**实际检索路径**：原始题页打开 → 两套学术词组：“non congruent simplices vertices n cube A126776”；“hypercube simplices Euclidean congruence enumeration Kagey” → GitHub/Lean 查询：“site:github.com "cube" "simplices" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "simplices" "non-congruent"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：本轮没有计算真正 S(5)/S(6)，只有严格错配与 S(5)<237 的推论。 下一步：采用距离矩阵模顶点置换的可审计枚举，或寻找明说欧氏 congruence 的序列/论文；不运行未审代码。

#### QX-P-002018 · 版本 8cb3493e8a82e763

**分项结论**：原有曲面群与自由群因子同构路线：完整证明/反例声明待核；新增直接例：F_2 与 F_3：完整证明/反例声明待核；相应 Lean 声明与实际原题的对应：未作判断。

**旧卡 → 本轮发现**：新作者原稿和固定提交代码提供 F_2/F_3 的直接候选，补上旧卡遗漏的自由群因子同构声明。数学接受度和形式化运行均未独立审定，保留 claimed；不能把读取代码当成验证成功。

- P0 · 自由群因子问题本身仍 open → 新增 OpenAI 2026-09-23 的 L(F_2)≅L(F_3) 完整声明，锁定 commit；状态仍为声明待核。

- P0 · 未列可定位代码或容易把 comparator 当证明 → 分别登记 comparator、solution、配置和依赖；明确代码已取得未重跑。

**量词与适用范围**：是否存在两个不同构的有限生成、无扭双曲群 G,H，使其群冯诺依曼代数 L(G)≅L(H)？例如若 L(F_2)≅L(F_3) 的声明成立，则 F_2、F_3 直接满足原问。

**直接证据与定位**：

- [Is there a pair of non-isomorphic torsion-free hyperbolic groups that have isomorphic von Neumann algebras?](https://mathoverflow.net/questions/486250/is-there-a-pair-of-non-isomorphic-torsion-free-hyperbolic-groups-that-have-isomo)：原题存在性与有限生成双曲群范围。须给两个非同构无扭双曲群；F_∞ 不可直接充当有限生成例子。 获取状态：已打开并读取正文。审计：trace_id=`part_1/007_priority_revision`。
- [D. Shlyakhtenko: On the II_1 Factors of Fuchsian Groups](https://arxiv.org/html/2609.11074v1)：v1 2026-09-10；Corollary 1（g≥2）；§1.1 AI 参与说明。声称 L(π_1Σ_g)≅L(F_{2g−1})；原始来源可直接适配原题，但本轮没有独立审定长证明。 获取状态：已打开全文和版本页，未独立证明审定。审计：trace_id=`part_1/002_priority_search`。
- [OpenAI: An isomorphism of the free group factors](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/An-isomorphism-of-the-free-group-factors-September-23-2026/build/main.tex)：2026-09-23；固定 commit 3344da59991ed94f9ba711217b29c1d760badfa6；main.tex 中 Theorem 1.2 / label thm:main；引言明确不依赖曲面群预印本。声明有 unital normal trace-preserving *-isomorphism L(F_2)→L(F_3)；main.tex 的各节由 input 引入，本轮未取得并审读全部子文件。 获取状态：已取得主 TeX；PDF 直接访问失败；完整证明各节未审计。审计：trace_id=`part_1/034_free_factor_tex`。
- [InterpolatedFactors comparator statement](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/InterpolatedFactors.lean)：OAI.FreeGroupFactorMain.Interpolation.allInterpolatedIsomorphic；groupVonNeumann 定义与整数参数分支。端点 r,s:ℝ≥0∞，1<r,1<s，结论 NormalTracialEquiv；比较器含 sorry 是待比对陈述，不可作证明本体。 获取状态：已取得固定提交文件；未重跑。审计：trace_id=`part_1/029_free_factor_code_0`。
- [InterpolatedFactors solution module](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Analysis/InterpolatedFactors/Interpolation.lean)：allInterpolatedIsomorphic 调用 Model.allIsomorphic；导入 NormalTransport 等模块。本文件含所选端点的证明项；未审其传递依赖，不能据此宣称无额外公理或完整验证。 获取状态：已取得代码未重跑；未审完整依赖闭包。审计：trace_id=`part_1/030_free_factor_solution`。
- [InterpolatedFactors comparator configuration](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/InterpolatedFactors.json)：solution_module、theorem_names、permitted_axioms、enable_nanoda。配置允许 propext、Quot.sound、Classical.choice，enable_nanoda=false；这是配置，不是实际公理审计输出。 获取状态：已读固定提交配置。审计：trace_id=`part_1/029_free_factor_code_1`。
- [Lean dependencies for the fixed commit](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/lake-manifest.json)：mathlib revision d13f23b723b8a846827a245b89c10fc7d3f11612；另读 lean-toolchain 为 leanprover/lean4:v4.34.1。依赖版本已定位，未安装/运行；全部 raw 文件可审计。 获取状态：已取得依赖版本；未运行。审计：trace_id=`part_1/029_free_factor_code_2`。
- [oai-math-revised: An isomorphism of the free group factors](https://mathcommunity.github.io/oai-math-revised/papers/An-isomorphism-of-the-free-group-factors-September-23-2026/)：公开 AI 成果页的论文链接和 formalization/comparator 说明。用作发现作者仓库的线索和该社区自身记录，不作为独立确认定理正确性的数学证据。 获取状态：已打开；后续已转读作者仓库。审计：trace_id=`part_1/025_claims_primary`。

**形式化界限**：已取得代码未重跑；端点与 r=2,s=3 的局部对应已核，依赖闭包和全部语义对应未审；未独立通过。 比较器中的 sorry 是陈述占位，不能作证明本体；solution 仅末端模块已读，未核全部传递依赖。

**实际检索路径**：原始题页打开 → 两套学术词组：“Shlyakhtenko II1 factors Fuchsian groups 2609.11074”；“nonisomorphic torsion free hyperbolic groups isomorphic von Neumann algebras surface free” → GitHub/Lean 查询：“site:github.com "Shlyakhtenko" "Fuchsian" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "Fuchsian" "factors"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：主 TeX 的各节及 solution 的传递依赖未逐一审计，未编译；配置的 permitted_axioms 不等于已运行审计。 下一步：在后续专门深查中先读所有输入章节和依赖代码，核定义、占位及额外公理，再按安全流程决定是否独立重跑。；本轮固定仓库 commit 为 2026-11-25 的 3344da59991ed94f9ba711217b29c1d760badfa6；原稿与社区页可能继续更新。 下一步：保留固定提交复现，后续版本另立记录，不覆盖本次未重跑状态。

#### QX-P-002007 · 版本 c7c286b90ebdd423

**分项结论**：现卡 1/ζ 为整函数且无条件等于导数倒数：题面有误；RH+单性足以推出所列 Chavez 上界：题面有误；满足额外负性条件时的上界：部分进展；M(T) 的增长率：暂未找到可验证结果。

**旧卡 → 本轮发现**：这是原稿最新版的假设修正：旧卡遗漏关键负性条件，并有整函数/亚纯函数错误。不得将该论文写成只凭 RH+单性即可控制最大残数。

- P0 · 1/ζ 是整函数；ζ 的零点被抵消 → 1/ζ 为亚纯函数；单零点产生简单极点，残数为 1/ζ′。

- P0 · RH+单性条件有效上界 → 补 v10、Cor.1/2 的相关式右端为负条件；标出负性只有数值支持而非已证。

**量词与适用范围**：ρ 遍历 ζ 的非平凡零点，问 M(T)=max_{|Imρ|≤T}|Res_{s=ρ}(1/ζ(s))| 的合理增长猜想。只有在各零点简单时残数才等于 1/ζ′(ρ)；1/ζ 是亚纯函数。

**直接证据与定位**：

- [Growth of residues of 1/zeta(s): conjectures?](https://mathoverflow.net/questions/411943/growth-of-residues-of-1-zetas-conjectures)：问题 M(T) 定义；Petrov/Helfgott 的单零点评论；Lucia 2021-12-17 的 Gonek 猜想评论。非平凡零点上的最大残数；T^{1/3+o(1)} 为社区所转述猜想。 获取状态：已打开并读取正文。审计：trace_id=`part_1/010_sources`。
- [Gordon Chavez: Correlations of multiplicative functions with their partial sums](https://arxiv.org/abs/2409.02106)：版本历史：v10，2026-05-14；作者备注 2026-03 接收、修改；关联 DOI 10.1142/S1793042126500934。已核最新 arXiv 版本页；接收情况按作者元数据记录，未另核出版社出版全文。 获取状态：已打开版本页。审计：trace_id=`part_1/035_background_primary`。
- [Chavez v10 — Theorems 1–2 and Corollaries 1–2](https://arxiv.org/html/2409.02106v10)：§1.1 式 (1.5)、(1.6)；§1.2 Corollaries 1、2，式 (1.10)、(1.11)；随后数值证据警告。Cor.1 要 (1.5) 成立且右端为负才得 1/ζ′(ρ)=o(|ρ|)；Cor.2 同样要 (1.6) 右端负，另列 RH，才得 o(|ρ|loglog|Imρ|)。负性不由 RH+SZC 在此自动获得。 获取状态：已打开最新全文并核条件。审计：trace_id=`part_1/036_zeta_howe_versions`。
- [Heap–Li–Zhao: Lower bounds for discrete negative moments of the Riemann zeta function](https://arxiv.org/abs/2003.09368)：arXiv v1；Algebra & Number Theory 16 (2022), 1589–1625；摘要。负矩的下界不等于最大残数增长律或统一上界。 获取状态：已打开摘要和版本页；未逐节审计全文。审计：trace_id=`part_1/035_background_primary`。

**实际检索路径**：原始题页打开 → 两套学术词组：“growth residues reciprocal zeta function Gonek negative moments”；“maximum 1 zeta prime rho T one third 2409.02106” → GitHub/Lean 查询：“site:github.com "zeta" "residues" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "zeta" "negative moments"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：本轮核了版本与定理范围，但没有独立审计全文，也没有证明额外负性。 下一步：保留条件性结论；若后续有负性定理，核其量词是否足以代入 Cor.1/2。

#### QX-P-002013 · 版本 d11c4e96350af458

**分项结论**：随群变化的族与固定群的一致性：题面有误；SL_n(Z) 等无限线性群的一般一致 Kazhdan 常数：完整证明/反例声明待核；指定 S_{p,q} 家族的下界：暂未找到可验证结果。

**旧卡 → 本轮发现**：本轮新增可定位的 d+2 生成元声明，同时发现旧卡来源元数据与本次官方索引正文冲突；不能用它消除已单列的 S_{p,q} 剩余问题。

- P0 · 一族群与生成集共同正下界 → 固定群 Γ 的全部有限生成集；单列 S_{p,q}。

- P0 · 题名写否定解决；2608.03561 作者/题名当作已完全核定 → 一般版本保留完整声明待核；特殊族不宣告解决；登记官方索引与其他条目版本元数据冲突。

**量词与适用范围**：固定有限生成群 Γ，问 κ_u(Γ)=inf_S κ(Γ,S) 是否为正，S 遍历有限生成集；具体剩余问 SL_3(Z) 的 S_{p,q}={I+pE_ij,I+qE_ij:i≠j}（gcd(p,q)=1）是否有一致正下界。

**直接证据与定位**：

- [On uniform Kazhdan's property (T)](https://mathoverflow.net/questions/280665/on-uniform-kazhdans-property-t)：固定 Γ 上所有有限生成集；SL_3(Z) 的 S_{p,q} 子问。一般一致性和特殊生成集族是两个层次。 获取状态：已打开并读取正文。审计：trace_id=`part_1/012_sources`。
- [Finite direct-product quotients and uniform Kazhdan constants（本次官方索引正文题名）](https://arxiv.org/abs/2608.03561)：索引正文作者 Jvbin Yao、2026-08-04；Theorem 1.1；κ(Γ,S_m)≤2/√m。任意多因子的非平凡有限直积商给 κ_u(Γ)=0，适用 SL_n(Z)；未约束 S_m 为 S_{p,q}。其他检索条目显示 Lubotzky–Yao/不同题名，版本关联未核清。 获取状态：已读索引缓存正文；最新官方版本页/直接 PDF 不可达，元数据有冲突。审计：trace_id=`part_1/007_priority_revision`。
- [Gelander–Lubotzky–Yao: Small Kazhdan constants for small generating sets of linear groups](https://arxiv.org/abs/2609.36098)：本次索引正文 Theorem 1.1，2026-09；无限有限生成线性群、d+2 个生成元。声称固定无限有限生成线性群可用大小 d+2 的生成集让 Kazhdan 常数任意小；没有固定 S_{p,q} 形状。 获取状态：已读索引缓存正文；直接最新版及版本历史未能访问。审计：trace_id=`part_1/007_priority_revision`。

**实际检索路径**：原始题页打开 → 两套学术词组：“uniform Kazhdan property SL3 Z Lubotzky Yao 2026”；“Kazhdan constants I+pEij I+qEij relatively prime p q” → GitHub/Lean 查询：“site:github.com "Kazhdan" "uniform" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "Kazhdan" "uniform"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：2608.03561 出现题名/作者冲突；直接 abs/html/pdf 多次失败。对 v3 的访问尝试不构成该版本存在证据。 下一步：取得官方可达版本历史和固定版本全文，核作者、题名、定理与修订/撤回情况。；S_{p,q} 未被任意生成集定理覆盖。 下一步：单独核有关 p、q 及初等矩阵生成集的定量定理。

#### QX-P-001993 · 版本 6949d1d8e146bbda

**分项结论**：现卡的最大维数问法：题面有误；原题最小 d 的确值：暂未找到可验证结果。

**旧卡 → 本轮发现**：把最小维数改成最大维数是实质题面错误；原始上下界约束的是最小值。乘射影空间给出的无上界是本轮根据原题条件所作的直接数学推论。

- P0 · 无有理点光滑真 Z-概形维数上限；最多能到几 → 无截面光滑真 Z-概形的最小相对维数；注明 Spec Z 截面及 2≤d≤5。

**量词与适用范围**：求非空、光滑、真态射 X→Spec Z 且无截面的最小相对维数 d。原页给出的界是 2≤d≤5。

**直接证据与定位**：

- [What can be the dimension of a pointless smooth proper Z-scheme?](https://mathoverflow.net/questions/111708/what-can-be-the-dimension-of-a-pointless-smooth-proper-z-scheme)：问题正文开头及 2≤d≤5 的讨论。最小相对维数、非空、光滑真、无截面。 获取状态：已打开并读取正文。审计：trace_id=`part_1/007_priority_revision`。

**实际检索路径**：原始题页打开 → 两套学术词组：“pointless smooth proper scheme integers minimum dimension Sawin”；“smooth proper Z scheme without section dimension 2 5 E7” → GitHub/Lean 查询：“site:github.com pointless smooth proper scheme (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) pointless smooth proper scheme”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：现有检索只核到原始上下界；不能复用旧卡“2013–2026 零推进”。 下一步：核能改进最小相对维数的具体构造或下界证明。

#### QX-P-001994 · 版本 ce94070932e4310e

**分项结论**：现卡的方向线段覆盖叙述：题面有误；强版满测度结论：部分进展；单圆弱版与区间版的关系：部分进展。

**旧卡 → 本轮发现**：弱版不是来源毫无进展的另一题：Eberhard 已给紧集归约。此发现纠正旧备注，但不足以把整题提升为已证。

- P0 · 每个方向的单位线段；圆环总面积能否很小 → 恢复所有中心、半径区间趋近 1、整圆包含与补集正测度命题。

- P1 · 弱化变体 open → 记录 Eberhard 的弱版归约及非可测性保留；强版维持评论草图级证据。

**量词与适用范围**：S⊂R²，任意中心 x 与 ε>0 都有非退化区间 [a,b]⊂[1−ε,1]，使该中心、这些半径的整圆均含于 S；问 S 的补集能否有正 Lebesgue 测度。另有正测度半径集版与每中心每 ε 仅一圆版。

**直接证据与定位**：

- [A Kakeya-like problem: must a union of annuli fill the plane?](https://mathoverflow.net/questions/108507/a-kakeya-like-problem-must-a-union-of-annuli-fill-the-plane)：问题正文与更新；Tao 2012-10-01 评论；Eberhard 同日 20:11/20:28 评论。以所有中心及趋近 1 的半径为量词；Eberhard 讨论正测度补集的紧子集归约，并保留非可测情形疑问。 获取状态：已打开并读取正文。审计：trace_id=`part_1/006_recovery`。

**实际检索路径**：原始题页打开 → 两套学术词组：“annuli Kakeya full measure Aaronson Tao Marstrand”；“set circles every centre radii approaching one complement positive measure” → GitHub/Lean 查询：“site:github.com Kakeya annuli (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) union annuli fill plane”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：来源没有完整成文回答；Tao 的一段评论不足以独立审定全测度结论。 下一步：核 Marstrand 改造中的统一局部密度估计，并在可测版本明确写出紧集归约。

#### QX-P-001998 · 版本 587cbd098eae78f4

**分项结论**：现卡全部根共线问法：题面有误；Q1/Q2/Q3/Q4 的存在性与 Q2 斜率分类：部分进展；相关变体：若 N_p(α)>1，是否必为 2 的幂：原题已反驳。

**旧卡 → 本轮发现**：新发现是旧备注对根数变体的状态过弱、且人话版目标错误；四个存在性构造早已在旧卡，不能重标为新突破。

- P0 · 全部复根同一直线及完整分类 → 恢复四个编号子问和排除条件。

- P1 · 2 的幂猜想仅被 3×6 实例削弱 → 注明 338213 无附加限制版本被六次 Eisenstein 反例否定；保留斜率分类及更严格版本的区别。

**量词与适用范围**：不可约有理系数多项式，在排除坐标轴、平移退化及原文所述旋转对称情形后，分别问：一条线可否含超过四个根；四根以上的非水平非竖直线与可能斜率；恰有三个根共线；所有根形成 p×q 网格且 p 非 2 的幂是否可能。

**直接证据与定位**：

- [Aligned roots of irreducible polynomials](https://mathoverflow.net/questions/219315/aligned-roots-of-irreducible-polynomials)：四个编号子问、两次 EDIT、18 次 3×6 根网格实例。四个存在性问题及斜率分类；不是全部根共线。 获取状态：已打开并读取正文。审计：trace_id=`part_1/011_sources`。
- [Collinear Galois conjugates — Jeremy Rouse's answer](https://mathoverflow.net/questions/338213/collinear-galois-conjugates)：Rouse 2019-08-12 回答：六次例子与 Eisenstein 反例。一般位置三根共线；N_p(0)=6 的无附加限制根数变体。 获取状态：已打开并读取正文。审计：trace_id=`part_1/011_sources`。

**实际检索路径**：原始题页打开 → 两套学术词组：“aligned roots irreducible polynomials collinear Galois conjugates”；“irreducible polynomial rational slopes 3 by 6 grid roots Rouse” → GitHub/Lean 查询：“site:github.com "collinear" "polynomial" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "aligned roots"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：斜率全分类未获证据；18 次例子未独立代数重算。 下一步：后续审查分开核四项存在性、斜率集和带轴线/对称排除的根数变体。

#### QX-P-001999 · 版本 2a6ca66a0f531b96

**分项结论**：现卡复数/高度计数口径：题面有误；受限类别的计数公式：部分进展；原题所有同源类的统一上界：暂未找到可验证结果。

**旧卡 → 本轮发现**：新增已刊的精确质量公式只属于受限情形；它同时暴露现卡遗漏有限域和群胚权重的问题，不支持一般 solved。

- P0 · 复环面、按高度或判别式计数 → 改为 F_q、Frobenius 特征多项式、主极化及 Σ1/|Aut(A,λ)|。

- P1 · 只概括 Howe 2020/simple ordinary → 增加 2023 Theorem A，并细分 fixed order、极化同源类及一般上界。

**量词与适用范围**：在 F_q 上固定 g 维阿贝尔簇的 Frobenius 特征多项式，计所有主极化对象的群胚基数 Σ1/|Aut(A,λ)|；求公式，或统一 O(q^{g(g+1)/4+ε}) 上界。标准维数记号下特征多项式次数为 2g。

**直接证据与定位**：

- [Counting abelian varieties over finite fields in a given isogeny class](https://mathoverflow.net/questions/218085/counting-abelian-varieties-over-finite-fields-in-a-given-isogeny-class)：问题正文，groupoid cardinality 与 O(q^{g(g+1)/4+ε})。有限域主极化对象的加权计数；原页首句 degree g 与后文 g 维口径有记号不一致，回写应统一。 获取状态：已打开并读取正文。审计：trace_id=`part_1/009_sources`。
- [Achter–Altuğ–Garcia–Gordon: Counting abelian varieties over finite fields via Frobenius densities](https://discovery.ucl.ac.uk/id/eprint/10183003/3/Garcia%20Martinez_Counting%20abelian%20varieties%20over%20finite%20fields%20via%20frobenius%20densities_VoR.pdf)：Algebra & Number Theory 17 (2023), 1239–1280；Theorem A 印刷 p.1240，PDF 第 3 页；同源定义 §2A p.1242。交换自同态环，且 ordinary 或 q 为素数；质量为 q^{g(g+1)/4}τ_Tν_∞∏ν_l；不能抹去各因子就得统一上界。 获取状态：已打开全文并核 Theorem A、定义及条件。审计：trace_id=`part_1/019_primary_followups`。
- [Howe: Variations in the distribution of principally polarized abelian varieties among isogeny classes](https://arxiv.org/abs/2005.14365)：arXiv v1 2020-05-29；摘要及本轮取得的 PDF。simple ordinary 同源类内进一步固定自同态环的层；不等于全部一般同源类。 获取状态：已核版本页并取得 PDF；未逐节审定全部证明。审计：trace_id=`part_1/035_background_primary`。

**实际检索路径**：原始题页打开 → 两套学术词组：“counting principally polarized abelian varieties isogeny class Howe 2005.14365”；“isogeny class groupoid cardinality upper bound q g(g+1)/4” → GitHub/Lean 查询：“site:github.com "isogeny" "counting" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "counting abelian varieties"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：没有控制 Theorem A 中 τ_T 与全部局部因子的统一估计，也未核由极化同源子类到原固定 Frobenius 类的求和。 下一步：核所求 ε 上界的常数依赖与各因子、各子类数量；不要把公式主幂直接当上界。

#### QX-P-002008 · 版本 fb842dc283c46b6a

**分项结论**：省略向量丛的题面：题面有误；中心对称 toric Fano 特例：部分进展；所有光滑射影 toric varieties：暂未找到可验证结果。

**旧卡 → 本轮发现**：新检得的受限向量丛存在定理值得补卡，但其范围不能膨胀成所有 toric varieties。

- P0 · full exceptional collection，未注明向量丛 → 补向量丛，不要求 strong；区分任意复形与线丛版本。

- P1 · 未列该已刊特例 → 增加 Cor.1.4 及适用范围和域约定。

**量词与适用范围**：每个光滑射影 toric variety 是否具有由向量丛组成的 full exceptional collection？不预设 strong，也不把向量丛限制成线丛；任意导出范畴对象的 exceptional collection 是不同问法。

**直接证据与定位**：

- [Full exceptional collection of vector bundles for toric varieties](https://mathoverflow.net/questions/396168/full-exceptional-collection-of-vector-bundles-for-toric-varieties)：原问题、vector bundles 限制；Kawamata II Remark 7 的更正指引。向量丛存在性；任意复形、strong 或全为线丛版本均须区分。 获取状态：已打开并读取正文。审计：trace_id=`part_1/015_sources`。
- [Ballard–Duncan–McFaddin: Derived categories of centrally-symmetric toric Fano varieties](https://arxiv.org/pdf/1812.09392)：v2 2020-06-16；Corollary 1.4 印刷 p.4（PDF 第 4 页）；Theorem 1.3 p.3。中心对称 toric Fano 的 forms；非代数闭域时 exceptional 的除代数端环约定须与原题惯例对照。 获取状态：已取得全文并核 Cor.1.4。审计：trace_id=`part_1/023_cube_primary`。
- [Derived categories of centrally-symmetric toric Fano varieties — publication](https://onlinelibrary.wiley.com/doi/10.1002/mana.201900358)：Mathematische Nachrichten 295 (2022), 218–241；DOI 10.1002/mana.201900358。刊物元数据及摘要；范围是中心对称 toric Fano。 获取状态：已打开出版页/摘要。审计：trace_id=`part_1/018_primary_papers`。

**实际检索路径**：原始题页打开 → 两套学术词组：“toric varieties full exceptional collection vector bundles Kawamata 2026”；“smooth projective toric vector bundles exceptional complexes Remark 7” → GitHub/Lean 查询：“site:github.com "toric" "exceptional" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "toric" "exceptional collection"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：中心对称/Fano 限制尚未去除；非闭域定义可能不同。 下一步：后续逐核底域、光滑射影、向量丛、full、exceptional 的完整条件。

#### QX-P-002010 · 版本 a1f14de80955da34

**分项结论**：现卡消去与模主体：题面有误；三变量含坐标的正则 cofinite 子环：部分进展；不加坐标条件的一般原题：暂未找到可验证结果。

**旧卡 → 本轮发现**：把消去改回有限平坦扩张问题，并校正 2024 文献刊物及关键含坐标假设。

- P0 · 多一个变量能否消去；A 自身作为 A-模平坦整 → B=k[x_1,…,x_n] 是有限平坦 A-模，问 A 是否为多项式环。

- P1 · Gurjar 2024 J. Algebra 相关进展 → Gurjar–Miyanishi, JPAA 228(8),107655；Theorem 6 三变量且含坐标的正则 cofinite 情形。

**量词与适用范围**：k 为代数闭特征零域，A⊂B=k[x_1,…,x_n] 且 B 是有限平坦 A-模，问 A 是否也是 k 上多项式环？有限性和平坦性是扩张 B/A 的性质。

**直接证据与定位**：

- [If a polynomial ring is a finite flat module over some subring, is that subring a polynomial ring?](https://mathoverflow.net/questions/309256/if-a-polynomial-ring-is-a-finite-flat-module-over-some-subring-is-that-subring)：原问题假设、n=2 讨论及正文更正。B 为有限平坦 A-模；不涉及 A[y]≅B[y]。 获取状态：已打开并读取正文。审计：trace_id=`part_1/012_sources`。
- [Gurjar–Miyanishi: Normal subalgebras of a polynomial ring](https://www.sciencedirect.com/science/article/pii/S0022404924000525)：JPAA 228(8), 107655 (2024)；DOI 10.1016/j.jpaa.2024.107655；索引可读 Introduction 对 Theorem 6 的范围说明。三变量中 cofinite 正则子环并含一个环境坐标；出版页直接抓取 403，检索返回的原出版页摘要/引言可读。 获取状态：摘要和引言索引已读；全文未取得，直接入口 403。审计：trace_id=`part_1/019_primary_followups`。

**实际检索路径**：原始题页打开 → 两套学术词组：“polynomial ring finite flat subring Miyanishi Gurjar”；“regular subring k[x1 xn] cofinite polynomial ring characteristic zero” → GitHub/Lean 查询：“site:github.com "finite flat" "polynomial" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "polynomial ring" "subring"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：本轮只取得原出版页索引的摘要/引言，未取得 Theorem 6 全文。 下一步：补原稿核证明及精确条件，核是否另有去掉坐标条件的后续结果。

#### QX-P-002012 · 版本 b38e369c3ee5f465

**分项结论**：常数对象 α 与 φ：题面有误；α 的无理性：暂未找到可验证结果；α 的超越性：暂未找到可验证结果。

**旧卡 → 本轮发现**：原题背景常数与真正悬赏常数被混同；需以 α 的精确公式重写。

- P0 · 约 0.7731 的 Flajolet–Martin φ 是否无理/超越 → 以 α 的精确无穷乘积为题面；φ 只作背景并写清关系。

**量词与适用范围**：令 t(n) 为 Thue–Morse 序列，α=∏_{n≥1}(2n/(2n+1))^{(−1)^{t(n)}}。原题问 α 是否无理、是否超越；文中另定义 φ=2^{−1/2}e^γ/α。

**直接证据与定位**：

- [Is the Flajolet-Martin constant irrational? Is it transcendental?](https://mathoverflow.net/questions/230288/is-the-flajolet-martin-constant-irrational-is-it-transcendental)：Shallit 2016-02-05：α 的乘积、φ 与 α 的关系、两个明确问句及移位乘积附注。问的是 α，不是叙述背景中的 φ；乘积起点和因子位置不可互换。 获取状态：已打开并读取正文。审计：trace_id=`part_1/014_sources`。

**实际检索路径**：原始题页打开 → 两套学术词组：“Flajolet Martin constant irrational transcendental Shallit”；“Thue Morse infinite product (2n)/(2n+1) irrationality alpha” → GitHub/Lean 查询：“site:github.com "Flajolet" "Martin" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "Flajolet Martin"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：相关乘积公式可能只改变起点或分子分母，但算术性质不同。 下一步：对任何新结果逐式核指数 t(n)、n 起点和因子，不按常数别名合并。

#### QX-P-002014 · 版本 43b16df324766885

**分项结论**：现卡的满射/纤维与可数性叙述：题面有误；R^ω 上的指定逆像等式：暂未找到可验证结果。

**旧卡 → 本轮发现**：原始逆像等式可明确恢复；错误的满射、纤维条件和可数性不应继续流入后续查新。

- P0 · 连续满射、每点纤维可数稠密或 Q^ω 可数 → 恢复 f^{-1}(Q^ω)=Q_0^ω 及最终为零定义；删除满射/逐纤维限制。

**量词与适用范围**：Q_0^ω 为最终为零的有理数序列集合；是否存在连续 f:R^ω→R^ω，使 f^{-1}(Q^ω)=Q_0^ω？原题没有要求 f 满射，也没有逐纤维计数条件。

**直接证据与定位**：

- [Is there a continuous map f:R^ω→R^ω with dense countable inverse image of Q^ω?](https://mathoverflow.net/questions/280236/is-there-a-continuous-map-f-mathbb-r-omega-to-mathbb-r-omega-with-dense-cou)：原问 f^{-1}(Q^ω)=Q_0^ω；有限维空间的部分构造。Q^ω 不可数，Q_0^ω 可数；没有满射要求。 获取状态：已打开并读取正文。审计：trace_id=`part_1/017_sources`。

**实际检索路径**：原始题页打开 → 两套学术词组：“Banakh continuous map dense countable preimage rational sequences”；“R omega Q omega eventually zero preimage continuous map” → GitHub/Lean 查询：“site:github.com "Banakh" "rational" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "continuous map" "rational sequences"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：有限维构造尚未核到可推广到 R^ω 的依据。 下一步：重点核无限维拓扑与描述集合论约束，不能靠有限维例子结束。

#### QX-P-002006 · 版本 cc0cf77ca9083968

**分项结论**：现卡一般有限项验证说明：题面有误；任意有理权序列下的精确系数计数有理性：暂未找到可验证结果；邻近变体：k-bonacci 权重的模 m 计数有理性：完整证明/反例声明待核。

**旧卡 → 本轮发现**：实际打开 AI 成果页后可确认其问法并非本题：权序列限制和模 m/精确等值计数均不同。

- P0 · 猜出递推即可由有限数据验证；未列具体序列 → 恢复 G_n、r、k、P_n 与 ν_k 公式。

- P1 · D. Ray 证明线索笼统待核 → 将 k-bonacci/模 m 变体和原题精确系数计数分列，记录 SSRN 不可达、ProbXiv 无人工检查。

**量词与适用范围**：正整数 G_n→∞ 且 ΣG_nx^n 为有理函数。固定正整数 r,k，令 P_n(x)=∏_{i=1}^n(1+x^{G_i}+⋯+x^{rG_i})，ν_k(n) 为 P_n 系数恰等于 k 的项数；是否 Σν_k(n)x^n 总为有理函数？否则刻画哪些 G_n 成立。

**直接证据与定位**：

- [A conjectured rational generating function](https://mathoverflow.net/questions/431075/a-conjectured-rational-generating-function)：原题 G_n、P_n、ν_k 公式和两个问句。任意符合条件的权序列；精确等于 k 的系数计数。 获取状态：已打开并读取正文。审计：trace_id=`part_1/011_sources`。
- [ProbXiv: Theorems and Conjectures on Some Rational Generating Functions — 6](https://probxiv.com/problems/theorems-and-conjectures-on-some-rational-generating-functions-6)：Conjecture 6.2 的陈述；GPT-5.5 xhigh 2026-08-17 的 proof attempt；human-review 提示。k-bonacci 权重、系数的同余类模 m 计数；AI 有限自动机证明尝试，不覆盖本题任意权序列和系数恰等于 k。 获取状态：已打开陈述与证明尝试；无人工验证记录。审计：trace_id=`part_1/020_priority_scope`。
- [D. Ray: k-bonacci products modulo m / Stanley Conjecture 6.2 线索](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7590502)：SSRN abstract_id=7590502；搜索条目与直接打开的 403。只有题名/摘要级线索，不能据此核证明；所述变体范围与原题不同。 获取状态：全文入口 403；只有检索信息。审计：trace_id=`part_1/025_claims_primary`。

**实际检索路径**：原始题页打开 → 两套学术词组：“Stanley conjectured rational generating function coefficients equal k products G_n”；“G_n rational generating function nu_k coefficient counts Stern triangle rationality” → GitHub/Lean 查询：“site:github.com "Stanley" "generating function" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "Stanley" "rational generating"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：没有取得 SSRN 全文；ProbXiv 的声明属于相邻变体。 下一步：若取得文稿，核是否另有覆盖任意 G_n 及精确系数值的定理；不得仅靠生成函数主题相同归并。

#### QX-P-002000 · 版本 469369009401ffcc

**分项结论**：现卡的光滑参数要求：题面有误；连续族的相对 C^0 光滑逼近：部分进展。

**旧卡 → 本轮发现**：纠正参数正则性；本轮取得的 PL 文献属于技术支撑，不能据此把整问升级为已证。

- P0 · 参数也光滑依赖 → 恢复连续参数族，注明 Diff 的 C^0 拓扑、D^n 与相对边界条件。

**量词与适用范围**：对紧曲面 S，连续族 D^n→Homeo(S rel∂S) 能否一致逼近为连续族 D^n→Diff(S rel∂S)；Diff 取 C^0 拓扑。原问主要关心二维圆盘，另讨论相对参数子集的版本。

**直接证据与定位**：

- [Approximating homeomorphisms of 2-disk by diffeomorphisms](https://mathoverflow.net/questions/171633/approximating-homeomorphisms-of-2-disk-by-diffeomorphisms)：原问题及作者四步方案；相对参数集与 Kirby–Siebenmann 的备注。连续 D^n 参数，目标 Diff 使用 C^0 拓扑；不是参数可微性定理。 获取状态：已打开并读取正文。审计：trace_id=`part_1/010_sources`。
- [Yagasaki: Homotopy types of homeomorphism groups of noncompact 2-manifolds](https://arxiv.org/pdf/math/0010224)：本轮取得 PDF；原问题指向 Proposition 3.1 的 PL 逼近用途。相关 PL/同伦技术，不能单凭引用证明整个带相对条件的光滑族结论。 获取状态：已取得全文；未对相对光滑版本完成证明审计。审计：trace_id=`part_1/036_zeta_howe_versions`。

**实际检索路径**：原始题页打开 → 两套学术词组：“parametrized approximation homeomorphisms surfaces diffeomorphisms”；“continuous D^n Homeo surface Diff C0 topology isotopy approximation Yagasaki” → GitHub/Lean 查询：“site:github.com "homeomorphisms" "diffeomorphisms" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "approximating homeomorphisms"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：PL 同伦逼近和自述四步方案未自动覆盖相对 D^n 边界。 下一步：核参数相对集合是否满足原引用的 retract 条件，核每一步连续性与逼近尺度。

#### QX-P-001997 · 版本 1befe8c582f436af

**分项结论**：现卡的 P/NP 叙述：题面有误；符合原题要求的新复杂度类：暂未找到可验证结果。

**旧卡 → 本轮发现**：原题并未要求解决 BSS 的 P/NP 问题；人话版把问题的目标替换了。

- P0 · 在 BSS 模型刻画 P、NP 或 P=NP 的结构条件 → 寻找无明显经典 Turing 对应物的自然、有用的 BSS 复杂度类。

**量词与适用范围**：对任意一阶结构 S 上的 BSS 机器，寻找自然且有用、而在经典 Turing 复杂度中没有明显对应物的复杂度类；原例关注带上数值生成的 S-模的维数资源。

**直接证据与定位**：

- [Complexity classes for BSS machines](https://mathoverflow.net/questions/221438/complexity-classes-for-bss-machines)：问题正文，任意一阶结构及 module-dimension 资源的例子。要求没有明显经典对应物的自然复杂度类，不是 P versus NP 决定问题。 获取状态：已打开并读取正文。审计：trace_id=`part_1/009_sources`。

**实际检索路径**：原始题页打开 → 两套学术词组：“BSS complexity classes natural algebraic dimension use set Schweber”；“Blum Shub Smale computation subring dimension resource complexity class” → GitHub/Lean 查询：“site:github.com "BSS" "complexity" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "BSS" "complexity classes"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：2025 BSS/几何复杂度等结果只作为检索线索，未逐定义审定。 下一步：有候选时核具体类、底结构及用途，而非凭 P/NP 词语匹配。

#### QX-P-002009 · 版本 646ddc672fa28697

**分项结论**：现卡 virtual 的解释：题面有误；高连通 Morava K Eilenberg–Moore 收敛：暂未找到可验证结果。

**旧卡 → 本轮发现**：术语 virtual 的误释改变了待研究对象；本轮没有可验收的状态升级。

- P0 · 对发散谱序列作虚拟化/正则化 → 按原文定义 virtual：X 的足够高连通部分；补高度 d 和收敛目标。

**量词与适用范围**：固定 Morava K 理论高度 d，对足够高连通的 X（原文 X=X(m,∞)，m≫d），是否有收敛的 Eilenberg–Moore 谱序列 Cotor^{K_*X}(K_*,K_*)⇒K_*ΩX？

**直接证据与定位**：

- [Does virtual Morava K-theory have an Eilenberg-Moore spectral sequence?](https://mathoverflow.net/questions/330218/does-virtual-morava-k-theory-have-an-eilenberg-moore-spectral-sequence)：问题对 virtual、X(m,∞)、m≫d 的解释；Bauer 结果的原文讨论。高连通截断后的收敛问题；不是任意空间或正则化程序。 获取状态：已打开并读取正文。审计：trace_id=`part_1/012_sources`。

**实际检索路径**：原始题页打开 → 两套学术词组：“virtual Morava K theory Eilenberg Moore spectral sequence Peterson Kuhn”；“Morava K homology highly connected spaces Cotor loop space convergence” → GitHub/Lean 查询：“site:github.com "Morava" "Eilenberg" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "virtual Morava"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：没有核定已知谱序列的假设涵盖原题。 下一步：以高度、连通度、有限型和收敛类型逐项对照候选定理。

#### QX-P-002015 · 版本 0f78ce001d7fc0e8

**分项结论**：稠密 Q̄ 点推出 Q̄ 定义：原题已证。

**旧卡 → 本轮发现**：这是来源和查重的新核实：补正确站点/答案编号，并确认与 001986 同题；不把旧有已证事实重新包装为本轮突破。

- P1 · MO#4475853 → MSE#4475853；对应 MO#428384，Sawin 答案 #428394。

- P1 · 关联线索未逐正文核清 → 与 QX-P-001986@00b8701da1d461f7 标记同题。

**量词与适用范围**：复仿射代数集 X⊂C^n 若 Q̄ 点在 X 中 Zariski 稠密，是否 X 可由 Q̄ 系数多项式定义？更一般可对域扩张 K/F 作同样下降论证。

**直接证据与定位**：

- [Sawin answer: Zariski-dense algebraic points and field of definition](https://mathoverflow.net/questions/428384/is-a-complex-algebraic-set-with-a-zariski-dense-subset-of-algebraic-points-alrea/428394)：答案 428394，Will Sawin，2022-08-12；按 K/F 基展开系数的完整短证明。仿射代数集的域下降；取 F=Q̄、K=C 即原题。 获取状态：已打开并读取正文。审计：trace_id=`part_1/016_sources`。

**实际检索路径**：原始题页打开 → 两套学术词组：“Zariski dense rational points field of definition Milne Proposition 16.8”；“algebraic set K F dense F points basis descent defining polynomials” → GitHub/Lean 查询：“site:github.com "Zariski" "descent" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "Zariski dense" "algebraic points"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：本轮没有新的数学状态变更，已有 solved 被实际原证据支持。 下一步：由维护者决定同题卡链接或合并方式；保留两个版本号。

#### QX-P-002017 · 版本 badc2e89fa1fff2b

**分项结论**：任意度序列完全分类的现卡问法：题面有误；原题的有限度共尾存在性：暂未找到可验证结果。

**旧卡 → 本轮发现**：必须跟踪充分大有限度，而不是仅构造某个有无限度的线图不变图；原问也不要求全分类。

- P0 · 分类所有 G≅L(G) 图的度或度序列 → 存在可数连通 G≅L(G)，其有限度集合包含所有 n≥N_0。

**量词与适用范围**：是否存在以 N 为顶点集的连通简单图 G，使 G≅L(G)，且存在 N_0，使每个整数 n≥N_0 都是某个顶点的度？没有要求所有顶点度均有限。

**直接证据与定位**：

- [Degrees in infinite graphs G with G≅L(G)](https://mathoverflow.net/questions/487188/degrees-in-infinite-graphs-g-with-g-cong-lg)：Question 中 E⊂[N]^2、connected、LG-invariant 和 ∀n≥N_0 的量词。要求有限度集合含全部充分大的整数，不排除别的顶点有无限度。 获取状态：已打开并读取正文。审计：trace_id=`part_1/017_sources`。
- [Infinite graphs isomorphic to their line graph — Wofsey's construction](https://mathoverflow.net/questions/194641/infinite-graphs-isomorphic-to-their-line-graph)：答案的 G→L(G) 嵌入与 L^ω 余极限构造。提供线图不变性的构造方法，但有限度的逐级保持不由此自动给出。 获取状态：已打开并读取正文。审计：trace_id=`part_1/018_primary_papers`。

**实际检索路径**：原始题页打开 → 两套学术词组：“infinite graph isomorphic line graph all sufficiently large degrees”；“degrees infinite graphs G isomorphic L(G) cofinite Banakh” → GitHub/Lean 查询：“site:github.com "line graph" "degree" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "infinite graphs" "line graph"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：现有嵌入/余极限方案不保证指定有限度在极限保持。 下一步：若尝试使用该方法，显式跟踪每个所需有限度顶点及后续新增邻边。

#### QX-P-002019 · 版本 f896657197e906d5

**分项结论**：现卡对 Cauchy 刚性的说明：题面有误；边图+对应边长+顶点角亏的一般唯一性：暂未找到可验证结果。

**旧卡 → 本轮发现**：需修正 Cauchy 的适用条件，并保持角亏与二面角区别；本轮没有一般唯一性的状态变更。

- P0 · Cauchy 已说凸多面体由边长唯一决定 → Cauchy 要对应面全等；仅在已给三角面等条件下可用边长确定面。

**量词与适用范围**：三维凸多面体是否由其边图、各对应边长和各对应顶点角亏唯一确定到欧氏等距？角亏为 2π 减去该点所有面角之和，关联数据给定。

**直接证据与定位**：

- [Is a convex polyhedron determined by its edge lengths and angular defects?](https://mathoverflow.net/questions/466455/is-a-convex-polyhedron-determined-by-its-edge-lengths-and-angular-defects)：问题定义与给定组合关联的评论；作者删去的 Alexandrov 推论及更正。固定边图和对应数据；顶点角亏，不是各棱二面角。 获取状态：已打开并读取正文。审计：trace_id=`part_1/017_sources`。

**实际检索路径**：原始题页打开 → 两套学术词组：“convex polyhedron edge lengths angular defects determined rigid”；“polyhedra same graph edge lengths vertex curvatures rigidity counterexample” → GitHub/Lean 查询：“site:github.com "polyhedron" "angular defects" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "polyhedron" "angular defects"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：候选刚性文献常使用二面角或全部面角，而原题只给每顶点角亏。 下一步：逐一核候选定理的数据和组合关联；不按 rigidity 关键词推论。

#### QX-P-002020 · 版本 d18bb1af6b4fdbde

**分项结论**：投影条件被换成禁止构造方法：题面有误；符合两个投影条件的自由离散 Γ：暂未找到可验证结果。

**旧卡 → 本轮发现**：原问的投影条件应直接保留；稠密投影的非自由格只是背景反例，不能误当答案。

- P1 · 非 Schottky 构造或无法用乒乓引理的自由群 → 自由离散 Γ，而两个投影各自不同时自由且离散。

**量词与适用范围**：是否存在自由且离散的子群 Γ<SL_2(R)×SL_2(R)，使两个典范投影 π_1(Γ)、π_2(Γ) 均不同时具有“自由且离散”这两个性质？

**直接证据与定位**：

- [Are there free and discrete subgroups of SL_2(R)×SL_2(R) without free discrete projections?](https://mathoverflow.net/questions/450079/are-there-free-and-discrete-subgroups-of-mathrmsl-2-mathbbr-times-math)：原文首句；Γ_λ 动机与 SL_2(Z[√2]) 的非自由例子。两个投影都不同时自由且离散；不禁止任何可能的乘积空间构造方法。 获取状态：已打开并读取正文。审计：trace_id=`part_1/017_sources`。

**实际检索路径**：原始题页打开 → 两套学术词组：“Smilga free discrete subgroup SL2R times SL2R neither projection discrete”；“free discrete subgroup product SL2 real dense projections 2202.04027 2308.07785” → GitHub/Lean 查询：“site:github.com "SL2" "Schottky" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "free discrete" "projections"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：离散格有稠密投影不够，必须核 Γ 自由及两个投影条件。 下一步：任何候选分别核自由性、乘积内离散性和两个投影的自由/离散状态。

#### QX-P-002021 · 版本 ec137200b146945b

**分项结论**：现卡的选非交对角线优化：题面有误；inf_n nA_n 与 sup_n nA_n：暂未找到可验证结果；弱问 A_n=O(1/n)：暂未找到可验证结果。

**旧卡 → 本轮发现**：恢复所有对角线排列、边长 1 和奇数中心例外；原卡不交划分优化不是同题。

- P0 · 选一些互不相交对角线，使最大块最优 → 画全部对角线；边长 1；奇数排中心；求 nA_n 的全 n 界。

**量词与适用范围**：边长为 1 的正 n 边形画出所有对角线，A_n 为所得最大单元面积（n 为奇数时排除中心单元）。求 nA_n 随 n 的下确界与上确界；弱问是 nA_n 是否有统一上界，即 A_n=O(1/n)。

**直接证据与定位**：

- [Regular n-gon with diagonals: bounds on area of largest cell](https://mathoverflow.net/questions/436753/regular-n-gon-with-diagonals-bounds-on-area-of-largest-cell)：正文、主问与 EDIT；外侧单元面积 tan(π/n)/4。所有对角线；边长 1；奇数排除中心格；研究 nA_n 的全 n 界。 获取状态：已打开并读取正文。审计：trace_id=`part_1/017_sources`。
- [Regular polygon with diagonals: bounds on area of largest cell](https://math.stackexchange.com/questions/4593337/regular-polygon-with-diagonals-bounds-on-area-of-largest-cell)：原作者 Math.SE 交叉题正文。与 MO 同一面积问题；未取得完整上界证明。 获取状态：已打开并读取正文。审计：trace_id=`part_1/035_background_primary`。

**实际检索路径**：原始题页打开 → 两套学术词组：“regular polygon all diagonals largest cell area n inverse”；“regular n gon largest noncentral cell area diagonals asymptotic bounds” → GitHub/Lean 查询：“site:github.com "polygon" "largest cell" (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) "polygon" "largest cell"”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：固定 n 的图形和数值内切圆半径不构成单元面积的全 n 上界。 下一步：核直接面积估计与中心例外；区分半径 1 和边长 1 的缩放。

#### QX-P-001995 · 版本 e1c8bf77ee00052b

**分项结论**：所给 P_n(q) 的非负系数：暂未找到可验证结果。

**旧卡 → 本轮发现**：补回原始公式，并将现代 Borwein 结果保留为待核蕴含线索；没有可验收的 solved 状态变更。

- P1 · 只有“多项式正系数”主题 → 补全 P_n 公式、n 的范围、非负系数结论及 q-Pochhammer 记号。

**量词与适用范围**：对每个 n≥1，P_n(q)=Σ_{r=1}^n q^{r²}(q;q)_{3n−r}(q³;q³)_{r−1}/[(q;q)_r(q;q)_{2r−1}(q³;q³)_{n−r}] 是否为系数非负的多项式？须保留此明确公式及 q-Pochhammer 定义。

**直接证据与定位**：

- [Polynomials with presumably positive coefficients](https://mathoverflow.net/questions/29233/polynomials-with-presumably-positive-coefficients)：问题中的 P_n(q) 公式、互反关系、作者关于 Borwein 的评论。特定 q-超几何表达式的非负系数；相关 Borwein 猜想不自动覆盖。 获取状态：已打开并读取正文。审计：trace_id=`part_1/006_recovery`。
- [Chen–Wang: A proof of the Borwein conjecture](https://www.sciencedirect.com/science/article/abs/pii/S0001870821004679)：出版入口；本轮读取返回 403。仅作为可能相关论文线索；未取得全文，未核到本题 P_n 的等价或推论。 获取状态：原文入口 403；搜索摘要可见。审计：trace_id=`part_1/025_claims_primary`。

**实际检索路径**：原始题页打开 → 两套学术词组：“Zudilin polynomials presumably positive coefficients Borwein”；“q r squared (q;q) 3n-r (q3;q3) r-1 positive coefficients” → GitHub/Lean 查询：“site:github.com Zudilin positive coefficients (Lean OR mathlib OR formalization)” → 公开 AI 查询：“(site:zenodo.org OR site:probxiv.com OR site:mathcommunity.github.io) Zudilin Borwein positive coefficients”。关键跟进文稿和代码如上列；两次本地查重扫描及指定对子对照在 JSONL 中逐条记录。

**待复核**：Chen–Wang 原入口不可达，未读全文；原作者说相关不等于等价证明。 下一步：取得论文全文后对照 P_n 的恒等式与具体定理，给出明确代入或注明不适用。

### 查重结论

指定 6 个对子和新增同题候选均已读随包双方现版正文；没有线上合并。其他宽关键词命中仅保留索引审计，不当作等价判断。

| 主卡与版本 | 对卡与版本 | 结论 | 关键差别或同一性 |
|---|---|---|---|
| QX-P-001993 / 6949d1d8e146bbda | QX-P-001666 / dc92111bc5da9521 | 相关但不等价 | 1993 求无截面光滑真 Z-概形的最小相对维数；1666 问处处局部点但无整体点的存在性，另加局部条件且不求最小维数。 |
| QX-P-001994 / ce94070932e4310e | QX-P-002271 / bd4740ab518c054b | 相关但不等价 | 1994 是平面整圆/圆环在所有中心的满测度问题；2271 是高维 Bochner–Riesz 傅里叶乘子的估计，命题、维数和结论均不同。 |
| QX-P-001994 / ce94070932e4310e | QX-P-002358 / 4109c92b03d006f9 | 相关但不等价 | 1994 是 R² 中所有中心的整圆及满 Lebesgue 测度；2358 是 n≥4 的方向线段 Kakeya 集满 Minkowski 维数，几何对象及测度/维数结论不等价。 |
| QX-P-001995 / e1c8bf77ee00052b | QX-P-002500 / 18f9bcef315b745a | 相关但不等价 | 1995 是具体 q-多项式系数非负性；2500 是 ζ(5) 无理性及相关声明。即使出现共同作者名也不构成同题。 |
| QX-P-002015 / 0f78ce001d7fc0e8 | QX-P-001986 / 00b8701da1d461f7 | 同题 | 两卡均为 C 中仿射代数集含 Zariski 稠密 Q̄ 点则定义于 Q̄；原始交叉题均指向 MO428384/Sawin428394，现版正文均已读。 |
| QX-P-002019 / f896657197e906d5 | QX-P-002254 / 6688a12aee6911d6 | 相关但不等价 | 2019 要固定边图、边长、角亏下的凸多面体唯一性；2254 要单面型凸多面体的分类，所给数据和结论均不同。 |
| QX-P-002021 / ec137200b146945b | QX-P-001373 / 88778bbd4eedaa49 | 相关但不等价 | 2021 研究全部对角线分割的最大单元面积；1373 研究正多边形边向量随机排列形成简单多边形的概率，与该固定排列面积问题不同。 |

### 覆盖与可靠性边界

- 25/25 原始出处实际打开；25/25 各有两组独立保留的学术查询词，共 50 条基础学术查询，另有专题跟进。
- 25/25 各执行 1 条 GitHub/Lean 限定域名查询、1 条公开 AI 组合域名查询。公开 AI 查询仅限所列 Zenodo、ProbXiv、mathcommunity 入口；未宣称穷尽 aiXiv、EulerSolve、ProofForum。
- 原始 MO/必要 MSE 文本是作者问题、回答和评论的第一手记录；未把“未答”本身当作数学开放性的证明。
- 数学结果分别记录原问、子问、受限特例和辅助识别；002016 的反驳针对错误序列识别，002018 的大定理仍是声明待核。
- 全部形式化验证未运行。唯一深入读取的代码候选为 002018，固定提交和依赖已列，完整代码依赖闭包及论文所有章节待核。
- 25/25 全库出处/题号和别名匹配；6/6 指派对子完成正文对照，另新增 1 对同题。没有把标题相似判作等价。
- 403、工具 DisabledError、只有索引正文或摘要、最新版未核清的情况均保留原始返回及待办。检索结果合并返回时，query 的 URLs 明示属于整次调用清单，不伪造单条关键词专属命中。


## 第3部分：分题证据与复核事项


检查日期：2026-11-26（Asia/Shanghai）。范围：25 张指定现版题卡；只做初查，不修改线上。下列内容区别已刊结论、预印本完整声明、题面纠错与未完成复核。所有实际查询及访问失败均保留在 QX-NEW-06_逐题回传.jsonl 与 检索审计文件。

### 优先变化

#### QX-P-002033 · `99d4b41fcdf9e9f0` · 原题已证；原题已反驳；题面有误

原问光滑嵌入的清单已完整：S³ 与 S³/Q₈。Hillman 2024 原书区分 locally flat TOP 的额外 I* 情形和光滑的 Rochlin 障碍，化解旧卡所谓文献冲突；三维到 S⁴ 是余维一。

**旧卡 → 本轮变化：** 部分解决；1、Q₈ 与 1、Q₈、I* 两种转述冲突；余维二 → 原题按 smooth 分类更新为已证：仅 S³ 和 S³/Q₈；locally flat TOP 变体另含 S³/I*。修正余维为一，原问无穷多个子问为否。

**直接证据与范围：**

- [Which spherical space forms embed in the four-sphere? — 原始提问](https://mathoverflow.net/questions/219313/which-spherical-space-forms-embed-in-s4?r=31)；题面明确 spherical 3-manifolds smoothly embed in S⁴；是否有无穷多个；Agol 评论。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。
- [J. A. Hillman, Locally flat embeddings of 3-manifolds in S⁴](https://www.maths.usyd.edu.au/u/pubs/publist/preprints/2024/hillman-2.pdf)；Theorem 5.2，印刷 p.46（PDF 第52页）；印刷 p.47（PDF 第53页）I* 的 Rochlin 障碍及 Q₈ 光滑构造。finite fundamental group 的 locally flat 分类，以及光滑子类的精确删减。 访问：已打开原始全文并核所列定位；未逐行审证明。 版本：作者站 2024 版本。
- [Crisp–Hillman, Embedding Seifert fibred 3-manifolds and Sol³-manifolds in 4-space](https://www.cambridge.org/core/journals/proceedings-of-the-london-mathematical-society/article/abs/embedding-seifert-fibred-3manifolds-andsol3manifolds-in-4space/8D083D1D9DADA8C585CF238482DADC14)；期刊书目及摘要；Thm 2.2 定位由原问和作者书追溯。历史分类出处；本轮未打开 1998 正文。 访问：仅出版社检索摘要/书目；未打开 1998 期刊正文。 版本：Proc. LMS 76(3), 1998, 685–710；DOI 10.1112/S0024611598000379。

**实际搜索路径：** 原帖打开；system2 搜索 `Crisp Hillman "Embedding Seifert fibred" "2.2"` / `Crisp Hillman 1998 spherical "S3" "Q8" pdf`；代码：`site:github.com "spherical" "space forms" "embedding"`；公开 AI/社区：`"spherical" "space forms" "embedding" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** Crisp–Hillman 1998 原版只取得出版社摘要；本结论依据作者 Hillman 2024 原书的明文定理及后页光滑说明，不宣称已通读 1998 全文。 未做形式化或构造程序复算；2026 K3 ambient 的 AI 预印本检索结果与 S⁴ 不同，不用于本题结论。 未执行形式化验证；未运行检索到的外部代码。

#### QX-P-002031 · `a9f81a5fe5d46380` · 原题已证；部分进展；完整证明/反例声明待核；未作判断；题面有误

发现已刊的三维线性非消失：Müller 2025 Cor.B 已覆盖 projective klt 三维 nef 反对数典范，旧卡“仅数值、线性有效性 open”已过时。OpenAI 2026 另声称任意维数光滑 Hermitian 半正定反典范非消失，假设强于 nef，不能宣布一般原题全解。

**旧卡 → 本轮变化：** 三维数值非消失已证，而线性有效性仍 open；人话版 klt/伪有效，遗漏第二问 → 更新为 Müller 2025 三维实际线性非消失已证；保留一般维数条件范围。恢复原问光滑射影且 −KX nef，并列出 ample divisor 限制子问；2026 光滑度量半正定声明单列为加强假设。

**直接证据与范围：**

- [Non-vanishing of the anticanonical class in general dimension — 原始提问](https://mathoverflow.net/questions/231303/if-the-anticanonical-bundle-is-nef-must-it-have-an-effective-multiple?r=31)；问题 1：正倍数有截面；问题 2：某 ample divisor H 上限制有截面。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。
- [Lazić–Matsumura–Peternell–Tsakanikas–Xie, The Nonvanishing Problem for varieties with nef anticanonical bundle](https://arxiv.org/pdf/2202.13814)；Theorem A p.2、Theorem D p.3、Theorem G p.4。三维等情形的数值有效性；与实际线性非消失区分。 访问：已打开原始全文并核所列定位；未逐行审证明。 版本：arXiv v4，2023-10-10；Doc. Math. 28 (2023), 1393–1440；DOI 10.4171/DM/936。
- [Niklas Müller, Two Non-Vanishing Results Concerning the Anti-Canonical Bundle](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1E68F2B88B818A7CBD47B96B7D700548/S0027763024000217a.pdf/two_nonvanishing_results_concerning_the_anticanonical_bundle.pdf)；Theorem A p.201；Corollary B p.202；§1.2 p.203 的复数域和 Q-边界约定。Cor.B：射影 klt 三维 nef 反对数典范有正倍数截面；Theorem A：任意维数另需 MRC 一般纤维半丰沛。 访问：已打开原始全文并核所列定位；未逐行审证明。 版本：Nagoya Math. J. 258 (2025), 201–218；DOI 10.1017/nmj.2024.21；arXiv 2305.19109v3，2025-03-25。
- [OpenAI, Anticanonical nonvanishing from smooth semipositivity](https://github.com/openai/math/blob/main/preprints/Anticanonical-nonvanishing-from-smooth-semipositivity-September-26-2026/build/source/sections/introduction.tex)；Introduction, theorem label thm:headline；Geometry, monodromy, and earlier methods。任意维数、光滑连通复射影，−KX 有光滑半正定 Hermitian 度量；不是仅 nef。 访问：已取得该引言源文件全文；全证明未审、未运行，main 为可变引用。 版本：目录日期 2026-09-26；工具报告文件修改时间 2026-10-06。

**实际搜索路径：** 原帖打开；system2 搜索 `"nef anticanonical" "nonvanishing" Lazić Peternell 2025 2026` / `"nef anticanonical" "effective multiple" nonvanishing 2026`；代码：`site:github.com "anticanonical" "nonvanishing"`；公开 AI/社区：`"anticanonical" "nonvanishing" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** OpenAI 2026 原稿本轮只取得引言与主定理源文件，未逐章核证明；猜测路径 lean/docs/068.md 返回 404，不能据此断言不存在形式化。 Müller Cor.B 已刊范围确认；一般维数仅 nef 及第二问仍需后续针对性检索，不由零命中确认开放。 未执行形式化验证；未运行检索到的外部代码。

#### QX-P-002051 · `5a09d3d2ff10a284` · 完整证明/反例声明待核；未作判断；题面有误

本卡仍以 2025 评论写 F amenability“still open”，需同步 2026 的重大非 amenability 声明。已核 OpenAI family 248 原稿主定理、标准 F 定义/Comparator 和固定提交 Main.lean，并核 Kim–Lodha arXiv 原文 Thm0.1；没有重跑 Lean，故保持完整证明声明待核。原帖是后果的宽问，并非指定逆向数学子系统问题。

**旧卡 → 本轮变化：** Thompson F 仍 open；标题预设逆向数学；旧 AI 暴露中 → 背景状态更新为 2026 非 amenability 完整声明待核；交叉链接 2477，原宽问和背景定理分列。明确取得 Lean 代码但未重跑，不借第三方 verified 标签升格。

**直接证据与范围：**

- [Reverse-mathematical strength of the amenability of Thompson's group F — 原始提问](https://math.stackexchange.com/questions/198886/how-strong-is-the-statement-that-thompson-f-is-amenable)；原问 if F is amenable what would this signify；开头 Moore 证明错误说明。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。
- [OpenAI formalization coverage note 248](https://github.com/openai/math/blob/main/lean/docs/248.md)；Complete result、formalized statement 和 explicit exclusions。标准 dyadic PL F 不存在正归一化左不变均值；不提供原问未指定的 generating set/显式 boundary constant。 访问：已打开全文并与 Comparator/Main 的声明对照；未编译。
- [OpenAI Thompson F 的 Lean solution Main.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/GroupTheory/Thompson/Main.lean)；OAI.ThompsonNonamenability.thompson_F_nonamenable_composition；thompson_F_not_amenable。标准 dyadic PL group 的非 amenability；imports StandardCharacterization、FiniteBoundary、AnalyticConstruction、MeanToFolner。 访问：已取得代码并核顶层定理对应、未重跑；依赖闭包未逐项审核。 版本：固定提交 adc7f1241b42e322a6451854ab7e4b4c146bf78a；Main 路径提交 API 返回 2026-10-06。
- [OpenAI, Thompson’s group F is nonamenable](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Thompsons-group-F-is-nonamenable-September-23-2026/build/sections/introduction.tex)；Introduction，主定理 thm:main；定量陈述的量词说明。F 非 amenable；先固定有限 S 再对任意有限 A 给 expansion。 访问：已取得引言源文件；主证明全篇未深审，GitHub PDF 页面并未给出可读 PDF 正文。 版本：固定提交 adc7f1241b42e322a6451854ab7e4b4c146bf78a。
- [Sang-hyun Kim–Yash Lodha, A note on the proof of nonamenability of F](https://arxiv.org/pdf/2610.18360)；Theorem 0.1 p.1；同页与 OpenAI 的关系说明；§2 证明。标准 F 非 amenable；作者自述同一想法的人类精简写法、本文写作无 AI。 访问：已打开全文、核定义与主定理；未独立审完整证明。 版本：2610.18360v1，2026-10-13。
- [ThompsonNonamenability Comparator 配置](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ThompsonNonamenability.json)；solution_module、theorem_names、permitted_axioms、enable_nanoda。声明连接到 Main；配置允许 propext、Quot.sound、Classical.choice，enable_nanoda=false。 访问：已取得固定提交 JSON；未运行 comparator 或 nanoda。

**实际搜索路径：** 原帖打开；system2 搜索 `"Thompson" "amenable" "reverse mathematics"` / `"Moore" "Thompson" "amenability" retracted withdrawn proof`；代码：`site:github.com "Thompson" "nonamenable"`；公开 AI/社区：`"Thompson's group F is nonamenable" site:github.com/openai/math`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** 尚未独立重跑 Lean 或审全部 imported dependencies；Comparator 配置仅列 propext、Quot.sound、Classical.choice，不等于本轮已核公理闭包。 Main.lean 无 sorry 不足以独立保证整体通过；challenge 模板中的 sorry 为待替换目标，不能单凭此判最终解答有占位。 lean/docs/248.md 不提供指定生成集或显式边界常数，不能移用于其他定量/显式构造题；Kim–Lodha 自述同一思路，不能称完全独立证实。 已取得代码、已核顶层定理与标准 F 对应，未重跑；未审进口依赖闭包，未作独立通过结论。

**指定查重：** QX-P-002151（bdbbe7ee3e44ce36）：相关但不等价，2151 要 F 的具体悖论分解，属于非 amenability 后的显式构造问题；2051 原帖宽问假设 amenability 的后果。非 amenability 的存在性声明不自动提供指定显式分解。；QX-P-002386（ce0de649f367f1eb）：相关但不等价，2386 为 Thompson F 是否 automatic（Kourovka 21.143）；自动结构与 amenability 的问题不同。；QX-P-002477（45caaca857ed42f7）：相关但不等价，2477 已记录 OpenAI 2026 非 amenability 证明声明及核验；2051 原问是假设 amenability 的后果。应交叉链接并同步背景，不能合并软问题与“一题一验”的证明审查。。

#### QX-P-002046 · `1e7d4cf5d265032a` · 完整证明/反例声明待核；题面有误

取得 Suvrit Sra 的 2026 完整证明稿，Theorem 1.1/Corollary 1.2 明确涵盖原题，且声明 OpenAI GPT Pro 协作；原帖 jvvk 回答也明示 Claude 帮助。维持完整证明声明待核，同时修正旧卡“AI 暴露=无”及具体对称多项式表述。

**旧卡 → 本轮变化：** 仅有 jvvk 未验证回答；具体比值缺失；AI 暴露=无 → 补 Sra 2026 原稿、精确 Theorem 1.1/Cor.1.2 和特殊矩形分拆常数情形；维持声明待核，AI 来源分别记录 Claude 和 OpenAI GPT Pro 自述。

**直接证据与范围：**

- [Is the ratio of two symmetric polynomials monotone? — 原始提问](https://mathoverflow.net/questions/467261/monotonicity-of-ratio-of-symmetric-polynomials)；题面 Hᵢ 与 Ψᵢ,ₙ；jvvk 回答末段 Claude 帮助声明。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。
- [Suvrit Sra, Monotonicity of Turán-ratios of symmetric polynomials](https://hexagonmath.org/pdf/2610.00720v1)；Theorem 1.1、Corollary 1.2，p.1；Lemma 2.1、§2.2；§3 单行情形。Schur 分拆 λ₁>λₙ、x>1、1≤i<n；矩形 λ=(rⁿ) 为常数 1；单行 λ=(ℓ) 涵盖原题。 访问：已打开原始全文并核所列定位；未逐行审证明。 版本：Hexagon 2610.00720v1，页面版本日期 2026-11-02。
- [Sra 论文的版本和 provenance 页面](https://hexagonmath.org/2610.00720v1)；版本历史；AI provenance 栏。作者声明 OpenAI GPT Pro 数学协作；与原帖 Claude 帮助为两条来源。 访问：已打开页面，来源自述未作外部身份核验。
- [Suvrit 作者仓库固定提交的 sym-turan-v1.pdf](https://github.com/suvrit/preprints/blob/8c491b589dafa24f67e12c9edb030e4c6e508725/preprints/sym-turan/v1/sym-turan-v1.pdf)；preprints/sym-turan/v1；提交 8c491b589dafa24f67e12c9edb030e4c6e508725。固定论文版本；未发现本次取得材料中的 Lean 定理。 访问：已核 commits API 与目录文件；PDF 正文在 Hexagon 阅读，未执行 .ots 或代码。 版本：路径最近提交 2026-10-08；作者页面发布标注 2026-10-07。

**实际搜索路径：** 原帖打开；system2 搜索 `"Monotonicity of ratio of symmetric polynomials"` / `"Turán-ratios" "Meixner" Sra`；代码：`site:github.com "monotonicity" "Turan" "symmetric"`；公开 AI/社区：`"monotonicity" "Turan" "symmetric" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** Sra 的 Toda/max-principle 及 Meixner 两条论证尚未独立逐步核验；无 Lean 验证。 作者仓库的 .ots 文件只是时间戳材料，不能当数学证明；原帖计算范围和论文代码均未重跑。 未执行形式化验证；未运行检索到的外部代码。

#### QX-P-002049 · `6b8fcddb0dd2bba0` · 完整证明/反例声明待核；原题已证；题面有误

已把 Li–Zhan 2026 原稿的精确 Corollary 3 与原帖对应：n≥6 的无向 Hamilton 路径最大数 (n−2)!，有向计数为 2(n−2)!，极值图为 Kₙ₋₁ 加一悬挂点。n=3,4,5 已由本轮自写有限穷举补核；完整一般证明仍作预印本声明待核。

**旧卡 → 本轮变化：** 仅摘要层未知公式是否等于 OP 的 2(n−2)!；计数方向未明 → 记录 Cor.3 的精确公式、n≥6 范围、极值图与方向因子 2；补本轮 n=3..5 的独立有限穷举。维持一般证明的预印本待核层级。

**直接证据与范围：**

- [Maximum number of Hamiltonian paths in an n-vertex graph with no Hamiltonian cycle — 原始提问](https://math.stackexchange.com/questions/914345/how-many-hamilton-paths-can-a-non-hamiltonian-graph-have)；原问题及 Erick Wong/OP 评论确认 ordered paths。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。
- [Chengli Li–Xingzhi Zhan，非 Hamilton 图中指定长度路径数的极值](https://arxiv.org/html/2605.26479v1)；Theorem 2；Corollary 3；极值图 Kₙ₋₁·K₂ 定义。n≥6、1≤k≤n−1；k=n−1 给原题无向公式，乘 2 对应 ordered 计数。 访问：已打开原始全文并核所列定位；未逐行审证明。 版本：arXiv 2605.26479v1，2026-05-26。
- 本轮自写枚举：n=3,4,5 的非 Hamilton 简单图（local:part_2/finite_2049.json）；finite_2049.json；finite_2049_reproduce.py。只验证三个 n，全部标号简单图；不是外部代码或形式化证明。 访问：实际运行完成；结果文件保留，未跑 Lean。

**实际搜索路径：** 原帖打开；system2 搜索 `"2605.26479" non-Hamiltonian paths` / `"nonhamiltonian" "Hamilton paths" "Li" "Zhan" 2026`；代码：`site:github.com "nonhamiltonian" "paths"`；公开 AI/社区：`"nonhamiltonian" "paths" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** Li–Zhan arXiv v1 的全证明未独立审查，未见本轮可核正式发表或勘误；不把有限穷举说成一般 n 的验证。 未执行 Lean 等形式化验证；仅运行本轮自写的 n=3,4,5 有限穷举，没有运行未审查外部代码。

#### QX-P-002052 · `0162577235db0ea7` · 暂未找到可验证结果；题面有误

恢复原帖被截断的最终问题：Tango 丛 F 是否同构于 N(1)。原文给 F 的完整余核序列；未扭转 F 的 c₁=2h，N 的 c₁=0，旧卡“c₁=0 一致”把归一化混淆。

**旧卡 → 本轮变化：** 最终问题缺失；N 与 Tango 都 c₁=0 → 写回 F 的序列 0→O→Λ²T(−2)→F→0 和问题 F≅N(1)；c₁(F)=2h，区分 F 与 F(−1)，保留截面/辛形式选择。

**直接证据与范围：**

- [Null-correlation bundles and Tango bundles on P^3 — 原始提问](https://math.stackexchange.com/questions/1606113/null-correlation-and-tango-bundles-on-mathbbp3)；两条定义正合列及最后问句 F≅N(1)。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。

**实际搜索路径：** 原帖打开；system2 搜索 `"Tango bundle" "null-correlation" "P3"` / `"Tango bundles" "null correlation" twist rank two`；代码：`site:github.com "null correlation" "Tango"`；公开 AI/社区：`"null correlation" "Tango" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** 下一步应核映射对应及不同无零截面的 moduli，而非只比秩/Chern 类；本轮未取得精确同构论证的原始文献全文。 未执行形式化验证；未运行检索到的外部代码。

#### QX-P-002039 · `4c9986227a01d647` · 暂未找到可验证结果；题面有误

原帖两问及其修正归一化已恢复。旧卡把 Re s=0 直接归结为已知自然边界缺乏本轮可核原文；原帖评论明确指出仅在 0 聚集的奇点不能证明整条直线为自然边界。

**旧卡 → 本轮变化：** 只保留普通 Dirichlet 级数延拓，并把自然边界作为确定事实 → 恢复两问及 digamma 归一化；将“Estermann 已处理”改为待核文献线索，区分 κ、log κ 与 prime zeta。

**直接证据与范围：**

- [Analytic continuation of the Dirichlet series of the multiplicative partition function — 原始提问](https://mathoverflow.net/questions/123571/analytic-continuation-of-the-dirichlet-generating-series-of-the-multiplicative-p)；κ 的 Euler product、两问、digamma 归一化；Greg Martin/Loïc Teyssier 评论。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。
- [Kaneiwa, On the multiplicative partition function](https://barrel.repo.nii.ac.jp/record/2137/files/Tsukubajmath7%282%29_355-365.pdf)；Tsukuba J. Math. 7(2), 1983, 355–365；仅检索/仓储入口。需核其实际研究范围；本轮不引用为延拓或自然边界定理。 访问：打开返回 HTTP 429；未获全文。

**实际搜索路径：** 原帖打开；system2 搜索 `"multiplicative partition" "Dirichlet" "continuation"` / `"zeta(ks)" "natural boundary" product partitions`；代码：`site:github.com "multiplicative partition" "continuation"`；公开 AI/社区：`"multiplicative partition" "continuation" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** Kaneiwa 1983 原稿 URL 打开返回 HTTP 429；未读正文，不能定位自然边界定理。 Hexagon 2611.00262v1 页面讨论 prime zeta 的相邻论述，不等同本 κ；未将其当作证明。 未执行形式化验证；未运行检索到的外部代码。

**指定查重：** QX-P-002478（75ff62b0e87f0fe1）：相关但不等价，2478 为有限三项复指数和 2^(−1−it)+3^(−1−it)+5^(−1−it) 的实 t 零点；2039 为无限 Euler product 的解析延拓。有限/无限、零点/边界延拓不同。。

### 其余会影响题意或证据范围的校准

#### QX-P-002025 · `6162792a082e281f` · 暂未找到可验证结果；题面有误

原帖问每个给定不可约表示能否由单个类和的特征值从所有其他表示中分离。旧人话版改成多个共轭类的特征标串，量词及归一化均变。2026 年相关论文讨论多个类和联合分离，未据此验证原题全解。

**旧卡 → 本轮变化：** 人话版称“给定几个共轭类看一串特征标值” → 改为对每个 V，问是否存在一个 C，使 |C|χ_V(C)/dim(V) 与所有其他不可约表示的对应值不同；单类同时分离全部表示作为另一个更强问题。

**直接证据与范围：**

- [Uniqueness of character spaces for classes of the symmetric group — 原始提问](https://mathoverflow.net/questions/343742/which-irreducible-representations-of-the-symmetric-group-are-eigenspaces-of-clas)；题面 λ(C,V) 定义及末段两个问题。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。
- [Kemp–Ramgoolam, Gauge-string duality, monomial bases and graph determinants](https://arxiv.org/pdf/2603.05259)；引言 pp.3–4；Appendix A。T₂ 与 T₃ 等多个类和联合区分表示；不能代替原题的单类量词。 访问：已打开原始全文并核所列定位；未逐行审证明。 版本：2603.05259v2，2026-03-07。

**实际搜索路径：** 原帖打开；system2 搜索 `"class sums" "eigenspaces" "symmetric group" representations` / `"symmetric group" "normalized characters" distinguish irreducible conjugacy class`；代码：`site:github.com "class sums" "eigenspaces"`；公开 AI/社区：`"class sums" "eigenspaces" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** 需查单类分离问题是否有全 n 分类或反例；2026 论文 Appendix A 的 SAGE 未运行。 未执行形式化验证；未运行检索到的外部代码。

**指定查重：** QX-P-002115（a3b0771e26a17812）：相关但不等价，2025 是有限群类和在不可约表示上的标量分离；2115 是 Riemannian covering 的 Laplace 谱间隙。仅“特征值”共同词，量词、对象和结论不同。。

#### QX-P-002026 · `1a5ebabaf613134c` · 暂未找到可验证结果；部分进展；题面有误

已恢复同一 4 维流形 X 的标准 double 与边界扭接 double 比较。Melvin–Schwartz 原稿 Cor.1.17 连接 AC cork 的扭倍与任意同伦 4 球；它没有无条件给出原题要求的 exotic 扭倍。

**旧卡 → 本轮变化：** 人话版对 exotic twisted double 的构造和比较对象失真 → 写明 DX=X∪id(−X)、DXτ=X∪τ(−X)，τ 可延拓成同胚而不可延拓成微分同胚；比较两者微分同胚类型。原作者应为 Kyle Hayden。

**直接证据与范围：**

- [Do exotic twisted doubles of four-manifolds exist? — 原始提问](https://mathoverflow.net/questions/320319/are-there-exotic-twisted-doubles-of-4-manifolds)；题面 DX 与 DX_τ 的定义，τ 延拓条件；Kyle Hayden 原问。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。
- [Melvin–Schwartz, Higher order corks](https://arxiv.org/pdf/1902.02840)；Remark 1.2(b) p.3；Corollary 1.17 p.8。AC cork 标准 double 与同伦球的扭倍表示；不是原题无条件构造。 访问：已打开原始全文并核所列定位；未逐行审证明。 版本：1902.02840v2，2020-11-28。

**实际搜索路径：** 原帖打开；system2 搜索 `"exotic twisted doubles" 4-manifolds corks` / `"Higher order corks" "1.17" twisted double`；代码：`site:github.com "exotic" "twisted doubles"`；公开 AI/社区：`"exotic" "twisted doubles" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** 尚未核得全题的具体 exotic 例子或不存在定理；不把 smooth Poincaré 的声明直接代入一般 X。 未执行形式化验证；未运行检索到的外部代码。

**指定查重：** QX-P-002080（284ef83bf653d0c9）：相关但不等价，2080 问 S²×S² 的 exotic 光滑结构存在性；2026 要同一 X 的标准/扭接 double 并满足边界延拓条件，不能从一般 exotic 结构存在直接推出。；QX-P-002469（cc4ede605134dba2）：相关但不等价，2469 核 smooth 4D Poincaré 的全称声明；2026 允许一般 4-manifold 的 doubles。AC cork 子类由 Cor.1.17 与同伦球相连，但不构成一般两题等价。；QX-P-002471（6a19322796118183）：相关但不等价，2471 为 smooth Schoenflies：S³⊂S⁴ 两侧是否标准 B⁴；2026 是预先指定 X 及边界 τ 的双倍光滑类型比较。。

#### QX-P-002027 · `96b68fa3af214c4b` · 暂未找到可验证结果；题面有误

原题是具体 Legendre 符号矩阵 A_p 的 −det(A_p) 是否总为奇平方，不是把素数 p 表示为某种行列式。恢复首行例外至关重要；本轮未找到对该精确矩阵可核的后续全解。

**旧卡 → 本轮变化：** 人话版把问题改为素数的行列式表示 → 逐项写回 n=(p−1)/2，首行 a₁ⱼ=(j/p)，其余 aᵢⱼ=((i²+j²)/p)，问 −det A_p 为奇平方。

**直接证据与范围：**

- [A determinant problem for primes congruent to 1 modulo 4 — 原始提问](https://mathoverflow.net/questions/310301/a-determinant-problem-for-primes-p-equiv-1-pmod4)；题面 A_p 的分段定义及 −det(A_p) 猜想。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。

**实际搜索路径：** 原帖打开；system2 搜索 `Sun determinant "i^2+j^2" "odd square"` / `"310301" determinant Yang Zhang`；代码：`site:github.com "determinant" "odd square" "Sun"`；公开 AI/社区：`"determinant" "odd square" "Sun" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** 旧备注涉及 Yang–Zhang 2026 的邻近矩阵，本轮未取得该文原稿，不能把其结论移植；需以首行例外和平方项逐式核对。 未执行形式化验证；未运行检索到的外部代码。

#### QX-P-002028 · `2863b7738cc0785f` · 暂未找到可验证结果

原问的难点包含严格的 κ⁺ 链条件以及同一次扩张中的基数、共尾数和 GCH 条件。κ⁺⁺-cc 或单独改变共尾数的相邻结果不能回答该组合。

**旧卡 → 本轮变化：** “良好 forcing”未明确链条件及需要同时满足的条件 → 题面写回 V₁ 中 κ 不可达、V₂ 为 κ⁺-cc 扩张、κ 在 V₂ 中为 ℵω、κ 以下 GCH 与 κ 处失败；不能用 κ⁺⁺-cc 替换。

**直接证据与范围：**

- [Forcing GCH to fail at aleph_omega — 原始提问](https://mathoverflow.net/questions/287362/the-failure-of-gch-al-aleph-omega-by-nice-forcing)；原题 V₁、V₂、κ 与链条件的条目。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。
- [Benhamou–Poveda, Non-Normal Magidor-Radin Types of Forcings](https://arxiv.org/abs/2405.16704)；摘要及版本历史。共尾数及 Cohen 子集的邻近 forcing 构造；本轮未核得与目标组合等价。 访问：已打开摘要和版本页；未读全文。 版本：2405.16704v1，2024-05-26。

**实际搜索路径：** 原帖打开；system2 搜索 `"GCH" "aleph_omega" "kappa^+" forcing chain condition` / `"2405.16704" Prikry chain condition`；代码：`site:github.com "GCH" "aleph" "chain condition"`；公开 AI/社区：`"GCH" "aleph" "chain condition" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** 2405.16704 只核摘要与版本；若作为解答需再核具体 forcing 的 κ⁺-cc 和全部基数算术条件。 未执行形式化验证；未运行检索到的外部代码。

#### QX-P-002029 · `a2e4923bcf2888a8` · 暂未找到可验证结果；题面有误

原题的全称量词是每个 powerful n>1 都可写成另一个 powerful 数加素数，允许 powerful 数 1。旧人话版只问存在或无穷多对，明显较弱。Paparella 2019 的出版社页面把相关内容列作猜想，原稿 PDF 未能访问。

**旧卡 → 本轮变化：** 题名/人话版侧重存在一对或无穷多对 → 明确“每个 n>1”及 m=1 允许，并将任何数值范围写为作者报告而非本轮复算。

**直接证据与范围：**

- [Can the difference of two powerful numbers be prime? — 原始提问](https://mathoverflow.net/questions/269080/is-every-powerful-number-the-sum-of-a-powerful-number-and-a-prime?noredirect=1)；题面首段及关于 1、计算和 Hardy–Littlewood 的评论。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。
- [Paparella, Eisenstein’s criterion, Fermat’s last theorem, and a conjecture on powerful numbers](https://nntdm.net/volume-25-2019/number-2/22-29/)；出版社摘要；参考文献 [3] 指向 MO269080；pp.22–29。同题猜想的文献出处；本轮不将其当作已证成果。 访问：已打开出版社摘要/参考文献；PDF 超时，arXiv PDF 不可达。 版本：NNTDM 25(2), 2019；DOI 10.7546/nntdm.2019.25.2.22-29。

**实际搜索路径：** 原帖打开；system2 搜索 `"powerful number" "sum" "prime" Paparella conjecture` / `"Eisenstein’s criterion, Fermat’s last theorem, and a conjecture on powerful numbers"`；代码：`site:github.com "powerful number" "prime"`；公开 AI/社区：`"powerful number" "prime" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** Paparella PDF 与 arXiv PDF 均未成功获取；具体猜想编号仅摘要检索线索，尚不能作正文定理定位。 未执行形式化验证；未运行检索到的外部代码。

#### QX-P-002030 · `ae58e8b2836f0f11` · 原题已证；部分进展

已核 type A 的已刊证明范围；它不能覆盖任意有限 Coxeter 群。旧卡的进展方向正确，需把 θ 的幂所作用的次数及 Sn 的限制写清，并删去未经支持的“三篇独立”描述。

**旧卡 → 本轮变化：** A 型结论与一般有限 Coxeter 群表述容易混列；“三篇独立论文”未核实 → 保留 A 型已证，并将一般 W 单列；书目写全作者与正式期刊版本。

**直接证据与范围：**

- [Hard Lefschetz for nilCoxeter algebras beyond type A — 原始提问](https://mathoverflow.net/questions/260020/a-hard-lefschetz-theorem-for-nilcoxeter-algebras)；题面 θ^(N−2i):N(W)i→N(W)N−i；Speyer 后续评论。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。
- [Hamaker–Pechenik–Speyer–Weigandt, Derivatives of Schubert polynomials and proof of a determinant conjecture of Stanley](https://arxiv.org/pdf/1812.00321)；Proposition 1、Theorem 2，p.2。Sₙ/type A 的加权弱序行列式及 nilCoxeter Lefschetz 子问。 访问：已打开原始全文并核所列定位；未逐行审证明。 版本：Algebraic Combinatorics 3 (2020), 301–307；DOI 10.5802/alco.93。

**实际搜索路径：** 原帖打开；system2 搜索 `nilCoxeter Lefschetz other Coxeter types 2025 2026` / `"1812.00321" "1811.05501" nilCoxeter`；代码：`site:github.com "nilCoxeter" "Lefschetz"`；公开 AI/社区：`"nilCoxeter" "Lefschetz" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** 一般有限 Coxeter 类型是否已有后续全解，本轮列出的入口未核到；未运行原稿或仓库中的计算代码。 未执行形式化验证；未运行检索到的外部代码。

#### QX-P-002032 · `f80f27afc7d1fa2d` · 暂未找到可验证结果；题面有误

原问是完整面格的组合自同构是否与对跖映射交换。边图的反例确已找到，但不能当作原题反例；旧人话版也不能把该命题写成每个顶点只能映到自身或其负点。

**旧卡 → 本轮变化：** 人话版弱化/误写自同构与对跖的关系 → 明确完整面格组合自同构以及 f∘(−id)=(−id)∘f；不得以边图反例或逐点 ±v 替代。

**直接证据与范围：**

- [Do automorphisms of symmetric polytopes respect antipodal pairs? — 原始提问](https://mathoverflow.net/questions/223642/is-combinatorial-automorphism-of-symmetric-convex-polytope-always-antipodal)；题面 f(−v)=−f(v)；Perles/Stanley 注释。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。
- [David E Speyer：中心对称多面体边图的非对跖自同构反例](https://mathoverflow.net/questions/440534/does-the-edge-graph-of-a-centrally-symmetric-polytope-determine-which-vertices-a/440823)；回答 440823，R⁴ 对称矩曲线上的 12 顶点构造。只处理 edge graph，未核为完整 face lattice 自同构。 访问：已打开回答全文；未执行构造代码。

**实际搜索路径：** 原帖打开；system2 搜索 `"Perles" "centrally symmetric" automorphism polytope` / `"antipodal" "combinatorial automorphism" polytope counterexample`；代码：`site:github.com "polytope" "antipodal" "automorphism"`；公开 AI/社区：`"polytope" "antipodal" "automorphism" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** 需取得 Kalai ICM 1994 对 Perles 问题 对完整面格问题的精确原文；Speyer 2023 构造未运行，只作为已读社区数学论证的边图变体。 未执行形式化验证；未运行检索到的外部代码。

**指定查重：** QX-P-002360（3d372a96094424a0）：相关但不等价，2360 是中心对称 d-polytope 的 Kalai 3^d 面数下界；2032 问面格自同构是否与对跖交换，数量不等式与群作用性质不同。。

#### QX-P-002035 · `0374791b3db9c90e` · 暂未找到可验证结果；原题已反驳；题面有误

原问允许任意序数长度的链；旧人话版把它写成可数 H₁⊂H₂⊂⋯，把难点丢掉。小于 cov(B) 的链已有否定结果，不能推出任意长度的否定。

**旧卡 → 本轮变化：** 人话版只展示可数递增链并当作原问 → 恢复 α<δ 的任意序数链；将已知短链结果与附加商群条件单列。

**直接证据与范围：**

- [Is Z^omega a union of a strictly increasing chain of proper copies of itself? — 原始提问](https://mathoverflow.net/questions/182326/is-mathbbz-omega-ever-the-union-of-a-chain-of-proper-subgroups-each-isom)；题面 Gα (α<δ) 与 δ 的说明；Blass–Irwin 评论。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。
- [Oren Kolman, Strong subgroup chains and the Baer-Specker group](https://arxiv.org/pdf/0901.2291)；引言 pp.1–2，Blass–Irwin 结果及 quotient 条件。<cov(B) 的链及更强 quotient 条件；不自动给出一般原题结论。 访问：已打开原始全文并核所列定位；未逐行审证明。 版本：arXiv 0901.2291；Groups and Model Theory (2008), 187–198；DOI 10.1515/9783110203035.187。

**实际搜索路径：** 原帖打开；system2 搜索 `"Blass" "Irwin" "Baer-Specker" chain` / `"Strong subgroup chains" "Baer-Specker" Kolman`；代码：`site:github.com "Baer-Specker" "chain"`；公开 AI/社区：`"Baer-Specker" "chain" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** 一般 δ 且仅每项同构 Z^ω 的结论本轮未核得；不得把 cotorsion-free 商群性质当作自动满足。 未执行形式化验证；未运行检索到的外部代码。

#### QX-P-002036 · `9d659963adbc713b` · 暂未找到可验证结果；题面有误

原问要一个 Hausdorff 维数 1 的实数加法子群，其所有子群维数只能为 0 或 1。旧人话版关于构造各种维数子群并非此问；Borel 子环的 0–1 结论也不能套用到任意加法子群。

**旧卡 → 本轮变化：** 人话版以普通 Hausdorff 维数实现问题取代对子群谱的限制 → 写明 dim_H G=1，∀H≤G，dim_H H∈{0,1}，并区分 ZFC 与 CH 条件结果、加法子群与子环。

**直接证据与范围：**

- [Which Hausdorff dimensions can real additive subgroups have? — 原始提问](https://mathoverflow.net/questions/171428/are-there-additive-subgroups-of-reals-of-dimension-1-with-no-subgroups-of-dimens)；题面 ZFC、dim G=1 与所有 H≤G 的维数限制；CH 注释。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。
- [J. Beck, A Very Sparse Set of Dimension 1](https://www.cambridge.org/core/journals/mathematika/article/abs/very-sparse-set-of-dimension-1/0A7AABF795EA68B152D8CA1E347AF414)；出版社摘要检索结果。维数 1 紧集生成的子群不等于 R；并非排除所有中间维子群。 访问：仅检索摘要；未打开全文。

**实际搜索路径：** 原帖打开；system2 搜索 `"Erdős" "Volkmann" subgroup "no subgroups" dimension` / `"A Very Sparse Set of Dimension 1" Beck ZFC`；代码：`site:github.com "additive subgroup" "Hausdorff dimension"`；公开 AI/社区：`"additive subgroup" "Hausdorff dimension" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** Beck 全文未打开；本轮只有出版社检索摘要，不能据此判原题已证。 指定参考卡 2169、2177 缺少其所称问题的完整形式，查重保留待定，不能仅凭标题作同题判断。 未执行形式化验证；未运行检索到的外部代码。

**指定查重：** QX-P-002169（d807a40adc752ec7）：待定，2169 的参考卡仅称 Hausdorff gauge 函数取值的四个问题，未给四问完整形式。可见内容与实加法子群谱不同，但材料不足以作严格同题/不同题最终判定。；QX-P-002177（393d712b851e12d0）：待定，2177 为某树原则的 Hausdorff dimension 版本，参考题面缺少完整原则及量词。标题相似不足以判与实加法子群的中间维排除等价。；QX-P-002183（062bfae24d996910）：相关但不等价，2183 讨论 profinite 群的维数类实现及描述复杂度；2036 是 R 的加法子群及其所有子群维数。ambient 群、度量和目标性质不同；参考卡细节未外部深核。。

#### QX-P-002037 · `abd6348e0d797cd8` · 暂未找到可验证结果；题面有误

原题是严格包含意义下的单调注入，而非把树边映到超立方体的一条边；一次下降可以添加多个坐标。旧人话版的图嵌入版本改变问题。

**旧卡 → 本轮变化：** 人话版把 monotone embedding 当成树的边嵌入 → 改为单射 f，若 v 为 u 的子节点，则 supp f(u) 严格包含于 supp f(v)；保留一次可增加多个坐标。

**直接证据与范围：**

- [Monotone embeddings of complete binary trees into hypercubes — 原始提问](https://mathoverflow.net/questions/168099/monotone-embedding-of-complete-binary-tree-in-hypercube?noredirect=1)；题面 monotone embedding 定义及 n(d) 界。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。

**实际搜索路径：** 原帖打开；system2 搜索 `"Monotone embedding" "complete binary tree"` / `"binary tree" "Boolean lattice" "1.29" embedding`；代码：`site:github.com "monotone" "binary tree" "hypercube"`；公开 AI/社区：`"monotone" "binary tree" "hypercube" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** 原帖的有限计算和常数界未独立复算；精确渐近常数仍需后续文献核查。 未执行形式化验证；未运行检索到的外部代码。

#### QX-P-002038 · `f90af92266bbd252` · 暂未找到可验证结果；题面有误

原问固定协方差为单位阵，研究超平面投影体积与本体积之比的维数无关上界。人话版变成体积归一化下的任意 k 维投影，不能据此引用不同归一化的结果。

**旧卡 → 本轮变化：** 只固定体积并泛称低维投影 → 恢复协方差归一化及 inf_u |proj_{u⊥}B|/|B|；问题是所得 c_d 能否一致有界。

**直接证据与范围：**

- [Order of magnitude of the minimal projection area of a convex body — 原始提问](https://mathoverflow.net/questions/155728/how-large-are-the-smallest-area-projections-of-a-high-dimensional-convex-body?noredirect=1)；题面 isotropic 条件、inf 投影比以及 dimension independent 问句。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。

**实际搜索路径：** 原帖打开；system2 搜索 `"isotropic convex body" "minimal projections" volume` / `"covariance" "projection volume" convex body dimension independent`；代码：`site:github.com "isotropic" "projections" "convex"`；公开 AI/社区：`"isotropic" "projections" "convex" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** 旧卡提及 arXiv math/9201204 的结论本轮未取得原文核对，不将其当作已验反例。 检到 isotropic constant 的 AI 目录线索，其结论不是该投影比命题；未核得推导，不能宣告原题解决。 未执行形式化验证；未运行检索到的外部代码。

#### QX-P-002041 · `951f6ac17dc0b9ad` · 暂未找到可验证结果；部分进展

复二维稠密与实平面区域稠密必须分开。Ok–Perrett 原稿提供实 (q,v) 平面多个区域的定理；正实象限无零点并不能否定复 C² 稠密。

**旧卡 → 本轮变化：** 旧备注“Ok 2016 部分区域稠密”未给实坐标、定理与区域定位 → 补 Ok–Perrett Theorem 1.2 p.3 的实 (q,v) 坐标范围；与复 C² 主问分列。正实象限的排除只解释实域，不自动排除复稠密。

**直接证据与范围：**

- [Are the zeros of the Tutte polynomial dense in C^2? — 原始提问](https://mathoverflow.net/questions/103491/are-the-zeros-of-tutte-polynomials-dense-in-mathbb-c2)；题面 C² 问句及实数版本讨论。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。
- [Ok–Perrett，Tutte 多项式实零点稠密性](https://arxiv.org/pdf/1608.08747)；Theorem 1.2 p.3；Figure 1 与紧接未覆盖区域说明。仅实 (q,v) 平面的指定区域；不能回答 C² 全域稠密。 访问：已打开原始全文并核所列定位；未逐行审证明。 版本：arXiv 1608.08747v1 版本入口；已核出版社题名 Density of Real Zeros of the Tutte Polynomial。

**实际搜索路径：** 原帖打开；system2 搜索 `"Tutte polynomial" "zeros" "dense" "complex"` / `"Ok" "2016" "Tutte" "zeros"`；代码：`site:github.com "Tutte" "zeros" "dense"`；公开 AI/社区：`"Tutte" "zeros" "dense" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** 复二维命题本轮未核到直接全解；不能用实域零点分布替代。 未执行形式化验证；未运行检索到的外部代码。

#### QX-P-002042 · `2d08120d028d0000` · 暂未找到可验证结果；题面有误

Hartshorne 的原问题是 P³ 中闭不可约曲线是否总是两张曲面的集合论交，不是一般光滑仿射子簇的连通性/完全交问题。原帖还明确请求 2020 年以后的进展。

**旧卡 → 本轮变化：** 旧题意混入一般仿射情形/连通性 → 按 Hartshorne I.2.17：P³ 中闭不可约曲线，是否是两曲面的集合论交；保留原帖请求 2020 年后文献的意图。

**直接证据与范围：**

- [Hartshorne's set-theoretic complete intersection question (corrected form) — 原始提问](https://mathoverflow.net/questions/511340/progress-on-a-two-star-problem-of-algebraic-geometry-by-robin-hartshorne?r=31)；Hartshorne I.2.17 双星问题的原句及时间范围。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。

**实际搜索路径：** 原帖打开；system2 搜索 `"Hartshorne" "I.2.17" "set-theoretic" 2026` / `"space curves" "set-theoretic complete intersections" progress 2024 2025 2026`；代码：`site:github.com "space curves" "set-theoretic"`；公开 AI/社区：`"space curves" "set-theoretic" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** 检到关于 primitive complete intersections 的相邻稿件未打开全文，不作全题解决依据；需进一步核最新综述及特征假设。 未执行形式化验证；未运行检索到的外部代码。

#### QX-P-002043 · `0ff7d690949d31ed` · 暂未找到可验证结果；未作判断；题面有误

原问是是否可能由加入一个 Cohen real 创造 Kurepa 树，及小 forcing 的更一般版本；它没有断言每次 Cohen 扩张都增加。weak Kurepa 与 Kurepa、特殊模型中的保持结论都必须分开。

**旧卡 → 本轮变化：** 人话版可能将 can 改为必然，或混用 weak Kurepa → 题面保留存在性与原始树定义，并把一般 size κ 的子问单列。

**直接证据与范围：**

- [Does a Cohen extension add a Kurepa tree? — 原始提问](https://mathoverflow.net/questions/492088/can-a-cohen-real-add-a-kurepa-tree)；题面 V 无 Kurepa，V[c] 是否可能有；size κ 的概括。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。
- [Honzík–Stejskalová, Generalized cardinal invariants for an inaccessible κ with compactness at κ⁺⁺](https://arxiv.org/abs/2308.13478)；摘要及版本历史。weak Kurepa 的特定模型结论；不是单个 Cohen real 对普通 Kurepa 的全面判定。 访问：已打开摘要和版本页；未读正文。 版本：v2，2025-04-25，27 pp.。

**实际搜索路径：** 原帖打开；system2 搜索 `"Cohen" "Kurepa" "2308.13478"` / `"Can a Small Forcing Create Kurepa Trees" Jin Shelah`；代码：`site:github.com "Cohen" "Kurepa"`；公开 AI/社区：`"Cohen" "Kurepa" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** Jin–Shelah 原文的 forcing 类型、基数假设仍需全文复核；本轮仅原帖与检索摘要。 2308.13478 已看最新版本摘要，未读全文；不能迁移其 weak Kurepa 结论。 未执行形式化验证；未运行检索到的外部代码。

#### QX-P-002045 · `7665e6b4e1a9eaba` · 暂未找到可验证结果；题面有误

原问是两个平面鼓的 Dirichlet 谱在某阈值以上完全相同、阈值以下不同，既不是近似谱，也不是通常的全谱等谱非等距例子。相关 strong multiplicity one 文献的流形类别未核得覆盖平面域。

**旧卡 → 本轮变化：** “几乎一样”被解读为近似谱/全谱等谱 → 恢复阈值以上完全相同、以下不同；补核是否按带重数谱计数，原帖集合写法未完全消除此细节。

**直接证据与范围：**

- [Can two drums be almost isospectral without being isometric? — 原始提问](https://mathoverflow.net/questions/474950/can-two-drums-almost-sound-the-same)；原题阈值 λ 以上的两谱相等及低谱不同。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。

**实际搜索路径：** 原帖打开；system2 搜索 `"almost isospectral" "planar" "finite" eigenvalues` / `"strong multiplicity one" "Laplacian" planar domains`；代码：`site:github.com "drums" "almost" "isospectral"`；公开 AI/社区：`"drums" "almost" "isospectral" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** 需明确域的光滑性、连通性以及谱重数约定；本轮检到的 strong multiplicity one 相邻论文只获摘要，未判适用。 未执行形式化验证；未运行检索到的外部代码。

#### QX-P-002047 · `6a63f7abe1393480` · 未作判断；题面有误

原帖是“无限单群有没有分类”的宽问，没有限定有限生成，也没有给出可验收的分类标准。有限 Morley rank、可计算可分类性或某类有限生成单群均是独立的更精确问题。

**旧卡 → 本轮变化：** 把软问题标成具体有限生成分类难题 → 恢复原帖不限有限生成的范围，标为待明确的综述型问法；若要形成数学卡需另写可判定命题，不能直接替用户创造。

**直接证据与范围：**

- [Is there a classification, or a beginning of one, for infinite simple groups? — 原始提问](https://math.stackexchange.com/questions/1895467/is-there-a-classification-of-infinite-simple-groups)；原题短文及 infinite simple groups 的范围。用于恢复本题的对象、量词、参数和子问。 访问：已打开原帖全文及可见评论；不以无正式回答推断数学开放。

**实际搜索路径：** 原帖打开；system2 搜索 `"classification" "infinite simple groups" finitely generated` / `"simple groups" "finite Morley rank" classification 2026`；代码：`site:github.com "infinite simple groups" "classification"`；公开 AI/社区：`"infinite simple groups" "classification" (site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:mathoverflow.net OR site:math.stackexchange.com)`。另有后续原稿、版本及目录定位，逐条见 JSONL。

**待复核：** 本轮检到 2026 finite Morley rank 综述/识别论文的摘要，未读全文，也不把这些子类进展当全分类；需先明确拟研究的精确分类对象。 未执行形式化验证；未运行检索到的外部代码。

### 审计范围与限制

- 25/25 原出处已取得可读全文；部分短编号 URL 最初失败，之后用完整 slug 打开，失败记录未抹去。
- 25/25 执行至少两组学术关键词查询；25/25 执行 GitHub 主题查询；25/25 执行公开 AI/社区适配组合查询。组合查询不等于逐站穷尽搜索，也不证明某站没有内容。
- 12/12 指定对子已比较题面正文；其中 2 对因参考卡完整形式不足保留待定，其余为相关但不等价。没有合并题卡。
- 未独立运行 Lean、Mathlib、Comparator 或外部代码。2049 的小 n 穷举是本轮自写代码，仅验证 n=3,4,5。
- 形式化覆盖只按实际取得的声明、定义、配置和顶层代码记录。无“独立重跑通过”结论。所有在线写入均为 false。


## 第4部分：分题证据与复核事项


核查日期：2026-11-26（Asia/Shanghai）。范围：QX-P-002053–002077，共25题。仅初查；未写线上、未发帖、未运行未经审查的外部代码。

### 覆盖与证据界限

25题均执行原出处核对、两套学术查询、GitHub定向查询、公开AI/社区定向查询、随包全库索引候选检查。关键原稿另行打开；实际词、合并调用返回、失败记录在 QX-NEW-06_逐题回传.jsonl 和 检索审计文件。域名限定搜索不等于逐站全站穷尽。2055的MSE数字入口失败，已读作者MO交叉帖，并由搜索返回核MSE正文；2072的MO补充回答仅由搜索工具返回文本。

本文件仅列影响题面、结论、出处、证据等级的变化。已存在旧卡的定理/实验明确标为补证，未装作2026新成果。所有形式化均未独立重跑。

### QX-P-002053 · cd509c35ea3cf5cb · 原题已证；部分进展

**旧卡 → 本轮发现：** 旧卡把范畴等价记为未知 → Moerdijk 的开放原稿 §1.2、Corollary 2.4 已给出所需构造和范畴等价；原帖未指定 Haefliger 结构的箭头/覆盖细化，需按标准定义补齐。

**结论与范围：**

- **按标准群胚 cocycle 定义，Haefliger 结构与主 Γ^q 丛的对应：原题已证。** Moerdijk §1.2 给出 cocycle 与主丛的互构；在 cocycle 按覆盖细化及同构处理的标准意义下适用于 Haefliger 群胚。Cor.2.4 将主丛范畴与到 BΓ^q 的拓扑斯态射对应。

- **原帖未明确箭头的“Haefliger 结构范畴”及弱同伦表述：部分进展。** 须明确范畴和所取等价关系；Remark2.5 的 [X,BG] 对应 concordance 类，并非将主丛同构类直接等同于映射同伦类。

**直接证据与定位：**

- [Haefliger 结构与主 Γ^q-丛：原出处](https://math.stackexchange.com/questions/2729692/relationship-between-haefliger-structures-and-principal-gammaq-bundles) — 题干、补充及公开回答/评论（具体适用段落见各子问）。全文已打开；核相关段落。
- [I. Moerdijk, Classifying toposes and foliations (1991)](https://www.numdam.org/article/AIF_1991__41_1_189_0.pdf) — §1.2 pp.191–192；Corollary2.4 pp.195–196；Remark2.5 p.196。全文已打开；核相关段落。

**本轮实际检索路径：**

- 名称/学术：`Haefliger structures principal groupoid bundles cocycles Moerdijk classifying spaces topoi`；公式/特征：`Haefliger Gamma q cocycle category equivalence principal bundles`。
- GitHub：`site:github.com (Haefliger OR Gammaq) (bundle OR cocycle OR Lean)`。本题 GitHub 定向查询未取得对应定理的形式化证明；返回的同名用户/一般群胚代码不能作解答。
- 公开AI/社区：`(site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org OR site:proofforum.org) "Haefliger"`。已列 AI 域名限定查询未取得同题可核证明；不表示逐站站内全量检索。

**待复核：** 若要求完全按原帖某一非标准范畴定义，先由题卡编辑明确其对象和箭头。

### QX-P-002054 · d85f33b1e94f42c9 · 题面有误；原题已证；未作判断

**旧卡 → 本轮发现：** 旧卡只描述所有变量置换不变 → 原帖问 f(x0,x1,…,xn) 仅对 x1,…,xn 对称，并允许双变量内函数。Deep Sets Thm7 的原稿足以支持一个直接的双变量构造。

**结论与范围：**

- **现有人话版是否忠实原题：题面有误。** 遗漏 x0 和部分置换不变性，并把原帖讨论的向量 φ 改写成单纯标量叠加问题。

- **允许向量值双变量 φ(x0,xp) 时是否存在连续表示：原题已证。** 本次基于原稿幂和引理作直接推论：n≥1，取 φ(x0,t)=(x0/n,t,…,t^n)，求和确定 x0 与其余变量的无序多重集。紧致排序单纯形上的幂和映射为到像的同胚；连续对称 f 因此给出像上的连续外函数，再作连续延拓。这是本次给出的短推导，不冒充文献逐字结论。

- **给定原帖提及的某个通用单变量内函数，只改变 λ0 是否总足够：未作判断。** 原帖未固定 φ 的具体版本；不能将已证明的双变量/向量表示直接当作对任意预先给定 Lorentz 内函数的结论。

**直接证据与定位：**

- [置换不变函数的 Kolmogorov–Arnold 表示：原出处](https://math.stackexchange.com/questions/4972681/kolmogorov-arnold-representation-for-permutation-invariant-functions) — 题干、补充及公开回答/评论（具体适用段落见各子问）。全文已打开；核相关段落。
- [Zaheer et al., Deep Sets](https://arxiv.org/html/1703.06114v3) — Appendix A：Lemmas4、6；Theorem7，HTML 行424–517。全文已打开；核相关段落。

**本轮实际检索路径：**

- 名称/学术：`Deep Sets representation partially permutation invariant functions distinguished variable`；公式/特征：`continuous f x0 symmetric x1 xn sum bivariate phi representation power sums`。
- GitHub：`site:github.com "Deep Sets" "representation" theorem`。搜索命中 Deep Sets 实现和相关架构；数值实现不构成原表示定理的形式化证明。
- 公开AI/社区：`(site:hexagonmath.org OR site:aixiv.org OR site:zenodo.org) "permutation invariant" "representation"`。检索命中置换不变表示相邻资料，未取得该部分对称问法的独立 AI 完整证明。

**待复核：** 编辑复核所附幂和短推导；若坚持特定 Lorentz 内函数，须补全固定函数及权重要求。

### QX-P-002055 · 15454afe7fd45b88 · 原题已反驳；题面有误

**旧卡 → 本轮发现：** 旧卡结论并非本轮新解；新增可定位的原回答和局部/全局范围校准，并将“AI 无”改为“评论有 ChatGPT 证明转述，未取得原产物”。

**结论与范围：**

- **互素实多项式在原点同有孤立零点，商能否在原点 C∞ 延拓：原题已反驳。** MO题干额外设f(0)=1，但回答末段的形式幂级数论证不使用该限制：若p=sq，则消去某变量的互素性组合与最低齐次项矛盾。故局部不可能性也排除MSE要求的全平面C∞延拓。

- **孤立零点条件是否保证商在整个 R²减去原点 上有定义：题面有误。** 孤立性只保证某个穿孔邻域内分母非零；全局定义域还须处理其他零点。

**直接证据与定位：**

- [互素多项式商 C^∞ 延拓（MO#506765 已答：永不可）：原出处](https://mathoverflow.net/questions/506765/c-infty-quotient-of-polynomials-in-mathbbrx-y-with-isolated-zeroes-at?noredirect=1) — 题干、补充及公开回答/评论（具体适用段落见各子问）。全文已打开；核相关段落。
- [原 MSE 问题5115316](https://math.stackexchange.com/questions/5115316/is-the-quotient-of-two-coprime-polynomials-in-mathbbrx-y-with-isolated-ze?r=31) — 题目、交叉帖链接。搜索工具返回题目正文；编号直接打开失败，已另打开作者 MO 交叉帖。
- [MO506765 回答与评论](https://mathoverflow.net/questions/506765/c-infty-quotient-of-polynomials-in-mathbbrx-y-with-isolated-zeroes-at?noredirect=1) — fedja 回答及2026-01-18评论；另一回答的初等论证。全文已打开；核相关段落。

**本轮实际检索路径：**

- 名称/学术：`smooth rational functions coprime polynomials isolated zero C infinity Nash analytic`；公式/特征：`polynomial quotient p q formal power series relatively prime smooth germ isolated zero`。
- GitHub：`site:github.com "coprime" "polynomials" "smooth" quotient`。未取得对应商光滑性结论的 Lean/代码证明。
- 公开AI/社区：`"5115316" (ChatGPT OR AI OR proof)`。MSE 编号定向查询和已打开 MO 评论出现 ChatGPT 证明的转述；原始 AI 产物未取得，不能核其正确性。

**待复核：** 如需评价 ChatGPT 证明，取得被转述的原始对话/证明文本。

### QX-P-002057 · f1fd554dc2389239 · 暂未找到可验证结果；部分进展

**旧卡 → 本轮发现：** 旧卡主要记小样本数值 → 补原帖2025-04-08的10^11次报告及代码，并发现 UQ260 收录此题的一般 n 版本与多模型作答，页面评审未给可信的3×3精确解。

**结论与范围：**

- **9个元素独立 Uniform[0,1] 的3×3矩阵全实特征值精确概率：暂未找到可验证结果。** 正态矩阵公式不适用于此分布；已列检索中未取得精确值的证明。

- **原帖提出的解析界与数值实验：部分进展。** 原帖提出构造界 (1/12)^8≤P≤1−6(1/8)^9，本轮未逐项重证扰动估计；Izaak van Dongen 报告10^11次试验约0.7076。后者仅模拟估计，未独立运行或证误差。

**直接证据与定位：**

- [3×3 均匀随机矩阵全实特征值概率：原出处](https://math.stackexchange.com/questions/5054093/probability-for-a-3x3-matrix-to-have-only-real-eigenvalues) — 题干、补充及公开回答/评论（具体适用段落见各子问）。全文已打开；核相关段落。
- [goedel-gang 模拟程序](https://gist.github.com/goedel-gang/3fc6be97696864abc95ac721b35f040d) — 原帖 Izaak van Dongen 2025-04-08 评论所链 gist。代码网页已取得；未锁定历史修订、未运行。
- [UQ Question260](https://uq.stanford.edu/question/260) — 题目来源及模型作答/评审栏目。全文已打开；核相关段落。

**本轮实际检索路径：**

- 名称/学术：`random 3 by 3 uniform positive matrices all eigenvalues real probability`；公式/特征：`iid uniform [0,1] 3x3 matrix real eigenvalues 0.7076 probability bounds`。
- GitHub：`site:github.com "uniform" "eigenvalues" "probability" "3"`。GitHub 定向检索和原帖链接取得 gist；仅审阅网页，未重跑10^11样本。
- 公开AI/社区：`"real eigenvalues" "uniform" ("AI" OR "EulerSolve" OR "ChatGPT")`。已打开 UQ260 原产物；问题为一般n，不能把页面收录当作解题成功。

**待复核：** 精确概率或可验证积分表达式仍需单独证明；模拟程序若复核须固定修订并处理数值判别误差。

### QX-P-002058 · 098fe86cde058aeb · 暂未找到可验证结果；部分进展

**旧卡 → 本轮发现：** 旧卡仅保留发帖人 m≤32 → 原帖2018-05-20评论称已验至 m≤50000。这是历史计算线索的本轮补录，非2026新定理。

**结论与范围：**

- **是否仅有 (m,n)=(2,28),(5,3207)：暂未找到可验证结果。** 原题两组解直接可核；两套学术检索及后续精确查询未获得全称排除证明。有限计算不证明仅有两解。

- **有限搜索范围：部分进展。** Sil 在原帖报告 m≤50000；未提供本轮可运行的证书，未独立重跑。

**直接证据与定位：**

- [∏(pᵢ²+i)=n²−27² 仅两解？：原出处](https://math.stackexchange.com/questions/2788367/are-2-28-and-5-3207-the-only-solutions-m-n-in-mathbbn2) — 题干、补充及公开回答/评论（具体适用段落见各子问）。全文已打开；核相关段落。

**本轮实际检索路径：**

- 名称/学术：`"prime squares" "3207" product`；公式/特征：`"p_i" "27" "2788367"`。
- GitHub：`site:github.com ("2788367" OR "3207") "prime"`。编号/3207/prime 定向 GitHub 查询未取得对应计算脚本。
- 公开AI/社区：`"prime squares" "27" (site:hexagonmath.org OR site:zenodo.org OR site:mathoverflow.net)`。prime squares/27 的 AI与社区限定查询未取得同题完整证明；无命中不能支持开放性断言。

**待复核：** 取得对应脚本、素数范围与精确整数平方判据，或统一排除论证。

### QX-P-002059 · e8190e8a3852f8e2 · 暂未找到可验证结果；部分进展；完整证明/反例声明待核；题面有误

**旧卡 → 本轮发现：** 旧卡只记 OEIS 及实验 → 2022 Chase–Pandey Thm1.1 已给统一幂界；2026-10-27 Hexagon2610.00588v1 声称把指数降到 β*≈0.2941336553，并公开固定 Lean 提交。至首次1的步数比正项长度少1。

**结论与范围：**

- **最坏情形首次到1步数是否 O(log P)：暂未找到可验证结果。** 以下文献是 a 的正幂上界或平均长度下界，不能推出原素数情形最坏步数 O(log P)。

- **统一幂次上界：部分进展。** Chase–Pandey Thm1.1 为 O(a^(1/3−2/177+ε))，统一于初值；常数依 ε。原题可取 a=P，再作步数约定调整。

- **2026 更强幂界及其形式化声明：完整证明/反例声明待核。** Davies Thm1.1 声称对任意 ε>0 存在 Cε，所有0<b<a有 P(a,b)≤Cε a^(β*+ε)，β*=(41301−3√82849)/137480。已取得固定提交主定理与工具链文件，但未完整审依赖、未编译，不能写独立通过。

- **P=t x!−1 例称到1恰为x步：题面有误。** 递推依次为 x,x−1,…,1，因此按原帖“到首次1”的定义是 x−1 次；若计正项或到0则为x。

**直接证据与定位：**

- [x↦P mod x 迭代步数 O(log P) 界：原出处](https://math.stackexchange.com/questions/2756510/iterating-fx-p-bmod-x) — 题干、补充及公开回答/评论（具体适用段落见各子问）。全文已打开；核相关段落。
- [Z. Chase and M. Pandey, On the length of Pierce expansions](https://www.math.kent.edu/~zchase/pierce.pdf) — Theorem1.1，稿件p.2；arXiv2211.08374v1。全文已打开；核相关段落。
- [Jason Davies, Hankel determinants and the length of finite Pierce expansions (2026-10-27, v1)](https://hexagonmath.org/pdf/2610.00588v1) — Theorem1.1 p.2；§12 p.47；网页 provenance。全文已打开；核相关段落。
- [pierce-length-bound 固定提交](https://github.com/jasondavies/pierce-length-bound/blob/6da6511cea9f8526054dd5ad60d77164f45de52e/PierceLengthBound/PolarProjectionMain.lean) — PierceLengthBound.P_le_polar_optimal；README、lean-toolchain、lakefile、lake-manifest。通过 GitHub connector 取得；未编译/未执行。
- [Min Woong Ahn, Uniform lower bounds for the average length of finite Pierce expansions (2026,v1)](https://arxiv.org/html/2610.26594v1) — Theorem1.1。全文已打开；核相关段落。
- [作者链接的 Palomar entry](https://palomar-registry.org/entry?id=PALOMAR-2026-10-27-000017&version=1) — 页面壳。直接打开仅返回 JavaScript 页面壳。

**形式化范围：** {"status": "已取得代码未重跑", "commit": "6da6511cea9f8526054dd5ad60d77164f45de52e", "theorem_path": "PierceLengthBound/PolarProjectionMain.lean : PierceLengthBound.P_le_polar_optimal", "statement_checked": true, "definition_and_full_dependency_audit": "未完成；未取得/核完 P 的定义与全部导入链", "lean_toolchain": "leanprover/lean4:v4.35.0", "mathlib_commit": "56a005855ea17e0b0958f73ec801ae140b0a1679", "CCDN_commit": "bb025e7207f3a35a21b898629f5678b72aa7e44f", "other_dependencies": "vendored openai_math 等；见 lake-manifest。README 说明 Challenge.lean 的题目占位不在正式 Solution 中，不等于本次已审清完整链。", "independent_run": "未执行", "external_code_executed": false}

**本轮实际检索路径：**

- 名称/学术：`Pierce expansion length rational numbers modular inverse iteration prime`；公式/特征：`"P mod x" "log" iterations number theory`。
- GitHub：`site:github.com "Pierce" "length" bound`。检索命中作者仓库；通过 connector 锁定提交6da6511…，取得主定理与依赖版本文件，未重跑。
- 公开AI/社区：`"Pierce expansions" (site:hexagonmath.org OR site:palomar-registry.org OR site:zenodo.org)`。打开 Hexagon2610.00588v1 的正文、PDF与来源说明；Palomar入口仅取得页面壳，不能独立验证注册/通过状态。

**待复核：** 独立构建固定提交并审完整 import 链、P 的定义、依赖与可能额外公理；本轮未执行。；对数界仍需针对最坏情形的证明或反例；Ahn 平均下界不能替代。

### QX-P-002063 · 11ba45955916c6ce · 原题已证；部分进展；原题已反驳；暂未找到可验证结果

**旧卡 → 本轮发现：** 旧卡“κ-complete 情形出处不明、题面一致” → 原文实际明确常结构与基数界，并在末段主张 U≡RK U×U。本轮识别其所用投影映射并不满射。

**结论与范围：**

- **κ完备、常结构、|A|<κ的情形：原题已证。** 每个I→A函数因κ完备性在U大集上常值，所以单次超幂同构于A，迭代亦同。不能删去常结构及基数界。

- **good/可数不完备超滤子下的充分条件：部分进展。** 原帖引Chang–Keisler6.1.9，明确|I|^+=2^|I|、|A|<|I|^+与|I|^+-good；语言大小等适用条件仍需核原书。Keisler综述可核相邻饱和框架。

- **原帖Final case中 π0 导出的映射为满射：原题已反驳。** 这是对该证明步骤的反驳，不是对所有抽象同构的反驳：非主U取H(i,j)=j。任意f(i)与H相等的内层集合至多单点，不属于U，因此[H]不在[f∘π0]的像中。

- **一般非平凡κ完备条件的完整分类：暂未找到可验证结果。** 上述投影论证失效，尚不能据此判定所有可能的其他同构/条件。

**直接证据与定位：**

- [迭代超积的"无害性"条件：原出处](https://math.stackexchange.com/questions/5106082/when-is-the-iterated-ultrapower-innocuous) — 题干、补充及公开回答/评论（具体适用段落见各子问）。全文已打开；核相关段落。
- [H. J. Keisler, The ultraproduct construction](https://people.math.wisc.edu/~hkeisler/ultraproducts-web-final.pdf) — §10 good ultrafilters / saturated ultrapowers，约p.14。全文已打开；核相关段落。

**本轮实际检索路径：**

- 名称/学术：`iterated ultrapowers isomorphic good ultrafilter Chang Keisler 6.1.9`；公式/特征：`normal fine complete ultrafilter Fubini product Rudin Keisler self product`。
- GitHub：`site:github.com "iterated ultrapower"`。iterated ultrapower GitHub精确查询未取得该投影满射/一般同构的适配形式化证明。
- 公开AI/社区：`"iterated ultrapower" (site:hexagonmath.org OR site:zenodo.org OR site:proofforum.org)`。公开AI域名定向检索未取得本题完整结果；源帖末段是作者自述，不认作AI产物。

**待复核：** 取得Chang–Keisler定理原书核语言基数等全部假设；一般RK等价需独立论证。

### QX-P-002064 · aff2597af517638d · 完整证明/反例声明待核；题面有误

**旧卡 → 本轮发现：** 旧卡泛称115KB/84引理 → 固定2026-08-15提交，核StarryGraphs.lean的Peculiar/Starry定义和starry_iff_not_peculiar；代码119757字节、2524行，不以旧摘要当本轮核验。

**结论与范围：**

- **有限连通简单图有偶度点时归约清空：完整证明/反例声明待核。** 原作者2026-03-04自答、2026-08-09编辑完整证明；有限Lean主引理描述存在合法删法后无peculiar连通分量，可经有限归纳连到清空。已核语句对应但未完整审纸证/独立编译。

- **卡片不声明有限图而要求有限次归约清空：题面有误。** 应补“有限”。若按任意简单图字面理解，双向无限路径每点度2，每次仅删有限个顶点，有限次不能清空。Lean文件明确Fintype假设。

**直接证据与定位：**

- [偶度点归约清空连通图：原出处](https://math.stackexchange.com/questions/5099016/removing-vertices-from-graphs-by-reductions-a-continuation-of-an-unsolved-prob) — 题干、补充及公开回答/评论（具体适用段落见各子问）。全文已打开；核相关段落。
- [Starry-Graphs-Lean 固定提交](https://github.com/two-skeletons/Starry-Graphs-Lean/blob/085cc5ad687a7354d9bc5213b2f26118b0df01e8/StarryGraphs.lean) — Peculiar行219；Starry行224；starry_of_even_degree行2182；starry_iff_not_peculiar行2511–2521。GitHub connector取得完整单文件，静态检查；未编译。

**形式化范围：** {"status": "已核定理对应、未重跑", "commit": "085cc5ad687a7354d9bc5213b2f26118b0df01e8", "blob_sha": "9d0c2057ba6d58e6fd0408008644ccd433818bc5", "file": "StarryGraphs.lean", "theorem": "starry_iff_not_peculiar", "lines": "2511–2521", "assumptions": "Fintype V、DecidableEq V、DecidableRel G.Adj、G.Connected", "dependencies": "import Mathlib；仓库未附lean-toolchain/lakefile/lock，Mathlib版本未锁", "static_scan": "完整文件未见 sorry/admit/axiom/unsafe/implemented_by/run_tac/run_elab/initialize；只属文本检查，不证明可信内核通过", "independent_run": "未执行", "external_code_executed": false}

**本轮实际检索路径：**

- 名称/学术：`"starry" "peculiar" "graphs"`；公式/特征：`"even-degree" "reductions" "Katic"`。
- GitHub：`site:github.com "Starry-Graphs-Lean"`。已锁定提交085cc5…并取得119757字节完整文件；固定blob校验一致，未执行外部代码。
- 公开AI/社区：`"starry" "peculiar" (Aristotle OR Harmonic OR AI)`。原帖2026-08-15评论明确称Aristotle完成形式化；这是作者来源陈述，独立验证仍未执行。

**待复核：** 仓库缺lean-toolchain、lakefile及锁文件；需取得可复现实测环境后编译，核Mathlib版本与所有假设。；归约清空的有限归纳桥梁与主引理一并人工复核。

### QX-P-002067 · 6ff96995fd2b2cd8 · 题面有误；暂未找到可验证结果

**旧卡 → 本轮发现：** 旧卡“对任意有界E，是否存在内部紧集列逼近” → 恢复原MO每个递增紧集列(Kn)、K=∪Kn仍紧时是否γ(Kn)→γ(K)。二者不是同一问题。

**结论与范围：**

- **卡片人话版与原题是否一致：题面有误。** 存在一列逼近与每个指定递增序列连续性量词不同；还遗漏并集K紧条件。某些扩展γ(E)的约定本就用内部紧集上确界，不能据此解原问。

- **递增紧集列、并集紧时γ是否从下连续：暂未找到可验证结果。** Younsi稿件末尾Remark确实提出同问；这说明该稿时的未解决状态，不自动证明2026现状。两套检索及AI/代码检索未取得解决原问的可验结果。

**直接证据与定位：**

- [解析容量内正则？：原出处](https://mathoverflow.net/questions/86220/is-analytic-capacity-inner-regular) — 题干、补充及公开回答/评论（具体适用段落见各子问）。全文已打开；核相关段落。
- [Malik Younsi, On analytic and Cauchy capacities](https://math.hawaii.edu/~myounsi/CauchyCap.pdf) — 末尾Remark，正文p.15（PDF第15页）。全文及相关Remark已打开；不依据搜索页面相对日期断言论文发表于2026。

**本轮实际检索路径：**

- 名称/学术：`"analytic capacity" "inner regular" Younsi`；公式/特征：`"analytic capacity" "increasing" "compact" "continuity"`。
- GitHub：`site:github.com "analytic capacity" "regular"`。analytic capacity/regular GitHub查询未取得本题正式化或反例。
- 公开AI/社区：`"analytic capacity" "inner regular" (AI OR proof OR counterexample)`。inner regular + AI/proof/counterexample检索未取得适配量词的新证明；单调性不推出从下连续。

**待复核：** 若后续核最新状态，应追踪该Remark的具体后续引用；本次初查未找到解。

### QX-P-002068 · 1c75b23e33c2586d · 暂未找到可验证结果；未作判断

**旧卡 → 本轮发现：** 旧备注称5.5年且存在摘要误导风险 → 原帖日期为2024-05-15；Noah Schweber确有“ZF不可证”的评论声明，但本次未取得其完整证明。相邻PP论文不能直接填补。

**结论与范围：**

- **ZF能否证明每集合是某全序集的满射像：暂未找到可验证结果。** 已打开原问题与评论。Schweber称不可证并表示稍后给证明；本轮未取得该证明、ZF反模型或可靠原文定理。不能把评论权威性或ZFA模型当成ZF独立性证明。

- **由X全序且满射X→Y直接给Y排序/给满射选择截面的论证：未作判断。** 这种论证未提供所需的逐纤维选择：一般全序不保证非空子集有最小元。它不能证明原命题，也不能当作反驳原命题的依据。

**直接证据与定位：**

- [ZF 中每集合为全序集满射像？（⚠️摘要幻觉陷阱题）：原出处](https://math.stackexchange.com/questions/4916951/is-every-set-an-image-of-a-totally-ordered-set) — 题干、补充及公开回答/评论（具体适用段落见各子问）。全文已打开；核相关段落。

**本轮实际检索路径：**

- 名称/学术：`"surjective image" "linearly ordered" "ZF"`；公式/特征：`"every set" "image of a totally ordered set" independence`。
- GitHub：`site:github.com "surjective" "linearly ordered" "ZF"`。surjective/linearly ordered/ZF GitHub查询未取得对应反模型形式化。
- 公开AI/社区：`"every set" "linearly ordered" (site:hexagonmath.org OR site:wcook04.github.io OR site:zenodo.org)`。实际查询命中Plectis Atlas上PP≠AC相邻内容；该入口是镜像，且PP为满射推注入原则，非原问，未据其得出结论。

**待复核：** 取得Schweber所指ZF反模型及无全序集满射覆盖的证明；有模型后再核与AC模型的相对一致性。

### QX-P-002069 · fae21783f4c3f827 · 原题已证；部分进展

**旧卡 → 本轮发现：** 旧卡只把2025预印本用于姐妹初值 → arXiv2508.05347v3（2026-09-09）§1的通用引理覆盖原初值；原MSE的2025-08-08 Final Addition也已说明不共线获解。

**结论与范围：**

- **初值(0,0),(2,0),(4,1)经规定90°跳跃能否共线：原题已证。** v3§1主引理：若任何首次跳跃都不减无向面积，则任何有限跳跃序列都不减。原初值有向双面积2，边长平方为4、5、17，首次跳跃双面积为2±4、2±5、2±17，绝对值均≥2。因此任何可达面积非零。此为对已核引理的显式代入。

- **原初值所有不能达到的面积/双面积的完整刻画：部分进展。** 原稿列实验序列，未取得其完整性的证明。Theorem2使用初值(0,0),(2,1),(3,2)，不得把姐妹问题结论直接移至原初值。

**直接证据与定位：**

- [格点跳转面积 2S 错失值集合（OP 论文部分解决姊妹初值）：原出处](https://math.stackexchange.com/questions/4885453/on-three-integer-points-in-the-plane-and-a-strange-sequence-0-1-4-5-9-11-1) — 题干、补充及公开回答/评论（具体适用段落见各子问）。全文已打开；核相关段落。
- [Giedrius Alkauskas, Squares, Three Fleas, Sporadic Sets, and Squares（v3）](https://arxiv.org/html/2508.05347v3) — §1通用Lemma；Theorem2；arXiv版本记录v1 2025-08-07、v2 2026-09-03、v3 2026-09-09。全文已打开；核相关段落。
- [Alkauskas 同稿v1](https://arxiv.org/html/2508.05347v1) — §1原初值及所列面积序列。全文已打开；核相关段落。

**本轮实际检索路径：**

- 名称/学术：`"Squares, three fleas" Alkauskas 2508.05347`；公式/特征：`"fleas" "collinear" "2,0" "4,1"`。
- GitHub：`site:github.com "fleas" "Alkauskas"`。fleas/Alkauskas GitHub查询未取得相应形式化代码。
- 公开AI/社区：`"three fleas" (site:hexagonmath.org OR site:zenodo.org OR site:hub.valency.io)`。AI成果域名查询未取得同题独立AI证明；新依据是作者预印本v3。

**待复核：** 若要完整缺失面积谱，仍需针对原初值的证明；本次未取得。

### QX-P-002071 · f91dc9966feba3a6 · 暂未找到可验证结果；完整证明/反例声明待核；部分进展

**旧卡 → 本轮发现：** 旧卡只列历史数论背景 → 新检出Li Song的2026完整否定声明，并在原稿§3.3发现把待证x=z−x当成前提；同时定位Yuan Si最新2026-11-14 Zenodo版本，其范围仍是部分约束。旧卡所谓原代码截断也与已打开完整MSE正文不符。

**结论与范围：**

- **具有自然数边、等长互相垂直对角线的目标四边形是否存在：暂未找到可验证结果。** 原帖代码与后续公开完整解声明均未提供本轮可接受的解。与单位正方形内部有理距离点的对应须保留凸性/两对角线内交条件。

- **viXra2605.0013v1的完全否定证明：完整证明/反例声明待核。** 已定位足以阻断该稿证明的缺口：§3.3式(3),(4)仅给x=4r−s、z−x=4r′−s′和rs=r′s′；英文p.4随即使用4r−s=4r′−s′，即无根据假设x=z−x，再由此推出点在中线。不能据该稿把原题判为已反驳。

- **Zenodo24212887 v1.1.0的部分成果：部分进展。** 记录页称排除某个相对边距离差1/5来源的全部高度，补充局部算术约束；同时明确整体问题未解决。正文PDF下载失败，本轮仅能登记作者摘要层声明。

**直接证据与定位：**

- [自然边与对角线的 midsquare（=四距离问题内点版本）：原出处](https://math.stackexchange.com/questions/4806891/does-there-exist-a-midsquare-with-natural-sides-and-diagonal) — 题干、补充及公开回答/评论（具体适用段落见各子问）。全文已打开；核相关段落。
- [Li Song, A Complete Proof of the Rational Distance Problem for the Unit Square](https://vixra.org/pdf/2605.0013v1.pdf) — 英文§3.3 Theorem3.1，式(3),(4)后，英文p.4（PDF第4页）；Theorem3.3。全文已打开；核相关段落。
- [Yuan Si, Arithmetic constraints and covering curves for rational distances in a square, v1.1.0](https://zenodo.org/records/24212887) — 2026-11-14记录页说明；91页、83 statements、59/83 formalized 的作者计数。记录页全文已打开；PDF两种URL均获取失败，未核页码或Lean代码。
- [viXra2605.0013版本页](https://vixra.org/abs/2605.0013) — v1上传日期2026-05-05；管理员说明。全文已打开；核相关段落。

**形式化范围：** {"status": "他人声称已形式化验证", "artifact": "Zenodo24212887 v1.1.0作者说明；59/83 statements", "scope": "局部/特定来源结果，非原问题完全解", "code_obtained": false, "independent_run": "未执行", "external_code_executed": false}

**本轮实际检索路径：**

- 名称/学术：`"midsquare" "natural sides" diagonal`；公式/特征：`"rational distance" "square" interior point K3 2026`。
- GitHub：`site:github.com "rational distance" "square" "Lean"`。GitHub检索命中rational-distance相关Lean/数值仓库线索；本轮未取其中完整代码和固定提交，不能宣称形式化通过。
- 公开AI/社区：`"rational distance" "square" (site:hexagonmath.org OR site:zenodo.org OR site:aixiv.org)`。公开AI/Zenodo查询取得最新Zenodo记录；viXra原稿和版本页均打开。管理员提示不能证明该作者使用AI。

**待复核：** viXra若有修订须重新核§3.3，不能用作者标题作证明。；Zenodo全文和形式化仓库未核，需另取PDF、固定提交及具体定理。；原问题与内部有理距离问题的几何等价条件需在题面固定。

### QX-P-002073 · 78c9caeac2d391cd · 暂未找到可验证结果；部分进展

**旧卡 → 本轮发现：** 旧卡把S²上总空间统一写成SU(2)/C_n → n=0时是平凡丛S²×S¹，须单列；原问题只要求某个传递Lie群作用，不要求保留给定丛结构。

**结论与范围：**

- **一般紧齐性底空间的主U(1)丛总空间是否齐性：暂未找到可验证结果。** 已打开MSE及MO交叉帖；非主圆丛及仅否定某一提升作用的例子不能反驳原命题。

- **底空间S²的低维例及Euler类0：部分进展。** Euler类非零时对应lens-space类齐性例；Euler类0时总空间S²×S¹亦齐性。原卡若统写SU(2)/C_n遗漏零类。

**直接证据与定位：**

- [紧齐性底 U(1)-主丛全空间齐性？：原出处](https://math.stackexchange.com/questions/4759062/is-the-total-space-of-a-u-1-principal-bundle-over-a-compact-homogeneous-spac) — 题干、补充及公开回答/评论（具体适用段落见各子问）。全文已打开；核相关段落。
- [主U(1)丛总空间齐性的MO交叉帖](https://mathoverflow.net/questions/454339/is-the-total-space-of-a-u-1-principal-bundle-over-a-compact-homogeneous-spac?noredirect=1) — 题目与低维表。全文已打开；核相关段落。

**本轮实际检索路径：**

- 名称/学术：`"principal circle bundle" "homogeneous" compact total space`；公式/特征：`"U(1)" "homogeneous" "Mostow" bundle`。
- GitHub：`site:github.com "homogeneous" "principal circle bundle"`。homogeneous/principal circle bundle GitHub检索未取得总空间一般齐性定理的形式化。
- 公开AI/社区：`"principal circle bundle" (site:hexagonmath.org OR site:zenodo.org OR site:proofforum.org)`。主圆丛AI成果域名查询未取得完整答案；未把相邻非主丛例子作反例。

**待复核：** 一般高维结论需直接定理或主丛反例；本轮未取得。

### QX-P-002074 · ff0421039a708e76 · 题面有误；原题已反驳；暂未找到可验证结果；部分进展

**旧卡 → 本轮发现：** 旧人话版称所有Clifford元素均可写为向量积且未提n=1 → 原帖只问已给向量积，并明确n=1需空积前标量。旧备注的退化反例出处应直接锚到原帖的R^{1,1,1}计算。

**结论与范围：**

- **“所有Clifford元素都是向量积”的题面说明：题面有误。** 每个向量积具有固定Z/2奇偶性；一般元素如1+e含混合奇偶分量，并非这样的单个乘积。

- **n=1不允许标量前因子的字面命题：原题已反驳。** 取一维e²=1，则(2e)e=2不能写成0个向量的空积1或1个向量。原作者已明说n=1需要标量前因子；这不是对修正后高维主问的反例。

- **n≥2、非退化二次型、允许null因子的向量积还原：暂未找到可验证结果。** Cartan–Dieudonné适用可逆向量所表示的反射，不能覆盖含null因子。原帖仅声称n=2,3,4已证、n=5有思路，未取得一般n≥6证明。

- **退化不定二次型的相邻反例：部分进展。** 原帖R^{1,1,1}中四向量积1+(e1+e2)e3不可为两向量积。这说明去掉非退化假设会失败，不反驳当前非退化主问。

**直接证据与定位：**

- [Clifford 代数 ≤n 向量还原问题：原出处](https://math.stackexchange.com/questions/4629333/in-a-clifford-algebra-over-an-n-dimensional-non-degenerate-space-is-a-product) — 题干、补充及公开回答/评论（具体适用段落见各子问）。全文已打开；核相关段落。

**本轮实际检索路径：**

- 名称/学术：`Clifford algebra product null vectors n factors nondegenerate`；公式/特征：`"Clifford" "Cartan-Dieudonne" "null" "product"`。
- GitHub：`site:github.com "Clifford" "null vectors" "product"`。Clifford/null vectors/product GitHub查询未取得覆盖该零因子范围的对应定理；一般Clifford代码不等同于解答。
- 公开AI/社区：`"Clifford" "product of vectors" (site:hexagonmath.org OR site:zenodo.org OR site:hub.valency.io)`。AI成果定向查询未取得覆盖null因子的≤n定理；Cartan–Dieudonné式标题须核可逆性。

**待复核：** 严格核一般非退化且含null因子的向量积上界；低维chat证明本轮未逐项复核。；如需引用3952133，另核该帖实际半正定/退化范围，本轮不据其摘要判定。

### QX-P-002075 · 3aae96598e6cf409 · 原题已反驳

**旧卡 → 本轮发现：** 旧卡claimed仅据Suárez-Álvarez评论 → 取得Kolář–Michor–Slovák作者公开书稿Theorem4.21及证明，直接覆盖题问。

**结论与范围：**

- **通常R^n拓扑上是否存在不同/异域光滑结构仍使加法和取负光滑：原题已反驳。** 若存在，它与标准R^n均为同一拓扑群的Lie群结构。两方向恒等映射均是连续群同态，由Theorem4.21均光滑，故恒等映射是微分同胚，极大光滑图册相同。无需以Hilbert第五问题代替这一精确定理。

**直接证据与定位：**

- [exotic Rⁿ 加法/取负光滑（评论级否定）：原出处](https://math.stackexchange.com/questions/4536297/do-any-exotic-smooth-structures-on-mathbb-rn-leave-addition-and-negation-smo) — 题干、补充及公开回答/评论（具体适用段落见各子问）。全文已打开；核相关段落。
- [Kolář, Michor, Slovák, Natural Operations in Differential Geometry](https://www.mat.univie.ac.at/~michor/kmsbookh.pdf) — Theorem4.21，正文p.37（PDF第40页）及证明。全文已打开；核相关段落。

**本轮实际检索路径：**

- 名称/学术：`Lie group unique smooth structure continuous homomorphism automatically smooth`；公式/特征：`simply connected abelian Lie group exponential map diffeomorphism exotic R4`。
- GitHub：`site:github.com "LieGroup" "continuous" "homomorphism" Lean`。LieGroup/continuous/homomorphism Lean查询未取得本次可锁定且完整对应的定理文件；结论依据书稿，不声称Lean通过。
- 公开AI/社区：`"exotic" "addition" "smooth" (site:hexagonmath.org OR site:zenodo.org OR site:mathoverflow.net)`。AI成果与MO限定查询无新的必要证据；原评论数学结论由书稿支持。

**待复核：** 题卡编辑核上述标准定理的直接应用即可；无独立形式化重跑。

### QX-P-002077 · 668f73d0a9b4514e · 原题已证

**旧卡 → 本轮发现：** 旧卡已有Odlyzko–Richmond锚点 → 本轮直接打开作者PDF定位Theorem1及端点正性条件，严格覆盖全部系数正的有限多项式；MO回答日期为2022-03-13。

**结论与范围：**

- **全部系数正的多项式所有足够高次幂的系数是否单峰：原题已证。** 归一化为支撑0,…,d的有限概率密度。Odlyzko–Richmond Theorem1假设p0,p1,p(d−1),pd>0，结论充分高卷积强单峰/对数凹；原题全部系数正满足之。d≤1的情形直接成立。

**直接证据与定位：**

- [正系数多项式高次幂终单峰（Odlyzko–Richmond 1985 已解）：原出处](https://math.stackexchange.com/questions/4399939/prove-or-disprove-that-the-power-of-positive-term-polynomial-will-be-eventually) — 题干、补充及公开回答/评论（具体适用段落见各子问）。全文已打开；核相关段落。
- [Odlyzko and Richmond, On the unimodality of high convolutions of discrete distributions (1985)](https://www-users.cse.umn.edu/~odlyzko/doc/arch/unimodal.convolut.pdf) — Theorem1，稿件p.2（PDF第3页）；与Theorem2的范围区分。全文已打开；核相关段落。
- [MO417928 Handelman回答](https://mathoverflow.net/questions/417928/prove-or-disprove-that-the-power-of-positive-term-polynomial-will-be-eventually) — 2022-03-13回答。全文已打开；核相关段落。

**本轮实际检索路径：**

- 名称/学术：`"Odlyzko" "Richmond" "unimodality" 1985`；公式/特征：`"polynomial" "high powers" "positive coefficients" "log-concave"`。
- GitHub：`site:github.com "Odlyzko" "Richmond" "unimodal"`。Odlyzko/Richmond/unimodal GitHub精确查询未取得对应Lean证明。
- 公开AI/社区：`"positive polynomial" "unimodal" (site:hexagonmath.org OR site:zenodo.org OR site:proofforum.org)`。positive polynomial/unimodal AI域名查询未取得新适配产物；结论来自已核历史原稿。

**待复核：** 无新的必需数学核项；形式化本轮未执行。

### 指定查重：4组均不建议合并

均已读取随包参考题卡正文；只复核本组owner指定对子。未把标题关键词相近当成同题。

| Owner | 对方版本 | 关系 | 理由 |
|---|---|---|---|
| QX-P-002070 | QX-P-001390 · 13c0b3969485f865 | 相关但不等价 | 对方G_n=F_dn/F_n研究奇素数模下的同余。取d=a,n=a^k仅让表达式相接，不能把同余问题等同于本题商为素数的分类。 |
| QX-P-002070 | QX-P-001776 · 071ff71fc9a3787c | 相关但不等价 | 对方问F_n²+F_m²是否为平方；本题问幂指标商的素性。没有双向归约证据。 |
| QX-P-002070 | QX-P-002242 · d26ae49dfc6a4c8a | 相关但不等价 | 对方为有理数的展开周期性；本题为整除商素性，仅共享Fibonacci词。 |
| QX-P-002074 | QX-P-002276 · 2c5ba57d07cebb99 | 相关但不等价 | 对方是C²中Hamilton同痕分类；Clifford名称不构成Clifford代数乘积还原问题的等价。参考卡正文还明确排除002074。 |

### 其余题的处理

002056、002060、002061、002062、002065、002066、002070、002072、002076均已逐题查询，完整记录在JSONL。未取得足以改变主问状态的新可验结果；其中既有反例、已知部分界和作者计算按子问保留，不能把无新命中当作开放性证明。002070的OEIS25000位界已在旧卡，本轮直接页403，仅保留搜索记录级证据。

### 审计文件

- `QX-NEW-06_逐题回传.jsonl`：25题逐项回传，保留题号、版本、实际查询、证据、子问及限制。
- `检索审计文件`：原样工具返回（包括失败），每条记录带实际参数。
- `index_scan.json`：随包全库索引候选检索结果。
- `external_code/StarryGraphs.lean`：只读取得的固定代码副本；未执行。
- `academic_queries.json`、`code_ai_queries.json`：实际使用的查询词矩阵。
