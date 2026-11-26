# QX-NEW-09｜突破点、检索路径与复核清单

核查日期：**2026-11-26（Asia/Shanghai）**。按包内《00_先读我》与《查新规则与回传格式》执行，仅处理 `任务.jsonl` 指定的 **100 张题卡**。原 `batch_id`、`id`、`card_rev` 全部保留；没有修改线上库、合并卡片或发帖。

## 一、交付与读法

- `QX-NEW-09_逐题回传.jsonl`：100行，每题独立记录数学子问、实际查询、证据访问级别、查重关系、修订建议与待复核点。
- 本文件：集中列会影响状态、题面、出处、证明范围或查重的变化；逐题无新解的常规记录留在JSONL。
- `复核附件/`：三份自写核验程序及各自JSON结果。Jackson与加权族的有限检查实际运行通过，另有矩阵算术和贪心展开两项局部检查。均不是外部Lean工程重跑。
- `QX-NEW-09_交付校验.json`：题号/版本/字段、指定配对覆盖、路径覆盖、文件哈希与执行边界。

共记 **935条检索、取证和查重记录**、**305条证据项**。该记录数包含原文/代码读取与本地查重，不等于独立网页请求次数。每题均实际执行名称与公式/特征两组学术查询、GitHub/Lean及公开AI/社区查询，并有带近期过滤的复查。多查询工具的联合返回不伪装为逐条独立命中。

**状态按子问解释。** 28张卡含“完整证明/反例声明待核”子项，46张卡含“题面有误”子项；二者可以重叠。后者包括主问题、辅助论断、公式、定义及书目说明，并不等于46个研究问题为假。4个“原题已反驳”子项中还包含字面边界反例和某个特定构造的适用性判断；6个“原题已证”子项多为已知特例，不能用来关闭整张主问题卡。

“完整声明待核”包含本轮新发现和旧声明重新核源；不表示全部是新成果，也不表示已被独立接受。公开目标陈述、实际证明端点、作者报告的编译结果、独立重跑是不同证据层级。本轮**没有重跑任何外部Lean、SAT/DRAT或大型证书工程**，没有从零命中推导全球开放状态。原站失败、镜像、仅摘要、全文不可达及命中不适用均逐题记录。

## 二、优先处理的发现

| 题号 | 本次变化 | 建议与边界 |
|---|---|---|
| 002353 | 对已有12点Jackson候选另写完整有限枚举：144个Hamilton圈、168个边不交圈对、无三圈分解 | 原全称命题有可复现的有限反例；不影响充分大阶数定理，不作历史优先权或Lean重跑声明 |
| 002357 | 卡面允许k=1；n=2、F={∅,{1,2}}、x₁=x₂=1/2同时违反两个目标不等式 | 修复预期范围为k≥2；字面反例不传播到修正后的加权猜想 |
| 002316 | Ho v3 Theorem1.2声称给出覆盖当前L²稀疏和速率的反例 | 补入完整反例声明待核，重点审§6与几乎处处量词 |
| 002330 | Yang–Hou–Fang Theorem4.18、Corollary4.19声称三个投影生成无限维R*代数 | 主问与三投影特例都被声明覆盖；本轮取得镜像，未独立审构造 |
| 002339 | 新界1.2937与1.337分别折算0.64685、0.6685，超过卡面0.6402 | 两项完整下界声明待核；完整大证书尚非公开；同时修正缩放系数 |
| 002343 | 作者新稿承认旧Gap归约证明有误，新归约增加GAPSY分支 | 撤去无条件引用；证明有误不等于定理已被反例否定 |
| 002388 | 统一F∞宿主的公开声明与实际Lean端点覆盖n≥3的两个嵌入问句 | 完整证明声明待核；修复F∞与有限BG混同及Higman递归呈示条件遗漏 |
| 002358/002359 | 全维Hausdorff声明若成立，即覆盖高维紧集Minkowski子问 | 统一登记声明待核；PR陈述检查不等于完整解答已审 |
| 002361/002389 | 直接有限性与wreath/Hopfian相关新声明，假设和依赖不同 | 逐个记录底域、挠/无挠、有限呈示及桥梁定理，不合并证明等级 |
| 002390 | Nilradical实际Lean端点保留两个显式结构定理参数 | 已核对应、未重跑；不能写成无条件完整分类定理形式化 |
| 002391 | 卡内短正合列与本次核得的通常群类乘积顺序不符 | 优先校勘核/商方向；原提出人记号仍待原稿核对，不据另一方向的短证明结题 |

各项直接链接、定理/页码/提交、量词范围、实际搜索词与待复核点见以下分节及JSONL。

## 三、查重总览

60组指定配对均读取了双方所附版本正文。若参考正文缺少决定性的公式，读取完成仍不能判定等价，相关条目继续标“待定”。全库2469条简索引用于定位线索，不代替全文。

去重后共83组关系：同题3组、特例/强化8组、同源不同问3组、相关但不等价48组、待定21组。其中23组是本轮在指定清单外补充的关系或候选。另有宽泛索引命中保留于各题`index_review`，没有自动升级为配对。

| 双方题号与原版本 | 全文核对结论 |
|---|---|
| QX-P-002322 @ bf300aabd68f9f5e ↔ QX-P-002323 @ 62ec2c026002e746 | 同题：变化指数下的Fermat–Catalan有限性 |
| QX-P-002331 @ 89b68848f0121448 ↔ QX-P-002385 @ 4f78e3be345984ba | 同题：无限有限呈示IF群的自由/闭曲面分类 |
| QX-P-002332 @ 595672dd2fdf95a1 ↔ QX-P-002392 @ 43678a5b3637fc55 | 同题：有限呈示无限单群是否可能需要超过两个生成元 |

仅报告关系，不建议凭索引自动合并。两项值得特别纠正的关系：002347与000322存在明确单向蕴含，应记特例/强化；000420的Green35来源是自卷积问题，不能因误译标题而与002335的球面restriction合并。

## 四、数论、组合与矩阵问题的重要变化

### 优先复核的状态变化

#### QX-P-002316 · a875a56adac7ed6d

发现覆盖原题的重大新反例声明：Ho 的 arXiv:2604.18535v3（2026-10-23）Theorem 1.2。已核假设与增长量级，未独立审完整证明，应升级为完整反例声明待核。旧卡还含归一化及均值条件的多项错误。

- **均值零 L²、Hadamard 稀疏序列的 o(N√loglog N) — 完整证明/反例声明待核。** Theorem 1.2 对每个 p≥2 构造实均值零 f∈L^p 与 n_(j+1)/n_j≥2，使几乎处处、所有 ε>0 的 limsup S_N/[N(log N)^(1/p−ε)]=+∞。取 p=2、ε=1/4 即否定本题，因为 (log N)^(1/4)/√loglog N→∞。 证据：作者 arXiv v3 预印本，主定理精确对应；完整证明未独立审查；形式化：未取得该主反例完成 Lean；当前 FC 仍 open/sorry。

**关键来源与定位**

- [版本记录：v1 2026-04-20，v3 2026-10-23](https://arxiv.org/abs/2604.18535)：v3 修订说明提到 referee comments，但不能据此自动称已正式发表。（本次访问层级：摘要与版本）
- [Theorem 1.2；§6 证明位置](https://arxiv.org/html/2604.18535v3)：原题反例主定理；本次已核 f、n_j、几乎处处与归一化，未审完整证明。（本次访问层级：全文相关段）
- [Theorem 2；刊页51–56，尤其52页附近](https://users.renyi.hu/~p_erdos/1949-09.pdf)：原出处定理范围与旧卡归属纠正。（本次访问层级：全文相关段）

**实际路径**：Erdos 995 lacunary strong law L2 N sqrt log log 2026 → "strong law" "Erdos" "1949" "lacunary" L2 → site:github.com "erdos_995" → "995" "lacunary" (site:hexagonmath.org OR site:mathoverflow.net OR site:proofatlas.ai) → 以上关键来源的打开/定位。完整原词、直接链接与访问级别见逐题 JSONL。

**待复核**：首要待核 §6 的测度/集合构造与几乎处处量词；需要后续独立专家审查；未取得主反例形式化或核验；v3 修订不是本次独立复现；论坛无法读到全帖。

#### QX-P-002317 · c65b96c9f659e32d

重新核到覆盖原题全部量词的完整反例声明；已取得固定Lean源并核主陈述，作者侧验证报告与PR仍待外部审查。本次未编译，不提升为独立验证通过。

- **平衡双集合余有限覆盖是否迫使无界表示 — 完整证明/反例声明待核。** Theorem1.1给正整数无限A,B，|a_i-b_i|≤5√b_i、[16384,∞)⊂A+B及全序表示≤47005 证据：公开预印本＋固定作者代码＋作者验证报告；形式化：已核定理对应、未重跑。
- **A=B的Erdős–Turán特例 — 未作判断。** 两集合反例不解决同一集合特例 证据：逻辑范围核对；形式化：不适用。

**关键来源与定位**

- [第1页Theorem1.1；§§2–6；§7为附加变体](https://hexagonmath.org/pdf/2611.00758v1)：主定理三个条件吻合当前题面；作者声明而非本次证明审计。（本次访问层级：全文相关节）
- [Erdos1145Prop、convolution_eq_card、erdos_1145_false、full_counterexample](https://github.com/Ghuffy1/erdos-1145/blob/9caddccde51364623c3c985c9fddd0b52a023e6b/Erdos1145.lean)：已取得75608字符文件；核无限、正性、Nat.nth枚举比值、余有限覆盖、全卷积计数定义；文本扫描未见sorry/admit/axiom/unsafe/native_decide。没有运行。（本次访问层级：代码已取得并核目标）
- [Actual checks、Axiom audit](https://github.com/Ghuffy1/erdos-1145/blob/911146df2b7e103c81038d46bd469f4a1583649f/verification/REPORT.md)：作者报告Lean4.34.0，六目标仅标准三公理，fresh Lean kernel replay通过；不是第二独立内核，也非本次重跑。Mathlib锁5ed2965256430c3649e86755f9576b54eca72435。（本次访问层级：作者报告全文）
- [PR元数据与正文；2026-11-26抓取](https://github.com/TheJustinSunPrize/awards/pull/5560)：open，merged=false，comments=0，review_comments=0；不能当官方接受。（本次访问层级：API元数据与正文）
- [扫描第3页Problem1.17](https://web.math.pmf.unizg.hr/~vjekovac/EP/Some_of_Pauls_favorite_problems.pdf)：本次截图实读原文A+B=N、a_n/b_n→1及无界g(n)；当前题面改余有限覆盖，预印本同时给此主版和含0的全覆盖附加版。（本次访问层级：扫描页视觉核对）

**实际路径**："Balanced additive complements with bounded representation functions" Howe Huffman → "Erdos" "1145" "47005" → site:github.com/Ghuffy1/erdos-1145 "erdos_1145_false" → "Erdős" "1145" (site:mathoverflow.net OR site:zenodo.org OR site:hexagonmath.org OR site:proofatlas.ai) → 以上关键来源的打开/定位。完整原词、直接链接与访问级别见逐题 JSONL。

**待复核**：固定依赖独立重跑及传递公理核对尚未执行；需要独立数学审查及PR最终接受情况；原题页面web受限；原出处已通过扫描Problem1.17补核。

#### QX-P-002291 · f5161e4ed5e7ff46

主猜想未取得全维解答。新增 n=4 完整证明声明、2025 谱限制定理与 2026 方法论文；Kovačec 的更强包含猜想已被其修订稿撤回。旧卡非正规反例的算术错误应修复。

- **任意维数、两个复正规矩阵的 Marcus–de Oliveira 猜想 — 暂未找到可验证结果。** 本次没有取得覆盖所有维数的证明或反例；当前形式化仍为开放占位。 证据：一手来源相关段；初查未审完整证明；形式化：未取得主命题完成证明；没有运行外部代码。
- **维数 n=4 — 完整证明/反例声明待核。** Denzel Zheng 的 66 页原稿 Theorem 1.1 声称证明所有 4×4 正规矩阵情形；已核陈述对应，未审全篇。 证据：作者公开原稿；有直接 DOI / 作者主页入口；形式化：未取得对应完成形式化代码。
- **2025 谱限制特例 — 部分进展。** Shitov：一矩阵谱全实、另一矩阵至多三个非实特征值的范围；不能替代一般情形。 证据：已刊论文摘要，正文未取得；形式化：未取得主命题完成证明；没有运行外部代码。
- **Kovačec 更强的区域包含命题 — 部分进展。** 2026-11-04 修订稿撤回原 Conjecture 7 的强包含关系，并列更强猜想反例；不反驳原 MOC。 证据：作者修订预印本及更强命题形式化蓝图；形式化：仅阅读蓝图；未取得固定证明源码、未重跑。

**关键来源与定位**

- [Theorem 1.1；66 页作者原稿；由作者主页 DOI 10.13140/RG.2.2.36790.25923 进入](https://www.researchgate.net/publication/416773999_The_Marcus-de_Oliveira_conjecture_for_n_4)：声称完成 n=4，不能推广为任意 n。（本次访问层级：全文相关段）
- [Shitov，2025，摘要；DOI 10.4213/im9292e](https://journals.rcsi.science/1607-0046/article/view/306781)：谱限制下的已刊特例。（本次访问层级：期刊元数据与摘要）
- [Mulero，2026；DOI 10.1016/j.laa.2026.03.019](https://www.sciencedirect.com/science/article/pii/S0024379526001266)：检索摘要说明变分方法的进展与障碍；直接正文 403。（本次访问层级：搜索摘要；正文不可达）
- [第2页修订说明；§4 第8–10页](https://www.mat.uc.pt/preprints/ps/p2611.pdf)：撤回更强 Conjecture 7；题名已改为大多边形包含于单连通区域。（本次访问层级：全文相关段）
- [更强猜想反例蓝图](https://the-omega-institute.github.io/trureturing-mdbook/Blueprint/D5/S3/Quantum/Matrix/KovacecStrengthenedMarcusDeOliveiraRefutation.html)：是强化命题的形式化线索，未核固定代码，不是原猜想反例。（本次访问层级：蓝图正文）

**实际路径**："Marcus de Oliveira" conjecture 2026 proof counterexample → "normal matrices" "convex hull" "determinant" conjecture → site:github.com "DeterminantalConjecture" Lean → "Marcus" "Oliveira" conjecture (site:mathoverflow.net OR site:zenodo.org OR site:hexagonmath.org OR site:proofatlas.ai) → 以上关键来源的打开/定位。完整原词、直接链接与访问级别见逐题 JSONL。

**待复核**：独立审查 n=4 原稿证明；本次仅核主定理对应；Shitov 与 Mulero 论文全文未完成审阅；1973/1982 最初文献未取得原刊全文；题面由当前形式化及作者后续文献交叉对应。

#### QX-P-002292 · 7e99d293d06fb38e

唯一更大扩张仍未闭合，但 2026-10/11 出现对不规则四元组的全局有限性、显式上界及九族约化声明。2601.19803 是 2021 已刊论文的补上传，不应计作 2026 新突破。

- **每个正整数丢番图三元组唯一更大扩张 — 暂未找到可验证结果。** 新论文没有证明所有不规则扩张均不存在；原猜想仍需排空剩余有限族。 证据：一手来源相关段；初查未审完整证明；形式化：未取得主命题完成证明；没有运行外部代码。
- **不规则扩张的全局约化 — 部分进展。** He–Togbé Theorem 1.2 声称不规则四元组有限并给 c<10^338、d<10^(10^24)；Dujella–Slijepčević 给非 Euler 九族及 c<10^99，明确未证明九族为空。 证据：2026 预印本主定理；未审完整证明；形式化：未取得主命题完成证明；没有运行外部代码。
- **Euler 型与首元为 2 的子族 — 部分进展。** Euler 预印本 v2 摘要给 c<4×10^48；{2,b,c} 论文发表于 2021，上传日期不能冒充成果日期。 证据：前者仅摘要与版本；后者期刊信息和 arXiv 摘要；形式化：未取得主命题完成证明；没有运行外部代码。
- **正则性方程的推导 — 题面有误。** (a+b−c−d)^2=4(ab+1)(cd+1) 是正则四元组约束；不能仅凭所有两两乘积加一为平方就假定该方程成立，否则已偷用了待证正则性。 证据：本次量词与定义审计；形式化：不适用。

**关键来源与定位**

- [§2 Conjecture 2.1](https://web.math.pmf.unizg.hr/~duje/quint.html)：原作者研究页面给唯一性问题与已知范围。（本次访问层级：全文相关段）
- [Conjecture 1.1；Theorem 1.2](https://arxiv.org/html/2610.18912v1)：全局有限性和巨大显式界，不是排除不规则四元组。（本次访问层级：全文相关段）
- [第4–5页及 Main Theorem 4.3；203页](https://hexagonmath.org/pdf/2611.00666v1)：九个候选族未证为空，文中明示剩余计算未完成。（本次访问层级：全文相关段）
- [2026-11-19 v2 摘要/版本栏](https://hexagonmath.org/2611.00431v2)：Euler 子族显式界声明；没有取得该版全文证明。（本次访问层级：摘要和版本）
- [Journal reference；DOI 10.2478/auom-2021-0016](https://arxiv.org/abs/2601.19803)：实际成果发表于 2021。（本次访问层级：摘要与期刊元数据）

**实际路径**："Diophantine" "unique extension" triple 2026 → "Diophantine quadruple" "regular" conjecture "2,b,c" → site:github.com "DiophantineTuple" "hasUniqueExtension" → "Diophantine" "triple" "extension" (site:mathoverflow.net OR site:zenodo.org OR site:hexagonmath.org) → 以上关键来源的打开/定位。完整原词、直接链接与访问级别见逐题 JSONL。

**待复核**：两篇 2026 大型证明需独立复核，尤其剩余九族是否后来排空；不把不存在五元组误写成唯一四元扩张已证；索引新增 QX-P-000734 仅题名相关，未指定全文，不判同题。

### 可直接修复的题面、边界与文献描述

下列修复不作为研究主命题已解决。对源文献也有同样过度表述的项目，保留正文复核事项，不因摘要权威性而忽略量词反例。

| 题号 / 版本 | 旧卡 → 本次修正及范围 | 本次依据与定位 |
|---|---|---|
| QX-P-002291 / f5161e4ed5e7ff46 | A=diag(0,1)、B=[[1,3],[0,-1]] 的两种谱乘积为 0、−2，并非均为 0；给定旋转 U 后 det(A+UBU*)=−4/3−√2<−2，仍是去掉正规性的有效反例。 | [Theorem 1.1；66 页作者原稿；由作者主页 DOI 10.13140/RG.2.2.36790.25923 进入](https://www.researchgate.net/publication/416773999_The_Marcus-de_Oliveira_conjecture_for_n_4)；[Shitov，2025，摘要；DOI 10.4213/im9292e](https://journals.rcsi.science/1607-0046/article/view/306781)；本次自写 elementary_checks_a.py / .json |
| QX-P-002292 / 7e99d293d06fb38e | (a+b−c−d)^2=4(ab+1)(cd+1) 是正则四元组约束；不能仅凭所有两两乘积加一为平方就假定该方程成立，否则已偷用了待证正则性。 | [§2 Conjecture 2.1](https://web.math.pmf.unizg.hr/~duje/quint.html)；[Conjecture 1.1；Theorem 1.2](https://arxiv.org/html/2610.18912v1) |
| QX-P-002295 / 8dd54239dbd6c728 | 只有 O(n) 对点处于三重线，并不能推出只有 O(n) 条普通线；应把条件改为仅 O(n) 对点不处于三重线（在无四点共线等相应假设下）。 | [第3页 Conjecture 2.1；结尾开放问题；2024 正式发表](https://real.mtak.hu/191930/1/s00454-023-00556-3.pdf)；[第32–33页 Problem 69](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf) |
| QX-P-002296 / f65b2270e75be053 | 当前材料只支持 GRH 单独不足以推出近满平均水平的通常推导；未建立 EH 与 GRH 的逻辑强弱关系。改写为“不知由 GRH 推出”。 | [第17章 Elliott–Halberstam 讨论](https://kskedlaya.org/ant/chap-bombieri.html)；[v2，2025-11-08；摘要](https://arxiv.org/abs/2411.19762) |
| QX-P-002297 / 1cd685f6523fc809 | Ulam 最低密度猜想断言球的最密堆积密度不高于任一凸体；某椭球可更密与此一致，不能构成反例。 | [4 页作者原稿；SM2 构造与结尾](https://math.nyu.edu/inmemoriam/donev/Packing/EllipsoidCrystal.pdf)；[Jin et al. SQ-TR 后续论文](https://arxiv.org/abs/1608.07697) |
| QX-P-002299 / a7bd494c37b7a684 | 将损坏的“本机文件 operatorname…”修为 {p∈ℕ : IsEmirp(p)}，保留十进制与逆序不等于自身。 | [摘要；作者列表与题名](https://arxiv.org/abs/2309.11380)；[A006567 定义检索结果](https://oeis.org/A006567) |
| QX-P-002300 / 98e6c15ef5280dc0 | 单元素 magma 自动满足任何恒等式；“最小模型为 5 阶”必须限定非平凡模型，并保留所用额外条件。 | [§8 Problem 8.1，约第49–50页](https://teorth.github.io/equational_theories/paper.pdf)；[677 章](https://teorth.github.io/equational_theories/blueprint/677-chapter.html) |
| QX-P-002301 / 86fa132e91be8930 | ∀四点量词可取某对重合，故零也是可比距离；任意不同点距离至少1。旧卡“最近距离可任意小”与该版本不相容。 | [v2，2026-10-23；题名与摘要](https://arxiv.org/abs/2604.15305) |
| QX-P-002305 / 826b5eea0eb1f938 | 没有蓝色三元齐性集比没有蓝色 k 元齐性集更强。k=3 负式推出任意 k≥3 负式；单个 k>3 的逆向没有由单调性得到。∀k≥3 与 k=3 等价因为包含 k=3。 | [PNAS 68(1),142；DOI 10.1073/pnas.68.1.142](https://pmc.ncbi.nlm.nih.gov/articles/PMC391181/)；[Theorem 7；后续开放问题](https://www.math.uni-hamburg.de/home/loewe/INFTY%40ESSLLI2011/larson3.pdf) |
| QX-P-002307 / 2014ff8fbf64d263 | 若存在 P₀ 未要求正，取 P₀=0 后 0<ε≤P₀ 的范围为空，使旧式字面命题平凡为真；应写 ε₀>0。<br>当 p^ε<2 时可用正整数仅1，若分母必须不同，则无法表示所有模 p 类；须说明充分大 p 或允许重复/小素数单独处理。计数下界也应计 ∑_{j≤k}M^j 而非直接 M^k。 | [Shparlinski 2002 摘要](https://link.springer.com/article/10.1007/s00013-002-8269-2)；[Glibichuk 2006 摘要](https://link.springer.com/article/10.1007/s11006-006-0040-8) |
| QX-P-002309 / 1f3e7e5615719bda | lower density=0 只推出若自然密度存在则等于0；不能排除自然密度存在。 | [摘要、下密度主定理](https://arxiv.org/html/2605.22763v1) |
| QX-P-002310 / b355c02d60016e7a | k≤N/d 加一般等差数列素数估计不能直接推出 k≪log N；公差随 N 变化且需要额外整除结构。 | [关于 longest arithmetic progression of primes 的问题段，刊页约339](https://www.renyi.hu/~p_erdos/1979-07.pdf)；[Green–Tao 摘要](https://arxiv.org/abs/math/0404188) |
| QX-P-002311 / a50607a6d9dfe033 | 1/3 第一步即减为零，不会重复3。2/3 的经典算法是 1/3+1/3，而不重复版沿 1/3+1/5+1/9+1/45 终止；两个轨道不同。 | [算法定义、Remark 2.4 与开放问题](https://www.fq.math.ca/Scanned/39-3/pihko.pdf)；[odd greedy / denominator restriction 讨论](https://ics.uci.edu/~eppstein/numth/egypt/approx.html)；本次自写 elementary_checks_a.py / .json |
| QX-P-002315 / 441d7869099b89a9 | d>√n 时 h=\|d−n/d\|=d−n/d；旧式 d+n/d−d 等于 n/d，明显不是因子差。<br>n^(1/4)(log n)^(1/7) 对任意固定 C 最终大于 Cn^(1/4)，不是更短尺度；其平方数结果覆盖本题限制到平方数的子问题。 | [card_window_le_one / card_window_le_four；five_divisors_infinite；erdos_887_rosenfeld_4_false](https://github.com/mnn31/erdos-lean/blob/5cb725981b3ad137103ef908eb6ecff9e7ed9bdf/ErdosLean/Erdos887.lean)；[2026 论文入口](https://arxiv.org/abs/2611.11574) |
| QX-P-002316 / a875a56adac7ed6d | 若 f 有界，\|S_N\|≤N\|\|f\|\|∞，除以 N√loglog N→0，完全不需稀疏性；不能把此同速率子问列开放。<br>常数均值项 cN 在本题归一化下也趋零，因此均值零对本题速率不必要；同一分母下有限 limsup 只给 O，不自动给 o。若真正 LIL 分母为 √(Nloglog N)，则可推出本题更弱速率。<br>原文 Theorem 2 是附 Fourier 尾条件的正向强律，旧卡下界例应定位第52页附近的论述，不能归为 Theorem 2。 | [版本记录：v1 2026-04-20，v3 2026-10-23](https://arxiv.org/abs/2604.18535)；[Theorem 1.2；§6 证明位置](https://arxiv.org/html/2604.18535v3) |
| QX-P-002318 / 8b4aab2d27b2c166 | 上界应为 50·10^5=5,000,000，不能读成 500,000；在线发表于 2025-06-20，卷期为2026。 | [Theorem 1.4](https://arxiv.org/html/2503.15714v1)；[Observation 2.2；BAMS 113(2026),15–25；DOI 10.1017/S0004972725100154](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/on-eswarathasanlevine-and-boyds-conjectures-for-harmonic-numbers/AADD00C255BBC1535F9F6DD8FFD4893A) |

各修题项的实际学术名称检索如下；公式、代码与社区的另外三条查询及后续读取均保留在 JSONL。

- QX-P-002291：`"Marcus de Oliveira" conjecture 2026 proof counterexample`（system1，recency=365天）→ 本题相关一手来源及固定形式化文件。
- QX-P-002292：`"Diophantine" "unique extension" triple 2026`（system1，recency=365天）→ 本题相关一手来源及固定形式化文件。
- QX-P-002295：`"Elekes Szabo" "ten" "cubic" 2026`（system1，recency=365天）→ 本题相关一手来源及固定形式化文件。
- QX-P-002296：`"Elliott Halberstam" 2026 proof conjecture`（system1，recency=365天）→ 本题相关一手来源及固定形式化文件。
- QX-P-002297：`"ellipsoid packing" densest 2026`（system1，recency=365天）→ 本题相关一手来源及固定形式化文件。
- QX-P-002299：`emirp infinitely many primes reversal proof 2026`（system1，recency=365天）→ 本题相关一手来源及固定形式化文件。
- QX-P-002300：`"677" "255" finite magma solved 2026`（system1，recency=365天）→ 本题相关一手来源及固定形式化文件。
- QX-P-002301：`Erdos 100 separated distances diameter linear Kanold Piepmeyer 2026`（system1，recency=365天）→ 本题相关一手来源及固定形式化文件。
- QX-P-002305：`Erdos 1169 omega1 squared negative partition relation ZFC 2026`（system1，recency=365天）→ 本题相关一手来源及固定形式化文件。
- QX-P-002307：`Erdos 1180 small inverses Glibichuk optimal epsilon exponent 2026`（system1，recency=365天）→ 本题相关一手来源及固定形式化文件。
- QX-P-002309：`Erdos 125 upper density AlphaProof ternary quaternary 2026`（system1，recency=365天）→ 本题相关一手来源及固定形式化文件。
- QX-P-002310：`Erdos 200 longest arithmetic progression primes o log N 2026`（system1，recency=365天）→ 本题相关一手来源及固定形式化文件。
- QX-P-002311：`odd greedy Egyptian fraction termination proof 2026 Erdos 282`（system1，recency=365天）→ 本题相关一手来源及固定形式化文件。
- QX-P-002315：`Erdos 887 absolute constant divisors square root short interval 2026`（system1，recency=365天）→ 本题相关一手来源及固定形式化文件。
- QX-P-002316：`Erdos 995 lacunary strong law L2 N sqrt log log 2026`（system1，recency=365天）→ 本题相关一手来源及固定形式化文件。
- QX-P-002318：`Eswarathasan Levine conjecture harmonic 1381 2026`（system1，recency=365天）→ 本题相关一手来源及固定形式化文件。

### 其他需要保留范围的新线索

#### QX-P-002294 · 64f9a23190838ecb

DC₂ 当前未取得解答。2026-11-20 修订预印本讨论 JC₂ 与 Mat₂(A₁) 上广义 DC₁′ 的关系，其中反向含附加猜想；不能替换本题第二 Weyl 代数 DC₂。

- 2026 Jacobian/广义 Dixmier 对应：Theorem 1.6 给 JC₂⇒DC₁′，逆向需 Conjecture 1.5；未见该定理给出 DC₂ 的无条件证明。（作者修订预印本相关定理；未取得主命题完成证明；没有运行外部代码）
- 与 DC₁/PC₁ 参考卡的关系：DC₂ 与维数一命题不是同题；DC₂ 是涉及更多生成元的强化问题，不能合并。（指定双方全文与当前来源的范围核对；不适用）

来源：[定义 DC₁′；Conjecture 1.5；Theorem 1.6](https://arxiv.org/html/2610.33919v2)；[Dixmier 1968；BSMF 96，209–242；DOI 10.24033/bsmf.1667](https://www.numdam.org/item/BSMF_1968__96__209_0/)

实际路径：`"Dixmier" "DC_2" 2026` → 当前作者原稿/期刊页面/固定代码（访问等级见 JSONL）。

待复核：原始 math/0608009 HTML 访问失败；形式化文件另列高维否定条目：本题初查未审其证明，不能把这些标签作为 DC₂ 结论。

#### QX-P-002296 · f65b2270e75be053

Elliott–Halberstam 主问题未取得可验证全解。2025/2026 命中是附加零点相关假设或特定权重/模数范围。另检索到非数论期刊技术报告的 Theorem 70 全命题字样，正文访问失败，列为未核声明线索。

- 有条件及受限模数进展：2411.19762：GRH 加 pair-correlation 假设；2602.20917 v6：双线性 9/17、三线性 17/32 等范围，不能替代一般 EH。（作者摘要和版本；后者版本记录说明修订；未取得主命题完成证明；没有运行外部代码）
- ISHIHARA 技术报告的 Theorem 70 线索：搜索摘要出现 Elliott–Halberstam 定理名与证明字样；已核 J-STAGE 元数据，PDF 超时，尚不能确定陈述等价、假设和证明有效性。（搜索片段＋技术报告元数据；未取得正文；未取得证明代码）

来源：[第17章 Elliott–Halberstam 讨论](https://kskedlaya.org/ant/chap-bombieri.html)；[v2，2025-11-08；摘要](https://arxiv.org/abs/2411.19762)；[v6，2026-05-27；摘要/修订说明](https://arxiv.org/abs/2602.20917)；[Fundamental theory of information technology；DOI 10.11517/jsaisigtwo.2025.AGI-031_01](https://www.jstage.jst.go.jp/article/jsaisigtwo/2025/AGI-031/2025_01/_article/-char/en)

实际路径：`"Elliott Halberstam" 2026 proof conjecture` → 当前作者原稿/期刊页面/固定代码（访问等级见 JSONL）。

待复核：J-STAGE 报告须取得正文并先核 Theorem 70 假设/命题；原始 EH 论文未取得全文；2610/2609 部分来源不可达；没有独立形式化重跑。

#### QX-P-002298 · d96c3453dbc028e2

原论文的启发式有限素数猜想与主问题对应，但原 Proposition 6/7 使用移除坏素数因子的 F_n，不能无说明替换为任意整数 W_n。筛法密度零不等于有限。

- 合数下标与倍点特例：原 Proposition 6/7 的 F_n 按原文 eq.(10) 规范化；须保留定义及坏素数处理，不能直接写成任意 W_n 的完全等价约化。（2001 已刊作者 PDF 相关定义与命题；未取得主命题完成证明；没有运行外部代码）
- 强整除序列筛法：2402.19301 讨论素数项下标的密度与筛；密度为零容许无限，不能解有限性。（作者 arXiv 摘要；HTML 访问失败；未取得主命题完成证明；没有运行外部代码）
- 旧卡 2026 模曲线分解论文：2610.37191 本次无法打开，故未重新核 Theorem 3.2 与指数限制；不复述为本次已验证。（旧卡线索；本次访问失败；不适用）

来源：[§2，eq.(10)，Propositions 6–7](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E2CE61AFB56AFDBC17263F9905DED3E9/S1461157000000772a.pdf/primes-in-elliptic-divisibility-sequences.pdf)；[摘要；Strong divisibility sequences and sieve methods](https://arxiv.org/abs/2402.19301)；[旧卡 2026 分解论文入口](https://arxiv.org/abs/2610.37191)

实际路径：`"elliptic divisibility sequences" primes 2026 finite` → 当前作者原稿/期刊页面/固定代码（访问等级见 JSONL）。

待复核：Ward 表示与整模型缩放的精确等价仍需专业复核；2605.25797、2610.37191 等新稿正文不可达；不从 primitive prime divisor 定理推断项本身为素数。

#### QX-P-002303 · 7f84241dac79dbb3

固定绝对 C 的阻集问题仍未取得证明。原 ESS 文献是 O(log n) 上界。2026 新论文给特定二次曲线并的障碍，不能推出所有阻集不存在常数上界。

- 对数上界：Erdős–Silverman–Stein 原文给 c>2e 的对数型控制；C 随阶增长。（1983 原作者 PDF；未取得主命题完成证明；没有运行外部代码）
- 2026 二次曲线并与小阻集进展：Asgarli–Ghioca–Yip Theorem 1.2 在奇数 q 的特殊不可约二次曲线并中要求至少 c₀ log q 条；Sziklai 线性猜想稿另有 p^e≠3,4 条件。均不解所有阻集的绝对 C。（前者作者预印本相关全文，后者摘要；未取得主命题完成证明；没有运行外部代码）

来源：[第8页/刊页255，c>2e 推论](https://users.renyi.hu/~p_erdos/1983-07.pdf)；[Theorem 1.2](https://personal.math.ubc.ca/~dghioca/papers/blocking-union-Oct-13.pdf)；[摘要及条件 p^e≠3,4](https://arxiv.org/abs/2610.30503)

实际路径：`Erdos 1159 projective plane blocking set constant 2026` → 当前作者原稿/期刊页面/固定代码（访问等级见 JSONL）。

待复核：社区 PG(2,11) 例未独立检验；没有读取所有非 Desarguesian 平面构造；不能据特定模型推全体。

#### QX-P-002304 · 90440e6347aad3c8

所有 2^m 的群同构类支配问题未取得一般解答。新社区计算声称验证 m=11 的更强总和不等式，适用范围只有该有限参数，数据未由本次复算。

- m=11 的有限验证声明：作者网页声称 ∑_{n<2048}g(n)=49,910,538,480，小于 1,774,274,116,992,170≤g(2048)；没有本次重新运行分类计算。（社区作者计算报告，未核底层枚举/论文定理；未运行代码；不能称独立验证）
- 奇数阶等受限参数：当前形式化注释引述既有奇数阶范围；本次未取得原始学位论文，不新增认证。（来源注释而非原证明；未取得主命题完成证明；没有运行外部代码）

来源：[正文的 m=11 比较及 Eick 引文链接](https://www.erdosproblemaday.com/day/1160-group-count-m11)；[有限群数列入口](https://oeis.org/A000679)

实际路径：`Erdos 1160 groups order powers two Pantelidakis 2026` → 当前作者原稿/期刊页面/固定代码（访问等级见 JSONL）。

待复核：原始 1999 问题集相关页未重新核图；m=11 需要追 Eick 原文和小群库确切计数；未取得 Pantelidakis 论文全文。

#### QX-P-002306 · 6eacd0b4d3fe0e86

Brown–Erdős–Sós 型阈值主问题仍未取得解答。2022 的 +2 边界极限与 2026 (9,6) 近二次下界，均不能替代 +3 阈值的 o(n²) 上界。

- 已知特例与边界相邻进展：EFR 1986 的特例、Shangguan 2210.11338 的 +2 边界极限是相关定理；注意顶点阈值相差1。（已刊摘要及作者预印本摘要；未取得主命题完成证明；没有运行外部代码）
- 2026 (9,6) 下界：Kong–Shangguan–Wang 搜索摘要声称 f₃(n,9,6)≥n²exp(−O((log n)^(2/3)))；这是近二次下界，与 o(n²) 上界可能同时成立。（作者 arXiv 搜索摘要；abs/html/pdf 均访问失败；未取得证明代码）

来源：[摘要；+2 阈值](https://arxiv.org/abs/2210.11338)；[EFR 1986 摘要](https://link.springer.com/article/10.1007/BF01788085)；[2026 v2 搜索结果摘要](https://arxiv.org/abs/2611.05261)

实际路径：`Brown Erdos Sos conjecture e edges r uniform (r-2)e+3 solved 2026` → 当前作者原稿/期刊页面/固定代码（访问等级见 JSONL）。

待复核：最新稿全文不可达，需要后续核主定理与修订记录；没有完成一般阈值证明审计。

#### QX-P-002315 · 441d7869099b89a9

统一绝对 K 主问题未取得解答。已读取固定作者 Lean 文件，核 C=7/2 的无穷五约数和 C=40 的“4 最优”变体反例陈述；未编译。旧卡因子差公式与 Chan 尺度方向应修正。

- 固定 C 五约数无穷族 / 四个最优变体：作者代码 five_divisors_infinite 用 C=7/2；erdos_887_rosenfeld_4_false 用 C=40。两者与任意绝对 K≥5 相容。（固定作者代码全文；核定理对应；已核定理对应、未重跑；导入 FormalConjectures.ErdosProblems.887，完整依赖未审）

来源：[card_window_le_one / card_window_le_four；five_divisors_infinite；erdos_887_rosenfeld_4_false](https://github.com/mnn31/erdos-lean/blob/5cb725981b3ad137103ef908eb6ecff9e7ed9bdf/ErdosLean/Erdos887.lean)；[2026 论文入口](https://arxiv.org/abs/2611.11574)；[Erdős–Rosenfeld 1997 原刊入口](https://matwbn.icm.edu.pl/ksiazki/aa/aa79/aa7944.pdf)

实际路径：`Erdos 887 absolute constant divisors square root short interval 2026` → 当前作者原稿/期刊页面/固定代码（访问等级见 JSONL）。

待复核：完整 Lean 依赖和传递公理未独立核/跑；Chan 原刊与 2026 论文全文仍需取得；四约数最优变体与统一 K 主问题不能混列。

#### QX-P-002318 · 8b4aab2d27b2c166

一般 J_p 有限仍未取得解答。2025 预印本已有正式出版记录（BAMS 113，2026，15–25）。旧卡把调和素数计算范围写为 5×10^5，原文实际为 50×10^5=5×10^6。

- 有限素数范围及调和素数计算：Theorem 1.4(i) 验证 p≤16843 且 p≠1381 的有限性；(ii)/Observation 2.2 在 [5,5×10^6] 的 348511 个素数中记录 128594 个调和素数。（已刊作者论文相关定理/计算说明；未本次复算；未执行作者计算程序）

来源：[Theorem 1.4](https://arxiv.org/html/2503.15714v1)；[Observation 2.2；BAMS 113(2026),15–25；DOI 10.1017/S0004972725100154](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/on-eswarathasanlevine-and-boyds-conjectures-for-harmonic-numbers/AADD00C255BBC1535F9F6DD8FFD4893A)

实际路径：`Eswarathasan Levine conjecture harmonic 1381 2026` → 当前作者原稿/期刊页面/固定代码（访问等级见 JSONL）。

待复核：1991 原刊 DOI 入口本次不可达；没有独立复算 Boyd/2025 论文的遍历与分支界；v1 中个别符号排字需以出版版为准。

### 指定查重结果

本组12个指定对子没有据此建议合并。关系标签只描述已读题面；参考卡内的额外数学断言没有自动视为真实。本组没有为未指派的标题候选偷做同题断言。

| 本题 / 版本 | 配对题 / 版本 | 关系 | 关键区别 |
|---|---|---|---|
| QX-P-002294 / 64f9a23190838ecb | QX-P-000449 / 091bfc91853d09f8 | 特例/强化 | 参考卡为第一 Weyl 代数 DC₁/PC₁，本卡是 DC₂；维数不同，不能当作同题，参考卡的 JC₂ 等价表述也需另核。 |
| QX-P-002295 / 8dd54239dbd6c728 | QX-P-000327 / 914746f5a3d6e973 | 相关但不等价 | Dirac 问存在一点决定至少 n/2−K 条线；本卡以 cn² 条三重线为前提问十点共三次曲线。 |
| QX-P-002295 / 8dd54239dbd6c728 | QX-P-001224 / 1461286641cbc648 | 同源不同问 | 果园题问恰三点线数量的极值；本卡问高数量条件下十点共三次曲线的结构。 |
| QX-P-002298 / d96c3453dbc028e2 | QX-P-002323 / 62ec2c026002e746 | 相关但不等价 | 参考卡为 Fermat–Catalan 变指数互素幂三元组有限；本卡固定 EDS 的素数项有限。对象与量词不同。 |
| QX-P-002299 / a7bd494c37b7a684 | QX-P-000350 / 5baa3dbe00e32668 | 相关但不等价 | 回文卡要求 R(p)=p，本卡要求 R(p)≠p；两集合互斥。参考卡对 2309.11380 的作者/适用范围另需核。 |
| QX-P-002299 / a7bd494c37b7a684 | QX-P-000863 / e756fc8b96c6c4ec | 相关但不等价 | 幸运素数由筛法定义，emirp 由十进制逆序定义；共有无穷性目标不构成等价。 |
| QX-P-002299 / a7bd494c37b7a684 | QX-P-001203 / d253fa328675196b | 相关但不等价 | Leinster 群由适当子群阶之和定义，非反向素数问题；属于主题误召回。 |
| QX-P-002299 / a7bd494c37b7a684 | QX-P-001705 / 8b406eaf03a07591 | 相关但不等价 | Mersenne 素数为 2^p−1，与十进制逆序素性不同。参考卡题面栏待补，已读说明也不建立等价。 |
| QX-P-002311 / a50607a6d9dfe033 | QX-P-000732 / f7f185f702a07e39 | 相关但不等价 | 参考 #287 是不同分母单位分数和为1时必须有间隔≥3；本卡是特定奇分母递归算法终止。 |
| QX-P-002317 / c65b96c9f659e32d | QX-P-000329 / 0dfe8cb524e651da | 特例/强化 | A=B 的 Erdős–Turán 是双集合命题的特例；新反例用两个不同集合，不解决同集合特例。 |
| QX-P-002317 / c65b96c9f659e32d | QX-P-000331 / db90820ea7a09861 | 相关但不等价 | 参考 #40 对同一集合 A 的密度设阈值，问自卷积无界；本卡研究双集合交叉卷积，不能传播反例。 |
| QX-P-002317 / c65b96c9f659e32d | QX-P-000334 / c16ce51e4cb646e8 | 相关但不等价 | 参考 #66 问自卷积表示与 log n 的比值能否趋正数；本卡问双集合交叉卷积是否无界。 |

全库索引另见 QX-P-000734（787757e13b2c3d9a，Dujella 三元组关联椭圆曲线整数点）与 2292、QX-P-000229（5f215c047f4b75b7，另一序数分划问题）与 2305、QX-P-002255（bbfd6a5636e5bffb，同集合 Erdős–Turán 强定量形式）与 2317 的主题线索。这些未指定对子只读到索引，未断言等价；可在后续另配全文。

## 五、代数、分析与增长问题的重要变化

### 1. 002330：出现直接覆盖三投影特例的完整反例声明

**题卡：QX-P-002330 @ `9fc63bbedee72b93`。** 旧卡保留有限生成逐元有限谱星代数的有限维问题。新检索找到 Yang–Hou–Fang 的 *Kadison’s open problem and R*-algebras*，标为 arXiv:2611.20690v1，2026-11-16。原 arXiv 入口不能读取，取得的是 [37 页原稿镜像](https://borowiecki.dev/pdf/2611.20690)。

Theorem 4.18（印刷第 36 页）声称构造三个投影代数生成的无限维含单位星代数 B，且每个 M_q(B) 都是 R* 代数；Corollary 4.19 给出在每个 II₁ 因子中的含单位嵌入。取范数闭包即可对齐本卡 C* 闭包问句。这不是仅有大量生成元的相邻反例：**三个投影特例也被声明覆盖**。

建议记为“完整反例声明待核”，不记成已接受反例。需从 [arXiv 原记录](https://arxiv.org/abs/2611.20690) 获取正式文件及修订，复核构造、代数性和嵌入。实际路径包括 `"finite spectrum" "Kadison" 2026`、`site:arxiv.org "2611.20690"` 和原页/镜像打开；

另须修正旧卡“单个算子有限谱等价代数”的说明。Volterra 算子 V 有谱 {0}，但 V^m1=x^m/m!，故并非代数算子。[Garrett 讲义 §4.2，第 8 页](https://www-users.cse.umn.edu/~garrett/m/fun/notes_2012-13/06b_examples_spectra.pdf) 提供谱计算；原稿 Definition 1.2 所用的是**整个星代数逐元**条件的等价，不能逐个非正规算子套用。

### 2. 002339：两个超过目标阈值的新完整下界声明，以及错误缩放

**题卡：QX-P-002339 @ `284a13ce2b734e3b`。** 旧卡只核到 1.2802（折算 0.6401），并对 PBV 的 1.292 留有公理/核验问题。本轮取得两项直接超过原题 0.6402 的声明：

| 来源 | 定位与新界 | 本卡口径 | 证据边界 |
|---|---|---:|---|
| [Kim–Pilanci，arXiv:2606.31182](https://arxiv.org/pdf/2606.31182) | §4.2；Theorem B.10、C.1；1.2937 | 0.64685 | 原稿说明严格区间算术/对偶证书，本次未复跑 |
| [Tomar，Hexagon:2611.00395v1](https://hexagonmath.org/pdf/2611.00395v1) | Theorem 1.1，第 2 页；1.337 | 0.6685 | 计算与 Lean 完整声明；完整数据尚非公开 |

Tomar 附录分别列原始上确界与本质上确界版本，量词覆盖本卡非负可积函数，而非仅有限维试探函数。**Data Availability（第 17–18 页）写明完整 1.337 数据约 1.88 TB，暂仅应请求提供**；公开哈希/较弱界材料不等于公开完整复现。稿中列仓库固定提交 [bfabb085b8c4725d2f3f1002341bdeb592cf8979](https://github.com/tejasvi/autocorrelation-lower-bounds/tree/bfabb085b8c4725d2f3f1002341bdeb592cf8979) 和 DOI [10.5281/zenodo.23715661](https://doi.org/10.5281/zenodo.23715661)，本轮两处均无法读到代码/数据。因此保留“完整证明声明待核／他人声称已形式化”，不可写独立通过。

书目也应保守：[Pilanci 作者页](https://stanford.edu/~pilanci/) 把 Kim–Pilanci 列为 ICML 2026 AI4Math Workshop；PDF 页脚的 PMLR 写法与作者页不一致，本次不把它升级为已核实主会发表。Hexagon 的编号也不能误标 arXiv。

旧卡缩放系数需确定修正。若 g 支撑在 [-1/4,1/4] 且质量 1，应取

\[
f(x)=\tfrac12g(x/2-1/4),\qquad
(f*f)(t)=\tfrac12(g*g)(t/2-1/2).
\]

旧系数 2 会使质量变成 4，卷积范数变成 8 倍。半倍常数换算正确，原文给出的函数公式错误。

实际路径包括 `"autoconvolution" "1.2937"`、`"AI-assisted discovery of convex relaxations via dual agents" Kim Pilanci`、`"2611.00395" "autocorrelation" "github"`；PBV [作者 README](https://github.com/AndreiPiterbarg/sidon-autocorrelation) 仍明列四个自定义数值公理；不应因有 Lean 文件而提升为无条件形式化证明。

### 3. 002343：作者新稿承认旧归约证明有误

**题卡：QX-P-002343 @ `f6e3da32d3ab9531`。** 旧卡把旧预印本 Theorem 8.5 的 just-infinite／残差多循环归约写成既定成果。本次找到 Grigorchuk 2026-11-12 新稿 [2611.16279 的原稿镜像](https://borowiecki.dev/pdf/2611.16279)：第 1–2 页承认对应已刊 Theorem 7.5 的证明有误，源于对三分类型结论的错误使用，且尚不能修补。

不能由此断言旧定理结论已被反例推翻；应撤下“已证明”标签，记为证明有误待修。新 Theorem 3.3（第 8 页）引入 **GAPSY 商**分支，不能省略。新 Corollary 3.2（第 7 页）仍支持残差有限群加单群的归约，并覆盖 β=1/2；因此不应一并删除全部旧归约。

[旧原稿](https://arxiv.org/pdf/1202.6044) Theorems 8.4–8.5 已重新读取作对应。旧文期刊应为 *Bulletin of Mathematical Sciences* 4 (2014), 113–128，DOI 10.1007/s13373-012-0029-4，非题卡元数据中的 *Journal of Algebra*。

实际路径：`"Grigorchuk" "Gap Conjecture" "2026" reduction`、带 recency 的 `"Grigorchuk gap conjecture" 2026`、`"Grigorchuk" "GAPSY" "Theorem 3.3"`；待获取新稿正式原站最新版本；一般 G*(1/2) 未获全称证明。

### 4. 002336：有理性问题遗漏有限值定义域

**题卡：QX-P-002336 @ `2a23916843a34dcb`。** 当前卡把所有 C₁ᴴ(F_Q;Q) 有理链都要求 scl∈Q。按 [原稿 §2 的定义与 §6 Conjecture D](https://arxiv.org/html/2507.14009v3)，非零实同调链的 scl 是 ∞；秩 1 自由 Q 群 (Q,+) 的链 c=1 就是字面反例。

建议限定 c∈B₁ᴴ(F_Q;Q)，或明确值域为 Q∪{∞}。这纠正有限值条件，并未解决真正的有理性猜想。原稿简写可能使用隐含域约定，不能由此宣称作者的实质猜想被推翻。Theorem B 等距、C 正性、E 曲面结论均不能替代有理性。

实际路径：`"Stable commutator length on free Q-groups" rational Conjecture D`，后续打开 §2、§6；待定稿采用哪一种等价修正口径。

### 5. 002332：Radu 一个候选已被二生成公式排除

**题卡：QX-P-002332 @ `595672dd2fdf95a1`。** [Ferudun 2026-10-14 四页原稿](https://eulersolve.org/papers/aim-geometric-group-theory-0126/paper.pdf?v=638a3bbc5b0a)，Theorem 1 第 1 页给 Radu Corollary IV(ii) 的群

\[
G=\langle x_1x_3,x_1y_3\rangle.
\]

Lemma 2 第 1–2 页提供恢复原生成元的明确群字。这只排除该具体候选，不证明所有有限呈示无限单群二生成。一般问题仍出现在 [Bleak–Elliott–Matucci 的 Question 6.1](https://www.cambridge.org/core/journals/journal-of-the-institute-of-mathematics-of-jussieu/article/sufficient-conditions-for-a-group-of-homeomorphisms-of-the-cantor-set-to-be-twogenerated/FB64BF6FC27C0E053C21D6A2D954104F)。

实际路径包括带 recency 的 `"Radu" "two-generated" 2026`、EulerSolve 原文与链接追踪；验证报告链接被工具返回为元数据，未提供正文；本次不声称审计报告或独立形式化通过。存在量词中的损坏文本“（本机文件 quad）”应恢复为 `\exists G,\quad`。

### 6. 002335：球面完整声明不能覆盖任意非零高斯曲率

**题卡：QX-P-002335 @ `d8d15707ddb053e0`。** 本轮读到 [Chung v1 Theorem 1.1](https://arxiv.org/html/2611.11060v1)、[OpenAI 079 范围说明](https://github.com/openai/math/blob/main/lean/docs/079.md) 和 [LocalSmoothing Comparator](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/LocalSmoothing.lean)。公开材料直接针对球面；本卡还允许其它非零曲率签名，当前不能由球面结论自动全域化。

Chung 的 n≥3 声明与 Comparator 的严格指数范围也不同。Comparator 中的 `sorry` 是目标占位，不能据此指控实际证明文件有洞；同样不能把目标声明当作完整证明。球面子问保持完整声明待核；任意非零高斯曲率的范围未由这些来源覆盖。形式化记“已核目标范围，未取得/重跑完整 proof target”。

另核 [Rios–Sawyer arXiv 2512.24990 的 v9 版本记录](https://arxiv.org/abs/2512.24990)，早先更简单证明的说法已经撤去，当前 testing characterization 不应当作一般解决。

实际路径：`"restriction conjecture" OpenAI Chung 2026 proof`、曲率特征检索、079 与球面目标打开。

### 7. 002340：无界子列已足以反驳主问；另有量级比较错误

**题卡：QX-P-002340 @ `dd554c9f643180ce`。** [OpenAI 191 范围说明](https://github.com/openai/math/blob/main/lean/docs/191.md) 明确声称在无界 n 子列上构造最小面积至少 n^(-2+η)、η>0 固定的点集，并说明纸面“每个充分大 n”比链接形式化更强。**无界子列已足够反驳本卡的统一 n^(-2+o(1)) 上界**；不能因缺少全 n 扩展而写成对原题不适用。单位正方形与圆盘的固定缩放只改常数。

保持“完整反例声明待核”，因为本次只核到官方范围和 Comparator 入口，未取得可审计纸面 PDF 全文或构建实际 Lean 证明。既有 [CPZ Theorem 1.8](https://arxiv.org/html/2409.07658v2) 的 n^(-7/6+ε) 上界已重新定位。

旧卡另称 Ellmann 的 n^(-3/2)(log n)^(-7/2) 声称“弱于 KPS82”，比较方向错误：其与 (log n)/n² 的比值为 n^(1/2)/(log n)^(9/2)，趋于无穷。应改成“若成立则渐近更强，但该启发式声明未核验”；本次没有据此认可 Ellmann。

实际路径：Heilbronn 名称/幂公式、带 recency 的 2026 查询、191 scope→Comparator。

### 8. 确定的题面或说明错误

| 当前题号与版本 | 旧卡 → 建议修正 | 核对依据与范围 |
|---|---|---|
| 002319 `af7fbe50881badc2` | `1≤n≤6` 的非存在断言 → `2≤n≤6`；统一“b”与“b⁷” | n=1,a₁=b=1 是直接反例；修正后的七次幂问题没有因此解决。错误 LPS 引句 `k+n>b` 也须删除/重引 |
| 002327 `4b002c47d0fb39cb` | “换对数底乘1/ln b，改变整数性” → 乘 (ln b)^(-1/n)，趋1 | 本次直接极限计算；[Olshanskii v1 原稿镜像](https://www.researchgate.net/publication/405923018_Finite_groups_and_rings_generating_varieties_with_rapid_growth) 只给极大 potential 子类，普通极限与整数性仍须分问 |
| 002337 `c6e6e5142b42edd2` | “单侧 census 不覆盖逆元球外” → 真正未覆盖左支撑球外 | [Tabei Theorem1.1](https://www.researchgate.net/publication/411182685_The_one-sided_unit_count_of_F_2P_at_radius_four_and_an_integral_separation_theorem) 作者声称恰52个非平凡单侧单位（完整性证书未独立复跑），逆元无预设球限制；16个逆元在半径5。DRAT 为作者报告，本次未跑 |
| 002337 同上 | “总支撑42比单侧21更强” → 修正逻辑方向 | 全称单侧21同时作用于u及u⁻¹便推出总42；总42不能反推各侧21 |
| 002341 `ebdc86fd0eadc912` | 损坏计数公式 → `N_A(θ,t)=#{a∈A: θa mod1∈I_t}` | 按 a 计重数；若把重合像去重，θ=0 会平凡化。题源为 [Green Problem86，p.41](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf) |

上述每题都另有本轮实际学术、代码、社区和近期查询；不是仅做静态题面扫描。2327 的最新 v3 与 2341 线性散列新稿全文不可达，限制已经分别写入逐题记录。

### 9. 002322/002323：同题，且解释不能把弱结果升级

**版本：002322 `bf300aabd68f9f5e`；002323 `62ec2c026002e746`。** 双方全文均要求变化指数下互素正整幂三元组总有限，是同题。方程 x^p+y^q=z^r 下，一个素数整除两个底数就整除第三个，故整体 gcd=1 与两两互素等价；002323 的“严格更强”解释应改。

Beal 只处理三个指数均≥3的无本原解，不能无说明地推出全部含指数2族的 FC 有限性。[Darmon–Granville Theorem2，印刷 p.515](https://www.math.mcgill.ca/darmon/pub/Articles/Research/12.Granville/pub12.pdf) 是固定指数结论。Tudor [Zenodo 22968502](https://zenodo.org/records/22968502) 完整证明线索本次不可读，保留待核。

后续已打开 [Chocian Theorem1.1 与 §8](https://arxiv.org/html/2609.26996v1)，为固定 (3,5,7) 的计算辅助完整声明；证书未复跑，不能全域化。[Jaswal 作者页](https://manvirjaswal.github.io/papers/x2-y5-z7/) 的 (2,5,7) 结论以 Putz 未刊分类为条件。实际查询分别使用 Fermat–Catalan 名称、幂三元组描述和具体签名；

### 10. 002344：PROVED 徽章不能覆盖任意块长

**题卡：QX-P-002344 @ `83ffb182b1e8895e`。** [Erdős Problem a Day #375 工作报告](https://erdosproblemaday.com/report/375) 顶部有 PROVED，但正文仅声称所有起点的固定块长 k≤59，并保留 k≥60 缺口。它不解决一般 Grimm。证书仓库本轮不可达，局部声明记待核。

[Laishram–Murty 原稿](https://arxiv.org/pdf/1306.0765) 第 2–4 页重新核到经典范围、条件关系与 n<1.9×10¹⁰ 的既有验证，均不覆盖全部 n,k。实际路径包括 `"Grimm conjecture" "2026" "59"`、连续合数素因子描述、仓库与社区定向、recency 查询；

### 11. 配对全文复核与来源误配

18 个指派配对均读取双方当前 `statement_text`；另新增三组可确认为同题的配对。没有合并或线上编辑。

| 双方题号与版本 | 结论 | 关键区别或一致性 |
|---|---|---|
| 002322 `bf300aabd68f9f5e` ↔ 002323 `62ec2c026002e746` | 同题 | 上节说明 |
| 002331 `89b68848f0121448` ↔ 002385 `4f78e3be345984ba` | 同题 | 无限、有限呈示、所有无限指标子群自由；闭曲面均含环面与Klein瓶 |
| 002332 `595672dd2fdf95a1` ↔ 002392 `43678a5b3637fc55` | 同题 | 双方正文 d>2；2392标题不能改读为 d>3 |
| 002339 `284a13ce2b734e3b` ↔ 000420 `0c2e2ec7521d7dbf` | 特例/强化，但参考卡需先纠错 | 000420 的源是 Green35 自卷积常数，被误译成球面 Fourier restriction；本卡为 p=∞ 且更高阈值 |
| 002335 `d8d15707ddb053e0` ↔ 000420 同上 | 相关但不等价；标题误配 | 按真正 Green35 来源，不是 restriction 猜想 |
| 002334 `55c56cdbe8040345` ↔ 002431 `09f2d8ae239d4dc3` | 相关但不等价 | 四维六个二元平方和与三维三元平方和条件不同 |

002331 的 [Wilton v3 原始 PDF](https://arxiv.org/pdf/2406.02121) 已读；Question0.1 p.1 明列一般问题，TheoremsA–D 为已证子类。

全库2469条标题索引又找到 2321↔1702、2324↔2483、2339↔0052、2340↔1647、2344↔0765 的相邻线索。对方正文不在本包参考集中，均保留“待定”，不凭标题判同题。其它指派的否定配对结论和双方版本见逐题 JSONL。

### 12. 复核顺序与实际限制

建议优先复核 002330 的三投影反例、002339 两个新下界、002343 的撤回式证明纠错，再修复 002319、002336 的主问域/平凡反例和确定的公式说明错误。凡是预印本或计算声明，逐题记录都把数学结论、证据类型和形式化状态分开。

本轮没有独立重跑 Lean、SAT/DRAT、Magma、浮点筛或 TB 级证书。原站失败时，镜像已明确标出；未列明的 Scholar、OpenAlex、zbMATH 或其它 AI 入口没有被声称为已查。多查询工具合并返回的命中也没有伪装成逐查询精确归因。原始工具回执为内部审计材料，不纳入对外交付包。

## 六、几何、拓扑、组合与群论的重要变化

### 1. 字面主命题已有精确反例：加权 k-union-closed

**QX-P-002357 @ e2951acaba143db4。** 旧卡把参数明确写成 `1≤k≤n`，又把整个命题视为未决。取

\[
n=2,\quad k=1,\quad\mathcal F=\{\varnothing,\{1,2\}\},\quad x_1=x_2=\tfrac12.
\]

族覆盖底集。对三个非空集合 A，所有包含在 A 内的族成员之并分别为空集、空集、全体，均仍在族内；权重满足下界 `2^(k−1)−1=0`。但每个 i 的不等式左边都是 1/4、右边都是 1/2。因此**卡片字面的全称命题为假**。

本会话编写并运行 `weighted_k1_counterexample.py`，用 Python `Fraction` 精确检查每项假设和两个失败不等式，结果在同名 JSON。它不是 Lean 证明。建议将字面错误与预期问题分开：把预期范围修为 `2≤k≤n` 后继续研究，不能声称 k≥2 也被反驳。

实际路径：四路名称/权重公式检索 → 打开 [MO 原提问及 Choice1979 回答](https://mathoverflow.net/questions/511338/frankl-like-conjecture-for-k-union-closed-family-of-sets) → 逐条参数代入 → 自写精确核验。公开回答证明所有权重至少 n−1 的情形，只覆盖原阈值满足该条件的范围。原提问主要讨论 k=2 与更高，不应把本次针对卡面 k=1 的发现宣传为推翻原作者全部猜想。

待复核：维护者确认题面拟采用的 k 下界；k=2 与普通并闭族的“等价”需要交代空并/空集约定。新索引候选 002494 未提供全文，不能合并。

### 2. Jackson 12 点反例：本轮独立有限枚举通过

**QX-P-002353 @ a17be8daa593c92b。** 旧卡已有 Mazur/ProofAtlas 反例声明，未有本会话独立复算。根据 [固定 Graph.lean 构造](https://www.proofatlas.ai/sources/jackson-hamilton-decomposition-counterexample/commits/52ae1c0b7cffe499aa0427ea08bed6e85eff6df3/JacksonHamiltonDecomposition/Graph.lean)，本轮另写 Python：四个循环层各三个顶点，相邻层弧顺时针，唯四条位置零到位置零的弧反向。

程序检查它确为 K6,6 的定向，12 点、36 弧、各点入出度均为 3；固定顶点 0 枚举所有 Hamilton 圈，得到 **144 个圈、168 个边不交圈对、0 个可由剩余弧补成第三个 Hamilton 圈的圈对**。任何分解必有三个圈，故穷举排除了全部分解。这提供原全称命题的独立有限计算反驳；[Granet 的充分大阶定理](https://arxiv.org/abs/2209.02988) 不受影响。

文件为 `jackson_independent_check.py` 与同名 JSON，包含完整弧集、144 个圈、度数与计数。程序也核对旧卡另外一个具体错误：固定二部和顶点标号时，4 点和 8 点正则定向的数量分别是 **2 和 90**，不是 1 和 6。该计数没有借用外部枚举程序。

还需修正：K_(2n,2n) 的 Hamilton 圈经过 **4n** 点；正则图总阶数是 4 的倍数，并非必须 8 的倍数。

实际路径：Jackson 精确名称/二部定向公式检索 → [平台 artifact](https://www.proofatlas.ai/proofs/artifact.jackson.flipped-c4-blowup-counterexample.lean-package.v001.html) → 固定提交 52ae1c0b7cffe499aa0427ea08bed6e85eff6df3 的构造 → 自写完整有限枚举。平台自报 Lean4.29.1、标准三公理与构建通过；**本轮没有 Lean rerun**。反例的历史新颖性、最小性及平台审稿独立性仍待专家核查。

### 3. Kakeya 两卡必须对齐声明范围，不能以 PR 代替证明审计

**QX-P-002358 @ 4109c92b03d006f9；QX-P-002359 @ 54695442b4f631b2。** 前者只问 n≥4 紧集的 Minkowski 满维，后者问所有 n≥2 任意 Kakeya 集的 Hausdorff 满维。旧状态一个 open、一个 claimed。后者的完整声明若成立，利用 `dimH≤lower dimM≤upper dimM≤n` 直接覆盖前者，因此 002358 也应登记“已有完整声明待核”。

本轮经 GitHub API 实读 [当前固定 Comparator.lean](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean)，确认 `OAI.Analysis.Fourier.LocalSmoothing.Comparator.kakeya` 对所有 n≥2、任意满足单位线段条件的 F 断言 Hausdorff 维数 n，没有额外可测或紧假设；顶层调用 `OAI.MeasureTheory.Kakeya.kakeya`。这只是**定理接口对应、未重跑依赖**。

另读 [formal-conjectures PR7741](https://github.com/google-deepmind/formal-conjectures/pull/7741)：仍 open、unmerged；作者说明只核对陈述 transport，明确没有检查 OpenAI 解答。PR 中移除 formal_proof 链接是作者授权政策，不是数学否定。反过来，reference challenge 含 sorry 也不能用来否定实际 solution。

实际路径：全维/四维与 Hausdorff/Minkowski 两组查询 → OpenAI 范围说明 → 当前固定 solution endpoint → PR body/current state。待复核：完整工程构建、依赖/公理与定义语义；本轮未作期刊接受或社区共识的最终判定。

### 4. Kaplansky：三个来源的范围要分开

**QX-P-002361 @ 6c9b90a07afcaf13。** [OpenAI 固定 FinitelyPresented.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/RingTheory/DirectFiniteness/FinitelyPresented.lean) 已经 API 读取。其 endpoint 是有限特征 2 域 K、有限呈示群 G、G 含奇素数阶元、标量 a,b∈K[G] 满足 ab=1 且 ba≠1。它匹配本卡，但不是无挠 F2 版本的同一证书。

[Mghirbi–Douglas 2611.04599v1](https://arxiv.org/html/2611.04599v1) 主定理与 §11 已读：作者声称对每个素数 p 都有有限呈示、无挠、词双曲群，且有有限二维分类空间，使 Fp[G] 出现反例。作者报告 Lean4.34.1 对主存在性定理重放；概率型 Theorem A 与后续 sofic/surjunctive 结论并非全部形式化。作者的报告不能写成本会话独立通过。

[Jaikin–Zapirain 2611.08268](https://arxiv.org/abs/2611.08268) 在本轮只有官方搜索摘要可用；abs/html/pdf 入口受限。不得把旧卡此前声称阅读全文当作本轮完成。

修复卡面两处被“本机文件”破坏的 `K:Type`、`G:Type` 量词。保留“完整反例声明待核”，不把顶层无 sorry 升格为全依赖检查。与 002389 的 wreath 问题有下游联系，仍是不同待验陈述；后者另有逐题记录，底域/矩阵环与 Hopfian 嵌入桥梁必须独立核对。

### 5. Jones：异议针对中间证明包，并非 Jones=1 的结反例

**QX-P-002355 @ 0370a7ad4ec06b58。** 本轮原 v1 的 arXiv 全文不可达，仅打开 [作者 ResearchGate 摘要](https://www.researchgate.net/publication/407507169_On_trivial_Jones--Vassiliev_polynomials)；完整检测声明存在。

经 API 实读 [Barnett claim-review.md](https://github.com/barnettcaleb1/jones-unknot-research/blob/main/archive/work/paper/carmi-cohen-obstruction/claim-review.md)，内容 blob 为 3f64dc864371ffdc38ed71c5d6bc77b51bdf5ad2。其反对对象是 Prop.5.12、Thm.5.6、Lemma5.8 的联合统一压缩包：三交叉固定宿主会给次数上界22，而指定反平行扭曲族在 L=23 给 b51=−1。适用性依赖标记几何识别；不能把它写成对每个单独引理的无条件否定，更不是非平凡结 Jones 多项式为1的反例。

实际路径：作者/题名和公式检索 → 原文入口失败 → 作者摘要 → 公开审计全文。旧卡中的本地整数复算属于历史会话，本轮没有复跑，不计为新执行。维持验证轨；待获得原全文并核 C1–C3、G2 与标记扭曲对应。

### 6. Kervaire 与 Kalai：部分形式化和作者构建报告的边界

**QX-P-002362 @ b8fad3470f404d86。** [Lin–Wang–Xu v2](https://arxiv.org/html/2412.10879v2) Theorems1.1、1.4、Corollary1.2 直接给126维存在声明；Questions1.6、1.7仍是强 Kervaire 变体。[GAIR README](https://github.com/GAIR-NLP/Kervaire126/blob/main/README.md) 已通过 API 阅读，明确基础构造、比较和计算认证仍有 sorry。旧卡187个/44文件计数没有在本轮重计。应分别记录数学论文声明、含占位的形式化项目和未执行的本轮重建。卡面等价式还有未绑定的 n；左边已固定126，右边应删除多余 n 条件或先定义它。

**QX-P-002360 @ 3d372a96094424a0。** [KitaKen1 五维仓库](https://github.com/KitaKen1/kalai-three-pow-five/blob/main/README.md) 与 [PR7341](https://github.com/google-deepmind/formal-conjectures/pull/7341) body/review 已读。外部证明指向 commit38bc3bb25949bc33de05bbd169a6012aa0b05165；审核者明确只核陈述、版本和日志，未独立 rerun。五维即使成立也不解决 d≥6。976模块/42660声明是作者自报，非本轮统计。Chambers–Portnoy 的 [EJC出版记录](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v33i3p24) 可达，本轮没有读其全文，不能仅凭元数据增加定理范围。

待复核：两个工程完整依赖、定理语义与计算输入认证；不能因无期刊元数据便断言作者从未投稿，也不能因项目存在便写独立形式化通过。

### 7. Hasse–Weil：原引用与潜在模性推导有实质错误

**QX-P-002348 @ 497c343f8eb7bec0。** [Tate原始扫描](https://www.numdam.org/item/SB_1964-1966__9__415_0.pdf) 印刷416页/PDF第3页已同时检查文本和截图：收敛半平面为 `Re(s)>3/2`，比较因子为 `(ζ_K(s−1/2))^(2d)`。卡片的 `≥3/2` 和 `ζ(s−1)^(2d)` 均需更正。

扩域后的 L(E/K,s) 与 L(E_L/L,s) 通常不同，不能说是同一个 Dirichlet 级数。[Buzzard作者综述](https://www.ma.imperial.ac.uk/~buzzard/maths/research/papers/survey.pdf) 的 Theorem1.16 提供全实域潜在模性/亚纯延拓语境，不能据错误基变换恒等式推出一般整延拓。[Gross讲义](https://people.math.harvard.edu/~gross/preprints/lectures-pcmi.pdf) Conjecture2.7同时要求完成L函数延拓与函数方程，比本卡单独延拓问题更强。

实际路径：Hasse–Weil名称/任意数域特征检索 → 原Tate PDF及截图 → 作者综述定理 → fixed formal-conjectures HasseWeil 陈述。另修复 `\mathcal L:\mathbb C→\mathbb C` 的乱码。待复核的是一般猜想，不能以潜在模性已有部分结果宣称已解。

### 8. 两份新发现的齐次空间反例摘要不满足假设

**QX-P-002350 @ 7ef0f198405d15cc；QX-P-002351 @ d45262ebd0ae2e80。** 名称/假设检索找到 Guedes2023两个直接反例声明，只读到作者摘要，无全文可得。

- [无非平凡收敛序列声明](https://www.researchgate.net/publication/371168684_Existence_of_Infinite_Homogeneous_Compact_Spaces_Without_Non-trivial_Convergent_Sequences) 用 βN；自然数点孤立、余部非孤立，所以 βN 不齐次。
- [ω-monolithic声明](https://www.researchgate.net/publication/371285690_Homogeneous_o-Monolithic_Compact_Spaces) 首例用无限离散空间一点紧化；其中孤立点与唯一非孤立点也否定齐次性。另两种产品构造只有概述，不能假装读过并否定其全部论证。

以上是本会话直接假设检验，不是全文同行审查。应新增“摘要级声称、所指首例不适用”，不能据此把两个原问题判已反驳。002350还把 sequential 定义成“每个闭包点可由原集合序列逼近”，实际这是 Fréchet–Urysohn；sequential 应为序列闭集均闭。原2013论文在 math.md超时、MathNet不可达，固定 Homogenous.lean 只作为精确问题陈述核对。

### 9. 其他明确题面/范围修复

| 题号与版本 | 旧卡 → 本次建议 | 证据、实际路径与范围 |
|---|---|---|
| 002345 @ ec2f377070ff151c | “两问独立，证明一个不证明另一个” → k=6 推出 k=5 | 本会话加通用顶点的归约：K6细分中删去含新增顶点的支点，或删去该点所在边的一端，留下原图K5细分。另读 [2026 Corollary1.2](https://arxiv.org/html/2605.10112v1)，只有K5或Khat5的析取，仍是部分进展。 |
| 002346 @ 299288a73d494a04 | 不统一写成 inf_g δ=∞ → sup_g δ_min=∞ 或 ∀δ∃g | [Problem4](https://arxiv.org/html/2502.21177v1) 与本会话量词核对；固定g双曲不代表统一常数。 |
| 002349 @ f8cbd556489fce13 | CP^n 总Betti数2(n+1) → n+1；不可又将已有覆盖的CP加权情形列为未决 | [Atallah v3 TheoremA、1.3](https://arxiv.org/html/2309.13791v3) 已读。一般非半单流形仍不能外推。Allais HAL受阻、作者旧PDF404单列限制。 |
| 002352 @ 8bc6d0d8f9176cef | a0=1解释为n=0 → k=0、n=1 | 代入n=2^k即可；[STOC作者稿](https://homes.cs.washington.edu/~rtweber2/StableMatchingSTOC.pdf)指数型上界不等于精确递推极值。Thomas与Thurber全文入口403，不声称已读。 |
| 002354 @ 2f5c268dd1be0e4f | 加J^0=R导致交变R → 加R不改变交 | 本会话集合恒等式；固定 [Jacobson.lean](https://github.com/google-deepmind/formal-conjectures/blob/9097e2f90e66d2f6244209cb1c07f7120d17ec53/FormalConjectures/Wikipedia/Jacobson.lean)也从n=0起。Herstein PMC入口被反机器人页挡住。 |
| 002364 @ 33e027da4ba86da1 | “n次幂” → 分别第1,…,n次幂；删除禁阶使命题变弱 → 假设更弱、全称断言更强 | [Kourovka v50 20.100](https://arxiv.org/pdf/1401.0300v50)，印刷173页。Ma2611.13582只读到官方摘要：有限群n4–6及限制子集结果，不是全题。 |
| 002365 @ 5b691c1ec48e5e62 | “全部pro-p解也只是特例” → 一般问题可归约至全部pro-p；受限子类才只是部分结果 | [Kourovka20.116](https://arxiv.org/pdf/1401.0300v50)印刷175页明确归约；[2602.18839v2 Lemma2.3](https://arxiv.org/html/2602.18839v2)只给固定幂落FC中心的条件结论。另修复g∈G乱码。 |
| 002367 @ 2b755b0f2221740f | ∀S下合取S合法 → 限制量词域或用蕴含；n≠5 → 原定理n≥6；边界与穿孔参数统一 | [Mangioni–Sisto v2 TheoremB](https://arxiv.org/html/2602.23275v2)已读，S_n为n穿孔球，不能误写成任意边界计数。 |

### 10. 查重新关系与新候选

**20个指定配对均完成双方全文阅读。** 不合并线上卡片。

- 002347 @ 9b457e74742a9fad 与 000322 @ d7fe3a812162c2a6：改记**特例/强化**。稠密两两有理距离集若存在，可用足够小的点位扰动保持任一有限平面直线图嵌入，再统一清分母，推出 Harborth。不是完全无关；逆向未证。
- 002358/002359：Hausdorff全维声明强化Minkowski高维紧集目标，关系见上。
- 002350/002503：同源不同问，分别是 Arhangel’skii2013 Problem13 与 Problem3。
- 002360配000323和000498：参考卡本身缺完整数学公式，记录**待定**；足以排除仅凭 Kalai姓名合并，不宣称已判定所有逻辑关系。
- 其余同姓 Hajós/Kotzig、不同 Kaplansky问题、Jones周边与Freyd/Kervaire配对均有对象/假设/目标差异，逐条理由在JSONL。

全库索引新增四条线索，**另一卡全文未提供，均只记待定**：

| 本卡 | 新候选与版本 | 线索 |
|---|---|---|
| 002356 | 000752 @ 2d366afeb45dfa91 | Juggler无非平凡周期变体 |
| 002357 | 002494 @ 09de741e122c26f8 | 加权初等对称式 |
| 002364 | 001560 @ c7f120052af1c48d | 同Kourovka20.100编号 |
| 002368 | 001548 @ 896ce8dd2f9a0c18 | 同Kourovka20.37编号 |

### 11. 已排除的进展外推与未执行项目

- 002363：读 [Montgomery–Pokrovskiy–Sudakov Theorem2.1](https://arxiv.org/pdf/2001.02665)，足够大n的ND-rainbow结果给循环树分解；不等于剩余全部小n已验证。[KRR README](https://github.com/walidelkersh/KRR)异议只针对 Gnang证明的Step5，不能写成Kotzig或graceful猜想反例。
- 002368：读 [Bergman2026修订作者PDF](https://math.berkeley.edu/~gbergman/papers/unpub/re_gp_factzn.pdf)全部3页；Theorem1.1子群链判据是充分条件，正文仍明确k=2未决。k≥3的多因子反例不能替代两因子问题。
- 002369：读 [Jaikin–Zapirain §6 Theorem6.1](https://arxiv.org/html/2212.00402v3)，有限生成子群的某有限维整线性不能升级为GL2。二维目标保持独立。
- 002366：[Monod作者问题页](https://sites.google.com/view/monod/problems)明说未自2026年初更新；访问日期不能当作数学状态更新日期。
- 002356：[作者Juggler计算稿](https://research.muzz.in/juggler/)只报告有限边界与经验模型；本轮没有执行作者代码。Zenodo不可达及目标GitHub文件404均不记零命中。

本轮没有Google Scholar全量引用追踪，没有全库所有正文扫描，没有外部Lean构建或完整数十万行依赖审计；公开AI/社区四入口使用同批site查询，工具返回的是联合结果，JSONL明确不伪造每条查询独立命中归因。所有“未取得解答”均限定实际列出的入口和访问层级。

## 七、Kourovka相关问题的重要变化

### QX-P-002370 @ 8b6b58870576e287

Kourovka 20.42：是否存在有限生成、剩余有限、非可均且满足群律的群

一般问题本轮未取得可核验的新解；核对了群律构造与非可均构造的差别。旧卡把特定含自由子群的例子泛化为全部已知构造，表述过强。

**旧卡 → 本轮建议**

- P1：非可均＋剩余有限已有大量例子，但已知构造含自由子群 → 所引同profinite完备化构造含自由子群；另有非可均剩余有限挠群，不含非阿贝尔自由子群，但未给固定群律。 避免用不成立的总括句描述现有文献。

**范围与直接证据**

- 题卡已知例子的适用范围：**题面有误**。已知有限生成剩余有限非可均挠群没有非阿贝尔自由子群。应把‘已知构造含自由子群’限于所引Kionke–Schesler同完备化构造；挠群并不自动满足固定群律。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：20.42，印刷第164页。
- [Cornulier–Mann，On groups with a group law](<https://www.normalesup.org/~cornulier/law_rf4.pdf>)：Theorems 1、8；Remark 13；Question 14；全文相关段落已读取。
- [Kionke–Schesler，Amenability and profinite completions of finitely generated groups](<https://ems.press/content/serial-article-files/30257>)：Theorem 1.1；Question 2.15；DOI 10.4171/ggd/732；全文相关段落已读取。
- [Kionke–Schesler，Realising residually finite groups as subgroups of branch groups](<https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.12948>)：Corollary 1.2及证明；2024，56(2),536–550；全文相关段落已读取。

**实际检索路径**

- `"Kourovka" "20.42"`
- `"finitely generated" "residually finite" "non-amenable" "law"`
- `site:github.com "Kourovka" "20.42"`
- `"20.42" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR "EulerSolve" OR "ProofForum")`
- `"residually finite" "non-amenable" "law" 2026`（近期过滤365天）

**待复核**

- 未重新运行或审查旧卡所列OpenAI挠群构造；该结果本身不能替代群律和非可均性两个条件。

### QX-P-002371 @ 730ceee348cbc418

Kourovka 20.43：满足共同群律的有限群族是否都一致可均

原问题仍未取得可核验的一般新解。定义必须明确F非空；Example 2.2只支持每一个虚拟可解群分别一致可均，不支持所有虚拟可解群组成的类共享一个界。

**旧卡 → 本轮建议**

- P0：存在有限集F，使|SF|≤(1+ε)|F|且|F|≤m(ε,|S|) → 存在非空有限集F，并满足相同不等式。 空集会使定义真空成立；原论文的比值式定义也需要非空约定。
- P1：虚拟可解群类也一致可均 → 每个虚拟可解群分别一致可均；若声称某个群族一致可均，需另给整个族统一的界。 量词交换造成过强结论。

**范围与直接证据**

- Følner定义及虚拟可解类陈述：**题面有误**。若允许F=∅，不等式对任意群族成立，定义退化。单群的一致可均性与整个群类的一致界不能互换。所有有限群皆虚拟可解，但其全体并非一致可均。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：20.43，印刷第164页。
- [Kionke–Schesler，一致可均定义与判据](<https://ems.press/content/serial-article-files/30257>)：Definition 2.1/2.4；Example 2.2(3),(5)；Theorem 2.10；Corollary 2.12；Question 2.15；全文相关段落已读取。

**实际检索路径**

- `"Kourovka" "20.43"`
- `"finite groups" "common group law" "uniformly amenable"`
- `site:github.com "uniformly amenable" "law"`
- `"uniformly amenable" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR "EulerSolve" OR "ProofForum")`
- `"uniform amenability" "common law" finite groups 2026`（近期过滤365天）

**待复核**

- 原论文Definition 2.1亦省写非空，建议在题卡显式补全约定而非伪称原文逐字如此。

### QX-P-002372 @ bebcaffd0e6ec3bd

Kourovka 20.48：有partition且存在素数阶无固定点自同态的有限p群是否指数为p

未取得一般原问题新解；题卡有指数p与初等阿贝尔混同、中心固定论证错误、公式损坏及否证量词错误。

**旧卡 → 本轮建议**

- P0：exp(P)=p等价于P为初等阿贝尔p群 → 只表示每个元素的阶整除p；另加交换性才是初等阿贝尔。 UT₃(F₃)否定旧辅助等价。
- P1：Z(P)被每个自同态固定，故排除阶p → Z(P)被自同构整体保持；用p阶作用的轨道计数排除无固定点。 整体不变与逐点固定不同。
- P1：Hughes与中央化子公式含‘本机文件’；出处第165页；自同态 → 恢复H_p(P)=⟨g∈P:g^p≠1⟩及C_P(α)；出处第164页；术语改自同构。 与原题和定义一致。
- P1：完整否定回答必须覆盖其他素数阶 → 完整否定只需一个反例；完整肯定需覆盖所有允许参数。 修正全称命题的否证量词。

**范围与直接证据**

- 辅助等价、证明与公式：**题面有误**。指数p不迫使交换：UT₃(F₃)非交换且指数3。中心是特征子群，不是被每个自同构逐点固定。阶p自同构不能无固定点可由轨道计数证明。否定全称命题只需一个满足全部假设的反例。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：20.48，印刷第164页。
- [E. I. Khukhro，Automorphisms of finite p-groups admitting a partition](<https://eprints.maths.manchester.ac.uk/1894/1/eart112.pdf>)：引言与Theorem 2；Algebra and Logic 51(2012)；DOI 10.1007/s10469-012-9189-2；全文相关段落已读取。
- 本会话直接数学校核：UT₃(F₃)：(I+N)³=I；I+E12与I+E23不交换。阶p作用在P上：|Fix|≡|P|≡0 (mod p)，且单位元固定，所以至少p个固定点。

**实际检索路径**

- `"Kourovka" "20.48"`
- `"Automorphisms of finite p-groups admitting a partition" exponent`
- `site:github.com "20.48" "partition"`
- `"Hughes subgroup" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR "EulerSolve" OR "ProofForum")`
- `"Kourovka" "20.48"`（近期过滤365天）

**待复核**

- UT₃(F₃)只反驳题卡辅助等价，不被标作20.48反例；尚需保留全部partition与无固定点假设。

### QX-P-002373 @ 462eac8ffa9d3475

Kourovka 20.49：每个有限群是否都有同指数的二生成子群

原问题未取得可核验的新解；原稿确认可解群二生成特例，旧卡期刊卷年页码有误。

**旧卡 → 本轮建议**

- P1：Forum Math.29(2011),875–890 → Forum Math.24(2012),875–887，DOI 10.1515/FORM.2011.092 原版首页可直接核定。

**范围与直接证据**

- 文献书目信息：**题面有误**。Lucchini–Morigi–Shumyatsky应引Forum Mathematicum 24(2012),875–887，非29(2011),875–890。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：20.49，印刷第164页。
- [Boundedly generated subgroups of finite groups](<https://www.research.unipd.it/retrieve/ff98d086-e8a5-492e-8ad3-48371cc392b1/10.1515_form.2011.092.pdf>)：首页及Theorem E，印刷877页；DOI 10.1515/FORM.2011.092；全文相关段落已读取。

**实际检索路径**

- `"Kourovka" "20.49"`
- `"finite group" "2-generated subgroup" "same exponent"`
- `site:github.com "Kourovka" "20.49"`
- `"Kourovka" "20.49" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR "EulerSolve" OR "ProofForum")`
- `"two-generated" "same exponent" "finite group" 2026`（近期过滤365天）

**待复核**

- 后续三生成改进本轮检索命中但未逐行重审；一般二生成命题未获得新完整证明。

### QX-P-002374 @ 0f3f758bf7d0f694

Kourovka 20.67：Brauer块的特征标次数个数能否控制亏群导出长度

两子问分别保留。2026年有p-可解群的相关导出长度界，但以正高度特征标个数计数，不是不同次数的个数，不能用来关闭本题。

**旧卡 → 本轮建议**

- P2：既有块次数部分结果 → 补2026 e70428的p-可解群正高度特征标计数界，并明确它不等于|cd(B)|界。 

**范围与直接证据**

- (a) dl(D)≤|cd(B)|：**部分进展**。Giannelli–Martínez–Schaeffer Fry给出特定块/少量次数等情形；2026新界用正高度特征标个数加一，假设及右端不同。未得一般结论。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：20.67(a)(b)，印刷第167页。
- [Character degrees in blocks and defect groups](<https://arxiv.org/pdf/2110.13227>)：v2，Question A；Theorems A/B；后刊J.Algebra，DOI 10.1016/j.jalgebra.2021.11.035；全文相关段落已读取。
- [Sylow subgroups and the number of irreducible characters of degrees divisible by a prime p](<https://onlinelibrary.wiley.com/doi/10.1112/blms.70428>)：2026，58(7),e70428；摘要的p-solvable block界；已取得出版社检索摘要；直接全文入口不可达。

**实际检索路径**

- `"Character degrees in blocks and defect groups"`
- `"derived length" "cd(B)" "defect"`
- `site:github.com "Character degrees in blocks and defect groups"`
- `"Character degrees in blocks and defect groups" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR "EulerSolve" OR "ProofForum")`
- `"derived length" "defect group" "2026"`（近期过滤365天）

**待复核**

- e70428全文本轮不可达，具体定理编号与证明留待全文复核。

### QX-P-002376 @ 2aa5b8bf71fd689b

Kourovka 20.77：有界生成的残有限群是否必在特征零域上线性

一般RF有界生成群的特征零线性问题未获新解。旧卡把residually finite-soluble定义成所有有限商可解，混淆原文两个不同推论；Prüfer秩应只对有限生成子群取上确界。

**旧卡 → 本轮建议**

- P0：残有限可解指每个有限商均可解 → 残有限可解指有限可解商分离每个非单位元；‘所有有限商可解’是更强的另一个条件。 Corollaries 1.3与1.4不可混同。
- P1：Prüfer rank=sup_{H≤G}d(H) → 只对有限生成子群H取d(H)的上确界。 允许非有限生成子群会改变定义。

**范围与直接证据**

- 一般剩余有限有界生成群是否特征零线性：**部分进展**。Pyber–Segal Corollaries 1.3–1.6确认特定剩余性质及无限线性商结果，未给一般忠实表示。
- 剩余有限可解与Prüfer秩定义：**题面有误**。residually finite-soluble意为非单位元可由有限可解商分离，不等同所有有限商可解。秩定义是sup{d(H):H≤G且H有限生成}。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：20.77，印刷第169页。
- [Pyber–Segal，Finitely generated groups with polynomial index growth](<https://arxiv.org/pdf/0711.0687>)：引言式(2)；Corollaries 1.3、1.4、1.5、1.6；全文相关段落已读取。

**实际检索路径**

- `"Kourovka" "20.77"`
- `"boundedly generated" "residually finite" "linear" "characteristic zero"`
- `site:github.com "Kourovka" "20.77"`
- `"Kourovka" "20.77" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR "EulerSolve" OR "ProofForum")`
- `"boundedly generated" "residually finite" "linear" 2026`（近期过滤365天）

**待复核**

- 2026 residual profiles相关论文仅命中摘要，其amalgam/pro-p完成结论不能直接解决抽象群忠实线性问题。

### QX-P-002377 @ 03a28c01072ae94e

验证：Qian 的元素阶整除不可约特征标 codegree 猜想

维持完整证明声明待核；Nanying Yang 2026预印本摘要声称覆盖全体有限群，本轮原站全文不可达，未把镜像摘要或题卡历史记录当证明核验。主codegree公式必须修复。

**旧卡 → 本轮建议**

- P0：codegree公式含‘本机文件’及ker项损坏 → cod(χ)=|G:kerχ|/χ(1) 原题20.78的核心定义需恢复。
- P0：完整证明声称 → 记录Yang 2026声明；全文本轮不可达，不能升级为原题已证。 

**范围与直接证据**

- 每个元素阶整除某不可约特征标codegree：**完整证明/反例声明待核**。检索到Yang arXiv:2609.06877全称证明声明；本轮只核到原站索引摘要，未完整核对证明或独立形式化。
- codegree定义：**题面有误**。恢复cod(χ)=|G:kerχ|/χ(1)；损坏的‘本机文件’串不能保留在数学公式中。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：20.78，印刷第169页。
- [Nanying Yang，Element orders and character codegrees of finite groups](<https://arxiv.org/abs/2609.06877>)：2026-09，摘要；完整覆盖声称；官方索引搜索摘要；abs/pdf/html直接打开均DisabledError。
- [Element orders and codegrees of characters in non-solvable groups](<https://arxiv.org/abs/2306.08545>)：摘要；2024已刊版本的部分结果；原站摘要已读取；未重审全文。

**实际检索路径**

- `"Element orders and character codegrees of finite groups" "Yang"`（近期过滤365天）
- `"Qian" "element orders" "codegrees" conjecture`（近期过滤365天）
- `"Yong Yang" "2609.06877" Theorem`
- `site:github.com "Qian" "element orders" "codegrees" conjecture`
- `"Qian" "element orders" "codegrees" conjecture (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR "EulerSolve" OR "ProofForum")`

**待复核**

- 取得arXiv:2609.06877固定版本全文，核Theorem 1.1全部假设与结论、修订/勘误；本轮未取得Lean实现。

### QX-P-002378 @ e2fdd45bc0bfe932

验证：所有 P-character 均为单项特征标能否刻画有限可解群

Lu–Meng最新版v2的Theorem A完整覆盖目标等价命题；已核定理与题卡量词对应，仍作为预印本完整证明声明待核，未做证明审稿或Lean重跑。

**旧卡 → 本轮建议**

- P0：Lu–Meng 2025/2026声称解决 → 固定引用v2及Theorem A，标‘定理对应已核，证明未独立复核’。 

**范围与直接证据**

- 有限群可解⇔所有P-character均monomial：**完整证明/反例声明待核**。Theorem A的(1)–(3)给出同一等价；只要求所有P-character，不是所有不可约特征标。v2于2026-03-30更新。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：20.80，印刷第170页。
- [Fengming Lu、Lin Meng，On permutation characters of finite groups](<https://arxiv.org/html/2511.20171v2>)：Theorem A；Lemma 2.1；§2证明；v2，2026-03-30；原站HTML定理与证明相关段落已读取。

**实际检索路径**

- `"On permutation characters of finite groups" "Lu" "Meng"`（近期过滤365天）
- `"On permutation characters of finite groups" Lu Meng`（近期过滤365天）
- `"P-characters" "monomial" "solvable"`
- `site:github.com "On permutation characters of finite groups" Lu Meng`
- `"On permutation characters of finite groups" Lu Meng (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR "EulerSolve" OR "ProofForum")`

**待复核**

- 未核实期刊接受/刊载记录；未获得对应Lean完整实现；后续审查v2证明及引用依赖。

### QX-P-002379 @ ca8c43ef35a38059

Kourovka 20.81：缺少扩张封闭性的有限群类能否具有无限 Baer–Suzuki 宽度

一般非扩张封闭类仍未取得可验证解。Revin已刊结果增加扩张封闭假设，不可推广。卡中把任意n个元素强制解释为互异会引入|D|<n时的空真。

**旧卡 → 本轮建议**

- P0：任意n个元素按D中n个不同元素理解 → 允许重复的n元组（等价检查至多n个元素生成的子群），并与原题逐字对齐。 旧解释引入未见于原文的互异条件。

**范围与直接证据**

- 任意n个共轭类元素的量词：**题面有误**。不应无依据增加‘不同元素’；应按可重复n元组或至多n个元素表述，以防|D|<n的空真改变问题。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：20.81，印刷第170页。
- [D. O. Revin，The Baer–Suzuki width of a complete class of finite groups is finite](<https://doi.org/10.1090/spmj/1896>)：St.Petersburg Math.J.37(2026),107–131；出版社摘要；检索摘要可读；DOI与AMS全文入口不可达。

**实际检索路径**

- `"Kourovka" "20.81"`
- `"Baer" "Suzuki" "width" "complete class"`
- `site:github.com "Kourovka" "20.81"`
- `"Kourovka" "20.81" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR "EulerSolve" OR "ProofForum")`
- `"Baer-Suzuki" "not" "extension" 2026`（近期过滤365天）

**待复核**

- Revin完整证明和上界的详细定理定位未取得；不把摘要核对写成全文审阅。

### QX-P-002380 @ 3c42cf81e6fddb5e

Kourovka 20.82：由元素阶集合唯一识别的有限群，其社会子群商是否必可解

原题与综述Problem 4.10互为肯定/反例问法，未获一般新解。旧卡把Suzuki参数2^7写成27，须修复示例。

**旧卡 → 本轮建议**

- P0：²B₂(27)及其平方、wreath底群 → ²B₂(2⁷)；标题‘社会子群’改为socle子群。 原稿上标在题卡转写中丢失。

**范围与直接证据**

- Suzuki群示例参数：**题面有误**。原综述用²B₂(2⁷)，不是²B₂(27)。后者不是该Suzuki群参数。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：20.82，印刷第170页。
- [Grechkoseeva等，Finite groups isospectral to simple groups](<https://arxiv.org/pdf/2111.15198>)：v3，§4.3；Theorems 4.6/4.7；Mazurov例；Problem 4.10，PDF第11–12页；全文相关段落已读取。

**实际检索路径**

- `"Kourovka" "20.82"`
- `"recognizable" "spectrum" "socle" "solvable"`
- `site:github.com "Kourovka" "20.82"`
- `"Kourovka" "20.82" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR "EulerSolve" OR "ProofForum")`
- `"recognizable" "spectrum" "socle" "2026"`（近期过滤365天）

**待复核**

- 2026有限单群识别工作的全部分类证明未重审；其范围即使成立也不自动涵盖非单socle一般情形。

### QX-P-002384 @ d0c63b45dcc7a595

Kourovka 20.99：两两不交的有限指数左陪集，其指数是否必有大的公因数

新增2026整数剩余类的渐近部分进展；另一个A₅-harmonic反例针对Ginosar问题，并不反驳Sun的gcd≥k。

**旧卡 → 本轮建议**

- P1：仅列k≤20的整数群情形 → 补Fornal–Sun2026渐近下界；Menon2026回答G-harmonic⇒Z-harmonic，不能写成Sun猜想反例。 

**范围与直接证据**

- 任意群的k个不交陪集存在gcd≥k的一对：**部分进展**。保留一般问题未取得完整解；Fornal–Sun 2026摘要报告Z情形近线性下界，弱于精确k且不是任意群结论。
- Menon 2026的适用范围：**部分进展**。(6,6,6,10,15)是A₅-harmonic非Z-harmonic的声明；其最大两两gcd为6≥5，不能作为Sun五陪集反例。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：20.99，印刷第173页。
- [Zhi-Wei Sun，A challenging problem on disjoint cosets](<https://mathoverflow.net/questions/316709/a-challenging-problem-on-disjoint-cosets>)：原作者问题、2004/2006出处、k≤4及p群线索；全文已读取。
- [Jan Fornal、Yu-Chen Sun，On the problem of large gcd for disjoint residue classes](<https://arxiv.org/abs/2607.24655>)：2026-07-27；摘要：max gcd ≫ k exp(-(2+o(1))√(log k/log log k))；官方索引摘要；abs/html直接读取DisabledError。
- [Murali Menon，Two Questions on G-harmonic Tuples](<https://arxiv.org/abs/2608.15873>)：2026-08-16；摘要；tuple(6,6,6,10,15)；官方索引摘要；原站全文与摘要直接打开不可达。
- 本会话范围校核：gcd(6,6)=6，其他配对最大不超过6，k=5。

**实际检索路径**

- `"Sun" "disjoint cosets" "conjecture"`
- `"cosets" "greatest common divisor" "indices"`
- `site:github.com "Sun" "disjoint cosets" "conjecture"`
- `"Sun" "disjoint cosets" "conjecture" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR "EulerSolve" OR "ProofForum")`
- `"disjoint cosets" "gcd" 2026`（近期过滤365天）

**待复核**

- 两篇2026稿全文本轮不可达；应取得固定版本并核定理及证书后再强化证据等级。

### QX-P-002385 @ 4f78e3be345984ba

Kourovka 21.138：无限指数子群全自由的有限呈示群是否必为自由群或闭曲面群

一般无限有限呈示IF群问题与002331同题。已知单关系群、cubulated hyperbolic等子类结果仍不能闭合一般问题；Wilton机构仓储显示接受稿元数据。

**旧卡 → 本轮建议**

- P1：此前库内无精确同题 → 当前包内002331@89b68848f0121448与002385@4f78e3be345984ba为同题；只报告，不合并。 

**范围与直接证据**

- 一般无限有限呈示IF群必自由或闭曲面群：**部分进展**。原题与002331全文同量词；已知单关系群等范围不等于任意有限呈示IF群。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：21.138，印刷第200页。
- [Henry Wilton，Surface groups among cubulated hyperbolic and one-relator groups](<https://www.repository.cam.ac.uk/items/76d66a8f-f767-4feb-b0f7-010c9486bc58>)：accepted version；peer-reviewed元数据；DOI 10.17863/CAM.125292；出版元数据已读；仓储PDFembargo；arXiv:2406.02121v3原站HTML/PDF本轮不可达。
- [随包002331全文](<https://www.qunxingmath.org/p/QX-P-002331/>)：card_rev 89b68848f0121448；题面与2385逐项核对；全文已读取；历史检索不计作本次。

**实际检索路径**

- `"Surface groups among cubulated hyperbolic and one-relator groups"`（近期过滤365天）
- `"infinite index subgroups" "free" "finitely presented" conjecture`
- `site:github.com "Surface groups among cubulated hyperbolic and one-relator groups"`
- `"Surface groups among cubulated hyperbolic and one-relator groups" (site:mathoverflow.net OR site:zenodo.org OR site:aixiv.org OR "EulerSolve" OR "ProofForum")`

**待复核**

- 本题源稿定理细节交叉参见同批002331的实际原文证据；本条自身不宣称成功读取arXiv v3全文。

### QX-P-002387 @ 58b48e7110bee5a4

Kourovka 21.144：Thompson 群 F 的子群是否必为初等可均群或含 F 副本

原二分未取得新解；旧卡多处辅助断言不正确：非阿贝尔单群可以初等可均、并非每个F的有限指数子群都同构F，而含F′确实足以含F副本。

**旧卡 → 本轮建议**

- P0：F′非阿贝尔单，所以不能EA → 删除该错误一般引理，按原论文给F非EA的专门论证。 有限非阿贝尔单群本身属于EA。
- P0：有限指数H≤F仍同构F → 有限指数H包含F′，因而含F副本；并非所有H同构F。 Bleak–Wassink原摘要明确区分两类。
- P0：含F′不能直接证明含F → F′含F副本，因此含F′是含F副本的充分条件，但非必要等价。 利用内部区间支撑副本。
- P1：闭包不是子群 → 这里的closure是F的一个子群，通常比原H大；从closure含F不能推H含F。 修正对象类别并保留真正的逻辑障碍。

**范围与直接证据**

- 每个H≤F是初等可均或含F副本：**部分进展**。既有正规、有限指数等特殊情形和EA复杂性构造不决定任意子群。
- 题卡论证与边界：**题面有误**。A₅已反驳‘非阿贝尔单群不可能EA’；Bleak–Wassink分类明确存在不与F同构的有限指数子群；F′包含支撑在内部二进区间的F副本，因此H≥F′足够。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：21.144，印刷第200页。
- [Bleak–Brin–Moore，Complexity among the finitely generated subgroups of Thompson’s group](<https://ems.press/content/serial-article-files/37139>)：J.Comb.Algebra5(2021),1–58；Introduction及Conjectures 1–2；DOI 10.4171/JCA/49；全文相关段落已读取。
- [Bleak–Wassink，Finite index subgroups of R. Thompson's group F](<https://arxiv.org/abs/0711.1014>)：摘要：分类与F同构和不与F同构的有限指数子群；原站摘要已读取。
- 本会话直接数学校核：EA类含所有有限群，故A₅是反例。内部dyadic区间上的F经缩放嵌入F′。对有限指数H取正规核，非平凡正规核含F′，故H含F副本。

**实际检索路径**

- `Thompson F subgroup elementary amenable contains F conjecture 2026`（近期过滤365天）
- `"Thompson" "finite index" "isomorphic" "Wassink"`
- `site:github.com "Thompson" "elementary amenable"`
- `"Thompson F" "contains a copy" MathOverflow AI Lean`

**待复核**

- 所有修正涉及辅助论证；未将其误标为Brin–Sapir一般二分的解决。

### QX-P-002388 @ ea176ee65162a0d7

Kourovka 21.146：F_{n-1} 型群是否总能嵌入 F_n 型群

新增覆盖原题的完整证明声明：OpenAI2026-09-23声称单个F∞群容纳所有有限呈示群。已取得固定提交的原稿源及Lean端点；未重跑，未审完依赖。旧卡F∞定义及无条件F₁→F₂断言同时错误。

**旧卡 → 本轮建议**

- P0：未发现升层或统一F∞宿主证明 → 改为完整证明声明待核；记录2026-09-23原稿主定理、固定提交、Lean端点和本轮未重跑限制。 
- P0：type F∞等价于有限CW分类空间/有限总胞腔 → type F∞为各维骨架有限，允许无限维与无限总胞腔；按通常记号，type F另指有限BG；Notebook 21.146 原文则临时把 F 用作 F∞，引用时应注明该局部记号。 原题与公开代码均用每维有限。
- P0：每个有限生成群可嵌入有限呈示群，F₁→F₂经典已知 → 有限生成递归呈示群可嵌入有限呈示群；无递归呈示假设的全称断言删除。 Higman定理缺失关键有效性假设。

**范围与直接证据**

- n≥3的F_{n−1}群嵌入F_n群及F∞加强版：**完整证明/反例声明待核**。主定理声称固定H为F∞且每个有限呈示G嵌入H；因n≥3时F_{n−1}⇒有限呈示，若该声明成立即覆盖两问。
- F∞与Higman嵌入的定义：**题面有误**。F∞只要求每维胞腔有限，不是总胞腔有限/有限维BG。任意有限生成群未必嵌入有限呈示群；经典Higman定理需有限生成且递归呈示。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：21.146，印刷第200–201页。
- [OpenAI，A universal group of type F∞](<https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-universal-group-of-type-F-infinity-September-23-2026/build/sections/introduction.tex>)：固定SHA 3344da59991ed94f9ba711217b29c1d760badfa6；§1 Theorem thm:main及Corollary cor:recursive；原稿TeX引言、定理及universal.tex实际读取。
- [Lean实现端点](<https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/GroupTheory/UniversalGroup/Main.lean>)：OAI.UniversalFInfinity.universal_group_of_type_FInfinity；import UniverseTransport；同一固定SHA；已取得代码并核端点量词对应；未重跑。
- [公开形式化范围说明](<https://github.com/openai/math/blob/main/lean/docs/250.md>)：250.md；universal群段落与Comparator链接；已读取；报告形式化，不代表本会话独立验证。
- [独立陈述挑战](<https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/ComparatorChallenges/UniversalFInfinity.lean>)：HasTypeFInfinity定义与同名theorem占位目标；已读取；此挑战文件含sorry，不能用它替代Main.lean实现或推断整个实现只有占位。

**实际检索路径**

- `"universal group of type" "F" "2026" OpenAI`（近期过滤365天）
- `"every finitely presented group" "F_infinity" embedding`
- `site:github.com/openai/math "universal" "F-infinity"`
- `"Kourovka" "21.146" proof`

**待复核**

- 对Main.lean的HasTypeFInfinity实现定义、全部import、公理/占位、构建环境与证书仍需独立审计；本轮不执行未审查外部代码。
- 正文额外‘有限生成子群恰为递归呈示群’不包含于已读Lean端点；不要混作形式化覆盖范围。

### QX-P-002389 @ cf0c00d7d3c3e583

Kourovka 21.22：两个有限生成 Hopfian 群的限制 wreath product 是否仍 Hopfian（2026 声称否定）

维持2026完整反例声明待核；作者给出由群代数单侧逆元到非Hopfian限制wreath积的归约，真正未决的核验重点在上游直接有限性反例。另有组合/置换wreath积结果，不能直接替换正则限制wreath积。

**旧卡 → 本轮建议**

- P0：2026声称否定 → 保留完整反例声明待核，链接002361上游群代数输入，区分已刊归约与待核输入。 

**范围与直接证据**

- 两个有限生成Hopfian群的标准限制wreath积仍Hopfian：**完整证明/反例声明待核**。Kriebel声称C₂ wr H非Hopfian且H有限生成Hopfian；归约以OpenAI群代数ab=1≠ba输入为基础。已刊Bradford–Fournier-Facio框架支持该桥接，但本轮未独立核上游全证明。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：21.22，印刷第182页。
- [Alec Kriebel，Two consequences of group-algebra and planar Fourier certificates](<https://aleckriebel.com/research/wreath-products-planar-triangle-bounds/>)：2026-10-06,v1.0.0；群论半部；DOI 10.5281/zenodo.23203143；作者网页全文已读。
- [Bradford–Fournier-Facio，Hopfian wreath products and the stable finiteness conjecture](<https://link.springer.com/article/10.1007/s00209-024-03589-3>)：Mathematische Zeitschrift308(2024),58；Theorem 4.4及稳定有限性等价；出版社搜索完整段落与机构接受稿记录已取得。
- [Mghirbi–Douglas，Kaplansky’s conjectures fail for torsion-free hyperbolic groups in positive characteristic](<https://arxiv.org/html/2611.04599v1>)：Abstract/Main Theorem及作者对形式化范围的说明；2026-11-03；原站HTML已读；详细上游初查见002361。

**实际检索路径**

- `"Kourovka" "21.22" "Kriebel"`（近期过滤365天）
- `"Hopfian" "wreath" "2026" Kriebel`（近期过滤365天）
- `"Hopfian" "wreath product" "direct finiteness"`
- `site:github.com "Hopfian" "wreath" Lean`
- `"Hopfian wreath products" proof AI`

**待复核**

- 未独立运行上游Lean；未把作者报告或群论归约检查升级为群代数反例独立验证。
- Kochloukova arXiv:2602.19235涉及combinatorial wreath products，作用X可能非正则，不可单凭标题关闭本题。

### QX-P-002390 @ baab676256ee237f

Kourovka 21.35：多线性换位子值的阶条件是否迫使言语子群 p-幂零

Nilradical完整声明仍待核。本轮静态读到了固定提交的Lean实际端点：结论保留两个显式数学假设，并非无条件完整CFSG形式化；作者报告的Lean/Nanoda检查没有在本会话重跑。

**旧卡 → 本轮建议**

- P0：作者声称已形式化 → 本轮已核固定端点对应、未重跑；两个未形式化结构定理仍为参数。Kourovka♯不能改写为确认解∗。 

**范围与直接证据**

- 多线性换位子值阶条件⇒w(G)有正规p补：**完整证明/反例声明待核**。端点覆盖原题的任意多线性词及混合p可整除阶y，但以MinimalSimpleClassification与QuasisimpleCoprimeCommutators为显式参数。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：21.35，印刷第184页（♯）。
- [Nilradical，Kourovka21.35 result record](<https://nilradical.ai/results/kourovka-21-35/>)：v1.0.0，2026-09-21；conditional proof与verification说明；网页已读；他人报告Lean/Nanoda验证。
- [Lean实际端点](<https://github.com/alunik/kourovka-lean/blob/eb026951d20b1a362c7ec206ac116cd55547e96d/Kourovka/Problem2135/Kourovka2135/ProblemComplete.lean>)：problem2135_outerWord、problem2135、productOrderCondition_iff_hasNormalPComplement；SHA eb026951d20b1a362c7ec206ac116cd55547e96d；已取得代码并核定理对应；保留两项假设；未重跑。
- [A p-nilpotency criterion for multilinear commutator words](<https://nilradical.ai/notes/kourovka-21-35/>)：The question and the answer；Credit and the formal record；正文检索段落已读。

**实际检索路径**

- `"Kourovka" "21.35" multilinear commutator`（近期过滤365天）
- `"Kourovka" "21.35" "2026"`（近期过滤365天）
- `"multilinear commutator" "normal p-complement" "coprime"`
- `site:github.com "Problem2135"`
- `"Kourovka 21.35" Nilradical proof review`

**待复核**

- 须独立检查两个输入结构定理在有限群、宇宙与量词上的对应关系，并审全部依赖/构建日志；本轮只作初查。

### QX-P-002391 @ 9ee791fb7a596104

Kourovka 21.36：tdlc 群的 Kropholler 层级是否对 profinite 扩张封闭

发现需优先校勘的核与商方向差异。按本次核得的通常群类乘积约定，原式(HαK)K是HαK正规子群、profinite商；卡片写成profinite核。后者可直接作超限拉回归纳，不能作为原式的解答。正式入库前仍须核对原提出人的记号约定。

**旧卡 → 本轮建议**

- P0：N是profinite，Q∈HαK；不是商为profinite → 按本次核得的通常类积约定，建议校正为N∈HαK、Q为profinite；拓扑短正合列须含闭正规核与商拓扑。正式入库前再核原提出人记号。 卡片的短正合列与通常类积顺序不符，会改变主问题；1993原稿尚不可达，该限制须与校勘建议一起保留。
- P0：离散原型也是有限核 → 原式的右乘有限群类表示有限商，即有限指数扩张。 同一类积约定的方向需一致。

**范围与直接证据**

- 题卡等价短正合列及‘核为profinite’边界：**题面有误**。按本次核得的通常类积XY约定，N◁G且N∈X、G/N∈Y。建议将短正合列校正为N∈HαK、G/N∈K，并在入库前复核原提出人的记号。卡片的profinite核版本是另一方向；对闭正规核、商拓扑及连续开商映射的拓扑短正合列，可作超限拉回归纳。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：21.36，印刷第184页；15.45，第92页。
- [Januszkiewicz–Kropholler–Leary，Groups possessing extensive hierarchical decompositions](<https://math.osu.edu/sites/math.osu.edu/files/09-07-MRI-preprint.pdf>)：§1定义；§2 Proposition 2.7中finite extension用法；原作者PDF全文相关定义已读。
- 本会话对卡片字面核版本的校核：前提：连续拓扑短正合列，核闭正规、商取商拓扑（商映射开）。α=0：profinite核与profinite商的扩张仍profinite。后继：将Q作用经G→Q拉回，细胞稳定子为N对Q稳定子的扩张，归纳仍在低层且开。极限：取已在的更低层。只证明卡片核方向，不证明原式的profinite商方向。

**实际检索路径**

- `"Kropholler" "profinite extensions" hierarchy 2026`（近期过滤365天）
- `"Cook" "hierarchy" "profinite" "extensions"`
- `site:github.com "21.36" "Kourovka"`
- `"Kropholler" "profinite" MathOverflow AI`

**待复核**

- 1993原始全文入口不可达；方向校勘依据原题公式、群类乘积常规约定及后续作者原稿的finite-index用法，建议正式入库前再与原提出人约定核对。
- 本会话未取得profinite商方向的证明；不得把字面核方向的短证明标作21.36已解。

### QX-P-002392 @ 43678a5b3637fc55

Kourovka 21.45：是否存在需要三个以上生成元的有限呈示无限单群

一般存在性问题与002332同题。Ferudun2026仅排除Radu具体候选，原卡已收该进展，本轮重新核对了作者公开声明的范围。

**旧卡 → 本轮建议**

- P1：相邻非二生成问题 → 与002332@595672dd2fdf95a1完全同题；原题要求d(G)>2，不要求恰好d(G)=3。 

**范围与直接证据**

- 存在有限呈示无限单群且最小生成数>2：**部分进展**。Ferudun给Radu Corollary IV(ii)群的具体生成对；它只排除一个候选，不能证明所有有限呈示单群二生成。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：21.45，印刷第185页。
- [Alper Ferudun，An Explicit Generating Pair for Radu's Simple Tree Lattice](<https://eulersolve.org/papers/aim-geometric-group-theory-0126/>)：2026-10-14；Theorem 1/摘要：x₁x₃,x₁y₃；原群Corollary IV(ii)；作者正文已读；本题读取中的PDF带版本查询入口失败，关联题002332另取得PDF。

**实际检索路径**

- `"finitely presented simple" "two-generated" "2026"`（近期过滤365天）
- `"Radu" "Ferudun" "two" generators`
- `site:github.com "simple group" "three generators" Lean`
- `"Kourovka" "21.77" proof AI`
- `"Kourovka" "21.45" (proof OR Lean OR github)`

**待复核**

- 具体候选的生成对不是对一般存在命题的否定证明；本轮未独立重跑形式化。

### QX-P-002393 @ 1ac955ac3151e9e4

Kourovka 21.46：是否存在有限呈示且整数上同调维数大于 2 的无限单群

未发现同时满足有限呈示、无限单与2<cd_Z<∞的可核验新例。Fournier-Facio–Sun的高维例明确不是有限呈示；旧卡由gd≥cd推出gd∞⇒cd∞的推理方向错误。

**旧卡 → 本轮建议**

- P1：由于gd≥cd_Z，gd=∞所以cd_Z=∞ → 补正确上界gd≤max{3,cd_Z}或原文专门论证；仅保留已证结论而撤去错误推理。 反向使用不等式。

**范围与直接证据**

- 存在有限呈示无限单群，2<cd_Z(G)<∞：**部分进展**。高有限维的有限生成例不满足有限呈示；F∞宿主声明也不保证有限上同调维数。
- 几何维数与上同调维数推理：**题面有误**。只由gd≥cd不能推出gd=∞⇒cd=∞；应另引用gd≤max{3,cd_Z}或原构造的直接无穷维论证。结论可成立，但现有理由不成立。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：21.46，印刷第185页。
- [Fournier-Facio–Sun，Dimensions of finitely generated simple groups and their subgroups](<https://arxiv.org/html/2503.01987v3>)：Introduction；Remark 4.4；Corollary 5.2；原站HTML相关段落已读。
- 本会话逻辑方向核对：a≥b且a=∞不强制b=∞；需要另一个上界或独立结构证据。

**实际检索路径**

- `"finitely presented" "simple" "finite cohomological dimension" "2026"`（近期过滤365天）
- `"simple groups" "2 <" "cohomological dimension"`
- `site:github.com "simple" "cohomological dimension" Lean`
- `"Kourovka" "21.78" proof AI`
- `"Kourovka" "21.46" (proof OR Lean OR github)`

**待复核**

- 未逐项重审旧卡列的全部2025–2026相邻构造；各类部分结果不能组合成同一个满足全部条件的群。

### QX-P-002395 @ e7444264be5ec9f5

Kourovka 21.59(a)：几乎单群是否由不可约特征标次数的多重集唯一确定

保留几乎单群与准单群、次数多重集与次数集合的区别。新核到Vasil’ev2026综述已正式刊于Algebra and Logic，属于书目更新；全文本轮不可读，不据此推定(a)已解。

**旧卡 → 本轮建议**

- P2：Vasil’ev arXiv:2608.12783预印本 → 可补正式期刊DOI与卷页，同时注明本轮未读取全文；状态不据元数据升级。 

**范围与直接证据**

- 2026综述的发表信息：**部分进展**。Vasil’ev综述已于2026-10-15发表，Algebra and Logic65,21–29；仅核出版信息与摘要，不声称读到全文新定理。
- [原题](<https://arxiv.org/pdf/1401.0300v50>)：21.59(a)，印刷第188页。
- [A. V. Vasil’ev，Arithmetic Invariants for Finite Simple and Related Groups](<https://link.springer.com/article/10.1007/s10469-026-09851-3>)：2026-10-15；Algebra and Logic65,21–29；DOI10.1007/s10469-026-09851-3；出版社元数据/摘要可读，正文订阅墙；arXiv:2608.12783v2 html/pdf不可达。

**实际检索路径**

- `"almost simple groups" "character degrees" "2026" Vasiliev`（近期过滤365天）
- `"almost simple" "multiset" "character degrees"`
- `site:github.com "21.69" "character"`
- `"Kourovka" "21.69" proof AI`
- `"Kourovka" "21.59" (proof OR Lean OR github)`

**待复核**

- 取得综述全文后核定其关于almost simple与quasisimple的详细范围；本轮只核到原题及发表信息。

### 本节新增及待定查重线索

指定配对的完整结论已归入JSONL；以下保留新发现的同题、方向联系和仅索引候选。

- QX-P-002370 @ 8b6b58870576e287 ↔ QX-P-002371 @ 730ceee348cbc418：**相关但不等价**。20.43肯定会排除20.42强读法正例；20.43否定不自动构造非可均群。保留方向性联系。
- QX-P-002372 @ bebcaffd0e6ec3bd ↔ QX-P-001551 @ 4ed88c2438602e32：**待定**。全库2469条索引中原题编号/英文题面高度匹配；尝试对方链接不可达，不能仅凭标题认定等价。
- QX-P-002373 @ 462eac8ffa9d3475 ↔ QX-P-001552 @ a55e1b96e28913d3：**待定**。全库2469条索引中原题编号/英文题面高度匹配；尝试对方链接不可达，不能仅凭标题认定等价。
- QX-P-002374 @ 0f3f758bf7d0f694 ↔ QX-P-000953 @ 97663efd1b9fff0c：**待定**。全库2469条索引中原题编号/英文题面高度匹配；尝试对方链接不可达，不能仅凭标题认定等价。
- QX-P-002376 @ 2aa5b8bf71fd689b ↔ QX-P-000534 @ 4c94645497e102db：**待定**。全库2469条索引中原题编号/英文题面高度匹配；尝试对方链接不可达，不能仅凭标题认定等价。
- QX-P-002378 @ e2fdd45bc0bfe932 ↔ QX-P-000957 @ c598a6332629bda3：**待定**。全库2469条索引中原题编号/英文题面高度匹配；尝试对方链接不可达，不能仅凭标题认定等价。
- QX-P-002379 @ ca8c43ef35a38059 ↔ QX-P-000142 @ 390d1908032d29b3：**待定**。全库2469条索引中原题编号/英文题面高度匹配；尝试对方链接不可达，不能仅凭标题认定等价。
- QX-P-002380 @ 3c42cf81e6fddb5e ↔ QX-P-000535 @ c293e2259a2fc4b8：**待定**。全库2469条索引中原题编号/英文题面高度匹配；尝试对方链接不可达，不能仅凭标题认定等价。
- QX-P-002381 @ b5cf1fe2df813dfb ↔ QX-P-001557 @ f8d22864d1efb6e1：**待定**。全库2469条索引中原题编号/英文题面高度匹配；尝试对方链接不可达，不能仅凭标题认定等价。
- QX-P-002383 @ b597fca6bba7b359 ↔ QX-P-000959 @ fd05405591d79bc4：**待定**。全库2469条索引中原题编号/英文题面高度匹配；尝试对方链接不可达，不能仅凭标题认定等价。
- QX-P-002384 @ d0c63b45dcc7a595 ↔ QX-P-000059 @ ac6c747c063c9e39：**待定**。全库2469条索引中原题编号/英文题面高度匹配；尝试对方链接不可达，不能仅凭标题认定等价。
- QX-P-002385 @ 4f78e3be345984ba ↔ QX-P-002331 @ 89b68848f0121448：**同题**。均为无限有限呈示群所有无限指数子群自由⇒自由或闭曲面群，含有限/无限生成子群的全称量词相同；同为Kourovka21.138。
- QX-P-002392 @ 43678a5b3637fc55 ↔ QX-P-002332 @ 595672dd2fdf95a1：**同题**。均问有限呈示无限单群d(G)>2，非恰好3生成；已对照完整题面。

## 八、后续复核顺序与本轮边界

1. 先修正会改变命题含义的参数、公式、定义和量词：尤其2319、2336、2348、2357、2371、2372、2388、2391。2391的校勘依现有来源，须把原提出人记号未最终核定的限制一起保留。
2. 再审直接覆盖原主问题的新完整声明：2316、2330、2339、2388，以及本轮重新厘清的Kakeya、Kaplansky等声明。先核原稿版本、完整假设和目标语义，再决定是否进行大型证书或形式化重建。
3. 修正旧证明或新稿范围：2343的旧归约证明错误、2337的非平凡单位范围与未复跑证书、2338所有已证子类的实系数假设、2390显式保留的数学参数。
4. 三组同题关系可供人工维护时考虑；其它待定候选先取双方完整题面，不能依标题或相邻编号合并。

全部100题的本轮初查已经完成。待复核清单表示后续深入数学审计、缺失全文与维护决策，不把这些环节伪装成已经完成。没有全量追踪所有引文，没有扫描全库2469张卡的全部正文，没有执行外部证明工程。历史题卡中的计算或验证没有计为本轮执行。

交付JSONL的`math_results.status`统一使用包内允许的八类状态；`conclusion`保存该子问的具体结论，证据和形式化层级另列。所有线上写入标志均为false。原始网页长文与工具抓取全文未收入回传包。
