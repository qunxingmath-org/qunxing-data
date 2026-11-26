# QX-NEW-08｜突破点、检索路径与复核清单

**核查截止：2026-11-26（Asia/Shanghai）。任务：附件《任务.jsonl》指定的100题。**

本轮完成逐题联网初查、题面与出处对应、代码及公开AI/社区路线、2469条随包全库索引搜索，以及74个指定配对的双方正文复核。未修改线上题库、未合并题卡、未发帖或对外发送消息。参考题卡只用于比较，不另增任务行。

这是初查回传。完整证明声明、已刊定理、作者仓库、社区声明、搜索摘要和直接算术反例分别标明。没有运行外部代码或证明助手；作者自述、旧卡PASS、README中的核验报告均不当作本会话独立重跑。

## 1. 交付与数量核验

| 检查项 | 结果 |
|---|---:|
| 指定任务 / 逐题回传 / 唯一题号 | 100 / 100 / 100 |
| 原样保留批号、题号、card_rev | 100题全部通过 |
| 每题至少两组实际学术查询 | 100题全部通过 |
| 逐题归属检索、访问及本地核对记录 | 926条 |
| 证据条目 | 253条 |
| 指定配对 / 已复核 | 74 / 74 |
| 新增查重候选 | 7对 |
| 线上写入 / 外部代码执行 / 独立Lean重跑 | 0 / 0 / 0 |

记录数包含批量返回被分别归属到各题的查询、来源打开、代码读取及本地索引核对，**不等于独立网络请求次数**。数学判定以子问为单位：同一题可同时有“题面有误”“部分进展”和“完整声明待核”，不能相加成已解决题数。10张卡含“原题已证”子项、7张含“原题已反驳”子项，也包括特例、边界和稿内引理，**不表示新解决了17道主问题**。

必需交付为 `QX-NEW-08_逐题回传.jsonl` 与本文。压缩包另含总检索记录、查重复核表、校验摘要和SHA-256清单。逐题JSONL保持模板全部字段，并统一补充 `math_results[].subproblem/status/conclusion/evidence_ids`、`evidence[].evidence_id`、`formalization` 和 `duplicates[].relation`，原有更细字段保留。

## 2. 优先处理的结论

| 优先级 | 题号 | 应处理的变化 | 核验边界 |
|---|---|---|---|
| P0 | 2192、2210、2260 | 找到对应的历史原始证明或已刊定理，修正旧卡的开放/证据断裂记录 | 分离公理、Baire有效性、k≥2及严格最小度条件必须保留 |
| P0 | 2230 | 撤回“P33不存在、实为P27”的无版本勘误 | v1 P27与v2 P33同题；v2 P27另问Hamiltonian约化 |
| P0 | 2287 | Wang v9 Lemma2.5有明确n=4反例 | 否定稿内引理及该证明链；没有反驳Cramér主猜想 |
| P0 | 2269、2274、2288、2289 | 补入精确覆盖目标的新完整证明/算法声明 | 仍待独立纸审或代码验收；全文未取的来源另标 |
| P0 | 2219、2229、2231–2234、2261、2270 | 修复对象定义、量词、例外与分离性错误 | 以当前card_rev逐条建议，不在本轮改线上 |
| P0 | 2286 | 区分允许反射的E(2)和只保向的SE(2)覆盖 | Keller下界可传，上界须另核，不直接照搬 |
| P1 | 2187、2207、2213及2223–2228等 | 完整声明和局部/一般范围应分列 | general≠every；machine-verified可能只是AI审阅 |
| P1 | 2280 | 新子类/三次界进展不能被AI平台升级成一般Černý已解决 | 已追到原稿和固定仓库，仍未独立重跑 |

下文只保留影响题面、状态、来源、形式化范围或查重的新信息；未命中题的逐题记录保留在JSONL，不在此逐一复述。报告内的L1/G2等名称以及 `chunk_3_search_*.json` 是工作批次标识，实际检索词、链接和访问结论已汇入总检索记录；不附整段网页抓取内容。

## 3. 逻辑、描述集合论与拓扑

核查日期：2026-11-26。范围：QX-P-002187—QX-P-002211，共25题。保持题号、card_rev、batch_id原值，仅回传建议，不改线上。

本组完成了25题的原题对应、每题两套学术检索词、每题GitHub网页检索及Formal Conjectures / Mathlib4 / openai/math三仓代码索引查询、公开AI/社区组合索引、2469条全库索引查重。指定8对均读了两张现版题卡正文并对照原出处；另有2个新候选因缺另一题正文而保留“待定”。逐题文件含215条归属检索记录、60项证据；独立日志记录52批网页请求、31次GitHub请求（含限流与重试）。

### 1. 可改变状态的发现

#### QX-P-002192：Γ-space存在性取得1976原始证明

**旧卡 → 变化。** 旧卡因Math.SE / MathOverflow的答案删除而记为低置信“完整声明、证据链断裂”。本次通过MO原帖链接取得CWI保存的A. E. Brouwer原始报告，补上了这条证据链。存在性及T₁、Hausdorff、regular T₁三档可记“原题已证”。

**来源与范围。** [Brouwer, A connected metric space without nontrivial open connected subspaces](https://ir.cwi.nl/pub/6862/6862D.pdf)，ZW83/76，1976-08，§2(i)–(vii)，尤其印刷p.4的(vii)。报告构造非可分、弧连通的度量空间，而其非空真开子集均不连通。度量性覆盖原帖所问三档分离条件；非可分性必须保留，不能改称Polish例。末段另给可数Hausdorff变体，但本次没有把旧卡所有旁支性质一并升级。

**实际路径。** 两套检索词为 `"connected" "open connected subsets" "Brouwer"` 与 `"5121714" "507958" Gamma space`；打开[MO 507958](https://mathoverflow.net/questions/507958/connected-spaces-with-no-nontrivial-open-connected-subsets)，再循链接打开CWI PDF并阅读构造与(vii)。GitHub和公开AI组合查询未提供必要的新证明；证明依据是机构保存的原稿。

**待复核。** QX-P-002181（886a9866f063943e）与本卡标题完全吻合且索引标solved，但未取得其正文，不能据此直接合并。详见第5节。

#### QX-P-002210：Π⁰₁ MED在Baire空间中已由2018已刊结果解决

**旧卡 → 变化。** 旧卡将arXiv:1704.04751当作空间范围未核的线索，状态unknown。本次核清定义、定理及参数代入，建议改为“原题已证”。

**来源与对应。** [Schrittesser, Compactness of maximal eventually different families](https://arxiv.org/html/1704.04751v2)，Definition1.1及Theorem1.2；[期刊DOI](https://doi.org/10.1112/blms.12139)，BLMS50(2018),340–348。取可计算常值函数F(n)=∞，则定理中的N_F就是ω^ω，而Π⁰₁(F)就是无额外oracle的Π⁰₁。所得perfect MED满足原题的有效闭、最终不同及极大性。导言也直接说明包含Baire空间，旧“空间差异”疑点可以删除。

**实际路径。** 查询 `"Pi" "maximal eventually different family" Schrittesser` 与 `"effectively closed" "Baire space" "maximal eventually different"`，打开arXiv abs核v2/已刊元数据，打开HTML核定理。期刊检索摘要可见，直接打开期刊页403，因此没有冒称取得期刊全文。

**题面附修。** Π⁰₁不是“逐个枚举族里的函数”，而是补集可有效枚举为基本开集之并。工作坊Theorem46后括注“Gao asked”不能自动当作2025仍开放的证据。没有运行证明助手，也没有把“有效闭”误作“有效紧”。

#### QX-P-002187：2026-09泛解析完整声明覆盖旧卡未决部分

**旧卡 → 变化。** 旧备注称Gao–Nies–Paolini只解procountable子问、一般主问仍开放，逻辑上混合了两层任务：原Problem22先问能否找到一个Borel类，其拓扑同构不归约到图同构；随后问是否泛解析。一个满足要求的procountable子类已经回答前一存在性问题。题面也不是“归约能否绕开图同构”。

**本次证据。** [Gao–Nies–Paolini v4](https://arxiv.org/html/2512.12256v4)的ℓ∞下界支持非可数结构可分类性。新稿[Dai等, Topological isomorphism of procountable groups is universal analytic](https://arxiv.org/html/2609.20890v1)，Proposition1.1、Theorems1.2–1.3，声称procountable及全部非阿基米德Polish群拓扑同构均泛解析，还给固定计数群逆极限的强化。已核arXiv abs显示v1、2026-09-17。

**状态与界限。** 新稿是“完整证明声明待核”。本次核对参数化、定理与原题范围及证明结构末端，没有独立验算完整归约。§6不覆盖交换、幂零或固定指数等进一步限制。稿件披露使用Agent TARS与GPT-6 Astra；作者自述核验不等于本次形式化验证。

**实际路径。** 两组学术词 `"closed subgroups" "procountable" isomorphism Gao Nies Paolini 2026`、`"ell_infty" "procountable groups" Borel reducible analytic complete`，随后以新稿精确题名用第二检索系统复核并打开原稿。公开AI/社区组合查询命中[Zenodo 22705278](https://zenodo.org/records/22705278)，搜索页提示有更新，直接打开429。最新Zenodo内容未取得，保留版本复核任务。

#### QX-P-002207：Wróbel v2完整声明对应正确，但不继承旧纸审PASS

**题面必须重写。** 原Problem45中的β是F₂的另一个自由保概率作用，不是有限集合序列，也不是遍历平均定理。原题希望指定非平凡元、进而全部非平凡元在保持轨道关系时遍历。

**本次对应。** [Wróbel原稿镜像PDF](https://borowiecki.dev/pdf/2608.20165)，页脚核为2608.20165v2、2026-11-12。Theorem1.1在同一概率空间给出Rβ=Rα、β自由且totally weak mixing；Fn无挠，因而每个非平凡元弱混合，强于两个原子问。作者[当前研究页](https://sites.google.com/view/konrad-wrobel/home)仍列preprint。Question1.2的整体mixing是额外问题，不能随之升级。

**实际路径。** 精确题名及“free group / every nontrivial element / ergodic / Miller Tserunyan”两组查询；官方abs/html/pdf多次DisabledError，转到公开原稿镜像成功。已读主定理、Lemma2.2与§3证明骨架，未重新验算Lemma3.2的全部稠密性论证。旧卡2026-11-21的PASS保留为历史线索，本次结论是“完整证明声明待核”，不写“独立通过”。

### 2. 2026拓扑范畴性稿：三题必须分开

共同来源是[Topological categoricity of effective Polish spaces](https://heertern.wordpress.com/wp-content/uploads/2026/10/topological_categoricity-1.pdf)，35页、日期2026-10-03，从Koh作者发表目录当前链接取得。先前直接URL获取失败，本次沿作者页链接成功，因此旧卡的“全文未取得”已消除。使用两组“题名/作者”和“空间/性质”检索词，并读取定义、相关命题和未决问题。

| 本卡 | 原问题与关键变化 | 精确定位与本次结论 |
|---|---|---|
| QX-P-002193 | 0是可计算图灵度，绝非ℵ₀。问存在无限拓扑可计算范畴Polish空间。 | Definition1.3、Question1.4、Theorem1.5，pp.3–5。无限可数、Baire、computably compact及若干连通球呈现类被排除，一般存在性仍列为问题。 |
| QX-P-002194 | 原Problem28先问“是否存在最小度”，不能预设后只求数值。 | Thm4.8：非0′-范畴；Cor4.13：有效零维呈现间0″上界；Cor4.18，p.25：在有效零维呈现限制下无范畴度。紧接的Question4.19仍问一般Baire版本。不能拿受限否定结论宣布原题已反驳。 |
| QX-P-002195 | 原Problem29写every/any，应拆存在性与全称性。 | Proposition3.1，p.7：无限可数离散空间的范畴度为0′，覆盖“有某个c.e.度”的子问；此项记预印本完整声明待核。Question1.8仍保留其他度与d≱0′的无限空间问题，不提供所有不完备c.e.度的实现。 |

后续稿采用双向可计算同胚，应将该定义与工作坊简写的homeomorphism作明确衔接。本次没有把有限空间0度的平凡例与无限空间的存在问题混列。

### 3. 范围受限的后续进展

#### 超有限性问题组：QX-P-002198—002202、002206

[GMRS, Borel dimension growth and hyperfiniteness](https://arxiv.org/html/2608.22565v1)，v1、2026-08-23，Theorem A给点态体积增长≤exp(O(r^γ))的Borel图递增并的超有限性，其中γ≈0.1523是(1−γ)^3−4γ=0的实根。它覆盖Union Problem的受限实例及Weiss问题的局部增长受限群；一般有界度次指数图的另一个结论是Borel Følner tilings，不能擅改为一般超有限性。

[FSV, Hyper-hyperfiniteness and complexity](https://arxiv.org/html/2409.16445v2)已核最新v2为2026-09-21。Theorem0.3的前提是Union Problem反例，即hyper-hyperfinite但非hyperfinite的CBER，结论是**hyperfinite编码集合**Σ¹₂-complete。它不把前提换成hf/hf反例，因而不直接解决QX-P-002200 / Problem39。Theorem0.5还带determinacy和uniform effectivity前提，不能删去。

[Gao–Xiao, An order analysis of hyperfinite Borel equivalence relations](https://arxiv.org/html/2404.17516v3)，Theorem1.1只在self-compatible Z²-ordering条件下得超有限。原工作坊参考DOI写成10.1017/jsl.2024.26，arXiv主记录的相关期刊DOI为[10.1017/jsl.2024.82](https://doi.org/10.1017/jsl.2024.82)，应纠正。

[Open Logic Problems #25](https://www.openlogicproblems.com/problems/25)本次页面仍列一般递增并问题为Open；这是实际状态来源，不是根据搜索空结果猜测。[Bernshteyn–Yu](https://arxiv.org/abs/2302.04727)最新v6、2025-04-07的摘要确认无向多项式增长Borel图已知超有限，但不能替代QX-P-002206中有向出邻域增长假设。

实际检索包含“union problem / increasing union / hyperfinite”、两种hf/hf表述、“Weiss conjecture / amenable Borel actions”、“subexponential growth / exp / 0.1523”、“bounded in-degrees / out-neighborhoods”等逐题两套词，原稿和修订历史分别打开。

#### QX-P-002208—002209：闭I-MED的推广范围已核

官方arXiv入口失败后取得[2610.28275原稿镜像](https://borowiecki.dev/pdf/2610.28275)，PDF页脚v1、2026-10-20。He–Zhou–Zhuang的Corollary C（pp.1–2）覆盖Σ⁰₃理想及weakly Farah理想，不能外推到所有Borel理想，更不能覆盖含Fin的极大理想。原稿§2.1确定I-MED对象是ω^ω里的函数族：两函数的相等坐标集属I，极大性要求每个外来函数与某族员在I⁺上相等。旧卡把它写成MAD式集合族，需要更正。按含Fin的通常约定，极大理想不属于Borel理想类，QX-P-002209不是QX-P-002208的“收窄”。

#### QX-P-002203：Sinha新稿只有固定k的条件性摘要，原竞赛未闭合

[MSE原帖](https://math.stackexchange.com/questions/4423531/do-prime-of-the-form-4k1-ever-lead-the-greatest-prime-factor-race)实际数的是整数m≤n的最大素因子处于1/3 mod4的个数，另问差的增长率，不是“累计两边领先次数”。应排除n≤2的平凡相等。旧帖幂律拟合及数值界仅是作者实验，本次未重跑。

[Sinha2608.06435](https://arxiv.org/abs/2608.06435)的两套学术查询和精确题名再检索取得arXiv索引摘要：固定Ω(n)=k≥2，并假设ζ及L(s,χ₋₄)的RH，声称D_k最终负；摘要明确说不固定k的版本未解。本次abs/html/pdf和镜像均不可达，未取得版本历史/正文，故不记录定理编号或独立证明核验。固定k的最终符号既不能直接求和到无固定k，也不排除早期有限区间反超。

#### QX-P-002211：维数纠错，general完全交不等于every smooth超曲面

[Xu–Zhuang最新v2](https://arxiv.org/html/2601.15576v2)，2026-06-01，Problem6为每个光滑X⊂P^{n+1}、3≤d≤n+1的K-stability。n是X的维数，d=n+1是Fano指数1；旧卡将其误称Calabi–Yau必须修正。综述已知区包括n≤4及n+1−max{1,n^(1/3)}≤d≤n+1；general成员也已知。

[2608.09293官方摘要](https://arxiv.org/abs/2608.09293)与[原稿导言转录预览](https://paperity.org/p/379166234/k-stability-of-complete-intersections)互证：Conjecture1.1仍问every smooth Fano hypersurface；Theorem1.3只证general complete intersections，并明确针对Xu–Zhuang Problem8。预览只到约前2页，不能称取得完整论文。作者目录本次列submitted。对本卡仍应保留低次高维核心，不能从另一题的general结果株连升级。

### 4. 其余会改变题意的错误

共同原出处：[2507.03972v1](https://arxiv.org/html/2507.03972v1)。已核abs只列2025-07-05 v1；2026另一本[2608.26628v2](https://arxiv.org/html/2608.26628v2)是另一届问题集，不应当作其修订版。

| 卡号 | 原定位 | 修订要点 |
|---|---|---|
| 002188 | Problem23 | 第一、第二蕴含逆向是两问；保留Δ⁰₂，使用∅′求可计算索引的定义，删除“反转操作”。LMNS原论文Definition3.3、Thm3.4已核。正式展开第一逆向时仍需澄清oracle/度及退化度约定。 |
| 002189 | Problem24 | 范畴度衡量计算副本间同构所需的最小度；decidable是完整一阶图可计算，不只是基本关系。现场已解标注属于Problem32。 |
| 002190 | Problem25(i)–(iii) | 三项分别为Diag刻画、逆数学强度、Weihrauch度，不能写成三个定义是否相等。旧“Δ⁰₂层已刻画”未取得原定理，本轮不继承。 |
| 002191 | Problem26 | 加回（有效）紧和同胚。Koh–Melnikov–Ng期刊Thm1.1/1.4否定一般局部紧扩大版本，但没有解决原紧空间同胚版本；等距反例不适用。 |
| 002196 | Problem30 | 加回RCA₀+BΣ_n+¬IΣ_n、Π_n集合X、两两不交M-finite块以及f(s)∈A_s∩X。 |
| 002197 | Problem31 | 是Π⁰₁(∅′)树，已有保BΣ₂路径g，要求可定义且保BΣ₂的h；并非一般WKL。 |
| 002198 | Problem35 | 每层F_n是超有限，不是有限；否则一句话只是在重述定义。 |
| 002199 | Problem37 | hf/hf是逐类Z²序型，不是两个任意超有限关系的join。 |
| 002200 | Problem39 | 保留hf/hf反例前提；目标集合是“超有限”编码，旧“不超有限”写反。 |
| 002202 | Problem41 | 原文具体采用统一exp(r^c)，0<c<1；别把所有次指数函数自动视为这一类。 |
| 002204 | Problem42 | 补全Act(F∞,([0,1],λ))、弱拓扑和Lebesgue可测。Baire可测匹配存在性不等于该参数集Σ¹₁完全性。 |
| 002205 | Problem43 | 参数是全部Aut([0,1],λ)，原标题擅加遍历限制；矩阵/算子平方根不适用。 |
| 002206 | Problem44 | 保留有向、统一入度界与出邻域增长，不把它换成无向距离球增长。 |

[Chong–Wong2510.18490v1](https://arxiv.org/html/2510.18490v1)的Corollaries5.1–5.3与§6已读，是COH、RT²₂、TT¹可定义解的相邻进展；没有取得它覆盖Problem30/31的论证。因此不从相关题名推断这两卡已解。

### 5. 指定查重与新候选

以下8组都比对了包内两张正文与原始问题；关系是报告建议，未合并。

| 配对（版本） | 关系 | 判据 |
|---|---|---|
| 002191 7a499705660c3fdc ↔ 002193 72d0fd07ebec3fdc | 同源不同问 | 可计算呈现存在性与呈现间同胚的可计算范畴性。 |
| 002194 dcc8e10033e921f2 ↔ 002195 23467c0bfeb9ec22 | 同源不同问 | 固定Baire空间是否有度，与改变空间实现c.e.度。 |
| 002197 7e91551e232b3069 ↔ 002210 ccefaa8aea595ba5 | 相关但不等价 | 非标准模型的保BΣ₂路径与标准Baire空间Π⁰₁ MED，仅符号共现。 |
| 002198 561b9d02fda87ee9 ↔ 002199 5d933f61a15a8f02 | 同源不同问 | hyper-hyperfinite递增并与hf/hf逐类Z²序型。 |
| 002202 06f91f339300a83a ↔ 002206 54b9b90c58b19fa4 | 相关但不等价 | 对称图距离球增长与有向出邻域增长。 |
| 002204 e7ca672b33bf0be4 ↔ 002205 22bfafeba996de7b | 同源不同问 | 可测匹配参数集与平方根参数集。 |
| 002208 39dcc2b507bb0b96 ↔ 002209 5e14348b976e2457 | 相关但不等价 | Borel理想与含Fin的极大理想，不能视为包含子类。 |
| 002211 db92124e04438811 ↔ 002212 24b7c20ab25cf794 | 同源不同问 | smooth成员稳定性与整个K-moduli及边界描述。 |

新线索均只到索引、已尝试另一卡网页而不可达，故保留待定：

- **002192 c40bc86729042511 ↔ 002181 886a9866f063943e**：同名Γ-space，索引状态claimed/solved冲突值得优先核正文。
- **002203 2db5600b22029e1d ↔ 000906 4b9090e5ac89c5c5**：都关联Sinha最大素因子mod4偏差；000906标题更偏Σχ渐近，而002203还含追平/反超。不能只凭标题定同题。

### 6. 代码、AI结果与访问层级的实际边界

25题均有GitHub网页查询，并实际调用GitHub代码搜索限制于`google-deepmind/formal-conjectures`、`leanprover-community/mathlib4`、`openai/math`。出现429的查询均保留失败记录并重试。返回的代码片段未发现可对应本组原题的证明：常见假匹配是AEC的categoricity、概率矩阵diagonal、算子代数hyperfinite、范畴论topological/categorical、三角台球weak mixing，以及不同最大素因子问题。空结果只描述本次索引查询，不推导形式化不存在。

另外取得`openai/math/overview.tex`全文，固定提交`3344da59991ed94f9ba711217b29c1d760badfa6`，blob `1a56184b1f28a8750722dc2dd6306af8424da0b6`。按本组相关词筛出的条目不覆盖上述问题；目录声明本身也不是独立证明验证。

公开AI/社区路径是实际组合查询Zenodo、MathOverflow、Math.SE、ProofAtlas以及aiXiv / EulerSolve / ProofForum站名；本次没有宣称逐平台内部API或全站穷尽搜索。原稿、摘要、转录预览、404/403/429/DisabledError分别标注。没有运行Lean、下载后执行外部程序、向作者发消息或修改线上题卡。

### 7. 优先复核顺序

1. **2187完整新声明**：泛解析归约的Borel编码和反向恢复，及Zenodo后续版本。
2. **2194范围防误判**：严格区分Cor4.18的有效零维呈现限制与Question4.19的一般版本。
3. **2207完整声明**：独立复核edge sliding与Lemma3.2，不能沿用旧PASS充数。
4. **2203仅摘要线索**：取得Sinha稿当前全文/版本，核固定k条件和可能求和障碍。
5. **2211题面及量词**：保留every smooth，不受general完全交结果株连。
6. **两组新增查重**：取得002181与000906正文，之后才能决定同题/特例关系。

## 4. 代数几何与相邻问题

日期：2026-11-26。范围严格为chunk_2的25题；参考题卡不另立任务。25题均有五路线实际查询和两组学术词。24对指定查重完成双方全文对照；新增1条仅标题候选待定。数学结论是初查分级；未改线上、未发消息、未执行外部代码、未独立重跑形式化。

### 最重要的修复

#### 编号必须随版本：QX-P-002230

现卡将P33判为不存在并改为P27，需要撤回这一无版本勘误。

| 版本 | ODP gap题号 | 该版本P27内容 |
|---|---|---|
| [2601.15576v1](https://arxiv.org/html/2601.15576v1) | Problem 27 | ODP归一化体积间隙 |
| [2601.15576v2](https://arxiv.org/html/2601.15576v2) | Problem 33 | Hamiltonian约化极小化子下降 |

两版原文均已读取。ODP问题必须有singular、n≥2、零边界等条件。OpenAI仓库固定提交3344da59991ed94f9ba711217b29c1d760badfa6的主定理与此范围匹配，但仍只是本次取得的完整证明声明；引言显式依赖四维companion Theorem1.1，尚未审计闭合。

### 逐项有影响发现

#### QX-P-002230 · 归一化体积ODP间隙：v1 P27 / v2 P33

**旧卡 → 本次变化。** 现卡“P33不存在、实为P27”是混用版本：v1 P27与v2 P33同题，v2 P27是Hamiltonian约化。OpenAI固定提交存在全维主定理声明，未审完证明。

**范围/修复。** n≥2、零边界、奇异复代数klt germ；volhat≤2(n−1)^n，等号当且仅当解析普通二重点。 标题改“归一化体积ODP间隙（v1 P27 / v2 P33）”；补singular、复数、klt、n≥2、零边界、等号条件。

**状态建议。** 由open-only改为已有完整证明声明待核；不将GitHub主定理文本或目录自称视作独立确认。

**直接证据。**

- [Open problems in K-stability… v1](https://arxiv.org/html/2601.15576v1) — Problem 27，L404–410。访问层级：原综述v1全文。v1 P27为ODP体积间隙，与v2 P33同题。
- [The ordinary-double-point gap in every dimension](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-ordinary-double-point-gap-in-every-dimension-September-24-2026/build/sections/01-introduction.tex) — commit3344da59991ed94f9ba711217b29c1d760badfa6；build/sections/01-introduction.tex，thm:main。访问层级：固定提交TeX已取；核主定理/引言依赖，未全文审稿或运行。声明所有n≥2零边界奇异complex algebraic klt germ有界及等号ODP；显式依赖dim4 companion Thm1.1。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v1 §3.2 Problem 27；v2 §3.2 Problem 33。

**本次检索路径。**

- Web search system2："ordinary-double-point gap" "openai"（2026-11-26；G2-016）。
- Web search system2："normalized volume" "2(n-1)" conjecture 2026（2026-11-26；G2-016）。
- Web search system2：site:github.com/openai/math "ordinary-double-point" formalization（2026-11-26；G2-036）。
- Web search system2："ordinary-double-point gap" (site:math20.org OR site:mathcommunity.github.io OR site:mathoverflow.net)（2026-11-26；G2-036）。

**待核。** 核dimension-four companion Thm1.1及全维归纳依赖；取得独立专家核验。；固定commit lean/docs/037.md为404；未全面审计repo中全部Lean位置，不能宣称不存在形式化。

#### QX-P-002214 · a^b+b^a 表示唯一性

**旧卡 → 本次变化。** 现卡正整数版本有立即反例{1,7}与{2,2}均给8；原MO问题限制a,b>1，未被反例否定。

**范围/修复。** a≥b>1的无序对；本卡误写a,b为任意正整数。 把正整数改为整数a≥b>1；撤下未经本轮核实的“搜索至10^1000”说法或补范围/程序出处。

**状态建议。** 不得把平凡反例当MO原命题被反驳；原命题当前只核到条件性结果。

**直接证据。**

- [原题及精确设定](https://mathoverflow.net/questions/178555/for-integers-a-ge-b-1-is-fa-b-ab-ba-injective) — MathOverflow #178555提问及Joni Teräväinen回答；卡所引MSE #3286093未可访问。访问层级：原题正文已定位；网页可取得。a≥b>1的无序对；本卡误写a,b为任意正整数。
- [For integers a≥b>1 is a^b+b^a injective?](https://mathoverflow.net/questions/178555/for-integers-a-ge-b-1-is-fa-b-ab-ba-injective) — 提问L33；Teräväinen回答L103–118；数值评论L59。访问层级：原帖及回答全文。原限制>1；abcd只导出有限多。公开评论仅能直接核到2≤a<b≤1000的检查，不支持卡中的10^1000。
- [当前卡量词的算术检查](sandbox:/workspace/scratch/553884477a2a/QX-NEW-08_work/chunk_2_arithmetic_check.json) — (1,7)与(2,2)；2026-11-26。访问层级：本地精确整数计算。两者值均8；不适用于b>1修复后的命题。

原问题定位：[原出处](https://mathoverflow.net/questions/178555/for-integers-a-ge-b-1-is-fa-b-ab-ba-injective)，MathOverflow #178555提问及Joni Teräväinen回答；卡所引MSE #3286093未可访问。

**本次检索路径。**

- Web search system2："a^b+b^a" "unique" Teravainen（2026-11-26；G2-007）。
- Web search system2："3286093" "178555" powers（2026-11-26；G2-007）。
- Web search system2：site:github.com ("Leyland" OR "a^b+b^a") (Lean OR conjecture)（2026-11-26；G2-024）。
- Web search system2：("a^b+b^a" OR "Leyland") ("aiXiv" OR "Zenodo" OR "MathOverflow" OR "ProofForum")（2026-11-26；G2-024）。

**待核。** MSE #3286093入口不可达；核题号/删除/重定向与其和2014 MO的精确关系。；若保留10^1000数值界，需取原始程序与究竟按a,b还是按和取界的说明。

#### QX-P-002213 · Fano 完全交 K-稳定性

**旧卡 → 本次变化。** 原题限定一般完全交；原稿导言转录可核Theorem1.3明确解P8，Conjecture1.2仍为全部光滑完全交。全文不可达，本轮不继承旧卡深审。

**范围/修复。** 一般完全交X⊂P^{n+k}，k+2≤Σd_i≤n+k。 明确general（一般成员），恢复k+2≤Σd_i≤n+k；排除射影空间和光滑二次曲面例外。

**状态建议。** 旧solved只可对应收窄后命题；本轮证据层级写预印本摘要匹配、全文待核，不自动继承历史深审。

**直接证据。**

- [K-stability of complete intersections](https://arxiv.org/abs/2608.09293) — 2026-08-10 arXiv摘要；作者研究目录。访问层级：一手arXiv搜索摘要；abs/html/pdf直接访问DisabledError。一般Fano完全交K多稳定，除P^n和光滑二次曲面外K稳定。作者页面仅列submitted；本次未核全文。
- [K-stability of complete intersections — 原稿导言公开转录](https://paperity.org/p/379166234/k-stability-of-complete-intersections) — L32 Conj1.1；L34 Conj1.2；L36 Thm1.3；L38模空间；L41标truncated。访问层级：原始论文前约2页的第三方转录预览，非全文；与arXiv一手摘要互证。Thm1.3为general完全交并明示解P8；every smooth完全交仍是Conj1.2。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v2 §2.1 Problem 8。

**本次检索路径。**

- Web search system2："2608.09293" "K-stability"（2026-11-26；G2-005）。
- Web search system2："general complete intersections" "K-stable" 2026（2026-11-26；G2-005）。
- Web search system2：site:github.com "K-stability" "complete intersections"（2026-11-26；G2-023）。
- Web search system2：("aiXiv" OR "ProofForum" OR "EulerSolve" OR "MathOverflow") "K-stability" "complete intersections"（2026-11-26；G2-023）。

**待核。** 取得2608.09293完整PDF/最新版，核全文证明与依赖；当前只能直接核到导言Theorem1.3的转录。

#### QX-P-002219 · 正规拓展丛稳定性纯代数证明

**旧卡 → 本次变化。** canonical extension被错误解释成正规丛层层拼接；应修为典范扩张。Wu工作及2026辛退化论文并未无条件提供一般纯代数证明。

**范围/修复。** 由c1(X)确定的0→Ω_X^[1]→E→O_X→0；极化−K_X下斜率半/多稳定的纯代数证明。 标题改“典范扩张层斜率半/多稳定性的纯代数证明”；补准确短正合列及c1(X)扩张类，删除正规方向拼接解释。

**状态建议。** 不升级已证；已知解析稳定性与特殊代数情形分开。

**直接证据。**

- [Stability of the canonical extension of tangent bundles on Picard-rank-1 Fano varieties](https://arxiv.org/abs/2207.04573) — v2 2023-05-01，摘要。访问层级：arXiv摘要及版本史全文。Picard秩1、指数整除dim或dim+1；切丛稳定蕴含扩张(半)稳定。非P13一般解答。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v2 §2.2 Problem 13；前置扩张式。

**本次检索路径。**

- Web search system2："canonical extension" "algebraic proof" "K-semistable"（2026-11-26；G2-009）。
- Web search system2："Wu" "canonical extension" "semistability"（2026-11-26；G2-009）。
- Web search system2：site:github.com "canonical extension" "Fano" stability（2026-11-26；G2-026）。
- Web search system2：("MathOverflow" OR "aiXiv" OR "Zenodo" OR "ProofForum") "canonical extension" "semistability"（2026-11-26；G2-026）。

**待核。** Wu文用切丛扩张，对照原题余切侧的对偶约定；一般纯代数论证仍需复核。

#### QX-P-002229 · 短星积存在性（P31）

**旧卡 → 本次变化。** 现卡将short误写为只留偶数阶/统一有限截断，并误列作者；已读Etingof–Stryker已刊全文明确纠正。一般P31仍未找到全证。

**范围/修复。** 极小化子分次下短星积存在；short指C_k(a,b)=0当k>min(deg a,deg b)。 重写short/even定义并改正合著者；补原题指定(2/r)ord_E分次。

**状态建议。** 只记定义修复与既有构造；全体存在性不升级。

**直接证据。**

- [Short Star-Products for Filtered Quantizations, I](https://sigma-journal.com/2020/014/sigma20-014.pdf) — SIGMA16(2020)014，DOI10.3842/SIGMA.2020.014；PDF pp1–2定义。访问层级：已刊PDF全文；核定义与摘要。Pavel Etingof–Douglas Stryker。短性限制k≤min输入度；even是交换反号关系；一般存在性非该文定理。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v2 §3.1 Problem 31；Etingof–Stryker定义。

**本次检索路径。**

- Web search system2："short star-products" "conical symplectic" 2026（2026-11-26；G2-016）。
- Web search system2："minimizer" "short star" product（2026-11-26；G2-016）。
- Web search system2：site:github.com "short star-products"（2026-11-26；G2-034）。
- Web search system2："short star-products" (site:mathoverflow.net OR site:jihaoliu.org OR site:aixiv.online OR site:zenodo.org)（2026-11-26；G2-034）。

**待核。** 对新稿检索不宜只搜“有限截断”；后续以short star-product及minimizer grading精确匹配。

#### QX-P-002231 · (K_X+Δ)-非负映射体积下界 ε（P35）

**旧卡 → 本次变化。** ε允许依赖固定对(X,Δ)，并非仅依赖维数；研究局部归一化体积，不是映射或除子的全局体积。ACC结果以正下界为条件，不能倒过来证明P35。

**范围/修复。** 固定klt对(X,Δ)，对全部(K_X+Δ)-非负双有理模型及各点的局部归一化体积取统一正下界。 改为ε=ε(X,Δ)>0并写出量词；所有目标点均要求；删除仅依维数的加强。

**状态建议。** 不由ACC或无搜索命中改变原问题状态。

**直接证据。**

- [ACC for local volumes](https://arxiv.org/abs/2408.15090) — v2 2024-08-29；摘要与版本史。访问层级：arXiv摘要全文。Han–Liu–Qi研究局部体积ACC和mld问题；相关命题使用bounded away from zero条件，并非P35一般下界。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v2 §3.2 Problem 35 / Remark 36；v1 P29。

**本次检索路径。**

- Web search system2："normalized volume" "nonnegative birational" "lower bound"（2026-11-26；G2-018）。
- Web search system2："2408.15090" "ACC" volumes（2026-11-26；G2-018）。
- Web search system2：site:github.com "normalized volume" "birational maps"（2026-11-26；G2-036）。
- Web search system2："normalized volume" "non-negative" (site:mathoverflow.net OR site:jihaoliu.org OR site:aixiv.online)（2026-11-26；G2-036）。

**待核。** 非pseudo-effective时原作者也指出可能过强；需专门查反例或新增假设，当前未找到。

#### QX-P-002232 · complement 特殊赋值集结构（P41；双向活跃）

**旧卡 → 本次变化。** 当前卡把special简化为除子并写“有限生成↔special↔极大”，超出论文摘要。Liu实际只在有限生成类中给special iff偏序极大；结构反例不是全部P41被否定。

**范围/修复。** Fano type态射补对的特殊lc places集合LCP^S，含非除子/实值赋值。 改为“对有限生成赋值v，special⇔相应偏序极大”；补LCP为log canonical places及Fano type/complement设定，删除只取整数/除子的泛化。

**状态建议。** 保留部分进展；反例仅否定某有限三角剖分局部闭结构猜想。Liu–Xu2406.00228出版信息按作者页更新已刊。

**直接证据。**

- [Special valuations and automorphisms of affine log Calabi–Yau varieties](https://arxiv.org/abs/2609.22737) — 2026-09-19摘要；作者目录https://faculty.wcas.northwestern.edu/yuchenl/。访问层级：一手arXiv搜索摘要；作者目录已开，原稿不可达。有限生成类special iff偏序极大；special skeleton独立紧化；Markov补例在任何有限三角剖分某simplex上非局部闭。
- [G_m-Equivariant Degenerations of del Pezzo Surfaces](https://arxiv.org/abs/2503.06612) — v1 2025-03-09；摘要。访问层级：arXiv摘要/版本史全文。光滑delPezzo与节点反典则曲线时special valuations连通且局部有限分区间；商奇点仅较弱结论。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v2 §4.2.1 Problem 41。

**本次检索路径。**

- Web search system2："special valuations" "2609.22737"（2026-11-26；G2-018）。
- Web search system2："Liu" "special skeleton" "locally closed"（2026-11-26；G2-018）。
- Web search system2：site:github.com "special valuations" "skeleton"（2026-11-26；G2-035）。
- Web search system2："2609.22737" OR "special valuations" (site:mathoverflow.net OR site:aixiv.online OR site:jihaoliu.org)（2026-11-26；G2-035）。

**待核。** 2609.22737 abs/pdf直接DisabledError；取得全文核反例定理号及与P41全范围对应。

#### QX-P-002233 · LCP 全拟单项赋值猜想（P43）

**旧卡 → 本次变化。** 现人话版反转LCP⊂QM的蕴含；2026-11-05 Zhou valuations v4仅对特殊Zhou类及等价关系给新结构，不能替代全体lct-computing估值。

**范围/修复。** 计算给定m_x-primary分次理想族lct的所有赋值皆准单项；更强要求同一个log smooth model上形成连通凸集的锥。 定义LCP为A_X,Δ(v)/v(a_bullet)=c的赋值集合；纠正包含方向，分别列弱/强版本。

**状态建议。** 保持全体命题待解决；不因“all Zhou valuations”改为“all valuations”。

**直接证据。**

- [Algebraic Zhou valuations](https://arxiv.org/html/2505.19451v4) — v4 2026-11-05；Thm1.4(3)(4)，Cor4.5/4.7及Conj1.1。访问层级：arXiv HTML全文；核主定理。一般非平凡q的JM存在性与Zhou全准单项等价；q=O_X或维≤2的Zhou类全准单项；不覆盖全LCP统一模型。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v2 §4.2.2 Problem 43 (1)(2)。

**本次检索路径。**

- Web search system2："all valuations" "log canonical threshold" "quasi-monomial" 2026（2026-11-26；G2-019）。
- Web search system2："Algebraic Zhou valuations" "2505.19451"（2026-11-26；G2-019）。
- Web search system2：site:github.com "Jonsson" "Mustata" "quasi-monomial"（2026-11-26；G2-035）。
- Web search system2："log canonical places" "quasi-monomial" (site:mathoverflow.net OR site:aixiv.online OR site:jihaoliu.org)（2026-11-26；G2-035）。

**待核。** 最新v4说明修正旧版错误；若历史卡引旧版需替换，并核附加理想q及regular scheme假设。

#### QX-P-002234 · LCP 有限生成赋值存在（P44；最冷）

**旧卡 → 本次变化。** 卡把有限生成解释为赋值是有限多个除子权重线性组合，混淆准单项性；真正有限生成对象是关联分次代数。

**范围/修复。** 在LCP中存在Gr_v R有限生成的赋值；强问存在Kollár赋值。 用Gr_v R有限生成的代数条件替换人话版；另列更强Kollár valuation子问。

**状态建议。** 维持未决证据层级；不得把H-functional或weighted stability threshold特定赋值结果移用到任意LCP。

**直接证据。**

- [Finite generation for valuations computing weighted stability thresholds](https://jihaoliu.org/papers/finite-generation-for-valuations-computing-weighted-stability-thresholds.html) — 作者ai-results第38项，2026-11-01。访问层级：作者页搜索摘要，单篇全文未取得。仅声称log Fano weighted threshold≤1时计算赋值Gr有限生成；没有一般a_bullet的P44量词。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v2 §4.2.2 Problem 44 (1)(2)。

**本次检索路径。**

- Web search system2："LCP" "finitely generated" "valuation" "Problem 44"（2026-11-26；G2-019）。
- Web search system2："graded sequence" "Kollár valuation" "threshold" 2026（2026-11-26；G2-019）。
- Web search system2：site:github.com "LCP" "Kollar valuation"（2026-11-26；G2-037）。
- Web search system2："finite generation" "LCP" (site:mathoverflow.net OR site:jihaoliu.org OR site:aixiv.online)（2026-11-26；G2-037）。

**待核。** Liu作者页2026-11-01 weighted stability thresholds有限生成稿仅相邻范围；待核是否可推本题，当前未建立。

#### QX-P-002238 · Fvol 代数性？

**旧卡 → 本次变化。** 原问是数值代数性，不是有无代数表达式。Liu2026有限次数AI稿实存作者页，但声称P49而非P50，不能据此改本题为解决。

**范围/修复。** 强F正则奇点的数值Fvol是否总为代数数；Fvol=inf_a mult(a)fpt(a)^n。 补“代数数”及强F正则/固定正特征的定义；删除“可写为代数表达式”的替代表述。

**状态建议。** 不以P49声明更改P50；参考卡2235/2237关于Liu稿为幻觉的旧断言应列关联复核。

**直接证据。**

- [The finite degree formula for F-volumes](https://jihaoliu.org/papers/finite-degree-formulas-for-frobenius-volumes-of-pairs.html) — 作者ai-results第9项；2026-10-14初稿，10-26改题32页，SHA25640de41a883cc33ddbf616d2c66aede4b7717552bf3adf9d058cfdb5a2a4a49ac。访问层级：作者页搜索摘要；未取得单篇全文。声称强F正则、codim1 étale有限态射下Fvol及Hilbert–Kunz Fvol乘degree；是P49，不是P50。作者明确非形式化、未经人工验证。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v2 §4.3 Problem 50；v1 P44。

**本次检索路径。**

- Web search system2："Frobenius volume" "algebraic" number（2026-11-26；G2-021）。
- Web search system2："Fvol" "algebraic number" singularity（2026-11-26；G2-021）。
- Web search system2：site:github.com "Frobenius" "normalized volume"（2026-11-26；G2-039）。
- Web search system2："Frobenius" "normalized volume" (site:mathoverflow.net OR site:jihaoliu.org OR site:aixiv.online)（2026-11-26；G2-039）。

**待核。** P50的一般代数性需独立证明；本轮相关F-volume讲座及P49有限次数稿均不构成全证。

#### QX-P-002236 · 容纳所有自由 n-omino 的最小区域

**旧卡 → 本次变化。** 需修复目标函数与猜想n≥9前提；OEIS确实收录a9=26、a10=31及SAT/CP-SAT证明声明，但所索引开源仓库当前404，不能说本次已复现。

**范围/修复。** 原帖以单位格区域的大小计；OEIS规范化为连通容器polyomino的格子数，各free n-omino分别旋转/反射后放入。 目标固定为单位格数，删除“也可直径/外接矩形”；补公式适用n≥9和一次放一种。计算值按OEIS连通polyomino容器定义引用。

**状态建议。** 保留部分解决，计算证明写为收录/作者声明；“代码开源”改为当前可检索线索但入口404。

**直接证据。**

- [原题及精确设定](https://math.stackexchange.com/questions/2831675/smallest-region-that-can-contain-all-free-n-ominoes) — MSE #2831675；OEIS A327094。访问层级：原题正文已定位；网页可取得。原帖以单位格区域的大小计；OEIS规范化为连通容器polyomino的格子数，各free n-omino分别旋转/反射后放入。
- [Smallest region that can contain all free n-ominoes](https://math.stackexchange.com/questions/2831675/smallest-region-that-can-contain-all-free-n-ominoes) — 提问L40–51，评论L68–98。访问层级：原帖全文（q短链成功）。容器格子数；原问heptomino/octomino及OEIS建序。
- [OEIS A327094](https://oeis.org/A327094) — Comments Peter Exley 2026-03-08/23；DATA。访问层级：OEIS搜索索引摘要；页面及internal直接403。序列至a10=31；a9=26 SAT/CaDiCaL，a10=31 CP-SAT/CEGAR声明；一般公式限定n≥9。
- [pexley-math/oeis-A327094](https://github.com/pexley-math/oeis-A327094) — GitHub profile搜索结果；REST repo GET 2026-11-26。访问层级：profile索引命中；仓库网页和GitHub API皆404。只证明有过索引线索；没有取得代码，也没有运行或核验搜索完备性。

原问题定位：[原出处](https://math.stackexchange.com/questions/2831675/smallest-region-that-can-contain-all-free-n-ominoes)，MSE #2831675；OEIS A327094。

**本次检索路径。**

- Web search system2："smallest" "region" "polyomino" "A327094"（2026-11-26；G2-020）。
- Web search system2："A327094" "31" "Exley"（2026-11-26；G2-020）。
- Web search system2：site:github.com "A327094"（2026-11-26；G2-037）。
- Web search system2："A327094" (site:codegolf.stackexchange.com OR site:math.stackexchange.com OR site:mathoverflow.net OR site:zenodo.org)（2026-11-26；G2-037）。

**待核。** 获取a9/a10代码、所有容器的完备搜索论证及UNSAT证书；特别核n9形状限制的无损性。；原帖用任意region措辞，OEIS要求polyomino容器；两种可行域的等价还应明确，不擅自扩大计算证明覆盖。

#### QX-P-002221 · 辛奇点稳定退化的辛性

**旧卡 → 本次变化。** 已直接读取2606.02401v2 PDF，Thm1.1/5.11的非退化反身微分形式特化定理对应原问；现solved可保留为预印本定理层级。

**范围/修复。** 任意辛奇点的稳定退化及给定辛形式仍为辛。 补P20精确命题，给定辛形式也在稳定退化中保持；清理混列13/20/23/25的出处。

**状态建议。** 保留solved，证据具体化为Xu–Zhuang（Guenancia附录）2606.02401v2定理，非独立形式化验证。

**直接证据。**

- [Stable Degeneration, Non-degenerate Forms, and Kaledin's Conjecture](https://arxiv.org/pdf/2606.02401) — v2 2026-06-22；PDF p1 Thm1.1=5.11，p2 Thm1.2/Cor6.3。访问层级：PDF全文已取，核主定理和适用条件。任意klt奇点非退化反身p形式特化保持非退化，闭性保持；因此辛稳定退化结论成立。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v2 §3.1 Problem 20。

**本次检索路径。**

- Web search system2："2606.02401" symplectic（2026-11-26；G2-011）。
- Web search system2："stable degeneration" "symplectic singularities" Kaledin 2026（2026-11-26；G2-011）。
- Web search system2：site:github.com "stable degenerations" "symplectic"（2026-11-26；G2-032）。
- Web search system2："2606.02401" (site:mathoverflow.net OR site:aixiv.online OR site:jihaoliu.org OR site:math20.org)（2026-11-26；G2-032）。

**待核。** 发表状态与后续勘误尚需长期跟踪；初查不重审全部技术证明。

#### QX-P-002223 · 辛奇点=隐藏超凯勒锥

**旧卡 → 本次变化。** 2026-10-26出现Odaka任意辛奇点为hyperKähler锥的arXiv摘要声明；Liu作者页另声称解P25。两者全文不可取，不能沿用纯open也不能升级已证。

**范围/修复。** 辛奇点体积极小化子的Kollár分量、权、接触结构、K多稳定等五问；标题对应更强hyperKähler锥图景。 把五个子问列明，区分已证辛稳定退化、形式圆锥性与hyperKähler/K多稳定结构。

**状态建议。** 建议增加两项完整声明待核，而非把作者AI自审当正式解决。

**直接证据。**

- [Symplectic singularity as hyperKähler cone](https://arxiv.org/abs/2610.35510) — 2026-10-26摘要；v1/42页信息由索引显示。访问层级：一手arXiv搜索摘要；abs/html/pdf DisabledError。声称任意辛奇点均为hyperKähler锥且K多稳定；本轮无法核全文。
- [Minimizers of the normalized volume on symplectic singularities](https://jihaoliu.org/papers/minimizers-of-the-normalized-volume-on-symplectic-singularities.html) — 作者ai-results第11项；2026-10-26，11-10修订166页；SHA256 cebf5e89cae76aad3c191b54df0e64b1aea511d42f6ed40fa6339882d1d67765。访问层级：作者页搜索摘要；永久页403。声称解P25，标未经人工验证；内部AI检查明确不是formal verification。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v2 §3.1 Problem 25 (1)–(5)。

**本次检索路径。**

- Web search system2："2610.35510" hyperkahler（2026-11-26；G2-011）。
- Web search system2："symplectic singularities" "Kollár" minimizer "Liu"（2026-11-26；G2-011）。
- Web search system2：site:github.com "symplectic singularity" "hyperKähler cone"（2026-11-26；G2-032）。
- Web search system2："2610.35510" OR "Symplectic singularity as hyperKähler cone" (site:mathoverflow.net OR site:zenodo.org OR site:jihaoliu.org)（2026-11-26；G2-032）。

**待核。** 取得2610.35510最新版42页全文，核一般奇点度量构造和所有前提。；取得Liu166页2026-11-10修订全文；精核P25五问而非只标题。

#### QX-P-002224 · Hamiltonian 约化极小化子下降

**旧卡 → 本次变化。** Xu–Zhuang的hypertoric特例已核定理；Liu四元数结构稿有一般完整声明但仅作者页索引可读。

**范围/修复。** 极小化子诱导C*作用与Hamiltonian环面交换，Y=μ^-1(0)//T连同下降形式为辛奇点，问C*是否仍极小化。 补与环面交换及下降后确为辛奇点的假设；固定版本v2 P27。

**状态建议。** 保留完整声明待核；disputed应解释为未验收声明，不代表已找到反例或证明错误。

**直接证据。**

- [Stable Degeneration, Non-degenerate Forms, and Kaledin's Conjecture — hypertoric application](https://arxiv.org/pdf/2606.02401) — v2 PDF p2 Thm1.5=7.10。访问层级：PDF主定理已取。hypertoric Y(A,0)的标准膨胀给出归一化体积极小化子，是一般P27的特例。
- [Quaternionic structures on conical symplectic singularities](https://jihaoliu.org/papers/quaternionic-structures-on-conical-symplectic-singularities.html) — 作者ai-results/liuxiv条目，2026-10-26；声称P27,28,29,30(1)(2)。访问层级：作者页搜索摘要；永久页403；对应GitHub路径404。声称极小化分次下四元数结构、权对称、约化性、Chevalley twist及Hamiltonian下降；非形式化核验。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v2 §3.1 Problem 27（不是v1的P27）。

**本次检索路径。**

- Web search system2："Hamiltonian reduction" "minimizer" Liu 2026（2026-11-26；G2-012）。
- Web search system2："normalized volume" "Hamiltonian" "descends"（2026-11-26；G2-012）。
- Web search system2：site:github.com "Hamiltonian reduction" "normalized volume"（2026-11-26；G2-033）。
- Web search system2："Hamiltonian reduction" "minimizer" (site:jihaoliu.org OR site:mathoverflow.net OR site:aixiv.online)（2026-11-26；G2-033）。

**待核。** 取得Quaternionic structures全文及具体定理、依赖；不把AI审阅写成形式化验证。

#### QX-P-002226 · 特征标维数对称 dim R_(d,χ)=dim R_(d,−χ)

**旧卡 → 本次变化。** Liu作者页重新查到权重对称完整声明；并非任意环面分次环都对称，全文仍不可达。

**范围/修复。** 极小化子分次的圆锥辛R，Hamiltonian Poisson自同构的极大环面；dim R_(d,χ)=dim R_(d,−χ)。 补conical symplectic、极小化子诱导分次、极大Hamiltonian Poisson环面三个条件。

**状态建议。** 保留声明待核；不标他人形式化通过。

**直接证据。**

- [Quaternionic structures on conical symplectic singularities](https://jihaoliu.org/papers/quaternionic-structures-on-conical-symplectic-singularities.html) — 作者ai-results/liuxiv条目，2026-10-26；声称P27,28,29,30(1)(2)。访问层级：作者页搜索摘要；永久页403；对应GitHub路径404。声称极小化分次下四元数结构、权对称、约化性、Chevalley twist及Hamiltonian下降；非形式化核验。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v2 §3.1 Problem 28，式(7)。

**本次检索路径。**

- Web search system2："symplectic" "character" "dimensions" "Liu" 2026（2026-11-26；G2-012）。
- Web search system2："R_{d" "chi" "Liu" symplectic（2026-11-26；G2-012）。
- Web search system2：site:github.com "symplectic" "weight symmetry"（2026-11-26；G2-031）。
- Web search system2："symplectic" "weight symmetry" (site:jihaoliu.org OR site:mathoverflow.net OR site:aixiv.online)（2026-11-26；G2-031）。

**待核。** 获取73页稿的精确定理和分次归一化；作者AI自审不可替代证明核验。

#### QX-P-002227 · 反线性泊松共轭 ρ 存在性

**旧卡 → 本次变化。** 须保留四元数平方规律，ρ不是通常ρ²=id的实结构。Liu稿声称构造所需对象，仍为作者AI未人工验证声明。

**范围/修复。** 反线性、保分次、Poisson自同构ρ与T_c交换；ρ²在R_d上为exp(2dπi/r)。 补ρ²(f)=exp(2dπi/r)f，r为辛形式权；不可简化成普通共轭对合。

**状态建议。** 保持完整声明待核，disputed不表示已确认错误。

**直接证据。**

- [Quaternionic structures on conical symplectic singularities](https://jihaoliu.org/papers/quaternionic-structures-on-conical-symplectic-singularities.html) — 作者ai-results/liuxiv条目，2026-10-26；声称P27,28,29,30(1)(2)。访问层级：作者页搜索摘要；永久页403；对应GitHub路径404。声称极小化分次下四元数结构、权对称、约化性、Chevalley twist及Hamiltonian下降；非形式化核验。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v2 §3.1 Problem 29。

**本次检索路径。**

- Web search system2："quaternionic structures on conical symplectic singularities" Liu（2026-11-26；G2-015）。
- Web search system2："Poisson" "rho" "conjugation" "minimizer" symplectic（2026-11-26；G2-015）。
- Web search system2：site:github.com "quaternionic structures" "conical"（2026-11-26；G2-031）。
- Web search system2："real structure" "symplectic" (site:jihaoliu.org OR site:mathoverflow.net OR site:aixiv.online)（2026-11-26；G2-031）。

**待核。** 核定理中的ρ²相位、辛权r归一化、与T_c交换以及对所有分次的范围。

#### QX-P-002228 · R_r 约化李代数 + Chevalley 对合

**旧卡 → 本次变化。** Liu摘要宣称P30(1)(2)，不宣称(3)。现partially_solved如来源仅为AI自审稿，应降为“部分子问完整声明待核”的证据措辞。

**范围/修复。** R_r还原性；各R_d与Chevalley twist同构；全R上兼容的分次Chevalley对合为更强第三问。 列出三子问，区别线性表示同构与全代数对合；说明R_r的Lie括号由Poisson括号给出。

**状态建议。** 将partially_solved的证据改为(1)(2)声明待核；不能记为已核部分证明或Lean验证。

**直接证据。**

- [Quaternionic structures on conical symplectic singularities](https://jihaoliu.org/papers/quaternionic-structures-on-conical-symplectic-singularities.html) — 作者ai-results/liuxiv条目，2026-10-26；声称P27,28,29,30(1)(2)。访问层级：作者页搜索摘要；永久页403；对应GitHub路径404。声称极小化分次下四元数结构、权对称、约化性、Chevalley twist及Hamiltonian下降；非形式化核验。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v2 §3.1 Problem 30 (1)(2)(3)。

**本次检索路径。**

- Web search system2："conical symplectic" "Chevalley involution"（2026-11-26；G2-015）。
- Web search system2："R_r" "reductive" "graded" symplectic Chevalley（2026-11-26；G2-015）。
- Web search system2：site:github.com "symplectic" "Chevalley" "involution"（2026-11-26；G2-034）。
- Web search system2："Chevalley involution" (site:jihaoliu.org OR site:aixiv.online OR site:mathoverflow.net)（2026-11-26；G2-034）。

**待核。** 逐核稿件对(3)有无新修订；审计从各τ_d到全环τ所缺的相容性。

#### QX-P-002212 · 超曲面 K-模空间完全描述

**旧卡 → 本次变化。** 三次超曲面K/GIT对应出现2026年AI辅助完整声明；全次数的模空间问题未被这些材料覆盖。

**范围/修复。** H^K_{n,d}，3≤d≤n+1；完整边界/模空间描述。 补足参数n,d及K半稳定/多稳定对象和边界；把d=3声明单列。

**状态建议。** 保留总问题未决；增加三次子问完整声明待核，不能由讲座升级全题solved。

**直接证据。**

- [K-stability and GIT for cubic hypersurfaces](https://tianyuan.xmu.edu.cn/cn/info/1591/33485.htm) — 2026-10-15报告摘要，网页L40–55。访问层级：一手机构讲座摘要全文。维数至少5的三次超曲面K/GIT稳定与模stack对应声明；AI辅助，无ODP前提。
- [GIT-thresholds for K-moduli spaces of Hypersurfaces](https://aixiv.online/abs/2611.02689) — 摘要与Source arXiv:2611.30089；2026-11-23。访问层级：公开AI索引页全文，原稿未取得。研究(P^n,cH)且d≥n+1的第一壁；不是Fano超曲面本身全部K模空间。未链接代码/复现报告。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v2 §2.1 Problem 7。

**本次检索路径。**

- Web search system2："K-moduli" "cubic hypersurfaces" 2026 schememath（2026-11-26；G2-005）。
- Web search system2："H" "K-moduli" "degree" "hypersurfaces" 2026 GIT（2026-11-26；G2-005）。
- Web search system2：site:github.com "K-moduli" "cubic hypersurfaces"（2026-11-26；G2-023）。
- Web search system2：("schememath" OR "aiXiv" OR "Zenodo" OR "MathOverflow") "K-moduli" hypersurfaces（2026-11-26；G2-023）。

**待核。** 取得潘龙—吴昊宇完整预印本及修订，逐核模stack对应和边界。

#### QX-P-002215 · 曲线上半稳定向量丛模 K-稳定+边界模解释

**旧卡 → 本次变化。** 须区分向量丛的斜率稳定与其Fano模空间的K稳定。Zhao 2026已刊工作是genus2的Thaddeus束对模空间及边界，不覆盖原两问全部。

**范围/修复。** 固定行列式的曲线半稳定向量丛模空间M_{d,r}(C)本身的K稳定性；另问K模紧化边界解释。 明确K稳定的对象是M_{d,r}(C)这个Fano簇；补g、r、d、固定行列式及两子问，保留gcd(r,d)=1等光滑范围。

**状态建议。** 更新Zhao论文为2026已刊，并只记相关特例；不标整题已证。

**直接证据。**

- [K-stability of Thaddeus’ moduli of stable bundle pairs on genus two curves](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/kstability-of-thaddeus-moduli-of-stable-bundle-pairs-on-genus-two-curves/ED0AF7A129B9A4853278CADFA0309587) — FMS14 (2026)e33，DOI10.1017/fms.2026.10177，摘要L463–465。访问层级：期刊全文入口已取，核摘要/引言。genus2束对模K稳定、与quartic delPezzo三fold上线的GIT模同构；有到向量丛模的忘却映射。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v2 §2.1 Problem 9 (1)(2)。

**本次检索路径。**

- Web search system2："K-stability" "moduli" "vector bundles" Keller 2026（2026-11-26；G2-007）。
- Web search system2："M_{d,r}" "K-stable" "curve"（2026-11-26；G2-007）。
- Web search system2：site:github.com "K-stability" "vector bundles"（2026-11-26；G2-024）。
- Web search system2：("MathOverflow" OR "aiXiv" OR "Zenodo" OR "ProofForum") "K-stability" "moduli of vector bundles"（2026-11-26；G2-024）。

**待核。** Keller学位论文原证明及任意曲线/高秩部分需进一步精读。

#### QX-P-002217 · GM Fano 代数簇 K-稳定

**旧卡 → 本次变化。** Liu–Wang论文2026年已刊，主结论为一般special GM；不能把general special改成every smooth。

**范围/修复。** 每个光滑Gushel–Mukai n-fold，3≤n≤6。 补Gushel–Mukai全称、3≤n≤6以及every smooth的量词。

**状态建议。** 增加2026-07-06刊物记录；不因论文题名含K-stability便将全题解决。

**直接证据。**

- [K-stability of special Gushel-Mukai manifolds](https://epiga.episciences.org/18703) — EPIGA10 (2026)，DOI10.46298/epiga.2026.13743；摘要L31。访问层级：期刊元数据与摘要全文。Yuchen Liu–Linsheng Wang；一般special GM 3≤n≤6 K稳定；2026-01-23接受，07-06发表。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v2 §2.1 Problem 11。

**本次检索路径。**

- Web search system2："Gushel-Mukai" "K-stability" 2026（2026-11-26；G2-008）。
- Web search system2："smooth Gushel-Mukai" "K-stable" all（2026-11-26；G2-008）。
- Web search system2：site:github.com "Gushel-Mukai" "K-stability"（2026-11-26；G2-025）。
- Web search system2：("aiXiv" OR "Zenodo" OR "ProofForum" OR "MathOverflow") "Gushel-Mukai" "K-stability"（2026-11-26；G2-025）。

**待核。** 逐维核every smooth的后续，尤其n=4,5,6非一般成员。

#### QX-P-002225 · 4-正则图必含 3-正则子图？

**旧卡 → 本次变化。** 原帖已明确Tashkinov1982证明主命题；真正问的是从B到A的简易证明。子图不要求诱导或生成，B允许重边且多一条边，不能简单称为A的更强版。

**范围/修复。** 有限简单4正则图含一个3正则子图；原帖另问能否由加一条边版本给简易证明。 明确finite/nonempty/simple及非空3正则子图，不要求spanning/induced；若沿用MSE题源，将“由B得到简易证明”另列。

**状态建议。** 保留主图论定理solved；简易证明路线另作未验收，不把B直接当逻辑更强。

**直接证据。**

- [原题及精确设定](https://math.stackexchange.com/questions/2952985/every-4-regular-simple-graph-contains-a-3-regular-subgraph) — MSE #2952985：Theorem A与Theorem B以及末尾提问。访问层级：原题正文已定位；网页可取得。有限简单4正则图含一个3正则子图；原帖另问能否由加一条边版本给简易证明。
- [Every 4-regular simple graph contains a 3-regular subgraph](https://math.stackexchange.com/questions/2952985/every-4-regular-simple-graph-contains-a-3-regular-subgraph) — 原帖Theorem A/B及问题段。访问层级：原帖全文。A已由Tashkinov证明；B为4正则多重图加边；原帖追问B能否给A简证。

原问题定位：[原出处](https://math.stackexchange.com/questions/2952985/every-4-regular-simple-graph-contains-a-3-regular-subgraph)，MSE #2952985：Theorem A与Theorem B以及末尾提问。

**本次检索路径。**

- Web search system2："4-regular" "3-regular subgraph" Tashkinov Berge（2026-11-26；G2-020）。
- Web search system2："2952985" "regular" proof（2026-11-26；G2-020）。
- Web search system2：site:github.com "4-regular" "3-regular" Tashkinov（2026-11-26；G2-033）。
- Web search system2："4-regular" "3-regular" (site:mathoverflow.net OR site:math.stackexchange.com OR site:aisolve.org OR site:zenodo.org)（2026-11-26；G2-033）。

**待核。** Tashkinov原文Soviet Math Dokl26(1982)37–38尚未取得；初查依原帖准确书目信息及综述线索。

#### QX-P-002240 · klt 奇点好 Ricci 平坦度量（开放内核=无条件建立）

**旧卡 → 本次变化。** Namikawa–Odaka2503.15791v4只在smoothable projective symplectic设定给非条件结果，一般辛奇点仍附适当度量/DS延拓假设；P20的代数解答不自动解所有klt度量存在。

**范围/修复。** 对任意klt奇点无条件构造足够好的局部Ricci平坦Kähler度量并适用Donaldson–Sun理论。 将“与Donaldson–Sun延拓等价”的表述弱化为提出的充分路线，未经证明不得写逻辑等价；强调任意klt而非仅symplectic。

**状态建议。** 保留一般度量存在为未决；不能把Kaledin已证、辛锥完整声明转移至本题。

**直接证据。**

- [Canonical torus action on symplectic singularities](https://arxiv.org/abs/2503.15791) — v4 2026-02-06；摘要及版本说明Thm6.16。访问层级：arXiv摘要/版本史全文。对smoothable projective symplectic上的奇点有结果；一般辛奇点假设DS延拓与适当奇异(hyper)Kähler度量。
- [Stable Degeneration, Non-degenerate Forms, and Kaledin's Conjecture](https://arxiv.org/pdf/2606.02401) — v2 2026-06-22；PDF p1 Thm1.1=5.11，p2 Thm1.2/Cor6.3。访问层级：PDF全文已取，核主定理和适用条件。任意klt奇点非退化反身p形式特化保持非退化，闭性保持；因此辛稳定退化结论成立。

原问题定位：[原出处](https://arxiv.org/html/2601.15576v2)，v2 §3.1 item 21，前接Problem 20。

**本次检索路径。**

- Web search system1："good Ricci-flat" "klt" singularity（2026-11-26；G2-022）。
- Web search system1："klt" "Ricci-flat" "Donaldson" "Namikawa" "Odaka"（2026-11-26；G2-022）。
- Web search system2：site:github.com "klt" "Ricci-flat"（2026-11-26；G2-038）。
- Web search system2："good Ricci-flat" (site:mathoverflow.net OR site:jihaoliu.org OR site:aixiv.online OR site:zenodo.org)（2026-11-26；G2-038）。

**待核。** Odaka2610.35510虽声称任意辛奇点hyperKähler，仍不覆盖非辛klt；要解本题须独立的全klt范围论证。

### 关联参考卡的实质性纠错线索

QX-P-002235（9e5a037048365452）和QX-P-002237（711fbffa770faf65）不是本组任务，只在指定查重中读作参考。两卡旧备注把Jihao Liu的F-volume有限次数论文判为幻觉，应撤回此确定性断言并单列待核。2026-11-26通过一手作者页的搜索索引确实取得第9项：The finite degree formula for F-volumes，初稿2026-10-14，2026-10-26修订32页，SHA256 40de41a883cc33ddbf616d2c66aede4b7717552bf3adf9d058cfdb5a2a4a49ac。它声称解决v2 P49及带边界版本；与P50代数性不同。单篇全文尚未取得，不能反过来宣布P49已证。

直接入口：[作者AI成果页](https://jihaoliu.org/ai-results)；[永久页](https://jihaoliu.org/papers/finite-degree-formulas-for-frobenius-volumes-of-pairs.html)。本次证据为作者页搜索摘要，访问限制与原始返回见G2-040。

### AI审阅、计算证据和形式化必须区分

Jihao Liu作者页明确将machine-verified解释为内部AI核对/AI审阅，并明示不属于formal verification。QX2223、2224、2226、2227、2228及P49关联稿均不能由这个标签推出Lean验证。QX2236的SAT/CP-SAT说明未取得证书和代码；索引所列仓库在网页与REST API均404。QX2230只取得论文TeX主定理；固定commit的lean/docs/037.md为404，不足以证明全仓库没有其它形式化。

形式化索引补搜的域过滤返回库外噪声，因此另做了Formal Conjectures与Mathlib的精确GitHub代码API查询。查询0只限所列精确词；期间部分429已按重试间隔恢复，原始失败与成功记录均保留。Mathlib对canonical extension命中3个范畴论扩张文件，未建立几何P13的定理对应。没有任何题标为独立重跑通过。

### 指定查重结论


| 题号A / 版本 | 题号B / 版本 | 关系 | 核对理由 |
|---|---|---|---|
| QX-P-002213 / 0d7519ab0c189f67 | QX-P-002217 / 0b01249db6641ed1 | 同源不同问 | 2213是一般射影完全交的K稳定性（P8）；2217是每个光滑Gushel–Mukai簇（P11），量词与几何类不同。没有由题卡得出两者等价。 |
| QX-P-002214 / d88ae226494c9709 | QX-P-002251 / f55d8a6cf38038bc | 相关但不等价 | 2214是两个互换底/指数项a^b+b^a的无序对单射性且应限制>1；2251是固定k和项数/相异条件的k次幂和表示计数，不能互相代替。 |
| QX-P-002215 / 9c9e31b6eebe2fa5 | QX-P-002423 / b745d1e8b093b2e3 | 相关但不等价 | 2215研究曲线上向量丛模空间作为Fano簇的K稳定与紧化；2423核验余切丛中闭exact Lagrangian的Hamiltonian同痕反例声明。del Pezzo或bundle字样不构成同题。 |
| QX-P-002218 / 62b50aa56304e8cf | QX-P-002219 / ad62ee968ba01151 | 同源不同问 | P12对象为T_X及其拟étale乘积分解；P13对象为c1(X)典范扩张E。都求纯代数证明，但层、斜率条件及所问结论不同。 |
| QX-P-002221 / fed9fbbd6e7a5537 | QX-P-002223 / 24f9fa573a1f2042 | 同源不同问 | P20仅问稳定退化保持辛性；P25还要求Kollár分量、离散权、接触结构、K多稳定等。P20的2026定理不直接验收整个P25/hyperKähler包。 |
| QX-P-002224 / c522222215bc2949 | QX-P-001314 / 5f2a5fd127a08a29 | 相关但不等价 | 2224为代数辛奇点Hamiltonian环面约化的体积极小化子下降；1314为光滑圆盘保面积映射的零熵与混合动力学。Hamiltonian同名无同题关系。 |
| QX-P-002228 / f861bfcb9e478192 | QX-P-000704 / 5d90ed05ac8eba6e | 相关但不等价 | 2228问辛分次Poisson代数及Chevalley twist/对合；704问整数环上Chevalley群是否由三个对合生成，其中两个交换。对象、底环、结论皆异。 |
| QX-P-002229 / d1d0148351b304a8 | QX-P-002231 / f26431fc1831f119 | 同源不同问 | P31为辛锥短星积存在；P35为固定klt对的非负双有理模型上局部体积统一正下界。共享综述不构成等价。 |
| QX-P-002231 / f26431fc1831f119 | QX-P-002232 / 84b9c5e394a1562e | 同源不同问 | P35给固定klt对各双有理目标点的体积下界；P41描述Fano type补对的special lc places集合结构。前者为数值一致界，后者为赋值空间结构。 |
| QX-P-002231 / f26431fc1831f119 | QX-P-002233 / 202e3d9bb691cd3e | 同源不同问 | P35的全体模型/点体积下界与P43的固定理想族所有lct-computing赋值准单项/凸锥结构不同，不能由相似valuation词合并。 |
| QX-P-002231 / f26431fc1831f119 | QX-P-002234 / ed2c69473abd23df | 同源不同问 | P35求随双有理模型变化的局部体积统一正界；P44求固定理想族LCP中至少一个Gr_v有限生成/Kollár赋值。量词和目标不同。 |
| QX-P-002231 / f26431fc1831f119 | QX-P-002235 / 9e5a037048365452 | 同源不同问 | P35在特征0对固定klt对的双有理模型取下界；P46比较mod p约化的Fvol极限/维数常数比较。参数轴、体积对象不同。 |
| QX-P-002231 / f26431fc1831f119 | QX-P-002237 / 711fbffa770faf65 | 同源不同问 | P35为双有理模型一致下界；P49为正特征准étale有限态射下Fvol乘degree公式。有限态射与双有理非负映射不能互换。 |
| QX-P-002232 / 84b9c5e394a1562e | QX-P-002233 / 202e3d9bb691cd3e | 同源不同问 | P41是Fano type补对LCP中的special子集；P43是分次理想族LCP全体的准单项性/统一凸锥。共同缩写LCP掩盖不同设定。 |
| QX-P-002232 / 84b9c5e394a1562e | QX-P-002234 / ed2c69473abd23df | 同源不同问 | P41问补对special valuations全部结构；P44问分次理想族LCP内至少一个有限生成/Kollár赋值存在。存在性与集合结构并非同一问。 |
| QX-P-002232 / 84b9c5e394a1562e | QX-P-002235 / 9e5a037048365452 | 同源不同问 | P41是特征0补对special估值结构；P46是正特征约化Fvol与特征0归一化体积的极限/比较。不是同一主命题。 |
| QX-P-002232 / 84b9c5e394a1562e | QX-P-002423 / b745d1e8b093b2e3 | 相关但不等价 | P41涉及代数log CY/Fano紧化、special valuation骨架；2423涉及T*Q中的exact Lagrangian嵌入及Hamiltonian同痕。镜像/辛几何邻近不构成同题。 |
| QX-P-002233 / 202e3d9bb691cd3e | QX-P-002234 / ed2c69473abd23df | 同源不同问 | 同用固定理想族LCP；P43断言每个元素准单项且可能同模型凸锥，P44只断言存在Gr有限生成或Kollár元素。性质强弱与∀/∃交错，未建立等价或单向蕴含。 |
| QX-P-002233 / 202e3d9bb691cd3e | QX-P-002235 / 9e5a037048365452 | 同源不同问 | P43研究特征0 lct-computing估值的类型；P46研究mod p Frobenius体积极限，非同一对象或量词。 |
| QX-P-002233 / 202e3d9bb691cd3e | QX-P-002237 / 711fbffa770faf65 | 同源不同问 | P43的所有lct估值准单项性与P49的Fvol有限态射次数公式无已核等价。 |
| QX-P-002234 / ed2c69473abd23df | QX-P-002235 / 9e5a037048365452 | 同源不同问 | P44是LCP中的有限生成赋值存在性；P46是Fvol约化极限/比较，不是有限生成代数同义表达。 |
| QX-P-002234 / ed2c69473abd23df | QX-P-002237 / 711fbffa770faf65 | 同源不同问 | P44有限生成指Gr_v R；P49有限次数指有限态射的degree。两种finite所指对象不同。 |
| QX-P-002238 / e22e9ed6a5268773 | QX-P-002237 / 711fbffa770faf65 | 同源不同问 | P50问Fvol是否为代数数；P49问准étale有限态射的乘degree公式。2026作者AI稿声称P49，未直接覆盖P50。 |
| QX-P-002240 / 94f66baa0e7b3f20 | QX-P-001659 / 798b03f89d4a3d10 | 相关但不等价 | 2240为任意复klt奇点的局部奇异Ricci平坦Kähler度量；1659为光滑紧球面S^n是否容许全局Ricci平坦Riemann度量。局部/全局、奇异/光滑与Kähler条件不同。 |

全部24对均未判同题，不建议合并。新增QX2212↔QX2211仅来自全库标题索引，关系待定，双方版本写在逐题回传；未指派也未扩做全文审计。

## 5. 组合、数论与离散问题

核查日期：2026-11-26。范围：QX-P-002241—QX-P-002265，共25题；对应版本保留在逐题JSONL。原题/学术/代码/公开AI社区/库内索引均实际执行。本文只列影响题面、状态、来源、形式化或查重的发现。没有写线上、发帖或运行第三方代码。

### 优先结论

- QX-P-002260：标准k≥2版本已有已刊证明，旧开放状态应撤下。
- QX-P-002256：新官方摘要覆盖≥n/3边界，但全文不可达，只列完整声明待核。
- QX-P-002261：当前所谓修正版仍错；K3,3否定该变体，标准CLW未被此反例否定。
- QX-P-002255：题意偏离EP40，Lean主问仍占位；历史空集漏洞是形式化错误，不是数学解答。

### QX-P-002260：一般k“开放”改为已刊定理；必须补k≥2

**当前版本：** `d381d59b4d2dedf2`。**本轮分类：** 原题已证。

旧卡“一般k开放”失效：Messuti–Schacht Theorem1.2已证明对每个整数k≥2，oddgirth≥2k+1且δ>3n/(4k)的图同态到C_{2k+1}。原刊2014-11上线、2015卷80；旧卡k=1分支也错，K5为字面k=1反例。

**旧卡 → 建议变化：** 把标准k≥2命题改为原题已证并替换开放状态证据。；补严格>、k≥2、任意图，删除k=1AES与一般k开放旧注。

**直接证据与定位：**

- [Messuti–Schacht作者PDF](https://www.math.uni-hamburg.de/home/schacht/2015/3n4k.pdf)：PDFp2 Theorem1.2；p3明确回答ACH；§3 pp10–13。访问层级：正文相关节。
- [Wiley原刊记录](https://onlinelibrary.wiley.com/doi/10.1002/jgt.21840)：JGraphTheory80(1),69–81；First published2014-11-10（卷年2015）。访问层级：出版社页面/摘要。

**量词与适用范围：** k≥2，n阶图奇围长≥2k+1且δ>3n/(4k)⇒G→C_{2k+1}。 必须补k≥2、严格>；不要求平面。k=1时K5满足假设而非3色，故不能称AES已证该字面。

**实际检索路径：**
- web.system1_search_query：`"Albertson" "Chan" "Haas" conjecture homomorphism`（2026-11-26）。
- web.system1_search_query：`"odd girth" "3n/(4k)" homomorphism conjecture`（2026-11-26）。
- web.system1_search_query：`Messuti Schacht "odd girth" "3" "4k"`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_search_013.json, chunk_3_search_019.json, chunk_3_search_020.json, chunk_3_search_022.json, chunk_3_search_024.json, chunk_3_search_031.json, chunk_3_search_035.json。

**待复核：** 如要纳入δ=3n/(4k)等号需另立变体；原稿§4的极值例不能省略。

### QX-P-002256：≥n/3边界出现完整预印本声明，全文待取

**当前版本：** `bda67f828449efd2`。**本轮分类：** 完整证明/反例声明待核。

发现2026-09-21 Li–Li arXiv2609.24097完整声明，官方索引摘要明确写三角形自由、δ≥n/3⇒χ≤4，恰覆盖等号边界。abs/html/pdf直开均DisabledError，故仅把旧“等号仍开”改为“新完整声明待核”。

**旧卡 → 建议变化：** 将“等号仍开放”改为“2026-09完整声明待核”，不升级已证。；把最新来源与严格>历史结果分列；公式保留≥。

**直接证据与定位：**

- [Jiaao Li–Xinyuan Li, Bounded chromatic number of graphs with small clique number and large minimum degree](https://arxiv.org/abs/2609.24097)：官方索引摘要；2026-09-21 v1。访问层级：仅标题/摘要；abs/html/pdf DisabledError。
- [同名Brandt仓库](https://github.com/yachachli/brandt-conjecture-5-1/blob/main/README.md)：README检索摘要。访问层级：仅检索摘要。

**量词与适用范围：** 每个n阶无三角形图，若最小度δ≥n/3，是否χ≤4。 旧严格>结果不能覆盖≥；新官方摘要确实是≥。同名Brandt正则超图/总支配猜想是别题。

**实际检索路径：**
- web.system1_search_query：`"Brandt" "Thomassé" "n/3" triangle free 2026`（2026-11-26）。
- web.system1_search_query：`"2609.24097" "Theorem"`（2026-11-26）。
- web.system1_search_query：`"Bounded chromatic number of graphs with small clique number and large minimum degree" Li`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_search_011.json, chunk_3_search_016.json, chunk_3_search_018.json, chunk_3_search_020.json, chunk_3_search_023.json, chunk_3_search_028.json。

**待复核：** 最高优先取得2609.24097全文、定理编号、假设和版本记录，核是否勘误/撤回及独立验收。

### QX-P-002261：所谓权威改述仍漏奇完全二分图例外

**当前版本：** `2e9dc6e0bb5dc9d8`。**本轮分类：** 部分进展。

现卡所谓权威改述“k-可染且Δ≤k⇒均等k色”仍错：K3,3在k3时无法分成3个大小2的独立集。标准CLW必须排除K_{k+1}、k2奇圈和奇k的K_{k,k}。2025预印本给k≥cn的渐近进展，不是全解。

**旧卡 → 建议变化：** 用标准CLW重写，不再以k可染替代异常图排除。；加入K3,3对旧变体的显式反例；不要把标准CLW标disproved。；补Cor1.6渐近适用范围。

**直接证据与定位：**

- [Cheng–Li–Sun–Wang, A step toward Chen-Lih-Wu conjecture](https://arxiv.org/html/2511.03957v1)：Conjecture1.1、Theorem1.5、Corollary1.6。访问层级：正文相关节。
- [Equitable coloring of graphs beyond planarity](https://www.sciencedirect.com/science/article/pii/S0166218X25005839)：2026-01-30；Introduction CLW表述。访问层级：检索正文片段。

**量词与适用范围：** 连通最大度≤k图的均等k染色；仅障碍为K_{k+1}、k=2奇圈及奇k的K_{k,k}。 k-可染并未排除奇完全二分图；删异常图后才是标准CLW。

**实际检索路径：**
- web.system1_search_query：`"Chen" "Lih" "Wu" equitable colouring conjecture 2026`（2026-11-26）。
- web.system1_search_query：`site:github.com "Chen-Lih-Wu" conjecture`（2026-11-26）。
- web.system1_search_query：`"equitable" "maximum degree" "complete bipartite" "odd" Chen Lih Wu 2026`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_search_013.json, chunk_3_search_016.json, chunk_3_search_032.json, chunk_3_search_043.json。

**待复核：** 若未来完整证明出现，核全体度数范围与异常图列表；当前只完成初查。

### QX-P-002255：EP40题意修正、旧Lean漏洞与新增同题候选

**当前版本：** `bbfd6a5636e5bffb`。**本轮分类：** 暂未找到可验证结果。

EP40不是渐近基表示函数的显式增长下界，而是哪些g(N)→∞能使A(N)≫√N/g(N)推出表示函数无界。固定提交的Lean主问与弱存在版均sorry；条件蕴含EP28有证明，历史空集漏洞issue4977已关闭并改题面，不能当数学解决。

**旧卡 → 建议变化：** 重写人话版为密度阈值问题。；补Lean主问sorry与历史误形式化说明，避免把空集填洞或条件蕴含当解。；索引新增同题候选QX-P-000331；尚未取得其正文，关系暂定待定。

**直接证据与定位：**

- [Erdős Problems40](https://www.erdosproblems.com/40)：题干公式、与EP28关系；直接open403但检索全文提取可读。访问层级：检索正文提取；直开403。
- [固定提交Formal Conjectures40.lean](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/ErdosProblems/40.lean)：Erdos40For；erdos_40.answer；erdos_40；variants.weaker；variants.implies_erdos_28。访问层级：已取得完整代码未重跑。
- [Misformalization issue4977](https://github.com/google-deepmind/formal-conjectures/issues/4977)：旧638da20行45–57；Closed并关联PR4993。访问层级：正文相关节。
- [Erdős Problem a Day40](https://www.erdosproblemaday.com/report/40)：§0、§3、§6、§9；最终补查已读网页全文。报告自标PARTIAL；密度负范围、有限计算与无限主问分列，外部代码未运行。

**量词与适用范围：** 确定全部g:N→R, g(N)→∞，使每个满足A(N)≫√N/g(N)的集合A都有limsup r_A=∞。 不要求A为渐近基，不问r_A的具体增长下界；当前人话版把EP28/其他定量猜想混入。

**实际检索路径：**
- web.system1_search_query：`"erdosproblems.com/40"`（2026-11-26）。
- web.system1_search_query：`site:github.com "erdos_40"`（2026-11-26）。
- web.system1_search_query：`Erdos problem 40 strong Erdos Turan density representation function g(N)`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_pinned_0.json, chunk_3_search_011.json, chunk_3_search_017.json, chunk_3_search_022.json, chunk_3_search_028.json, chunk_3_search_040.json, chunk_3_search_043.json。

**待复核：** 复核QX-P-000331全文与当前rev；新AI报告引用的负范围可在后续核原稿，不在本轮宣布其范围最优。

### QX-P-002241：Fu不构成第三独立证明；齐性是结论

**当前版本：** `45dc9e33bd98d22f`。**本轮分类：** 完整证明/反例声明待核。

本轮核到 Hu–Liu–Wan 2610.38736 的完整齐性声明及 Fu 2611.01423v2 Theorem 1.1；Fu 明确依赖 OpenAI 与 HLW，不能计为第三条独立证明。卡片人话版把“齐性”误放入假设，须恢复猜想所断言的结论。

**旧卡 → 建议变化：** 删除标题与备注中“三路独立解决”的计数，将Fu写为依赖既有声明的解释性重写。；重写人话版，补光滑、复射影、接触Fano假设与齐性结论。；保持claimed/待核，不因专家作者、公开手稿或仓库总形式化比例升级已证。

**直接证据与定位：**

- [Hu–Liu–Wan 接触 Fano 预印本](https://arxiv.org/abs/2610.38736)：v1；摘要（2026-10-28）。访问层级：仅标题/摘要。
- [Fu: The classification of Fano contact manifolds revisited](https://arxiv.org/html/2611.01423v2)：v2（2026-11-14）；摘要、Introduction、Theorem 1.1。访问层级：正文相关节。
- [OpenAI 固定提交手稿入口](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Contact-Fano-manifolds-and-the-LeBrun-Salamon-conjecture-September-23-2026/paper.pdf)：commit adc7f1241b42e322a6451854ab7e4b4c146bf78a；PDF入口。访问层级：仅仓库页面/未取得PDF正文。

**量词与适用范围：** 光滑、连通、复射影接触 Fano 流形是否必齐性（等价于适当的伴随簇分类）。 现卡先假设齐性；标题把 Fu 的解释性重写计作独立解题链。

**实际检索路径：**
- web.system1_search_query：`"LeBrun" "contact Fano" "2610.38736"`（2026-11-26）。
- web.system1_search_query：`"The classification of Fano contact manifolds revisited"`（2026-11-26）。
- web.system1_search_query：`"Fano contact manifold" "OpenAI"`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_search_001.json, chunk_3_search_002.json, chunk_3_search_025.json, chunk_3_search_037.json。

**待复核：** 取得OAI固定版本PDF及适用主定理全文；核HLW与OAI的数学独立性、相互引用和后续勘误。；核正式评审/独立人类验收与本题确切Lean定理、依赖；本轮未重跑。

### QX-P-002249：保留不存在，删除错误强分类与聚点理由

**当前版本：** `4eeb711feab02a18`。**本轮分类：** 原题已反驳。

Eremenko在MO444411的作者证明给出不存在结论。主结论保留，但现卡“整数集在C有聚点”和更强分类f=z+b均有错；后者字面被f=-z（以及不加非恒定条件时的常数4）否定。

**旧卡 → 建议变化：** 删除“整数在C有聚点”及不对应题目的“满射到其余地方”。；删除或重新核定f=z+b强分类，注明f=-z反例；主不存在结论单列。

**直接证据与定位：**

- [Eremenko MO回答444446](https://mathoverflow.net/questions/444411/a-holomorphic-function-sending-integers-and-only-integers-to-0-1-2-3/444446)：2023-04-09回答主证明、Remarks2–3。访问层级：正文相关节。
- [Bergweiler–Eremenko 2009](https://arxiv.org/abs/0808.3800)：摘要、Proc AMS137 (2009)2329–2333；DOI10.1090/S0002-9939-08-09788-8。访问层级：仅标题/摘要。

**量词与适用范围：** 整函数f满足f(Z)={0,1,2,3}且f^{-1}({0,1,2,3})⊂Z是否存在。 应保留原题像集等号；整数集在C离散，没有有限聚点。额外分类漏条件/符号，不能当已核定理。

**实际检索路径：**
- web.system2_search_query：`site:mathoverflow.net/questions/444411`（2026-11-26）。
- web.system1_search_query：`holomorphic function integers only 0 1 2 3 Eremenko 444411`（2026-11-26）。
- web.system1_search_query：`site:github.com "holomorphic" "integers" "0,1,2,3"`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_search_005.json, chunk_3_search_007.json, chunk_3_search_009.json, chunk_3_search_022.json, chunk_3_search_027.json, chunk_3_search_039.json, chunk_3_search_041.json, chunk_3_search_044.json。

**待复核：** 若需升级证据级别，取得Marchenko–Ostrovskii英文Theorem1.1并逐项核对MO的实性/导数交错使用；本轮深度止于初查。

### QX-P-002250：Gelfond–Schneider层数错误及条件结果

**当前版本：** `04b8e53ca70d3045`。**本轮分类：** 部分进展。

恢复正有理非整数r的右结合四层幂塔问题。旧注把r^r称为超越数是错的：它是代数无理数，Gelfond–Schneider用于三层；四层有Schanuel条件下的已刊定理，未找到无条件解决。

**旧卡 → 建议变化：** 补r>0与右结合定义；纠正Gelfond–Schneider适用层数。；单列条件性Theorem3及公开AI暴露，不记已解决。

**直接证据与定位：**

- [MSE3655352](https://math.stackexchange.com/questions/3655352/if-r-in-mathbbq-setminus-mathbbz-is-it-possible-that-rrrr-in-math)：题干、Gelfond–Schneider评论、0回答。访问层级：正文相关节。
- [Schanuel’s Conjecture and the Transcendence of Power Towers](https://www.mdpi.com/2227-7390/9/7/717)：Theorem3、§5；DOI10.3390/math9070717。访问层级：正文相关节。
- [Stanford UQ 公开AI答复入口](https://uq.stanford.edu/question/299)：问题/模型答复搜索命中。访问层级：仅检索摘要。

**量词与适用范围：** r∈Q\Z时四层右结合幂塔是否可能有理；原题实数解释需r>0。 负底数未指定复对数分支；r^r的超越性说法错误。

**实际检索路径：**
- web.system1_search_query：`"rational" "power tower" "3655352"`（2026-11-26）。
- web.system1_search_query：`rational noninteger r four power tower r r r r rational Gelfond Schneider`（2026-11-26）。
- web.system1_search_query：`site:github.com "rational" "power tower" "conjecture"`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_search_010.json, chunk_3_search_012.json, chunk_3_search_027.json, chunk_3_search_029.json, chunk_3_search_038.json, chunk_3_search_039.json, chunk_3_search_041.json。

**待复核：** 若出现无条件四层声明，核其是否偷用Schanuel或把代数指数定理误用于超越指数。

### QX-P-002251：互异项数限定与平凡存在性子问

**当前版本：** `f55d8a6cf38038bc`。**本轮分类：** 部分进展。

原题要求恰好g(k)个互异非负整数的k次幂，排列视为同一表示。存在某个唯一表示数的子问可由最小和立即解决；全部n的刻画/计数是另一问题。A006431允许重复部件，不能直接给互异版本的完整分类。

**旧卡 → 建议变化：** 恢复恰g(k)项、互异非负底数、无序约定。；将平凡存在性与一般分类/计数拆开；A006431保留为相关部分来源。

**直接证据与定位：**

- [MSE103432](https://math.stackexchange.com/questions/103432/are-there-unique-solutions-for-n-sum-limitsj-1gk-a-jk)：题干a_u≠a_v≥0、14例、后续计数问。访问层级：正文相关节。
- [OEIS A006431关联检索](https://oeis.org/A006431)：唯一分拆成四个非负平方；检索可见定义。访问层级：仅检索摘要。

**量词与适用范围：** 恰g(k)个互异非负底数，n=Σa_j^k的无序表示唯一性及计数。 当前人话版遗漏固定项数、互异性，且把普通四平方唯一表示表当互异版完解。

**实际检索路径：**
- web.system1_search_query：`"Uniqueness" "representations" "103432"`（2026-11-26）。
- web.system1_search_query：`unique representation sums kth powers g(k) distinct integers Waring uniqueness`（2026-11-26）。
- web.system1_search_query：`"uniqueness" "Waring"`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_search_010.json, chunk_3_search_012.json, chunk_3_search_014.json, chunk_3_search_020.json, chunk_3_search_023.json, chunk_3_search_027.json, chunk_3_search_029.json, chunk_3_search_042.json。

**待复核：** 需核互异四平方的完整分类是否另有已刊结果；不能把允许重复的分类筛选后未经证明称完整。

### QX-P-002253：至少一次与无限次不能合并

**当前版本：** `98db1c5cc0d6c06c`。**本轮分类：** 部分进展。

原MSE只问每个a>1是否至少有一个p∤a−1使Φ_p(a)为合数，卡片升级成无限多个。Pomerance现稿§1明确连a=2的素数指数Mersenne合数无穷性也仍未解决；不能误称其论文已证该无穷性。

**旧卡 → 建议变化：** 把原帖存在版与卡片加强版分卡内子问，补p∤a−1。；不把Pomerance的一般分圆结论写为Mersenne素数指数合数无穷已证。

**直接证据与定位：**

- [MSE4149380](https://math.stackexchange.com/questions/4149380/for-any-fixed-integer-a-gt-1-how-do-you-prove-that-fracap-1a-1-is)：题干与补充问；p∤a−1。访问层级：正文相关节。
- [Pomerance, Cyclotomic primes](https://arxiv.org/html/2411.04213v2)：§1 Introduction，第2段；v2标记2024-12-03，正文Date显示2026-08-24。访问层级：正文相关节。

**量词与适用范围：** ∀a>1，∃素数p∤a−1，使(a^p−1)/(a−1)为合数；原帖另含Φ_{2p}及OR变体。 当前标题/备注把至少一次加强成无限多，遗漏p∤a−1。

**实际检索路径：**
- web.system1_search_query：`"4149380" "prime"`（2026-11-26）。
- web.system1_search_query：`"prime" "composite" "(a^p" "(a-1)"`（2026-11-26）。
- web.system1_search_query：`"composite" "a-1" "prime" cyclotomic`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_search_010.json, chunk_3_search_012.json, chunk_3_search_014.json, chunk_3_search_028.json, chunk_3_search_029.json, chunk_3_search_035.json, chunk_3_search_036.json。

**待复核：** 追所有a的存在版专门定理；核Pomerance页面v2标记与正文日期差异，不在初查中猜测修订。

### QX-P-002242：倒Fibonacci编码不是Zeckendorf整数编码

**当前版本：** `d26ae49dfc6a4c8a`。**本轮分类：** 暂未找到可验证结果。

核回MSE1618511：这是以1/2,1/3,1/5,…为权重的贪心小数编码，不是整数Zeckendorf编码或φ进制。评论引用2006年倒Fibonacci和的无理性，但出版社摘要的单等差子列结论不足以直接覆盖任意周期0/1数字块，不能据此宣布反驳原题。

**旧卡 → 建议变化：** 用原帖倒数贪心规则替换Zeckendorf式叙述。；将评论否定声明与已刊文献可见摘要范围分开，暂不改为已反驳。

**直接证据与定位：**

- [Do all rational numbers repeat in Fibonacci coding?](https://math.stackexchange.com/questions/1618511/do-all-rational-numbers-repeat-in-fibonacci-coding)：题干、1/4例、Random评论。访问层级：正文相关节。
- [Matala-Aho–Prévost 2006](https://link.springer.com/article/10.1007/s11139-006-6511-4)：Ramanujan J11,249–261；摘要。访问层级：仅标题/摘要；正文订阅墙。

**量词与适用范围：** 有理数的贪心倒Fibonacci展开是否最终循环。 现卡把整数Zeckendorf的不相邻1规则混入了原帖的小数编码。

**实际检索路径：**
- web.system2_search_query：`site:math.stackexchange.com/questions/1618511`（2026-11-26）。
- web.system1_search_query：`Fibonacci coding rational numbers eventually periodic Matala-aho Prevost`（2026-11-26）。
- web.system1_search_query：`"Matala-aho" "Prévost" "2006" Fibonacci irrationality`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_search_003.json, chunk_3_search_004.json, chunk_3_search_006.json, chunk_3_search_008.json, chunk_3_search_021.json, chunk_3_search_024.json, chunk_3_search_025.json, chunk_3_search_038.json。

**待复核：** 取得2006全文及2020线性无关后续，核任意周期0/1块是否落在定理条件内；对终止/非终止展开分别判断。

### QX-P-002243：染色对象是小格，非整块四连方

**当前版本：** `2b0877ac03382cde`。**本轮分类：** 暂未找到可验证结果。

现卡把格子染色改成整块骨牌染色，改变了问题。原题是在给定2n×2n铺砌中给每个小格染色，使每块四格各取四种颜色且相邻小格异色；不能直接套平面四色定理。

**旧卡 → 建议变化：** 完整替换人话版为逐格染色与每块彩虹条件。；把有限作者试验与一般证明分列；不以四色定理解决补K4后的图。

**直接证据与定位：**

- [Are tetromino packings always 4-colorable?](https://math.stackexchange.com/questions/5030629/are-tetromino-packings-always-4-colorable)：题干、Remarks、K4补边表述。访问层级：正文相关节。
- [Prismatic T-tetrominoes 检索命中](https://zenodo.org/records/23631079)：题名/摘要；2026-10-25。访问层级：仅检索摘要。

**量词与适用范围：** 任意给定2n×2n四连方铺砌，每格着1–4色，各四连方彩虹且正交邻格异色。 整块骨牌一色的邻接图问题与原题不等价。

**实际检索路径：**
- web.system2_search_query：`site:math.stackexchange.com/questions/5030629`（2026-11-26）。
- web.system1_search_query：`tetromino tiling 4 colouring every tile 1 2 3 4 5030629`（2026-11-26）。
- web.system2_search_query：`site:github.com "tetromino" "4-colorable"`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_search_003.json, chunk_3_search_004.json, chunk_3_search_006.json, chunk_3_search_008.json, chunk_3_search_025.json, chunk_3_search_033.json。

**待复核：** 取得任何候选反例铺砌的完整格点编码或一般证明；目前有限试验未复算。

### QX-P-002244：恢复访问次数驱动的确定性规则

**当前版本：** `00deda911026386c`。**本轮分类：** 暂未找到可验证结果。

原过程按第k次步长k、两候选位置的累计访问次数和固定平局方向决定下一步；题卡的禁点/循环描述不对应原问题。OEIS A329230记录覆盖时间与猜想，有限表不能证明所有n均覆盖。

**旧卡 → 建议变化：** 按原题与A329230重写动力规则，补覆盖时间定义与计数约定。；将所有n覆盖和a(n)=n刻画分别标为待核问题，不以有限表证明。

**直接证据与定位：**

- [Grasshopper jumping on circles](https://math.stackexchange.com/questions/3418970/grasshopper-jumping-on-circles)：题干运动规则与平局逆时针约定。访问层级：检索返回原帖正文片段。
- [OEIS A329230](https://oeis.org/A329230)：NAME、COMMENTS、table链接。访问层级：正文相关节。

**量词与适用范围：** n个圆周位置，逐步在±k两个候选位置中选访问较少者，平局按固定方向；问覆盖所有位置的时间/性质。 现卡加入原题没有的禁点设定；原MSE平局逆时针，OEIS采用顺时针，是反射等价的覆盖时间约定。

**实际检索路径：**
- web.system2_search_query：`site:math.stackexchange.com/questions/3418970`（2026-11-26）。
- web.system1_search_query：`grasshopper circle A329230 finite deterministic`（2026-11-26）。
- web.system1_search_query：`"Grasshopper jumping on circles"`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_search_003.json, chunk_3_search_004.json, chunk_3_search_006.json, chunk_3_search_008.json, chunk_3_search_023.json, chunk_3_search_025.json, chunk_3_search_042.json, chunk_3_search_044.json。

**待复核：** 读取并审计候选一般覆盖证明；独立复算属于后续，未执行。

### QX-P-002245：同一模数与有序串；Lau v2为部分结果

**当前版本：** `521a971e1c563690`。**本轮分类：** 部分进展。

原题固定同一个模数q及任意有序既约剩余类串，问能否由连续素数实现。现人话版误写为多模数互素/CRT。Lau的2026年v2已核：给定长串能抽出可实现块模式及计数下界，未证明所有指定模式。

**旧卡 → 建议变化：** 删除CRT式误译，写同一模数与有序串。；更新Lau至v2并补在线期刊元数据；不要将计数下界称为任意模式证明。

**直接证据与定位：**

- [MSE2194973 原题](https://math.stackexchange.com/questions/2194973/is-every-finite-list-of-integers-coprime-to-n-congruent-pmod-n-to-a-list-of)：题干有序列表及连续素数。访问层级：检索返回原帖正文片段。
- [Lau, Residue Class Patterns of Consecutive Primes](https://arxiv.org/html/2409.12819v2)：v2 2026-07-13；Conjecture1.1、Theorem1.2、Theorem1.5、Cor1.7–1.8。访问层级：正文相关节。
- [Acta Arithmetica 在线条目](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/online/116587/residue-class-patterns-of-consecutive-primes)：DOI10.4064/aa240925-22-9；online 2026-10-28。访问层级：检索元数据。

**量词与适用范围：** 任意q≥2及有序有限串(a1,…,am)，各gcd(ai,q)=1，是否有连续素数pi满足pi≡ai(mod q)。 不是多个两两互素模数的中国剩余定理。原帖一次出现与文献无限次出现应分开。

**实际检索路径：**
- web.system2_search_query：`site:math.stackexchange.com/questions/2194973`（2026-11-26）。
- web.system1_search_query：`consecutive primes prescribed residues coprime finite sequence Shiu Lau 2409.12819`（2026-11-26）。
- web.system1_search_query：`finite list coprime n consecutive primes residues`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_search_003.json, chunk_3_search_004.json, chunk_3_search_006.json, chunk_3_search_008.json, chunk_3_search_014.json, chunk_3_search_021.json, chunk_3_search_026.json, chunk_3_search_038.json, chunk_3_search_039.json。

**待复核：** 核一次出现与无限次出现的蕴含是否有另行定理；查新证明若出现须核任意q、任意串。

### QX-P-002252：内部定义及差1表的猜想身份

**当前版本：** `8127330b4f5c54f4`。**本轮分类：** 部分进展。

原题的“内部”排除左右最外两条对角线，等价2≤r≤n−2。Blokhuis–Brouwer–de Weger的差1表是Conjecture3.1，已核有限范围与特定指数对，不是所有三连续值不存在的证明。

**旧卡 → 建议变化：** 精确定义内部；把Conjecture3.1与已证有限范围分列。

**直接证据与定位：**

- [MSE4811425](https://math.stackexchange.com/questions/4811425/does-the-interior-of-pascals-triangle-contain-three-consecutive-integers/4816138)：原题内部定义及答案引用。访问层级：正文相关节。
- [Binomial collisions and near collisions](https://arxiv.org/pdf/1707.06893)：v2；PDFp4 §3.1、Conjecture3.1、表后范围。访问层级：正文相关节。

**量词与适用范围：** 集合{binom(n,r):2≤r≤n−2}是否含三个连续整数。 若只写排除r=1,n−1而仍保留外沿r=0,n，则内部定义不完整。

**实际检索路径：**
- web.system1_search_query：`"three consecutive integers" "Pascal"`（2026-11-26）。
- web.system1_search_query：`"Binomial Collisions and Near Collisions" "3.1"`（2026-11-26）。
- web.system1_search_query：`site:github.com "Pascal" "three consecutive"`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_search_010.json, chunk_3_search_021.json, chunk_3_search_027.json, chunk_3_search_035.json, chunk_3_search_036.json, chunk_3_search_040.json。

**待复核：** 核是否有差1表后续更新；三连续结论必须独立覆盖全部n,r。

### QX-P-002258：West目录非当前开放认证；Hasanvand线索未核

**当前版本：** `b399c3ee891ae814`。**本轮分类：** 暂未找到可验证结果。

West原目录核实确有5连通平面图4可选问题，但站点首段自述长期未维护，因此不能把“页面仍开”当2026状态证明。历史备注Hasanvand2022未在本次精确查询中核到原始对应论文；亦未找到可验完整解。

**旧卡 → 建议变化：** 把5-可染背景改成5-可选；West状态证据注明长期未维护。；Hasanvand2022保留为待定位线索，删除“本轮已核”的暗示。

**直接证据与定位：**

- [West open problems目录](https://dwest.web.illinois.edu/openp/)：首段long neglected；List Coloring条目。访问层级：正文相关节。

**量词与适用范围：** 每个5顶点连通有限简单平面图是否4-choosable。 背景应比较Thomassen的平面图5-可选定理，而非仅普通5-可染定理。

**实际检索路径：**
- web.system1_search_query：`"5-connected" planar "4-choosable" conjecture`（2026-11-26）。
- web.system1_search_query：`"5-connected planar" "4-choosable" proof counterexample`（2026-11-26）。
- web.system1_search_query：`"5-connected planar graphs" "Hasanvand"`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_search_013.json, chunk_3_search_019.json, chunk_3_search_020.json, chunk_3_search_023.json, chunk_3_search_030.json, chunk_3_search_031.json, chunk_3_search_034.json, chunk_3_search_037.json, chunk_3_search_042.json。

**待复核：** 需原Hasanvand2022精确题名/DOI及最新综述才能提高当前状态强度。

### QX-P-002259：新奇围长4k+3声明未覆盖原4k范围

**当前版本：** `c96bef12b3fe92b9`。**本轮分类：** 部分进展。

2026-11 Naserasr新稿官方摘要给odd girth≥4k+3时到C_{2k+1}的同态，比现卡普通girth≥4k更强的假设，不能算解决：后者仅保证odd girth≥4k+1。新稿全文不可达，列部分结果声明。

**旧卡 → 建议变化：** 补2026部分声明及精确奇围长门槛；不将其标题解释为原题已证。

**直接证据与定位：**

- [West原目录](https://dwest.web.illinois.edu/openp/)：Graph Homomorphism and Circular Coloring条目。访问层级：正文相关节。
- [Naserasr, Jaeger conjecture and Jaeger-Zhang conjecture](https://arxiv.org/abs/2611.08862)：官方摘要；v1 2026-11-06。访问层级：仅标题/摘要；abs/pdf DisabledError。

**量词与适用范围：** 每个围长至少4k的平面图是否同态到C_{2k+1}。 普通围长与奇围长不同；4k+3不能替代4k（奇围长至少4k+1）的缺口。

**实际检索路径：**
- web.system1_search_query：`"Jaeger" "4k" planar conjecture 2026`（2026-11-26）。
- web.system1_search_query：`site:github.com "Jaeger" "girth" conjecture`（2026-11-26）。
- web.system1_search_query：`"Jaeger conjecture and Jaeger-Zhang conjecture" arxiv`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_search_013.json, chunk_3_search_016.json, chunk_3_search_018.json, chunk_3_search_031.json, chunk_3_search_034.json, chunk_3_search_044.json。

**待复核：** 取得Naserasr全文和Jafari前置结果；核定理常数与原题4k+1奇围长缺口。

### QX-P-002262：5份构造是下界；AI局部不可扩展不解全问

**当前版本：** `b75dce2511e6e189`。**本轮分类：** 部分进展。

West与Meszka–Šiagiová记录构造了5个边不交Hoffman–Singleton图，这是下界，不是最大值等于5的上界。公开Codex工作日志涉及特定已标号三图不能扩展，无法排除所有7图分解。

**旧卡 → 建议变化：** 把“已知最多5个”改为“已构造5个，尚未由本轮核验最优性”。；AI部分packing阻碍单列，不改主问为反驳。

**直接证据与定位：**

- [West Hoffman-Singleton Decomposition](https://dwest.web.illinois.edu/openp/hoffsing.html)：Question及Comments/Partial results。访问层级：正文全文。
- [Meszka–Šiagiová covering construction](https://onlinelibrary.wiley.com/doi/pdf/10.1002/jcd.10049)：原刊题名/摘要。访问层级：仅检索摘要。
- [Codex Worklog](https://gist.github.com/siddhantdubey/22f22a7a23db5174ee59e32eaa8724aa)：West targets / Hoffman–Singleton部分。访问层级：正文相关节；工件未复跑。

**量词与适用范围：** K50的1225条边能否分成7个175边Hoffman–Singleton图。 已构造5个≠证明至多5个；特定部分packing不可扩展≠全局不可能。

**实际检索路径：**
- web.system1_search_query：`"K_50" "Hoffman" "seven" decomposition`（2026-11-26）。
- web.system1_search_query：`"Hoffman-Singleton" "decomposition" "seven" solved 2026`（2026-11-26）。
- web.system1_search_query：`site:github.com "Hoffman Singleton" "seven"`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_search_015.json, chunk_3_search_019.json, chunk_3_search_030.json, chunk_3_search_032.json, chunk_3_search_040.json, chunk_3_search_041.json。

**待复核：** 若有7份构造须取得每份边表并核边互斥覆盖；若有不可能证明须覆盖所有packings。

**最终补查补充。** [MSE #69399原帖及Douglas S. Stones的2011年回答](https://math.stackexchange.com/questions/69399/can-7-hoffman-singleton-graphs-cover-k-50)已读全文，辅助确认2003年五份packing是构造下界；历史回答不单独认证2026开放状态，也不证明七份不可能。

### QX-P-002263：单个abc-hit不是反例；新全文访问限制

**当前版本：** `dd3d194ce88ec9d2`。**本轮分类：** 完整证明/反例声明待核。

维持整数abc的争议证明口径。Scholze–Stix原报告与ZEN2026官方索引中LANA保留判断均重查；Soulé新稿仍只有弱指数声明。本卡“反例只需一个严格实例”错误：须固定正ε使所有常数都失效，单个abc-hit可被Kε吸收。

**旧卡 → 建议变化：** 修正“反例只需一个严格实例”为固定ε的无界族/无限例外。；注明LANA直开404、官方搜索可读与Soulé全文不可达的本轮层级，不复用旧卡全文已核声明。；维持争议/待核，弱指数与密度版本不当全解。

**直接证据与定位：**

- [Scholze–Stix, Why abc is still a conjecture](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf)：2018-07-16；p1 Conjecture1及开篇评价；后文IUT核心争点。访问层级：正文相关节。
- [ZEN Project LANA Interim Report官方公告](https://zen.ac.jp/news/zmcpostevent0717e)：2026-07-17；Current Status及Thm3.11→Cor3.12段。访问层级：官方搜索正文提取；直开404。
- [Soulé, On the abc conjecture](https://arxiv.org/abs/2611.05217)：2026-11-03；官方索引摘要。访问层级：仅标题/摘要；abs/pdf DisabledError。
- [LANA报告非官方转录检索](https://github.com/sfingali/joshi-abc-formalization/blob/main/docs/LANA_report_2026-07-16_fulltext.md)：非官方转录与状态笔记；原报告链接由E2官方公告给出。访问层级：入口与检索摘要；未取得固定提交完整主证明。

**量词与适用范围：** ∀ε>0∃Kε>0∀互素正整数a+b=c，c<Kε rad(abc)^{1+ε}。 量词顺序正确，但难度段把单个三元组误当反例；有限例外等价性反向通常使用ε/2等裕量。

**实际检索路径：**
- web.system1_search_query：`"abc conjecture" "Soulé" 2611.05217`（2026-11-26）。
- web.system1_search_query：`"abc conjecture" "LANA" "Scholze" 2026`（2026-11-26）。
- web.system1_search_query：`site:github.com abc conjecture LANA 2026`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_search_015.json, chunk_3_search_017.json, chunk_3_search_018.json, chunk_3_search_019.json, chunk_3_search_032.json, chunk_3_search_035.json, chunk_3_search_036.json, chunk_3_search_037.json, chunk_3_search_042.json, chunk_3_search_044.json。

**待复核：** 取得Soulé最新完整原稿与独立审查；核IUT/Joshi每个不同完整方案的具体后续，不用2018批评自动裁定新稿。；要声称形式化必须固定提交、核整数abc全部量词及依赖并独立重跑；本轮未执行。

### QX-P-002264：2026 RALI结果仍有附加条件；查重不可合并

**当前版本：** `8665c74a044acc68`。**本轮分类：** 部分进展。

原MO问有限可缩二维复形的无环子复形是否可缩，已核平衡子表现等价表述及超线性群条件结果。2026 Avramidi–Lück定理附带RALI基本群和tower假设，不能删去这些条件宣称原题已证；与Andrews–Curtis、Whitehead特例并非同题。

**旧卡 → 建议变化：** 补可缩/可塌、无环/单连通区别；新RALI结果标额外假设。；索引新增QX-P-002495 Whitehead一般猜想为待正文核线索，未合并。

**直接证据与定位：**

- [MO87342](https://mathoverflow.net/questions/87342/are-acyclic-subcomplexes-of-finite-contractible-2-complexes-contractible)：题干、平衡子表现重述、Muranov与Thom回答/评论。访问层级：正文相关节。
- [Avramidi–Lück 2026](https://arxiv.org/html/2602.04655v1)：§1.2 Conjecture1.1、Theorem1.2。访问层级：正文相关节。

**量词与适用范围：** 有限可缩二维simplicial复形Y中，连通且H1=H2=0的子复形X是否π1平凡/可缩。 无环不等于单连通，环境可缩不等于可塌；三维plus构造不是二维反例。

**实际检索路径：**
- web.system1_search_query：`"acyclic subcomplex" "contractible" 2026`（2026-11-26）。
- web.system1_search_query：`site:github.com "acyclic" "subcomplex" "contractible" conjecture`（2026-11-26）。
- web.system1_search_query：`"balanced" "subpresentation" "trivial" acyclic contractible 2-complex`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_search_015.json, chunk_3_search_017.json, chunk_3_search_030.json, chunk_3_search_032.json, chunk_3_search_034.json。

**待复核：** 取得Segev(4.3)与hyperlinear证明的已刊完整出处；核新RALI条件能否覆盖本题特定子类。

### QX-P-002265：固定提交确认主sorry；存在与收敛不等价

**当前版本：** `b66dccc4f9636c4a`。**本轮分类：** 部分进展。

重新核出版社搜索提取的§2、Thms1–3与§5，并取得固定提交Lean主声明和Roommates定义：主等式仍sorry，定义与完全严格偏好、单身rankN、至少k位改进一致。收敛阈值紧不能推出存在阈值紧。

**旧卡 → 建议变化：** 保留存在性/收敛区分；形式化记录更新为固定提交+主sorry。；将本轮论文访问写检索正文提取，不能复用旧轮PDF全读状态。

**直接证据与定位：**

- [Fanelli–Moscardelli, Approximately Stable Matching](https://journals.sagepub.com/doi/10.3233/FAIA251234)：§2、Theorems1–3、§5；DOI10.3233/FAIA251234。访问层级：检索返回正文相关节；full端点Timeout。
- [ApproximatelyStableMatching.lean 固定提交](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/Paper/ApproximatelyStableMatching.lean)：FanelliMoscardelli.stability_threshold_tight。访问层级：已取得完整代码/已核声明对应，未重跑。
- [Roommates.lean 固定提交](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjecturesForMathlib/Combinatorics/Roommates.lean)：CompleteProfile、IsKBlockingPair、stabilityThreshold。访问层级：已取得完整代码/静态核对应，未重跑。

**量词与适用范围：** 对所有完全严格偏好，允许单身的室友匹配，最小通用k稳定阈值K(N)是否最终=ceil(N/2)。 与二分稳定婚姻计数/随机阈值不同；作者§5提出N/2可能是真阈值，卡片的最终等式是精确定义后的任务版本。

**实际检索路径：**
- web.system1_search_query：`"Approximately Stable Matching" "threshold" 2026`（2026-11-26）。
- web.system1_search_query：`"Approximately stable" "roommates" "threshold" Fanelli Moscardelli ceil`（2026-11-26）。
- web.system1_search_query：`"approximately stable matching" Fanelli Moscardelli Lean AI proof counterexample`（2026-11-26）。
- 后续打开/代码/索引记录：chunk_3_index_log.jsonl, chunk_3_pinned_1.json, chunk_3_pinned_2.json, chunk_3_search_015.json, chunk_3_search_017.json, chunk_3_search_034.json, chunk_3_search_037.json。

**待复核：** 原刊小N枚举缺独立复现；主阈值下界须对所有充分大N，不能仅无穷子列或动力学循环。

### 查重新发现与配对结论

16个指定对子均读双方当前正文；没有据标题直接合并。关系：1对“特例/强化”（2255→000329），其余15对“相关但不等价”。两个新索引候选尚未取得对方全文：

| 本题版本 | 对方版本 | 关系 | 下一步 |
|---|---|---|---|
| QX-P-002255 `bbfd6a5636e5bffb` | QX-P-000331 `db90820ea7a09861` | 待定 | 索引题名精确指向EP40密度版本，与原题校准后疑同题；未取得对方全文，不越过索引级。 |
| QX-P-002264 `8665c74a044acc68` | QX-P-002495 `a2670bdd28053378` | 待定 | 索引为一般Whitehead非球面性猜想，与本题有可能的特例/强化关系；未取得对方正文，不确认等价或蕴含范围。 |

其中2257与000102、001192、2261分别是不同的列表/拟阵/均等染色问法；2263与000221、001244是条件应用或方法关联；2264与000496、000628的变换、无挠与无环子对象问题不同；2265与000438的室友通用存在阈值和随机二分婚姻计数不同。详见每行duplicates中的双版本、全文SHA256和具体理由。

## 6. 分析、几何、算法与末段25题的实质变化

### QX-P-002287 · Cramér 猜想：相邻素数间隙是否为 O((log p_n)^2)？

**当前版本：** `77c4f0fd287bc13c`。**主目标初查分类：** 暂未找到可验证结果。

**旧卡 → 变化。** 原渐近O(log²p)与常数1的强形式须继续分开。亲读Wang2605.14871v9（2026-11-23）发现Lemma2.5的明确小反例：n=4，A₃=(7−2)/3=5/3<g₃=2，但g₄=11−7=4并不小于g₃²=4。该版本不能作为主猜想的有效证明；这是反驳稿内引理，不是反驳Cramér猜想。

**建议修订。** 将2605.14871v9从笼统“待核”提升为“已发现明确引理反例”，附完整数字与定位。 其他未经取得/核验的Zenodo等声明不据此一并判错；常数1反例不否定big-O主句。

**直接证据与定位。**

- [预印本 / v9 2026-11-23；comments: attempt to revamp the proof](https://arxiv.org/abs/2605.14871)。读取层级：原始版本页。
- [预印本 / Definition2.1、Lemma2.5及Theorem2.6引用](https://arxiv.org/html/2605.14871v9)。读取层级：预印本正文。
- [预印本 / 11页PDF，与HTML交叉检查Lemma2.5](https://arxiv.org/pdf/2605.14871v9)。读取层级：预印本PDF。
- 本次直接数学检查：p1=2,p2=3,p3=5,p4=7,p5=11；A3=5/3,g3=2,g4=4；本地Fraction精确复算。

**范围。** 相邻素数间隙O((log p_n)²)主猜想。 子项分别为：Wang v9 Lemma2.5：原题已反驳。 作者核验及代码状态：未取得可对应原题的形式化证明；未独立重跑。

**实际检索路径。**

- system1_search_query：`"Cramer conjecture" "2026" "prime gaps"`（2026-11-26）。
- system2_search_query：`"prime gaps" "O" "log" "2605.14871"`（2026-11-26）。
- system2_search_query：`"Cramer" "conjecture" site:github.com proof 2026`（2026-11-26）。
- system2_search_query：`"Cramer conjecture" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.online OR "EulerSolve")`（2026-11-26）。

**待复核。** 其他完整声明仍需逐稿复核；主猜想本轮未得可验证证明或无界比值反例。

### QX-P-002269 · Bayesian 简单安全博弈能否精确计算 Bayes–Nash 均衡

**当前版本：** `67a01b916cc53d1b`。**主目标初查分类：** 完整证明/反例声明待核。

**旧卡 → 变化。** 新命中Kintali作者主页三份手稿；SecurityGames.pdf日期2026-11-20，Theorem1.1声称显式有理输入L位的精确BNE确定性O-tilde(L^4)算法，覆盖任意增长的类型/目标及零覆盖效应。原题作者v2仍称open，两者需并列；新闻所谓作者确认不冒充亲核。

**建议修订。** 由仅开放线索改为新增完整算法声明待核，链接作者PDF和主定理。 不要用Stackelberg或一般normal-form复杂度替代该结构化BNE问题。

**直接证据与定位。**

- [预印本 / §1–2；2026-11-21版本](https://arxiv.org/html/2610.08796v2)。读取层级：全文。
- [作者或机构原始页面 / PDF pp1–3, Theorem1.1](https://shivakintali.github.io/papers/SecurityGames.pdf)。读取层级：作者预印本主定理。
- [作者或机构原始页面 / 12页短证版本](https://shivakintali.github.io/papers/SecurityGames-short.pdf)。读取层级：已取得PDF入口。
- [作者或机构原始页面 / exists_isPolyTime_bayesNash](https://google-deepmind.github.io/formal-conjectures/src/FormalConjectures/Arxiv/%C2%AB2610.08796%C2%BB/BayesianSecurityGames/)。读取层级：形式化题面页面。

**范围。** 显式有理输入下精确Bayes–Nash均衡的确定性多项式算法。 作者核验及代码状态：已取得代码未重跑；未独立重跑。

**实际检索路径。**

- system1_search_query：`"Bayesian simple security games" polynomial equilibrium`（2026-11-26）。
- system2_search_query：`"Bayesian simple security games" "exact" "polynomial"`（2026-11-26）。
- system2_search_query：`Bayesian simple security games`；域名限制 aixiv.online（2026-11-26）。
- system2_search_query：`"Bayesian simple security games" (site:github.com OR site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org)`（2026-11-26）。
- 早期组合查询中的aixiv.org是入口拼写错误，仅保留实际执行痕迹；有效AI站点覆盖使用随后真实aixiv.online域的查询，不由错误入口推出无结果。

**待复核。** 核确定性位复杂度、退化收益、零先验类型及输出稀疏混合；未重跑算法或Lean。

### QX-P-002274 · 有界像归一化单叶函数的逆平方积分均值普遍谱是否等于 1

**当前版本：** `c38c1d3c7c7afaf5`。**主目标初查分类：** 完整证明/反例声明待核。

**旧卡 → 变化。** 原卡将全类B(-2)=1与有界类隔离为无法传递，遗漏Makarov关系在t=-2直接给B=Bb，也遗漏显式有界单叶见证f(z)=z−z²/2。新读Binder–Ivrii–Prause–Smirnov2610.23853给有界谱上界；结合本次核得β_f(-2)=1可对应本题完整等式。

**建议修订。** 修正“全类声称不回答有界类”的范围判断；登记有界谱完整证明声明待核。 保留FC bounded命题仍open/sorry的事实，但不能把标签当数学反证。

**直接证据与定位。**

- [预印本 / p1定义(3)、p2 Makarov恒等式(4)，主定理](https://arxiv.org/pdf/2610.23853)。读取层级：预印本正文。
- [形式化题面仓库 / brennan_universalSpectrumBounded](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/Wikipedia/Brennanconjecture.lean)。读取层级：已取得代码未重跑。
- 本次直接数学检查：f=z−z²/2：|f|<3/2；f(z1)=f(z2)且z1≠z2迫使z1+z2=2不可能；∫|1−re^{iθ}|^-2 dθ=2π/(1−r²)，β(-2)=1。

**范围。** 有界像单叶函数普遍谱B_b(-2)=1。 子项分别为：有界类下界B_b(-2)≥1：原题已证；有界/全类的范围对应：题面有误。 作者核验及代码状态：已取得代码未重跑；未独立重跑。

**实际检索路径。**

- system2_search_query：`"Brennan" "bounded" "spectrum" "-2" 2026`（2026-11-26）。
- system2_search_query：`"inverse-square" "integral means" "bounded"`（2026-11-26）。
- 形式化题面仓库：`https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/Wikipedia/Brennanconjecture.lean`（2026-11-26）。
- system2_search_query：`"Brennan" (site:mathoverflow.net OR site:aixiv.org OR site:zenodo.org OR "ProofForum") "bounded"`（2026-11-26）。
- 早期组合查询中的aixiv.org是入口拼写错误，仅保留实际执行痕迹；有效AI站点覆盖使用随后真实aixiv.online域的查询，不由错误入口推出无结果。

**待复核。** 全文上界证明及依赖仍未逐行审计/重跑；不写成本会话独立解决Brennan。

### QX-P-002288 · 四维 De Giorgi 单调解刚性命题的 2026 预印本声称是否成立

**当前版本：** `226c5c147b3911e2`。**主目标初查分类：** 完整证明/反例声明待核。

**旧卡 → 变化。** 原卡Liu等2609.21680声明确认存在，arXiv原页不可达，镜像可取得43页PDF首部但后续定位超时。新增Chan–Fernández-Real–Figalli–Florit-Simon–Serra2609.30194v1（2026-09-24），作者提交的CVGMT页及18页原PDF均明确得到四维单调解刚性。这是新的完整证明来源，需与free-boundary版本和附加能量增长的四维stable结论区分。

**建议修订。** 在验证轨道并列补2609.30194，不把已有多个来源当本次独立验证通过。 Formal Conjectures DeGiorgi_four仍open/sorry是代码事实；不能据此否认新预印本。

**直接证据与定位。**

- [预印本 / Liu等43页镜像，首页摘要；后续find/open超时](https://borowiecki.dev/pdf/2609.21680)。读取层级：原稿镜像，定理细节未成功定位。
- [预印本 / v1 2026-09-24，PDF p2 Theorem1.1、p3 Corollary1.2（四维单调刚性，无附加端点极限）](https://arxiv.org/pdf/2609.30194)。读取层级：原始预印本全文。
- [作者或机构原始页面 / 2026-10-03由Florit-Simon创建的论文页](https://cvgmt.sns.it/paper/8042/)。读取层级：作者发布页。
- [形式化题面仓库 / DeGiorgi_four；blob959aa16dd95513437c43fa9d36df5699ac29cdca](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/Paper/DeGiorgi.lean)。读取层级：已取得代码未重跑。
- [作者仓库/代码 / thm:monotone：八维无额外能量/端点假设；导言提及LLWWW/CFFFS](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/De-Giorgis-conjecture-in-dimension-eight-September-26-2026/build/sections/00-introduction.tex)。读取层级：作者源码；四维可常坐标延拓到八维，此归约不构成独立证明审计。

**范围。** 四维有界整Allen–Cahn严格单调解的一维刚性。 作者核验及代码状态：已取得代码未重跑；未独立重跑。

**实际检索路径。**

- system1_search_query：`"De Giorgi" "2609.21680"`（2026-11-26）。
- system2_search_query：`"stable" "Allen-Cahn" "four" "Liu" 2026`（2026-11-26）。
- system2_search_query：`"DeGiorgi" site:github.com 2609.21680`（2026-11-26）。
- system2_search_query：`"De Giorgi" "four" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.online OR "ProofForum")`（2026-11-26）。

**待复核。** 逐行核新的稳定刚性证明、单调维数提升与有界整解值域归约；本次未深审。

### QX-P-002289 · Dean 猜想剩余的 k=5 情形

**当前版本：** `cce6def1a40d053f`。**主目标初查分类：** 完整证明/反例声明待核。

**旧卡 → 变化。** 2026-01/05 arXiv原稿确实留下k5，但本轮找到两项后续完整声明：Botsford Zenodo22182448 v1.0.1及Sieniawski作者仓库Dean's conjecture at five。后一固定提交的论文、README和DeanK5Solution.lean给与原题吻合的非空有限简单图/最小度≥5/圈长整除5接口，并公开全AI生成声明；未审依赖、未重跑，不能升级原题已证。

**建议修订。** 撤去“未发现可靠后续完整声明”的断言，进入完整声明待核。 原题显式补非空图，或约定空图minDegree=0，与形式化一致。 区分Botsford计算辅助证书与Sieniawski Lean项目两条证据链，不混称一次独立核验。

**直接证据与定位。**

- [预印本 / v1 2026-01-20，k≥6范围](https://arxiv.org/abs/2601.13552)。读取层级：原始摘要/版本。
- [预印本 / v1 2026-05-04，k≠5已知、仅k3/4强化](https://arxiv.org/abs/2605.02731)。读取层级：原始摘要/版本。
- [作者存储库声明 / 2026-08-31 version1.0.1；9项计算辅助配置；PDF下载429](https://zenodo.org/records/22182448)。读取层级：作者预印本声明页。
- [作者仓库/代码 / Abstract、§1.3、§8；blob b67e02d96fa8b3476627278d297d9be6b6dca58b](https://github.com/pkchv/dean-conjecture/blob/eee0a3f0a1fdc42f11d93bec1a64957f4e5511b4/paper/Dean_conjecture_k5.md)。读取层级：作者仓库论文。
- [作者仓库/代码 / DeanK5.Comparator.dean_conjecture_k5；import DeanK5.FinalDeduction](https://github.com/pkchv/dean-conjecture/blob/eee0a3f0a1fdc42f11d93bec1a64957f4e5511b4/DeanK5Solution.lean)。读取层级：已核顶层题意对应、依赖未全审、未重跑。

**范围。** 非空有限简单图最小度≥5必含圈长被5整除的圈。 子项分别为：空图边界：题面有误。 作者核验及代码状态：已核定理对应、未重跑；未独立重跑。

**实际检索路径。**

- system1_search_query：`"Dean" "conjecture" "k=5" cycles 2026`（2026-11-26）。
- system1_search_query：`"minimum degree five" cycle length divisible five proof`（2026-11-26）。
- 作者仓库/代码：`https://github.com/pkchv/dean-conjecture/blob/eee0a3f0a1fdc42f11d93bec1a64957f4e5511b4/paper/Dean_conjecture_k5.md`（2026-11-26）。
- system2_search_query：`"Dean" "five" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.online OR "EulerSolve")`（2026-11-26）。

**待复核。** 完整审计COY/GHLM/BGLP内部依赖和公理导出；Botsford计算补充22167084本轮未执行。

### QX-P-002286 · 凸万有覆盖的单位弧最小面积是多少

**当前版本：** `093c45ac5a29480b`。**主目标初查分类：** 部分进展。

**旧卡 → 变化。** Keller2609.21968v1 Theorem1.1给0.239≤α≤7170601298323360123534337/29109471743520000000000000，并报告Lean验证，但§2明确允许O(2)反射；现卡只允许保向运动。因此下界可传到现卡，0.246332…上界对现卡须另补保向覆盖证明，不能直接照录。精确最优值仍未给出。

**建议修订。** 把论文E(2)版本与题卡SE(2)版本分别命名；保留主题保向定义时暂不将该上界认作完全对应。 作者README核验时间/axiom报告均标他人声称；本次只读取，未运行。

**直接证据与定位。**

- [预印本 / v1，p2 Theorem1.1；p3 Definition2.2/E(2)；p11 Theorem4.1；§5作者形式化报告](https://arxiv.org/pdf/2609.21968)。读取层级：预印本全文。
- [作者仓库/代码 / MoserWorm.bounds及复现指令，README blob255599d2f93562d7bd21ea43a716569576092b1b](https://github.com/ethan-keller/moser-worm-improved-bounds/blob/9a3394130fe4f7b1df6ffdeffda16601795d9ce4/README.md)。读取层级：作者仓库说明，未取得全部证明、未重跑。

**范围。** 只允许平移旋转的凸单位弧万有覆盖精确最小面积。 子项分别为：Keller论文的E(2)版本：部分进展。 作者核验及代码状态：他人声称已形式化验证；未独立重跑。

**实际检索路径。**

- system1_search_query：`"Moser worm" "2609.21968"`（2026-11-26）。
- system2_search_query：`"universal convex covers" "unit arcs" 2026 theorem`（2026-11-26）。
- 作者仓库/代码：`https://github.com/ethan-keller/moser-worm-improved-bounds/blob/9a3394130fe4f7b1df6ffdeffda16601795d9ce4/README.md`（2026-11-26）。
- system2_search_query：`"Moser worm" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.online OR "ProofForum")`（2026-11-26）。

**待复核。** 核上界验证器是否只使用旋转或能提供从E(2)到SE(2)的补充归约；精确α未定。

### QX-P-002270 · 宾–博苏克猜想：齐性可度量 ANR 是否必为同维拓扑流形

**当前版本：** `1df53c020a7aba12`。**主目标初查分类：** 题面有误。

**旧卡 → 变化。** 题面未列可分，边界说明又误把可度量性当作可分性，却要求结论第二可数。非可数离散集D×R^n即齐性可度量n维ANR而不第二可数，故字面全称不成立。对通常可分/局部紧版本，补到Bryant–Ferry在2018/2019官方报告宣布n≥6反例，2025 Valov论文摘要也提及修订稿，旧卡“未发现任何完整声明”应撤。

**建议修订。** 补明可分/第二可数及局部紧约定，并区分字面反例与经典Bing–Borsuk猜想。 记录Bryant–Ferry高维反例公开声明待核；不能仅据旧综述或Lean open标签维持无声明判断。

**直接证据与定位。**

- [作者或机构原始页面 / 2018-04-27报告摘要](https://www.math.fsu.edu/~mio/colloquium17-18/bryant.math)。读取层级：官方作者报告。
- [作者或机构原始页面 / Steve Ferry plenary abstract](https://e.math.cornell.edu/sites/topology/2019/talks.php)。读取层级：官方报告。
- [作者或机构原始页面 / Valov 2025引言搜索摘要，DOI10.1016/j.topol.2025.109259](https://www.sciencedirect.com/science/article/pii/S0166864125000574)。读取层级：仅搜索摘要；直开403。
- 本次直接数学检查：D非可数离散，X=D×R^n；拓扑和各分量均为R^n，局部可缩、可度量、ANR；非可数个不交开集排除第二可数。

**范围。** 按当前题卡允许不可分但要求第二可数流形的字面命题。 子项分别为：当前字面全称命题的反例：原题已反驳；经典可分Bing–Borsuk版本：完整证明/反例声明待核。 作者核验及代码状态：未取得可对应原题的形式化证明；未独立重跑。

**实际检索路径。**

- system1_search_query：`"Bing-Borsuk" "separable" "locally compact"`（2026-11-26）。
- system1_search_query：`"Bing-Borsuk" conjecture 2026 homogeneous ANR`（2026-11-26）。
- system2_search_query：`Bing Borsuk`；域名限制 aixiv.online（2026-11-26）。
- system2_search_query：`"Bing-Borsuk" (site:github.com OR site:aixiv.org OR site:zenodo.org OR "ProofForum")`（2026-11-26）。
- 早期组合查询中的aixiv.org是入口拼写错误，仅保留实际执行痕迹；有效AI站点覆盖使用随后真实aixiv.online域的查询，不由错误入口推出无结果。

**待复核。** 取得Bryant–Ferry修订稿并核齐性构造，n=3,4,5不得由n≥6反例推断已解决。

### QX-P-002273 · 整系数多项式的对数 Mahler 测度值集是否随变量数严格增大

**当前版本：** `f8901a09b37a09bc`。**主目标初查分类：** 暂未找到可验证结果。

**旧卡 → 变化。** 主要严格层次问题本次未见可验证解决；但旧卡的L0={0}、m(1+X)=log2均错误。按本卡定义，L0={log m:m≥1整数}，m(1+X)=0；L0严格包含于L1可用X²−X−1的测度log((1+√5)/2)见证。

**建议修订。** 修正零变量值集与例子；不要把显式高变量测度公式当作严格分层证明。

**直接证据与定位。**

- [形式化题面仓库 / intLogMahlerSet定义；strict_hierarchy定理仍sorry](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/Wikipedia/MultivariableMahlerMeasure.lean)。读取层级：已取得代码未重跑。
- [预印本 / v2 2026-01-07摘要仅motivic regulator/Dirichlet L值](https://arxiv.org/abs/2510.21515)。读取层级：摘要；HTML/PDF v2未取得。
- 本次直接数学检查：常数的积分是log|c|；Jensen根公式计算1+X及X²−X−1。

**范围。** 所有n≥1的变量层级L_n严格包含于L_(n+1)。 子项分别为：L0与两个示例：题面有误；题外零变量边界L0⊊L1：题面有误。 作者核验及代码状态：已取得代码未重跑；未独立重跑。

**实际检索路径。**

- system2_search_query：`"Mahler measure" "L_n" "strict" Boyd`（2026-11-26）。
- system2_search_query：`"Mahler measure" "number of variables" "2510.21515"`（2026-11-26）。
- 形式化题面仓库：`https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/Wikipedia/MultivariableMahlerMeasure.lean`（2026-11-26）。
- system2_search_query：`"Mahler" "hierarchy" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR "ProofForum")`（2026-11-26）。
- 早期组合查询中的aixiv.org是入口拼写错误，仅保留实际执行痕迹；有效AI站点覆盖使用随后真实aixiv.online域的查询，不由错误入口推出无结果。

**待复核。** 严格层次猜想的原始首出处仍需精确页码；Boyd1981不能仅由后世注释定位。

### QX-P-002281 · 高维双曲空间是否存在由有限阶等距生成的余紧离散群

**当前版本：** `5be716bf95b955f6`。**主目标初查分类：** 暂未找到可验证结果。

**旧卡 → 变化。** 卡把∃N∀n≥N与任意大维数∀N∃n≥N写成等价，实际前者更强。原MO102644问n很大时的余紧torsion-generated作用；发问者是Anton Petrunin，Greg Kuperberg为编辑者。有限阶生成与商单连通在原帖被明确称等价，不宜只因原帖未附证明而删除。现有算术Kleinian、Vinberg反射算法及抽象双曲群结果不解决全部高维余紧晶格。

**建议修订。** 拆开“所有充分大维数”和“无界维数族”两个量词；保留原帖措辞并待精确择定。 原作者改Anton Petrunin（2012-07-19），Kuperberg列编辑者。 将商单连通等价的Armstrong商空间基本群定理列为需补精确引用，而不是凭未附证明否定。

**直接证据与定位。**

- [原始社区问题/回答 / 主问、署名和2012-07评论](https://mathoverflow.net/questions/102644/actions-on-%E2%84%8D%E2%81%BF-generated-by-torsion-elements)。读取层级：原帖全文。
- [预印本 / v2 2017-07-07，算术三维Kleinian有限性](https://arxiv.org/abs/1610.06147)。读取层级：原始摘要。
- [预印本 / v2 2022-07-13，Vinberg反射子晶格算法](https://arxiv.org/abs/2206.01282)。读取层级：原始摘要。
- [预印本 / v2 2018-09-09，抽象双曲群子类而非全部Hⁿ晶格](https://arxiv.org/abs/1710.05684)。读取层级：原始摘要。

**范围。** 高维Hⁿ中由有限阶元素生成的余紧离散群的一般存在性。 子项分别为：量词及原帖署名：题面有误。 作者核验及代码状态：未取得可对应原题的形式化证明；未独立重跑。

**实际检索路径。**

- system1_search_query：`"hyperbolic" "generated by torsion" cocompact arbitrarily large dimensions`（2026-11-26）。
- system2_search_query：`"102644" "torsion" hyperbolic`（2026-11-26）。
- system2_search_query：`"torsion" "cocompact" "hyperbolic" site:github.com`（2026-11-26）。

**待复核。** 量词不等价可直接纠正；主存在性未找到可验证完整解，商基本群等价需补原定理定位。

### QX-P-002282 · 验证 Colton 猜想：refactorable 数是否至少有多半数素数那么多

**当前版本：** `04461d03865923ad`。**主目标初查分类：** 完整证明/反例声明待核。

**旧卡 → 变化。** 亲读Jack作者仓库固定提交391a42a的论文源文件与README：Theorem1明确n≥1，三段计算/解析覆盖n≤10^10、[10^10,2.07×10^13]、x≥2×10^13，边界相接。独立复算及referee等措辞均是作者报告，本会话未执行。额外“等号仅n=7”须保留n≥1；形式化主句若沿用Nat包含0，则等号还在0成立。

**建议修订。** 维持验证轨道，补固定提交、thm:main与三段覆盖范围。 将额外等号结论写成n≥1⇒(π(n)=2T(n)↔n=7)，或全Nat下n∈{0,7}。 Zenodo入口未取得，不把OEIS数值收录或PR标签修改当正式审稿。

**直接证据与定位。**

- [作者仓库/代码 / thm:main；Sections Part1/2/3](https://github.com/leandrejack-afk/colton-conjecture/blob/391a42aacaeb39b31ae290e406f1be4b60a1f8d0/paper/colton-note.tex)。读取层级：作者预印本源码。
- [作者仓库/代码 / Proof/Checks；blob bcddc05942e76d133e4c2aae81f96bde78a90e89](https://github.com/leandrejack-afk/colton-conjecture/blob/391a42aacaeb39b31ae290e406f1be4b60a1f8d0/README.md)。读取层级：作者仓库，未重跑。
- [作者或机构原始页面 / §2.3 计数猜想](https://cs.uwaterloo.ca/journals/JIS/colton/joisol.html)。读取层级：原始论文网页。
- [已刊论文 / 2002论文摘要；网页注明2003-02-17 corrections](https://cs.uwaterloo.ca/journals/JIS/VOL5/Zelinsky/zelinsky9.html)。读取层级：已刊摘要与版本页。
- [形式化题面仓库 / colton_conjecture仍research open/sorry](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/OEIS/111291.lean)。读取层级：已取得代码未重跑。

**范围。** π(n)≤2T(n)的Colton主不等式验证。 子项分别为：等号仅n=7的定义域：题面有误。 作者核验及代码状态：已取得代码未重跑；未独立重跑。

**实际检索路径。**

- system1_search_query：`"Colton conjecture" "Jack" refactorable`（2026-11-26）。
- system2_search_query：`"refactorable" "pi" "2" "2026" conjecture`（2026-11-26）。
- 作者仓库/代码：`https://github.com/leandrejack-afk/colton-conjecture/blob/391a42aacaeb39b31ae290e406f1be4b60a1f8d0/paper/colton-note.tex`（2026-11-26）。
- system2_search_query：`"Colton" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.online OR "EulerSolve" OR "ProofForum")`（2026-11-26）。

**待复核。** 复核分段筛、所有素数处最小差、生成元枚举与定向数值误差；本次没有执行计算。

### QX-P-002266 · Archdeacon 整数 Heffter 阵列猜想：部分填充阵列的完整存在条件

**当前版本：** `296583ae3cfa389d`。**主目标初查分类：** 部分进展。

**旧卡 → 变化。** 2025预印本Theorem C确认整数矩形Heffter阵列的已解参数范围，未封闭k=3,5互素残余族。卡首条把整数集合Ω与−Ω的并写成正整数集合{1,…,2nk}，并称等价于绝对值半集，这在Z中矛盾；该笔误确实也出现于2510.08302v1摘要及正文，已看PDF截图，不能机械继承。

**建议修订。** 将定义改为{|a|:a∈Ω}={1,…,nk}且绝对值各出现一次，或Ω⊔(−Ω)={±1,…,±nk}。 保留一般矩形整数分支的部分进展，relative/signed magic不冒充主猜想完成。

**直接证据与定位。**

- [预印本 / §6, Conjecture 6.3, PDF p15](https://arxiv.org/pdf/1412.0949)。读取层级：全文定位。
- [预印本 / p1定义及p3 Theorem C, Problems 1–2](https://arxiv.org/pdf/2510.08302)。读取层级：全文定位并截图核公式。

**范围。** 校准绝对值定义后的整数矩形Heffter阵列一般存在性。 子项分别为：题面定义的正负集合：题面有误。 作者核验及代码状态：未取得可对应原题的形式化证明；未独立重跑。

**实际检索路径。**

- system2_search_query：`"Archdeacon" "integer Heffter arrays" conjecture 2026`（2026-11-26）。
- system2_search_query：`"Heffter" "k=3,5" Morini Pellegrini`（2026-11-26）。
- system2_search_query：`"Heffter" site:github.com proof conjecture`（2026-11-26）。
- system2_search_query：`"Heffter" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR "EulerSolve" OR "ProofForum")`（2026-11-26）。
- 早期组合查询中的aixiv.org是入口拼写错误，仅保留实际执行痕迹；有效AI站点覆盖使用随后真实aixiv.online域的查询，不由错误入口推出无结果。

**待复核。** 逐项审计剩余k=3,5构造及最新相关工作，不以初查零命中推出开放。

### QX-P-002272 · 次数与系数高度同步有界的多项式能否连续取素数值

**当前版本：** `e341319c262b7fb1`。**主目标初查分类：** 暂未找到可验证结果。

**旧卡 → 变化。** 原帖明确0≤a_i≤M；卡接着改述为|a_i|≤M，错误引入负系数。主公式和原帖一致，原帖当前可读页面未列出解决答案，不能据此证明开放。

**建议修订。** 删去错误“等价地绝对值不超过M”，写“各非常数系数在0至M之间”。

**直接证据与定位。**

- [原始社区问题/回答 / 主问及nonconstant coefficients between0 andM](https://mathoverflow.net/questions/512119/do-there-exist-polynomials-of-degree-and-height-m-taking-prime-values-at-1-2)。读取层级：原帖全文。

**范围。** 0≤a_i≤M、次数及高度同步约束的连续取素值存在性。 子项分别为：非负高度与绝对值高度的等价改述：题面有误。 作者核验及代码状态：未取得可对应原题的形式化证明；未独立重跑。

**实际检索路径。**

- system2_search_query：`"bounded height" "polynomials" "prime values" 512119`（2026-11-26）。
- system2_search_query：`"f(0)=1" "M" polynomial primes coefficients`（2026-11-26）。
- system2_search_query：`bounded height polynomial prime values`；域名限制 aixiv.online（2026-11-26）。
- system2_search_query：`"bounded height" "prime values" (site:arxiv.org OR site:github.com OR site:zenodo.org)`（2026-11-26）。

**待复核。** 主全称S(M)>0仍未找到可验证解；检索中无关素数生成器不适用。

### QX-P-002276 · 标准 C² 中单调 Lagrangian T² 的 Clifford–Chekanov 分类

**当前版本：** `2c5ba57d07cebb99`。**主目标初查分类：** 暂未找到可验证结果。

**旧卡 → 变化。** Polterovich–Schlenk 2406.15967v2 的 Open Problem4 明确允许 Clifford 与 Chekanov 两者的缩放。现卡只给 Clifford 参数a，却把 Chekanov写成一个固定标准环面，未匹配单调常数λ。修正后的C²全称分类本轮未找到可验证解决。

**建议修订。** 将两个模型均写成与L单调常数相同的缩放；Hamiltonian同痕保持面积/Maslov比例。 其他辛流形中的exotic tori不能直接当C²分类反例。

**直接证据与定位。**

- [预印本 / v2，打印p11，Open Problem4](https://arxiv.org/pdf/2406.15967)。读取层级：原作者综述全文定位。

**范围。** 允许单调尺度变化的Clifford–Chekanov Hamilton同痕分类。 子项分别为：Chekanov模型尺度：题面有误。 作者核验及代码状态：未取得可对应原题的形式化证明；未独立重跑。

**实际检索路径。**

- system2_search_query：`"monotone Lagrangian tori" "C2" "classification" 2026`（2026-11-26）。
- system2_search_query：`"monotone Lagrangian tori" "Hamiltonian isotopy" "standard"`（2026-11-26）。
- system2_search_query：`monotone Lagrangian tori Clifford Chekanov`；域名限制 aixiv.online（2026-11-26）。
- system2_search_query：`"monotone Lagrangian tori" (site:github.com OR site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org)`（2026-11-26）。
- 早期组合查询中的aixiv.org是入口拼写错误，仅保留实际执行痕迹；有效AI站点覆盖使用随后真实aixiv.online域的查询，不由错误入口推出无结果。

**待复核。** 标准模型缩放记号必须写清；未核得本题完整新证明/反例。

### QX-P-002285 · 任意进制的合数重素数能否只改一位得到素数

**当前版本：** `12b4f74403b8181c`。**主目标初查分类：** 暂未找到可验证结果。

**旧卡 → 变化。** 原MO516812的主问与卡全称公式吻合；未找到可验证全进制解。卡解释中的平方底数因式分解漏掉(c+1)：R_n(c²)=R_n(c)(c^n+1)/(c+1)，并非简单乘积；“平方底数所有n≥2均合数”被R₂(4)=5反驳。此修正不反驳主问要求n≥3且母数合数的命题。

**建议修订。** 修正背景因式分解并删去错误普遍合数断言。 原帖某索引显示2 answers，但实际打开页只得主问，无答案正文；不能报已审两答。

**直接证据与定位。**

- [原始社区问题/回答 / 主问n≥3、1≤k≤n−2及母数合数](https://mathoverflow.net/questions/516812/composite-repunits-and-near-repunit-primes-across-arbitrary-bases)。读取层级：原帖全文（答案未返回）。
- 本次直接数学检查：c=2,n=2：R₂(4)=5，而R₂(2)(2²+1)=15；正确恒等式含除以c+1。

**范围。** 任意进制存在满足原帖内部单比特改动的合数重素数及素数。 子项分别为：平方底数的背景恒等式：题面有误。 作者核验及代码状态：未取得可对应原题的形式化证明；未独立重跑。

**实际检索路径。**

- system1_search_query：`"composite repunits" "near-repunit" primes`（2026-11-26）。
- system2_search_query：`"R_n(b)" "b^k" prime composite repunit`（2026-11-26）。
- system2_search_query：`"near-repunit" site:github.com`（2026-11-26）。

**待复核。** 需再次取得原帖答案区并逐一评估；本轮没有覆盖任意进制的证明/反例。

### QX-P-002284 · 每个紧 Hausdorff 空间是否是齐性紧空间的连续像

**当前版本：** `53e30ff5507d6b2b`。**主目标初查分类：** 暂未找到可验证结果。

**旧卡 → 变化。** 已通过MathNet取得Arhangel'skii2013原文：打印p42 Problem14，p38约定compact=compact Hausdorff，和本卡吻合。该页仅指出可度量紧空间是Cantor像，不能把全部紧空间替换为dyadic。最新正式代码仍是research open/sorry，不单凭标签证明开放。 另发现当前题卡空目标空间的边界例子错误：若允许X=∅，只能取Y=∅才有满射，单点源空间到空目标不存在函数。

**建议修订。** 补精确页码p42 Problem14及p38分离性约定；原math.md连续超时，改留可达MathNet期刊入口。 修正空空间分支：X=∅时取Y=∅；若约定空间一律非空则删去该分支。

**直接证据与定位。**

- [已刊论文 / 2013打印p42 Problem14，p38约定](https://www.mathnet.ru/php/getFT.phtml?jrnid=basm&option_lang=rus&paperid=344&what=fullt)。读取层级：已刊全文。
- [形式化题面仓库 / homogeneousSpace_exists_surjective](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/Paper/Homogenous.lean)。读取层级：已取得代码未重跑。

**范围。** 任意紧Hausdorff空间是齐性紧Hausdorff空间连续像。 子项分别为：空目标空间边界：题面有误。 作者核验及代码状态：已取得代码未重跑；未独立重跑。

**实际检索路径。**

- system1_search_query：`"compact Hausdorff" "continuous image" "homogeneous" problem`（2026-11-26）。
- system2_search_query：`"compact Hausdorff" "homogeneous" "Arhangelskii" "2013" 37 46`（2026-11-26）。
- system2_search_query：`"Homogenous.lean" compact continuous image`（2026-11-26）。
- system2_search_query：`"homogeneous compact" "continuous image" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.online)`（2026-11-26）。

**待复核。** 一般紧Hausdorff主命题在本次列出的学术/社区入口未找到可验证解决；不能由零命中断定开放。

### QX-P-002280 · Černý 猜想：同步自动机的最短复位字长度

**当前版本：** `ee224043d6033676`。**主目标初查分类：** 部分进展。

**旧卡 → 变化。** 一般Černý二次界本轮未找到可验证完整解。新增Zhu2607.19675v1：Theorem2.4声称全部one-cluster同步自动机满足rt≤(m−1)(n−1)+mℓ≤(n−1)²，边界m=1与ℓ=0另处理；这是重要子类声明，不能封闭任意DFA。 另通过aiXiv追到Borisov的Hexagon2611.00932v1（11月23日）及作者仓库：Thm1.1声称(7/48−δ)n³，仍为三次界；aiXiv题目页的claimed resolved标签把one-cluster特例提升为一般问题，不能采信该标签。

**建议修订。** 补录one-cluster全子类声明及Theorem2.3/2.4范围，保持一般主问题与子类分开。 增加11月三次系数改进声明；平台总标签不能覆盖主定理的子类限制。

**直接证据与定位。**

- [预印本 / §2 Theorems2.3/2.4及边界讨论](https://arxiv.org/html/2607.19675v1)。读取层级：预印本正文。
- [预印本 / Shitov一般三次上界](https://arxiv.org/abs/1901.06542)。读取层级：原始摘要。
- [公开AI索引 / Status及Results；claimed resolved所指2609.00160仅one-cluster](https://aixiv.online/problems/cerny-conjecture)。读取层级：AI索引页面，已打开。
- [预印本 / v1 2026-11-23，p2 Theorems1.1–1.2；24页](https://hexagonmath.org/pdf/2611.00932)。读取层级：作者预印本全文。
- [作者仓库/代码 / General Cubic Upper Bounds；What Remains Open；Cerny/StatementCheck.lean为作者所列审计路径](https://github.com/antonborisov571/cerny-lean/blob/cce904976550e15a378a13e424f2bf3ca7eea9c2/README.md)。读取层级：作者README已读；未取得全部证明、未重跑。

**范围。** 任意n状态同步DFA的复位阈值≤(n−1)²。 子项分别为：one-cluster与新三次界：完整证明/反例声明待核；AI索引汇总标签：题面有误。 作者核验及代码状态：他人声称已形式化验证；未独立重跑。

**实际检索路径。**

- system1_search_query：`"Cerny" conjecture solved 2026`（2026-11-26）。
- system1_search_query：`"Černý" "annular spectral"`（2026-11-26）。
- 作者仓库/代码：`https://github.com/antonborisov571/cerny-lean/blob/cce904976550e15a378a13e424f2bf3ca7eea9c2/README.md`（2026-11-26）。
- system2_search_query：`Cerny conjecture`；域名限制 aixiv.online（2026-11-26）。
- system2_search_query：`"Cerny" (site:github.com OR site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR "ProofForum") conjecture proof`（2026-11-26）。
- 早期组合查询中的aixiv.org是入口拼写错误，仅保留实际执行痕迹；有效AI站点覆盖使用随后真实aixiv.online域的查询，不由错误入口推出无结果。

**待复核。** one-cluster新证明未逐行核验；没有运行其代码、验证器或Lean。 新三次界及作者声称Lean证明未独立审计或运行；所读README不等于已核全部定理依赖。

### QX-P-002267 · 平衡素数是否有无穷多个

**当前版本：** `d0cc3c9b4925ac5f`。**主目标初查分类：** 暂未找到可验证结果。

**旧卡 → 变化。** 连续三个素数构成等差数列的无穷性，本轮未找到可验证完整解。亲读Formal Conjectures文件仍是research open/sorry；2026社区回复明确仍开放。整数除法形式在n=0有额外例(2+5)/2=3，只与原定义的无穷性等价，不是逐指标完全相同。

**建议修订。** 将“只差指标平移”修为除去有限的初始整数除法例外后等价；勿把Green–Tao非连续等差素数定理当解。

**直接证据与定位。**

- [形式化题面仓库 / BalancedPrimes.balanced_primes；文件blob c013d850ed260385e8468a81835a9d3eaf5756a2](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/Wikipedia/BalancedPrimes.lean)。读取层级：已取得代码未重跑。
- [原始社区问题/回答 / answer n=2讨论](https://mathoverflow.net/questions/515079/linear-equations-with-consecutive-primes/515082)。读取层级：社区原帖。

**范围。** 无限多个连续三素数等差组。 子项分别为：与Nat整数除法形式的对应：题面有误。 作者核验及代码状态：已取得代码未重跑；未独立重跑。

**实际检索路径。**

- system2_search_query：`"balanced primes" infinitely many consecutive arithmetic progression proof`（2026-11-26）。
- system1_search_query：`"balanced primes" proof arxiv`（2026-11-26）。
- 形式化题面仓库：`https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/Wikipedia/BalancedPrimes.lean`（2026-11-26）。
- system2_search_query：`"balanced prime" (site:zenodo.org OR site:aixiv.org OR "EulerSolve" OR "ProofForum")`（2026-11-26）。
- 早期组合查询中的aixiv.org是入口拼写错误，仅保留实际执行痕迹；有效AI站点覆盖使用随后真实aixiv.online域的查询，不由错误入口推出无结果。

**待复核。** OEIS A006562打开403；未重跑形式化，社区说明不是完整文献证明。

### QX-P-002290 · 第十个 Dedekind 数 M(10) 的精确值是什么

**当前版本：** `21be4c0a79f0433d`。**主目标初查分类：** 部分进展。

**旧卡 → 变化。** 2611.13887主摘要只给M10≡106mod210；2606.09795/2607.08446主摘要都是统计估计，不能填精确整数。正式FC当前Dedekind_10.answer仍sorry。原题精确值本轮未找到可验证结果；“自由分配格”需说明含0,1的有界格约定。

**建议修订。** 维持精确整数验收，不把统计误差写成严格区间或值。 若保留自由分配格等价表述，写明有界分配格；无常数运算的自由分配格通常少两个常值元素（n≥1）。

**直接证据与定位。**

- [预印本 / 2026-11-10；M10≡106(mod210)](https://arxiv.org/abs/2611.13887)。读取层级：官方学术搜索摘要；直开abs/PDF均DisabledError。
- [预印本 / Monte Carlo估计(8.9360±0.0010)×10^78](https://arxiv.org/abs/2606.09795)。读取层级：官方学术搜索摘要；直开DisabledError。
- [预印本 / D10四位有效数字统计估计](https://arxiv.org/abs/2607.08446)。读取层级：官方学术搜索摘要；直开DisabledError。
- [形式化题面仓库 / Dedekind_10与答案占位；blob393ea27901c1c99b60e266ea1fa255a47ea83578](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/Wikipedia/DedekindNumber.lean)。读取层级：已取得代码未重跑。

**范围。** 第十个Dedekind数M(10)的精确整数值。 子项分别为：自由分配格的等价解释：题面有误。 作者核验及代码状态：已取得代码未重跑；未独立重跑。

**实际检索路径。**

- system1_search_query：`"Dedekind" "M(10)" exact 2026`（2026-11-26）。
- system1_search_query：`"2611.13887" Dedekind congruences`（2026-11-26）。
- 形式化题面仓库：`https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/Wikipedia/DedekindNumber.lean`（2026-11-26）。
- system2_search_query：`"Dedekind" "10" (site:github.com OR site:mathoverflow.net OR site:aixiv.online OR site:zenodo.org)`（2026-11-26）。

**待复核。** 精确M10计算证书、严格整数结果未得；最新同余/估计全文仍需补取。

## 7. 跨组查重结论与新候选

74个指定配对全部读取双方现版正文。主关系计数：同源不同问25对；相关但不等价46对；特例/强化2对；待定1对。未合并任何题卡。

三个需要保留的细节：2274↔000479因对方当前字面错误而暂记待定，修复到标准Brennan后才使用Makarov桥判断同题；2279↔000516整卡相关但不等价，普通圈子问中另列Hamilton强化而不覆盖诱导圈；2287↔001170记录Firoozbakht到Cramér的强化方向，其余几个全参数素数猜想不由渐近界自动逐个关闭。

| 本题 / 版本 | 新候选 / 版本 | 关系 | 当前限制 |
|---|---|---|---|
| QX-P-002192 / `c40bc86729042511` | QX-P-002181 / `886a9866f063943e` | 待定 | 标题与原始问题线索高度重合；输入仅索引，正文在线入口不可达，未以标题认定同题。 |
| QX-P-002203 / `2db5600b22029e1d` | QX-P-000906 / `4b9090e5ac89c5c5` | 待定 | 同为Sinha最大素因子mod4偏差；候选标题问Σχ渐近，本卡还问追平/反超。另一题正文未取得，不能只凭索引定为同题或强化。 |
| QX-P-002212 / `24b7c20ab25cf794` | QX-P-002211 / `db92124e04438811` | 待定 | 全库索引新增候选：超曲面K稳定性与K模空间完整描述相邻。未指派此对，未作双方正文等价审计；不得合并。 |
| QX-P-002255 / `bbfd6a5636e5bffb` | QX-P-000331 / `db90820ea7a09861` | 待定 | 索引题名精确指向EP40密度版本，与原题校准后疑同题；未取得对方全文，不越过索引级。 |
| QX-P-002264 / `8665c74a044acc68` | QX-P-002495 / `a2670bdd28053378` | 待定 | 索引为一般Whitehead非球面性猜想，与本题有可能的特例/强化关系；未取得对方正文，不确认等价或蕴含范围。 |
| QX-P-002280 / `ee224043d6033676` | QX-P-000482 / `a6275c7dd7360689` | 同题 | 两卡主命题均为：对任意n状态完全确定同步自动机，存在长度≤(n−1)^2的复位字；B的acceptance同样量化所有n及所有n状态同步自动机。2280给出的完整定义与000482人话版的每字母全状态映射一致。 |
| QX-P-002286 / `093c45ac5a29480b` | QX-P-001648 / `28153cb3ee26990b` | 待定 | 2286正式要求凸覆盖及SE(2)保向刚体运动；1648题面/人话版/acceptance不写凸性，查新备注却明确“判定对象=凸万有覆盖变体”。B的版本内部存在可行域冲突，不能仅从遗漏凸性认定它必为非凸问题，也不能仅从Keller数值认定同题。两卡运动群约定也需统一。 |

2280↔000482的主命题相同，但000482把“同步”误写成“强连通+同步”，已记录应先修的边界冲突。2286↔001648另有凸性在题面与查新备注间的内部冲突，且运动群尚未统一，保留待定。其他仅标题候选不作同题推断。

参考卡正文污染另在配对表保留：1701/1703正式题面仍待补；2462和2450各有“本机文件”字符串侵入公式。它们不是本包新增任务行。

## 8. 下一轮复核清单

1. **先修能直接确认的题面。** 优先处理2219、2229、2230–2234、2261、2266、2270、2272–2273、2276、2281、2284–2286的对象、量词、参数、公式及边界；保持原card_rev供回写前并发比较。
2. **先登记能明确定位的旧定理。** 对2192、2210、2260保留出处、定理范围和历史来源；不得把子问已证批量转成整卡全部已证。
3. **审查改变状态的新完整声明。** 重点取齐2269的位复杂度与退化情况、2274的有界谱上界、2288的稳定刚性及维数提升、2289的计算/Lean依赖，并核版本及勘误。原稿不可达的条目先补全文。
4. **处理有实质缺陷的证明声称。** 2287先保存v9 Lemma2.5反例与证明中≥误成>的位置，避免同一稿再次作为可靠解答导入；不得据此否定其他稿或Cramér主猜想。
5. **逐仓库核题意与依赖后才安排重跑。** 复核顶层定理、定义、非空与端点、imports、axioms和占位；作者machine-verified/zero sorry文字不是本轮独立运行结果。
6. **最后处理合并。** 先修复000479、000482、001648等当前文字冲突，再审新候选；本报告只给关系，不替代线上合并审批或版本检查。

**检索局限。** 本轮并非穷尽所有语言、站内数据库或不可达版本。403/404/429/超时、搜索摘要可见但正文不可达、只取到README或顶层声明的情形逐项保留。普通开放状态不由零命中推出。精确数学结论、证据层级、形式化状态均以逐题JSONL为准。
