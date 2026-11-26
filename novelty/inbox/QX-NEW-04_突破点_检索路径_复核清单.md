# QX-NEW-04｜突破点、检索路径与复核清单

检查日期：2026-11-26（Asia/Shanghai）。范围严格限于原包任务表中的100题；38个指定查重配对按owner逐对复核。原id、card_rev、batch_id均保留。无线上库修改、无发帖、无合并。

## 先看这些变化

| 题号 | 本轮最重要的变化 |
|---|---|
| 1805 | Cohen66有独立复算的有限反例：Cσ(3959)=697>10+686，脚本及输出随包。 |
| 1806 | 全1权重、所有k≥2的anti-k-nacci窄命题已有Fokkink–Joshi定理；任意正权重强化声明另列。 |
| 1793 | 已刊群论结果支持a_n=Θ(n^(1/3))的增长阶；不声称给出每个n的精确值。 |
| 1772 | 一般光滑H的全局温和分布版本有直接反例；局部D′与多项式分支分开。 |
| 1765 | Mignotte1974可补显式旧界；μ(π)=2新声明不提供原题需要的有效阈值。 |
| 1826 | 三种凸性半径定义必须分流；标准同心版本有Xu反例，原帖单球sup字面版未判。 |
| 1835、1837 | 独立边模型新增FOCS录用证据；循环模型区分奇数阶原稿与11月全阶新声明。 |
| 1838、1846、1848 | 新/新版完整声明与固定提交代码可追踪；未独立运行Lean，不继承作者的验证标签。 |
| 1751、1762；1850、000055、000291 | 前两卡同题；后三卡有明确子问重叠，不能整卡互换。 |

数学状态在逐题文件中按子问给出。本文出现“原题已证/已反驳”时，只覆盖紧邻写明的版本；不把一个子问已解提升为整卡全部已解。论文已刊、预印本完整声明、代码可取得与本轮独立运行是不同证据层级。

## 发现与卡片修订建议

### QX-P-001751｜正二十面体每面可含有理点？（同题：1762）

**旧卡 → 本轮变化：** 旧标签 `claimed`。已核实新作者预印本及固定提交主定理与原题闭面版本对应；仍记完整反例声明待核，未独立重跑 Lean。与本分区另一二十面体卡同题。

**量词与范围：** 存在 I⊂R³ 为正二十面体，使每个闭三角面均与 Q³ 相交；允许平移、正缩放和正交变换。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://mathoverflow.net/questions/452847/can-a-regular-icosahedron-contain-a-rational-point-on-each-face) — 原题正文；已打开并阅读相关正文。存在 I⊂R³ 为正二十面体，使每个闭三角面均与 Q³ 相交；允许平移、正缩放和正交变换。
- [v1，2026-11-08；正文 Theorem 1.1](https://arxiv.org/abs/2611.11577) — 作者预印本；已打开并阅读相关正文。作者提出对任意正比例相似变换后的正二十面体，不可能20个闭三角面均有Q³点的完整反证。
- [Theorem 1.1；§1.1–1.2](https://arxiv.org/html/2611.11577v1) — 作者预印本；已打开并阅读相关正文。量词包含平移、任意正缩放、正交变换；闭面允许边和顶点；不是仅要求所在无限平面。
- [Icosahedron.no_rational_point_on_every_face](https://github.com/MikhailLevit1987/icosahedron-rational-faces/blob/f2539dbc4000b5168711fa2155bf1d13a2bf2a33/lean/Icosahedron/Main.lean) — 作者仓库；已打开并阅读相关正文。已读取固定提交的主定理，检查 t、s>0、R∈orthogonalGroup、Fin20 与 ¬∀j HasRatPoint 的结构对应；证明调用 reduction/separation。
- [face、IsRat、HasRatPoint 定义](https://github.com/MikhailLevit1987/icosahedron-rational-faces/blob/f2539dbc4000b5168711fa2155bf1d13a2bf2a33/lean/Icosahedron/Defs.lean) — 作者仓库；已打开并阅读相关正文。已取得定义源码；face 为显式顶点三角面的 convexHull，HasRatPoint 是变换后的三坐标有理点。未独立核验20面枚举和所有依赖。

**建议改动：** 补入 arXiv:2611.11577v1、固定提交、定理路径与形式化核验层级；保留 claimed 直至独立复核。；删除“有理点在任意平面上稠密”这一错误解说；Q³ 在 R³ 稠密不推出任意仿射平面上稠密。；记录1751/1762为同题，报告但不合并。

**实际路径：** `"No regular icosahedron" "rational"`；`"2611.11577"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 独立核查20面定义、转换等价性、48份证书及额外公理/占位扫描；未运行 Lean。；Zenodo记录24059304本轮入口不可达，不当作已取得完整档案。

### QX-P-001752｜全部导数根处于严格凸位置的多项式（P_n 拓扑）

**旧卡 → 本轮变化：** 旧标签 `open`。原题已恢复：要求每一阶导数各自的根分别处于严格凸位置；旧解说易误读为所有导数根并集。未取得覆盖各拓扑子问的完整新结果。

**量词与范围：** 首一 n 次多项式 P，对每个 k=0,…,n−2，P^(k) 的根各自严格凸；分别研究实系数连通分支、复系数连通性及相应基本群。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://mathoverflow.net/questions/26799/polynomials-with-roots-in-convex-position) — 原题正文；已打开并阅读相关正文。首一 n 次多项式 P，对每个 k=0,…,n−2，P^(k) 的根各自严格凸；分别研究实系数连通分支、复系数连通性及相应基本群。

**建议改动：** 把“全部导数根”明确为逐阶条件，包含 P 本身，不能把高阶导数根统称临界点。；分别登记实/复系数和连通分支/基本群子问。

**实际路径：** `"polynomials" "strictly convex position" Bacher derivatives topology`；`"Bacher" "P_n" polynomials connected components 26799`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 原帖有后续构造/评论线索，未核其覆盖范围与各拓扑断言；需针对每子问追踪 Bacher 的论文或完整论证。

### QX-P-001753｜24 次恰 20 实根多项式难寻

**旧卡 → 本轮变化：** 旧标签 `open`。旧卡遗漏固定 Galois 群和不可约性，导致问题变成容易构造的一般实根个数问题。原帖研究 IGP24 各 (G,r) 签名的经验难度差异。

**量词与范围：** G≤S24 传递，r为允许的复共轭固定点数；找有理域不可约24次多项式实现(G,r)，解释r=20等经验覆盖差异。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://mathoverflow.net/questions/512818/why-are-polynomials-of-degree-24-with-20-real-roots-hard-to-find) — 原题正文；已打开并阅读相关正文。G≤S24 传递，r为允许的复共轭固定点数；找有理域不可约24次多项式实现(G,r)，解释r=20等经验覆盖差异。
- [Mathematical Background / Task](https://competition.sair.foundation/competitions/igp24/overview) — 原始官方赛题；已读检索返回的官方正文摘要。官方赛题验证不可约性、24Tt 群标签及实根数；签名并非对每个群均允许所有偶数。
- [2026-07-17 对话记录](https://github.com/ash9241/team-dirac-igp24/blob/main/conversations/2026-07-17-team-dirac-update.md) — 作者公开代码/对话；仅检索返回正文摘要。命中 AI 队伍的搜索/构造记录；未核验系数、群计算或证明，不视为本题解决。

**建议改动：** 重写题面以包含不可约、有理/整系数、指定传递群G和竞赛统计口径。；删除把随机小系数多项式实根稀少直接当作原帖解释的段落。

**实际路径：** `"degree 24" "20 real roots" Sawin`；`"24T15308" "20" polynomial`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 有限入口初查未覆盖全部文献、修订及社区讨论；不以未命中推断开放。

### QX-P-001757｜Coxeter 元的中心化子

**旧卡 → 本轮变化：** 旧标签 `solved`。作者已刊论文支持有限秩不可约 Coxeter 群的结论 C_W(c)=<c>；应保留 solved 并补全范围，不能推广成所有可约系统同一个循环群。

**量词与范围：** 有限秩不可约 Coxeter 系统的 Coxeter 元 c，其中心化子是 <c>；无限不可约部分由 Hollenbach–Wegener 证明。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://mathoverflow.net/questions/323233/what-is-the-centralizer-of-a-coxeter-element) — 原题正文；已打开并阅读相关正文。有限秩不可约 Coxeter 系统的 Coxeter 元 c，其中心化子是 <c>；无限不可约部分由 Hollenbach–Wegener 证明。
- [Theorem1.1；Vol54 Issue2 pp682–693](https://doi.org/10.1112/blms.12596) — 已刊论文；已读官方检索正文；DOI直接打开不可达。已刊声明覆盖任意无限、不可约、有限秩 Coxeter 系统。
- [v2，2020-02-28](https://arxiv.org/abs/1912.01529) — 作者预印本；已打开并阅读相关正文。作者预印本最新版显示v2；摘要与已刊结论一致，版本说明为第4节小修。

**建议改动：** 写明作者 Ruwen Hollenbach、Patrick Wegener，BLMS54(2)(2022)682–693，DOI10.1112/blms.12596，Thm1.1。；补充有限秩、不可约；可约 W=∏W_i 时 C_W(c)=∏<c_i>，一般不等于<∏c_i>。

**实际路径：** `"Hollenbach" "centralizer of a Coxeter element"`；`"Coxeter element" "centralizer" github Lean AI proof`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 本轮核到已刊定理及预印本版本，不独立复证论文。；尚未找到完整对应 Lean 定理；不影响已有数学发表证据。

### QX-P-001758｜L²(G) 含于 C_c(G) 的标准正交基

**旧卡 → 本轮变化：** 旧标签 `open`。原题允许一般局部紧 Hausdorff 群。第二可数及紧交换情形已在原帖说明；“需要光滑”不是原题要求。未取得一般非可分情形的完整证明。

**量词与范围：** 对任意局部紧Hausdorff群G及Haar测度，L²(G)是否有全部元素属于C_c(G)的Hilbert标准正交基。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://mathoverflow.net/questions/406658/existence-of-orthonormal-basis-for-l2g-in-c-cg) — 原题正文；已打开并阅读相关正文。对任意局部紧Hausdorff群G及Haar测度，L²(G)是否有全部元素属于C_c(G)的Hilbert标准正交基。
- [题干及评论](https://math.stackexchange.com/questions/4277823/existence-of-orthonormal-basis-for-l2g-in-c-cg) — 原题正文；已打开并阅读相关正文。同作者交叉帖确认问题并说明在Blackadar书中见此断言；并非已取得该书完整证明。

**建议改动：** 删去一般群上“光滑”要求；C_c只要求连续紧支撑。；补记原帖已有第二可数、紧交换两类；不能笼统把非离散全部称为难例。

**实际路径：** `"orthonormal basis" "C_c(G)"`；`"locally compact group" "continuous compactly supported" "orthonormal basis"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 有限入口初查未覆盖全部文献、修订及社区讨论；不以未命中推断开放。

### QX-P-001760｜Hilbert 空间闭连通加法子群分类

**旧卡 → 本轮变化：** 旧标签 `open`。旧卡把已知非线性例子的存在误当主要未决点。原文给出L²(I,Z)并提出Hölder连接阈值/连通但非道路连通等更具体问题。

**量词与范围：** 可分无限维实Hilbert空间闭连通加法子群：指定Hölder/连续模的路径连接性、连通但非道路连通例子及应用。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://mathoverflow.net/questions/45322/closed-connected-additive-subgroups-of-the-hilbert-space) — 原题正文；已打开并阅读相关正文。可分无限维实Hilbert空间闭连通加法子群：指定Hölder/连续模的路径连接性、连通但非道路连通例子及应用。

**建议改动：** 补入原帖 L²(I,Z) 非线性闭道路连通例子及1/2-Hölder路径；不要把其存在当未解。；以原帖列出的子问代替无定义的“完整分类”；有限维闭子群也可为子空间与格的混合，旧二分叙述需修正。

**实际路径：** `"closed connected additive subgroups" "Hilbert"`；`Hilbert subgroup Holder paths exponent one half Pestov`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 有限入口初查未覆盖全部文献、修订及社区讨论；不以未命中推断开放。

### QX-P-001761｜gcd{ord_p(q)} 偏大现象

**旧卡 → 本轮变化：** 旧标签 `open`。旧人话版交换了p与q的角色，已由原文明确纠正。原帖提供统计和概率启发；并未取得几乎所有素数上的定理。

**量词与范围：** 固定素数p，F_p=gcd{ord_p(q):q为p−1的素因子}。解释F_p通常大、F_p=1罕见；特兴趣p≡1(mod4)、p−1为√p-smooth。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://mathoverflow.net/questions/185683/why-gcd-rm-ord-pq-colon-q-mid-p-1-likes-to-be-large) — 原题正文；已打开并阅读相关正文。固定素数p，F_p=gcd{ord_p(q):q为p−1的素因子}。解释F_p通常大、F_p=1罕见；特兴趣p≡1(mod4)、p−1为√p-smooth。

**建议改动：** 整段重写量词：对同一个模p、多个q取gcd；不是固定q对多个素数模p取gcd。；Lucia关于最大素因子和非q次幂的解释标为启发，不标“已证明p^(1−ε)几乎处处”。

**实际路径：** `"185683" "gcd"`；`"gcd" "multiplicative orders" "large"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 有限入口初查未覆盖全部文献、修订及社区讨论；不以未命中推断开放。

### QX-P-001763｜PSL(3,R) 酉对偶分类

**旧卡 → 本轮变化：** 旧标签 `open`。原题是酉对偶的拓扑、Hausdorff商及Casimir上方结构，不只是列出不可约表示。PSL(3,R)=SL(3,R)，旧卡“模±I”有误。

**量词与范围：** 描述 SL(3,R) 酉对偶作为拓扑空间、到R²的两个Casimir映射及分层/闭开结构。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://mathoverflow.net/questions/515373/what-is-the-unitary-dual-of-psl3-r) — 原题正文；已打开并阅读相关正文。描述 SL(3,R) 酉对偶作为拓扑空间、到R²的两个Casimir映射及分层/闭开结构。

**建议改动：** 纠正−I不在SL(3,R)，实3×3中心只有I。；改题为拓扑分类而非单纯表示清单；逐项保留原帖三问。

**实际路径：** `"PSL(3,R)" "unitary dual"`；`site:mathoverflow.net/questions/515373`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 原帖所引Speh、Lipsman等为后续追踪线索，未取得并核对足以覆盖全部拓扑子问的全文。

### QX-P-001764｜5-smooth 例外区间渐近密度（口径重写）

**旧卡 → 本轮变化：** 旧标签 `open`。已恢复“例外”的确切含义为左端点奇数。Størmer的固定差相邻数论题不能替代此加权区间密度问题。

**量词与范围：** N={2^a3^b5^c:a,b,c≥0}按N_k递增；I_k=[N_k,N_(k+1))∩N；E为N_k奇数的I_k之并。问自然密度d(E)=0。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://mathoverflow.net/questions/468790/consecutive-integers-of-the-form-2a-3b-5c) — 原题正文；已打开并阅读相关正文。N={2^a3^b5^c:a,b,c≥0}按N_k递增；I_k=[N_k,N_(k+1))∩N；E为N_k奇数的I_k之并。问自然密度d(E)=0。

**建议改动：** 直接登记上述E定义；删“与例外相邻对相关”占位。；区分区间数量与区间总长度；原帖的二素数等分布思路是特例线索。

**实际路径：** `"5-smooth" "density" Konieczny`；`"468790" smooth intervals`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 有限入口初查未覆盖全部文献、修订及社区讨论；不以未命中推断开放。

### QX-P-001765｜π 的有效无理性度量

**旧卡 → 本轮变化：** 旧标签 `open`。可补入Mignotte1974显式阈值定理，至少解决“更新于Mahler42且带明确阈值”的子问。Bai2026新上界及OpenAI μ(π)=2作者稿分别记录，均未提供本轮所需的现代指数显式q0。

**量词与范围：** 为 |π−p/q|>q^−μ 给出可明示的分母阈值，特别希望改进Mahler的显式42，而非只知道渐近无理性指数。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://mathoverflow.net/questions/210509/looking-for-an-effective-irrationality-measure-of-pi) — 原题正文；已打开并阅读相关正文。为 |π−p/q|>q^−μ 给出可明示的分母阈值，特别希望改进Mahler的显式42，而非只知道渐近无理性指数。
- [印刷p125，Théorème1；PDF第6页（0-based5）](https://www.numdam.org/article/MSMF_1974__37__121_0.pdf) — 已刊论文；已读PDF文本抽取；截图请求未返回可见图像。正文定理给指数21及20的显式分母范围；摘要20.6与正文需继续核读，保守保留21。
- [Theorem1.1；§5；v2于2026-09-11](https://arxiv.org/html/2609.11276v2) — 作者预印本；已打开并阅读相关正文。作者声称μ(π)<7.101862832357；需区分指数数值的精确区间与实际有理逼近阈值。
- [thm:main后紧接的effectivity说明](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/main.tex) — 作者仓库预印本；已打开并阅读相关正文。稿称∀ν>2有Q(ν)使q≥Q时|π−p/q|≥q^−ν，同时明确Q不effective。
- [theorem main](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/PiExponent.lean) — 作者仓库；已打开并阅读相关正文。取得的是比较挑战目标，含by sorry；不能误当实际证明文件或据此宣判整项形式化失败。

**建议改动：** 增列Mignotte1974 Thm1的显式旧界；把宽泛存在问与接近纪录指数的显式阈值问拆开。；Bai2026仅核到严格上界声明，不再把“所有量显式”直接当已经给出q0。；新μ=2稿标作者完整声明待核，其Q(ν)明确不可有效；不据此把本题判已解决。

**实际路径：** `"Effective irrationality measure" "pi" Bai`；`"pi" "7.101862832357" q0`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** Mignotte摘要/引言有20.6，而印刷页125 Thm1提取为21；本轮保守引用21，后续人工检查扫描。PDF截图工具仅返回ImageDisplayed文字，未取得可见像素，不能声称已视觉核验。；独立核Bai v2证明与可否提取有效常数；未核出实际q0。；OpenAI仓库只取得论文相关段、docs/017和ComparatorChallenges/PiExponent.lean；后者是含sorry的目标比较文件，不是证明入口。未据此断言整份形式化证明含占位，也未独立运行。

### QX-P-001766｜x³+y³+z³=c 可判定性

**旧卡 → 本轮变化：** 旧标签 `open`。原题是对任意整数c都停机的可解性算法。旧解说把mod9条件“未证充分”写成“不充分”，需纠正。

**量词与范围：** 是否有算法对每个c∈Z判定∃x,y,z∈Z：x³+y³+z³=c并停机。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://mathoverflow.net/questions/203957/decidability-of-x3y3z3-c) — 原题正文；已打开并阅读相关正文。是否有算法对每个c∈Z判定∃x,y,z∈Z：x³+y³+z³=c并停机。
- [v1，摘要；提交2025-12-12，期刊栏2020](https://arxiv.org/abs/2512.15763) — 作者预印本；仅摘要及版本信息。介绍已有种子解及参数化/替代方法，摘要不提供任意整数输入的完整停机判定定理。

**建议改动：** 将“同余条件不充分”改为“尚未证明充分”；非±4(mod9)全可解是原帖所述猜想，若成立就给mod9判定器。；区分给有解输入半判定的穷举、有限c计算纪录和任意输入全停机。

**实际路径：** `"sum of three cubes" decidability algorithm`；`"x^3+y^3+z^3" "decidable"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** arXiv:2512.15763仅核摘要中的种子方程/参数化方法，未核其声称能否决定所有c；不得将标题或构造法当完备停机算法。

### QX-P-001767｜Mertens 类命题亚线性检验

**旧卡 → 本轮变化：** 旧标签 `open`。原题强调对所有x≤X的严格检验和空间优化，未要求随机抽样。单点M(X)亚线性算法并不解决整段验证。

**量词与范围：** 全区间验证Mertens型不等式或优化|Σ_{n≤x}μ(n)/n|≤c/√x的常数；问优于近线性时间或远小于√X空间。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://mathoverflow.net/questions/237308/checking-mertens-and-the-like-in-less-than-linear-time-or-less-than-sqrtx-s?noredirect=1) — 原题正文；已打开并阅读相关正文。全区间验证Mertens型不等式或优化|Σ_{n≤x}μ(n)/n|≤c/√x的常数；问优于近线性时间或远小于√X空间。

**建议改动：** 删除“只抽样随机算法”这一非原题设定；保留确定性全范围保证与时间/空间二目标。；旧文献单点O(x^(2/3)loglogx)不能称最佳：原帖本就列O(x^(1/2+ε))方法；该事实仍不解决全范围。

**实际路径：** `"Mertens" "sublinear" Helfgott`；`"237308" "Mertens"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 需核后续区间认证算法及时间/空间模型；命中单点Mertens代码未解决全范围正确性。

### QX-P-001768｜(N^κ,≤) 共尾度（不可数 κ）

**旧卡 → 本轮变化：** 旧标签 `open`。已核逐点序及Hathaway定理的准确指数条件。把所有不可数κ笼统写为“依赖公理”过强；原帖两个剩余子问应分开。

**量词与范围：** f(κ)=cof(N^κ,逐点≤)；求ZFC可计算的额外κ，并求f(aleph1)<2^aleph1的一致性参考。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://mathoverflow.net/questions/221236/the-cofinality-of-mathbbn-kappa-le-for-uncountable-kappa) — 原题正文；已打开并阅读相关正文。f(κ)=cof(N^κ,逐点≤)；求ZFC可计算的额外κ，并求f(aleph1)<2^aleph1的一致性参考。
- [A Lower Bound for Generalized Dominating Numbers，v3(2014-05-04)，摘要](https://arxiv.org/abs/1401.7948) — 作者预印本；已打开摘要与版本；未逐行核全文。Hathaway给无限基数λ、κ且λ^κ=λ时，κ^λ处处支配共尾度为2^λ。

**建议改动：** 登记κ^aleph0=κ⇒f(κ)=2^κ的已知范围；不要无依据推广为剩余κ一律独立。；保留不可数参数与逐点支配；κ=ω与eventual dominating number等势不等于两种序相同。

**实际路径：** `"cofinality" "N^kappa"`；`"Hathaway" "cofinality" "omega"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 有限入口初查未覆盖全部文献、修订及社区讨论；不以未命中推断开放。

### QX-P-001769｜不可约整值多项式倒数和有理性

**旧卡 → 本轮变化：** 旧标签 `open`。原帖为不可约整系数f∈Z[x]、n从1起；旧解说把“整系数”改成更大整值有理系数类，且遗漏原帖平移互素变体。

**量词与范围：** 对f∈Z[x]、deg f≥2且不可约，问Σ_{n≥1}1/f(n)是否无理；另问放宽为所有正整数k使f(x)、f(x+k)互素。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://mathoverflow.net/questions/311485/rationality-of-sum-of-reciprocals-of-irreducible-polynomial) — 原题正文；已打开并阅读相关正文。对f∈Z[x]、deg f≥2且不可约，问Σ_{n≥1}1/f(n)是否无理；另问放宽为所有正整数k使f(x)、f(x+k)互素。

**建议改动：** 以原帖Z[x]替换整值多项式的误释；即使可用有理缩放讨论扩展，也须单独证明对应。；分别登记不可约版与平移互素版，明确无正整数极点及求和下限。

**实际路径：** `"irreducible polynomial" "reciprocals" irrational sum`；`"311485" "rational" polynomial`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 原帖特殊二次例子的超越性评论需追踪其实际引用；不能据个例或特殊函数表达式解决一般f。

### QX-P-001770｜除环上反射群分类

**旧卡 → 本轮变化：** 旧标签 `open`。原帖限定特征0除环上的有限不可约反射群。旧卡混入仿射/非离散群及实反射定义，影响题目范围。

**量词与范围：** 分类特征0除环上由伪反射生成的有限不可约线性群；需明确除环向量空间左右约定。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://mathoverflow.net/questions/349809/is-there-a-classification-of-reflection-groups-over-division-rings) — 原题正文；已打开并阅读相关正文。分类特征0除环上由伪反射生成的有限不可约线性群；需明确除环向量空间左右约定。

**建议改动：** 补有限、不可约、char0；将实反射“法向翻转”改成适用的伪反射定义。；删“仿射Weyl群非离散”错误例子；四元数/复数分类不是任意除环分类。

**实际路径：** `"reflection groups" "division rings" classification`；`"Shephard Todd" "division ring" Cohen Amitsur`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 原帖Amitsur、Cohen和Banieqbal文献是局部范围线索；未逐篇核足以覆盖任意除环的完备结论。

### QX-P-001771｜乘积密度似然比 liminf=0

**旧卡 → 本轮变化：** 旧标签 `partially_solved`。已追回完整原帖：目标是截断似然比的期望，也就是平均接受率；不是裸乘积几乎处处liminf。历史partial记录不能代替本轮的假设及证明核验。

**量词与范围：** f>0为C³概率密度，g=log f，g′ Lipschitz且g‴有界；X~f^⊗d，独立Z~N(0,I_d)，Y=X+ℓd^−αZ。问α<1/2时liminf E[1∧∏f(Y_i)/f(X_i)]=0及α>1/2时期望→1。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://math.stackexchange.com/questions/3140066/if-x-i%E2%88%BCf%CE%BB-z%E2%88%BC-mathcal-n0-i-d-and-y-x-ell-d-%CE%B1z-with-%CE%B11-2-then-l) — 原题正文；已打开并阅读相关正文。f>0为C³概率密度，g=log f，g′ Lipschitz且g‴有界；X~f^⊗d，独立Z~N(0,I_d)，Y=X+ℓd^−αZ。问α<1/2时liminf E[1∧∏f(Y_i)/f(X_i)]=0及α>1/2时期望→1。
- [Joris Bierkens回答及2019-03-15评论](https://stats.stackexchange.com/questions/396005/how-can-we-verify-the-intuition-that-in-the-rw-metropolis-hastings-algorithm-wit?noredirect=1) — 社区原回答；已打开并阅读相关正文。指出RGG1997 Lemma2.6需适配非临界α，提问者明确说原文未显式证明两半；此为研究路线。
- [RGG1997，Ann ApplProb7(1)110–120](https://sites.stat.columbia.edu/gelman/research/published/theory7.pdf) — 作者提供已刊稿；入口可达、全文文字不可读。作者PDF可达但web工具返回0可读行，正文及Lemma2.6尚未核。

**建议改动：** 写明E、截断1∧、Gaussian扰动尺度、两侧α条件与全部正则性；不把式(5)/(6)的探索路线当目标结论。；按α<1/2、α>1/2与经典临界α=1/2分项；partial来源须能对应本题假设。

**实际路径：** `"3140066" "density"`；`"liminf" "product" "density" "alpha" Metropolis`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** RGG1997作者PDF可打开但工具无可读文字，未核Lemma2.6；CrossValidated作者回答也明确需要适配，不是现成完整证明。；本轮未独立补出α=0端点或所有正则条件下的完整证明。

### QX-P-001772｜1/(H±i0) 分布良定义

**旧卡 → 本轮变化：** 旧标签 `solved`。旧solved把局部D′结论错当全局S′。一般光滑H版有直接反例；多项式H版须另核，不能由局部换元直接宣布全局温和。

**量词与范围：** 实光滑H:R^n→R，H=0处∇H≠0；问ε↓0时1/(H±iε)是否在S′中有边界值。原帖另允许收窄为多项式H。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://math.stackexchange.com/questions/2199058/is-frac1hx-pm-i0-a-distribution-if-nabla-h-neq-0-for-hx-0) — 原题正文；已打开并阅读相关正文。实光滑H:R^n→R，H=0处∇H≠0；问ε↓0时1/(H±iε)是否在S′中有边界值。原帖另允许收窄为多项式H。
- [本轮自写范围核查，详见analysis_note](local:QX-P-001772-counterexample) — 本轮独立初等推导；已完成书面推导。H=e^(−x²)；紧支撑测试下1/(H+iε)→e^(x²)。若有S′极限，其D′限制只能为该函数，与温和性矛盾。

**建议改动：** 去除将H当一般自伴算子的漂移；按D′局部分布、一般光滑S′、多项式S′分项。；撤销无条件整体solved；一般C∞版本可记反例，不能据此否定多项式分支。

**实际路径：** `"2199058" distribution`；`"1/(H" "distribution" Plemelj noncritical`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 多项式分支需全局增长/Łojasiewicz型估计或准确引用；本轮未取得足够证据，不作判断。；原帖同意可先证零集紧的版本，但零集紧本身也不能控制无穷远倒数增长。

**本轮推导：** 本轮初等反例：H(x)=exp(−x²)严格正，零集为空故零点非临界条件成立。对每个紧支撑φ，分母在supp φ上有正下界，支配收敛给1/(H+iε)→exp(x²)于D′。若存在S′极限，它限制到D′必为同一函数。取非负φ∈C_c∞(0,1)非零及φ_R(x)=φ(x−R)，其任意固定阶Schwartz半范数随R至多多项式增长，而∫exp(x²)φ_R(x)dx≥exp(R²)∫φ，违背温和分布的有限半范数连续估计。若另要求零集非空，可取H(x)=x exp(−x²)：零集{0}紧且H′(0)=1；在远离0的正半轴极限为exp(x²)/x，同一平移测试给增长至少exp(R²)/(R+1)，仍非温和。故一般光滑S′主张为假。这些例子非多项式，不决定多项式分支。

### QX-P-001774｜代数数数字交换保持代数性

**旧卡 → 本轮变化：** 旧标签 `open`。原题交换每对相邻小数位，不是任意重排或全局互换数字字符。原帖只给有理性保持观察和猜测，未取得√2交换后数的代数/超越性证明。

**量词与范围：** 十进制小数位a_(2i+1)与a_(2i+2)对每i≥0交换；问代数无理a（尤其√2）是否仍代数。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://math.stackexchange.com/questions/1656736/swapping-the-digits-of-an-algebraic-number-e-g-sqrt-2) — 原题正文；已打开并阅读相关正文。十进制小数位a_(2i+1)与a_(2i+2)对每i≥0交换；问代数无理a（尤其√2）是否仍代数。

**建议改动：** 用相邻成对交换定义替换“随意重排”。；有限位修改只改变一个有理数，保持代数性；不能把有限位改动也说成普遍超越性未明。；原帖评论的0↔1字符替换是另一问，禁止混记。

**实际路径：** `"algebraic" "swapping digits" decimal`；`"1656736" algebraic`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 有限入口初查未覆盖全部文献、修订及社区讨论；不以未命中推断开放。

### QX-P-001775｜无穷乘积空间同调群

**旧卡 → 本轮变化：** 旧标签 `open`。取得Kawamura2002已刊原稿，可补明确特例及同伦工具；原帖允许加假设寻计算工具，不是已经精确定义的全称开放猜想。

**量词与范围：** 给无限指标族Xi，在适当附加假设下计算乘积拓扑∏Xi的奇异同调，寻类似有限Künneth的工具。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://math.stackexchange.com/questions/1411462/the-homology-groups-of-an-infinite-product-of-spaces) — 原题正文；已打开并阅读相关正文。给无限指标族Xi，在适当附加假设下计算乘积拓扑∏Xi的奇异同调，寻类似有限Künneth的工具。
- [K. Kawamura, Fundamenta Math175(2002)285–289；Thm1.1、Cor1.2、Thm1.4](https://www.impan.pl/shop/en/publication/transaction/download/product/88471) — 已刊原稿；已打开并阅读相关正文。在(n−1)-连通continua等假设下给悬挂/乘积比较；可数n球乘积的H_(n+1)为0（n≥2）。

**建议改动：** 补Kawamura2002 Thm1.1/Cor1.2及Thm1.4；把一般问题与具体可计算族分开。；不要用无限乘积“非局部紧”作通用理由：无限紧空间乘积仍紧；实际问题是所用同调与局部连接性质。

**实际路径：** `"homology" "infinite products" Kunneth`；`"1411462" "homology"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 有限入口初查未覆盖全部文献、修订及社区讨论；不以未命中推断开放。

### QX-P-001777｜重建猜想对 partial 2-树

**旧卡 → 本轮变化：** 旧标签 `open`。原题是顶点重建对partial2树的特例；跨站讨论中某“bidegreed”引用其实是边重建，不能作为顶点版进展。与000265为特例关系而非重复。

**量词与范围：** 有限至少3顶点的partial2树（树宽≤2）是否由顶点删除子图多重集唯一确定。

**直接证据与定位：**

- [原帖题干、可见评论及回答区](https://math.stackexchange.com/questions/23945/reconstruction-conjecture-and-partial-2-trees) — 原题正文；已打开并阅读相关正文。有限至少3顶点的partial2树（树宽≤2）是否由顶点删除子图多重集唯一确定。
- [交叉帖2012回答](https://cstheory.stackexchange.com/questions/5155/reconstruction-conjecture-and-partial-2-trees) — 社区原回答；已读检索返回相关正文。指明原提问所引bidegreed结果为edge-reconstructible而非vertex-reconstructible。

**建议改动：** 明确顶点deck；新增与000265的特例/强化方向关系，不合并。；“反复折掉二度顶点”需说明删除/补边约定，避免把普通2退化性当树宽≤2等价。

**实际路径：** `"partial 2-trees" "reconstruction"`；`"series-parallel" "vertex reconstruction" graph`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 需追踪针对partial2树的最新顶点重构定理；本轮未找到直接完整证明。；CST所纠正引用是边重建，不适用顶点deck。

### QX-P-001778｜大 Witt 向量环素理想谱

**旧卡 → 本轮变化：** 旧标签 `open`。原题为整数大 Witt/necklace 环 W(Z) 的素谱。检索缓存出现声称完整分类的新答复，但所引 Vaseghi 论文及答复全文均未取得，不能据缓存提升为已解决。

**按子问判断：** W(Z) 的全部素理想及谱结构：完整证明/反例声明待核；搜索缓存答复提出由 Spec D 限制及超滤子描述 Spec W，引用 Vaseghi Thm 3.1/Cor 3.2；本轮只得到缓存文字，未核定该文及全部假设。

**直接证据与定位：**

- [题面与原始观察](https://math.stackexchange.com/questions/5147706/prime-ideals-of-big-witt-vectors-over-bbb-z/5152931) — 社区原题；原题正文可读；打开页未显示检索缓存中的新增答案。
- [搜索缓存答复及所引 Arithmetic profiles and the prime spectrum of the integer necklace ring, Thm 3.1 / Cor 3.2](https://math.stackexchange.com/a/5152931) — 社区完整声明，未核；仅搜索缓存；直接打开答复失败；论文全文未取得。

**建议改动：** 把题面底环明确为 Z，不推广到任意 A。；新增完整分类声明待核标签及论文获取任务；不改为已证。

**实际路径：** `site:math.stackexchange.com/questions/5147706 Witt spectrum`；`"Arithmetic profiles" "Vaseghi"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 取得 Vaseghi 原稿的稳定版本并核完整分类、超滤子及无限 Krull 维数的范围。；解决搜索缓存新答案与打开页面旧缓存不一致，核答复作者、时间与引用。

### QX-P-001779｜闭图+连通图⇒连续？

**旧卡 → 本轮变化：** 旧标签 `solved`。否定结论有可读的已刊原稿支持：Jelínek 2003 构造 R²→R 的不连续函数，其函数图闭且连通。旧卡把“函数图连通”改写为“连通集的像连通”，须修正。

**按子问判断：** 闭且连通函数图推出连续（n≥2）：原题已反驳；Jelínek 的 R² 反例否定；更高维延拓为本轮直接推论。；n=1 对照情形：原题已证；同文 Proposition 3 给一维正面结论，不能混入 n≥2。

**直接证据与定位：**

- [题面、Jelínek 答复链接](https://math.stackexchange.com/questions/4777434/is-a-function-mathbbrn-to-mathbbr-which-has-a-closed-and-connected-gra?r=31) — 社区原题；原题正文已读。
- [Acta Universitatis Carolinae 44(2) (2003), 73–77；R² 构造、Proposition 3](https://dml.cz/bitstream/handle/10338.dmlcz/702089/ActaCarolinae_044-2003-2_8.pdf) — 已刊论文；原稿 PDF 已读。

**建议改动：** 保留否定已知，但把图连通与连通性保持分开；补齐维数限定和已刊原稿。；解除与 QX-P-002064 的关键词误配。

**实际路径：** `site:math.stackexchange.com/questions/4777434 closed connected graph`；`Jelinek 2003 discontinuous function closed connected graph 73 77`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 若要保留现有人话版的连通性保持问题，必须另建精确题面，不得复用本题反例结论。

### QX-P-001780｜微分同胚局部本原分解

**旧卡 → 本轮变化：** 旧标签 `solved`。局部坐标分解是 Munkres 的已知结论；primitive 在此指保持某个坐标（更强版本每步仅改一个坐标），旧卡将其解释成不可再分的本原因子有误。原帖还请求检查其自写证明，不能与定理已知合并。

**按子问判断：** 给定微分同胚的局部 primitive 分解存在：原题已证；原帖指向 Munkres Analysis on Manifolds Thm 18.3 及 §18 Exercise *2；检索文本显示保持所有但一个坐标的更强形式。；原帖所写证明逐行正确性：未作判断；本轮只做初查，未逐行审核其长证明。

**直接证据与定位：**

- [题面定义、Munkres 引文与证明核查请求](https://math.stackexchange.com/questions/3790625/any-diffeomorphism-can-be-locally-factorised-with-several-primitive-diffeomorphi?r=31) — 社区原题；原题正文已读。
- [Thm 18.3；§18 Exercise *2, p160](https://djvu.online/file/pLmS0XTKIcbwo) — 教材原文的转录检索结果；仅检索到书籍转录摘录；未完整打开该书版本。

**建议改动：** 把 primitive 的定义改为原帖的坐标条件；保留局部存在定理已知，另标自写证明未逐行验。

**实际路径：** `site:math.stackexchange.com/questions/3790625 primitive diffeomorphism Munkres`；`Munkres Analysis Manifolds primitive diffeomorphism Theorem 18.3`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 如要引用精确教材页码用于出版式回填，取得该版书页核对 Thm 18.3 与习题编号。

### QX-P-001781｜无条件收敛级数 Cauchy 乘积封闭

**旧卡 → 本轮变化：** 旧标签 `open`。已核原题确为 Banach 代数中两个无条件收敛级数的 Cauchy 乘积是否无条件收敛。原页评论中的“可能为假”未给完整反例；本轮未找到可验证的原题解答。

**按子问判断：** 一般 Banach 代数中的 Cauchy 乘积封闭性：暂未找到可验证结果；已查原题、名称、乘积公式特征与代码/AI；原页只见非完整反例意见。；交换代数或幂级数子情形：暂未找到可验证结果；本轮未获得与这些附加条件准确对应的完整论证。

**直接证据与定位：**

- [题面、附加子问、评论区](https://math.stackexchange.com/questions/3452696/are-the-unconditionally-convergent-series-with-terms-in-a-banach-algebra-close?noredirect=1) — 社区原题；原题正文已读。

**建议改动：** 隔离尚未核实对应关系的历史 MO 317905 引用，不作为本轮原题证据；将“无条件”与“绝对”收敛严格区分。

**实际路径：** `site:math.stackexchange.com/questions/3452696 Cauchy unconditionally`；`"unconditionally convergent" "Cauchy" "Banach algebra"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 若后续获得反例，应同时核 Banach 代数乘法连续性及两个级数确实无条件收敛，另核是否交换。

### QX-P-001782｜Q(a,b) 次数值域

**旧卡 → 本轮变化：** 旧标签 `open`。一般复合域次数取值问题未获全解；Virbalas 2023 已刊论文对两个同素数次数给出详细分类，其中一族仍附有具体群可在 Q 上实现为 Galois 群的条件，不能删去条件写成无条件全分类。

**按子问判断：** 任意 n,m 的全部复合次数：暂未找到可验证结果；本轮未找到覆盖任意 n,m 的完整分类。；(p,p,ps) 素数次数情形：部分进展；Virbalas Thm 1.1 给 s=p、s|(p−1)、(11,6) 及射影线性族等分类；最后一族保留 transitive group 位于 PSL(n,q) 与 PΓL(n,q) 间并可在 Q 上实现的条件。；2025 prime-power 后续：未作判断；只取得作者发表目录/DOI 线索，未取得定理正文。

**直接证据与定位：**

- [固定两个代数次数及 (5,5,15) 讨论](https://mathoverflow.net/questions/284885/the-possible-degrees-of-mathbbqa-b-in-terms-of-the-degrees-of-a-and-b) — 社区原题；原题检索文本已读。
- [NYJM 29 (2023), 171–192；Thm 1.1, pp172–173](https://nyjm.albany.edu/j/2023/29-6v.pdf) — 已刊论文；原稿 PDF 已读。
- [DOI 10.1007/s10986-025-09683-1](https://elaba.mb.vu.lt/mif/?aut=Paulius+Virbalas) — 作者机构目录；仅题名/发表元数据。

**建议改动：** 补充 2023 已刊部分进展及精确适用范围；不能泛化到任意两个次数。；解除与 QX-P-002195 的 degree 一词误配。

**实际路径：** `site:math.stackexchange.com/questions/2359474 degrees`；`"2359474" "degrees"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 取得 2025 论文全文核 prime-power 范围及是否无条件。；复核 Thm 1.1 射影线性族的 Galois 可实现性条件后再录入结构化分类。

### QX-P-001783｜₂F₁(a,b;1/2;γ)=δ 代数对无穷

**旧卡 → 本轮变化：** 旧标签 `open`。原帖实际请求证明四组固定参数的 η 商/椭圆积分恒等式；旧卡的一般代数参数叙述扩大了问题。2026 新预印本仅取得题录，未取得正文，不能判定覆盖这四式。

**按子问判断：** 原帖四组参数恒等式的严格证明：暂未找到可验证结果；已定位并核四式与 Zucker–Joyce 系列关系；本轮未取得逐式完整证明。；2026 Exceptional Sets 论文是否解决四式：未作判断；arXiv 2607.16331 全文不可达，题录/摘要不足以对齐四式。

**直接证据与定位：**

- [公式 (1)–(4)、四组参数、N 的范围](https://math.stackexchange.com/questions/2066932/infinitely-more-algebraic-numbers-gamma-and-delta-for-2f-1-lefta-b-t) — 社区原题；原题正文已读。
- [出版社摘要；涉及的另一参数组合不能覆盖所有四式](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/special-values-of-the-hypergeometric-series-iii/94C323267B1507A1DFA3DB99D7E4A072) — 已刊论文摘要；仅出版社摘要。
- [2026 题录；PDF https://arxiv.org/pdf/2607.16331](https://arxiv.org/abs/2607.16331) — 预印本元数据待核；仅检索题录/摘要；abs 和 PDF 直接访问均失败。

**建议改动：** 以四组参数与四个具体恒等式替换泛化的人话题面。；把 2026 题录作为待取全文线索，不作解决标签。

**实际路径：** `site:math.stackexchange.com/questions/2066932 hypergeometric`；`"2066932" hypergeometric`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 取得 2607.16331 正文和最新版本，并逐一映射原帖 (1)–(4)。；Zucker–Joyce 的 II/III 及勘误需逐参数核实；本轮命中的早期系列勘误不自动作用于这四式。

### QX-P-001784｜秩>1 椭圆曲线非挠点显式构造

**旧卡 → 本轮变化：** 旧标签 `open`。原问关注高秩椭圆曲线非挠有理点的解析/几何显式构造，并可假设 BSD。原页引述的某构造在解析秩≥2时只产挠点，不是所有构造均失败；2019 指向的 AMS 进展全文本轮不可达。

**按子问判断：** 原题所需的高秩构造方案：暂未找到可验证结果；原页、两路学术和代码/AI 检索未给出与整问完全对应的可核全文。；§5.2 相关构造的高解析秩障碍：部分进展；Stein 在原页明确限定 §5.2 的另一构造与 triple-product L 函数；不能视为全题不可能定理。

**直接证据与定位：**

- [题面；Stein 2011-02-14 评论；Helfgott 2019-05-27 后续链接](https://mathoverflow.net/questions/55423/constructing-non-torsion-rational-points-over-mathbbq-on-elliptic-curves/509727) — 社区原题/研究者评论；原题正文已读。
- [原帖 2019 评论给的文章链接](https://www.ams.org/journals/mcom/2016-85-301/S0025-5718-2015-03057-9/S0025-5718-2015-03057-9.pdf) — 期刊论文入口不可达；403；精确 DOI 检索未获得可读定理正文。

**建议改动：** 把“所有高秩构造无效”改为原评论明确的 §5.2 特定构造障碍；保留原题可假设 BSD 的范围。

**实际路径：** `site:mathoverflow.net/questions/55423 rational points rank greater one`；`"explicit construction" "non-torsion" "rank" "55423"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 取到原帖链接的 AMS 正文并核题名、定理及与原问的对应。；若见一般 BSD 或穷举点代码，另核是否满足原题的解析/几何构造要求。

### QX-P-001785｜G₂ 为某射影空间等距群？

**旧卡 → 本轮变化：** 旧标签 `solved`。旧卡的 solved 依据仅讨论经典秩一射影空间，未覆盖原帖明确允许的 Rosenfeld 广义射影平面。原问还要求等距李代数而不必是整个群。建议撤回无条件已解决标签并澄清“射影空间”类别。

**按子问判断：** 经典标准度量射影空间的 G2 实现：部分进展；标准对称空间分类只约束这个较窄版本。；原帖允许广义 Rosenfeld 平面的整问：暂未找到可验证结果；未定位覆盖其完整类别的肯定构造或排除定理；2020 跟进明确自称非完整答案。

**直接证据与定位：**

- [原题的 Lie algebra 与 Rosenfeld 范围](https://math.stackexchange.com/questions/1402870/does-the-exceptional-lie-algebra-mathfrakg-2-arise-from-the-isometry-group?r=31) — 社区原题；原题正文已读。
- [答案开头 not a full answer；rolling balls 的分布几何](https://math.stackexchange.com/questions/3921311/g-2-as-the-group-of-isometries-of-a-projective-space/3921476) — 社区部分答复；正文已读；不构成全题答案。
- [射影平面和例外群背景；相关 ball.pdf 为滚动球分布问题](https://math.ucr.edu/home/baez/octonions/node13.html) — 作者综述；作者网页检索文本；未取得对原问全部广义类别的定理。

**建议改动：** 建议把无条件 solved 改为待核/范围需澄清；保留窄版本的已知分类背景。；不要把 G2/SO4 或 split G2 滚动球分布直接命名为所需度量射影空间。

**实际路径：** `site:math.stackexchange.com/questions/1402870 G2 projective`；`G2 isometry group projective space compact symmetric G2 SO4`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 先明确允许哪些广义射影平面和哪种度量，再寻找完整的实现或排除定理。

### QX-P-001786｜3 生成元 Higman 群平凡？

**旧卡 → 本轮变化：** 旧标签 `solved`。三生成元三循环关系的 Higman 群平凡是已知事实；原帖真正要求的是有几何动机的证明，并明确区分代数证明。旧卡的“四个关系”和将 H4 称为简单群均应纠正或重核。

**按子问判断：** 三生成元 Higman 群平凡：原题已证；原帖和 Higman/Hirsch 文献线索均把平凡性作为已知事实；本轮并未给新的群论证明。；满足原帖意图的几何动机证明：暂未找到可验证结果；检索尚未取得原帖所要求的完整几何解释。

**直接证据与定位：**

- [三循环关系及请求 geometric proof 的明确限制](https://math.stackexchange.com/questions/479835/higman-group-with-3-generators-is-trivial) — 社区原题；原题正文已读。
- [§4.2, p83 的 Higman 群讨论](https://d-nb.info/102971116X/34) — 学术原稿检索摘录；仅检索到文献摘录；未作逐行证明核验。

**建议改动：** 修正三生成元版本的关系数；把已知平凡定理与几何证明请求分成两个状态。；不要把四生成元 Higman 群无有限商误写成群本身简单。

**实际路径：** `site:math.stackexchange.com/questions/479835 Higman geometric proof`；`Higman group three generators trivial 1951 geometric proof`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 若回填 H4 的性质，需单独给出准确原始引文；H4 性质不是 H3 几何证明。

### QX-P-001787｜π 的"Galois 群"=Z？

**旧卡 → 本轮变化：** 旧标签 `partially_solved`。“π 的 Galois 群是 Z”混合了不同对象。André 的周期/动机框架给出 Q×；普通超越函数域 Aut_Q Q(π) 是 PGL₂(Q)，指数覆盖的 Z 是另一种单值群。需修正题面含义，不能视为一个通常代数数的最小多项式问题。

**按子问判断：** André 框架下 π 的周期 Galois 群解释：部分进展；作者稿 §2.1 提出 Q×，§5.3 用 §3.6(2) 回收该结论；一般周期定义中的猜想假设不能在所有周期上省略。；把 Z 认作普通域论意义的 Gal(π)：题面有误；没有唯一未加定义的 Gal(π)；Aut_Q Q(π)=PGL₂(Q) 与 exp 覆盖的单值群 Z 是不同对象。

**直接证据与定位：**

- [原问、Myshkin 关于 Q× 的答复；MSE 94994 为相关来源](https://mathoverflow.net/questions/84569/the-galois-group-of-pi-is-mathbbz) — 社区原题/解释；原讨论正文已读。
- [§2.1 (p2), §3.6(2), §5.1–5.3 (p10)](https://arxiv.org/pdf/0805.2569) — 作者预印本/学术综述；作者原稿 PDF 已读。

**建议改动：** 删除最小整数多项式式的人话解释；列明三种不同定义并将 André 的 Q× 引文归回其框架。；解除与 QX-P-002056 具体多项式 Galois 群问题的误配。

**实际路径：** `site:math.stackexchange.com/questions/94994 galois pi`；`"Galois group of pi" Andre`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 若保留 conjectural 一词，应指明是一般周期体系的假设，不能把 π 特例与所有周期混为一谈。

### QX-P-001788｜移动沙发"涂漆"变体

**旧卡 → 本轮变化：** 旧标签 `open`。原题是在沙发通过直角走廊的同时要求扫遍走廊地面，再最大化沙发自身面积。旧卡把目标写成涂漆面积/墙面覆盖有误；经典 moving sofa 的结果不自动适用于该额外覆盖条件。

**按子问判断：** 有全地面覆盖约束的最大沙发面积：暂未找到可验证结果；本轮未取得这个变体的最优性证明；经典 moving sofa 结果和其他走廊问题均不对齐。

**直接证据与定位：**

- [目标与全地板涂漆约束；候选 limacon r=√2−a sinθ](https://math.stackexchange.com/questions/5145614/a-variant-of-the-moving-sofa-problem-involving-paint) — 社区原题；原题正文已读。

**建议改动：** 修正目标函数与覆盖对象；把 inverse Hammersley/limacon 标为候选而非最优解。

**实际路径：** `site:math.stackexchange.com/questions/5145614 sofa`；`"moving sofa" "wet paint"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 任何后续面积上界都须检查是否同时使用并满足全地面覆盖约束。

### QX-P-001789｜定长 3D 闭曲线凸包最大体积

**旧卡 → 本轮变化：** 旧标签 `open`。未取得任意定长空间闭曲线的凸包体积全局最大值。已定位 Melzak 的受限对称类工作及原帖 2026 数值积分上限纠正评论；0.00379648/0.0037965369 仍是候选数值，不能写成已证最优。

**按子问判断：** 任意长度 L 空间闭曲线的最大凸包体积：暂未找到可验证结果；本轮只取得受限类与候选资料，没有全局最优证明。；原帖候选数值与 Melzak 公式：部分进展；gerw 2026-01-28 评论提出积分上限 b t1 应为 t1，给出修正数值 0.0037965369；本轮未独立重算。

**直接证据与定位：**

- [候选 V/L³≈0.00379648；gerw 2026-01-28 评论](https://math.stackexchange.com/questions/5120376/what-3d-closed-loop-with-given-length-has-convex-hull-with-largest-possible-volu?r=31) — 社区问题/计算纠错声明；原题与评论正文已读；数值未独立复算。
- [受限类结果与一般问题的区别](https://mathoverflow.net/questions/83026/largest-possible-volume-of-the-convex-hull-of-a-curve-of-unit-length/179161) — 社区原讨论；原题检索文本。
- [Proc. AMS 11 (1960), 265–274；p266 Class A；DOI 10.1090/S0002-9939-1960-0116263-0](https://scispace.com/pdf/the-isoperimetric-problem-of-the-convex-hull-of-a-closed-2os87kk5qk.pdf) — 已刊原稿镜像；作者论文扫描检索摘录；未整篇逐行核证。

**建议改动：** 删除“两圆弧拼接已最优”的未证断言；写明受限类假设和数值候选身份。；新增积分上限纠错待核项，不把论坛数值自动提升为定理。

**实际路径：** `site:math.stackexchange.com/questions/5120376 curve volume`；`"convex hull" "closed curve" "Melzak" maximum volume`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 独立核算被指积分上限及该数值是否仅在选定 ansatz 下最优。；Nudelman 等凸曲线类别结果不能自动覆盖所有闭曲线。

### QX-P-001790｜无穷维切向量三定义等价？

**旧卡 → 本轮变化：** 旧标签 `partially_solved`。已取得 Kriegl–Michor 作者版全书并纠正旧卡定位：切向量比较在 §28，非该版 §19.6。书中有非运动学的操作性切向量反例，曲线速度与运动学定义则对应；但 MSE 5066411 原页未取到，原帖使用的微积分体系仍待核。

**按子问判断：** convenient 框架内曲线速度与运动学切向量：原题已证；作者书 §28.13 明确给出曲线速度描述。此项是相应定义比较的已知结论，原帖体系仍未核。；操作性切向量总等于运动学切向量：原题已反驳；§28.3–28.4 有无限维 Hilbert 空间上的高阶操作性导子，说明一般等价断言失败；不是所有空间都严格不等。；MSE 原题的精确假设和全部子问：未作判断；原页多次检索/打开不可达，不能宣布原帖全部解决。

**直接证据与定位：**

- [原始编号及 ?answertab=votes 重试](https://math.stackexchange.com/questions/5066411) — 原题未取得；入口不可达；精确编号查询不足以恢复完整题面。
- [AMS Surveys 53；§28.3–28.4, p279；§28.13, p285；该版 §19.6 为 realcompactness](https://www.mat.univie.ac.at/~michor/apbookh-ams.pdf) — 已刊专著作者版本；作者 PDF 已取得并定位关键节。

**建议改动：** 把该版 §19.6 错引改为 §28.3–28.4、§28.13，注明版次。；将一般不等价、特定空间充分条件及曲线/坐标一致三件事分开。；保留原帖未取得的限制，不以教材结果替代未核假设。

**实际路径：** `site:math.stackexchange.com/questions/5066411 tangent`；`"tangent vectors" "5066411"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 取得 MSE 原题完整正文，核 smoothness 体系、导子类型与局部性。；§28.7 的 bornological approximation property 不等于通常 Banach approximation property，引用时必须保留定义。

### QX-P-001791｜多面体二面角同时增大？

**旧卡 → 本轮变化：** 旧标签 `open`。原题要求两个组合等价且无自交的多面体逐边二面角不减时，是否所有对应角必相等；不是推出多面体全等。现有原页论证只给 Schläfli 公式控制的局部无穷小版本，未解决任意两端多面体的全局比较。

**按子问判断：** 任意两组合等价多面体的全局角比较：暂未找到可验证结果；本轮未得全局定理或反例；原页答复明确是局部微分观点。；光滑形变中的一阶同时非减：部分进展；Σ_e ℓ_e θ'_e=0 且 ℓ_e>0 排除非零的一阶全同号变化；不能由端点大小关系推整条路径单调。；所有角相同推出全等的旧释义：题面有误；整体缩放保持二面角但通常不全等；这不是原题欲证结论。

**直接证据与定位：**

- [原题全局 θ_e≤θ_f(e)；答复引用 Pak Thm 28.3 / Schläfli 公式](https://mathoverflow.net/questions/466174/is-it-possible-for-the-dihedral-angles-of-a-polyhedron-to-all-grow-simultaneousl) — 社区原题/部分论证；原题、答复正文已读。

**建议改动：** 把结论改回所有角相等；保留非自交与组合对应，另列凸多面体子问。；把 Schläfli 结论标为无穷小部分进展，不能据此标全题 solved。

**实际路径：** `site:math.stackexchange.com/questions/4866564 dihedral`；`"all dihedral angles" polyhedron increase`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 若新文构造所有二面角都变化的柔性多面体，还需核是否所有变化方向一致，不能据 all vary 判全题反例。

### QX-P-001792｜1/(n^p·sin n)→0 的 p 存在？

**旧卡 → 本轮变化：** 旧标签 `partially_solved`。存在性早已为真（p=7 即可）；p=1 不趋零可由 Dirichlet 逼近直接证明，旧卡把此边界当未知有误。2026 OpenAI 作者仓库声称 μ(π)=2，若该声明成立则全部可行 p 为 p>1、下确界 1 不取得；本轮未核完整证明或独立形式化。

**按子问判断：** 存在 p>0 使 1/(n^p sin n)→0：原题已证；Zeilberger–Zudilin 的 μ(π)≤7.103205334137 推出每个 p>6.103205334137 可行，特别是 p=7。；p=1 及 0<p≤1 的可行性：原题已反驳；本轮直接推论：无穷多 |π−a/q|<q^−2，令 n=a，则 |n sin n|≤(πq+1)/q 有界，故倒数不趋零；p<1 同一子列更不趋零。；所有 p>1 均可行、下确界 1 且不取到：完整证明/反例声明待核；作者仓库 thm:main 声称 μ(π)=2；该结论若成立，以上阈值由原题的 Diophantine 对应推出。未把作者声明等同已审核证明。

**直接证据与定位：**

- [三问与 Conrad 的 μ(π) 对应评论](https://math.stackexchange.com/questions/4385468/does-there-exist-any-p-0-such-that-frac1np-sinn-to-0-n-to-inft) — 社区原题；原题正文已读。
- [作者页面：2020 论文及 μ(π)≤7.103205334137](https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/pimeas.html) — 已刊结果作者入口；作者页面已读。
- [thm:main；紧邻文字说明 Q 非有效；协作固定提交 3344da59991ed94f9ba711217b29c1d760badfa6](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/build/main.tex) — 作者预印本/完整声明待核；main 源码页面正文已读；本分区固定提交 URL 访问失败；固定提交由同轮 a 分区核对，不作本分区独立获取。

**建议改动：** 存在性与 p=1 边界改为各自已知结论，撤去 p=1 未知的陈述。；μ=2 只记完整声明待核；与 QX-P-001765 的有效阈值要求分开，作者稿明确非有效 Q。；QX-P-000390 的二分叙述需另校：liminf≠0 不推出极限为∞。

**实际路径：** `site:math.stackexchange.com/questions/4385468 sin`；`"n^p" "sin n" "4385468"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 独立取得固定提交实际证明入口，审核主定理假设和依赖，再决定是否提升 p>1 尖锐阈值的状态。；本轮不运行外部 Lean，不给独立验证通过标签。

### QX-P-001793｜无小非平凡表示的群类

**旧卡 → 本轮变化：** 旧标签 `open`。发现可改变状态的已刊成果：Barbieri–Sabatini, Discrete Analysis 2025:21 的 Corollary D 与 PSL₂(q) 表值推出原题 a_n=Θ(n^{1/3})。这是从已刊结果到题面定义的短推论，解决增长阶问题，但不声称每个 n 的精确值已求出。

**按子问判断：** a_n 的数量级：原题已证；Corollary D 除 J1、O'N 两个有限例外外给 f(G)<|G|^{1/3}，例外吸收入绝对常数。对 n≥64，取 q=2^r≤n^{1/3}<2q，则 q≥4，PSL₂(q) 阶 q(q²−1)≤n 且 f=q−1≥q/2>n^{1/3}/4，故与上界合得 Θ(n^{1/3})。这是本轮基于已刊原文的推论。；每个 n 的精确 a_n：未作判断；增长阶解答不自动给逐 n 精确极值表。

**直接证据与定位：**

- [f(G)、a_n 定义与增长速度问题](https://math.stackexchange.com/questions/3574456/groups-with-no-small-nontrivial-representation) — 社区原题；原题正文已读。
- [Discrete Analysis 2025:21；2025-10-02；DOI 10.19086/da.144893](https://discreteanalysisjournal.com/article/144893-quasirandom-and-quasisimple-groups) — 已刊论文；期刊页已读。
- [Corollary D, p3；Table 2, p21（PSL₂(q), q even）](https://arxiv.org/pdf/2404.05550v3) — 已刊论文作者稿；期刊对应版本 PDF 已读并定位。

**建议改动：** 建议把增长阶子问更新为已解决，补记 a_n=Θ(n^{1/3}) 的推导与已刊出处。；历史 Sawin/MO 讨论仅作背景，不再作为最新状态的唯一依据。

**实际路径：** `site:math.stackexchange.com/questions/3574456 representations`；`"small" "representations" "3574456"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 如管理侧需要完全替换旧卡状态，请核“增长速度”是否还另含精确常数或逐 n 取值要求；本轮结论仅数量级。

### QX-P-001794｜(2^x−1)(3^y−1)=2z² 求解

**旧卡 → 本轮变化：** 旧标签 `partially_solved`。原式正整数全解仍未取得。原 MO 答复只完成 gcd(2^x−1,3^y−1)=1 子情形，明确留下非互素情形；旧卡将答复日期记成 2019 及泛化为全解均需校正。

**按子问判断：** 互素因子子情形：原题已证；2021-05-08 答复化为 x=1 及 2z²+1=3^y，引用 Nagell 的已知解 z=1,2,11；本轮已读答复，未独立重证 Nagell。；无互素假设的全题：部分进展；原答复明确未处理 gcd≠1；Rivin 的“Walsh 方法可照做”评论未提供完整对应证明。

**直接证据与定位：**

- [2021-05-08 答复；互素假设、Nagell 约化、Walsh 评论](https://mathoverflow.net/questions/296729/solve-this-diophantine-equation-2x-13y-1-2z2) — 社区部分证明；原题和答复正文已读。

**建议改动：** 保留正整数与互素子情形，修正答复日期；不要把因子 2 不同的 Walsh 方程直接套用。

**实际路径：** `"(2^x-1)(3^y-1)" "2z" integers`；`"2^x" "3^y" "2z" Fujita equation`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 取得并核一般 gcd≠1 情形的完整论证；本轮未核到历史所称 Fujita 2024 对应原文。

### QX-P-001795｜{a/(b+c)+b/(a+c)+c/(a+b)} 整数集刻画

**旧卡 → 本轮变化：** 旧标签 `open`。问题是按输入整数 n 决定是否存在正整数 a,b,c 使 a/(b+c)+b/(c+a)+c/(a+b)=n。2025 勘误只改有限表格，未给统一判定法；公开 UQ33 出现相互冲突的 AI 完整声明，其中有待核及人工验证失败，不能据此标已解决。

**按子问判断：** 整数值集合的无条件可计算性：暂未找到可验证结果；原问与作者论文/勘误未提供全输入的停机判定算法；依赖 BSD 的条件思路不等于无条件结论。；公开 AI 关于可计算/不可计算的完整声明：完整证明/反例声明待核；UQ33 中 K2Think 项待核；o3 Pro 项显示 Failed Human Verification；反向不可计算声明也有验证失败记录。仅看到预览及状态，不是已核论证。；2014 数值结果的 2025 修正：部分进展；勘误纠正 Table 2 的最小正解最大位数数据，不能据此推出集合可计算。

**直接证据与定位：**

- [按输入 n 的成员判定问题、正解与椭圆曲线讨论](https://mathoverflow.net/questions/278747/is-the-set-of-integers-of-the-form-a-bcb-acc-ab-computable) — 社区原题；原题正文已读。
- [Annales Mathematicae et Informaticae 43 (2014), 29–41](https://asu.elsevierpure.com/en/publications/an-unusual-cubic-representation-problem/) — 已刊论文元数据；机构作者题录/摘要；另检索到期刊整期扫描摘要。
- [AMI 62 (2025), 26–27；Table 2；DOI 10.33039/ami.2025.10.022](https://publikacio.uni-eszterhazy.hu/8862/1/AMI_62_from26to27.pdf) — 已刊勘误；勘误 PDF 已读。
- [2025-09-18 等提交；K2Think、o3 Pro、Gemini 状态](https://uq.stanford.edu/question/33) — AI 完整声明待核/已有失败标记；页面已读；只有答案预览及验证状态，完整证明未取得。

**建议改动：** 把人话版改成存在量词的可判定性；加入正性条件。；新增 2025 勘误与 UQ AI 状态，禁止把自动验证标志或失败声明写成已证。

**实际路径：** `site:mathoverflow.net/questions/278747`；`"a/(b+c)" "computable" "elliptic"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 逐项取得 UQ 完整答案、人工报告及最新验证结果，再核是否存在统一有效停机算法。；勘误只影响有限数据，勿据此变更可计算性状态。

### QX-P-001796｜树↔七元组树双射推广

**旧卡 → 本轮变化：** 旧标签 `partially_solved`。原题是无标号平面有根二叉树的自然双射推广，关系 T=1+T²；旧卡错写为 Cayley 标号树 T=xe^T。MO 三子问已有不同程度答复，Fiore–Leinster 一般定理有明确多项式假设；不能据此宣称任意线性递推树类均可七合一。

**按子问判断：** 二叉树 T⁷≅T 及适当多项式类推广：原题已证；Blass 七树与 Fiore–Leinster Thm 5.2 给已知构造/推广；该定理要求 p(x)−x primitive、次数≥2、常数非零且无重根，并限制 q1,q2 非常数。；Fibonacci 与二幂类型之间的对应：部分进展；原 MO 答复以 1、2 字符串的不同分级给自然对应，并指出有界长度偏移打包的计数障碍；不等于抽象可数集不存在双射。；公开程序是否构成可复核实现：未作判断；SML sto/ots 的 gist 只有搜索缓存，直接访问 404，未取得固定提交或运行。

**直接证据与定位：**

- [三个子问；Bruno Le Floch 答复；原树类定义](https://mathoverflow.net/questions/168913/to-what-extent-is-it-possible-to-generalise-a-natural-bijection-between-trees-an) — 社区原题/部分解答；原题与答复正文已读。
- [作者原稿，七棵独立二叉树的构造](https://sites.lsa.umich.edu/ablass/wp-content/uploads/sites/1471/2025/10/7trees.pdf) — 作者学术原稿；作者原稿检索摘要；本轮未整篇重审。
- [Theorem 5.2 的多项式假设](https://arxiv.org/pdf/math/0212377) — 作者学术原稿；作者 PDF 已读。
- [sto/ots 程序搜索片段](https://gist.github.com/liaopeiyuan/baa1baed65011df5ccb5c1a36d195c8d) — 公开代码线索不可达；仅代码缓存；直接打开 404；未执行。

**建议改动：** 纠正树的类型、T 方程与独立七元组；按三个子问拆状态。；给出 Fiore–Leinster 的全部适用条件，不套用线性 Fibonacci 特征式。

**实际路径：** `"trees" "seven" "817011"`；`"trees" "7-tuples" "bijection"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 若需要程序成果，先恢复固定版本代码和双射互逆性证明。；“自然”不是纯集合论等势，需约定构造允许的复杂度/长度变化。

### QX-P-001797｜"每有界算子达范数"的无穷维 Banach 空间

**旧卡 → 本轮变化：** 旧标签 `open`。原题限定每个有界线性自算子 T:X→X 都达范数。2026 新稿的可达摘要仍把该问题列为长期未解，并证明的是伴随/二重伴随变体；这些变体不能改写成原题解决。

**按子问判断：** 存在所有有界自算子均达范数的无限维 Banach 空间：暂未找到可验证结果；原讨论及 2026 作者摘要均未给全题解答；本轮也未获得可核完整新证明。；伴随/二重伴随达范数变体：部分进展；2609.00794 摘要有 c0、l1、c 上 NA2/NA3 结果；全文不可达，且命题并非 T 自身达范数。

**直接证据与定位：**

- [自算子量词、必要条件及讨论](https://mathoverflow.net/questions/232291/do-there-exist-infinite-dimensional-banach-spaces-in-which-every-bounded-linear) — 社区原题；原题搜索文本已读。
- [作者 arXiv 摘要；PDF https://arxiv.org/pdf/2609.00794](https://arxiv.org/abs/2609.00794) — 预印本摘要，全文不可达；仅搜索返回的作者摘要；abs/PDF 访问失败。

**建议改动：** 保留自算子量词；把 2026 伴随变体作为相关进展，不标原题已解。

**实际路径：** `"every" "bounded operator" "232291"`；`"Do there exist infinite-dimensional Banach spaces" "attains"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 取到 2609.00794 完整最新版本，核变体定义与必要条件；不能依二级 TheoremDB 状态替代。

### QX-P-001798｜镜面凸体遮光问题

**旧卡 → 本轮变化：** 旧标签 `open`。原题为平面点光源与有限个两两不交凸镜物体，问能否阻断所有逃向无穷远的射线。本轮新发现的 MacAulay 作者主页声明对圆盘情形作否定，但论文 PDF 不可达；仅能记圆盘子问题完整声明待核，不能扩为所有凸物体。

**按子问判断：** 任意有限不交凸镜体是否可完全阻光：暂未找到可验证结果；本轮未获完整范围的肯定构造或排除证明。；有限不交圆盘的否定声明：完整证明/反例声明待核；作者主页声称给出负面答案，社区新评论提及 Chernov–Dolgopyat；PDF 两入口均不可达，假设及论证未核。作者主页未提供声明发布日期，本轮发现日期不等于首次发表日期。

**直接证据与定位：**

- [点光源、两两不交凸体及圆盘/线段变体](https://mathoverflow.net/questions/156344/blocking-light-with-mirrored-convex-objects) — 社区原题；原题正文已读。
- [主页 enchanted forest / disks 写作链接](https://noahmacaulay.com/) — 作者完整声明；作者主页已读；只核到公开声明。
- [另入口 https://noahmacaulay.github.io/forest.pdf](https://noahmacaulay.com/forest.pdf) — 作者论文入口不可达；直接不可达；作者链接重定向返回 500，不假称全文核验。

**建议改动：** 修正点光源题面，并把圆盘声明单列待核，不覆盖一般凸体。

**实际路径：** `"Blocking light with mirrored convex objects"`；`"Blocking light with mirrored convex objects" MacAulay Chernov Dolgopyat`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 取得 forest.pdf 稳定版本，核圆盘之间严格不交、相切/擦碰轨道、所有初方向及逃逸的量词。；作者和社区声明尚不能替代完整证明审阅。

### QX-P-001799｜Cohen 猜想6：循环数 Legendre 类比

**旧卡 → 本轮变化：** 旧标签 `open`。Cohen Conj 6 是每个相邻整数平方间存在 cyclic 整数。Le 2509.26138 的相关全解声明已撤回；Pomerance 2026 正式期刊版明确仍把连续平方间命题称为猜想，不能把其双生/Goldbach/线性模式成果套用到本题。

**按子问判断：** cyclic Legendre / Cohen Conj 6：暂未找到可验证结果；已核原文及最新相关期刊版；撤回的 AI 辅助稿不计证明，Pomerance §4 末明确区分平方短区间。；Le 旧完整证明声明：未作判断；最新 v3 明示 withdrawn 及 AI 证明错误；已撤回声明不作原题成立证据。

**直接证据与定位：**

- [JIS 28 (2025), 25.4.7；Conjecture 6, p7](https://cs.uwaterloo.ca/journals/JIS/VOL28/Cohen/cohen41.pdf) — 已刊猜想原出处；期刊 PDF 已读。
- [v3，2025-11-06 撤回；版本说明涉及 AI 辅助证明错误](https://arxiv.org/abs/2509.26138) — 撤回预印本；arXiv 版本/撤回页已读；未把旧搜索摘要作为现状态。
- [INTEGERS 26A (2026), #A20；2026-09-28；p6 §4 末；DOI 10.5281/zenodo.23018287](https://math.colgate.edu/~integers/aap20/aap20.pdf) — 已刊相关进展，不解决本题；7 页正式期刊版已读，区别于先前 6 页预印本。

**建议改动：** 登记 Le 撤回及 Pomerance 正式期刊版；不要把研究论文的相邻猜想解决误归本题。；与 1701 标注 prime Legendre⇒cyclic Legendre 的强化关系；与同源 Cohen 条目标注不同问。

**实际路径：** `Cohen conjecture 6 cyclic numbers Le 2509.26138 withdrawn`；`Pomerance "cyclic numbers" "26A" 2026`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 有新的完整证明时核所有 n 及严格开区间，不以密度或有限计算替代。

### QX-P-001800｜Deligne 2025：相邻平方间素数个数 ∼ n/log n

**旧卡 → 本轮变化：** 旧标签 `open`。已核 Cohen Conj 8 的原始表述与 Deligne 2025-03-06 私人通信归属：相邻整数平方间素数数目 N_P(n)~n/log n。普通素数定理只给启发，不能直接推出如此短区间渐近；未取得本题新解。

**按子问判断：** N_P(n)~n/log n：暂未找到可验证结果；原刊原文明确为猜想；名称及 N_P/nlog 特征检索未得与此全称短区间渐近完全对应的证明。；从一般素数定理直接推出该式：题面有误；全局 π(x) 主项的误差不能直接相减成此尺度的渐近；只能作为启发式。

**直接证据与定位：**

- [Conjecture 8, p8；Deligne personal communication 2025-03-06](https://cs.uwaterloo.ca/journals/JIS/VOL28/Cohen/cohen41.pdf) — 已刊猜想原出处；期刊 PDF 已读。
- [Thm 1–2、§4；对象为 cyclic 数的若干模式](https://math.colgate.edu/~integers/aap20/aap20.pdf) — 已刊相关但不适用；全文已读；未声称本题素数短区间渐近。

**建议改动：** 补记原出处与精确逐区间渐近量词；不得写成 PNT 推论或 Pomerance 已解决。

**实际路径：** `Deligne Cohen conjecture 8 primes squares n log n 2025`；`"Deligne" "primes" "successive squares" conjecture proof`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 后续结果须区分平均区间、几乎所有 n、带假设及所有充分大 n。

### QX-P-001801｜Cohen 猜想22：k-fold Brocard（素数）

**旧卡 → 本轮变化：** 旧标签 `open`。旧卡混淆了 Brocard 的两个同名领域且遗漏阈值。Cohen Conj 22 前段对 k=4,…,20 给 B(k) 并论相邻素数平方；末段印刷原文却写相邻整数平方的一般 k 版本，须保留这一端点切换并待核是否勘误。

**按子问判断：** k=4,…,20 的指定 B(k) 断言：暂未找到可验证结果；原文给出有限数据支持的猜想，不是已证阈值表。；末段任意 k 的最终整数平方短区间断言：暂未找到可验证结果；按印刷原文保留端点和 ∃B(k)∀n≥B(k)；未得解决证据。；人话版无阈值/阶乘 Brocard 描述：题面有误；与原文量词、研究对象均不对应。

**直接证据与定位：**

- [p16，Conjecture 22 前后两段及其之前 B(k) 定义](https://cs.uwaterloo.ca/journals/JIS/VOL28/Cohen/cohen41.pdf) — 已刊猜想原出处；期刊 PDF 已读；已核印刷的端点切换。
- [Thm 1–2、§4；不为素数 k-fold Brocard](https://math.colgate.edu/~integers/aap20/aap20.pdf) — 已刊相关文献；全文已读；命中范围不适用。

**建议改动：** 按原刊恢复阈值和两段题面；将末段端点切换记为版本疑点，不擅自修成同一种端点。；解除与 QX-P-002321 阶乘平方间隔问题的同名误配，并标该参考卡对 1801 的说明也需纠正。

**实际路径：** `Cohen cyclic numbers JIS 25.4.7 conjecture 22`；`"k-fold Brocard" Cohen conjecture 22 proof`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 查作者勘误/确认末段是否有意强化为相邻整数平方；本轮未找到明确勘误。；B(k) 数表：2,2,3,5,5,5,7,7,10,10,10,10,10,13,13,13,13（k=4…20）仍为猜想值。

### QX-P-001802｜Cohen 猜想23：循环数 Brocard 类比

**旧卡 → 本轮变化：** 旧标签 `open`。原刊 Conj 23 明确 n>2。旧卡漏掉此条件会使 n=1,2 成为立即反例；另将 cyclic 数写成正密度也错误。修正后的 n>2 命题本轮未获可验解决，Pomerance 最新期刊版的模式结果不等价。

**按子问判断：** 含 n=1,2 的无条件旧题面：题面有误；原刊展示两个首区间各仅有两个 cyclic 数，故必须保留 n>2。；修正为 n>2 的 cyclic Brocard：暂未找到可验证结果；本轮核原刊、Pomerance 期刊版及名称/特征查询，未获得该短区间计数结论的证明。

**直接证据与定位：**

- [Conjecture 23, p16；n=1,2 的反例计数；引言 cyclic 渐近计数](https://cs.uwaterloo.ca/journals/JIS/VOL28/Cohen/cohen41.pdf) — 已刊猜想原出处；期刊 PDF 已读。
- [INTEGERS 26A (2026), #A20；Thm 1–2、§4 与 p6 平方间问题](https://math.colgate.edu/~integers/aap20/aap20.pdf) — 已刊相关进展；全文已读；线性模式/Goldbach/twins 不等价于本题。

**建议改动：** 补 n>2，撤正密度说法；将 C(x)~x/(e^γ log log log x) 与局部短区间结论分开。；与 Cohen Conj6/22 标同源不同问，不合并。

**实际路径：** `Pomerance 2026 cyclic numbers Cohen conjectures 23`；`Pomerance "cyclic numbers" "26A" 2026`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 后续证明必须处理相邻 cyclic 平方端点，不能套用相邻素数平方或固定线性模式的结果。

### QX-P-001803｜x²+1 型素数的椭圆类比

**旧卡 → 本轮变化：** 旧标签 `open`。原MO正文已取得。旧人话版将对象改成整数参数的素值族，未表达原题。原帖及本轮名称/曲线群阶平方特征检索未给出这一固定曲线、变化素数问题的完整解；不能由此确认开放。

**量词与范围：** 固定非CM椭圆曲线 E/Q，是否有无穷多个好素数 p 使 #E(F_p) 为完全平方？

**直接证据与定位：**

- [问题正文及作者对 arXiv:2003.09951 的回复](https://mathoverflow.net/questions/439985/elliptic-analogue-of-primes-of-the-form-x2-1) — 原始社区问题/回答；全文已读。问题是 #E(F_p) 平方；作者排除固定有限域上变动扩张次数的相邻结果。

**建议改动：** 将人话版替换为固定非CM曲线的平方群阶素数问题；不要写成Koblitz素群阶或Lang–Trotter固定迹。

**实际路径：** `"elliptic" "square" "439985"`；`"elliptic analogue" "x^2+1" primes`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 未做完整引文追踪；arXiv:2003.09951本轮仅核原帖的不适用说明，未读该论文全文。

### QX-P-001804｜Cohen 猜想64：SG 素数 HL-2 类比

**旧卡 → 本轮变化：** 旧标签 `open`。原刊Conjecture 64的下限是2，不是卡中全部正整数。错误扩展在m=n=1即失败，但这不反驳原猜想。未找到原范围完整证明或反例。

**量词与范围：** Cohen Conjecture 64：对整数 2≤m≤n，π_SG(m+n)≤π_SG(m)+π_SG(n)。

**直接证据与定位：**

- [印刷第29页（PDF第29页），Conjecture 64](https://cs.uwaterloo.ca/journals/JIS/VOL28/Cohen/cohen41.pdf) — 已刊原稿；全文已读。原文明确2≤m≤n；同页有限计算是作者报告。
- [cohen64_domain](附件/verify_small_checks.json) — 自写可复算核对；本轮独立整数算术。独立算出π_SG(2)=1，π_SG(1)=0；仅反驳卡片的错误量词。

**建议改动：** 补2≤m≤n；删除“并集计数所以应次可加”的不成立直觉。；与Conjecture66分开；后者反例不直接迁移至素数计数。

**实际路径：** `Cohen "Conjecture 64" "Sophie Germain"`；`"Cohen" "Conjecture 64" Sophie Germain subadditivity`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 原猜想64仍只记本轮未找到可验证全解，不据此写已确认开放。

### QX-P-001805｜Cohen 猜想66：SG 循环数 HL-2 类比

**旧卡 → 本轮变化：** 旧标签 `unknown`。Ibarra 2026预印本摘要提出31、3928反例。本轮按原刊定义独立重算：Cσ(31)=10，Cσ(3928)=686，Cσ(3959)=697，故697>696。此有限反例足以反驳原Conjecture66；Lean验证仍仅他人声明。

**量词与范围：** 对1≤m≤n，计数同时满足gcd(k,φ(k))=gcd(2k+1,φ(2k+1))=1的1≤k≤x整数，是否次可加？

**直接证据与定位：**

- [印刷第30页（PDF第30页），Conjecture 66及Cσ定义](https://cs.uwaterloo.ca/journals/JIS/VOL28/Cohen/cohen41.pdf) — 已刊原稿；全文已读。核实计数对象、1≤m≤n范围；其旧有限无反例报告与新小反例冲突。
- [Ibarra，2026-07-09，题名及摘要；工具ref turn174189605academia45](https://arxiv.org/abs/2607.09793) — 作者预印本索引；仅原站索引摘要；abs/PDF/anc多次DisabledError。摘要声明Cohen66反例并声称Lean4内核验证。
- [本轮自写Euler φ与gcd计数，1≤k≤3959](附件/verify_cohen66.py) — 独立有限算术复核；本地执行通过。精确反例31、3928已独立整数算术复核。

**建议改动：** 建议数学状态由unknown改为disproved，附精确反例与自写核对。；删除“Cσ定义未给出”；纠正原刊有限检索可信度，不将其沿用为本轮结论。

**实际路径：** `Cohen "Conjecture 66" cyclic numbers`；`"2607.09793" github Lean Ibarra`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** arXiv正文/最新修订及anc/cohen66.lean不可达；未取得依赖版本或重跑Lean。；预印本优先权和发表状况未作穷尽核验。

### QX-P-001806｜Clergyman 猜想（anti-k-nacci 自动性）

**旧卡 → 本轮变化：** 旧标签 `partially_solved`。Fokkink–Joshi arXiv:2506.13337v1 §3 Theorem8覆盖所有k≥2的全1系数anti-bonacci，解决本卡窄命题。其“restricted”指任意正权重更大猜想，不等于只证k=3,4。已核2026年Integers26 A24发表版。另有trureturing对全部正系数的形式化全解声明，独立列待核。

**量词与范围：** JIS Conjecture13：对k≥2，anti-k-nacci（连续k个缺项求和的互补贪心序列）减去(k²+1)n后为k-automatic。

**直接证据与定位：**

- [Conjecture13，印刷第16页](https://cs.uwaterloo.ca/journals/JIS/VOL28/Fokkink/fokkink9.pdf) — 已刊原稿；全文已读。原anti-k-nacci由缺项贪心互补规则定义；不是带负号的普通线性递推。
- [§3，Theorem8；提交记录v1 2025-06-16](https://arxiv.org/html/2506.13337v1) — 作者预印本；定理及上下文已读。全1权重任意k≥2的显式均匀替换与线性偏差公式；足以涵盖Clergyman窄命题。
- [Integers26 (2026) A24；首页出版2026-01-19](https://oro.open.ac.uk/109142/1/109142.pdf) — 作者机构存档/已刊稿；PDF已取得；定理定位使用arXiv版。确认Anti-recurrence sequences已刊，DOI10.5281/zenodo.18305140。
- [Evidence/Triage；D5/S1/Recurrence/AntiRecurrenceAutomaticity.result](https://github.com/the-omega-institute/trureturing/blob/d9395451c3b795eb34407c2783c87a793820d03d/Problems/fokkink-joshi-whole-antirecurrence-automaticity.md) — 作者仓库声明；固定提交问题说明与Blueprint已读，非Lean重跑。作者库声称全部正系数成立，公理闭包propext/Classical.choice/Quot.sound。
- [Walnut目录](https://cs.uwaterloo.ca/journals/JIS/VOL28/Fokkink/walnut/) — 作者代码目录；目录可达，未执行。原刊有配套计算材料；本轮仅读目录。

**建议改动：** 窄命题状态改为已证；人话版重写序列定义、线性主项和自动序列含义。；将任意正权重的更强猜想及公开形式化声明另列，不能用于否认窄命题已解决。

**实际路径：** `"Clergyman" conjecture anti k nacci Fokkink Joshi 2026`；`"Clergyman" "conjecture" anti`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** trureturing全权重定理尚需对应真实Lean文件、import闭包、工具链及原命题参数，再独立复跑；不得将其网站Proved标签当本轮验证。

### QX-P-001807｜交换代数导子-流实现

**旧卡 → 本轮变化：** 旧标签 `open`。找到MO#39745正式交叉帖及3个回答，改变旧卡“MSE无回答”的单源印象。Goodwillie指出无拓扑的全线性泛函导数过强，连紧光滑流形示例也不满足，提问者承认需修正。不能继续按一般导子均能指数化的统一猜想收录。

**量词与范围：** 原问寻求实交换含幺代数上所有导子具有流的充分条件；导数用所有代数线性h:A→R测试，定义本身受质疑。

**直接证据与定位：**

- [问题导数定义和作者2010-09-28评论](https://math.stackexchange.com/questions/4963/in-which-commutative-algebras-does-any-derivation-possess-a-flow) — 原始社区问题/回答；全文已读。作者承认定义问题并给MO交叉帖。
- [Tom Goodwillie 2010-09-24回答及作者认可评论](https://mathoverflow.net/questions/39745/in-which-commutative-algebras-does-any-derivation-possess-a-flow) — 原始社区问题/回答；全文已读。全代数线性泛函测试导数导致局部有限维限制；无拓扑情形不能沿用C∞示例。

**建议改动：** 补MO交叉帖，纠正“0回答”仅限MSE的范围。；重写为寻求充分条件的问题，先明确拓扑、连续性与局部/全局流。

**实际路径：** `"Does every derivation" "flow" commutative algebra`；`site:math.stackexchange.com "derivation" "flow" commutative algebra`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** MO另外两个回答本轮只获页面、未完整审计；不能宣称已得到统一充分必要条件。

### QX-P-001808｜复合平方根存在性

**旧卡 → 本轮变化：** 旧标签 `open`。原MSE取得。2022 Chen–Scheinerman论文明确研究任意集合上的同类方程，并提示Isaacs主定理及有限集NP完全性；期刊全文403，不能仅凭摘要判定原帖全部问题已解决。Scheinerman Julia库只实现有限置换的平方根。

**量词与范围：** 任意集合A上的自映射g，何时存在f:A→A使f∘f=g？原帖含无限集合与集合论子问。

**直接证据与定位：**

- [问题正文与子问](https://math.stackexchange.com/questions/120405/compositional-square-roots) — 原始社区问题/回答；全文已读。不限连续/可测函数；核心是一般自映射及函数图/无限集合。
- [Chen–Scheinerman 2022摘要与脚注1](https://www.tandfonline.com/doi/full/10.1080/00029890.2022.2105054) — 已刊作者论文索引；仅摘要/索引脚注，全文403。可检索到一般g:A→A、Isaacs与Kosaraju文献线索。
- [README sqrt功能](https://github.com/scheinerman/Permutations.jl) — 作者仓库；README已打开；未运行。有限置换的复合平方根实现，非任意非单射自映射刻画。

**建议改动：** 保持任意集合自映射范围；添加2022文献线索并列为优先全文复核。

**实际路径：** `"120405" "square" function math.stackexchange`；`site:math.stackexchange.com "120405"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 取得Chen–Scheinerman与Isaacs原文，核对其主定理是否覆盖原帖无限集合/CH子问。

### QX-P-001813｜⌊ζ(−n)⌋ 仅 n=23 素？

**旧卡 → 本轮变化：** 旧标签 `open`。原帖可达。卡片将负整数zeta零点奇偶性写反：ζ(−2m)=0，奇n用Bernoulli公式。独立小核算ζ(−23)=236364091/65520，向下取整3607为素数。唯一性仍未找到完整证明；有限搜索作者报告不能升格。

**量词与范围：** 对于正整数n，⌊ζ(−n)⌋是否仅n=23时为正素数？

**直接证据与定位：**

- [问题Bernoulli公式、代码及2019评论](https://math.stackexchange.com/questions/3257373/is-lfloor-zeta-n-rfloor-only-prime-for-n-23) — 原始社区问题/回答；全文已读。原帖考虑奇负整数处非零值及3607；只提供有限搜索。
- [zeta23及zeta_even](附件/verify_small_checks.json) — 有限算术核对；本轮本地精确计算。自写调用已装SymPy求精确有理数、取整与素性核对。

**建议改动：** 把“奇n为零/偶n非零”反转为正确奇偶性。；唯一性命题保留未获全解，不写数学已反驳。

**实际路径：** `"3257373" zeta prime`；`site:math.stackexchange.com/questions/3257373`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 未复算原帖上万项Bernoulli/素性检验；折叠评论不保证全取。

### QX-P-001814｜2↑↑∞ + 3 是否被素数整除（2-adic 形式化）

**旧卡 → 本轮变化：** 旧标签 `open`。原MO与作者GPU仓库可达。2026-07更新报告p<6×10^15未发现因子，范围由旧检索与新区间重叠拼合，未独立验证。作者README明确原始推导/代码由ChatGPT5.6 sol生成且作者未独立复核。此为公开AI计算进展，非无因子证明。

**量词与范围：** 模每个正整数m稳定的无限2幂塔T，是否存在素数p使T≡−3 mod p？

**直接证据与定位：**

- [定义及2026-07-30更新](https://mathoverflow.net/questions/479419/is-2-uparrow-uparrow-infty-3-divisible-by-a-prime-number) — 原始社区问题/回答；全文已读。定义是各模数稳定；有限检索上限更新。
- [README AI authorship、Search history、Zero-loss pipeline；runs/2026-07-27--2026-07-30-rtx5090](https://github.com/hzyhhzy/infinite-tetration-factor-search) — 作者代码/计算声明；README与检索说明已读；commit SHA未取得。作者报告[1.1e12,6e15)无因子并明确AI生成；无独立审计。

**建议改动：** 将2-adic表述改为profinite/各模数稳定；仅2-adic极限0不足以讨论奇素数。；更新AI暴露为公开计算/推导；不把无因子范围当全解。

**实际路径：** `"2↑↑∞" "3" prime`；`site:github.com "infinite tetration" "3"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 固定commit、完整运行日志和CPU/GPU算法正确性待审核；未运行外部代码。

### QX-P-001816｜连续二项式系数低次插值退化

**旧卡 → 本轮变化：** 旧标签 `open`。原帖consecutive被译成continuous，改变对象。其判据为m阶差分Σ(-1)^i C(m,i)C(n,k+i)=0，含Hermite主项子问。原帖给若干小m计算，未取得一般分类。

**量词与范围：** 固定整数n与m,k，m+1个连续二项式系数C(n,k),…,C(n,k+m)何时可由次数≤m−1的多项式在相邻整数上插值？

**直接证据与定位：**

- [问题正文、Q1/Q2与评论](https://math.stackexchange.com/questions/5033916/when-can-m1-consecutive-binomial-coefficients-be-interpolated-by-a-polynomial) — 原始社区问题/回答；全文已读。固定Pascal行上的连续项；低次数插值退化，不是连续变量广义二项式。

**建议改动：** 修正中英文标题continuous→consecutive；补m+1点与次数≤m−1。

**实际路径：** `"binomial coefficients" "polynomial" "5033916"`；`"consecutive binomial coefficients" "polynomial" interpolation`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** Krawtchouk/超几何变换与Hermite极限是后续方向，本轮未核足以全解的定理。

### QX-P-001817｜f(f′)=x 的 a.e. 解

**旧卡 → 本轮变化：** 旧标签 `partially_solved`。MSE及MO交叉帖均核。Chamberland只给x>0的幂函数；评论中的偶延拓与奇延拓都会使复合为|x|，随后被指出。不能把这一回答算全实轴解。

**量词与范围：** 是否有全实轴连续、几乎处处可微的f:R→R，使f(f′(x))=x几乎处处成立？

**直接证据与定位：**

- [问题正文](https://math.stackexchange.com/questions/3313126/existence-of-function-satisfying-ffx-x-almost-everywhere) — 原始社区问题/回答；全文已读。保留全局连续及a.e.可微条件。
- [Marc Chamberland回答及Pietro Majer 2019-08-05评论](https://mathoverflow.net/questions/337607/existence-of-function-satisfying-ffx-x-almost-everywhere) — 原始社区问题/回答；全文已读。正半轴有解，两个常见全轴延拓失败；全轴连续原问未解决。

**建议改动：** 人话版须明确全实轴和连续性；正半轴解单列部分结果。

**实际路径：** `"functional equation" "3313126"`；`"f(f'(x))=x" almost everywhere`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 未重新证明全处可微版本不存在；只读原帖及交叉帖的证据范围。

### QX-P-001818｜指定奇异值保体积微分同胚

**旧卡 → 本轮变化：** 旧标签 `partially_solved`。原问题两半须分开。MO构造中平移远离原点的径向缩放及角度放大映射改善映射半问到σ1<1/2；穿孔盘映射不在原点可微，不能解决整盘微分同胚。Gevirtz2003 Conjecture7.1提出无非平凡cps圆盘自同胚；本轮期刊PDF不可达，只核原作者/原讨论引文及索引。

**量词与范围：** 给定常数0<σ1<σ2且σ1σ2=1，闭单位圆盘是否有导数处处具有这两个奇异值的光滑映射/微分同胚？

**直接证据与定位：**

- [问题、Panov/OP构造与2021评论](https://mathoverflow.net/questions/352982/is-there-a-volume-preserving-diffeomorphism-of-the-disk-with-prescribed-singular) — 原始社区问题/回答；全文已读。σ是固定常数；任意平移a>1的改进给σ1<1/2映射；微分同胚半问另在。
- [原MSE索引正文](https://math.stackexchange.com/questions/3531282/is-there-a-volume-preserving-diffeomorphism-of-the-disk-with-prescribed-singular) — 原始社区问题；搜索索引正文。确认与MO为同一原问。
- [Gevirtz，2003，pp739–776，Conjecture7.1 p775](https://doi.org/10.1155/S0161171203204166) — 已刊原稿线索；原稿链接不可达；仅原讨论与题名/摘要索引。相关猜想为无cps圆盘自同胚；原PDF本轮不可达。

**建议改动：** σ1、σ2是固定常数，奇异值来自(Df)^T Df而非Df本身特征值。；更新映射半问已知范围<1/2；保持整盘微分同胚为单独子问。

**实际路径：** `"3531282" singular values diffeomorphism`；`"volume-preserving" "singular values" disk diffeomorphism Gevirtz`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 补Gevirtz原稿及后续引文；不因本轮无新解断定一般开放。

### QX-P-001819｜平方和保持型数列刻画

**旧卡 → 本轮变化：** 旧标签 `open`。原帖允许0和非负项已明确。2023周期4的{r,s,t,s}族否定“只有常数/线性”的期望，但原分类问题并未因此终结。另已读线性化六维解空间回答，原问还要求函数值为非负平方，需单独处理。

**量词与范围：** 非负整数序列(a_n)（含n=0），保持全部i²+j²=k²+l²⇒a_i²+a_j²=a_k²+a_l²，求所有序列。

**直接证据与定位：**

- [问题定义及uvdose 2023-08-07评论](https://math.stackexchange.com/questions/1162534/looking-for-all-sequences-such-that-a-i2a-j2-a-k2a-l2-whenever-i2j2) — 原始社区问题/回答；全文已读。非负整数、含0；mod4三参数周期族是原期望分类反例。
- [Julian Rosen 2020-10-04回答](https://math.stackexchange.com/questions/3850115/dimension-of-subspace-defined-by-a2b2-c2d2-rightarrow-fafb-fcfd) — 原始社区问题/回答；全文已读。线性化函数空间为六维，加入3倍数指示与mod5 Legendre符号；不直接移除平方值约束。
- [2023回答公式](https://math.stackexchange.com/questions/4743181/sequences-a-n-such-that-i2j2-k2-ell2-longrightarrow-a-ia-j-a-ka-e) — 原始社区回答；索引正文。含0线性化给六初值表达，属于邻近问题。

**建议改动：** 删“是否允许负项需约定”，写明原帖非负且含0。；把期望分类被反驳与完整分类未核分开。

**实际路径：** `"1162534" squares sequence`；`"sequence" "i^2+j^2=k^2+l^2"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 六维线性化在平方值约束下能否完成分类，本轮不深入证明。

### QX-P-001820｜列子集和互异矩阵最大宽度

**旧卡 → 本轮变化：** 旧标签 `open`。原帖问宽高比而非没有固定行数的“最大列数”。原PPCG构造为36/19，附Java代码，但本轮未执行。一般无循环约束的检测矩阵问题不是简单F2线性无关，MO交叉相关问给2n/log2 n量级背景；不能说删circulant便平凡。

**量词与范围：** m×n的部分循环0–1矩阵无两列子集同和时，列/行比n/m是否有上界2？

**直接证据与定位：**

- [问题正文与评论](https://math.stackexchange.com/questions/1017169/upper-bound-for-the-widest-matrix-with-no-two-subsets-of-columns-with-the-same-v) — 原始社区问题/回答；全文已读。有限行数、列/行比2猜测；低票1.5回答与已知构造冲突。
- [Peter Taylor Java答案36/19与源代码](https://codegolf.stackexchange.com/questions/41021/find-highest-scoring-matrix-without-property-x) — 原始社区问题/回答；全文已读。可复核构造/搜索代码已公开，当前未运行；有限搜索不证明上界。
- [问题正文与非稀疏限定](https://mathoverflow.net/questions/208015/a-circulant-coin-weighing-problem) — 原始社区问题/回答；全文已读。一般coin-weighing与部分循环版本分开；压缩感知的稀疏假设不能代替全部子集。

**建议改动：** 改为部分循环矩阵的列/行比上界；删除漏circulant则平凡及F2线性无关的错误解释。

**实际路径：** `"1017169" matrix circulant`；`"widest matrix" "subsets" columns circulant`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 未审计/运行PPCG Java；MO后续完整答案未全审，未找到上界2的证明。

### QX-P-001822｜a⁴+b⁴+c⁴=d⁴+kabcd 本原解

**旧卡 → 本轮变化：** 旧标签 `open`。原帖精确剩余十个k已核，不能泛化为任意整数解。k=−1的(263,904,2462,2497)本轮精确验证，但它不属剩余十问；其倍数均非本原，不能证明本原解无穷。旧卡GPU范围在当前折叠评论未完整取到，未沿用为本轮已验。

**量词与范围：** 对k∈{−10,−8,−7,−6,−5,−3,3,5,7,10}，求a,b,c,d均正且gcd=1的a⁴+b⁴+c⁴=d⁴+kabcd解。

**直接证据与定位：**

- [正文及可见评论；展开评论尝试未新增内容](https://math.stackexchange.com/questions/5122227/primitive-positive-integer-solutions-of-a4-b4-c4-d4-kabcd) — 原始社区问题/回答；全文已读。正整数、本原与十个指定k；−1例另列。
- [quartic_minus1](附件/verify_small_checks.json) — 有限算术核对；本轮精确计算。验证给定四元组满足k=−1且gcd=1。
- [Veselovac–Piezas 2026摘要](https://arxiv.org/abs/2610.12181) — 作者预印本；仅原站摘要。四个四次方和等第五个四次方的线性切片，变量/方程不同，非本题全解。

**建议改动：** 显式限制正整数与十个k；将−1唯一性写成未证，不能由唯一已知改成唯一。

**实际路径：** `"5122227" primitive fourth powers`；`"a^4+b^4+c^4" "kabcd" primitive`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 补取全部GPU评论及搜索日志、精确范围；不运行外部代码。

### QX-P-001824｜⌊αn⌋ 序列等和切分（题面修正）

**旧卡 → 本轮变化：** 旧标签 `open`。原帖已核，是从1开始的前缀切为两连续段，不是任意多段。作者列整数α/Pell、部分α范围与有理数实验；本轮未找到全实数α的完整证明或反例。

**量词与范围：** 对每个实数α，是否存在正整数k<l使Σ_{n=1}^k⌊αn⌋=Σ_{n=k+1}^l⌊αn⌋？是否总有无穷多对？

**直接证据与定位：**

- [正文定义、进一步问题及My try](https://math.stackexchange.com/questions/4836880/can-the-sequence-lfloor-alpha-n-rfloor-be-divided-into-two-parts-with-e) — 原始社区问题/回答；全文已读。明确两个连续段、实参数，71/3大例属于作者报告。

**建议改动：** 补精确两段等和式与k<l，删除“切成几段未写明”。

**实际路径：** `"floor" "alpha n" "equal" "4836880"`；`"4836880" equal sums floor`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 未独立复验71/3超大最小解；有理数实验不升级为全实数定理。

### QX-P-001825｜正整数递推 c_{n+1}=c_n(c_n+n+d)/n 存在性

**旧卡 → 本轮变化：** 旧标签 `open`。原MO必须严格递增，且问某个d存在，不是要求给出全部d分类。若漏递增，c_n≡c、d=−c提供平凡正整数常数列。原帖2025编辑后仍只有动力系统/cluster线索，无一般解。

**量词与范围：** 是否存在某个整数d和严格递增正整数序列c_n，对所有n≥1满足c_{n+1}=c_n(c_n+n+d)/n？

**直接证据与定位：**

- [问题框、2025-08-09编辑及Sawin/Hopkins评论](https://mathoverflow.net/questions/282159/is-there-any-positive-integer-sequence-c-n1-fracc-nc-nndn) — 原始社区问题/回答；全文已读。严格递增、n≥1、某整数常数d；从k>1起是独立扩展。

**建议改动：** 补严格递增；主问恢复存在性，将所有d分类及晚起点作为另加子问。

**实际路径：** `"c_n" "c_n+n+d" integers`；`"recurrence" "c_n" "n+d" "integer"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** p-adic与Laurent现象仅评论方向，未取得实现或排除所有轨道的定理。

### QX-P-001826｜凸性半径连续性

**旧卡 → 本轮变化：** 旧标签 `open`。发现Xu2017原稿Theorem1.7明确反驳(A)普遍连续：维数≥2可有z_i→z且conv_ct(z_i)<2、conv_ct(z)>10；(B)按定义为1-Lipschitz。原帖写(C)而未加所有更小半径，故须先修定义，再认定(A)已反驳，不能把三者混称仍开放。

**量词与范围：** 须区分：(A)所有≤r同心球凸的conv_ct(p)；(B)B_r(p)内任意子球凸的conv(p)；(C)原帖仅单个凸球半径的sup。

**直接证据与定位：**

- [问题首段定义](https://math.stackexchange.com/questions/4461581/is-the-convexity-radius-continuous) — 原始社区问题/回答；全文已读。仅写sup单个凸球；未明示所有更小同心球。
- [Shicheng Xu；v2 2017-06-29；DOI10.1142/S0219199717500602](https://arxiv.org/abs/1704.03269) — 作者预印本/已刊对应；原站元数据已读。版本说明由pointed改称concentric。
- [§1第4–5页定义与Theorem1.7；§4第16–17页Theorem4.1及证明](https://arxiv.org/pdf/1704.03269) — 作者原稿；定义、定理及构造结尾已读。区分1-Lipschitz的内含子球版本与不连续的同心版本；有具体反例构造。
- [原题链接的重复讨论](https://math.stackexchange.com/questions/4330131/convexity-radius-function-on-manifold-is-continuous) — 原始社区入口；页面已取得。同题源线索已打开；本轮未重新审计其错误答案全过程。

**建议改动：** 将凸性半径定义分流；标准同心版本标已反驳，并引Xu Theorem1.7。；若坚持单个凸球sup的字面定义，需单独核对反例适用，不能自动宣称全解。

**实际路径：** `"convexity radius" "continuous" Ehrlich Ferrera`；`"concentric convexity radius" discontinuous`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 本轮未证明(C)与(A)等价；后续须回到原问者约定，或以标准(A)修题。；未独立形式化Xu几何反例。

### QX-P-001827｜自指标准差递推渐近

**旧卡 → 本轮变化：** 旧标签 `open`。MSE#4190405直接/替代/API不可达，标准差递推名称、asymptotic及0.3522011特征检索未取得原文或匹配原稿。旧卡给出的衰减拟合与人话版增长描述冲突，不能将历史拟合作本轮证据。总体标准差下有简单有界性，故人话版c√n正系数增长不合理，但精确衰减指数本轮不判。

**量词与范围：** x_{n+1}=Stdev(x_1,…,x_n)的渐近；初值与样本/总体标准差约定待取原文。

**直接证据与定位：**

- [原ID及API尝试](https://math.stackexchange.com/questions/4190405) — 原始社区入口；不可达。本轮未取得正文、初值或标准差分母。

**建议改动：** 要求补初值及标准差定义；删无来源的c√n增长猜测。

**实际路径：** `"4190405" standard deviation sequence`；`site:math.stackexchange.com "standard deviation" "sequence" "0.352"`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 未重新核0.3522011指数或0.54常数；需原帖后才能判其推导/经验地位。

### QX-P-001828｜数字串联数列中的素数

**旧卡 → 本轮变化：** 旧标签 `open`。原MSE确认主问为存在素数，而不是直接问无穷多。OEIS A007908本轮403但搜索索引报告Mersenne Forum到n=344869无素数；不沿用旧卡约10^6项。2025 Ripà说明处理循环移位及筛法，不是基础拼接序列找到素数。

**量词与范围：** C_n=十进制串联1,2,…,n；是否至少存在一个素数项？

**直接证据与定位：**

- [UPD问题与OEIS链接](https://math.stackexchange.com/questions/4084257/whether-there-is-a-prime-in-sequence-1-12-123-1234-12345-123456-1234567-12345) — 原始社区问题/回答；全文已读。主问至少一个素数项；原发帖者有限检查到500。
- [搜索ref turn338158100search0/2；COMMENTS摘要](https://oeis.org/A007908) — 数据库编辑记录；仅索引摘要，原页403。目前索引报告344869范围，原页403；不作独立计算或最新纪录确认。
- [Marco Ripà，2025-10-18 v1，Description](https://zenodo.org/records/17382562) — 作者预印本；作者摘要已读。研究S(r)的循环移位和模筛周期，不能替代原拼接序列。
- [检索到oeis-research/Amarnath Murthy/拼接数最大素因子/prog.sf](https://github.com/trizen/experimental-projects) — 作者代码索引；仅搜索索引，未执行。有限因数计算程序线索，非存在素数的证明。

**建议改动：** 主问固定为至少一素数；纠正无可核依据的10^6范围。；与任意数字截断Champernowne前缀及循环移位分开。

**实际路径：** `"1,12,123" "prime" "4084257"`；`"A007908" prime found`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** OEIS主页面和Mersenne Forum日志未完整取得；不能宣称截至今天绝无已知素数。

### QX-P-001829｜ℵ_ω 处朴素力迫违反 SCH

**旧卡 → 本轮变化：** 旧标签 `open`。MSE和MO交叉帖已读：原方案从大基数/Prikry扩张出发；卡片“不靠大基数”的解释错误。SCH也不是对全部奇异κ断言2^κ=κ^{cfκ}。Jech1990原章节书目核实，全文只到付费入口；不能把评论引用当已读定理或完整解。

**量词与范围：** 在Prikry扩张后以满支撑乘积/迭代Levy塌缩将奇异强极限κ变为ℵ_ω时，是否必塌缩κ^{++}，破坏既有2^κ=κ^{++}？

**直接证据与定位：**

- [问题正文与Hannes Jakob 2023评论](https://math.stackexchange.com/questions/4679785/naive-way-to-violate-sch-at-aleph-omega) — 原始社区问题/回答；全文已读。Prikry后乘积Col(κ_n^+,κ_{n+1})是否塌缩κ^{++}，可改变κ_n选择。
- [正文具体问题与Jech讨论](https://mathoverflow.net/questions/466283/naive-way-to-violate-mathsfsch-at-aleph-omega) — 原始社区问题/回答；全文已读。MO进一步问Col(κ_n^{++},<κ_{n+1})版本；具体塌缩方案区别于一般一致性。
- [Thomas Jech，A Tribute to Paul Erdős，1990，DOI10.1017/CBO9780511983917.021](https://www.cambridge.org/core/books/abs/tribute-to-paul-erdos/on-the-cofinality-of-countable-products-of-cardinal-numbers/BC14F2058702E4A83C163D179E555A75) — 原出版社书目；书目页可达，正文受限。确认章节存在，全文未取得。

**建议改动：** 纠正SCH常用强极限奇异版本2^κ=κ^+；删除“不靠大基数”。；区分MSE/MO两个具体乘积版本与一般κ^+-c.c.问题。

**实际路径：** `"naive" "forcing" "SCH"`；`"On the cofinality of countable products of cardinal numbers" Jech`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** Jech章节全文及Abraham–Magidor相关内容未读；对非Prikry泛序列的情形未判。

### QX-P-001830｜随机骨牌铺砌测度良定性

**旧卡 → 本轮变化：** 旧标签 `partially_solved`。原题由 MSE 交叉帖定位到 MO382808。方形/环面中心极限与局部统计已有经典 Gibbs/determinantal 理论；任意耗尽边界无关并不成立。逐步精确采样子问仍需单列，本轮未取得覆盖其全部要求的算法证明。

**按子问判断：** 均匀方形/环面耗尽的中心极限及局部概率：部分进展；Cohn 答复给出经典文献链；不可推广成任意边界条件均同一极限。；逐步输出无限铺砌的精确采样要求：暂未找到可验证结果；仅限本轮已列入口；答主不确定采样文献不是开放性证明。

**直接证据与定位：**

- [原问题；Henry Cohn 2021-02-02 答复；Speyer 同日评论](https://mathoverflow.net/questions/382808/random-domino-tilings-is-this-distribution-well-defined-and-how-can-it-be-samp) — 原始社区问题与专家答复；全文已读。区分最大熵 Gibbs 测度、边界高度/斜率依赖、局部概率与采样。原 MSE 短链接访问失败后成功追回交叉帖。

**建议改动：** 笼统铺砌测度良定性，可能被读成任意区域/权重 → 限定均匀正方形耗尽；另列环面、Aztec diamond、一般边界、可渐进精确采样。

**实际路径：** `random domino tiling measure Henry Cohn 382808 maximal entropy sampling`；`uniform infinite domino tiling finite cylinder probabilities Burton Pemantle Kenyon Sheffield`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 如需确认采样子问，沿 Burton–Pemantle / Wilson 森林采样对应逐项核对算法输出与无偏性；本轮仅初查。

### QX-P-001831｜四面体穿最小孔洞

**旧卡 → 本轮变化：** 旧标签 `partially_solved`。题目是单位正四面体穿过平面孔洞的最小面积，不是 Rupert 型同体穿孔。2012 原论文 p17 Problem1 已明确提出同一面积问题；1/√8 是仅平移时的最优面积，允许转动的任意形状孔洞仍不能由该定理解决。

**按子问判断：** 仅平移最小孔面积：原题已证；限定子问，面积1/√8。；允许任意刚体运动、任意孔形的最小面积：暂未找到可验证结果；2012 Problem1 与原帖对应；本轮未查得后续完整解答，不据此断言截至今日仍开放。

**直接证据与定位：**

- [问题正文及文献评论](https://math.stackexchange.com/questions/4102164/fitting-a-tetrahedron-through-the-smallest-hole?r=31) — 原始问题；全文已读。问题优化的是平面孔面积，允许物体转动。
- [Bárány–Maehara–Tokushige, Computational Geometry45(2012), p17 Problem1；Theorems2–3](https://www.renyi.hu/~barany/cikkek/127.pdf) — 已刊论文；全文定位已读。任意三角孔可转化为平移；最小等边三角孔和一般最小面积是不同问题。

**建议改动：** 与相同四面体钻孔/孔径问题相混 → 改为平面孔面积优化；列已知上界1/√8及仅平移最优，不把特定孔形结果当全解。

**实际路径：** `tetrahedron smallest hole Maehara Itoh Tanoue Zamfirescu minimum area`；`unit regular tetrahedron passing through planar hole sqrt2 4 optimal area`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 复核2012论文后续引用中的任意孔形、允许转动版本。

### QX-P-001832｜Penrose 铺砌与 Fibonacci 词分形

**旧卡 → 本轮变化：** 旧标签 `open`。原帖只猜特定 P3 膨胀构造、偶数代、指定射线所平分的菱形读出的0/1词与 OEIS A221150 一致；题卡概括为一般 Penrose 与标准 Fibonacci 词对应会扩大命题。四个指定 Fibonacci 配对全文均非同题。

**按子问判断：** 原帖指定种子/射线/偶数代的词一致性：暂未找到可验证结果；需保留两种菱形编码、射线及偶数代量词；一般 substitution 文献不能直接替代。；现题面范围：题面有误；删去任意 Penrose 铺砌均有该性质的暗示。

**直接证据与定位：**

- [正文图示与第6、8代观察](https://math.stackexchange.com/questions/2993076/a-conjecture-about-the-connection-between-a-penrose-tiling-and-the-fibonacci-wor) — 原始问题；全文已读。具体切线所平分菱形的有限词是目标，不是一般数字Fibonacci的算术性质。

**建议改动：** Penrose铺砌与Fibonacci词的一般对应 → 恢复原帖特定切线、种子、编码和所有偶数代的猜想。

**实际路径：** `Penrose tilings Fibonacci word fractal 2993076`；`Fibonacci word fractal 72 degree 144 degree Penrose tiling relation`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 图示的种子与替换规则需在深查时形式化；本轮未把有限图像一致当归纳证明。

### QX-P-001833｜3D Rep-tiles/Irreptiles 分类

**旧卡 → 本轮变化：** 旧标签 `open`。原帖征求排除 polycube 与二维 rep-tile 柱体之后的三维例子。Blair–Marley–Richards 的同胚分类是相关进展，不能作为这些几何排除条件下的完整分类。

**按子问判断：** 紧三维流形rep-tile的拓扑分类：部分进展；arXiv2107.10216摘要为同胚类型分类，非原帖要求的几何形状分类。；原帖排除两类平凡构造后的例子/分类：暂未找到可验证结果；保留非polycube、非二维挤出限定。

**直接证据与定位：**

- [问题正文、2024评论](https://math.stackexchange.com/questions/2839754/3d-rep-tiles-and-irreptiles?r=31) — 原始问题；全文已读。明确排除两类易得构造；irreptile允许不同尺寸的小相似块。
- [v1(2021-07-21)摘要](https://arxiv.org/abs/2107.10216) — 预印本；摘要已读；HTML全文入口失败。分类对象是同胚类型：S³中连通图的外部。

**建议改动：** 泛称全部3D rep-tiles/irreptiles分类 → 改回原帖几何例子问题，拓扑分类单列且注明不覆盖排除项。

**实际路径：** `three dimensional rep tiles irreptiles classification Ed Pegg 2839754`；`Blair Marley Richards 2107.10216 rep tiles non polycube topology`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 如新增具体构造，逐项核查是否仅为polycube或二维挤出。

### QX-P-001834｜对称张量 Type-2 常数上界

**旧卡 → 本轮变化：** 旧标签 `partially_solved`。Conjecture16的r是张量阶数、p≥2是ℓp注入范数参数，隐常数可依赖r,p。题卡把p当张量阶数并暗示对阶数统一，会改变命题。p≥2r已有几何方法进展，经典矩阵r=p=2结论本身不是待证猜想。

**按子问判断：** 一般r,p的type-2量级：部分进展；已知范围p≥2r；仍须保留多对数损失和r,p依赖。；题卡参数解释：题面有误；r与p角色混淆、常数统一性扩大。

**直接证据与定位：**

- [Entry8 Conjecture16及紧随讨论](https://arxiv.org/html/2603.29571v1) — 原始问题汇编；全文定位已读。对称r阶张量的ℓp注入范数，目标d^(1/2−1/p)乘平方和且容许polylog损失。
- [Bandeira–Gopi–Jiang–Lucca–Rothvoss v1摘要；原汇编BGJLR引用](https://arxiv.org/abs/2411.10633) — 研究预印本/后续会议论文线索；摘要已读。几何覆盖数方法给部分参数范围的近最优维度依赖；不能认作全r,p解决。

**建议改动：** p为张量阶数、可能对所有阶数统一 → 分开r阶与p范数；允许常数依赖r,p；把已知参数区间单列。

**实际路径：** `Type 2 constants symmetric tensors injective lp norms 2411.10633`；`Gaussian tensor series p >= 2r d^(1/2-1/p) type two bound`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 若声称全解，检查2≤p<2r区间及对称性、维度/样本数的polylog依赖。

### QX-P-001835｜E ϑ(G(n,1/2))=√n

**旧卡 → 本轮变化：** 旧标签 `claimed`。Potechin–Xu论文主定理给G(n,1/2)的θ/√n依概率趋1，FOCS2026官网已列录用，旧卡“仅未评审声明”应更新。期望式可由该定理与标准符号矩阵的L²范数控制推出（此转移是本轮推论）。另有2026-11-23 aiXiv统一两模型论文与Lean源码，另记未独立重跑。

**按子问判断：** Eθ(G(n,1/2))/√n→1：原题已证；依据Potechin–Xu Theorem1.2/Corollary1.3；期望转移详见本轮推导说明，不把w.h.p.直接等同期望。；Jin统一两模型新证明及形式化：完整证明/反例声明待核；aiXiv论文与代码可取得；本轮未审完全部依赖、未运行Lean。

**直接证据与定位：**

- [Potechin–Xu v1, PDF第4页 Theorem1.2 / Corollary1.3](https://arxiv.org/pdf/2609.30064) — 会议录用论文，预印本全文可读；全文主定理已读。给独立边模型高概率sharp常数1。
- [Accepted papers: The Lovász Theta Function on G(n,1/2)](https://focs.computer.org/2026/accepted-papers/) — 会议官方录用目录；已打开。核实FOCS2026录用状态，不等同逐行独立证明审计。
- [Shanmu Jin, Theorem1, 2026-11-23v1](https://aixiv.online/html/2611.02472v1) — 作者完整证明声明；正文已读。同时声明独立边与循环模型的期望sharp常数1。
- [LovaszTheta.tendsto_normalizedExpectedTheta_both](https://github.com/jinshanmu/LovaszTheta/blob/37019ecfa2c34ce22c8a9fe9f54e97efb01c71df/Lean/LovaszTheta/Limit.lean) — 作者仓库；固定提交代码已取得、未重跑。导出两种期望极限；Lean4.36.0，Mathlib fc4f59e577feb1a4956671bc04ac18aaaf8cd842。

**建议改动：** 仅2026年9月未评审声明 → 增加FOCS官方录用证据与精确Theorem定位；把期望式与高概率式之间的桥接写明。

**实际路径：** `Sharp Lovasz Theta Bounds Random Graphs Potechin Xu`；`G(n,1/2) theta expectation (1+o(1)) sqrt n 2609.30064`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** aiXiv/Lean独立证明路线需另行依赖/模型审计及可信内核重跑；原主定理不因另一个新声明而失去已核出版信息。

**本轮推论说明：** 本轮期望转移：令W对称、上三角非对角元独立公平±1，W_ij=+1对应边、−1对应非边，W_ii=0。I−W为θ的谱对偶可行矩阵，故0≤θ≤1+||W||。对单位x，xᵀWx=2Σ_(i<j)x_i x_j ε_ij，系数平方和≤2；1/4-net大小≤9^n，结合Hoeffding并积分尾部得E||W||²=O(n)。于是θ/√n在L²有界、从而一致可积；结合论文依概率趋1得到Eθ/√n→1。仅桥接步骤为本轮推论，未独立重证论文主定理。

### QX-P-001836｜R³ 单位距离图的 3-染色（无三色单位菱形）

**旧卡 → 本轮变化：** 旧标签 `open`。Pak原题要求R³的3着色没有彩虹单位等边三角形，同时指定超越对角线的单位菱形四色点呈1,1,2,3。它不要求单位距离边端点异色；现标题“无三色单位菱形”与原题相反。

**按子问判断：** 指定菱形颜色且无彩虹单位等边三角形的存在性：暂未找到可验证结果；原帖2020更新仍区分动机问题与本题；本轮未查得原题完整解答。；标题及proper coloring解释：题面有误；不是χ(R³)≤3；菱形本身允许并要求出现三色。

**直接证据与定位：**

- [原帖条件(1)(2)与2020-08-08更新](https://mathoverflow.net/questions/202861/3-colorings-of-the-unit-distance-graph-of-bbb-r3) — 原始作者问题；全文已读。和通常单位距离图色数问题不等价。

**建议改动：** 无三色单位菱形、通常图3染色 → 改为无彩虹单位等边三角形并存在指定颜色/对角线菱形的R³着色。

**实际路径：** `Igor Pak 202861 3 colorings unit distance graph R3 rainbow`；`unit rhombus transcendental diagonal colors 1 1 2 3 no rainbow triangle`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 任何局部有限构造须说明可延拓到全R³且满足超越长度条件。

### QX-P-001837｜随机循环图 Lovász 数期望

**旧卡 → 本轮变化：** 旧标签 `claimed`。Chen–Hu–Hu–Wang–Yang arXiv2610.22971v1 Theorem1.1 明确覆盖所有奇数阶（含合数），不能自动外推偶数阶。新发现Jin aiXiv2611.02472v1声称全体n且处理偶数反足距离类，固定提交Lean端点可读；其完整声明待核。

**按子问判断：** 所有奇数阶的Eθ∼√n：完整证明/反例声明待核；2026-10预印本Theorem1.1已对齐，尚未独立证明审计。；全体n含偶数阶：完整证明/反例声明待核；2026-11-23新声明显式含偶数阶；不再只写“覆盖未确认”，但不能据仓库标记认定已验证。

**直接证据与定位：**

- [Theorem1.1、Definition2.1；v1 2026-10-16](https://arxiv.org/html/2610.22971v1) — 预印本完整证明声明；全文定位已读。每个非零取反轨道独立Bernoulli(1/2)，结论只沿奇数n。
- [Theorem1及循环模型定义](https://aixiv.online/html/2611.02472v1) — 作者完整证明声明；正文已读。明确所有正整数阶，包括偶数n的单独反足类；aiXiv页面无复现报告。
- [LovaszTheta.tendsto_normalizedExpectedTheta_both](https://github.com/jinshanmu/LovaszTheta/blob/37019ecfa2c34ce22c8a9fe9f54e97efb01c71df/Lean/LovaszTheta/Limit.lean) — 作者仓库；固定提交代码已取得、未重跑。Lean4.36.0；Mathlib fc4f59e577feb1a4956671bc04ac18aaaf8cd842；导出m+1遍历所有正阶。

**建议改动：** 偶数覆盖未确认、仅传闻AI贡献 → 明确区分10月奇数稿与11月全阶新声明；贡献归属以论文声明为准，目录标签不作证据。

**实际路径：** `Sharp asymptotics Lovasz number random circulant graphs Chen Hu Wang Yang`；`2610.22971 even odd orders Bernoulli distance theta expectation`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 核对Jin底层图模型、有限偶阶例外、全部公理依赖及独立Lean重跑。

### QX-P-001838｜相位恢复 4M−5 注入概率

**旧卡 → 本轮变化：** 旧标签 `claimed`。原Conjecture19是p_M<1与p_M→0；人话版概率为1写反。Li arXiv2606.17922已从v1推进到2026-11-10v2完整声明；FR05固定提交给O(1/M)与趋零Lean端点，并可读到上游CI步骤success。本轮没有重跑。

**按子问判断：** 原题(a)pM<1及(b)pM→0：完整证明/反例声明待核；v2完整声明；旧v1仅(a)不可代替最新范围。M≥2，原始复高斯/Haar子空间、对所有信号注入。；人话版pM=1：题面有误；与原猜想方向相反。

**直接证据与定位：**

- [Entry10 Conjecture19(a)(b)](https://arxiv.org/html/2603.29571v1) — 原始问题；全文定位已读。4M−5复测量，概率严格小于1并趋0。
- [v1 2026-06-16；v2 2026-11-10, Resolution of Vinzant's Conjecture on Phase Retrieval Injectivity](https://arxiv.org/abs/2606.17922) — 作者完整证明声明/预印本；版本页摘要已读；v2 PDF/HTML直接入口不可达。最新摘要声称O(M^-1)；不可把旧版摘要当最新结论。
- [NLA.FR05.phaseRetrieval_injective_probability_le_inv；phaseRetrieval_injective_probability_tendsto_zero](https://github.com/ajt60gaibb/OpenProblemsInNLA/blob/bca7904b8d6f43b7258bc0eaed636a2b6b4a8792/frames-and-matrix-designs/FR-05/lean/Solution.lean) — 作者仓库；固定提交代码已取得、未重跑。README列Lean4.33.1，Mathlib0df444a360ea，LeanCert621a43d7cf21；公共端点使用原始概率名称，无附带未证假设显列于端点。
- [Fresh sandboxed statement, axiom and kernel verification步骤](https://github.com/ajt60gaibb/OpenProblemsInNLA/actions/runs/38000947893/job/114058782811) — 上游CI记录；通过GitHub专用步骤接口读到success，未取得/复跑完整内核日志。上游运行成功与本轮独立验证必须分开；一次通用endpoint调用被工具拒绝后专用只读步骤接口成功。

**建议改动：** pM=1或仅v1第一问 → 恢复pM<1与趋0；增加v2日期、固定提交与上游CI层级。

**实际路径：** `Resolution Vinzant conjecture phase retrieval injectivity Zhangsong Li`；`4M-5 injectivity probability p_M C/M phase retrieval 2606.17922`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 深查v2完整证明、import NLA.FR05.Proof的信赖链及完整CI日志；本轮不作独立通过声明。

### QX-P-001839｜相位恢复稳定性 β^M 界

**旧卡 → 本轮变化：** 旧标签 `partially_solved`。原确定性猜想必须含最大行范数归一化、实(2M−1)×M full-spark矩阵与0<β<1。当前删掉尺度因子的表述可被缩放直接破坏，且ω是衰减、其倒数才反映不稳定。高斯结果现已期刊在线发表，但不证明对一切A的猜想。

**按子问判断：** 原归一化、确定性普适猜想：部分进展；高斯随机子类的指数底数已知；不能推广至每个full-spark矩阵。；删尺度后的题卡公式/增长解释：题面有误；ω(tA)=|t|ω(A)，所以无归一化的一切A上界不可能；这不是反驳正确原题。

**直接证据与定位：**

- [Definition10.1、Conjecture20](https://arxiv.org/html/2603.29571v1) — 原始问题；全文定位已读。ω(A)≤C max_k||A_k|| β^M；M>1；0<β<1；full-spark。
- [2026-10-14在线；Corollary1.2；DOI10.1017/S0004972726101713](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/extreme-least-singular-values-of-gaussian-row-submatrices-and-a-phase-retrieval-stability-problem/4AE5A681CF3F2B36732447F34E2A45C0) — 已刊论文；期刊正文定理定位已读。实标准高斯临界行数给指数底数1/4；论文仍区分原确定性猜想。

**建议改动：** ω≤Cβ^M对任意A，不稳定性最多指数增长 → 恢复尺度和full-spark假设；解释ω指数衰减与逆稳定性关系；更新高斯论文为已刊。

**实际路径：** `Balan Wang phase retrieval stability universal exponential conjecture`；`omega(A) 2M-1 M full spark beta Gaussian subgaussian 2607.06249 2611.06736`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** Wen–Häggblom–Yang 2611.06736本轮全文入口不可达，仅检索摘要显示有界密度亚高斯假设；不得写成所有亚高斯普适全解。

### QX-P-001840｜高斯矩阵 ω(A) 值

**旧卡 → 本轮变化：** 旧标签 `partially_solved`。Shmalo高斯结果已从7月预印本变为2026-10-14期刊First View；Corollary1.2解决指数尺度与最优渐近底数1/4子问。有限维分布/亚指数项不是该结论，题面所说“指数增长”应改衰减。

**按子问判断：** 标准实高斯(2m−1)×m的渐近指数底数：原题已证；ω(A_m)=4^(−m+o_P(m))，概率意义；任何β>1/4给渐近高概率上界，不能推出β=1/4的统一常数C。；有限m精确分布、亚指数精度及精确临界前因子：暂未找到可验证结果；不得把指数尺度结果写成精确随机值公式。

**直接证据与定位：**

- [Theorem1.1、Corollary1.2、式(1.6)；2026-10-14](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/extreme-least-singular-values-of-gaussian-row-submatrices-and-a-phase-retrieval-stability-problem/4AE5A681CF3F2B36732447F34E2A45C0) — 已刊论文；期刊正文已读。全spark临界矩阵的ω等于全部m行方子矩阵最小奇异值的最小值；给概率指数率。

**建议改动：** 仅预印本部分解决、β^M增长 → 更新出版状态；指数底数子问已解，有限维/细尺度另列，衰减方向纠正。

**实际路径：** `Shmalo Gaussian phase retrieval stability constant omega`；`omega Gaussian (2m-1) m 4^{-m+o(m)} smallest singular values`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 不把固定ε偏离概率O(m^-1)误读成随机变量本身误差O(m^-1)。

### QX-P-001842｜Paley 1-定位子图 ϑ

**旧卡 → 本轮变化：** 旧标签 `open`。1-localization是0的邻居诱导子图，取其补图的普通Lovász θ；不是任意局部判据。已读Wang–Shen–Kobzar障碍论文，其固定层块对角SDP下界不否定常数1/√2的θ渐近猜想。

**按子问判断：** θ(补G_p,1)∼√(p/2)：暂未找到可验证结果；数值动机与相关下界不是该渐近等式证明。

**直接证据与定位：**

- [Conjecture26及localization定义](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/) — 作者问题页；正文/检索返回可读。补图与普通theta约定必须保留。
- [Wang–Shen–Kobzar, Theorem3.3；摘要](https://people.math.osu.edu/kobzar.1/papers/paley.pdf) — 研究原稿；已打开并定位相关结论。固定层和固定localization仍为√p阶下界；不确定目标常数。

**建议改动：** 1-定位定义未展开 → 写明邻居0诱导子图与补图；把普通theta和Schrijver强化版本区分。

**实际路径：** `Lovasz theta Paley graph one localizer Magsino Mixon Parshall`；`Paley graph neighborhood theta complement sqrt(p/2) conjecture`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 若声称已解，检查常数而非只检查Θ(√p)，以及p沿素数1 mod4。

### QX-P-001843｜Paley 2-定位子图 ϑ

**旧卡 → 本轮变化：** 旧标签 `open`。旧卡“Kunisky2303.16475不涉及本猜想”不准确：AppendixA直接研究同类2-localization theta，ConjectureA.1给严格优于1/√2的常数，但不指定2/3。它是直接先行猜想，仍非证明。题卡关于theta压低同时给色数上界的解释也错误。

**按子问判断：** 充分大素数的θ(补G_p,2)≤(2/3)√p：暂未找到可验证结果；Kunisky较弱的未知常数改进猜想不能推出指定2/3。；来源关系与色数推断：题面有误；AppendixA确实直接相关；ω≤θ(补G)≤χ并不使θ上界成为χ上界。

**直接证据与定位：**

- [Conjecture27](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/) — 作者问题页；正文/检索返回可读。共邻居0,1诱导子图；p充分大；团数链加2。
- [AppendixA pp37–38(印刷页), eq98, ConjectureA.1](https://arxiv.org/pdf/2303.16475) — 研究原稿；全文对应段已读。作者在独立集/非邻居 convention表述；经Paley自补对齐为同类localization，常数1/√2−ε未固定。

**建议改动：** Kunisky不涉及本猜想；压theta同时压色数 → 补AppendixA直接来源但区别2/3强度；删去错误色数上界推断。

**实际路径：** `Lovasz theta Paley graph two localizer conjecture`；`Paley common neighborhood theta two thirds sqrt p sufficiently large primes`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 初查已核对应：取非平方g，x↦gx将{0,1}共邻居送到{0,g}共非邻居并翻转邻接，故Kunisky子图同构于原子图的补图。未知ε>0未保证达到1/√2−2/3。完整证明仍待后续核验。

### QX-P-001844｜Paley 团数 4 度 SoS 界

**旧卡 → 本轮变化：** 旧标签 `open`。Kunisky–Yu的CCC2023论文确为degree4 SoS的Ω(p^(1/3))下界；它与存在0<ε≤1/6的O(p^(1/2−ε))上界兼容。块对角/Lovász–Schrijver的√p障碍针对较弱松弛，不能挪来反驳完整degree4 SoS猜想。

**按子问判断：** degree4 SoS达O(p^(1/2−ε))：部分进展；Ω(p^(1/3))为已刊障碍；本轮未得所需上界或覆盖全部ε>0的反例。

**直接证据与定位：**

- [Kunisky–Yu, CCC2023 Article30, DOI10.4230/LIPIcs.CCC.2023.30](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CCC.2023.30) — 已刊会议论文；出版页已读。已证degree4下界，数值趋势不等于上界证明。
- [摘要、Theorem3.3](https://people.math.osu.edu/kobzar.1/papers/paley.pdf) — 研究原稿；已读。块对角SDP弱于完整SoS；下界的方向不能跨层级误用。

**建议改动：** 可能将Ω(p^(1/3))视为否定任意破平方根上界 → 明确仅排除ε>1/6；保留尚可兼容区间。

**实际路径：** `degree four sum of squares Paley graph clique Kunisky Yu`；`Paley SOS4 upper bound p^(1/2-epsilon) lower bound p^(1/3)`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 任何新下界须说明松弛层级、变量编码及是否真的覆盖fullSoS4。

### QX-P-001846｜KLS 猜想

**旧卡 → 本轮变化：** 旧标签 `solved`。Bizeul–Klartag–Lehec与Song–Zhang的2026年10月原稿确有维数无关KLS完整声明；前者明示依赖后者关键criterion，不能叫两份独立证明。另取得KLS500固定提交导出源码。DeepMind formal-conjectures的相关PR是题面条目，不能当证明。

**按子问判断：** 维数无关KLS猜想：完整证明/反例声明待核；原稿主定理范围已对齐；本轮未逐行审计两稿全部论证，未确认正式期刊评审。；KLS500形式化：完整证明/反例声明待核；代码已取得但不等于本轮可信内核验证。

**直接证据与定位：**

- [Bizeul–Klartag–Lehec, Theorem1.1及摘要，2026-10-04](https://arxiv.org/html/2610.05474v1) — 预印本完整证明声明；全文主定理已读。各向同性对数凹概率测度的维数无关Poincare界；明示Song–Zhang关键criterion。
- [Song–Zhang v1 2026-10-01；v2 2026-10-04](https://arxiv.org/html/2610.01447v2) — 预印本完整证明声明；版本页及主定理已读。v1迭代对数界与v2 O(1)必须区分。
- [KLS500.poincare500、openaiKLS、universalPoincareRange](https://github.com/hongruzhao/KLS500/blob/c1a50992a81456849996deef2971d4a0b3190bdd/KLS500.lean) — 作者仓库；固定提交源码已取得、未重跑。端点上界500；读取README与源码。README的1710模块、标准公理/内核报告属于作者报告；Comparator/Nanoda不能伪记已跑。
- [关联PR7712, FormalConjectures/Arxiv/2610.05474/KLS.lean](https://github.com/google-deepmind/formal-conjectures/issues/7711) — 题面登记仓库；页面已读。题面占位/五个sanity checks，非KLS全证明。

**建议改动：** 已有两份相互独立证明、Lean目录可当已解决确认 → 保留完整证明声明，删独立性夸大；按论文、作者代码、题面仓库、独立运行分层。

**实际路径：** `Kannan Lovasz Simonovits conjecture proof 2026 Bizeul Klartag Lehec`；`isotropic log concave universal Poincare constant KLS Song Zhang revision 2`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 独立专家审查Song–Zhang criterion及两稿依赖；KLS500准确admissibleMeasure定义/导入闭包/工具链待完整核对和重跑。

### QX-P-001848｜图矩阵范数精确界

**旧卡 → 本轮变化：** 旧标签 `open`。新增DiarHaidary作者仓库完整分类声明，固定提交导出任意有限simple shape的公平符号、injective graph matrix期望范数n^f(log n)^g及g为非负半整数。代码端点已取得，但本轮未运行也未审完定义/依赖；旧卡“无完整代码声明”需更新。题面不是一般邻接矩阵α参数。

**按子问判断：** Conjecture31固定shape图矩阵精确幂/对数阶：完整证明/反例声明待核；作者代码声称无附加估计假设；须对齐独立公平符号法则、注入标号求和、边界/孤立点。

**直接证据与定位：**

- [Definition14.2与Conjecture31](https://arxiv.org/html/2603.29571v1) — 原始问题；全文定位已读。图shape决定矩阵；独立全局边符号与注入标号构造，不是普通随机邻接矩阵。
- [GraphMatrices.Classification.full_dense_sign_classification；expected_dense_sign_classification；classification_logarithmic_exponent](https://github.com/DiarHaidary/Sharp-Bounds-for-Graph-Matrices/blob/01994362f8543743d556e7544d2538e93c62c02b/GraphMatrices/FullClassification.lean) — 作者仓库完整证明声明；固定提交代码与README已读、未重跑。README给f=(h+i0−s)/2、g=b*/2；Lean4.33.0/Mathlib v4.33.0。先前Comparator数值编码修复与本地成功日志并不自动等于完整独立Linux验证。

**建议改动：** 图矩阵泛化为邻接矩阵，缺完整声明线索 → 补shape/注入标号定义；新增固定提交全分类声明及尚未审计边界。

**实际路径：** `sharp graph matrix norms Bandeira Lucca Nizic Nikolac van Handel`；`graph matrices shape alpha Theta n^f log n^g 2412.18468`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 读Shape、normMoment、rate与全部导入信赖链；核对空边界/边界相交、孤立点、p=1覆盖；不要把Challenge.lean目标占位误当证明模块缺口。

### QX-P-001849｜4 度 SoS 能否证"C⁶ 无 7 组 MUB"（OP23 两编码下否定=Sarkar 2026）

**旧卡 → 本轮变化：** 旧标签 `claimed`。Sarkar2606.13903对OP23两个向量坐标编码给否定完整声明，本轮检索摘要与旧卡方向一致，但PDF/HTML入口均不可达，不能把旧卡“全文已读”算作本次已读。任意编码、projector编码及MUB(6)实际个数仍是不同问题。

**按子问判断：** OP23明示两种向量坐标编码的degree4 SoS反驳存在性：完整证明/反例声明待核；摘要声称任意d,m的Haar伪期望可行，从而该两编码回答否；本轮未获得全文逐项复核。；允许任意编码或实际MUB(6)<7：未作判断；Sarkar摘要不提供该更广结论；m≤d+1在d6,m7处取等，不能排除7。

**直接证据与定位：**

- [Open Problem23、Definition11.1](https://arxiv.org/html/2603.29571v1) — 原始问题；全文定位已读。必须指定变量编码和degree计数。
- [Shreyhaan Sarkar v1 2026-06-11 摘要；旧卡列Theorems5.1/7.1及Cor9.1/9.2](https://arxiv.org/abs/2606.13903) — 预印本完整否定声明；本轮仅学术检索摘要；abs/PDF/HTML直接访问失败。支持两vector-coordinate编码的不可反驳声明；上述正文定理号来自旧卡，尚未本轮重新定位。

**建议改动：** 旧卡全文已读易被继承为本轮核验 → 明确本轮只摘要、全文不可达；不据此降为无命中，也不升级为独立核验完成。

**实际路径：** `Degree Four Vector Coordinate SoS Cannot Detect MUB Upper Bound Sarkar`；`2606.13903 MUB degree 4 Haar pseudoexpectation Hermitian LMI projector`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 取得作者PDF后核实localizing约束、复向量实变量化与各定理号；AI是否参与不能由未披露推定为无。

### QX-P-001850｜Ryser–Brualdi–Stein 拉丁方横贯猜想

**旧卡 → 本轮变化：** 旧标签 `partially_solved`。综合原题包含全n的n−1部分横贯及奇n的n全横贯两个子问。Montgomery证明充分大n的n−1部分横贯，不证明全部奇n全横贯。指定000055、000291分别与两个子问重叠，应建父题/子题关系而非整卡合并。

**按子问判断：** 充分大n的n−1部分横贯：原题已证；Montgomery主定理，所有充分大阶数；标题large even不限制其n−1结论仅偶数。；全n的n−1部分横贯；全奇n的n全横贯：部分进展；后者强于相同奇阶的n−1子问，两个整体量词不能简单互相等同。

**直接证据与定位：**

- [A proof of the Ryser–Brualdi–Stein conjecture for large even n, 摘要/主定理，2023-10-29](https://rhmontgomery.warwick.ac.uk/papers/30OnRBSconj.pdf) — 研究原稿；全文主定理已读。充分大n有n−1单元；非全奇阶n单元结论。
- [Conjecture1.2、Theorem1.3](https://arxiv.org/html/2412.01121v2) — 2026修订综述；全文定位已读。明确拆分两支，并保持充分大限定。

**建议改动：** n−1要求比奇阶全横贯更强；可能把大阶结果当全解 → 拆两支及阈值；指定对000055/000291记子问重叠；参考000055内大奇阶全横贯的笼统历史说法不可回灌。

**实际路径：** `Ryser Brualdi Stein Latin transversals Montgomery conjecture`；`Latin squares partial transversal n-1 sufficiently large n odd full transversal 2026`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 若主张剩余有限范围已验全，必须给有效阈值与全覆盖证书；本轮未进行拉丁方枚举。

### QX-P-001851｜横贯拷贝元问题

**旧卡 → 本轮变化：** 旧标签 `open`。原Definition1.1/Problem1.4中的图系统共享顶点集，每条H边配不同来源图；题卡写成顶点分部、每部取一点是另一类横贯。该条是研究元问题，不能用一篇特例论文整体标已证。

**按子问判断：** 统一哪些图系统性质保证H横贯拷贝的元问题：未作判断；先明确H、图/有向图/超图、性质族再形成可判真的子命题。；现人话版横贯定义：题面有误；边的来源标号与顶点分部混淆。

**直接证据与定位：**

- [Definition1.1、Problem1.4、Problem3.4](https://arxiv.org/html/2412.01121v2) — 原始综述问题；全文定位已读。图可重复，来源颜色配在边上；指定颜色普适性比存在一个边色分配更强。

**建议改动：** 顶点分部选择各一个顶点 → 改共享顶点集和边到来源图的双射；与1855的指定边着色普适性建强化关系。

**实际路径：** `transversal graph systems meta problem Joos Kim survey`；`2412.01121 Problem 1.4 graph collection same vertex set rainbow H copy`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 元问题拆可操作子问后再判断状态；本轮不新增任务卡。

### QX-P-001852｜r≥4 k-rainbow 极值数

**旧卡 → 本轮变化：** 旧标签 `open`。必须恢复ex*_{binom(r,2)}(n,K_r)：r为团顶点数，k=binom(r,2)为来源图数，目标最大化各图边数的最小值。现人话版把r当颜色数、k-rainbow当只见k种颜色，与原问题不符。

**按子问判断：** r≥4的min-edge型rainbow极值数：暂未找到可验证结果；完整彩虹Kr；不能用sum-edge型KSSV完全图结果替代。；现变量/极值目标解释：题面有误；min_i e(G_i)不是总边数；完整rainbow不是放宽的k色出现条件。

**直接证据与定位：**

- [§2定义、Problem2.3；与§2 ex_k定义对照](https://arxiv.org/html/2412.01121v2) — 原始综述问题；全文定位已读。两种不同extremal函数的星号和优化目标不可省略。

**建议改动：** r颜色、k彩虹放宽版、一般最大边数 → 完整写ex*、r团阶、k=边数、max min_i e(G_i)。

**实际路径：** `multicolor Turan k rainbow extremal r >=4 cliques graph systems`；`2412.01121 Problem 2.3 k binomial r 2 rainbow extremal density`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 追踪新论文先检查min-edge与sum-edge函数；原综述r3公式的排版floor位置也不宜照抄成零。

### QX-P-001853｜KSSV 色临界极图系统猜想

**旧卡 → 本轮变化：** 旧标签 `partially_solved`。原KSSV猜想问总边数极值图系统的两种结构，不是彩虹数与普通Turán数同阶。r-color-critical是存在一条删去降色数的边，不要求每条边都如此。已知若干r/大k子范围仍不能替代全猜想。

**按子问判断：** KSSV一般色临界图系统结构猜想：部分进展；完全图/r3、4-critical及部分一般范围在综述列出；本轮未得到全参数证明。；色临界定义与结论：题面有误；存在critical edge；目标为max{(h−1)C(n,2),k t_(r−1)(n)}和两种极值结构。

**直接证据与定位：**

- [Conjecture2.5、紧后部分进展及色临界定义](https://arxiv.org/html/2412.01121v2) — 原始综述；全文定位已读。n充分大、k≥h、r≥3，H有h条边；总边数型。

**建议改动：** 每条边皆临界、彩虹/普通极值同阶 → 恢复存在临界边、充分大n与两极值构造的精确结构命题。

**实际路径：** `KSSV color critical rainbow Turan extremal graph systems`；`Keevash Saks Sudakov Verstraete conjecture colour critical multigraph 2204.02575`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 若需升级部分结果，分别取得CKLLS2204.02575、Li–Ma–Zheng2407.14905全文核参数；本轮已检索但不冒称独立重核所有定理。

### QX-P-001854｜Dirac 系统 Hamilton 幂横贯阈值

**旧卡 → 本轮变化：** 旧标签 `open`。原图系统共享n个顶点，横贯约束在边上。令k=r−1，目标是kn个图各最低度≥kn/(k+1)保证C_n^k横贯拷贝；渐近多一个εn的已知结果和任意预指定边着色的universality均不等于此精确阈值。

**按子问判断：** Hamilton幂横贯精确最低度阈值：部分进展；已知渐近版；k=1经典横贯Hamilton情形与k≥2应分开。；现图系统/横贯定义：题面有误；不是顶点分部模型。

**直接证据与定位：**

- [§3 Problem3.3及前述渐近定理](https://arxiv.org/html/2412.01121v2) — 原始综述问题；全文定位已读。G1..G_(r−1)n同顶点集；δ≥(1−1/r)n；GHMPS渐近阈值另列。

**建议改动：** 顶点来自不同部分、未明确图数和阈值 → 补同顶点集、kn图、边来源双射和k/(k+1)n精确最低度。

**实际路径：** `Hamilton cycle powers transversals graph systems exact threshold`；`minimum degree rn/(r+1) rainbow Hamilton power graph collection Gupta Hamann Mogge Parczyk Sgueglia`。原源定位、GitHub/Lean、公开AI/社区入口及失败情况完整保留在该题queries与审计日志。

**待复核：** 不要将2510.18163指定着色普适性结果或不同阈值误入本题；深查需核整数取整和充分大n约定。

## 查重汇总

38个指定对子均已读双方题卡正文并给出关系，详见审计/QX-NEW-04_指定38对复核.jsonl。查重参考卡不作为新增任务；未作线上合并。

- **1751 / 1762：同题。** 同一个MO452847问题，闭三角面及允许相似变换的范围一致。
- **1850 / 000055 / 000291：综合题与子问。** 分别对应全n部分横贯和奇n全横贯，不把整个综合题并入任一子卡。
- **1835 / 1837：同源不同问。** 独立边概率模型与循环距离类概率模型不同。
- **1832的四个Fibonacci候选：非同题。** 几何切线词与算术同余、平方和、素性、实数展开周期性没有命题等价。
- **1714与Cohen编号子题：待定候选。** 本包只有该总题简索引，未凭标题认定包涵或重复。

## 复核顺序与访问限制

1. 先修量词、对象、尺度、编码及方向写反，再调整数学状态。重点包括1761、1772、1783、1791、1804、1814、1826、1829、1834、1838–1840、1851–1854。
2. 对1751/1762、1778、1792、1798、1837、1838、1846、1848、1849等完整声明追踪原稿版本与定理对应。作者仓库已给出的commit、路径和依赖保留于逐题证据；尚未取得的依赖不补造。
3. 独立复核形式化时再审import闭包、定义、额外公理、占位与可信内核。此次没有独立Lean运行，也没有执行下载的外部代码。
4. MSE、arXiv、OEIS或期刊入口失败均按题记录；只取得摘要的来源不写成已读全文。某个URL失败也不等于该成果不存在。
5. 自写有限算术核验与他人计算范围分开。附件中的Cohen66脚本可直接复算；GPU、Java、Walnut等作者程序本轮未运行。
6. 实际搜索覆盖以日志为准。两套搜索引擎、域名限定结果及可见社区页面都不是全部数据库/折叠评论/付费全文的穷尽检索。空结果只支持已列范围内未取得可验证结果。

## 文件和字段说明

- QX-NEW-04_逐题回传.jsonl：100行，按原任务名录排序。math_results.status统一为包内规定的中文状态；其他原证据字段保留。
- 审计/QX-NEW-04_实际检索日志.jsonl：实际请求、日期、入口、来源链接与错误记录。批量工具返回的来源集不虚构为某条查询独占的命中。
- 审计/QX-NEW-04_指定38对复核.jsonl：双方id/card_rev、关系与理由。
- 附件：自写有限算术核验脚本及输出。审计/完整性校验.json包含数量、身份字段与配对覆盖校验。
- 原网页长段正文不随包转载；所有影响判断的来源均给直接URL和可定位的章节、定理、页码或提交。
