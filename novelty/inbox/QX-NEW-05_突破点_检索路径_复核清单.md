# QX-NEW-05：突破点、检索路径与复核清单

检查日期：2026-11-26。对应上传包中的100张指定题卡；保留全部 `batch_id`、`id`、`card_rev`。本轮为逐题初查，原问题、数学子问、已刊结果、公开完整证明声明、计算与形式化证据分别记录。

## 交付与覆盖

逐题机器可读文件为 `QX-NEW-05_逐题回传.jsonl`，恰100行。全部题目都有实际查询记录：两组学术查询、GitHub/代码、公开AI/社区、原始出处追踪及库内索引。原始入口不可达、仅摘要、检索命中不适用、代码未重跑均保留原样，不以无命中证明开放。

全库索引共2,469条。46个指定对子已逐对记录双方版本、关系与理由；新增候选见文末，其中仅有标题线索的保留“待定”。未改线上题库，未发帖，未执行未审查的外部代码。

本轮**没有独立重跑Lean项目**。A276175等已检查定理对应的代码，仍标“已核定理对应、未重跑”；带额外公理/占位的开发明确排除全解。1863/1864的小反例是另外编写标准库Python并实际运行的有限穷举，范围仅为附件列出的三个构造。

## 优先复核入口

| 题号 | 本轮变化 | 建议处置 |
|---|---|---|
| 1863、1864 | 全n版本的小反例与充分大n报告声明并存；三个构造已独立穷举 | 拆开量词；反驳字面全n，保留大n声明待核 |
| 1890、1901、1961 | 额外公理、只证弱化命题、未合并且仍含sorry的PR | 不将“形式化”字样直接当完整证明 |
| 1928、1958 | 原全称题面有直接可检查反例或缺失例外 | 分开原字面命题、修正版和特殊子问 |
| 1883、1907、1908、1929 | 已刊文献覆盖了此前未正确收录的明确子问 | 只更新有证据覆盖的范围 |
| 1885、1880、1923、1935、1953、1963 | 作者来源冲突、仅摘要或公开AI完整证明声明 | 按逐题定位表列出的缺口进一步复核 |
| 1855—1866、1878、1879、1894、1895、1902、1921、1944、1952 | 对象、量词或译文改变了数学问题 | 先修卡面，再沿正确命题追查 |
| 1946、1957 | 同一A276175递推整数性问题；对应Lean主定理已核 | 新增同题关系，共用证据；代码仍未重跑 |

以下仅列会影响题面、数学子问状态、出处或查重关系的发现。普通零命中不逐题复述，完整实际检索词与访问状态在JSONL中。

## 第1—25题：经核查的变化

### 1. QX-P-001863 / 001864：全 n 版本的小反例与充分大 n 声明必须分开

**旧卡 → 变化。** 1863 把精确阈值统一写成强解决声明，1864 又将单图结果当作可直接使用的定理。原综述 Conjectures 7.1、7.5 的“所有 n≥k+1”字面版本有小规模反例；大学报告明确只宣布 **for large n**，两者没有逻辑冲突。

**直接证据与定位。** [Ferudun 公开稿](https://eulersolve.org/papers/owr-1782-009/paper.pdf?v=ee3b8aa85751)，2026-09-28，Theorem 1.2(a)、§2、pp.2–3；DOI 10.5281/zenodo.23006718。该稿未审稿并披露 AI 辅助。[Toronto 第一方报告](https://seminars.math.utoronto.ca/pages/seminars?case=view_talk&talk_id=1793718000-1793311670-815)，Shoham Letzter，2026-11-03，摘要明确“充分大的 n”，列联合作者 Lang、Ranganathan、Sanhueza-Matamala。本轮未取得这一新定理的完整稿。

**本轮独立复核。** 取六点集 W={1,…,6}，三元组族

`D′={123,124,135,146,156,236,245,256,345,346}`。

另添 k−2 个顶点。H_k 的边是所有满足 `|e∩W|≠3` 或 `e∩W∈D′` 的 k 元集。我们按这个数学定义另写标准库 Python，没有运行作者提供的程序。对固定一个起点并除去反向等价后的所有循环排列逐一检查连续 k 点是否为边，结果如下。

| k | n | 边数 | 最小 (k−1)-度 | 检查的循环排列 | 紧 Hamilton 圈 |
|---|---|---|---|---|---|
| 3 | 7 | 25 | 3 | 360 | 0 |
| 4 | 8 | 50 | 3 | 2,520 | 0 |
| 5 | 9 | 96 | 3 | 20,160 | 0 |

三个例子都达到 `floor((n−k+3)/2)=3`。后两个直接落在 1863 的 k≥4 范围。脚本 `verify_small_n_hamilton.py` 与实际输出 `small_n_hamilton_verification.json` 随包交付。这里是**独立有限穷举**，没有声称 Lean 形式化通过，也没有复核稿件的其它 SAT 构造或最小性断言。

**对横贯版的推论（本轮推导）。** 将 H_4 重复 8 次，构成同顶点集的 8 个超图；底层没有紧 Hamilton 圈，所以也不可能有横贯紧 Hamilton 圈。因此 Conjecture 7.5 的全 n 字面版本也被反驳。该推论不反驳充分大 n 的精确横贯版本。

**实际路径。** 名称检索、精确 codegree 公式检索 → EulerSolve/Zenodo 公开声明 → PDF 构造与验证报告 → 本轮独立代码穷举；另以 Letzter/联合作者/报告标题检索 → Toronto 官方报告。

**待复核。** 优先取得充分大 n 新稿，逐一定义阈值、取整与 n_0(k)。禁止将“稿件已公开”作为自动升级已解决的充分条件。

### 2. QX-P-001855、001857、001859—001866、001870：横贯的系统性误译

**旧卡 → 变化。** 多张人话版把 transversal 解释成“顶点分成若干部、每部取一个点”。[原综述 v2](https://arxiv.org/html/2412.01121v2) Definition 1.1 的系统共用一个顶点集；通常是**边**分别使用不同图编号。1855 指定边色普适性还允许规定的颜色重复，不应同时额外要求 rainbow。

逐题修订已写入 JSONL，关键对象包括：1859 的 **K_r-factor**（不是等分独立色类，须 r|n）；1860 的 **oriented graph** 与 `ceil((3n−4)/8)`，不能混用一般 digraph 的 n/2 定理；1861 的偶数阶反定向圈和单图 n/2+1 基准；1862 的非反定向圈系统问题与 tournament 特例；1865 的“同一 d 下有色与无色阈值一致”；1866 的相邻边重叠量 ℓ、tight 的 ℓ=k−1 与整除条件。

**新进展及定位。** [Li–Luo](https://arxiv.org/html/2512.12143v1) Question 1.4 保留原 Ore 圈问题，Theorem 1.5 给 Hamilton 连通性/圈的析取型进展。[GHMPS 已刊全文](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.12896) Theorem 1.3(B1–B3) 已覆盖数组 (k,ℓ,d)；Theorem 2.6 是充分框架，不是所有 colour-blind 族的充要分类。[Tang 等原稿](https://arxiv.org/html/2302.00080v1) §8 Conjectures 8.1、8.2 对齐 1865，后者余量原文 `μ binom(n,d)` 存在归一化疑点，本回传保留原文、提示核对，未静默改公式。

**版本检查。** 1859 的 [2026 勘误](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/rainbow-spanning-structures-in-graph-and-hypergraph-systems-erratum/022C5A6ED0AFB2F7B136AF2C67F9C802) 只修参考文献年份 2003→2023，不改变主定理。1855 的新稿 [arXiv:2611.07421](https://arxiv.org/abs/2611.07421) 本轮仅取得官方索引摘要，多种全文入口失败，应记待核声明。

**路径与待复核。** 各题分别进行名称、公式两组查询，再查原文相应问题号和最新版本；GitHub 的 workshop 日程命中不计证明代码。下一轮应按修正后的宿主与量词查精确阈值，勿继续沿错误“顶点分部”模型检索。

### 3. QX-P-001858：Lohrey 文献不能直接用作自由性多项式定理

**旧卡 → 变化。** [原 MO](https://mathoverflow.net/questions/328165/do-two-integral-matrices-generate-a-free-group) 问给定两整矩阵生成秩二自由群的判定。[Lohrey 已刊文](https://link.springer.com/article/10.1007/s00224-023-10122-2) 的摘要与主定理是 **subgroup membership** 和指数问题；本轮全文搜 `freeness` 未定位对应结论。应将归引收窄，不能把 membership 算法未经推导直接说成“自由性判定多项式”。

**路径与待复核。** 原帖、作者名/题名、GL(2,Z)与freeness组合及已刊全文定位均已查。n=2 自由性可判定性和具体复杂度如要保留，应另给直接定理或完整算法归约；半群自由性不判定结果也不能移作群结论。

### 4. QX-P-001868：原入口恢复，小数校正，最优性仍缺下界

**旧卡 → 变化。** [MO](https://mathoverflow.net/questions/398390/what-is-the-covering-density-of-a-very-thin-annulus-is-it-frac-pi-sqrt51-sq) 与 [MSE](https://math.stackexchange.com/questions/4035664/what-is-the-covering-density-of-a-very-thin-annulus-is-it-frac-pi-sqrt51-sq) 原文均已读到，不能继续标本轮 MSE 不可达。公式 `π√(51√17−107)/16` 实算约 **1.9954213429**；网页小数不一致时以公式为准。

原文展示的是薄环覆盖的构造上界，不是匹配下界。须区别厚度趋零的极限问题与每个固定厚度最优性。指定的 2358 是高维 Kakeya Minkowski 维数题，不等价。另由全库索引发现 1994“圆环并覆盖平面 Kakeya 型”，因本包未给该卡全文，仅登记待定候选及双方版本。

### 5. QX-P-001869：超图 rainbow matching 不应误写为总有全长 n

**旧卡 → 变化。** [BFKY, arXiv:2501.03216](https://arxiv.org/abs/2501.03216) 摘要与版本页已核。对于 n 个、各大小 n 的 r 一致匹配，r≥3 的保证长度参数满足上界 `n−Θ_r(n^(1−1/r))`，因此“普遍全长 n”不是未解决猜想。一般图、r 部 r 一致超图和非 r 部模型分别记录。

**路径与待复核。** 名称与匹配数/长度公式分别检索，追到原作者摘要；精确常数、一般图奇偶性及不同数量参数需后续全文复核。000098 仅索引题名触发，未冒充已读正文的同题关系。

### 6. QX-P-001873—001877、001881：补假设、区分已有子类与一般问题

**1873。** [HMST 最新稿](https://arxiv.org/html/2401.10853v2) Conjecture 1.1 明确要求 **connected bipartite H**。2026 [Jiang–Longbrake](https://arxiv.org/html/2604.05288v1) 推进特定诱导有理指数族，未给全部 H。

**1874/1875。** [Janzer–Pohoata](https://arxiv.org/abs/2009.00130) 已得 t≥d≥3 的 little-o 改善；这不蕴含固定 ε_d>0 的幂改善。1875 的“指数向 2 推进”写反，完整边数指数是从 `2−1/d` 降到 `2−1/(d−ε_d)`。新增这两卡的“特例/强化”关系，不直接合并。

**1876/1877/1881。** [CKS v2](https://arxiv.org/html/2412.06490v2) Theorems 1.1、1.2 已把盒子与满足 y-monotone、general position 条件的伪圆盘界写为线性 t；其引言明确 v2 相比 SoCG 初版的 t^6 改进。圆盘 r=3 的 `O(t n² log n)` 已在范围内，不能再说没有近二次上界。所有“nice”对象仍须逐类定义，尤其共同相交与两两相交不能混为一谈。

**新增 2026 来源。** [Chao 等](https://arxiv.org/html/2604.20815v1) Theorem 1.1 按各部盒子可变方向集是否 2-coherent 给出二分，解释何时能达 `Θ_r(t n^(r−1))`、何时至少须有对数损失。这是特定盒子模型的进展，不能写成所有几何对象的完整分类。

**路径与待复核。** 各题独立名称/公式查询后，打开原始猜想、版本页与新全文定理；核对参数和版本。后续重点是其它对象族、固定正幂改善和全称 H，而不是重复登记已有子类为未解。

### 7. QX-P-001878 / 001879：两处改变研究对象的翻译错误

**1878。** [几何综述](https://arxiv.org/html/2410.03702v2) §5.4 Problem 5.7 的 **strings 是平面曲线**，不是圆内 chords。须保留 K_(t,t)-free 条件，并说明只计跨族相交、忽略族内相交；所得二部图未必是普通 string graph，t=2 已有 Ω(n^(4/3)) 例，所以不能直接套用普通 string 图的线性界。随机弦概率题 1912 与此不同。

**1879。** [原 MO](https://mathoverflow.net/questions/219860/a-kaleidoscopic-coloring-of-the-plane) 求两个 Lebesgue 可测集等分每个单位圆盘面积，等价于 ±1 可测函数与圆盘指标卷积为零。现卡“每个有限配置各色齐备”属于另一类问题，需整段重写。

**公开 AI 线索。** [UQ #66](https://uq.stanford.edu/question/66) 有九个模型回答；页面显示 o3 的 Failed Human Verification，以及 Gemini 的 Failed UQ Validation / Needs Human Verification。Gemini 所引 Kolountzakis 否定论文题名经精确检索未独立找到，不能把模型回答记为文献证明。

**路径与待复核。** 先按卡面词检索，发现 G-space 命中失配；恢复原帖后改用 measurable/unit disk/convolution 再查。错误词串查询如实登记“命中不适用”，不隐藏失败路径。

### 8. QX-P-001880：新 r=3,t=2 全解声明仅取得摘要

**旧卡 → 变化。** 官方索引新增 [Dean Menezes, arXiv:2609.22381](https://arxiv.org/abs/2609.22381)，题名 *The Three-Dimensional Erdős Box Problem Has Exponent 11/4*，声称匹配 K^3_(2,2,2)-free 构造。abs、HTML、PDF 多次取得 DisabledError，因此只可记**完整证明声明待核、仅标题/摘要**，不能标已证。

即使该稿正确，也只是 r=3,t=2，不解决一般 r,t。原卡还把 K^r_(t,…,t) 的 r 个各 t 顶点的部分写反，须修正。交叉数 Zarankiewicz 的 AI/Lean 声明与本题最大边数无关。

### 9. QX-P-001882：恢复4维基本块，使用修正后的论文版本

**旧卡 → 变化。** [原 MO #113875](https://mathoverflow.net/questions/113875) 的 Mikhalkin pants 为实四维基本块，不是二维三个边界圆的裤子。[Golla–Martelli](https://arxiv.org/abs/1503.05839) v3（2016-09-14）版本说明明确修正旧稿 Theorem 2 的错误证明，应使用 v3/2017 已刊版。

任意有限表示群的实现性不是所有4流形可分解性的判别；[Zhang](https://arxiv.org/abs/2102.10037) 的特殊曲面分解还涉及 K3 子集，不能当作纯 pants 全分类。需继续核允许的面拼接与边界塌缩定义。

### 10. 查重新增与明确不应合并的谱系

全库索引实际扫描 2,469 条；本组 23 个指定对子均对照本包正文。新增明确关系：1855/1856 为一般普适性与指定 Hamilton 精确阈值；1872/1871 为平衡参数特例；1874/1875 为 little-o 与固定幂改善。新增仅索引候选 1868/1994、1869/000098 标待定，均保留双方 card_rev。

000270 与 000835 的 Zarankiewicz 交叉数/有符号数线索，不等于 1873、1877、1880 的禁子图极值问题。1863/1864 则是单图与系统强化关系，不能合并丢掉量词。所有合并操作均未执行。

## 第26—50题：经核查的变化

### 1. 可改变子问状态的已知定理

#### QX-P-001908 · f0eb742bb8763eaf：四维D4已经回答“还有别的维数吗”

**旧卡 → 变化。** 旧卡已把“perfect”校准为locked/几何刚性，仍把1、2、8、24之外的存在性整体当开放，并引用评论暗示四维没有。按这个刚性口径，四维D4/24-cell就是已知肯定例。

- Musin，*The kissing number in four dimensions*，Annals168(2008)1–32：κ(4)=24。[出版社原文页](https://annals.math.princeton.edu/2008/168-1/p01)，摘要；
- Cohn–Jiao–Kumar–Torquato，*Rigidity of spherical codes*，Geometry & Topology15(2011)2235–2273：[已刊PDF](https://msp.org/gt/2011/15-4/gt-v15-n4-p11-p.pdf)，Proposition3.3（pp2243–2244）证明D4 infinitesimally jammed；Theorem2.2（p2240）推出jammed。
- [原MSE问题](https://math.stackexchange.com/questions/3868726/perfect-solutions-to-the-kissing-number-problem-besides-in-dimensions-1-2-8-a)正文未严密定义“perfect”，

**适用范围。** 得到一个额外维数的最优刚性例，不是完整维数分类；整体旋转必须视为平凡运动。24-cell是否唯一最优不是此存在性子问的必要条件。D_n/E6/E7的刚性也不自动证明它们达到对应维数的最优接吻数。

**实际路径。** `perfect kissing configurations dimensions`、`jammed kissing 24 cell` → Cohn等原始论文 → `Musin kissing number four dimensions 24 arxiv` → Annals出版社结果。

**复核。** 卡片应明确jammed、locally jammed或sharp code口径；若保留当前几何刚性释义，存在性改已证并列n=4。

#### QX-P-001883 · 21eeaad12d662501：squarefree Erdős–Kac已有直接现代引用

**旧卡 → 变化。** 原帖本来是作者自称已有证明的folklore文献请求。新定位的Fan论文可直接取权重μ²，覆盖原帖的有界强加性正态极限定理，不能继续以无回答当作数学命题未证。

[Fan，Weighted Erdős–Kac theorems via computing moments](https://stvfan.github.io/files/papers/WEK_online%20first.pdf)，作者提供Acta Arithmetica Online First副本：p5列μ²∈M*并定义A、B；p6 Theorem2.1；p10 Corollary2.5。取α=μ²、β=σ0=1，得到与原帖相同的A(x)=Σf(p)/p、B(x)=Σf(p)²/p及按squarefree个数归一的正态极限。

[MO原帖](https://mathoverflow.net/questions/84754/erdos-kac-for-squarefree-numbers)，

**适用范围。** 必须保留素数值统一有界、B(x)→∞。强加性还要求f(p^k)=f(p)，旧卡仅写互素可加是普通加性定义。以上是核定假设后的特例引用，不是重新证明。

**实际路径。** `Erdos Kac strongly additive squarefree theorem` → 作者PDF → 查Theorem2.1、Corollary2.5、Möbius → 核α=μ²与A、B定义。

**复核。** 最早历史文献及最终卷期/勘误尚未核定；作者副本首页出版日期仍有星号占位，不能伪填卷页。

#### QX-P-001907 · 0051647bbb11faf5：一个标准projective范围已有已刊答案

**旧卡 → 变化。** “Banach/纯代数已知”的范围可扩充到完备Hausdorff局部凸TVS配完成projective tensor；其他张量拓扑不能一并改状态。

[Stolz–Teichner，Traces in monoidal categories](https://people.mpim-bonn.mpg.de/teichner/ewExternalFiles/Traces-Offprint.pdf)，TransAMS364(2012)4425–4464，p4426明确给出上述范畴中dualizable iff finite-dimensional，§4.5给设定。[MO原题](https://mathoverflow.net/questions/471619/are-dualizable-topological-vector-spaces-finite-dimensional)，

**实际路径。** `dualizable topological vector spaces finite dimensional` → Stolz–Teichner原论文 → p4426及§4.5。

**复核。** injective、inductive、非局部凸空间、任意monoidal子范畴仍需各自处理。C[T]-模的反例不是单位对象C的TVS反例；Scholze的Fredholm评论不替代完整论证。

### 2. 同一作者的新声明与最新清单相冲突

#### QX-P-001885 · b69cfcd8129338fb：六解存在性，另有五解无穷族冲突

**旧卡 → 变化。** 人话版把问题改成固定a,b,c的计数增长阶，原题实为存在互异正整数a1,a2,a3使乘积为平方的不同正整数x至少有六个。

[Dujella的MO原题](https://mathoverflow.net/questions/511399/how-often-can-an1bn1cn1-be-a-square)，2026-07-26 EDIT报告Sadowski首个五解无穷族：a1=1、a2=12t+7、a3=12t²+19t+8，Pell型条件s²=33t²+46t+17，并列五个x。更新段L50–52。

但是[Dujella最新问题清单](https://web.math.pmf.unizg.hr/~duje/pdf/open2.pdf)封面写2026-11-14，p2 Problem1.5仍称不知是否有无穷多五解例，且六解主问未标Solved。

**判定。** 六解主问未由这些资料解决；五解无穷性记录为“完整声明待核”，明确两份原作者资料冲突，不自行猜测撤回、遗漏更新或正确性。旧卡“最好五解仅3组”已不符合原帖列例数量。

**实际路径。** MO编号/`Dujella (ax+1)(bx+1)(cx+1) square solutions` → 原帖 → 点击open2.pdf → 核最新日期及Problem1.5。

**复核。** 优先核五解族的Pell无穷性、正参数、五个x互异及是否有勘误。未运行Magma或外部代码。

### 3. AI完整解声明、形式化有限排除与主问须分开

#### QX-P-001890 · b83b6e0f6c9a354c：额外公理已在固定提交源码中确认

**旧卡 → 变化。** 当前人话版漏掉有限、模数两两不同且>1；不加这些条件，用模3的三个剩余类即可覆盖所有整数。

本轮确有AI完整反证声明命中，不应写“未发现AI”。

| 对象 | 已核位置 | 本轮判定 |
|---|---|---|
| Archivara/Aristotle相关总反证 | [spicylemonade/erdos-007固定提交main.lean](https://github.com/spicylemonade/erdos-007/blob/90eae934a8ae01e68697f1445b4306c6d1eb5330/main.lean)，第631行`axiom HoughNielsenGoodFibre`；第653/685行总定理 | 已取源码；依赖额外公理，HoughNielsenFact另作参数；未重跑，不是无条件全解 |
| Mian–Siddique有限排除 | [arXiv2607.25628v1](https://arxiv.org/abs/2607.25628)，28July2026；[centurion固定提交Enumeration.lean](https://github.com/ibrahimmian36/centurion/blob/76ed2325673ade215d8ce56e2c6d66bffd6d0ed4/Erdos7/Enumeration.lean)，第366行 | 仅断言有限distinct odd>1覆盖的lcm>10000；作者明确数学界已知，贡献为形式化 |
| 形式化对应/依赖 | centurion同提交`Bridge.lean`、`lake-manifest.json` | 核到对应有限覆盖目标；Mathlib pin为`c5ea00351c28e24afc9f0f84379aa41082b1188f`；未重跑/未完整审公理闭包 |
| Lee总反证 | [公开审计记录](https://erdosproblems.ai/wiki/problems/covering_systems/E0007/claims/2026_05_02_lee) | 二级社区记录称核心axiom错误、作者承认；本轮未取得原Zenodo/原论坛完整过程，保留为待复核线索 |

源码由GitHub connector直接读取，没有生成web引用号，固定URL已列。

**实际路径。** `odd covering distinct moduli 2026`、Erdős7公式/限制 → GitHub+Lean及AI组合域查询 → claims目录 → 原arXiv与两个作者仓库 → GET branch取得固定SHA → 读取主定理、桥接及manifest。

**复核。** 总问题仍不能改已解。需要验收Lean时，必须独立构建并审依赖；主问与lcm≤10000有限范围、squarefree变体分别记录。

#### QX-P-001901 · 6c52e94a220e68b8：Lean无限性不等于正上密度

[Ding–Sun–Zhao arXiv2607.05357v1](https://arxiv.org/html/2607.05357v1)，Theorem1.1给出任意η>0、充分大x的下界

\[
N(x)\gg_\eta x\exp\!\left(-(4+\eta)\log x\,\frac{\log\log\log x}{\log\log x}\right).
\]

这仍不能推出正上密度。旧卡`log³log`必须改成明确的三重迭代对数，不能读作三次方。

[Formal Conjectures固定提交9.lean](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/ErdosProblems/9.lean)第78–79行原正上密度目标仍为sorry；第70行无限性变体链接到[linrock固定提交Solution.lean](https://github.com/linrock/math-proofs/blob/de08009e59829727653bfa20b8d8f7ed1b1baf79/erdos-9/Solution.lean)，其目标只是`Erdos9A.Infinite`，调用`Erdos9Unified435`。已取入口代码，未审全部依赖、未重跑。

**实际路径。** Erdos9/density与Ding–Sun–Zhao编号检索 → 原arXiv HTML → GitHub索引命中 → connector读取固定提交及外链。

### 4. 必须重写或补齐的题面

#### QX-P-001902 · 1080b10296cd19a1：四灯是一个元素的重量，不是四个生成元

**旧卡 → 变化。** 人话版“F*最少用4个元素生成”完全错误。原题取p>5素数，在p位F2偶权重循环模式中做卷积；当ord_p(2)=p−1时C_p是有限域，问是否总有一个恰四灯的模式A，其乘幂遍历全部非零元，即在指定表示中寻找重量4的本原元。

[原题](https://mathoverflow.net/questions/516565/can-four-lights-generate-every-nonzero-element-of-this-field)，Question与p≤269作者穷举、p11例，

**路径。** 516565编号、`four lights field` → 原题 → 运算、Question、Sawin评论逐项核对。

**复核。** 作者计算未独立重做。当前所取正文没有旧卡Claude致谢，需读修订史才可标成本轮已核AI辅助。

#### QX-P-001895 · 0d9e536bac87f388：No被误翻成*R，GB+AC被改成ZF

[Hamkins原题](https://mathoverflow.net/questions/227849/is-the-universality-of-the-surreal-number-line-a-weak-global-choice-principle?noredirect=1)，正文L32–48。

**旧卡 → 变化。** 题目是超现实数No的类线性序普适性UNo：所有类大小线性序可序嵌入No。已知globalAC⇒UNo，问GB+AC是否已经可证、逆向是否成立、是否严格中间原则。与非标准超实数*R的超滤子/饱和性无关。

**路径。** weak global choice/universality、surreal UNo → 原题及作者解释二阶类集合论评论。

**复核。** 旧卡Hamkins2021预印本只作为历史线索，本轮未打开确认其后续开放标签；不写“未有任何已知蕴含”。

#### QX-P-001899 · 0900ff9ce6e0064d：平移尺度独立、连通穿一对相对边

[原题](https://mathoverflow.net/questions/120415/does-every-connected-set-that-is-not-a-line-segment-cross-some-dyadic-square)，

**旧卡 → 变化。** 原方格是x+2^(-n)[0,1]²，x∈2^(-m)Z²，m,n≥0独立，非每级标准划分格。作者评论明确否定m≤n限制。crosses要求A∩S里存在连通子集碰一对相对边，不是只碰边，更不是历史备注的“两对边”；A要求非平凡、闭且连通。

**源帖自身待澄清。** 正文以整条45°直线为不穿越例，又询问不是line segment的闭连通集，未明写紧性。严格理解有界线段时有歧义；不可自行补紧性后宣称已忠实重述。

**路径。** connected/dyadic square、原编号 → 原文定义 → Rote与作者回复。相关MO446092仅搜到未全文核，未采用其路径连通正解声明。

#### 其他题面/范围校正

| 题号与版本 | 旧卡 → 建议变化 | 原始定位 |
|---|---|---|
| 1884 · 8c7fd49aeb361b92 | 任意拼串矩阵/比较算法 → H_b=tridiag(1,b_i,1)的a_n计数与碰撞分类；W0W1W构造是部分结果，本轮未复算旧数据 | [MO514920](https://mathoverflow.net/questions/514920/when-do-two-binary-strings-have-the-same-characteristic-polynomial)，Q1/Q2与未完成回答， |
| 1886 · 5e3bfed5f8cbc7d0 | 指定π幂插值 → 代数系数、C上亚纯、统一d、f(2n)∈Qbar·π^(2nd)的例子/联系；实极点⇒负偶数零点另问 | [MO504373](https://mathoverflow.net/questions/504373/dirichlet-series-that-gives-power-of-pi-at-positive-even-integer?noredirect=1)，正文定义与末猜想， |
| 1887 · 05c2d5aca128083c | 只要求有理临界点 → 全部临界点必须单且在P¹(Q)；不是所有极点都临界；不同临界值另问 | [MO486998](https://mathoverflow.net/questions/486998/rational-functions-over-mathbbq-with-rational-critical-points)，首段/EDIT， |
| 1888 · b173db6cab3cfd99 | 模糊Manin簇 → 四个n×n块的精确交换关系、q量词；n=2可逆块枚举不能冒充一般计数证明 | [MO468145](https://mathoverflow.net/questions/468145/number-of-f-p-matrices-ac-ca-bd-db-ad-da-cb-bc-is-polynomial-in-p)；[pjt33 Gist](https://gist.github.com/pjt33/53159baa48054789c6affdc8a7d0b930)，；revision页受限 |
| 1889 · 5cff9c95264470cc | 任意极大子群 → 给定196883维实表示中的极大闭子群；Monster自身极大子群分类包含方向相反 | [MO464253](https://mathoverflow.net/questions/464253/is-the-monster-group-maximal-in-so196883)，正文closed， |
| 1891 · e8be3e76bc998b4c | 自然同调局部系统 → 从MCG固定的不可约曲面群表示构造的局部系统；g≤2反例报告、低秩肯定与一般子问分开 | [Litt原帖](https://mathoverflow.net/questions/345955/are-these-local-systems-on-mathscrm-g-1-motivic)，2022编辑， |
| 1892 · 5d5c951b9bf0d152 | “一致有限” → 每条E/K分别有限秩；原帖更强有限生成另列，E/Q已知结果不能外推E/K | [MO291268](https://mathoverflow.net/questions/291268/infinite-extensions-such-that-every-elliptic-curve-has-finite-rank)，首段， |
| 1894 · 6a7efebd554edc08 | 数值det(A)是否y⁸ → H₃(O)实线性嵌入24×24矩阵使多项式恒等式成立；对称与一般End两版本分开 | [MO278981](https://mathoverflow.net/questions/278981/when-is-the-determinant-an-8-th-power)，Question与后两段， |
| 1896 · 76d5537e6c1ddccb | 初等生成所以有界 → 必须引用Carter–Keller；48初等矩阵宽度与48固定循环因子次序未核 | [Morris作者讲稿](https://deductivepress.ca/dmorris/talks/BddGenSLn.pdf)，；MO218056本轮多个入口不可达 |
| 1903 · 26627679d1af685d | 多项式或有理函数 → 整系数多项式映射；原始Vaserstein支持3变量不够而非4不够，暂记4≤N≤46 | [Vaserstein Annals PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n2-p07-p.pdf)，p979–980、Theorem1，；Zannier原PDF403 |
| 1906 · 33656ada7e0ec637 | R⁴计数本身未知/闭四维不可数背景 → 原帖已列R⁴连续统、闭流形至多可数；补第二可数/连通/Hausdorff/无边界 | [MO474243](https://mathoverflow.net/questions/474243/must-the-number-of-smooth-structures-be-countable-or-continuum)，Edit1/3/4、Silver讨论， |

### 5. 新近来源及原始定理范围补强

#### QX-P-001897 · 87a74eb814c57720

[2026 K3问题集](https://bpb-us-e2.wpmucdn.com/websites.umass.edu/dist/b/22144/files/2026/04/K3-problem-list-watermarked.pdf)书页163、Problem3.44再次提出给定open book判定tight或fillable的算法。这是较新来源，不只是Pardon2015帖子未答。标题“纽结”应删除。Right-veering等判据不自动保证全输入停机算法。实际路径：tightness decidable/contact algorithm检索 → K3 PDF → find Problem3.44。

#### QX-P-001898 · 0aa6ccb40db76a03

[Eckhardt arXiv2307.08841v2](https://arxiv.org/html/2307.08841v2)，TheoremA；发表于Adv.Math444(2024)109628：有限生成虚幂零群的**不可约表示**生成C*代数可分类，因此满足UCT。2016 Eckhardt–Gillaspy对应幂零情形。旧卡应明确这些是primitive quotient范围，不能写成任意理想商已全部解决。实际路径：UCT/quotients/virtually nilpotent检索 → 作者出版列表/期刊 → arXiv最新版与TheoremA。

### 6. 查重：5个指定对子全部按正文复核，不合并

| 左卡（本组版本） | 右卡（参考版本） | 关系与正文依据 |
|---|---|---|
| QX-P-001886 · 5e3bfed5f8cbc7d0 | QX-P-002039 · 4c9986227a01d647 | 相关但不等价；一个问π特殊值函数类，一个固定乘法分拆系数问解析延拓 |
| QX-P-001886 · 5e3bfed5f8cbc7d0 | QX-P-002478 · 75ff62b0e87f0fe1 | 相关但不等价；固定三个倒幂的实t零点问题不含正偶数π特殊值假设 |
| QX-P-001887 · 05c2d5aca128083c | QX-P-002065 · e0660e38b7a5d02c | 相关但不等价（实际无同题数学关系）；Q有理函数分歧点 vs 有限群非自逆共轭类/中心化子平方阶免特征标证明 |
| QX-P-001896 · 76d5537e6c1ddccb | QX-P-002466 · 59d2c0d76219185e | 相关但不等价；整个SL₃(Z)固定循环因子乘积 vs 所有有限生成子群有限表现 |
| QX-P-001898 · 0aa6ccb40db76a03 | QX-P-002094 · c2fd85fa8af76d71 | 相关但不等价；群C*代数商UCT vs 代数张量积第三种C*范数 |

新增索引线索仅作待定，不扩成新查新任务：

- 1885 ↔ QX-P-000734 · 787757e13b2c3d9a：Dujella triple整点反例标题接近，须取得正文确认猜想编号和量词。
- 1908 ↔ QX-P-000295 · 0c11563a24e37cc2：5/6维精确接吻数与最优构型刚性有背景联系，但只读索引不能判同题或特例。

### 7. 优先复核顺序

1. 1885两份同作者2026来源冲突：查五解无穷族完整证明与是否勘误。
2. 1902、1895、1899、1894先修数学对象/量词，避免针对错误题面评价求解状态。
3. 1908明确jammed口径并纳入四维肯定例；1883按Fan定理归入已有结果/文献请求。
4. 1890全反证必须处理good-fibre额外公理；如需形式化验收，使用本报告固定提交独立构建与完整依赖审计。
5. 1896原帖仍不可达、1903下界来源冲突，勿把历史记录写成本轮已核精确界。

所有“暂未找到可验证结果”只描述本轮已列入口范围；不由零命中推断数学开放性。

## 第51—75题：经核查的变化

### 1. QX-P-001935｜caf721ada4a34e53：被误认“幻觉”的真实Hexagon预印本

**旧卡 → 变化。** 旧卡查到arXiv同号不是目标论文，即认定“2611.00689预印本不存在”。本次确认目标实际为 **Hexagon:2611.00689v1**，并非arXiv编号。页面记录2026-11-20、v1 current；PDF署日期2026-11-19。

- 原稿：[Character coefficients for integrals of odd products of hyperbolic tangents](https://hexagonmath.org/pdf/2611.00689v1)，2页，**Theorem1.1、式(1)及其证明**。贡献者为Will Howe、Grant Huffman、Jensen Kohlmeyer、Liam Kruer。
- [原始发布页](https://hexagonmath.org/2611.00689v1)明确标主要AI生成文本、所有部分经人理解；PDF另明确致谢Codex参与探索、检查、证明起草与文稿准备。
- [aiXiv:2611.02128](https://aixiv.online/abs/2611.02128)是索引，来源栏回指Hexagon；页面没有仓库或复现报告。其“tools none named”摘要不应覆盖原稿明确的Codex致谢。

**范围。** 声称对每个奇数n≥3给出原始偶Dirichlet L函数在−1处导数及对数项的有限系数公式；对数系数有理，导数项系数可为代数数并成共轭对。它精确引用MSE5150767。不得把这个声明扩写成所有系数均有理或所有偶n均由该文重新解决。

**判定。** 完整证明声明待核；已读两页全文，但没有独立完整审稿、复算、Lean核验或同行验证。应删去旧卡的绝对“幻觉已证伪”结论，改“奇n有2026完整证明声明待核”。

**实际路径。** 题名与`tanh(kx) Dirichlet integral`检索 → Hexagon/aiXiv命中 → 两个发布页和PDF全文 → system1近期题名复核。工具定位：、、。

**复核。** 每个单位根处极点阶数、周期系数、特征标正交分解、诱导特征标Euler因子、s=−1解析延拓与有理对数系数的Galois论证。

### 2. QX-P-001929｜a3b10b4441a81b90：基本群包括n=4已能直接引用已刊结论

**旧卡 → 变化。** 旧卡“n=4未明、其余仅未发表评论拼装”的基本群结论应撤销。Friedl–Nagel–Orson–Powell的2025正式专著已有直接定理。

**直接来源。** [NYJM Monographs6(2025)正式PDF](https://nyjm.albany.edu/m/2025/6p.pdf)，**pp.53–54，Proposition7.5、7.6**及其后正文。Prop7.5明确n≥4时TOP(n)/O(n)到K(Z/2,3)为5-connected；n=4的证明单独引Freedman–Quinn1990 **Theorem8.7A**。Prop7.6及紧接的正文给出所需基本群。[arXiv v3](https://arxiv.org/html/1910.07372v3)为2024-01-02版本，也已核同一命题。作者旧站100页稿较旧，不能与正式版混用页码。

以恒等映射为基点，有

\[
\pi_1(\operatorname{Homeo}(\mathbb R^n))=
\begin{cases}
0,&n=1,\\
\mathbb Z,&n=2,\\
\mathbb Z/2,&n\ge3.
\end{cases}
\]

Homeo与固定原点子群之间的平移因子Rⁿ可缩；n=1保持定向分支用线性插值可缩。**仅基本群子问记原题已证**；原帖更广泛询问的全部高阶同伦群未作全面判断。

**实际路径。** `Fundamental group Homeo`、`pi_1 TOP(n) Kirby` → 最新调查论文 → arXiv版本历史 → v3 Proposition7.5/7.6 → 作者出版信息 → 2025正式PDF对应页。工具定位：、、。

**复核。** 正式回填时保留紧开拓扑、基点与维数范围；不要把该低阶结论写成所有高阶群已算出。原书FQ1990未在本轮逐行审读，本轮证据为已刊专著给出的定理与推导。

### 3. QX-P-001928｜3c1e142330dbfad9：定义符号错误；无底数限制的校正版全称命题有反例

**旧卡 → 变化。** [原帖定义](https://math.stackexchange.com/questions/4754539/does-reinterpreting-the-base-of-a-number-leave-transcendence-unchanged)中D_{a,i}提取小数第i位，却乘b^i。取x=1/2、a=b=2就得到2而不是1/2；无穷非零小数位的正向权重和还会发散。应先改成b^{−i}，或同时反转数字索引。该错号是源帖已有，不只是中文转录问题。

**本次直接推导的反例，不是文献新成果。** 原文没有a≤b限制。按预期修正为负指数权重后，取a=3、b=2，将三进制小数每两位分一块。第k块在k=m!（m≥2）时取`10`，其他时取`02`。其三进制数为

\[
x=\sum_{k\ge1}2\,9^{-k}+\sum_{m\ge2}9^{-m!}
=\frac14+\sum_{m\ge2}9^{-m!}.
\]

\(\sum_{m\ge2}9^{-m!}\) 是Liouville数。截断至m=M时分母可取\(q=9^{M!}\)，余项小于\(2q^{-(M+1)}\)，从而有任意高次有理逼近；加上1/4仍超越。也可以直接用分母\(4\cdot9^{M!}\)对x应用同一估计。

但按二进制权重读取数字时，两种两位块给出相同贡献：

\[
0\cdot2^{-(2k-1)}+2\cdot2^{-2k}
=1\cdot2^{-(2k-1)}+0\cdot2^{-2k}
=2\cdot4^{-k}.
\]

所以\(R_{3,2}(x)=\sum_{k\ge1}2\cdot4^{-k}=2/3\)，为有理数。**这反驳“先修权重、再保持原文任意整数a,b>1”的全称版。** 数字2不是合法的标准二进制数字，但原文代数定义明确容许所有a,b，正是需要澄清的范围问题。

**不覆盖。** π的6→10特例、限制a≤b的版本，以及要求每个数字都属于目标字母表的版本，均未由该反例解决。旧卡“有理性平凡保持”也应附合法数字条件，不能泛化到原文全部底数。

**实际路径。** 精确题名、数字/超越性特征检索 → 原帖全文核定义和量词 → 较早[MSE1870691](https://math.stackexchange.com/questions/1870691/can-a-change-of-basis-modify-irrationality-transcendence/1872074)的条件性讨论 → 本次两位块短推导。已另行交叉复核反例代数和Liouville逼近；没有形式化运行。

### 4. QX-P-001913｜2c011dc8f463a0ee：原题被改写；遗漏多项式自同构文献

**旧卡 → 变化。** [MSE3040494](https://math.stackexchange.com/questions/3040494/are-all-verbal-automorphisms-inner-power-automorphisms)问Va(G)=Ip(G)，Ip由内自同构与幂自同构生成；中文草稿改成Va(G)=Inn(G)，导致题目变化。无限群时“Va总是正规子群”本身也不成立。

**直接来源。** Endimioni，[On the polynomial automorphisms of a group](https://acta.hu/download.phtml?id=2926)，Acta Sci.Math.(Szeged)73(2007)，**pp.61–62**及参考文献[7]；[arXiv:0704.0500](https://arxiv.org/abs/0704.0500)仅v1。

- 定义与本题含常数的一元群词自同构吻合。
- p.61举(Q,+)中x↦2x，但其逆x↦x/2不是整数指数词，否定无限群自动成为子群的附带断言。
- p.62报告存在有限G使P(G)/Inn(G)非可解，并引 **Kowol, Polynomautomorphismen von Gruppen, Arch.Math.57(1991),114–121，DOI10.1007/BF01189997**。

有限G时多项式自同构集合为群且等于P(G)。另一方面，幂自同构两两交换，且与所有自同构交换，所以Ip(G)/Inn(G)为阿贝尔。因此该已刊存在性结论提供否定Va=Ip全称命题的直接文献链。

**判定。** 无限群子群断言已反驳；校准后的Va=Ip全称命题暂保守列“完整反例文献声明待核”，因为Kowol具体有限群构造原文未取得。不能继续以MSE/MO零回答当作开放证据。

**实际路径。** verbal automorphism → polynomial automorphism同义检索 → Endimioni arXiv → Acta正式PDF → p.62引文 → Kowol DOI尝试失败。定位：、；Kowol入口失败。

**复核。** 取得Kowol正文，落实具体有限G及词表示，再正式登记原全称命题已反驳；保留对无限群“集合”与“生成群”的区别。

### 5. QX-P-001924｜1223c96b0f659cc7：2026限制取向进展，不能升级全题

**旧卡 → 变化。** [作者研究页Prime squares and half-turns](https://vamshij.com/research/prime-squares-half-turns/)记录v1日期2026-10-10，给两条受限结果：所有素数p的平移+半转；奇素数p的平移+一种固定反射。两条均不要求块连通。

**范围。** [原题MO487157](https://mathoverflow.net/questions/487157/is-there-only-one-way-to-dissect-a-p-times-p-square-into-p-congruent-p-omi)允许任意旋转反射。作者明确90度旋转或两种反射超出证明，所以一般原题未被覆盖。

**形式化。** 作者声称Lean4验证代数核心，Laurent环唯一分解及铺砌编码作为引用输入；作者声明使用Claude。仅[GitHub PDF文件页](https://github.com/jvvk/mathematics/blob/main/prime-squares-half-turns/paper/note.pdf)可达，目录、README和raw内容请求失败。本次没有拿到固定提交、精确定理路径或代码依赖，更没有重跑。只能登记作者部分形式化声明。

**实际路径。** 原题名与p-omino特征检索 → 作者页面 → 原MO核允许变换 → 点击论文/仓库 → GitHub/raw失败 → system1近期核查。定位：、`/6`。

**复核。** 获取预印本实际证明和固定提交；核Lean中被引用假设；继续追踪完整D4取向版本。

### 6. QX-P-001915｜71e2034a0c26b70d：OEIS映射不等价

原题允许a1≤…≤an，区分两两和的`<`与`=`。[A231074](https://oeis.org/A231074)与[A231085](https://oeis.org/A231085)采用严格递增输入，后者进一步要求和互异。

简单核验：n=3时原题有4种弱序，两个序列的n=3项均为1；即便输入严格，n=4原题也区分中间两和小于、等于、大于三种，而序列值为2。因此原帖评论中的“就是这些OEIS序列”不应原样沿用。[MO186515](https://mathoverflow.net/questions/186515/number-of-orders-of-k-sums-of-n-numbers)的区域计数与2024面计数评论是相关线索，仍需匹配闭排序锥中的各维面。A231085的n=7项另于2024修正为4680。

实际路径：原帖定义 → OEIS两条完整定义/例子 → MO超平面排列讨论。定位、`/1/2`。索引候选QX-P-001177（585de00134c27cd7）仅取得X+Y排序标题，关系记录“待定”，不据标题并题。

### 7. QX-P-001916｜d2bce9debd8133a0：已证结论补足复矩阵及多因子直接定理

旧卡已标解决，本轮加强证明定位：[Ogasawara2024](https://jbds.isdsa.org/public/journals/1/html/v4n2/ogasawara/) **§3 Theorem3**给实矩阵任意因子版本；[Le等PMLR162(2022)](https://proceedings.mlr.press/v162/le22a/le22a.pdf) **p.5 Lemma3.5**明确复矩阵和酉因子版本。对一个因子乘相位使迹实且非负，即得到绝对值上界。无需依赖旧卡的6万次数值验证；本轮没有重跑该计算。

实际路径：多矩阵迹不等式题名/特征 → Ogasawara全文定理 → PMLR全文查Kristof → Lemma3.5。定位、。矩形矩阵另有适配问题，不在本题同阶方阵结论中混写。

### 8. QX-P-001927｜04ab93247d58b262：不只n=7；极限已有公开评论

[BBB作者稿](https://carmamaths.org/resources/jon/sinc-sums.pdf) **Theorem1、pp.8–9 Example3/4及式(27)–(30)**提供一般方法。按其Poisson框架，同频sincⁿ的傅里叶变换为区间密度的n重卷积，在(−n,n)正，因此a_n=b_n恰为1≤n≤6，而n≥7误差严格正。

[原帖](https://math.stackexchange.com/questions/4918505/when-is-sum-k-in-mathbbz-left-frac-sinkk-rightn-int-inf)现有a_n的有限公式，且Dave在**2024-05-18评论**已指出a_n→1、b_n→0；故c_n→1不能再归为本库“未发表独立发现”。该极限也可分别以Σ1/k²和sinc²作支配直接验证。相等判别与极限可登记已解决；未将笼统“简单关系”的所有可能加强一并解决。

实际路径：sinc名称/公式 → 原帖全文 → BBB全文、定位Example3/4 → 归属核对。定位、、。

### 9. QX-P-001923｜5392238e48ab4485：角速度被改成姿态；公开AI否定证明有缺口待核

[原MO题](https://mathoverflow.net/questions/448773/can-a-4d-spacecraft-with-just-a-single-rigid-thruster-achieve-any-rotational-v)已经给完整模型：存在M、简单反对称T，使非负输入f(t)驱动任意角速度Ω0到Ω1。旧卡人话版的任意姿态转移及“没有具体模型”应重写。

[UQ的GPT-5答案](https://uq.stanford.edu/answer/06724448-e7f0-4121-80e0-43d648489f2d)，2025-09-02，声称一般否定；页面同时标 **Needs Human Verification**，没有review。其误差估计O(t1ε²)针对固定t1。缩放L_k(t)=kL(kt)时终止时间变t1/k、总冲量变kε，误差只变O(k)，不能自动相对主项趋零。故“由局部障碍推出任意时间全局不可控”的桥梁须补证。

登记完整反例声明待核，不能依据UQ Validated标签写已反驳。AI暴露应改有明确公开证据。实际路径：题名system1 → MO全文 → UQ139及单独答案页；定位`/1`。

### 10. QX-P-001914｜cb98e0b84671fa25：直接引用本题的2024构造论文

Manuell–Wrigley，[The representing localic groupoid for a geometric theory](https://arxiv.org/html/2305.15209v2)，**Theorem4.1、参考文献[23]**直接引用MSE2728171。版本v2日期2024-04-18，对应Expositions in Theory and Applications of Categories2024 No.2 pp.1–41。TAC PDF超时/502，arXiv HTML全文可达。

通用语法构造是实际文献进展；本次没有把它具体落实为方案small étale topos的几何群胚，不能仅因引用本题而判完全解决。small/big étale区别及分类理论选择仍须说明。实际路径：原MSE/MO → 题名检索 → arXiv版本历史/全文 → Thm4.1及引用定位（`/5`）。

### 11. 其他会改变题面或证据口径的修正

| 题号与版本 | 旧卡 → 本次修正 | 直接出处与定位 |
|---|---|---|
| QX-P-001910 / 9b6f3f75cfa40861 | 原帖已将“+1”明确成X∪{X}，不再标为缺定义。 | [MSE3738034](https://math.stackexchange.com/questions/3738034/is-this-statement-equivalent-to-ac?r=31)，题干后部。 |
| QX-P-001912 / c06c0172d3ca6fe2 | 原模型已指定两端点独立均匀于圆周；比较各边数的总面积，不是块数或中心单块。 | [MO481060](https://mathoverflow.net/questions/481060/the-stained-glass-window-problem-draw-many-random-chords-in-a-circle-which-k)，题干、Peter Taylor模拟评论。 |
| QX-P-001918 / 955ff33b980c6f6a | 补[MO385173同题](https://mathoverflow.net/questions/385173/are-all-linear-vector-fields-geodesible-vector-fields)；连续生成元的收缩应以Reλ<0说明，不能直接抄离散映射的模长<1。反向收缩覆盖整体膨胀。 | [MO409161回答](https://mathoverflow.net/questions/409161/is-a-linear-vector-field-a-geodesible-vector-field/410733)，Verbitsky模型；其引文Thm2.24本轮未读。 |
| QX-P-001920 / 5f4a378013b688d5 | ∥改|；要的是至少三阶整除，且p<q、二者素数。 | [MSE456744](https://math.stackexchange.com/questions/456744/can-pq-1-equiv-1-pmod-q3-for-primes-pq)，题干。 |
| QX-P-001921 / aef306682d6dcbb9 | 目标是任意秩平凡丛，不是张量单位；“秩>1不可能”的解释无效。可见负面K0回答混虚类/实际丛、概形/CW，不可采作反例。 | [MSE4046526](https://math.stackexchange.com/questions/4046526/does-every-vector-bundle-have-a-tensor-inverse)，题干、hm2020答复及Zhen Lin评论。 |
| QX-P-001922 / 39a60b0054b8dcd4 | Pinelis排列/耦合路线仍有o(1)猜想，不能记构造已完成；公开AI参与有原文声明。 | [MO510512](https://mathoverflow.net/questions/510512/bounded-positive-sequence-where-the-fractional-parts-of-x-i-x-ix-i1-are)，4月26日回答及ChatGPT说明。 |
| QX-P-001925 / d7547e44bf815a5e | a6已回1；原问是∃n>6。依赖n的递推不是一个固定值状态下的自治Collatz映射。 | [MSE4986018](https://math.stackexchange.com/questions/4986018/does-this-sequence-involving-multiplication-and-primorials-ever-return-to-1)，前六项及问题句。 |
| QX-P-001926 / 588b262d3272b719 | 有限倍数/平方等势的可见局部推论作者为Jade Vanadium，不是Karagila的完整证明。 | [MSE4952227](https://math.stackexchange.com/questions/4952227/does-this-equality-imply-choice)，2024-08-05/06评论。 |
| QX-P-001930 / 8da62eac3080579b | ∥改|；1e14计算只覆盖平方/两倍平方相关子类，1e18是Carmichael子类；一般通查声明仅1e9。 | [MSE4025226](https://math.stackexchange.com/questions/4025226/is-n2-mid-sigman-sigman-1-possible-for-n1)，题干与Hopf评论。 |
| QX-P-001931 / fd6feb8137c0480b | 2×10¹¹是k的界，不是N=k⁴+1的界；只是他人计算。 | [MSE3336724](https://math.stackexchange.com/questions/3336724/are-there-any-3-fermat-pseudoprimes-of-the-form-k41)，2023-01-20评论。 |
| QX-P-001932 / 362689db82c6930b | n=1为2，在Z[q]为不可约元，Q[q]则为单位；不能更换系数环制造反例。117上界未重跑。 | [MO324865](https://mathoverflow.net/questions/324865/irreducibility-of-q-factorial-plus-1)，题干及Sil引用。 |
| QX-P-001933 / 1b958bb7d369bc91 | AMM10523链接仍只是出处线索：本次PDF不可达，不能写已审小n分类证明或通用n已解。 | [原MSE](https://math.stackexchange.com/questions/742408/if-fraca-1a-2a-3-cdots-a-n-1a-1-1a-2-1a-3-1-cdotsa-n)；[PDF入口](https://www.mat.uniroma2.it/~tauraso/AMM/AMM10523.pdf)。 |

上述结论均通过各题实际题名/特征查询、原页面定位产生；无命中题没有在本清单重复列举。所有计算上界、旧卡数值测试及形式化成果均未在本轮重跑。

### 12. 指定查重配对：7组正文均不等价

不合并题卡。以下判断基于双方statement_text，不是标题相似。

| 本题（版本） | 另一题（版本） | 关系与正文差异 |
|---|---|---|
| 001914（cb98e0b84671fa25） | 001938（b00e3a83b75bf0a9） | 相关但不等价：方案étale群胚呈现，对比computability forcing对应topos构造。 |
| 001920（5f4a378013b688d5） | 000043（7516ea1af9a52ebd） | 相关但不等价：变量素数p<q的模q³问题，对比固定底47的普通Wieferich模平方问题。 |
| 001923（5392238e48ab4485） | 002334（55c56cdbe8040345） | 相关但不等价：4D单输入Euler控制ODE，对比4D Euler砖整数平方方程组。 |
| 001924（1223c96b0f659cc7） | 002236（d3d0d6e14014fca5） | 相关但不等价：固定p方格铺同一种形状的p个复制，对比容纳所有n-omino的最小区域。 |
| 001925（d7547e44bf815a5e） | 002130（8cc5f5fea0fbd7b2） | 相关但不等价：时间依赖primorial递推回1，对比固定参数ax+1迭代的逃逸。 |
| 001929（a3b10b4441a81b90） | 002362（b8fad3470f404d86） | 相关但不等价：Homeo空间同伦群，对比126维Kervaire invariant one流形存在性。 |
| 001930（8da62eac3080579b） | 002227（ada93a31bc64abe9） | 相关但不等价：约数和同余，对比反线性Poisson实结构；无数学等价线索。 |

表中题号均为QX-P-前缀。另有001915与001177仅为索引待定线索，未执行正文比对，不列为同题。

## 第76—100题：经核查的变化

### 1. QX-P-001958：q=5直接反驳字面题面，q>5版本须另存

- 当前版本：`c9c8f58e4405062d`。
- **旧卡 → 变化**：卡面与原帖都未排除5；原帖正文写每个奇素数q≥3。现在可把“缺例外”的问题明确定位。
- **可复核反例**：q=5且p<q为素数，只能p=2或3。若|y|≥2，则py²≥8>5；若y=0，则x²=5；若|y|=1，则x²=3或2。均不可能。
- **适用范围**：仅反驳含5的字面全称命题。将题面修订为q>5以后，不能沿用这个否定状态；本轮未取得修订命题的完整证明。
- 原始来源：[MO437635](https://mathoverflow.net/questions/437635/is-every-odd-prime-q-of-the-form-x2-py2-for-some-prime-pq)，正文开头两式；Will Jagy于2023-01-01评论提醒加入x²+y²才能包括5。工具引用：。
- **真实检索路径**：原题特征词“q / x^2+py^2 / prime”→完整slug原帖→公式与5的特征检索→GitHub/公开AI检索。反例为本轮手工核验，未运行外部程序。
- **后续**：修题时保留原版、例外和修订理由，不把y=1子问题的有限反例当作任意y的反例。

### 2. QX-P-001946 / QX-P-001957：完全同题，形式化核验确实前进一层，但尚未重跑

| 题号 | 当前版本 | 建议 |
|---|---|---|
| QX-P-001946 | `81c8efeacbeebc03` | 主卡候选 |
| QX-P-001957 | `d2f0b69baef1adb8` | 保留历史、并入同题证据 |

- **正文依据**：两题均问四个初值a₀=a₁=a₂=a₃=1及递推aₙ=(aₙ₋₁+1)(aₙ₋₂+1)(aₙ₋₃+1)/aₙ₋₄的全部自然数项是否为整数；都指向MO248604及其交叉发布MSE1905063。差别只有历史核验深度，未出现不同初值或不同量词。
- **旧卡 → 变化**：旧记录称未读Proof.lean和Mathlib依赖；本轮实际取得全文、工具链和依赖清单，核最终定理与递推逐项对应。1957不应继续保留“因MSE 403而未直读”的旧限制。
- 固定提交：`2e5b1c397ae89af800c4aee585a9d0eac982d962`（2026-07-13）。
- [Proof.lean固定版本](https://github.com/TheSil/mse_1905063/blob/2e5b1c397ae89af800c4aee585a9d0eac982d962/Proof.lean)：`def a`在开头约28–30行；约928行有限检查器`checkerB_ok`用`native_decide`；末尾`A276175_integrality (n : ℕ) : ∃ z : ℤ, A276175.a n = z`覆盖全n。全文约1724行，文本未见sorry/admit/axiom声明。
- [lake-manifest.json](https://github.com/TheSil/mse_1905063/blob/2e5b1c397ae89af800c4aee585a9d0eac982d962/lake-manifest.json)：Mathlib锁定`8a178386ffc0f5fef0b77738bb5449d50efeea95`；同提交工具链为Lean 4.29.0。
- **形式化层级**：已取得代码、已核定理对应、未重跑。不能写“本轮独立验证通过”；无sorry静态扫描也不等于编译及公理依赖核验。
- 原始作者声明：[MSE1905063](https://math.stackexchange.com/questions/1905063/is-a276175-integer-only)，Sil于2026-07-10回答、07-13编辑；工具引用。代码网页引用。
- **真实检索路径**：A276175/Lean/Sil/Mathlib→MO/MSE原文→作者仓库→GitHub API读取代码、manifest、toolchain、提交→全库编号/题名匹配发现两卡一致。
- **后续**：固定版本编译、打印最终定理公理依赖、复核有限native_decide检查器；不把Lean本身当作AI参与证据。

### 3. QX-P-001953：原题是双线性卷积；Z的完整否定声明及证明边界已定位

- 当前版本：`54221734e6c2e791`。
- **旧卡 → 变化**：人话版将原题改成固定μ的线性算子Tμ；真正的问题是m:ℓ¹(Z)×ℓ¹(Z)→ℓ¹(Z)。线性开映射定理不能代答。
- 原题：[MO504613](https://mathoverflow.net/questions/504613/is-convolution-in-ell-1-mathbb-z-an-open-map)，工具引用。
- 原始论文：F. Flores，*The convolution product is generally not an open map*，arXiv:2610.38722v1，2026-10-28。arXiv原站本轮访问被工具阻断，但成功读到[完整论文PDF镜像](https://borowiecki.dev/pdf/2610.38722)；引用、。
- **定位与范围**：PDF p.2 Theorem 2.1直接覆盖Z；pp.3–4 Example 2.3在A(T)取f=max(cos t,0)、g=max(−cos t,0)，fg=0，论文继而声称半径1/2开球的乘积不含0的邻域。本轮已核f、g的绝对收敛Fourier级数及fg=0；非开放性仍依赖Theorem2.1及未展开的Lemma2.2（ultrapower到ℓ¹(G^U)的代数同态）。全文及关键逻辑已读，但没有独立核验该环节与整条证明链，故Z情形记“完整证明/反例声明待核”。
- **不能扩大**：Theorem 1.2覆盖非阿贝尔群或含无限阶元的群；文中明示一般无限挠阿贝尔群仍未覆盖。
- **AI披露**：PDF p.5明确主结果来自与GPT-6 Astra迭代对话，作者随后简化、完善、写稿。此为作者一手披露，不是本轮复现。
- **真实检索路径**：原卷积开放性题→Flores题名/2610.38722/Theorem检索→原站失败→原论文PDF→定理、明确反例、AI statement逐项定位。
- **后续**：保留“完整否定声明、全文已读、明确零乘积对已核、预印本”强度；独立核Lemma2.2及Theorem2.1后才可提升为本轮验证。零乘积对本身不能证明非开放性，不能把该部分核验写成已反驳原题。

### 4. QX-P-001963：下半区间无条件发散，上半区间依赖新π证明；形式化模板与实际解答须分清

- 当前版本：`a32bb0afe9b5eb5f`。
- 原题及2026回答：[MO409550 / vengy回答](https://mathoverflow.net/questions/409550/convergence-of-the-series-sum-n-1-infty-frac2-sin-nn3n-na-for/515940)，、。
- **0<a≤1/2**：回答给不交区块上的下界证明，无条件发散；本轮核对了该论证的范围。
- **1/2<a<1**：回答将问题比较到Σm⁻ˢ/|sin m|，s=a+1/2>1，依赖OpenAI预印本Cor.5.2；该推论又依赖μ(π)=2新主张。应记录为完整证明声明待核，不能把上游声明的存在写成本轮独立验证。
- **原帖第二问**（此级数收敛反过来对π的无理指数有什么含义）须单独保留；从μ=2推收敛并未自动清除反向问题。
- 固定OpenAI/math提交：`3344da59991ed94f9ba711217b29c1d760badfa6`（2026-11-25）。
- [series.tex](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/sections/series.tex)：`series:generalized` / Cor.5.2为广义Flint Hills阈值，不能省掉主定理依赖。
- [实际Main.lean](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/NumberTheory/PiExponent/Main.lean)和[比较器配置](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/PiExponent.json)：配置选中`OAI.PiExponent.main`并指向实际解答模块。挑战目录PiExponent.lean含sorry是目标模板，不能据此宣称实际解答有sorry。
- **形式化层级**：已取得并核对定理目标，未build、未跑比较器、未审计全部导入公理闭包。实际模块中其它Flint Hills结论也不等于原级数已被形式化。
- **真实检索路径**：公式/编号检索未稳定召回→Boppana/Clement题名词找到原帖→2026回答→OpenAI原仓库TeX与配置/真实Lean模块→固定提交核验。
- **后续**：独立重跑选中π定理、公理依赖，并审查Cor.5.2到本级数的比较；保留反向子问。

### 5. QX-P-001961：形式化“已解”PR实际上仍sorry；新AI计算也有明确有限边界

- 当前版本：`f8acf0c7ab8ef54e`。
- **题面修正**：原题是n>1，变量a,b,c,d为非负整数。因为3ᶜ+5ᵈ≥2，卡片若只写“每个整数”会平白引入0、1反例。
- **失效声明**：[PR3396](https://github.com/google-deepmind/formal-conjectures/pull/3396)，2026-03-03声称Claude Sonnet生成证明并通过Lean；[原始diff API](https://api.github.com/repos/google-deepmind/formal-conjectures/pulls/3396/files)显示唯一修改是把research open标签改成formally solved，`by sorry`原封保留。PR closed、merged:false，head=`e1026247b6a5204e55ef2d80b19f7b600eaaa044`。正文所列公理甚至包含sorryAx。
- [当前正式文件](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/OEIS/303656.lean)本轮取得blob=`3d720f8f3486fbbbde1f99f08218c22452e5293a`，仍research open / sorry；测试少数n不等于证明全称。
- [Issue1477](https://github.com/google-deepmind/formal-conjectures/issues/1477)因题面合并PR1482而关闭，不是数学问题被解决。工具引用、。
- **另有有限计算**：[Samsen879/a303656固定README](https://github.com/Samsen879/a303656/blob/21ca85cc4eb2058ea165ceedabeb60425532a54d/README.md)，提交`21ca85cc4eb2058ea165ceedabeb60425532a54d`（2026-11-24），声称两套C++扫描覆盖240000000001≤n≤241600000000无反例。README与STATUS明确：AI模型研究/交叉审阅，无人类数学审阅、无形式化、无一般证明。本轮未运行扫描器；不能把作者“independent audits”误译成人类独立复核。
- **另一公开稿件**：[Basta 2025卷积公式文章](https://www.researchgate.net/publication/395445233_A_Convolutional_Characterization_of_the_Sun-OEIS_A303656_Conjecture)全文§6仍以Sun猜想为前提称T(n)>0；计数恒等式不证明每个n的正性。工具引用。
- **真实检索路径**：公式/A303656→OEIS/正式题面→公开AI检索命中aiXiv trace66→其PR3396线索→原GitHub API差异；另经仓库索引取得Samsen879 README/STATUS及HEAD。
- **后续**：数学状态保留部分进展；收录失败声明、有限扫描区间和AI-only审阅边界。无本轮独立编译/计算通过结论。

### 6. QX-P-001944：题源已恢复，四个Thompson F候选均非同题

- 当前版本：`fc70be4dde970f03`。
- **旧卡 → 变化**：撤销“原帖删除/不可恢复，因此剔除”的依据。本轮成功读取[完整slug原帖](https://mathoverflow.net/questions/130123/splay-trees-and-thompsons-group-f)，。
- **真问题**：能否用Thompson F中的词长等概念重述Sleator–Tarjan动态最优猜想。树旋转与F的关系是已知背景，不是要问树旋转是否生成F。
- 指定配对2051、2151、2386、2477分别是可均性后果、显式悖论分解、自动结构、非可均证明核验；都保留独立卡。只共享群F不构成等价。
- **真实检索路径**：splay / Thompson / MathOverflow→完整原帖→dynamic optimality / word特征检索→四张现版参考卡全文比对。
- **后续**：需要明确原帖“重述”的接受标准；不得以F非可均的其它声明代答。

### 7. QX-P-001938：旧“AI暴露=无”应纠正为公开UQ尝试且人工核验未过

- 当前版本：`b00e3a83b75bf0a9`。
- [UQ question236](https://uq.stanford.edu/question/236)列多模型答案；o3 Pro显示UQ Validated但Failed Human Verification。已读[其具体回答](https://uq.stanford.edu/answer/13532a0b-b6f4-4dbd-ba6b-74e8ad98bf52)。工具引用、。
- **范围**：只能记录该公开AI尝试与评估结果，不能提升为计算论强迫的完整拓扑斯对应；也不能由一次失败否定所有方案。
- **真实检索路径**：computability / forcing / topos→computed dense sets特征→UQ原题和回答。
- **后续**：有效拓扑斯内部强迫方案仍需专家核对与原题可计算稠密集泛性的对应。

### 8. 其它应修的题面：对象和量词决定是否为同题

| 题号／版本 | 旧卡 → 应改内容 | 原始定位与真实检索入口 |
|---|---|---|
| 001936／d431bdadb2844044 | 只谈Lemoine → 任意互素m1,m2的GGC，补gcd、奇偶和充分大n条件；JIS计算不等于全称证明 | [JIS PDF](https://cs.uwaterloo.ca/journals/JIS/VOL27/Juhasz/juhasz3.pdf) p.4 Conjecture1；Juhasz/Goldbach与m1,m2检索 |
| 001937／4a6723dc287606c9 | 范数/单一子空间 → 不同非零Uk的Σdim(Uk)，且f(U1⊗⋯⊗Un)=0 | [MO206211](https://mathoverflow.net/questions/206211/bunnity-of-multilinear-maps) 首定义；Bunnity与Bun(f)检索 |
| 001939／d99275286e299399 | 泛谈近等边规模 → ∀ε∃Cε∀n∀X，dim X≥Cεlog n，统一距离误差 | [MO188161](https://mathoverflow.net/questions/188161/large-almost-equilateral-sets-in-finite-dimensional-banach-spaces) 正文；nearly/almost equilateral、logarithmic检索 |
| 001940／1b694530a8fe5cb3 | 声称预期Mg(Q)全3g−3维稠密 → 问其闭包最大维数；大g一般型背景正是限制稠密性 | [MO187116](https://mathoverflow.net/questions/187116/what-is-the-expected-dimension-of-the-zariski-closure-of-the-rational-points-on) 开头及低gonality讨论；expected dimension/Zariski closure与trigonal检索 |
| 001942／5893e14e09bc35d6 | 泛泛不可约多项式系数 → 每步取使新增多项式Q上不可约的最小正系数的贪心递推 | [MO149560](https://mathoverflow.net/questions/149560/do-the-coefficients-of-these-irreducible-polynomials-always-become-periodic) 定义及分项提问；irreducible/periodicity与smallest positive coefficient检索 |
| 001952／ba66d2bd84a1aa83 | 固定a,b变n → 给定n>2，求1≤a,b<n且(a,b)≠(1,1) | [MO509825](https://mathoverflow.net/questions/509825/do-there-exist-a-b-such-that-both-anb-and-bna-are-primes) 正文及更新；an+b/bn+a与base-n permutable primes检索 |
| 001954／46db18853b132f1c | N→N → 任意结合含幺环R→S的brachymorphism | [Wehrung原论文](https://arxiv.org/html/2405.08364v3) §1.1、§11.1、§11.4；multiplication/successor与f(xy)/f(x+1)检索 |
| 001959／ca7f6c9af33334e0 | Λ²V上叉积且O(n)相容 → V×V→Λ²V，保留两个收缩为零与面积范数公理 | [MO354736](https://mathoverflow.net/questions/354736/are-0-1-4-7-8-the-only-dimensions-in-which-a-bivector-valued-cross-product) 开头公理；bivector-valued cross product检索 |
| 001960／276715551af06cfb | 任意拓扑空间/Steenrod → 光滑射影簇、char0系数的Weil上同调环实现；拓扑版另列 | [MO312272](https://mathoverflow.net/questions/312272/which-rings-are-cohomology-rings) 主体及末尾拓扑附问；题名与Weil cohomology检索 |
| 001964／f03188488f8e60aa | 无条件“连通纤维⇔结构层推前等式” → 询问性质(P)的名称和稳定性；补proper等适用条件 | [MSE3097234](https://math.stackexchange.com/questions/3097234/morphisms-with-connected-fibers) 性质(P)；[Stacks03H2](https://stacks.math.columbia.edu/tag/03H2)充分方向；connected fibres与O-connected检索 |
| 001965／e86bb2a6527c4bda | ε同态逼近真对称的固定稳定性问题 → 保留扰动二十面体与不均匀树两个实例的软性理论/文献问法 | [MSE3091126](https://math.stackexchange.com/questions/3091126/is-there-a-theory-of-almost-symmetry-generalizing-group-theory) 两个实例；approximate symmetries与Blum-Smith检索 |

001964的错误逆向还有直接反例：Spec k[t]→Spec k[t²,t³]的尖点正规化是有限态射，几何纤维底空间为单点，但全局函数推前不是原结构层。该例仅反驳卡面无条件等价；proper加(P)推出几何连通的标准充分方向仍成立。

001954应分别记录“若干环类已证”“半环变体反例”“一般含幺结合环待解”；不把半环反例统计为一般环原题反例。001955原帖Dold流形作用下降评论已由作者撤回，也不可当作整个含挠bordism环的生成证明。

### 9. 查重交付说明

本组完成11个指定pair_id，另新增1个同题pair_id。结构化结果中A276175在两行互引，因此共有13个duplicates条目、12个唯一pair_id。除1946/1957外均保留独立卡；1936/779只标Lemoine支线的特例/强化关系，其余指定对均“相关但不等价”。每一对包含双方版本及正文差异，不据标题或候选相似度判等价。

所有未来复核事项已留在逐题pending。全组代码核验最高层级为“已核定理对应、未重跑”，没有一题被记录为本轮独立形式化验证通过。

## 新增查重候选汇总

| 本轮新增候选 | 关系 | 复核边界 |
|---|---|---|
| QX-P-000098 ↔ QX-P-001869 | 待定 | Aharoni–Berger匹配题参数可能关联；未提供对方全文，不能直接等同本题一般图/超图多子问。 |
| QX-P-000295 ↔ QX-P-001908 | 待定 | 候选索引是5/6维精确kissing number，当前题是最优构型是否刚性及维数分类；仅索引不足确定子问包含关系。 |
| QX-P-000734 ↔ QX-P-001885 | 待定 | 索引题名涉及Dujella的Diophantine triple椭圆曲线整点反例，但本题为一般互异三元组的六解存在性；尚未取得候选正文，不能判断等价。 |
| QX-P-001177 ↔ QX-P-001915 | 待定 | 全库索引出现X+Y排序题；仅标题相似，本次未取得该候选全文，不能判同题。 |
| QX-P-001855 ↔ QX-P-001856 | 特例/强化 | 1855为一般H指定边色普适性，1856为H=C_n且精确n/2+1阈值；全文已核。 |
| QX-P-001868 ↔ QX-P-001994 | 待定 | 索引题名“圆环并覆盖平面Kakeya型”触发，参考包无其正文；不能凭标题同题。 |
| QX-P-001871 ↔ QX-P-001872 | 特例/强化 | 1872为1871一般Kst问题中的平衡s=t≥4；双方全文已核。 |
| QX-P-001874 ↔ QX-P-001875 | 特例/强化 | 1874宽泛“渐近改进”含已证little-o；1875固定正幂改善更强；二卡同源但不能抹去量词差别。 |
| QX-P-001946 ↔ QX-P-001957 | 同题 | 两张当前题卡标题/题面均为OEIS A276175全项整数性；metadata均指MO248604，MO明确交叉到MSE1905063。原始初值a0=a1=a2=a3=1、同一四阶递推、量词所有n完全相同；差异只是历史核验深度/置信等级。 |

所有候选的双方完整题号和 `card_rev` 均在JSONL。关系为“待定”的项目尚未取得对方现版正文，不能作为合并指令。指定46对的逐对理由同样在JSONL，不以词面相似代替等价证明。

## 下一轮复核顺序

1. 先落实会改变全称命题的题面修正与显式反例，保留修正版未解决部分。
2. 再审公开完整证明声明：取得原稿、版本与修订；核主定理、假设、证明依赖及与原题对应。已刊结果只在明确范围内更新。
3. 对形式化项目固定提交和工具链，审完整依赖后再决定是否独立重跑；不要把仓库存在、PR标题、平台标签或无sorry文本搜查等同于通过。
4. 对仍无可验证结果的条目保留具体检索边界；“本次未找到”不是开放性的证明。
