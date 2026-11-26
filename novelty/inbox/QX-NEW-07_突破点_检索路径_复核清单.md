# QX-NEW-07 · 突破点、检索路径与复核清单

查核日期：2026-11-26（Asia/Shanghai）  
批次范围：包内100题；保留原 `id`、`card_rev`、`batch_id`。

## 阅读口径

本轮是按题初查。下面记录会影响题面、来源、子问状态、形式化判断或查重的发现；未命中事项的完整记录在逐题 JSONL。数学结论与证据强度分列，作者声明不等同于独立验证，来源写有“open”也不等同于本轮证明其仍开放。

全文不可达、仅摘要、撤回记录、静态读取代码与未重跑均按实际情况标注。所有线上题卡写入、合并、发帖均为零。指定31对均按双方给定版本正文复核；新候选只作线索报告。

## 优先处理

| 题号 | 本次最重要的变化 | 保留的边界 |
|---|---|---|
| 002182 | 已刊结果结合定义桥接覆盖 Problem 15(a)、(b) | (c) 的额外非嵌入要求未关闭；桥接论证与文献原定理分开列出 |
| 002181 | Brouwer 1976 可度量例子覆盖原帖三个存在性子问 | 非可分的存在性与可分情形分开 |
| 002111 | Kenyon Theorem 1 给相邻边长矩形最少方块数 Θ(log n) | 首次需要 15–18 块的具体阈值未关闭 |
| 002114 | 同源/好素数结论有正式出版依据；非极小整模型的全素数点数读法有小反例 | 不反驳正确的局部 L 因子或极小模型版本 |
| 002112 | 有理集合构造经清分母可用于整数三集合 | 任意大规模、沿构造族；不是每个 n 的最优值或精确渐近 |
| 002156 | 2026-10-28 勘误要求补 Hypothesis V | 按修订定理的完整假设使用，不外推一般 Selberg 类 |
| 002134 | 新发现公开完整凸体反例声明 | 保持声明待核；一般测度反例与均匀体积原问隔离 |
| 002079 / 002082 / 002151 | 公开形式化声明及实际代码入口需要分别核范围 | 本轮独立 Lean 重跑为零；相邻结论不自动解决原问 |
| 002093 / 002149 | 旧反驳理由或宽字面反例的范围必须限定 | 不把定向限制或非等模反例用于更窄的原始问题 |

背景和相关变体使用 `background_results`、`related_variant_results` 单独保存；`math_results` 不据这些扩展字段自动改整卡状态。

---

# A组重点发现（QX-P-002078—002104）

查核日期：2026-11-26（Asia/Shanghai）。以下仅收题面、状态、文献或查重的实质变化。

## QX-P-002078 · 1c15e4f8935bfa02

**旧卡**：大量整同调 3-球面？（原记录 open）。

**本次变化**：原卡漏掉三角剖分复杂度 N。新增 2025 图同调基构造论文及 2026 三维球面计数预印本线索，均不能当作整同调三球面超指数下界的完成证明。

**量词和范围**：按含 N 个单形的组合三角剖分计数整同调三维球面，问 C^N 型指数上界的加强猜想是否已知为假；须固定复杂度与组合等价口径。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/87393/are-there-lots-of-integer-homology-three-spheres) — 原问正文；必要时注明追加/update/评论。按含 N 个单形的组合三角剖分计数整同调三维球面，问 C^N 型指数上界的加强猜想是否已知为假；须固定复杂度与组合等价口径。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。
- [Adiprasito–Lackenby–Souto–Yashfe: On graphs, homology bases, and triangulated homology spheres](https://people.maths.ox.ac.uk/lackenby/homology_spheres_preprint_draft.pdf) — Theorem 4、Corollary 5，PDF 第2页；arXiv:2509.06275。比较 H1(-;F)=0 的流形三角剖分计数与有短同调基的图；高维超指数增长推出三维对应增长是条件性归约。 访问：全文已读关键段落；验证：仅本次文献与范围核对；未独立重证。
- [Durhuus–Pavelka: Counting Triangulated 3-Spheres, Nuclei, and Polyhedra](https://arxiv.org/abs/2611.16518) — 2026-11-12 摘要。摘要给出若干指数计数问题的等价归约，不能据此宣布整同调三球面计数问题解决。 访问：搜索索引摘要；原站全文不可达；验证：仅本次文献与范围核对；未独立重证。

**实际搜索路径**：原题完整URL打开；学术查询 `counting triangulations integral homology three spheres exponential bound`、`integer homology 3 spheres N tetrahedra C^N superexponential`；GitHub/代码查询 `site:github.com homology spheres exponential triangulations (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `homology spheres exponential triangulations (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**查重**：QX-P-000875@b6bf38b6713b455e → 相关但不等价：已读双方指定版本完整正文：2078问固定单形复杂度下三角剖分计数；0875问Θ³_Z→Θ³_Z/2的核/光滑4球填充。计数问题与配边核存在性不同，不能合并。

**待复核**：核 2611.16518 的全文与版本历史；其原站 abs/html 本轮不可达。

## QX-P-002079 · 558f18b4f6ca0792

**旧卡**：熵多项式下界不等式（三元 SOLVED_CLAIMED=Lean 4；n 元开放）（原记录 partially_solved）。

**本次变化**：三元不等式有 Zenodo 完整证明与 Lean 制品声明；本轮读到记录页而未取得可核的 PDF/代码包，保持声明待核。n 元追加公式单列，本轮未找到可验证解答。

**量词和范围**：分开三元 Shannon 熵的特定多项式下界与 11月3日新增的 exp(H(x)) ≥ Σ_{k=1}^n k·k!·e_k(x)（n≥3）。后一式不是把前三元公式直接替换变量个数。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://math.stackexchange.com/questions/5149777/a-polynomial-lower-bound-for-e-sum-x-i-ln-x-i) — 原问正文；必要时注明追加/update/评论。分开三元 Shannon 熵的特定多项式下界与 11月3日新增的 exp(H(x)) ≥ Σ_{k=1}^n k·k!·e_k(x)（n≥3）。后一式不是把前三元公式直接替换变量个数。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。
- [A Polynomial Lower Bound for Ternary Shannon Entropy: Proof and Lean 4 Formalization](https://zenodo.org/records/23176453) — Description / Files / version v1；DOI 10.5281/zenodo.23176453。作者报告三元原不等式和等号的证明及 Lean 验证；记录称最优系数仅在数学稿中证明。 访问：记录页全文；PDF/ZIP 下载入口失败；验证：他人声称已形式化验证；本轮未取得可执行制品、未重跑。

**实际搜索路径**：原题完整URL打开；学术查询 `A Polynomial Lower Bound for Ternary Shannon Entropy Proof Lean Formalization`、`entropy exp sum k k! elementary symmetric polynomials inequality Dang Dang`；GitHub/代码查询 `site:github.com ternary Shannon entropy polynomial lower bound (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `ternary Shannon entropy polynomial lower bound (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**待复核**：取得 Zenodo PDF 与 TernaryEntropyLean-v1.0.0.zip，核定理、边界、等号及公理闭包；最优系数未包含在作者所述 Lean 形式化范围。

## QX-P-002081 · f6cd731e734ba508

**旧卡**：无有限完备重写系统的双曲群（原记录 open）。

**本次变化**：Gray–Linton 2026 Theorem 1.6 提供明确部分进展：局部拟凸且虚紧特殊的双曲群及其有限生成子群有有限完备重写系统；未覆盖任意双曲群。

**量词和范围**：是否存在对任何有限生成集都不具有限完备重写系统的 word-hyperbolic 群；判单位元的 Dehn 系统不等于全局终止且合流的系统。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/136806/what-is-an-example-of-a-word-hyperbolic-group-without-a-finite-complete-rewritin) — 原问正文；必要时注明追加/update/评论。是否存在对任何有限生成集都不具有限完备重写系统的 word-hyperbolic 群；判单位元的 Dehn 系统不等于全局终止且合流的系统。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。
- [Gray–Linton: Finite complete rewriting systems for graphs of free groups...](https://arxiv.org/abs/2607.07496) — Theorem 1.6（印刷页3–4）；Theorem 1.5；Corollary 1.7。有限生成 virtually free-by-cyclic 群与上述双曲子类有系统；不能把加入自由积因子后的结论去掉因子。 访问：arXiv 搜索摘要；原作者稿镜像全文已读；验证：仅本次文献与范围核对；未独立重证。
- [同一原稿的公开全文镜像](https://www.researchgate.net/publication/408623283_Finite_complete_rewriting_systems_for_graphs_of_free_groups_with_applications_to_free-by-cyclic_one-relator_and_three-manifold_groups) — Introduction、Theorem 1.6。核到局部拟凸与 virtually compact special 两个假设及子群算法范围。 访问：全文已读关键段落；验证：仅本次文献与范围核对；未独立重证。

**实际搜索路径**：原题完整URL打开；学术查询 `Gray Linton finite complete rewriting systems hyperbolic groups 2026`、`hyperbolic group finite convergent rewriting system locally quasiconvex virtually special`；GitHub/代码查询 `site:github.com hyperbolic groups finite complete rewriting (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `hyperbolic groups finite complete rewriting (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**待复核**：原 arXiv 页面不可达；本轮核对了原作者稿的公开全文镜像。后续核正式修订与依赖定理。

## QX-P-002082 · 39bf62e887758c51

**旧卡**：GL(n) 的 Siegel–Landau 零点缺失（原记录 open）。

**本次变化**：修正题面，并补核 OpenAI GL(1) 文献/代码链：旧卡“无 Lean 形式化”已不准确；实际声明仍属 Dirichlet/特定 Hecke 情形，不能移植为任意 GL(n) 结论。

**量词和范围**：数域上的自对偶尖点自守表示 GL(n)，重点 n≥4；原问为其标准 L 函数排除 Siegel–Landau 异常实零点。一般允许例外零点的零点自由区域不能回答原问。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/223829/no-siegel-landau-zeros-for-mathrmgln) — 原问正文；必要时注明追加/update/评论。数域上的自对偶尖点自守表示 GL(n)，重点 n≥4；原问为其标准 L 函数排除 Siegel–Landau 异常实零点。一般允许例外零点的零点自由区域不能回答原问。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。
- [OpenAI Lean scope 003](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/003.md) — Scope；固定提交 adc7f1241b42e322a6451854ab7e4b4c146bf78a。说明 Dirichlet 实零点满足统一正对数间隙；亦有 Dirichlet 7/8 与特定 Hecke 声明，不含任意 GL(n)。 访问：全文已读关键段落；验证：已读范围说明；未重跑。
- [SiegelZeros 真正证明入口及定理](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/SiegelZeros/Conclusions/Theorem.lean) — OAI.SiegelZeros.WeightedTorusJets.exists_absolute_real_zero_gap；另 Characters/DirichletRealZeroBoundProof.lean。q≥3、primitive nonprincipal real Dirichlet character、0<β<1 的统一间隙。Main.lean 为导入入口；ComparatorChallenges 中 sorry 是挑战模板，不是这一证明文件。 访问：GitHub connector 取得文本并静态读取；验证：已核相邻定理对应、未重跑；未审计全部传递依赖。
- [Tao: A sketch of the proof of non-existence of Siegel zeroes](https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/) — 2026-10-19 正文及 Banks/Kerr/Green 文献链接。提供 GL(1) 证明解释和后续简化来源；未给一般 GL(n) 排除。 访问：全文已读关键段落；验证：仅本次文献与范围核对；未独立重证。

**实际搜索路径**：原题完整URL打开；学术查询 `absence Siegel zeros self dual GL n cuspidal automorphic representations`、`GL4 exceptional zeros Langlands functoriality Siegel Landau zeros general n`；GitHub/代码查询 `site:github.com Siegel Landau zeros GL(n) (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `Siegel Landau zeros GL(n) (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**待复核**：若深查 GL(1) 形式化，需重跑并核传递依赖、公理；若要解决 GL(n)，须给出明确自守推广桥接。

## QX-P-002083 · b941059c6b0fca8e

**旧卡**：Julia 集上的丢番图逼近（原记录 open）。

**本次变化**：人话版把周期点及其代数次数改写成有理数 p/q 和分母，是实质换题。Hill–Velani 的 expanding map 逆像点/压力维数定理是邻近结果，不直接回答本题。

**量词和范围**：有理映射 f 的周期/预周期点 y 逼近 Julia 集中的 x，复杂度取 [F(y):F]（或另问周期）；问 Brolin–Lyubich 测度几乎处处的 Diophantine 性及每点可逼近性。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/233020/diophantine-approximation-in-the-julia-set) — 原问正文；必要时注明追加/update/评论。有理映射 f 的周期/预周期点 y 逼近 Julia 集中的 x，复杂度取 [F(y):F]（或另问周期）；问 Brolin–Lyubich 测度几乎处处的 Diophantine 性及每点可逼近性。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。
- [Hill–Velani: Metric diophantine approximation in Julia sets of expanding rational maps](https://www.numdam.org/item/10.1007/BF02699537.pdf) — Abstract 与 Theorem 1，PDF 第2–3页。适用 expanding rational maps；逼近点是 T^n(y)=z0 的逆像，半径由 Birkhoff 和控制，与本题代数次数不同。 访问：全文已读关键段落；验证：仅本次文献与范围核对；未独立重证。

**实际搜索路径**：原题完整URL打开；学术查询 `Diophantine approximation Julia set periodic points Dimitrov`、`rational map periodic points Galois degree d(y) Brolin Lyubich Diophantine approachable`；GitHub/代码查询 `site:github.com Julia Diophantine periodic points (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `Julia Diophantine periodic points (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**查重**：QX-P-001295@a5d4d2c8f8202193 → 待定：非Archimedean Julia中排斥周期点稠密性的标题线索；非指定对子，未读正文

**待复核**：补查专门使用代数次数衡量周期点的文献；不能以 expanding map 的逆像定理直接代入。

## QX-P-002084 · bc6f376fc12a562b

**旧卡**：三角范畴的张量积构造（原记录 open）。

**本次变化**：需将“任意给两个三角范畴造张量积”收窄到原问题的增强遗忘兼容性。公开索引命中相邻 aiXiv:2611.01442，但其记录已撤回且不构成本题证据。

**量词和范围**：问增强范畴 C,D 的张量积之同伦范畴能否仅由 Ho(C)、Ho(D) 恢复，亦即相应同伦范畴函子能否成为强对称幺半函子；并问最小必要附加结构。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/212543/a-tensor-product-for-triangulated-categories) — 原问正文；必要时注明追加/update/评论。问增强范畴 C,D 的张量积之同伦范畴能否仅由 Ho(C)、Ho(D) 恢复，亦即相应同伦范畴函子能否成为强对称幺半函子；并问最小必要附加结构。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。
- [aiXiv:2611.01442 撤回记录](https://aixiv.online/abs/2611.01442) — 记录页撤回通知：2026-11-17 12:55:02 UTC。搜到的 Deligne tensor 相关索引不能支持本题；原记录已撤回，PDF 返回404。 访问：撤回页已读；原 PDF 不可达；验证：排除为有效解答证据。

**实际搜索路径**：原题完整URL打开；学术查询 `tensor product triangulated categories homotopy stable infinity Schommer Pries`、`ho C tensor D recovered homotopy categories nonunique enhancements tensor counterexample`；GitHub/代码查询 `site:github.com triangulated categories tensor product (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `triangulated categories tensor product (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**待复核**：若采用非唯一增强反例，必须核实两个张量结果确实不同；本轮未完成此桥接。

## QX-P-002085 · 33ebddad2c3c7007

**旧卡**：无限群内同调相同的有限子群（原记录 open）。

**本次变化**：原卡丢掉“不相同构”及“两条包含到 K 都诱导整同调同构”。Culler 的有限群同调等价定理不能直接用于无限 K。

**量词和范围**：寻找不相同构的有限群 G,H 嵌入同一个无限群 K，且两条单射各自诱导整同调所有次数的同构；原作者偏好 perfect 的例子。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/238770/finite-groups-inside-an-infinite-group-with-the-same-homology) — 原问正文；必要时注明追加/update/评论。寻找不相同构的有限群 G,H 嵌入同一个无限群 K，且两条单射各自诱导整同调所有次数的同构；原作者偏好 perfect 的例子。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。
- [Culler: Homology equivalent finite groups are isomorphic](https://marc-culler.info/static/home/papers/HomologyFiniteGroup.pdf) — Proc. AMS 72(1), 1978, 218–220；Theorem，PDF第1页。若两个有限群之间的同态诱导整同调同构，该同态为同构。两端有限是关键，不能套向无限 K。 访问：全文已读关键段落；验证：仅本次文献与范围核对；未独立重证。

**实际搜索路径**：原题完整URL打开；学术查询 `Culler homology equivalent finite groups infinite group monomorphisms`、`finite subgroups G H infinite K integral homology isomorphisms nonisomorphic groups`；GitHub/代码查询 `site:github.com finite groups homology equivalent infinite (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `finite groups homology equivalent infinite (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**查重**：QX-P-000134@d7d03d474828f5de → 待定：有限群同调消失问题的标题线索；可能共享Culler背景，非指定对子，未读正文

**待复核**：新索引线索 QX-P-000134 需另行分配正文比较；本轮不合并。

## QX-P-002086 · 6d1c0b907e64f8c8

**旧卡**：素特征下约化李代数的定义缺失（原记录 open）。

**本次变化**：这是定义与刻画请求，不能把“Lie(G), G reductive”或特征零半单结构直接当成解答；人话版半单等于可对角化的表述不准确。

**量词和范围**：Humphreys 寻求素特征下纯李代数/受限李代数意义的合理约化定义及其与约化代数群李代数的关系。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/284713/is-there-a-reasonable-way-to-define-reductive-lie-algebra-in-prime-characteris) — 原问正文；必要时注明追加/update/评论。Humphreys 寻求素特征下纯李代数/受限李代数意义的合理约化定义及其与约化代数群李代数的关系。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。

**实际搜索路径**：原题完整URL打开；学术查询 `reductive Lie algebra prime characteristic definition Humphreys`、`restricted Lie algebra purely Lie theoretic characterization reductive algebraic group`；GitHub/代码查询 `site:github.com reductive Lie prime characteristic (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `reductive Lie prime characteristic (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**查重**：QX-P-002228@f861bfcb9e478192 → 待定：R_r约化李代数和Chevalley对合的标题线索；非指定对子，未读正文

**待复核**：需与提问者目标相符的受限李代数判据；库内 QX-P-002228 只有标题级线索。

## QX-P-002087 · 3d936d646cd3b872

**旧卡**：模 p 同构 ⇒ 微分同胚？（原记录 open）。

**本次变化**：原卡“实或复对象/任意整方程”过宽，应恢复 Q、smooth proper 与光滑约化。Serre 的数域共轭例不能未经桥接改成 Q 上反例。

**量词和范围**：Q 上光滑 proper 代数簇在某个素数有光滑同构约化，问复化后流形是否微分同胚；需指定整模型和共同好约化。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/364843/varieties-isomorphic-mathrmmod-p-are-diffeomorphic) — 原问正文；必要时注明追加/update/评论。Q 上光滑 proper 代数簇在某个素数有光滑同构约化，问复化后流形是否微分同胚；需指定整模型和共同好约化。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。

**实际搜索路径**：原题完整URL打开；学术查询 `varieties isomorphic mod p diffeomorphic smooth proper rational numbers`、`Serre conjugate varieties smooth reductions Q diffeomorphism integral models`；GitHub/代码查询 `site:github.com varieties isomorphic mod p diffeomorphic (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `varieties isomorphic mod p diffeomorphic (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**待复核**：后续重点核 Serre 共轭例与 Q/模型条件；Weil restriction 不能自动保留所需区别。

## QX-P-002088 · aa507b0b922a2469

**旧卡**：Noether 不等式普适性（题面修正）（原记录 open）。

**本次变化**：题名和人话版误归为 Noether 下界；原问是典范体积与全纯 Euler 特征的上界，且原文有明确高维公式。

**量词和范围**：X 为光滑射影 n 维复簇，K_X ample，问 K_X^n ≤ (−n−1)^n χ(O_X) 是否总成立，尤指 n≥4。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/389471/the-inequality-k-xn-leq-n-1n-chi-mathscro-x) — 原问正文；必要时注明追加/update/评论。X 为光滑射影 n 维复簇，K_X ample，问 K_X^n ≤ (−n−1)^n χ(O_X) 是否总成立，尤指 n≥4。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。

**实际搜索路径**：原题完整URL打开；学术查询 `canonical ample volume holomorphic Euler characteristic inequality (n+1)^n`、`K_X^n (-n-1)^n chi O_X inequality general type higher dimension`；GitHub/代码查询 `site:github.com canonical volume Euler characteristic inequality (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `canonical volume Euler characteristic inequality (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**待复核**：核高维例子的典范正性及 χ 符号；不能混用 Noether 的下界文献。

## QX-P-002090 · a115f7e16490c058

**旧卡**：不可达基数 κ→[κ]²₃ 与 κ→[κ]²₂ 等价？（原记录 open）。

**本次变化**：人话版把三色方括号关系误写成单色集合，并把显然蕴涵方向写反。两色关系（弱紧性）推出三色遗漏一色，原问是逆向。

**量词和范围**：方括号 κ→[κ]^2_r 表示每个 r 色染色有大小 κ 的子集遗漏至少一色；问不可达 κ 下 r=3 是否推出 r=2。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/461637/is-kappa-rightarrow-kappa2-3-the-same-as-kappa-rightarrow-kappa2) — 原问正文；必要时注明追加/update/评论。方括号 κ→[κ]^2_r 表示每个 r 色染色有大小 κ 的子集遗漏至少一色；问不可达 κ 下 r=3 是否推出 r=2。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。

**实际搜索路径**：原题完整URL打开；学术查询 `square bracket partition relation three colors inaccessible weak compact`、`kappa [kappa] 2 3 productive chain condition weak compactness Rinot`；GitHub/代码查询 `site:github.com square bracket partition inaccessible three colors (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `square bracket partition inaccessible three colors (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**待复核**：复核 productive κ-cc 等已知必要条件的精确量词，不能用两色有限迭代论证代替本问。

## QX-P-002091 · d46ad2afa444cc86

**旧卡**：区间中素数幂个数上界（原记录 open）。

**本次变化**：应从笼统开放界问题改为参考文献请求。Ramaré–Viswanadham Lemma14 覆盖 y≤2x 的加权情形；作者称另补 y>2x，但本轮未得其完整证明。

**量词和范围**：Helfgott 已宣称证明两条界，实际索求文献：(a) 无权素数幂个数≤2h/log h，h>1，有指定例外；(b) Π 的1/k加权差严格小于该值，无例外。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/461752/upper-bound-on-prime-powers-in-interval) — 原问正文；必要时注明追加/update/评论。Helfgott 已宣称证明两条界，实际索求文献：(a) 无权素数幂个数≤2h/log h，h>1，有指定例外；(b) Π 的1/k加权差严格小于该值，无例外。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。
- [Ramaré–Viswanadham: Modular Ternary Additive Problems with Irregular or Prime Numbers](https://ramare-olivier.github.io/Maths/SelbergIdentity-KVOR-21-withbib.pdf) — 2021-08-11 版本，Lemma14，PDF第12页（印刷页11）。A≥B>d≥1 的 Λ(m)/log m 进程界；原文明确必须保留 A≥B。 访问：全文已读关键段落；验证：仅本次文献与范围核对；未独立重证。

**实际搜索路径**：原题完整URL打开；学术查询 `Brun Titchmarsh prime powers Helfgott Ramare interval`、`Pi(y) Pi(x) 2 (y-x) log(y-x) prime powers exceptions 32`；GitHub/代码查询 `site:github.com Brun Titchmarsh prime powers (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `Brun Titchmarsh prime powers (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**待复核**：找覆盖 y>2x、严格性及无权例外的正式文稿/计算证书。

## QX-P-002092 · 0a554dcb1f087175

**旧卡**：s_n 素数项分布猜想（题面修正）（原记录 open）。

**本次变化**：补回精确渐近式。Formal Conjectures 已录入两个等价计数口径的命题，但固定版本均为 research open 且 by sorry，不是证明。

**量词和范围**：s_n=Σ_{k≤n}p_k；π_s(n)=#{k≤n:s_k 素}，猜想 π_s(n)~n/(2 log n)，并区分对偶数项 s_{2m} 的 m/log m 版本。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/434111/are-prime-numbers-among-sums-of-prime-numbers-distributed-as-frac-n2-lnn) — 原问正文；必要时注明追加/update/评论。s_n=Σ_{k≤n}p_k；π_s(n)=#{k≤n:s_k 素}，猜想 π_s(n)~n/(2 log n)，并区分对偶数项 s_{2m} 的 m/log m 版本。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。
- [Meštrović: Curious conjectures on the distribution of primes among the sums of the first 2n primes](https://arxiv.org/abs/1804.04198) — Conjecture3.3；2018摘要。原论文把偶数下标部分和的素数计数作为 conjecture，数值和启发不等于证明。 访问：摘要及来源定位；未逐页核证明（本就为猜想）；验证：仅本次文献与范围核对；未独立重证。
- [FormalConjectures / Mathoverflow / 434111.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/Mathoverflow/434111.lean) — MathOverflow434111.restricted_prime_number_theorem；variants.even_subsequence；约60/69行。两个目标均标 research open 并以 sorry 收尾；本轮已取得文件、toolchain 与 manifest。 访问：GitHub connector 取得代码，静态核对；验证：额外公理/占位：by sorry；不是完整证明；未重跑。

**实际搜索路径**：原题完整URL打开；学术查询 `Restricted Prime Number Theorem sums primes Mestrovic`、`prime partial sums s_n asymptotic n 2 log n conjecture`；GitHub/代码查询 `site:github.com 434111 Restricted Prime Number Theorem (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `434111 Restricted Prime Number Theorem (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**待复核**：后续应寻找针对稀疏序列的证明，不是一般 PNT；固定文件里的 sorry 不可标成机器验证完成。

## QX-P-002093 · 5e0e95f3eb4345c5

**旧卡**：近复结构细化版（字面版已否定）（原记录 partially_solved）。

**本次变化**：旧卡“字面版已否定”的所列证据不成立：反定向 CP² 只排除与该定向相容的结构；Kahn 所述是定向同伦等价，不是同胚。暂撤其反驳断言。

**量词和范围**：原问是不额外指定定向的光滑闭流形 M,N 同胚时，M 有 almost complex structure 是否推出 N 也有。须与指定定向相容和仅同伦等价版本分开。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/448318/does-the-existence-of-an-almost-complex-structure-solely-depend-on-the-topology) — 原问正文；必要时注明追加/update/评论。原问是不额外指定定向的光滑闭流形 M,N 同胚时，M 有 almost complex structure 是否推出 N 也有。须与指定定向相容和仅同伦等价版本分开。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。
- [Mills: Almost complex structures on homotopy complex projective spaces](https://www.sciencedirect.com/science/article/pii/S0166864123004030) — Topology and its Applications 344 (2024),108810；Introduction；arXiv:2201.07176。引言区分 Kahn 定向同伦例、Sutherland 稳定近复结构及本文 homotopy CP^n；提供后续核对线索而非本轮原问反例。 访问：出版商搜索索引引言；直开403；arXiv全文本轮不可达；验证：仅本次文献与范围核对；未独立重证。

**实际搜索路径**：原题完整URL打开；学术查询 `almost complex structure homeomorphic manifolds smooth structure topological invariant`、`Kahn Obstructions extending almost X structures Corollary 6 orientation homeomorphism`；GitHub/代码查询 `site:github.com almost complex homeomorphic manifolds (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `almost complex homeomorphic manifolds (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**待复核**：Mills 2024 引言提到 Sutherland 的 stable almost complex 非PL同胚不变量；还须核稳定/非稳定及实际同胚例，不能在此直接升级为原问反例。

## QX-P-002094 · c2fd85fa8af76d71

**旧卡**：C*-代数张量积的多于两个 C*-范数（原记录 open）。

**本次变化**：原卡把“任意非核对是否总有第三个”削弱成“是否存在第三种范数”。Ozawa–Pisier 已刊结果覆盖 von Neumann 代数对并给连续统多范数，但不是所有 C* 代数对。

**量词和范围**：对每一对非 nuclear pair 的 C* 代数 A,B，若 A⊙B 的 min≠max，是否必有第三个 C* 范数。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/442420/existence-of-more-than-two-c-norms-on-algebraic-tensor-product-of-c-algebras) — 原问正文；必要时注明追加/update/评论。对每一对非 nuclear pair 的 C* 代数 A,B，若 A⊙B 的 min≠max，是否必有第三个 C* 范数。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。
- [Ozawa–Pisier: A continuum of C*-norms on B(H)⊗B(H) and related tensor products](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/94FB717FC867BF212E8CA1E92868F5DD/S0017089515000257a.pdf/continuum_of_cnorms_on_mathbb_b_h_mathbb_b_h_and_related_tensor_products.pdf) — Glasgow Math.J.58 (2016),433–443；摘要、Theorem9；DOI10.1017/S0017089515000257。von Neumann M,N 的不唯一情形至少连续统多个；对象假设不能删去。 访问：全文已读关键段落；验证：仅本次文献与范围核对；未独立重证。

**实际搜索路径**：原题完整URL打开；学术查询 `exactly two C star norms algebraic tensor product nuclear pair`、`Ozawa Buss third C* norm minimal maximal tensor product Wiersma`；GitHub/代码查询 `site:github.com C star norms tensor product third (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `C star norms tensor product third (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**待复核**：不能以特例存在性结束全称问题；张量积 forcing 绝对性论文也非此问。

## QX-P-002095 · 01c712cbf8ae4835

**旧卡**：S³ 3-齐次多项式向量场（题面修正）（原记录 open）。

**本次变化**：人话版改写成闭轨道计数，完全偏离原问。原帖 update 已说明其 Hopf 型构造不由 Wood 构造得到，旧卡若仍把 Wood 穷尽性当未知须修正。

**量词和范围**：分类 S³ 上三次齐次多项式切向单位向量场 P：x·P(x)=0 且 |P(x)|²=|x|^6；问分类是否可行。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/405202/unit-polynomial-vector-fields-on-the-sphere) — 原问正文；必要时注明追加/update/评论。分类 S³ 上三次齐次多项式切向单位向量场 P：x·P(x)=0 且 |P(x)|²=|x|^6；问分类是否可行。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。

**实际搜索路径**：原题完整URL打开；学术查询 `unit homogeneous cubic polynomial vector fields sphere classification Wood`、`S3 polynomial P dot x zero norm P squared norm x sixth Hopf Wood vector fields`；GitHub/代码查询 `site:github.com unit polynomial vector field sphere cubic (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `unit polynomial vector field sphere cubic (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**待复核**：复算原帖具体多项式及调和分解；S² 的一般三次场分类与本题不同。

## QX-P-002096 · 6fae664fd8153d77

**旧卡**：Hölder 球的度量熵估计（原记录 partially_solved）。

**本次变化**：已补核下界来源的适用界限：公开课程讲义 Theorem10 给标量 Lp 熵阶，原帖可见评论主要给上界；不能把仅上界引文当成向量值下界的完整出处。

**量词和范围**：α∈(0,1]，L,r>0，n,m正整数，[-1,1]^n→[-r,r]^m 的 Hölder 范数≤L函数类，在一致范数下的外部 ε 覆盖数下界。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/397935/covering-number-estimates-for-h%C3%B6lder-balls) — 原问正文；必要时注明追加/update/评论。α∈(0,1]，L,r>0，n,m正整数，[-1,1]^n→[-r,r]^m 的 Hölder 范数≤L函数类，在一致范数下的外部 ε 覆盖数下界。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。
- [Han / Chen: EE378C Lecture12, Global Fano’s method](https://web.stanford.edu/class/ee378c/scribe_lec12.pdf) — 2021-05-05，Theorem10，PDF第4页；Definition1–2。归引 Kolmogorov–Tikhomirov 的标量 Hölder 类 log N~ε^(−d/s)；文中 Lp 场景为 p<∞，仍需单独桥接原题 sup 范数/向量值。 访问：全文已读关键段落；验证：仅本次文献与范围核对；未独立重证。

**实际搜索路径**：原题完整URL打开；学术查询 `Holder balls covering number lower bounds metric entropy`、`vector valued Holder functions epsilon entropy lower bound n alpha m uniform norm`；GitHub/代码查询 `site:github.com Holder balls covering entropy lower (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `Holder balls covering entropy lower (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**待复核**：找原始 Kolmogorov–Tikhomirov 定理或提供完整嵌入、缩放和外部覆盖数论证，以匹配 m、L、r 的精确版本。

## QX-P-002097 · 8ec24e522c3f57b7

**旧卡**：completely Ramsey + 非 Baire 相容性（术语校准）（原记录 open）。

**本次变化**：原卡把全模型的全称正则性一致性问题换成某单集合两种性质关系，且完全 Ramsey 定义不对。Ellentuck 与通常 Polish 拓扑必须区分。

**量词和范围**：是否一致存在 ZF 模型使所有实数集都 Ramsey、同时存在无通常 Baire 性质的实数集；并问更强的“所有集 completely Ramsey”版本。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/395114/is-zf-all-sets-of-reals-have-the-ramsey-property-there-is-a-set-without-t) — 原问正文；必要时注明追加/update/评论。是否一致存在 ZF 模型使所有实数集都 Ramsey、同时存在无通常 Baire 性质的实数集；并问更强的“所有集 completely Ramsey”版本。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。

**实际搜索路径**：原题完整URL打开；学术查询 `all sets reals Ramsey property non Baire consistent Larson Zapletal`、`completely Ramsey Ellentuck Polish Baire property ZF consistency`；GitHub/代码查询 `site:github.com all sets Ramsey Baire consistency (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `all sets Ramsey Baire consistency (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**待复核**：后续核 Larson–Zapletal 相关模型及所需选择公理/一致性强度。

## QX-P-002098 · 104640e6b21734ea

**旧卡**：kS_n 的隐藏分次结构（原记录 open）。

**本次变化**：原卡将已存在的分次写为未知存在性。应改为具体计算与描述请求，区分群代数分次与按群元素任意指定次数。

**量词和范围**：Brundan–Kleshchev 分次已知；原问要求在正特征 kS_n 中显式计算小 n,p 的齐次元素、次数及更直接描述。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/390888/hidden-grading-on-ks-n) — 原问正文；必要时注明追加/update/评论。Brundan–Kleshchev 分次已知；原问要求在正特征 kS_n 中显式计算小 n,p 的齐次元素、次数及更直接描述。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。
- [Brundan–Kleshchev: Blocks of cyclotomic Hecke algebras and Khovanov-Lauda algebras](https://arxiv.org/abs/0808.2032) — 摘要的显式同构与正特征对称群代数非平凡 Z 分次。提供原题已经知道的分次存在性，不能代替题目索求的显式算例。 访问：原站索引摘要；验证：仅本次文献与范围核对；未独立重证。

**实际搜索路径**：原题完整URL打开；学术查询 `Brundan Kleshchev grading symmetric group algebra explicit examples`、`compute homogeneous elements kS_n KLR grading alternative description`；GitHub/代码查询 `site:github.com symmetric group algebra KLR grading (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `symmetric group algebra KLR grading (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**待复核**：KLR calculator 可作计算线索，但要验证与群代数基和 BK 同构的转换；本轮未运行工具代码。

## QX-P-002099 · a039bd5fa5dbe1c8

**旧卡**：分圆域类群的循环性（原记录 open）。

**本次变化**：原帖早有 Q(ζ29) 类群 C2³ 的评论反例，因此“只需是或否”误述原问。2026实分圆域类群新论文属邻近进展，不构成一般循环性分类。

**量词和范围**：要求确定 n 的条件使 Cl(Q(ζ_n)) 循环，是分类/判据请求；不是仅问是否所有分圆域类群都循环。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/379702/is-class-group-of-cyclotomic-fields-cyclic) — 原问正文；必要时注明追加/update/评论。要求确定 n 的条件使 Cl(Q(ζ_n)) 循环，是分类/判据请求；不是仅问是否所有分圆域类群都循环。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。
- [Byeon: Ideal class groups of real cyclotomic fields](https://link.springer.com/article/10.1007/s11139-026-01324-6) — 2026-01-30，Ramanujan J.69,45；摘要。任意有限阿贝尔群嵌入正密度子族的实分圆域类群；不是完整分圆域循环性判据。 访问：出版商页面全文入口与摘要已读；验证：仅本次文献与范围核对；未独立重证。

**实际搜索路径**：原题完整URL打开；学术查询 `cyclotomic fields cyclic ideal class group classification`、`cyclotomic 29 class group C2 C2 C2 Washington 10.1`；GitHub/代码查询 `site:github.com cyclotomic class group cyclic (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `cyclotomic class group cyclic (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**待复核**：核 Washington §10.1 或可复算的无条件类群数据；最大实子域类群结果与完整分圆域区分。

## QX-P-002101 · d15020f1189c4193

**旧卡**：2-平面图色数能否达 8 或 9（Karpov 2023 χ≤9 已发表）（原记录 partially_solved）。

**本次变化**：复核 Karpov Theorem1 确为 χ≤9；这只排除色数10，不给8或9的构造。新命中“biplanar + α≤2”的9色形式化属于不同图类。

**量词和范围**：有限 2-planar 图每边至多两次交叉；原问色数8、9或10是否可实现。已刊上界χ≤9排除10，8与9须分别询问。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/346655/does-there-exist-2-planar-graph-with-chromatic-number-8-or-9-or-10) — 原问正文；必要时注明追加/update/评论。有限 2-planar 图每边至多两次交叉；原问色数8、9或10是否可实现。已刊上界χ≤9排除10，8与9须分别询问。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。
- [Karpov: An upper bound on the chromatic number of 2-planar graphs](https://doi.org/10.7151/dmgt.2397) — Discussiones Math.Graph Theory43(3) (2023),703–720；Theorem1，p704。χ(G)≤9；正文说明尚不确定紧性。 访问：出版记录与原稿公开全文镜像已核；验证：仅本次文献与范围核对；未独立重证。
- [同一论文公开全文](https://www.researchgate.net/publication/349858415_An_upper_bound_on_the_chromatic_number_of_2-planar_graphs) — Theorem1 / Section4。供复核完整证明；非新的8/9色构造。 访问：全文已读关键段落；验证：仅本次文献与范围核对；未独立重证。

**实际搜索路径**：原题完整URL打开；学术查询 `2-planar graphs 9 colorable Karpov chromatic number`、`2 planar graph 8 9 chromatic number bound 2026`；GitHub/代码查询 `site:github.com 2 planar graph chromatic number (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `2 planar graph chromatic number (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**待复核**：如有候选图需同时验证交叉数绘图与色数；biplanar/thickness2 不等于每边最多两交叉。

## QX-P-002104 · 426fd0180332b947

**旧卡**：幂集函子迭代 Hom 集合有限性（题面修正）（原记录 open）。

**本次变化**：人话版同时错了变性、作用对象与 Hom 所在范畴。原文 Nat(P²,P²) 有2^16=65536个，旧备注写成216。

**量词和范围**：P 为以逆像作用的反变幂集函子；i,j≥0 且同奇偶。询问全体集合范畴上的 Nat(P^i,P^j) 的集合性与有限性，并问有限集限制的有限性/精确基数，以及从全范畴到有限集限制的单射性。

**直接证据与定位**：

- [原始题目及可见正文/评论](https://mathoverflow.net/questions/309222/is-mathrmhompi-pj-a-finite-set-p-power-set-functor-i-equiv-j-bmo) — 原问正文；必要时注明追加/update/评论。P 为以逆像作用的反变幂集函子；i,j≥0 且同奇偶。询问全体集合范畴上的 Nat(P^i,P^j) 的集合性与有限性，并问有限集限制的有限性/精确基数，以及从全范畴到有限集限制的单射性。 访问：原始页面正文已打开；未展开的隐藏评论不算已读；验证：题面和量词核对；评论不是独立证明。

**实际搜索路径**：原题完整URL打开；学术查询 `natural transformations iterated contravariant powerset finite`、`Hom P3 P3 powerset functor cardinality Gaillard`；GitHub/代码查询 `site:github.com contravariant iterated powerset natural transformations (Lean OR mathlib OR formal-conjectures)`；AI/社区查询 `contravariant iterated powerset natural transformations (site:aixiv.org OR site:aixiv.online OR site:zenodo.org OR EulerSolve OR ProofForum)`；本地索引查询见逐题JSONL。

**已知的基本边界**：有限集骨架是可数小范畴，每个自然变换分量有有限多个选择，故该限制范畴上的 Nat 确为集合，且基数至多 2^{ℵ0}（本次直接观察）。这并不给出有限性或精确基数，也不证明全范畴限制映射单射。

**待复核**：后续核有限性/精确基数及限制映射单射性；不能用固定集合函数数目直接回答。


---

# QX-NEW-07 子集 b：突破点、检索路径与复核清单

核查日期：2026-11-26。仅提出修订建议；未改线上、未发帖、未执行外部仓库代码。以下只收影响题面、状态、出处或查重的发现；严格区分已刊定理、社区证明、公开声明和本次推论。

| 题号 | card_rev | 类型 | 旧卡 → 本次变化 |
|---|---|---|---|
| QX-P-002105 | 32b4cb7207230fd0 | 题面有误 | open → 原问只要求找到一个正则对子，且正则度可依赖两边密度；人话版的整图分割/迭代轮数叙述偏离。Conlon 亲自指向 Conlon–Fox 的塔型部分结果，但没有宣称解决原问所期待的更好界。 |
| QX-P-002106 | 3328bb7ea40d03c7 | 题面有误 | open → 原题固定 n（不是10的幂），问无穷多个 k 使 S(n^k)>S(n^(k+1))；中文人话版交换了固定量和变化量。原帖明确 n=2 已有解；固定 k 变化 n 的论文是不同问题。 |
| QX-P-002107 | 049189d9db03a09e | 仅补出处 | open → 保留两层问题：无穷多个正整数 N 的立方不能表为三个严格正立方，以及加强到素数 N。2026 Maynard 综述研究全部整数的三正立方表示密度，未覆盖本题稀疏的立方数子集。 |
| QX-P-002108 | 05f0988c64c4c729 | 题面有误 | open → 原题是每个正偶数是否为两个欧拉函数值之和。中文人话版的‘每个充分大整数’与‘少数几个值’扩大并改变了命题。2017链接论文只是哥德巴赫的φ方程重述，未给两项表示的普遍证明。 |
| QX-P-002111 | ebf22a33a8e8d334 | 部分进展 | open → Kenyon 定理给 gcd(p,q)=1 的 p×q 矩形下界 max(q/p,log₂q)，整数正方形上界 q/p+C log₂p。代入 p=n,q=n+1，a(n)=Θ(log n)，所以 round(n^(1/3))+6 与a(n)必分离。原帖另问最小需要15–18块的n；这部分本次未核解。 |
| QX-P-002112 | cecc16cc714ecf0f | 部分进展 | open → 独立整数集合AB+C与同集合整数AA+A不同。2019论文的有理集合A满足\|AA+A\|=o(\|A\|²)；取公共分母D并令三集合为DA、DA、D²A，可转成原题的整数子二次构造。2026实数sum-product反例不能直接替代本题。最小值/尖锐阶仍未核定。 |
| QX-P-002113 | 5cd1d506cf265ba2 | 仅补出处 | solved → 已定位并实读 Petrunin 2019-10-04 的MO答案。最近点投影控制弧长测度及周长变化，从而给凸平面闭曲线弧长重心关于Hausdorff距离的统一Lipschitz界；保留原solved，但证据等级是社区数学证明。本次未确认最佳常数。 |
| QX-P-002114 | d2454bc372957ff7 | 题面有误 | claimed → 2026已正式发表FPSR论文；最新版Cor3.2以1.4²<2控制自守迹，可推出Q上椭圆曲线同源及共同好素数点数相等。但‘任意整Weierstrass模型在所有坏素数的朴素点数也相等’不成立：本次枚举给Q同构模型在p=5分别9点和6点。必须写清极小模型/局部L因子约定。 |
| QX-P-002115 | a3b0771e26a17812 | 原题已解 | claimed → 原问限定完备黎曼流形与有限叶黎曼覆叠，求正谱隙的存在性。2025论文§2.1式(2.2)保持谱底和本质谱底；在通常连通设定下即可推出正谱隙保持。圆覆盖例子只否定谱隙数值不变，不否定其为正。 |
| QX-P-002116 | f9fe2bade6fa8efe | 题面有误 | open → 附加问是能否把任意给定结构扩张成有序群/有序域，不是‘结构本来已有群/域时如何’。按原帖允许非稠密线序的定义，附加问已有简单否定障碍；一般可定义选择扩张仍未核到完整结果。2025 Dinis–Edmundo刻画已有Skolem函数的结构，并非自动解决扩张存在性。 |
| QX-P-002117 | ff5925b6516331b8 | 题面有误 | open → 原帖主问是ZFC是否对ZF的全部射影句保守。题目开头已陈述Σ¹3层保守，2019编辑又给Π¹3层的模型论证，并把疑难点推到第四层；现卡标题‘Σ¹3及以上悬置’与原帖相冲突。 |
| QX-P-002118 | 6f249ccd83a06de8 | 题面有误 | open → 原问不是哪些复杂度类整体绝对，而是给定n能否构造真正Δ_n^ZF、不能降低复杂度、却在ZF的∈-模型间绝对的单个公式。卡面还把向下绝对性的方向写反。MO评论表明模型背景和‘ZF可证明绝对’必须明确。 |
| QX-P-002119 | a10ef89f090f68bc | 题面有误 | partially_solved → MSE真正要求强于全部有限次Cesàro方法的线性泛函，并另问其稳定闭包；MO转述经历编辑，Gerald Edgar旧答案仅指出Lim=lim∘f的条件空泛。Abel正规化提供标量情形的重要已知方法，不能未经假设推广到任意度量模或所有几何发散列。 |
| QX-P-002120 | bb1d82639b21f973 | 题面有误 | partially_solved → 有界部分商与坏逼近等价是经典已知刻画。原MSE还要求不周期，卡面省掉了这一限制；在通常最终周期约定下应排除二次无理数。高次代数数能否有界部分商是相关更窄问题，不能替换原作者开放式‘好刻画’的含义。 |
| QX-P-002121 | 3b085171e3652871 | 仅补出处 | open → 原作者已知Baire空间乘积可非Baire，真正寻找的是不依赖平稳集等集合论工具的初等例子。Fleissner–Kunen和van Mill–Pol给已知存在性背景，不能把一般存在性继续挂牌开放，也不能据论文题名断言满足‘初等’要求。 |
| QX-P-002124 | 76d7d07a5a58279b | 题面有误 | open → 原公式对所有不超过素数p的素数q求和，目标是u>1时是否为平方；不是‘前p个素数’。u=1的既有例子只是背景，不能混入目标子问，也不能把任意连续素数区间的幂和论文当初始段结果。 |
| QX-P-002125 | a47d9260405d919c | 公开声明待核 | open → 原页2017更新和pietfermat评论已称x17为合数（PFGW测试）；卡面若仍把它作为未判首例应补这一历史声明。主问整个轨道是否有素数未见可核完整结论。本次未执行PFGW或重跑该140000位数测试。 |
| QX-P-002127 | 37d62199fb794d2b | 题面有误 | partially_solved → 原问关注l≥3；l=2无穷反例族是作者已给的背景。l=3的Voloch回答使用Bateman–Horn，不能改写为无条件解，也未覆盖每个l≥3。候选必须同时检查α+d和α−d；1291已被纠正，21362仅为原帖例子报告，未独立认证最小性。 |
| QX-P-002128 | b18e378e3591ff18 | 原题已解 | partially_solved → 原问题统计平方自由核的素因子来自指定剩余类的数ab²，不是把‘两平方和’再按n的剩余类筛选。令δ=t/φ(m)，Wirsing定理给T(x)∼C x/(log x)^(1−δ)，C>0；b=1的平方自由版本同指数，常数缩为C/ζ(2)。固定1/2指数仅在δ=1/2成立。 |
| QX-P-002129 | d2cecdcc48811f26 | 题面有误 | open → 源题问对有效join与相对可构造性封闭的实数集X是否必满足R∩L(X)=X，并另问术语。有效join是把两个实数编码在一起，不能换成普通集合并。原帖关于射影真理论和大基数下的例子是作者试探，不是已证反例；卡面不应把它写成已确认的反例定理。 |
| QX-P-002130 | 8cc5f5fea0fbd7b2 | 部分进展 | open → 原题要一个奇系数ax+1映射的正整数轨道被证明趋于+∞，长计算、不返1或排除有限周期均不够。2026作者仓库明确写严格目标未解决，且撤回曾声称的10^37周期屏障；当前内容只应列公开部分进展声明。 |
| QX-P-002131 | 22af64da72709549 | 仅补出处 | partially_solved → 原模型确实是停止版Shepp urn，f(r,b)=V(b,r)。复核到明确递推和经典停止边界文献；但‘边界的渐近’、可选择拒绝每次抽球的acceptance版、随机未知球数版都不是固定Δ的价值函数渐近。本次没有足够全文证据把f(n+Δ,n)精确首项判为新开放或已解。 |
| QX-P-002132 | 77212b60ad999019 | 题面有误 | solved → 原MSE问一族‘reasonable’的有理系数多项式，其分裂域对每个n有D₂n群；现卡把它改成单纯逆伽罗瓦存在性并标solved。MO回复确实指Ledet1999，但本次未取得该论文正文验证一族构造与原要求逐项对应，不能只靠引用将更强原问关闭，也不能因此断言它开放。 |
| QX-P-002133 | 7c2b6e4d27b79c28 | 同题或变体 | open → MSE和MO209894确为同一作者的同题交叉帖。主问是每个可数生成的Borel扩张σ代数可延拓Lebesgue测度，是否推出Sierpiński实数集；Carlson模型中两者同时成立不证明一般蕴含。两张指派Sierpiński数论卡仅共享人名，完全不是同题。 |
| QX-P-002134 | a1a3f435c97d98c4 | 公开声明待核 | partially_solved → 原均匀体积问题在d≥3本次仅记录完整反例声明待核及本次推论待核：2026-11-18的AI辅助预印本hexagon:2611.00588v1，Theorem1.3声称实解析正曲率凸体反例，已读定理与§6，未审完依赖。2025已刊Theorem2的一般质量测度反例另列相关推广；从它到连通光滑细管体的紧性桥接是本次独立证明草案，仍待复核。 |

## QX-P-002105 · 32b4cb7207230fd0 · 题面有误

原问只要求找到一个正则对子，且正则度可依赖两边密度；人话版的整图分割/迭代轮数叙述偏离。Conlon 亲自指向 Conlon–Fox 的塔型部分结果，但没有宣称解决原问所期待的更好界。

**链接与定位**

- [Gowers: Is there a weak strong regularity lemma?](https://mathoverflow.net/questions/291467/is-there-a-weak-strong-regularity-lemma?noredirect=1)：题面第3段；David Conlon 2018-01-26 评论；mathworker21 2020-03-09 评论。访问/证据：source_page_read；原作者问题与研究作者社区说明。核验：实读原题和可见评论；没有将社区部分结果升格为完整解决
- [Conlon–Fox, Bounds for graph regularity and removal lemmas](https://arxiv.org/abs/1107.4829)：检索题录；原帖评论所指论文。访问/证据：web_index_only；论文题录。核验：本次索引命中，未逐段读取其单对子参数结论

**量词范围**

- 单个对子、密度依赖的正则度及最佳界：部分进展。任意给定图与密度控制函数；不能替换为完整 AFKS 分割。已核原问及 Conlon 2018-01-26 评论；未核全文定理到精确量词的全部对应
- 题面忠实度：题面有误。中文人话版。与原文逐项比对

**实际路径**：源页读取；学术两组检索 `Is there a weak strong regularity lemma Gowers Conlon Fox` / `regular pair densities strong weak regularity single pair tower bound`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 追查 Conlon–Fox 单对子推论及精确塔高；本次未完成最优界判定

## QX-P-002106 · 3328bb7ea40d03c7 · 题面有误

原题固定 n（不是10的幂），问无穷多个 k 使 S(n^k)>S(n^(k+1))；中文人话版交换了固定量和变化量。原帖明确 n=2 已有解；固定 k 变化 n 的论文是不同问题。

**链接与定位**

- [Must the sum of the digits of n^k decrease infinitely often?](https://mathoverflow.net/questions/211283/must-the-sum-of-the-digits-of-nk-decrease-infinitely-often-for-n-k-in-mathb)：题面第2–3段；Stanley Yao Xiao 2015-07-11 评论。访问/证据：source_page_read；原题及专家评论。核验：核对原文，未找到一般底数新证明
- [Sum of digits of 2^n decreases infinitely often](https://math.stackexchange.com/questions/560624/is-it-true-that-for-infinitely-many-values-of-n-the-sum-of-digits-of-2n-is?noredirect=1)：原帖所链接的 n=2 问答。访问/证据：web_index_only；社区特例。核验：本次仅索引检索，未全文独立复算

**量词范围**

- 每个固定非10幂底数 n 的下降次数：暂未找到可验证结果。n∈Z_{>0}，排除10的非负整数幂；k变动。核题、两组检索和索引排歧；不以未答页面推开放定理
- n=2 特例：部分进展。仅底数2。原作者指明特例已答；本次只核关联索引，未复审特例证明
- 固定变量：题面有误。固定 n 与固定 k 不可交换。原文第2段和 Stanley Yao Xiao 评论直接区分

**实际路径**：源页读取；学术两组检索 `sum digits powers decreasing infinitely often fixed base n` / `"sum of digits" "powers" "decrease" infinitely`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 一般固定底数的直接证明/反例仍待专题复核

## QX-P-002107 · 049189d9db03a09e · 仅补出处

保留两层问题：无穷多个正整数 N 的立方不能表为三个严格正立方，以及加强到素数 N。2026 Maynard 综述研究全部整数的三正立方表示密度，未覆盖本题稀疏的立方数子集。

**链接与定位**

- [Are there infinitely many N^3 not a sum of three positive cubes?](https://mathoverflow.net/questions/208042/are-there-infinitely-many-n3-especially-for-prime-n-that-cannot-be-expressed)：题面；Daniel Loughran 2015-05-31 两条评论。访问/证据：source_page_read；原题/专家评论。核验：核题，无独立穷举
- [James Maynard, Sums of three positive cubes](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.70554)：§1，Theorems 1.1、1.2及其后的条件性正密度讨论。访问/证据：fulltext_sections_read；已刊综述。核验：已核范围，排除将总体密度当本题解答

**量词范围**

- 一般 N 的无穷多不可表示立方：暂未找到可验证结果。a,b,c≥1；N遍历正整数。原题和2026综述关键范围已核；密度结论不推出立方子集结论
- 素数 N 的加强：暂未找到可验证结果。额外 N 为素数。与一般整数计数严格区分

**实际路径**：源页读取；学术两组检索 `infinitely many cubes not sum of three positive cubes` / `"a^3+b^3+c^3" "N^3" "infinitely"`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；1组指定双方正文配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 未发现覆盖本题立方子集的完整结果；不能由总体零/正密度推断

## QX-P-002108 · 05f0988c64c4c729 · 题面有误

原题是每个正偶数是否为两个欧拉函数值之和。中文人话版的‘每个充分大整数’与‘少数几个值’扩大并改变了命题。2017链接论文只是哥德巴赫的φ方程重述，未给两项表示的普遍证明。

**链接与定位**

- [On a relaxed form of Goldbach's conjecture proposed by Erdős](https://mathoverflow.net/questions/269814/on-a-relaxed-form-of-goldbachs-conjecture-proposed-by-erd%C5%91s)：题面及 Guy 书页105 的出处评论。访问/证据：source_page_read；原题与书目线索。核验：原短链接成功取得正文
- [Felix Sidokhine, Goldbach’s conjecture and Euler’s φ-function](https://arxiv.org/pdf/1704.08117.pdf)：arXiv:1704.08117v2，2017-05-04，p1摘要与引言。访问/证据：fulltext_sections_read；预印本。核验：已读首页，未将其当二项 totient 猜想解决

**量词范围**

- 每个正偶数=φ(x)+φ(y)：暂未找到可验证结果。两项、x,y正整数、所有正偶数。实读原帖并核论文首页定位；未以改写当证明
- 中文范围：题面有误。偶数/充分大整数、两项/任意有限项。与原问直接比对

**实际路径**：源页读取；学术两组检索 `Erdos Goldbach sum of two totients conjecture` / `"every positive even integer" "totients"`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 尚未独立核完 Guy 原页及其后完整引文链

## QX-P-002111 · ebf22a33a8e8d334 · 部分进展

Kenyon 定理给 gcd(p,q)=1 的 p×q 矩形下界 max(q/p,log₂q)，整数正方形上界 q/p+C log₂p。代入 p=n,q=n+1，a(n)=Θ(log n)，所以 round(n^(1/3))+6 与a(n)必分离。原帖另问最小需要15–18块的n；这部分本次未核解。

**链接与定位**

- [Oblongs into minimal squares](https://math.stackexchange.com/questions/2057290/oblongs-into-minimal-squares?noredirect=1)：题面 a(n) 定义、重复方块说明、15–18块阈值问及立方根拟合问。访问/证据：source_page_read；原题。核验：实读，确认重复边长允许
- [Richard Kenyon, Tiling a rectangle with the fewest squares](https://arxiv.org/pdf/math/9411215)：Theorem 1，p1；发表于 JCTA76(1996),272–291，DOI10.1006/jcta.1996.0104。访问/证据：fulltext_sections_read；已刊定理的作者预印本。核验：已核定理适用条件并手工代入；未重做整篇证明

**量词范围**

- 渐近增长阶和立方根拟合是否最终分离：原题已证。n×(n+1)，允许正方形重复；整数边长上界，实边长亦有下界。已核 Kenyon Thm1并代入互素相邻边长；不是数值拟合
- 首次需要15、16、17、18块的具体阈值：暂未找到可验证结果。原帖数值子问。未独立运行精确铺砌枚举或核最新证书

**实际路径**：源页读取；学术两组检索 `Kenyon tiling rectangles with squares logarithmic 1996` / `minimal squares n n+1 rectangle asymptotic log`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 15–18块的首次阈值及最新OEIS数据证明状态未核全

## QX-P-002112 · cecc16cc714ecf0f · 部分进展

独立整数集合AB+C与同集合整数AA+A不同。2019论文的有理集合A满足|AA+A|=o(|A|²)；取公共分母D并令三集合为DA、DA、D²A，可转成原题的整数子二次构造。2026实数sum-product反例不能直接替代本题。最小值/尖锐阶仍未核定。

**链接与定位**

- [Minimum |AB+C| for three finite sets of integers](https://math.stackexchange.com/questions/2328450/let-a-b-c-n-be-three-finite-sets-of-integers-find-min-abc-mid-a)：题面A、B、C各n元。访问/证据：source_page_read；原题。核验：核对题面
- [Roche-Newton–Ruzsa–Shen–Shkredov, On the size of AA+A](https://www.ricam.oeaw.ac.at/files/reports/18/rep18-17.pdf)：正文p3 Theorem1.5、式(1.4)；PDF物理页4；p2脚注3。访问/证据：fulltext_sections_read；已刊论文公开稿。核验：对清分母：A'=DA,B'=DA,C'=D²A，A'B'+C'=D²(AA+A)，基数不变；这是本次明确推论
- [Bloom–Sawin–Schildkraut–Zhelezov, The sum-product conjecture is false for real numbers](https://arxiv.org/abs/2605.28781)：v1，2026-05-27，摘要。访问/证据：abstract_only；预印本摘要。核验：已核底域和目标表达式，未审全文证明

**量词范围**

- 独立整数 n 元集合的 min |AB+C|：部分进展。A,B,C可各自不同，含负数也允许；讨论n→∞。Thm1.5有理构造的清分母推论已逐式核对；没有把它当尖锐下界
- 同集合/实数变体：题面有误。不可把AA+A的整数组结果或实数sum-product反例直接套原命题。已核变量重合和底域差异

**实际路径**：源页读取；学术两组检索 `integer sets AB+C minimum size sum product` / `"AB+C" "n" "integers" lower bound`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 尖锐最小值/普适最优下界未核定
- 有理构造给任意大规模；本次未把其改写成每个指定n的最佳界

## QX-P-002113 · 5cd1d506cf265ba2 · 仅补出处

已定位并实读 Petrunin 2019-10-04 的MO答案。最近点投影控制弧长测度及周长变化，从而给凸平面闭曲线弧长重心关于Hausdorff距离的统一Lipschitz界；保留原solved，但证据等级是社区数学证明。本次未确认最佳常数。

**链接与定位**

- [Is the barycenter of a convex curve Lipschitz with respect to Hausdorff distance?](https://math.stackexchange.com/questions/3368345/is-the-barycenter-of-a-convex-curve-in-mathbb-r2-lipschitz-with-respect-to-t)：题面及MO交叉帖链接。访问/证据：source_page_read；原题。核验：已核交叉帖对应
- [Petrunin answer to convex-curve barycenter Lipschitz question](https://mathoverflow.net/questions/343122/is-the-barycenter-of-a-convex-plane-curve-lipschitz-with-respect-to-the-hausdorf)：答案343164，2019-10-04；最近点投影、周长差<2πε、2diam≤length。访问/证据：fulltext_sections_read；专家社区证明。核验：阅读证明链并核题，未复审最优常数或Lean

**量词范围**

- 存在统一Lipschitz常数：原题已证。凸平面闭曲线的归一化弧长重心与Hausdorff距离。已核投影测度证明关键不等式；无形式化重跑
- 最优Lipschitz常数：未作判断。最优数值非原主问所需。不把评论中的猜测常数当定理

**实际路径**：源页读取；学术两组检索 `Lipschitz barycenter convex curves Hausdorff Petrunin` / `"convex curve" "barycenter" "Lipschitz"`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；2组指定双方正文配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 若需显式或最佳常数，应另核非嵌套曲线约化时的常数损失

## QX-P-002114 · d2454bc372957ff7 · 题面有误

2026已正式发表FPSR论文；最新版Cor3.2以1.4²<2控制自守迹，可推出Q上椭圆曲线同源及共同好素数点数相等。但‘任意整Weierstrass模型在所有坏素数的朴素点数也相等’不成立：本次枚举给Q同构模型在p=5分别9点和6点。必须写清极小模型/局部L因子约定。

**链接与定位**

- [If numbers of points of two elliptic curves are close enough, then equal?](https://math.stackexchange.com/questions/2986919/if-the-number-of-points-of-two-elliptic-curves-are-close-enough-then-they-are-e)：引用FPSR旧稿p23的题面。访问/证据：source_page_read；原题引用。核验：已核来源指向FPSR而非仅Serre泛称
- [Farmer–Pitale–Ryan–Schmidt, Multiplicity one for analytic L-functions and applications](https://arxiv.org/html/1305.3972v2)：v2，2025-05-10；Corollary3.2；紧随其后的1.4²<2说明；§4。访问/证据：fulltext_sections_read；已刊论文作者修订稿。核验：定理假设和好素数范围已核，未重证
- [FPSR 正式出版页](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/multiplicity-one-for-analytic-lfunctions-and-applications/928354E8A31DF9903A8496AE65EDB24F)：在线2026-03-27；MPCPS181(1),885–911；DOI10.1017/S0305004126102011。访问/证据：publisher_metadata；出版社题录。核验：已打开官方页核日期/DOI；正文采用arXiv v2
- [本次对原题任意整模型读法的独立算例](https://math.stackexchange.com/questions/2986919/if-the-number-of-points-of-two-elliptic-curves-are-close-enough-then-they-are-e)：本地 local_arithmetic_check.json；y²=x³+x+1 与 y²=x³+625x+15625。访问/证据：local_independent_calculation；自编小整数枚举+明确代数论证。核验：已实际枚举；缩放(x,y)→(25x,125y)在p≠5可逆；没有执行外部代码

**量词范围**

- 接近的好素数点数推出同源：原题已证。Q上椭圆曲线；所有充分大好素数或适用Cor3.2平均条件；1.4<√2。已核Cor3.2与§4对应；同源不等于Q同构；未独立重做强重数一定理
- 任意整模型在全部素数的朴素点数相等：题面有误。不假设极小模型时的坏素数。本次独立F5枚举与Q有理坐标缩放；反驳此字面解释，不反驳正确局部因子版本

**实际路径**：源页读取；学术两组检索 `Multiplicity one L-functions Farmer Pitale Ryan Schmidt elliptic curves` / `"1.4" "elliptic" "points"`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 需按采用的局部点数定义核对FPSR旧稿p23与正式文本，不应混用任意非极小整方程

## QX-P-002115 · a3b0771e26a17812 · 原题已解

原问限定完备黎曼流形与有限叶黎曼覆叠，求正谱隙的存在性。2025论文§2.1式(2.2)保持谱底和本质谱底；在通常连通设定下即可推出正谱隙保持。圆覆盖例子只否定谱隙数值不变，不否定其为正。

**链接与定位**

- [Lifting spectral gap to covering space](https://math.stackexchange.com/questions/2841830/lifting-spectral-gap-to-covering-space?r=31)：题面：complete、finite sheeted；第2部分圆覆盖算例。访问/证据：source_page_read；原题与显式算例。核验：已读完整关键题面
- [Ballmann–Mondal–Polymerakis, On the spectral stability of finite coverings](https://arxiv.org/html/2507.17466v1)：§2.1式(2.2)、Theorem2.5；§2开头完备连通假设。访问/证据：fulltext_sections_read；2025作者预印本中引用的标准结论。核验：式(2.2)与原题定义对应已核；主定理额外曲率假设不用于这个基础等式
- [Does a spectral gap lift to covering spaces?](https://mathoverflow.net/questions/306102/does-a-spectral-gap-lift-to-covering-spaces)：R W 2018-07-17回答及 Jan Bohr 圆覆盖反驳评论。访问/证据：source_page_read；社区讨论。核验：未把回答数量或相等声称当证明

**量词范围（原问）**

- 有限叶覆叠是否保留λ>0：原题已证。完备连通黎曼流形、函数Laplace–Beltrami算子、有限叶黎曼覆叠；不要求曲率有界。依式(2.2)作本次推论：λ0>0直接保持；否则0是有限重孤立特征值且λess>0，覆盖后仍如此。无独立形式化重跑

**相关变体（不计原问解决）**

- 谱隙的数值是否相同：相关加强命题已反驳。这是社区错误回答所声称的更强命题。圆周长扩大d倍使非零谱底缩为d^−2；源题已给算式。范围说明：原问只问正谱隙是否存在；数值完全不变是社区回答提出的更强命题。

**实际路径**：源页读取；学术两组检索 `spectral gap finite sheeted Riemannian covering positivity` / `"finite coverings" "essential spectrum" Laplacian`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 若题库允许无限不连通流形，须另审统一谱隙量词；本次提升限定于连通标准设定

## QX-P-002116 · f9fe2bade6fa8efe · 题面有误

附加问是能否把任意给定结构扩张成有序群/有序域，不是‘结构本来已有群/域时如何’。按原帖允许非稠密线序的定义，附加问已有简单否定障碍；一般可定义选择扩张仍未核到完整结果。2025 Dinis–Edmundo刻画已有Skolem函数的结构，并非自动解决扩张存在性。

**链接与定位**

- [Can any o-minimal structure be expanded to one with definable choice?](https://math.stackexchange.com/questions/2920373/can-any-o-minimal-structure-be-expanded-to-an-o-minimal-structure-with-definable)：主问、Extra questions；Alex Kruckman 2018-09-17/19 评论。访问/证据：source_page_read；原题/专家评论。核验：已核密序约定差异；未把作者猜测当定理
- [Dinis–Edmundo, On definable Skolem functions and trichotomy](https://arxiv.org/abs/2207.11339)：v1摘要；正式发表APAL176(10),103632，DOI10.1016/j.apal.2025.103632之检索题录。访问/证据：abstract_only；已刊论文题录/作者摘要。核验：核摘要目标；未完成全文到任意扩张问题的推导

**量词范围**

- 任意o-minimal结构的选择扩张：暂未找到可验证结果。原帖给定结构和同一底集/顺序上的扩张。未把已有选择结构的分类当任意结构扩张定理
- 任意结构扩成有序群或有序域：部分进展。原帖定义允许非稠密有序集时普遍命题否定；稠密情形另问。Kruckman2018-09-17评论：o-minimal有序群必须稠密；与非稠密底序不相容
- 中文附加问：题面有误。扩成群/域 与 已有群/域的选择性质。逐项核原文

**实际路径**：源页读取；学术两组检索 `o-minimal structure expansion definable Skolem choice functions` / `"o-minimal" "expansion" "definable choice" Dinis Edmundo`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；1组指定双方正文配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 需读2025发表版本定理全文及其对扩张问题的推论
- 稠密情形扩成有序群/域是否有完整否定或构造，本次未核定

## QX-P-002117 · ff5925b6516331b8 · 题面有误

原帖主问是ZFC是否对ZF的全部射影句保守。题目开头已陈述Σ¹3层保守，2019编辑又给Π¹3层的模型论证，并把疑难点推到第四层；现卡标题‘Σ¹3及以上悬置’与原帖相冲突。

**链接与定位**

- [Projective conservativity of choice?](https://math.stackexchange.com/questions/3491349/projective-conservativity-of-choice)：开头Shoenfield推论；2019-12-30 EDIT；末句第四层说明。访问/证据：source_page_read；原作者数学说明。核验：已读题面与编辑；EDIT中N到N字面笔误应按论证需为N到M审校

**量词范围**

- ZFC相对ZF的全部射影句保守性：暂未找到可验证结果。全部有限射影层级，不预设DC。完成索引查新；没有把旧未答状态当现时开放证明
- Σ¹3与Π¹3边界：部分进展。Σ¹3在原帖作为已知；Π¹3为2019-12-30编辑给出的正向论证。已核编辑文本和量词；本次未独立审计无DC强迫及模型构造
- 当前标题：题面有误。不能把Σ¹3继续标为悬置。源页开头和EDIT直接矛盾

**实际路径**：源页读取；学术两组检索 `projective conservativity axiom choice ZF ZFC Schweber` / `"ZF" "ZFC" "projective sentences"`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 主问高层的最新模型结果未核到完整来源
- Π¹3编辑证明仍需集合论专家复审，尤其无DC情形

## QX-P-002118 · 6f249ccd83a06de8 · 题面有误

原问不是哪些复杂度类整体绝对，而是给定n能否构造真正Δ_n^ZF、不能降低复杂度、却在ZF的∈-模型间绝对的单个公式。卡面还把向下绝对性的方向写反。MO评论表明模型背景和‘ZF可证明绝对’必须明确。

**链接与定位**

- [Absolute formulas with high complexity (MSE)](https://math.stackexchange.com/questions/3305444/absolute-formulas-with-high-complexity)：题面最后一问及Π2的H(κ)–V向下说明。访问/证据：source_page_read；原题。核验：已核题面
- [Absolute formulas with high complexity (MO)](https://mathoverflow.net/questions/337943/absolute-formulas-with-high-complexity)：James E Hanson与Gabe Goldberg，2019-08-08评论。访问/证据：source_page_read；专家社区论证。核验：已核条件与结论，未将扩展理论等价当ZF本身等价

**量词范围**

- 逐n构造高复杂度绝对公式：暂未找到可验证结果。真正Δ_n^ZF且不等价更低复杂度；ZF的∈-模型。原题量词已恢复；未把条件性负面评论当一般否定
- 足够传递模型背景下的降阶：部分进展。额外每个集合属于某个传递ZF模型；且ZF证明向上绝对。Goldberg评论给Σ1等价式；仅在额外理论下
- 复杂度类与向下方向：题面有误。存在单个公式不等于整个复杂度类绝对；向下是V到H(κ)。直接原文比对

**实际路径**：源页读取；学术两组检索 `absolute formulas high complexity ZF models Codenotti Goldberg` / `"Delta" "absolute" "in-models" formulas complexity`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- ‘∈-模型’的精确定义和绝对性是外部性质还是ZF可证明性质须由原作者语境进一步确定

## QX-P-002119 · a10ef89f090f68bc · 题面有误

MSE真正要求强于全部有限次Cesàro方法的线性泛函，并另问其稳定闭包；MO转述经历编辑，Gerald Edgar旧答案仅指出Lim=lim∘f的条件空泛。Abel正规化提供标量情形的重要已知方法，不能未经假设推广到任意度量模或所有几何发散列。

**链接与定位**

- [Generalized limits (MSE)](https://math.stackexchange.com/questions/3298993/generalized-limits)：ω-Cesàro定义与两个末问；Calvin Khor 2019-10-14 Abel评论。访问/证据：source_page_read；原题/社区方法线索。核验：已核主问，不以建议当全范围证明
- [Generalized limits (MO), Gerald Edgar answer](https://mathoverflow.net/questions/345164/generalized-limits/345215)：2019-11-03回答345215；后续‘explicit’评论与编辑争议。访问/证据：source_page_read；专家社区分析。核验：已核回答只针对旧条件2，非完整加强问题
- [NIST DLMF §1.15 Summability Methods](https://dlmf.nist.gov/1.15)：Cesàro/Abel可和性。访问/证据：web_index_only；官方数学参考索引。核验：本次索引定位，未逐条全文复核所有推广关系

**量词范围**

- 强于ω-Cesàro的显式线性方法：部分进展。实/复标量序列；普通Abel定义域。原帖Calvin Khor指出Abel；NIST给经典可和性背景；未逐段证明任意模版本
- 更强于稳定闭包及任意度量模：暂未找到可验证结果。必须指定标量环、除法、定义域与‘显式’。旧MO答案不是此加强问题的构造
- 类型与范围：题面有误。写成部分映射X^N⇀X；一般模不能随意消去1−a或除n。原题与卡面符号审计

**实际路径**：源页读取；学术两组检索 `generalized limits omega Cesaro Abel summability stable linear` / `"generalized limits" "345164"`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 需完整核Abel对全部有限次Cesàro的方法包含关系及稳定闭包定义
- 任意度量模缺少可除标量结构，不宜保留无条件公式

## QX-P-002120 · bb1d82639b21f973 · 题面有误

有界部分商与坏逼近等价是经典已知刻画。原MSE还要求不周期，卡面省掉了这一限制；在通常最终周期约定下应排除二次无理数。高次代数数能否有界部分商是相关更窄问题，不能替换原作者开放式‘好刻画’的含义。

**链接与定位**

- [Continued fractions with a bounded sequence of terms](https://math.stackexchange.com/questions/3295784/continued-fractions-with-a-bounded-sequence-of-terms)：题面bounded but not periodic；Mark 2019评论。访问/证据：source_page_read；原题及经典等价说明。核验：已核原问限定
- [On badly approximable numbers](https://www.cambridge.org/core/journals/mathematika/article/abs/on-badly-approximable-numbers/85CDAE1BE543B25DB77BAB771A16792F)：索引摘要中的有界连分数等价。访问/证据：web_index_only；期刊题录。核验：未逐页复审原论文

**量词范围（原问）**

- 有界且不最终周期连分数的“好刻画”：未作判断。无理实数，有界且不周期；若按通常最终周期约定，则排除二次无理数。原作者未给“好刻画”的额外验收标准。。恢复源题遗漏限定；经典坏逼近等价另列背景，不由其直接宣布原问已解或开放。若原帖“周期”仅指纯周期，仍需澄清。

**已知背景（不计原问解决）**

- 有界部分商的丢番图刻画：已知背景。无理实数；存在c>0使|x−p/q|≥c/q²。原帖评论与经典论文题录一致；未作形式化重跑。范围说明：有界部分商与坏逼近的经典等价不自动满足原作者对不周期实数的“好刻画”要求。

**相关变体（不计原问解决）**

- 高次代数数子问题：未作判断。不是原问明示的全部目标。不擅自把原题改成另一猜想。范围说明：高次代数数的有界部分商问题是更窄的邻接问题，不是原帖提出的完整对象范围。

**实际路径**：源页读取；学术两组检索 `bounded partial quotients irrational badly approximable characterization` / `nonperiodic bounded continued fraction algebraic degree three`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；1组指定双方正文配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 原作者‘good characterization’的额外要求未形式化；不能据此自动断言全题开放或全题已解

## QX-P-002121 · 3b085171e3652871 · 仅补出处

原作者已知Baire空间乘积可非Baire，真正寻找的是不依赖平稳集等集合论工具的初等例子。Fleissner–Kunen和van Mill–Pol给已知存在性背景，不能把一般存在性继续挂牌开放，也不能据论文题名断言满足‘初等’要求。

**链接与定位**

- [Elementary example of Baire spaces whose product is not Baire](https://math.stackexchange.com/questions/3274718/elementary-example-of-baire-spaces-whose-product-is-not-baire)：题面已有集合论构造的说明；bof关于X=Y的评论。访问/证据：source_page_read；原题。核验：已核题面范围
- [Fleissner–Kunen, Barely Baire spaces](https://www.impan.pl/en/publishing-house/journals-and-series/fundamenta-mathematicae/all/101/3/101973/en/publishing-house/journals-and-series/fundamenta-mathematicae/all/101)：Fundamenta Mathematicae101(1978),229–240；DOI10.4064/fm-101-3-229-240。访问/证据：web_index_only；出版社题录。核验：本次未逐页检验构造是否达到原作者的初等标准

**量词范围（原问）**

- 原作者要求的初等构造：暂未找到可验证结果。排除既有平稳集方法；‘初等’需给具体标准。检索未定位符合限制的新完整构造

**已知背景（不计原问解决）**

- 存在两个Baire空间乘积非Baire：已知背景。一般拓扑空间，不要求完全可度量或局部紧。原题明确作为已知；已刊存在性文献定位。范围说明：原作者已知一般存在性，主问要求避免平稳集等工具的初等构造。

**实际路径**：源页读取；学术两组检索 `elementary Baire spaces product not Baire Fleissner Kunen` / `"Baire" "product" "elementary" Codenotti`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 需为‘初等’制定可验收标准并复审完整构造
- 相关2020 ZF版本仅检索线索，本次未全文核题

## QX-P-002124 · 76d7d07a5a58279b · 题面有误

原公式对所有不超过素数p的素数q求和，目标是u>1时是否为平方；不是‘前p个素数’。u=1的既有例子只是背景，不能混入目标子问，也不能把任意连续素数区间的幂和论文当初始段结果。

**链接与定位**

- [Can the sum of powers of the first primes be a square?](https://math.stackexchange.com/questions/2215828/can-the-sum-of-powers-of-the-first-primes-be-a-square)：题面公式及u>1末问；作者有限范围计算。访问/证据：source_page_read；原题及作者计算报告。核验：未把有限检验当证明
- [Algorithms and Bounds on Sums of Powers of Consecutive Primes](https://math.colgate.edu/~integers/y4/y4.pdf)：2024论文索引；DOI10.5281/zenodo.10450932。访问/证据：web_index_only；已刊论文索引。核验：仅核题名与对象排歧，未审定理全文

**量词范围**

- Σ_{q≤p,q素} q^u 为平方，p>2,u>1：暂未找到可验证结果。从素数2开始的完整初始段；整数u>1。原问量词已核；未独立复算作者大范围枚举
- 索引和指数界：题面有误。p为上界素数而非素数个数；u=1不在目标。核公式与末问

**实际路径**：源页读取；学术两组检索 `sum powers first primes perfect square` / `"sum" "prime powers" "square" "2215828"`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 未核到目标范围的证明、反例证书或新数值记录；不以搜索无命中推开放

## QX-P-002125 · a47d9260405d919c · 公开声明待核

原页2017更新和pietfermat评论已称x17为合数（PFGW测试）；卡面若仍把它作为未判首例应补这一历史声明。主问整个轨道是否有素数未见可核完整结论。本次未执行PFGW或重跑该140000位数测试。

**链接与定位**

- [Does x0=12, x(n+1)=x(n)^2+1 contain a prime?](https://math.stackexchange.com/questions/2412646/does-the-sequence-x-0-12-x-n1-x-n21-contain-a-prime)：UPDATE；pietfermat 2017-09-01 18:47评论；G Tony Jacobs 2017-08-31筛除同余类。访问/证据：source_page_read；社区计算声明。核验：已核原文；未取得可重放合数证书，未执行外部代码

**量词范围**

- x17是否为素数：完整证明/反例声明待核。仅x0=12、x_{k+1}=x_k²+1的第17项。原作者FactorDB更新与pietfermat2017-09-01 PFGW报告；没有证书/底数残数，未独立重跑
- 是否至少有一个素数项：暂未找到可验证结果。全部k≥0。筛除若干同余类不覆盖全体k，未把有限计算当不存在素数证明

**实际路径**：源页读取；学术两组检索 `sequence x0 12 x n squared plus 1 prime 17` / `"12" "2412646" "prime"`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 取得x17非平凡因子或Fermat/Miller–Rabin具体见证后独立验证
- 整个轨道是否含素数的结论本次未核定

## QX-P-002127 · 37d62199fb794d2b · 题面有误

原问关注l≥3；l=2无穷反例族是作者已给的背景。l=3的Voloch回答使用Bateman–Horn，不能改写为无条件解，也未覆盖每个l≥3。候选必须同时检查α+d和α−d；1291已被纠正，21362仅为原帖例子报告，未独立认证最小性。

**链接与定位**

- [An interesting problem which only needs elementary number theory (MSE)](https://math.stackexchange.com/questions/1917847/an-interesting-problem-which-only-needs-elementary-number-theory)：Proposition1与l≥3主问。访问/证据：source_page_read；原作者证明。核验：已核主要分类论证
- [Voloch answer on q−α dividing α^l−α](https://mathoverflow.net/questions/249829/an-interesting-problem-which-i-think-only-needs-elementary-number-theory)：题面REMARK；2016-09-14负因子评论；2016-09-15回答。访问/证据：fulltext_sections_read；专家社区条件性论证。核验：已核原文假设和结论；未独立枚举21362最小性

**量词范围（原问）**

- l=3无穷反例：部分进展。Voloch α=210n+160 的Bateman–Horn条件性构造。已核三条线性素数条件、128正因子与两种符号；未解除猜想
- 每个固定l≥3的无条件无穷反例：暂未找到可验证结果。l任意，需分别证明。l=3条件性论证不覆盖全部l
- 符号/最小例：题面有误。q−α可为负；q为正素数，通常排除零除数q=α。α=182,q=179为漏负因子示例；21362只是原帖计算报告，未独立验证最小性

**已知背景（不计原问解决）**

- l=2无穷多α无合适素数q：已知背景。α=2p+1，p≡11或41(mod60)素数。已读原帖命题及分类证明；无形式化重跑。范围说明：作者先证明 Proposition 1，随后明确提出把平方换成立方及每个 l≥3；l=2 不是待解决主问。

**实际路径**：源页读取；学术两组检索 `Li Yuan Wang prime q alpha divides alpha l alpha Voloch` / `"210n+160" "prime"`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- l=3条件性上界能否用筛法无条件化；本次未核到结果
- q=α时零整除约定需明确，α=1等退化应单列

## QX-P-002128 · b18e378e3591ff18 · 原题已解

原问题统计平方自由核的素因子来自指定剩余类的数ab²，不是把‘两平方和’再按n的剩余类筛选。令δ=t/φ(m)，Wirsing定理给T(x)∼C x/(log x)^(1−δ)，C>0；b=1的平方自由版本同指数，常数缩为C/ζ(2)。固定1/2指数仅在δ=1/2成立。

**链接与定位**

- [Generalizing the growth of sums of two squares](https://math.stackexchange.com/questions/1828849/generalizing-the-growth-of-sums-of-two-squares)：题面ab²与Edit b=1；Erick Wong 2016-06-22评论。访问/证据：source_page_read；原题/专家路线。核验：已核T不是最终整数n的剩余类
- [Berndt–Moree, Sums of two squares and the tau-function: Ramanujan’s trail](https://arxiv.org/html/2409.03428v3)：Theorem4.1及常数乘积；§4.1；正式Expositiones Mathematicae2025,125721。访问/证据：fulltext_sections_read；已刊综述中的Wirsing定理。核验：已核条件。允许T中非互素类只额外影响有限多个p|m，改变常数不改变指数

**量词范围**

- ab²主计数的指数与常数存在：原题已证。固定m、T；T含0<t<φ(m)个与m互素的类；a平方自由且素因子模m落T；b任意正整数。本次将已刊综述Thm4.1应用到明确的乘性指标；PNT-AP给δ，Euler因子核对；这是文献定理的直接推论
- b=1版本：原题已证。平方自由数，仅允许素数集合P。Dirichlet级数F(s)=ζ(2s)∏_{p∈P}(1+p^−s)，故去掉b²因子常数除ζ(2)
- 所有T均有sqrt(log x)分母：原题已反驳。δ≠1/2的固定类集。正确指数1−δ与猜测1/2比较；不需数值反例

**实际路径**：源页读取；学术两组检索 `Landau Ramanujan generalization primes residue classes squarefree kernel` / `"Selberg Delange" "squarefree" "residue classes"`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 如需具体m,T的数值常数和有效误差项，应另行计算；本次未数值评估C

## QX-P-002129 · d2cecdcc48811f26 · 题面有误

源题问对有效join与相对可构造性封闭的实数集X是否必满足R∩L(X)=X，并另问术语。有效join是把两个实数编码在一起，不能换成普通集合并。原帖关于射影真理论和大基数下的例子是作者试探，不是已证反例；卡面不应把它写成已确认的反例定理。

**链接与定位**

- [What can the reals of an inner model be?](https://math.stackexchange.com/questions/1621883/what-can-the-reals-of-an-inner-model-be)：题面理想定义、射影真理论设想、命名附问。访问/证据：source_page_read；原题。核验：已核源文，未执行模型构造

**量词范围**

- 构造性理想能否实现为内模型实数：暂未找到可验证结果。实数编码为ω^ω；对有效join r⊕s:n↦2^{r(n)}3^{s(n)}及相对可构造性封闭；须明确L(X)约定。恢复题面与作者语气；未核到完整证明/反例
- 统一术语是否已有名称：未作判断。术语/文献问题。本次未找到权威统一命名；不以零命中断言无术语
- 作者射影真理论设想：题面有误。有足够大基数时作者‘I think’设想。必须保留假设与未证语气

**实际路径**：源页读取；学术两组检索 `constructibility ideal reals L(X) relative constructibility` / `"constructibility ideal" "projective"`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 需核L(X)与L[X]约定及有效join/相对构造闭包是否足以实现内模型的文献
- 未核到可关闭主问的模型论结果

## QX-P-002130 · 8cc5f5fea0fbd7b2 · 部分进展

原题要一个奇系数ax+1映射的正整数轨道被证明趋于+∞，长计算、不返1或排除有限周期均不够。2026作者仓库明确写严格目标未解决，且撤回曾声称的10^37周期屏障；当前内容只应列公开部分进展声明。

**链接与定位**

- [Collatz-type problems with known divergent trajectories](https://math.stackexchange.com/questions/1489225/collatz-type-problems-with-known-divergent-trajectories)：题面及接受非构造性证明的评论。访问/证据：source_page_read；原题。核验：已核主问
- [divergent-xn-plus-one-collatz repository](https://github.com/Grisha-Pochuev/divergent-xn-plus-one-collatz)：README Strongest current branch、Current exact target、Important retraction；2026-11-26读取。访问/证据：repository_readme_read；作者仓库/部分结果声明。核验：未取得固定提交hash；未克隆、未运行run_checks.py；不作为独立验证通过

**量词范围**

- 存在被证明趋于+∞的普通整数轨道：暂未找到可验证结果。奇a>1、正整数起点；偶数除2，奇数ax+1；可等价考察压缩奇数轨道。未将2-adic轨道或finite-prefix/无返1替代正整数无穷逃逸
- 2026仓库周期屏障与候选：部分进展。仓库具体巨大奇X与n0=1；只为必要周期条件。已读README当前状态与retraction；作者自称结果，未锁定提交、未执行脚本或审全依赖

**实际路径**：源页读取；学术两组检索 `Collatz ax+1 odd multiplier proven divergent trajectory` / `"1093" "divergent" "Collatz"`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 需固定提交并审查当前候选的所有证明依赖；本次未执行外部代码
- 并未穷尽所有奇a，现有检索不能证明一般存在性仍开放

## QX-P-002131 · 22af64da72709549 · 仅补出处

原模型确实是停止版Shepp urn，f(r,b)=V(b,r)。复核到明确递推和经典停止边界文献；但‘边界的渐近’、可选择拒绝每次抽球的acceptance版、随机未知球数版都不是固定Δ的价值函数渐近。本次没有足够全文证据把f(n+Δ,n)精确首项判为新开放或已解。

**链接与定位**

- [Asymptotic value of card drawing game](https://math.stackexchange.com/questions/1463216/asymptotic-value-of-card-drawing-game)：固定Δ主问、递推；Henry 2016-11-18指Boyce1973评论。访问/证据：source_page_read；原题/文献关联。核验：已核同一递推和价值函数的变量置换
- [Richard Voepel, Experimental results and generalizations for the stopping problem of Shepp’s urn](https://sites.math.rutgers.edu/~zeilberg/banim/SheppRichard.pdf)：p1 Problem1.1；p2式(2.1)/(2.2)；p1关于Shepp和Boyce的综述。访问/证据：fulltext_sections_read；作者公开研究稿。核验：已核相关段落；未复算Maple包

**量词范围（原问）**

- f(n,n)及固定Δ的f(n+Δ,n)渐近：未作判断。已知红黑牌数量，无放回，允许初始即停止；Δ固定整数。已对应递推；未取得Shepp/Boyce原论文完整价值渐近定理，不依据论坛无答案判开放

**已知背景（不计原问解决）**

- 模型识别与动态规划：已知背景。V(m,p)递推及停牌策略。源题与Voepel§2逐项对应；未运行数值计算。范围说明：递推与动态规划已写在源帖 Partial analysis；补核停止版 Shepp urn 对应，不解决固定 Δ 的价值函数渐近。

**实际路径**：源页读取；学术两组检索 `Shepp urn scheme asymptotic red black card stopping value` / `"Boyce" "Shepp" "asymptotic"`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 优先取得Shepp1969与Boyce1973完整原文，核固定Δ价值函数首项/误差；本轮未完成
- 随机球数组成及逐球可拒绝变体的线性渐近不可代入

## QX-P-002132 · 77212b60ad999019 · 题面有误

原MSE问一族‘reasonable’的有理系数多项式，其分裂域对每个n有D₂n群；现卡把它改成单纯逆伽罗瓦存在性并标solved。MO回复确实指Ledet1999，但本次未取得该论文正文验证一族构造与原要求逐项对应，不能只靠引用将更强原问关闭，也不能因此断言它开放。

**链接与定位**

- [A sequence of rational polynomials whose splitting fields have dihedral Galois groups](https://math.stackexchange.com/questions/1219158/a-sequence-of-rational-polynomials-whose-splitting-fields-over-mathbfq-have)：题面：x³−2、x⁴−2例及reasonable sequence末问。访问/证据：source_page_read；原题。核验：已核D₂n表示群阶2n及例子
- [Polynomial with Galois Group D₂n](https://mathoverflow.net/questions/58847/polynomial-with-galois-group-d-2n/58903)：2011回答58903指向Ledet1999；另一回答只演示小群不变量法。访问/证据：source_page_read；社区引文声明。核验：已核引用，未取得Ledet全文；没有独立核统一公式
- [Arne Ledet publications](https://www.plenilunary.com/publications.html)：Dihedral extensions in characteristic0；C.R.Math.Rep.Canada21(1999),46–52；MR1697454。访问/证据：web_index_only；作者目录索引。核验：直接打开非www页超时；检索仅确认题录而无全文

**量词范围**

- D₂n在Q上的一般实现：部分进展。每个n的存在/构造文献。MO指Ledet为一般方法；作者出版目录核到题录，未读该7页论文
- 原问统一‘reasonable’多项式序列：完整证明/反例声明待核。全部n、Q系数、群阶2n；‘reasonable’需给验收定义。当前solved证据未完成精确序列构造的对应；不把缺正文当数学否定
- 题面替换：题面有误。统一序列与逐n抽象存在性。核原MSE原句

**实际路径**：源页读取；学术两组检索 `Dihedral extensions characteristic 0 Ledet 1999 polynomials` / `"dihedral" "all n" "polynomial" Galois Q`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 取得Ledet1999全文，提取定理编号、参数选择与全部n覆盖
- 需定义‘reasonable’：可计算算法、统一显式公式或固定参数族

## QX-P-002133 · 7c2b6e4d27b79c28 · 同题或变体

MSE和MO209894确为同一作者的同题交叉帖。主问是每个可数生成的Borel扩张σ代数可延拓Lebesgue测度，是否推出Sierpiński实数集；Carlson模型中两者同时成立不证明一般蕴含。两张指派Sierpiński数论卡仅共享人名，完全不是同题。

**链接与定位**

- [Carlson’s model and Sierpinski sets](https://math.stackexchange.com/questions/644344/carlsons-model-and-sierpinski-sets)：题面。访问/证据：source_page_read；原题。核验：已核与MO同一作者和命题
- [Sierpinski sets and extensions of Lebesgue measure](https://mathoverflow.net/questions/209894/sierpinski-sets-and-extensions-of-lebesgue-measure)：开头明确复制旧MSE问题；主问及Carlson模型/总延拓特例。访问/证据：source_page_read；原作者交叉帖。核验：已核可数生成条件与特例边界
- [Carlson, Extending Lebesgue measure by infinitely many sets](https://msp.org/pjm/1984/115-1/pjm-v115-n1-p03-s.pdf)：Pacific Journal of Mathematics115(1),1984；索引题录。访问/证据：web_index_only；已刊论文题录。核验：本次未逐页复审该论文

**量词范围**

- 可数生成延拓性质⇒Sierpiński集：暂未找到可验证结果。[0,1]的Borel σ代数扩张；每个扩张可各自有不同延拓测度；不可数实数集与任意零测集交可数。已核MSE/MO精确同题；不把特定模型共同成立当蕴含证明
- Carlson模型提供两性质实例：部分进展。CH模型加ω₂个随机实数的模型。源题作为已知说明；本次仅核Carlson论文题录，未独立验证强迫证明

**实际路径**：源页读取；学术两组检索 `Carlson model Sierpinski sets Lebesgue measure extension` / `"countably generated" "Sierpinski" "measure"`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；2组指定双方正文配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 没有核到一般蕴含的完整证明或反模型；不可从论坛无答案认定全球开放

## QX-P-002134 · a1a3f435c97d98c4 · 公开声明待核

原均匀体积问题在d≥3本次仅记录完整反例声明待核及本次推论待核：2026-11-18的AI辅助预印本hexagon:2611.00588v1，Theorem1.3声称实解析正曲率凸体反例，已读定理与§6，未审完依赖。2025已刊Theorem2的一般质量测度反例另列相关推广；从它到连通光滑细管体的紧性桥接是本次独立证明草案，仍待复核。

**链接与定位**

- [Can I split E in equal-volume parts?](https://math.stackexchange.com/questions/4314058/can-i-split-e-in-equal-volume-parts)：连通有界开集、光滑边界/可测放宽；刚体移动坐标正交象限要求。访问/证据：source_page_read；原题。核验：已核对象与正交性
- [Maldonado–Roldán-Pensado, On the orthogonal Grünbaum partition problem in dimension three](https://arxiv.org/html/2404.01504v3)：Theorem2；§2 Lemmas4–5及Theorem2证明；Computational Geometry126(2025),102149；DOI10.1016/j.comgeo.2024.102149。访问/证据：fulltext_sections_read；已刊定理公开稿。核验：已核§2证明；d=3总交点≤6，d≥4用1+d(d−1)<2^d−1
- [Convex-body volume counterexamples to hyperplane equipartition (aiXiv index)](https://aixiv.online/abs/2611.01918)：2026-11-19索引；原发布2026-11-18；AI辅助标签及hexagon源链接。访问/证据：source_page_read；公开AI辅助预印本索引。核验：已直接访问；不是期刊审稿证明
- [Sihan Chen, Convex-body volume counterexamples to hyperplane equipartition](https://hexagonmath.org/pdf/2611.00588)：hexagon:2611.00588v1，2026-11-18；p2 Theorem1.3；§6 pp8–9；§7 Lemma7.1。访问/证据：fulltext_sections_read；AI辅助预印本完整反例声明。核验：已读声明及§6关键论证；依赖Proposition3.4尚未独立全面复核；未形式化重跑

**量词范围（原问）**

- d≥3连通有界光滑开集的均匀体积原题：完整证明/反例声明待核。2026预印本更强声称实解析正曲率凸体；取其内部即原题范围。已核Theorem1.3与§6论证对应；未独立审完Proposition3.4、全部小参数估计或任何形式化代码
- 由已刊测度反例到光滑连通体的本次推论：完整证明/反例声明待核。固定远端紧矩曲线弧；等厚细管，端点平滑；归一化体积弱收敛到弧长测度。独立标签：本次补足的证明草案，关键紧性桥接详见findings.md；不是论文原定理逐字内容，也未声称外部复核通过
- 低维情况：部分进展。d=1中位数；d=2可连续转动两条垂直平分线实现四等分。原题与论文背景支持；本次未重写完整平面证明

**相关变体（不计原问解决）**

- d≥3一般超平面零测度的质量测度：相关推广命题已反驳。是原题的测度推广；允许支持在矩曲线上，非直接均匀体积原型。已读已刊稿Theorem2及§2证明，尤其d=3需额外排除两组三交点，不误用d≥4计数。范围说明：允许矩曲线支撑的一般质量测度严格宽于原题均匀体积；必须补体积逼近和紧性桥接，不能直接宣布原问已反驳。

**实际路径**：源页读取；学术两组检索 `orthogonal Grunbaum partition problem smooth connected body counterexample` / `"orthogonal equipartition" "absolutely continuous"`；GitHub/Lean网页索引；四平台名称合并的AI/社区网页索引；全库2469条标题索引；本题无指定配对。 逐次参数与结果归档见 results.jsonl 的 queries/log_file；合并索引不等于逐站检索。

**待复核**

- 独立审核2026预印本Proposition3.4及Theorem1.3全部依赖；本次不宣布已验证
- 复核细管归一化体积弱收敛、平滑端帽和移动象限的连续性桥接
- 凸性是2026声明的加强，细管推论一般不保凸

## 指派查重：7/7组已读双方现版正文

| 双方题号/版本 | 关系 | 理由 |
|---|---|---|
| QX-P-002107 / 049189d9db03a09e；QX-P-001246 / 9e6c3f68818d8ac9 | 相关但不等价 | 001246问每个整数能否为四个允许正负的整数立方和；002107问有无无穷多立方数不能为三个严格正立方和，并有素数底数加强。项数、正性、目标数集合和量词均不同。 |
| QX-P-002113 / 5cd1d506cf265ba2；QX-P-002142 / 703140363ec50ab0 | 相关但不等价 | 002113是平面凸曲线弧长重心映射的Hausdorff稳定性；002142是S⁴的双Lipschitz流形结构唯一性。共享Lipschitz一词，无同一命题或相互蕴含关系。 |
| QX-P-002113 / 5cd1d506cf265ba2；QX-P-002180 / 87d56552cf1abddc | 相关但不等价 | 002180涉及乘R后的双Lipschitz嵌入维数消去；参考正文历史校准为X×R嵌入R^n能否推出X嵌入R^(n−1)。与凸曲线重心泛函稳定性不同。 |
| QX-P-002116 / f9fe2bade6fa8efe；QX-P-002196 / 57d34d9951127067 | 相关但不等价 | 002116固定o-minimal线序结构问保持o-minimal的选择/群/域扩张；002196在非标准算术模型及反推数学语境问可定义选择。模型类别、语言与扩张要求不同，不能因选择函数同词合并。 |
| QX-P-002120 / bb1d82639b21f973；QX-P-002406 / 0d069934522f347f | 相关但不等价 | 002120问单个实数有界且不周期的连分数刻画；002406问任意两个实数同分母乘法逼近的liminf=0。坏逼近数是Littlewood潜在反例的相关对象，但二实变量全称命题不等价于单实数刻画。 |
| QX-P-002133 / 7c2b6e4d27b79c28；QX-P-001656 / eca1d23d27003a11 | 相关但不等价 | 001656的Sierpiński数是奇整数k使k2^n+1恒合数，问最小性；002133的Sierpiński集是不可数实数集与每个零测集交可数，问测度延拓蕴含。仅共享人名，不是数学变体。 |
| QX-P-002133 / 7c2b6e4d27b79c28；QX-P-002302 / 90bbe3bb88387028 | 相关但不等价 | 002302问恒合数Sierpiński整数是否可无有限素数覆盖；002133问零测集意义的Sierpiński实数集。对象与量词完全不同，仅共享人名。 |

## 2134：本次补充的细管推论（独立标签，待复核）

这段是本次从已刊测度定理补出的桥接论证，不是Maldonado–Roldán-Pensado原文已明确陈述的光滑体定理，也不依赖2026 AI辅助预印本的正确性。

固定d≥3，取论文Lemma5所允许的足够远端矩曲线的一段紧光滑弧Γ={γ(t):M≤t≤M+1}，以归一化弧长作为μ。任何仿射超平面只与矩曲线有有限多个交点，故其μ质量为0。论文Theorem2的证明对任何支持在该远端曲线上的质量测度适用，所以μ没有正交2^d等分。d=3需使用论文中第二个平面至多两交点的补充论证，不能直接用d≥4的不等式。

令Eε是Γ的半径ε细管，端帽作光滑化。可使Eε有界、连通、开、边界C∞，并令端帽/平滑修正体积为o(ε^(d−1))；管体积的主项为ω_(d−1) ε^(d−1) length(Γ)。因此归一化体积测度με弱收敛到μ，且所有Eε位于同一固定球B_R内。这一标准管公式与端帽误差，是需要独立复核的第一个桥接点。

若有ε_j→0使E_(ε_j)存在正交等分，记单位法向量框架U_j∈O(d)，偏移t_j∈R^d。每个切平面都平分正体积，故它必须穿过B_R，从而|t_(j,i)|≤R。紧性给一子列(U_j,t_j)→(U,t)，其中U仍正交。每个极限超平面的μ质量为0，故移动象限的με_j质量收敛到对应极限象限的μ质量：可用固定薄层夹逼与Portmanteau定理证明，先令j→∞再令薄层厚度→0。这是第二个须复核的桥接点。

于是μ的每个极限象限质量都为2^−d，与已刊反例矛盾。因此所有充分小的这样的光滑细管都不允许正交等分。该论证不保持凸性；2026 Theorem1.3声称的凸体结果更强，证据级别须另列。

## 2112：清分母桥接与范围

论文Theorem1.5的原量词为：对任意n，存在有限A⊂Q且|A|≥n，满足其子二次上界。取整数D>0清掉A的分母，设A1=B1=DA、C1=D²A，则三集合都是同样基数的整数集合，而且A1B1+C1=D²(AA+A)。故沿任意大规模构造族，原题有o(|A|²)上界。这里没有证明每个指定基数n的最优函数m(n)=o(n²)；要作该加强须补构造基数的可控性。

## 2114：本次独立枚举的模型边界

取E:y²=x³+x+1和E′:y²=x³+625x+15625。二者经(x,y)↦(25x,125y)在Q上同构，且对每个p≠5该变换在F_p可逆。自编小整数枚举（local_arithmetic_check.json）给p=5时射影点数分别9与6，差3<1.4√5。E′在p=5是非极小整模型，其朴素约化为尖点曲线。因此只反驳“任意整方程的全部模p点数相同”读法，不反驳极小模型的局部L因子或好素数版本。


---

# QX-NEW-07 子集 C：突破点、检索路径与复核清单

字段说明：背景及另一定义已从原问 math_results 隔离。2140 的 up-to-isogeny、2151 的背景非可均性、2158 的 Polish 已知情形、2159 的 d=1 已知情形见 background_results；2147 的形式化工具、2157 的仅有限生成版本、2137 的临界线零点另一定义见 related_variant_results。以下叙述与数学判断保持不变，扩展字段不作为原问解决状态导入。

检索日期：2026-11-26。范围：QX-P-002135–QX-P-002159，共25题；指派对子12对。以下只列影响题面、数学范围、出处或声明等级的发现；“原题已解”可指对原有 solved 的核验，不必然是本轮新解。所有建议仅供离线回传，未改线上、未发帖、未执行外部代码。

公开 AI 路线为实际执行的联合网页索引查询，并非 aiXiv、Zenodo、EulerSolve、ProofForum 各站的站内全量检索。文献正文、摘要、不可达及静态代码分别记录。形式化材料仅2151取得具体入口，未独立重跑。

| 题号 | 当前版本 | 变化类别 | 关键变化 |
|---|---|---|---|
| QX-P-002135 | 32f64ab5cb34f8b2 | 部分进展 | 模型确为 trapped kinetic/growing self-avoiding walk。 |
| QX-P-002136 | 8bb1315ed144f7b7 | 题面有误 | 原题规则可完整恢复：X_{n+1}=(X_n+U_n)/2，U_n 为独立均匀圆周点。 |
| QX-P-002137 | 3ff946964af5edb9 | 原题已解 | 已解状态成立：Riemann–von Mangoldt 的 N(T)~T log T/(2pi) 给 gamma_n~2pi n/log n，再用 Stirling 得 floor(log Gamma(x))~x log x，复合后即 2pi x。 |
| QX-P-002138 | 4e4aed1935f0ea28 | 部分进展 | 保留部分进展。 |
| QX-P-002139 | 80b39c747eee0e48 | 题面有误 | 纠正人话版把“非”字怀疑为误写并称近乎自动的描述。 |
| QX-P-002140 | 6ee3bcbdf459c5d6 | 题面有误 | 题卡的人话版将原问弱化成 up to isogeny，必须修正。 |
| QX-P-002141 | fd14b036e65b5cbf | 题面有误 | 当前 HR E∞ 化叙述使问题变成已知常识，须改为沿 S→HZ 的谱提升。 |
| QX-P-002143 | b4c93142c191f456 | 题面有误 | 题卡混淆两处定义：有限维 Hopf 的积分空间一维不能作为半单等价，S²=id 也不替代 C*-Hopf/Kac 结构存在。 |
| QX-P-002144 | b8119b18201c1692 | 题面有误 | 原问是文献/精确化请求，题卡把它改写成特定递推构造并无出处。 |
| QX-P-002145 | 0652b5bc6b52768d | 题面有误 | 须修正实矩阵/归一化量纲。 |
| QX-P-002146 | fab839b1925f2409 | 题面有误 | 2014 Marché–Maurin 全文 Theorem1.1 给技术假设下除有限条斜率外 character variety reduced zero-dimensional，进而不可约 SL2(C) 表示 H¹=0。 |
| QX-P-002147 | 749390830da8e305 | 题面有误 | 应保留原帖三项方法论问题及2010背景。 |
| QX-P-002148 | 919aa2d1927089e5 | 公开声明待核 | Ohta原稿Example3.3.4 p.25确实提出配对k+k′=p+1同时整除问题，核心范围4≤k≤p−3，原帖加入的k=2是平凡边界。 |
| QX-P-002149 | 5c0b839c16830381 | 题面有误 | 未经等模限制的宽版本有直接反例：a=i、lambda1=1/2、lambda2=1给Theta(n)=arctan(2^(−n))，非零却指数趋零，故不可能有倒数次指数的正下界。 |
| QX-P-002150 | 779fe204efb1672f | 部分进展 | 英文标题2^k替代2k造成严重变义。 |
| QX-P-002151 | bdbbe7ee3e44ce36 | 公开声明待核 | 已定位公开非可均性预印本、人类解释论文和实际Lean solution入口。 |
| QX-P-002152 | 436108804343377d | 题面有误 | 标题“评论级否定共识”扩大了评论量词：Sawin对Q2机制的质疑不是Q1不存在的证明。 |
| QX-P-002153 | c3db20a7d8061003 | 题面有误 | 补回原题的维数、截面曲率范围和直径泛函。 |
| QX-P-002154 | d81b10eba4e703c8 | 题面有误 | 修正人话版“左右单模存在性尚不明显”：通常含幺非零环在选择公理下左右都有单模，原问比较同构类数目。 |
| QX-P-002155 | 9bd78f8936d34991 | 题面有误 | 应恢复为文献/已知范围询问，不能把无人答帖解释成“最优范围为文献空白”。 |
| QX-P-002156 | f509310fa8bebc17 | 题面有误 | 题面对象须整体修正。 |
| QX-P-002157 | b00158d587d41338 | 题面有误 | 人话版把 not virtually residually solvable 弱化成没有有限指数可解子群，改变了问题。 |
| QX-P-002158 | c3df1c36a2ed7f71 | 题面有误 | 恢复非可分范围。 |
| QX-P-002159 | fa91d245505d6291 | 题面有误 | 人话版“摆球”和 d=1 密度恒为1均错误。 |

## QX-P-002135｜32f64ab5cb34f8b2｜部分进展

**旧卡 → 本轮变化。** 输入状态为 `partially_solved`。模型确为 trapped kinetic/growing self-avoiding walk。经典文献支持必被困与有限平均长度，2020 论文给约 71 的数值背景；本次未找到原问解析期望的完整表达。保留部分进展，不能把模拟小数升级为精确结果。

**直接证据与定位。**

- [What is the expected length of the Slimy Slug cellular automata?](https://math.stackexchange.com/questions/4398553/what-is-the-expected-length-of-the-slimy-slug-cellular-automata)：题面 L71–85，黑格、自避和均匀选未访问邻点规则。原问题求二维方格增长自避游走被困前长度的解析期望；数值 70.799611 是发帖者的模拟，不是精确常数。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Hooper–Klotz, Trapping in Self-Avoiding Walks with Nearest-Neighbor Attraction](https://arxiv.org/pdf/2006.12680)：p.1 摘要与 Introduction；PRE 102, 032132 (2020)。增长自避游走被困长度约 71；有吸引模型与无吸引基线应区分。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Trapping of genuine self-avoiding walks](https://doi.org/10.1103/PhysRevA.34.3304)：出版社检索摘要。标准 genuine self-avoiding walk 被困性质的原始线索；全文未读，不据此增加未核定理细节。 访问层级：仅搜索摘要；验证层级：核对题面或所述结果范围；未独立重做文献证明。

**量词、范围和结论。**

- 模型与必被困背景：**部分进展**。二维方格，每步在未访问邻点中等概率选择；标准增长自避游走。 
- 原问期望的解析表达：**暂未找到可验证结果**。求被困前步数的解析期望，需明确是否把初始格计作一步。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `Slimy Slug kinetic growth self avoiding walk expected length`
2. `genuine self avoiding walk square lattice trapping length 70.85 Hooper Laforge`

GitHub/Lean 网页索引：`site:github.com kinetic growth walk trapping length Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`kinetic growth walk trapping length (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 保留 partially_solved；补上标准模型名称、步数约定和文献；将解析期望与几乎必然终止分为两项。

**仍需复核。**

- 如要登记终止/有限期望的严格定理，补读 1986 原文相应定理；2020 的小数误差和计数约定需逐页核对。
- 未完成穷尽式引文检索；未独立模拟或运行代码。

## QX-P-002136｜8bb1315ed144f7b7｜题面有误

**旧卡 → 本轮变化。** 输入状态为 `open`。原题规则可完整恢复：X_{n+1}=(X_n+U_n)/2，U_n 为独立均匀圆周点。Huisman 2017 文章给 Markov 转移与数值稳态密度；尚未核到双峰位置的严格闭式结论。题卡无需继续写“规则缺失”。

**直接证据与定位。**

- [Peaks in the circle chaos game](https://math.stackexchange.com/questions/2785511/peaks-in-the-circle-chaos-game)：题面 L70–77；提问者关于每步均匀角度的评论 L123。圆周上每步均匀随机取点，取当前位置与该点的中点；询问径向分布及模拟双峰的位置。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Sander Huisman, The Chaos Game, Infinitygon and Markov Chains (Part III)](https://community.wolfram.com/t/the-chaos-game-infinitygon-and-markov-chains-part-iii/10247)：Probability density function、单步 CDF/PDF 与 Markov chain 段。原作者给出一般步长 alpha 的单步转移和数值稳态；alpha=1/2 对应本题。 访问层级：正文相关段落已读；验证层级：读取模型、公式与数值方法；未执行文中代码。

**量词、范围和结论。**

- 概率模型与径向分布方法：**部分进展**。均匀圆周中点过程；区分面积密度与半径直方图密度。 
- 所问双峰的严格位置/闭式密度：**暂未找到可验证结果**。原问模拟的约 0.35、0.60 双峰；不得仅凭画图确定精确常数。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `circle chaos game radial density peaks stationary distribution`
2. `random series uniform circle Bessel product J0 2 power radius density`

GitHub/Lean 网页索引：`site:github.com circle chaos game radial density Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`circle chaos game radial density (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 补齐随机规则、步长 1/2、均匀角度与待求量；把数值方法记为部分进展。

**仍需复核。**

- 旧备注中的 MO #352853 / Pinelis 线索本次精确检索未定位到可读对应全文，不将旧记录当本次核验。
- 双峰的唯一性、位置误差及解析形式尚待核；与 2244 已做全文比对。

## QX-P-002137｜3ff946964af5edb9｜原题已解

**旧卡 → 本轮变化。** 输入状态为 `solved`。已解状态成立：Riemann–von Mangoldt 的 N(T)~T log T/(2pi) 给 gamma_n~2pi n/log n，再用 Stirling 得 floor(log Gamma(x))~x log x，复合后即 2pi x。无须 RH 或 França–LeClair 的更强公式。

**直接证据与定位。**

- [Is gamma_floor(log Gamma(x)) asymptotic to 2 pi x?](https://math.stackexchange.com/questions/922134/is-it-true-that-gamma-lfloor-log-gammax-rfloor-sim-2-pi-x?r=31)：原题与 2023 Gary 评论。问 gamma_{floor(log Gamma(x))}~2 pi x；必须将 gamma_n 解释为所有正虚部非平凡零点按重数排序的纵坐标。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Hasanalizade–Shen–Wong, Counting zeros of the Riemann zeta function](https://arxiv.org/pdf/2107.06506)：pp.1–2，式 (1.1)、Corollary 1.2；N(T) 定义。给全部非平凡零点计数的显式误差界，足够推出 n 阶纵坐标的一阶渐近；不假设 RH。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [NIST DLMF, Gamma function asymptotic expansions](https://dlmf.nist.gov/5.11)：§5.11(i)，式 5.11.1。Stirling 对数 Gamma 渐近，支撑 m~x log x。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。

**量词、范围和结论。**

- 原题渐近式：**原题已证**。x→+∞；gamma_n 为全部非平凡零点正纵坐标、按重数排序。 令 m=floor(log Gamma(x))，m~x log x、log m~log x，故 gamma_m/(2pi x)~m/(x log m)→1。
- 若只列临界线零点的另一定义：**未作判断**。该定义不等同于本卡已证版本，不把全部零点计数结论无条件转给它。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `Riemann von Mangoldt nth zero asymptotic Gamma Stirling`
2. `Franca LeClair 1307.8395 gamma n 2 pi n log n asymptotic`

GitHub/Lean 网页索引：`site:github.com Riemann von Mangoldt nth zero Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`Riemann von Mangoldt nth zero (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 维持 solved；补充标准零点排序与不依赖 RH 的简短推导；不把更强的零点定位式当作依赖。

**仍需复核。**

- 未核新的更精细误差阶；GitHub 中 RH/零点仓库仅为背景，不等同本复合渐近式。

## QX-P-002138｜4e4aed1935f0ea28｜部分进展

**旧卡 → 本轮变化。** 输入状态为 `partially_solved`。保留部分进展。新的 2026-10-22 MO 回答明确自称 partial、注明 AI assistance：处理有理根差、以及负/零判别式的整数或半整数平移；并明确正非平方判别式仍未解决。旧卡不可把 Gelfond–Schneider 的指数超越性误当 pi*cot(pi*sqrt(d)) 无理性。

**直接证据与定位。**

- [Reciprocal quadratic series rationality criterion](https://math.stackexchange.com/questions/1264972/is-it-true-that-sum-n-0-infty-frac1n22anb-in-bbb-q-iff-exists-k)：原题 L71–78，a,b 为正整数；k 为正整数。充分性以望远镜和完成，a²=b 时为 pi²/6 减有理数。必要性的正非平方判别式部分没有原帖解答。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [jvvk, partial answer to general quadratic reciprocal sum](https://mathoverflow.net/questions/498167/when-is-the-series-sum-n-1-infty-frac1a-n2-b-n-c-rational/516262)：回答 L135–153，分情形 1–3、Cases not settled；2026-10-22。说明已覆盖范围及正非平方残余；包含 AI assistance 自述，非完整解决声明。 访问层级：正文相关段落已读；验证层级：逐项核对参数替换与未覆盖范围；没有将社区帖视作完整专家认证。

**量词、范围和结论。**

- a²−b 为正平方时的充分性及零判别式：**部分进展**。a,b∈Z_{>0}；正平方时 k<a，有限望远镜和；零时不是有理。 
- a²−b<0：**部分进展**。MO 2026 回答用 Nesterenko Corollary 6 给相应超越性推导；本次未完整重审该原始超越性定理。 
- a²−b>0 非平方的必要性：**暂未找到可验证结果**。不能由 exp(i*pi*sqrt(d)) 超越直接推出 pi*cot(pi*sqrt(d)) 无理。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `rational infinite sums reciprocal quadratic polynomial Nesterenko`
2. `sum 1/(n^2+2an+b) rational square discriminant transcendental`

GitHub/Lean 网页索引：`site:github.com quadratic reciprocal series rationality Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`quadratic reciprocal series rationality (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 维持 partially_solved；补记 2026 partial 回答及其 AI assistance；新索引候选 1736 应关联为更一般二次多项式问题，待取正文。

**仍需复核。**

- Nesterenko 1996 Corollary 6 与 ASSST 2001 的原稿定理全文尚未审计。
- 正非平方情形无完整结论；1736 正文未在本包提供，只记查重候选。

## QX-P-002139｜80b39c747eee0e48｜题面有误

**旧卡 → 本轮变化。** 输入状态为 `open`。纠正人话版把“非”字怀疑为误写并称近乎自动的描述。原题明确问无限多个非 Wolstenholme 素数；有限范围中只有少数 Wolstenholme 素数或启发式密度不能证明该无限性。本次未找到无条件全解。

**直接证据与定位。**

- [Are there infinitely many non-Wolstenholme primes?](https://mathoverflow.net/questions/85383/are-there-infinitely-many-non-wolstenholme-primes)：原题定义和 regular primes 评论。确实问非 Wolstenholme 素数无穷，不是误写；p≥5，Wolstenholme 性对应加强到模 p⁴ 的同余。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [McIntosh, On the converse of Wolstenholme’s theorem](https://matwbn.icm.edu.pl/ksiazki/aa/aa71/aa7144.pdf)：Acta Arithmetica 71 (1995) 原刊检索条目。同余与逆命题背景；不是本次找到的无限性证明。 访问层级：搜索结果中的原刊摘录，未读完整 PDF；验证层级：核对题面或所述结果范围；未独立重做文献证明。

**量词、范围和结论。**

- 题面非 Wolstenholme 方向：**题面有误**。原帖明问 non-Wolstenholme；不能改成 Wolstenholme 素数无穷。 
- 非 Wolstenholme 素数无穷性：**暂未找到可验证结果**。对所有足够大范围的无限性问题，非有限扫描问题。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `infinitely many non Wolstenholme primes theorem`
2. `Bernoulli B p-3 nonzero modulo p infinitely many Booker 2101.11157`

GitHub/Lean 网页索引：`site:github.com non Wolstenholme primes Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`non Wolstenholme primes (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 删除“原作者也许问相反命题”“几乎自动”等误导；维持精确的无限性问题。
- 与 000041 标同源不同问，禁止合并。

**仍需复核。**

- Booker arXiv:2101.11157 的扫描上界本轮未逐页复查，不重报旧数字。
- 若出现基于 abc/regular primes 的论证，须核查是否真涵盖 B_{p−3} 的同一量词。

## QX-P-002140｜6ee3bcbdf459c5d6｜题面有误

**旧卡 → 本轮变化。** 输入状态为 `open`。题卡的人话版将原问弱化成 up to isogeny，必须修正。Voisin 2024 和 Scavia–Suzuki 2025 给的是阿贝尔簇意义下产品 Jacobian 的直和项与整 Hodge/Tate 类条件的等价。2025 引言指出复数上的普遍产品命题仍未定，并有 Q 上带有理点曲线版本的障碍；不能当作所有基域、单个 Jacobian 的全解。

**直接证据与定位。**

- [Is every abelian variety a direct summand of the Jacobian of a curve?](https://mathoverflow.net/questions/58500/is-every-abelian-variety-a-direct-summand-of-the-jacobian-of-a-curve)：原题：up to isogeny 已知，随后问 stronger statement。原问是真正直和项，不是只差同源；还须明确基域、单个 Jacobian 与产品的区别。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Voisin, Cycle classes on abelian varieties and the geometry of the Abel-Jacobi map](https://webusers.imj-prg.fr/~claire.voisin/Articlesweb/PAMQ-20-5-a14-VOISIN.pdf)：Pure Appl. Math. Q. 20(5) (2024), pp.2469–2470 引言。直和项为 abelian variety 意义；与整 Hodge 猜想的曲线类相关。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Scavia–Suzuki, On direct summands of products of Jacobians over arbitrary fields](https://arxiv.org/html/2507.09821v2)：v2 2025-07-22；Introduction L50–74，Theorem 1.2。产品 Jacobian 判据、带 k 点条件、Q 上障碍与复数范围尚未定的明确说明。 访问层级：正文相关段落已读；验证层级：已读引言和 Theorem 1.2 的对象/量词；未重做全篇证明。

**量词、范围和结论。**

- up to isogeny 的弱版本：**部分进展**。原帖已明确知道的经典弱结果；不是待解的 stronger statement。 
- 真正直和项/产品 Jacobian 的周期类判据：**部分进展**。Scavia–Suzuki Theorem 1.2 有极化条件；曲线带 k 点；复数结果对应 integral Hodge classes。 
- 单个 Jacobian 的原问：**暂未找到可验证结果**。需首先指定基域；不能由产品的等价条件自动推出。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `abelian variety direct summand Jacobian integral Voisin`
2. `2212.03046 direct summand product Jacobians universal zero cycle`

GitHub/Lean 网页索引：`site:github.com abelian variety direct summand Jacobian Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`abelian variety direct summand Jacobian (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 题面改为真正直和项并补基域；删除把 Voisin 结果记成 up-to-isogeny 的说法；单曲线与产品分别列。

**仍需复核。**

- 2025 结果引用的 Petrov–Skorobogatov Q 上反例仅带 k 点曲线版本；不能删除该条件。
- 若要把状态改为 solved，需先补原问具体基域和单个 Jacobian 条件。

## QX-P-002141｜fd14b036e65b5cbf｜题面有误

**旧卡 → 本轮变化。** 输入状态为 `open`。当前 HR E∞ 化叙述使问题变成已知常识，须改为沿 S→HZ 的谱提升。原帖记录 Z[i] 不可提升及函子性障碍；2026 Szafarczyk 论文给 delta-hat 必要条件的 scheme 推广，但本轮其全文不可达，不能宣称分类完成。

**直接证据与定位。**

- [What kind of commutative rings lift to the sphere?](https://mathoverflow.net/questions/475114/what-kind-of-commutative-rings-lift-to-the-sphere)：题面中的 HA ≃ S_A ⊗_S HZ；Rognes、Krause、Z M 评论。原问题不是 HR 是否有 E∞ 结构，而是存在 S_A 经基变换得到 HA，另问可提升环的分类与函子性。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Szafarczyk, An obstruction to lifting schemes to spectral schemes](https://arxiv.org/abs/2607.11853)：arXiv 提交 2026-07-13，摘要。将 Nikolaus 的 delta-hat 必要障碍推广到 schemes。 访问层级：作者摘要的学术索引；abs/html/pdf 直开均 DisabledError；验证层级：仅核摘要范围；未读定理编号或全文。
- [Szafarczyk 讲座摘要](https://www.mimuw.edu.pl/en/seminars/talk/an-obstruction-to-lifting-schemes-to-spectral-schemes/)：2025-03-12，Warsaw seminar。作者报告障碍及 Ga、椭圆曲线的 scheme 例子；不等于所有交换环分类。 访问层级：作者讲座摘要索引；验证层级：核对题面或所述结果范围；未独立重做文献证明。

**量词、范围和结论。**

- 现卡 HR/E∞ 表述：**题面有误**。应为 HA≃S_A⊗_S HZ 的交换环谱提升；HR 本身总可作为 E∞ 环谱。 
- 可提升环的分类与函子性：**部分进展**。有必要的 delta-hat 结构、反例及函子性障碍；不是 iff 分类。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `commutative rings lift sphere spectrum obstruction Szafarczyk`
2. `HA spherical lift tensor HZ Z[i] Schwanzl Vogt Waldhausen`

GitHub/Lean 网页索引：`site:github.com commutative ring lift sphere Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`commutative ring lift sphere (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 立即重写提升定义，拆出存在性、分类、函子性；不可把该卡标成“所有 R trivially lift”。
- 与 2423 的互引是稳定同伦/cotangent 关键词误配，非同题。

**仍需复核。**

- 2026 预印本三种公开端点均不可达；需补全文及最新修订才能核对具体定理。
- 原帖 Rognes 所引 Schwänzl–Vogt–Waldhausen 1999 pp.245–249 本轮未逐页读取。

## QX-P-002143｜b4c93142c191f456｜题面有误

**旧卡 → 本轮变化。** 输入状态为 `open`。题卡混淆两处定义：有限维 Hopf 的积分空间一维不能作为半单等价，S²=id 也不替代 C*-Hopf/Kac 结构存在。Abella 原刊摘要已证明维数<24 的半单复 Hopf 全部可紧致化；一般存在性及反例最小维数本次未获全解。

**直接证据与定位。**

- [Is there a non-Kac complex finite-dimensional semisimple Hopf algebra?](https://mathoverflow.net/questions/324111/is-there-a-non-kac-complex-finite-dimensional-semisimple-hopf-algebra)：原题对 Kac algebra 的 C*-Hopf 定义及最小维数/障碍子问。原问是复有限维半单 Hopf 代数是否总能赋予兼容的紧致/C* involution；不是只要求 antipode 平方等于 id。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Abella, Some advances about the existence of compact involutions in semisimple Hopf algebras](https://link.springer.com/article/10.1007/s40863-018-0109-9)：Abstract；São Paulo J. Math. Sci. 13 (2019), 628–651。dim<24 可紧致化，并有若干 twisting 家族；非全维结论。 访问层级：出版社摘要及参考文献；全文订阅限制；验证层级：核对题面或所述结果范围；未独立重做文献证明。

**量词、范围和结论。**

- 现卡 Kac/半单定义：**题面有误**。原帖要求兼容 * 和 C* 正性；Larson–Radford 的 S²=id 不能解决此紧致化问题。 
- 维数小于 24：**部分进展**。所有复半单有限维 Hopf 代数，dim<24。 
- 一般紧致化存在性及非 Kac 最小维数：**暂未找到可验证结果**。若有反例，则本次取得的已刊界给 dim≥24；不声称 dim24 已被完整分类。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `semisimple Hopf algebra compact involution Kac existence`
2. `Larson Radford S squared identity compatible C star Hopf algebra`

GitHub/Lean 网页索引：`site:github.com semisimple Hopf Kac compact involution Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`semisimple Hopf Kac compact involution (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 修正人话版半单与 Kac 定义；恢复存在兼容正 *-结构的量词；补 dim<24 的严格范围。
- 与 000448 上同调有限生成仅同属 Hopf 领域，主命题不等价。

**仍需复核。**

- 需要新的完整原稿才可声称一般已解或给出最小反例；本次未核传递的分类文献全文。

## QX-P-002144｜b8119b18201c1692｜题面有误

**旧卡 → 本轮变化。** 输入状态为 `open`。原问是文献/精确化请求，题卡把它改写成特定递推构造并无出处。可保留 1100–1106 例子和 Jacobsthal 函数线索，但须恢复原问题类型；单纯光滑数短区间成果不能自动算解答。

**直接证据与定位。**

- [Small primes attract large primes](https://mathoverflow.net/questions/78626/small-primes-attract-large-primes?r=31)：题面 L32–38；Kalai 与 Paseman/Jacobsthal 评论 L60–74。原作者问是否已有结果量化短区间小素因子聚集与邻近大素因子的现象，没有定义题卡叙述的递推序列。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。

**量词、范围和结论。**

- 题卡中的递推规则：**题面有误**。原帖没有该递推；是七个连续整数质因子例子和已有量化结果的询问。 
- 原问相关精确结果/文献：**未作判断**。缺少固定可检验的全称不等式，不能以 ordinary open theorem 标签替代。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `small primes attract large primes largest prime factor consecutive integers`
2. `Gil Kalai small large prime factors nearby integers smooth numbers`

GitHub/Lean 网页索引：`site:github.com small primes attract large primes Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`small primes attract large primes (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 删除无出处的递推过程；题型改为参考文献/问题精确化；保留原作者实际例子。

**仍需复核。**

- Jacobsthal 函数与 prime constellations/admissible sets 是原帖线索，本轮未取得与“吸引”同一条件化统计量的精确定理。
- 新增索引候选 000231 仅作相关文献方向，未读其全文，不报告重复。

## QX-P-002145｜0652b5bc6b52768d｜题面有误

**旧卡 → 本轮变化。** 输入状态为 `partially_solved`。须修正实矩阵/归一化量纲。cstheory 交叉帖有明确双侧界：上界 ceil(n²/(2eps))^{n²}，体积法下界 (Ω(n/eps))^{n²}；2011 Aubrun 的 cut-norm 球体积回答另提供改进线索，但不是本轮已核的最终最优 covering number。

**直接证据与定位。**

- [Epsilon-nets with respect to the cut norm](https://mathoverflow.net/questions/53542/epsilon-nets-with-respect-to-the-cut-norm)：原题的 [0,1]^{n×n}、未归一化 cut norm、non-proper net 编辑。实矩阵立方体，不限 0/1 图邻接矩阵；允许讨论中心在非负矩阵空间的 net。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Tsuyoshi Ito, answer on cut-norm epsilon nets](https://cstheory.stackexchange.com/questions/4622/epsilon-nets-with-respect-to-the-cut-norm)：回答 L111–128；non-proper 注释 L143。给初等上界及体积法下界，回答原问一部分。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Aubrun, volume of cut-norm unit ball](https://mathoverflow.net/questions/56218/the-volume-of-the-unit-ball-in-mathbbrm-times-n-with-respect-to-the-cu/77798)：2011-10-11 answer L75–77。给算子范数/张量空间体积比较与对数因子线索。 访问层级：正文相关段落已读；验证层级：仅核作者回答所述范围；未复核跨链接体积定理。

**量词、范围和结论。**

- 原问题对象：**题面有误**。[0,1] 实矩阵；cut norm 是所有矩形子块和绝对值的最大值，不除 n²。 
- 已有 covering 双侧界：**部分进展**。Ito 答案；对 non-proper nets 其下界仍适用；大小 eps 时需保留至少1的退化约定。 
- 最优 eps-net 精确渐近：**暂未找到可验证结果**。Aubrun 后续体积/张量范数线索尚需核对其依赖和参数区间。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `epsilon nets cut norm matrices covering number upper lower bounds`
2. `cut norm metric entropy unit cube n squared epsilon Tsuyoshi Ito`

GitHub/Lean 网页索引：`site:github.com epsilon net cut norm matrices Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`epsilon net cut norm matrices (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 维持 partially_solved；题面改回实矩阵与正确缩放；补交叉帖直接链接和 non-proper 下界范围。

**仍需复核。**

- 是否能使用后续球体积结果给更尖锐 net 界需另核；未把 graphon 置换商/归一化 cut distance 结果直接套用。

## QX-P-002146｜fab839b1925f2409｜题面有误

**旧卡 → 本轮变化。** 输入状态为 `partially_solved`。2014 Marché–Maurin 全文 Theorem1.1 给技术假设下除有限条斜率外 character variety reduced zero-dimensional，进而不可约 SL2(C) 表示 H¹=0。它是相关的泛型刚性成果，不能删去假设或把原问所有非中心 SU2 表示、所有斜率一并标 solved。

**直接证据与定位。**

- [Rigidity of representations of Dehn fillings on the figure-eight knot](https://mathoverflow.net/questions/62389/rigidity-of-representations-of-dehn-fillings-on-the-figure-eight-knot)：原问非中心 SU(2) 表示、H¹(M,Ad rho)=0；曲线 F(x,y) 与 px+qy=0。刚性指无穷小刚性，不是超曲表示全局唯一；原问非中心 SU(2) 表示的范围须保留。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Marché–Maurin, Singular intersections of subgroups and character varieties](https://webusers.imj-prg.fr/~julien.marche/papiers/SICV.pdf)：p.3 Theorem1.1；p.6 (v)；pp.7–8 Proposition2.2。明确三项技术假设、有限例外斜率及 H¹ 对应。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。

**量词、范围和结论。**

- 刚性的定义及原问范围：**题面有误**。无穷小 H¹=0；非中心 SU2，与 hyperbolic representation 唯一性不同。 
- 泛型 Dehn 填充的不可约表示：**部分进展**。Theorem1.1 假设 r proper、X(M) reduced、奇点边界像非 torsion；结论 all but finitely many slopes。 
- 原问全部斜率/非中心 SU2 表示：**暂未找到可验证结果**。原帖指出 |p/q|<sqrt20 的横截性、有限 p 数值检验；不能把数值检验当全称证明。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `figure eight knot Dehn filling infinitesimal rigidity Marche Maurin`
2. `Singular intersections subgroups character varieties 1406.2862 H1 SU2`

GitHub/Lean 网页索引：`site:github.com figure eight Dehn filling rigidity Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`figure eight Dehn filling rigidity (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 保留部分进展；修正刚性定义和表示范围；明确有限例外与适用假设。
- 与 000590 纯装饰手术（不同斜率的保向同胚）相关但不等价。

**仍需复核。**

- 本轮未完成八字结满足每项技术假设、全部例外斜率与可约但非中心表示的逐项验证。
- 未运行原帖数值程序或任何外部代码。

## QX-P-002147｜749390830da8e305｜题面有误

**旧卡 → 本轮变化。** 输入状态为 `open`。应保留原帖三项方法论问题及2010背景。自然证明屏障有 constructivity/largeness/usefulness 等精确假设，描述复杂性形式不自动豁免。2026 Zenodo/Lean 项目证明 Cook–Levin/Karp 完备性工具，不是这三个问题或 P vs NP 的解决。

**直接证据与定位。**

- [How can a descriptive-complexity approach to P vs NP avoid natural proofs?](https://mathoverflow.net/questions/34980/how-can-an-approach-to-p-vs-np-based-on-descriptive-complexity-avoid-being-a)：2010 原帖的三个问题及 Deolalikar 背景。原问讨论 uniformity 是否必需、既有描述复杂性证明如何避开屏障、以及超出对角化的用法；不直接要求证明 P≠NP。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Williams, Natural Proofs versus Derandomization](https://people.csail.mit.edu/rrw/natural-journal.pdf)：作者论文检索标题/摘要。自然证明和去随机化的相关理论背景，未当作原帖三问的完整回答。 访问层级：学术索引；未逐页读取；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [DescriptiveComplexity: Completeness by First-Order Reductions in Lean](https://zenodo.org/records/21678424)：发布摘要；DOI 10.5281/zenodo.21678424。声称形式化 machine-free Cook–Levin、Karp21 等，目标不同。 访问层级：公开索引摘要；验证层级：命题范围不适用，未独立形式化验证。

**量词、范围和结论。**

- 原帖三项方法论问题：**未作判断**。uniformity、描述复杂性既有例子与避障机制须逐项陈述，并非单一新猜想。 
- 相关形式化工具：**部分进展**。Zenodo/PierreSenellart 项目声称形式化逻辑归约与完备性，不蕴含 P vs NP 分离。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `descriptive complexity natural proofs uniformity Razborov Rudich`
2. `FO LFP circuit lower bounds natural proofs uniform complexity Deolalikar`

GitHub/Lean 网页索引：`site:github.com descriptive complexity natural proofs Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`descriptive complexity natural proofs (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 题型保留方法论/参考文献问题，列出三问；不要据 Deolalikar 2010 失败推断一切描述复杂性路线失败。
- 与000502的VP≠VNP相关但不等价，禁止合并。

**仍需复核。**

- Natural Proofs 1997 和 Williams 论文的全部假设/例子未深读；不做新的屏障定理裁决。
- AI站 P=NP 宣称未对准原问，且未审计，不升级状态。

## QX-P-002148｜919aa2d1927089e5｜公开声明待核

**旧卡 → 本轮变化。** 输入状态为 `open`。Ohta原稿Example3.3.4 p.25确实提出配对k+k′=p+1同时整除问题，核心范围4≤k≤p−3，原帖加入的k=2是平凡边界。2010“相信有证明”无文稿链接，2012尚有追问；本次未找到可核完整证明或反例，不能只写从无声明。

**直接证据与定位。**

- [A conjecture on p-divisibility of Bernoulli numbers](https://mathoverflow.net/questions/21125/a-conjecture-on-p-divisibility-of-bernoulli-numbers)：原帖L33–38；2012-03-14 Dalawat追问L86–90。p为奇素数，k偶且2≤k≤p−3，讨论既约分子不能同时被p整除；提问者2010自称相信有证明。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Ohta, Companion Forms and the Structure of p-adic Hecke Algebras](https://arxiv.org/pdf/math/0403428)：v2 2004-07-24，p.25 Example(3.3.4)，L1672–1696。核心配对范围、历史检查p≤4001、尚不知道例子的原始表述。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。

**量词、范围和结论。**

- 原命题与出处：**部分进展**。整除的是Bernoulli数分子；Ohta k+k′=p+1，4≤k≤p−3，p≤4001检查是历史界。 
- 2010提问者证明声称：**完整证明/反例声明待核**。只说believe I have a proof，未提供完整稿；不是本次新证明或已验证结果。 
- 一般配对不可整除命题：**暂未找到可验证结果**。所有奇素数与给定偶k的量词；不由历史有限表推出。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `Ohta conjecture Bernoulli numbers divisibility companion forms`
2. `B_k B_p-k+1 simultaneous divisibility odd prime Ohta 3.3.4`

GitHub/Lean 网页索引：`site:github.com Ohta Bernoulli divisibility Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`Ohta Bernoulli divisibility (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 补足原始问题定位和分子约定；旧证明声称单独记录为未提供稿件待核，不当作solved。

**仍需复核。**

- 需追踪unramified后来的文稿、Calegari Eisenstein primes线索及最新反例数据；本轮未找到可对应完整稿。

## QX-P-002149｜5c0b839c16830381｜题面有误

**旧卡 → 本轮变化。** 输入状态为 `partially_solved`。未经等模限制的宽版本有直接反例：a=i、lambda1=1/2、lambda2=1给Theta(n)=arctan(2^(−n))，非零却指数趋零，故不可能有倒数次指数的正下界。等模critical case不能据此否定；本轮LRS/Baker文献只算相关工具。

**直接证据与定位。**

- [Lower bounds for linear forms of logarithms (a la Baker)?](https://mathoverflow.net/questions/11212/lower-bounds-for-linear-forms-of-logarithms-a-la-baker)：题面L33–42，固定复代数a,lambda1,lambda2，arg的次指数倒数下界。文字上允许任意复代数参数，随后指出等模critical case；必须区分宽表述与等模限制。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Ouaknine–Worrell, Positivity Problems for Low-Order Linear Recurrence Sequences](https://www.cs.ox.ac.uk/james.worrell/pos12.pdf)：作者PDF p.1摘要；SODA2014。低阶LRS positivity决定性，不自动解决任意两指数和的argument下界。 访问层级：正文相关段落已读；验证层级：读摘要及对象；未将LRS positivity等同原题。

**量词、范围和结论。**

- 按原帖字面、不加等模条件的全称版本：**原题已反驳**。a=i,lambda1=1/2,lambda2=1，n≥1；主幅角Theta(n)>0。 此结论仅覆盖原文未加等模条件的字面全称版本，不覆盖作者强调的等模 critical case。 
- 原帖强调的等模critical case：**暂未找到可验证结果**。需加|lambda1|=|lambda2|，并指明有效/非有效下界；上述反例不满足等模。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `Baker lower bound argument sum algebraic exponential Ouaknine Worrell`
2. `arg a lambda1^n lambda2^n subexponential lower bound equal modulus`

GitHub/Lean 网页索引：`site:github.com Baker algebraic exponential argument lower bound Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`Baker algebraic exponential argument lower bound (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 宽版本给简单反例；等模情形另列待核，禁止一并标已反驳。
- 旧注记将本篇标为LICS2014，宜改SODA2014，DOI10.1137/1.9781611973402.27。
- 不得把宽字面版本反例导入为等模主问题已反驳；状态需保留这一版本区别。

**仍需复核。**

- 等模情形的有效性、分支和参数退化尚需专门审查；本轮未尝试完整证明。

## QX-P-002150｜779fe204efb1672f｜部分进展

**旧卡 → 本轮变化。** 输入状态为 `open`。英文标题2^k替代2k造成严重变义。Holo回答在AC_omega与E0 transversal（并从某强紧假设推出这些）下证明P⇒Q，没有纯ZF无条件蕴含。应记有条件部分进展，不能因有答帖标solved。

**直接证据与定位。**

- [If every infinite cardinal is divisible by 2, must every infinite cardinal k satisfy k=2k?](https://mathoverflow.net/questions/516973/if-every-infinite-cardinal-is-divisible-by-2-must-every-infinite-cardinal-k/518059)：题面P/Q；Holo answer#518059的假设与证明。ZF中P:每个无限基数k=2l某l；Q:k=2k对所有无限k。这里乘法2k，不是幂2^k。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。

**量词、范围和结论。**

- 题卡指数/乘法：**题面有误**。Q是所有无限基数k的k=2k；2^k=k与Cantor定理冲突。 
- 加入弱选择条件的P⇒Q：**部分进展**。ZF+P+AC_omega+E0 transversal证明Q；回答另用L_{omega1,omega}强紧基数条件。 
- 纯ZF下P⇒Q：**暂未找到可验证结果**。不能在没有AC_omega/E0 transversal的前提下引用该证明。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `infinite cardinal divisible by two doubling ZF choice`
2. `Self Complementary Graphs Weak Consequences Axiom Choice k infinite cardinal`

GitHub/Lean 网页索引：`site:github.com infinite cardinal divisible two doubling ZF Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`infinite cardinal divisible two doubling ZF (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 英文标题改乘法2k，恢复P、Q全称命题；建议open→partially_solved（条件结果），原问题未宣称全解。

**仍需复核。**

- 强紧条件的精确定义及可否去除、逆向蕴含/一致性强度需另核；未找到无条件答案。

## QX-P-002151｜bdbbe7ee3e44ce36｜公开声明待核

**旧卡 → 本轮变化。** 输入状态为 `open`。已定位公开非可均性预印本、人类解释论文和实际Lean solution入口。docs/248明说不给显式边界常数或指定生成集；Main仍用存在量词给S,b，不能算显式分解已答。ComparatorChallenges的sorry是比较模板，不能错判为solution缺失；本轮仅静态核声明，未重跑或递归审计依赖。

**直接证据与定位。**

- [Paradoxical decompositions of Thompson’s F](https://mathoverflow.net/questions/515834/paradoxical-decompositions-of-thompsons-f)：Salo原帖：有限T，两注入f_i(g)∈gT且像不交；S/T构造评论。原问显式/可计算悖论分解；背景非可均性与具体有限移动集、两个注入须区分。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [OpenAI math scope document248](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/248.md)：commit adc7f1241b42e322a6451854ab7e4b4c146bf78a；Scope。标准dyadic PL的F，明确不提供explicit boundary constant/prescribed generating set。 访问层级：正文相关段落已读；验证层级：读main说明，并用路径提交历史锁定初始提交；未运行。
- [OpenAI Lean solution: Thompson Main](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/GroupTheory/Thompson/Main.lean)：thompson_F_uniform_boundary；thompson_F_not_amenable；thompson_F_nonamenable_composition。实际入口用∃(S:Finset F)(b:R) uniform boundary导出非可均性，未给原问显式分解。 访问层级：固定提交源文件完整已读；验证层级：已核入口声明与量词、未重跑；未审计全部传递依赖。
- [Kim–Lodha, A note on the proof of nonamenability of F](https://arxiv.org/html/2610.18360v1)：v1 2026-10-13；Theorem0.1，说明no novelty、human written。背景非可均性的人类简化证明，未把显式分解作为结果。 访问层级：正文相关段落已读；验证层级：读引言、主定理和证明结构；未独立重建全篇证明。
- [Thompson comparator config](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ThompsonNonamenability.json)：challenge_module/solution_module/theorem_names/permitted_axioms。solution_module=OAI.GroupTheory.Thompson.Main；允许propext、Quot.sound、Classical.choice；enable_nanoda=false。 访问层级：固定提交JSON完整已读；验证层级：仅配置静态读取；模板sorry不计为solution占位。

**量词、范围和结论。**

- 背景非可均性：**完整证明/反例声明待核**。OpenAI2026-09-23，Kim–Lodha人类说明Theorem0.1；Lean声明排除标准dyadic PL群的不变均值。 
- 原问具体T、f1、f2的显式悖论分解：**暂未找到可验证结果**。需明确有限移动集与注入/不交的映射或算法；存在性∃S,b不足。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `Thompson group F explicit paradoxical decomposition OpenAI Kim Lodha`
2. `Thompson F nonamenability 2610.18360 D 2^62 Folner Lean`

GitHub/Lean 网页索引：`site:github.com Thompson F paradoxical decomposition Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`Thompson F paradoxical decomposition (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 显式构造原问独立于背景非可均性；补真实Lean solution路径，删除任何由Comparator模板sorry推断无形式化证明的描述。
- 新增2477与2051标题索引关联线索：核验非可均性/逆向数学强度；未取正文，不合并。

**仍需复核。**

- 未执行Lean/comparator，未审Main四个导入StandardCharacterization、FiniteBoundary、AnalyticConstruction、MeanToFolner的传递闭包。
- 已读lean/lean-toolchain=leanprover/lean4:v4.34.1；lean/lake-manifest.json中mathlib=d13f23b723b8a846827a245b89c10fc7d3f11612，不等于构建通过。
- 原帖Astra的D=2^62是低信心候选，未获具体S/T，不计解答。

## QX-P-002152｜436108804343377d｜题面有误

**旧卡 → 本轮变化。** 输入状态为 `open`。标题“评论级否定共识”扩大了评论量词：Sawin对Q2机制的质疑不是Q1不存在的证明。Rached2026摘要给genuine noncongruence权2例子，但未证明Deligne系数界；全文不可达，不能升级。

**直接证据与定位。**

- [Existence of any genuine noncongruence modular cusp form satisfying Deligne bound](https://mathoverflow.net/questions/514114/existence-of-any-genuine-noncongruence-modular-cusp-form-satisfying-deligne-boun?noredirect=1)：Question1/Question2；Will Sawin对第二问的评论。Q1问存在一个genuine noncongruence cusp form满足Fourier系数Deligne界；Q2问仿同余情形的上同调机制。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Rached, Noncongruence cusp forms, Veech groups and enumeration](https://arxiv.org/abs/2609.28514)：2026-09学术摘要；作者主页列submitted。genuine noncongruence权2尖形式构造；摘要没有本问系数增长界。 访问层级：仅作者摘要索引；abs/html/pdf均DisabledError；验证层级：仅核摘要，旧注记Question6.1本轮未取得正文。

**量词、范围和结论。**

- 存在一个满足Deligne界的genuine noncongruence form：**暂未找到可验证结果**。存在量词；Fourier a_f(n)，原帖界n^((k−1+eps)/2)，不能擅加Hecke eigenform。 
- Q2的几何/上同调解释：**未作判断**。Sawin负面评论限制于机制，不是一般不存在定理。 
- 题卡标题/人话版全称否定：**题面有误**。分开Q1、Q2，删除“否定共识”等未经证明状态。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `genuine noncongruence cusp form Deligne bound John Rached`
2. `2609.28514 Fourier coefficients noncongruence Selberg bound n four fifths`

GitHub/Lean 网页索引：`site:github.com noncongruence cusp form Deligne bound Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`noncongruence cusp form Deligne bound (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 重写两子问，恢复存在量词及Fourier系数；删除标题“评论级否定共识”。

**仍需复核。**

- Rached arXiv:2609.28514的§6/Question6.1及版本全文未成功取得。
- 须区分“非所有形式满足”与“无任何一个形式满足”。

## QX-P-002153｜c3db20a7d8061003｜题面有误

**旧卡 → 本轮变化。** 输入状态为 `open`。补回原题的维数、截面曲率范围和直径泛函。旧备注把 2015 MO #221270 称同题不准确：该帖询问能否避免可计算性给证明，与显式例子不是同一要求。本轮未定位精确原问的可验证具体例子。

**直接证据与定位。**

- [Do we have any concrete examples of Nabutovsky–Weinberger metrics?](https://mathoverflow.net/questions/513870/do-we-have-any-concrete-examples-of-nabutovsky-weinberger-metrics?noredirect=1)：原题：dim(M)≥5，sectional curvature∈[−1,1]，diameter functional 的局部极小。原问要可具体描述的 NW 度量；给定的几何量是受曲率约束的直径局部极小，不是最短闭测地线或分割超曲面。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Nabutovsky–Weinberger, Variational problems for Riemannian functionals and arithmetic groups](https://arxiv.org/abs/math/9711225)：1997 作者摘要 L16–19。闭包 R_1(M) 上直径存在极深局部极小的抽象背景；本文题名不是 The fractal nature of Riem/Diff，本轮未读证明全文。 访问层级：作者摘要及版本元数据已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Can we find minimal-diameter metrics without computability?](https://mathoverflow.net/questions/221270/can-we-find-minimal-diameter-metrics-without-computability)：索引中的题名/问题摘要。问题是能否不用可计算性证明相关几何结论，不是要求具体 NW 度量实例。 访问层级：仅搜索索引，未读该帖全文；验证层级：核对题面或所述结果范围；未独立重做文献证明。

**量词、范围和结论。**

- 现卡对 NW 度量的对象描述：**题面有误**。闭光滑 M，dim≥5；在曲率 [−1,1] 的度量空间中讨论 diameter 的局部极小。 
- 具体、可描述的 NW 度量实例：**暂未找到可验证结果**。须说明流形、度量及局部极小的可核验证明；只引用抽象存在性不够。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `concrete examples Nabutovsky Weinberger metrics diameter minima`
2. `sectional curvature minus one one diameter local minimum explicit metric Nabutovsky`

GitHub/Lean 网页索引：`site:github.com Nabutovsky Weinberger metric Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`Nabutovsky Weinberger metric (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 把人话版替换为原问的直径局部极小与曲率约束；删除“11 年无实例”的未经对应论证。
- 与 002277 的 Calabi–Croke 球面闭测地线/面积猜想不等价，不合并。

**仍需复核。**

- 局部极小所在空间的 C^{1,alpha} 完备化和光滑代表要求需进一步核定。
- 2015 相关提问未全文复查；本轮没有找到不代表证明不存在具体例子。

## QX-P-002154｜d81b10eba4e703c8｜题面有误

**旧卡 → 本轮变化。** 输入状态为 `open`。修正人话版“左右单模存在性尚不明显”：通常含幺非零环在选择公理下左右都有单模，原问比较同构类数目。Artinian 特例由半单商得到对应；2026 Rickard 的撤回答案不能作反例，Osofsky 1971 讨论的 R 与 R-bar 是不同环。本轮无一般双侧 Noetherian 的完整解。

**直接证据与定位。**

- [Bijection between left and right simple modules for Noetherian rings](https://mathoverflow.net/questions/513412/bijection-between-left-and-right-simple-modules-for-noetherian-rings)：原题；Artinian 评论；Rickard 2026-08-08 撤回说明；Denis T 对 Osofsky 的评论。问双侧 Noetherian 环的左/右单模同构类是否等势，进一步才问好/自然的双射。Rickard 的候选环只单侧 Noetherian，因此撤回答案。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。

**量词、范围和结论。**

- 现卡存在性/双射层次：**题面有误**。先问左右简单模同构类的基数相同，再问可描述双射；须双侧 Noetherian。 
- Artinian 情形：**部分进展**。左右 Artinian 的含幺环，按半单商各简单分量对应。 
- 一般双侧 Noetherian 环：**暂未找到可验证结果**。单侧 Noetherian 的候选反例不满足假设；不把已撤回答案当证据。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `two sided noetherian ring left right simple modules bijection`
2. `Osofsky 1971 number simple modules noetherian Rickard counterexample`

GitHub/Lean 网页索引：`site:github.com noetherian ring left right simple modules Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`noetherian ring left right simple modules (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 补双侧 Noetherian、含幺及同构类量词；删除对单模存在性的错误疑问。
- 登记 Rickard 2026-08-08 撤回的具体原因；与 002354 根幂交为零问题不等价。

**仍需复核。**

- 可继续核对 Osofsky 1971 原稿，DOI 10.1016/0021-8693(71)90142-6；本轮仅实读原帖对其误用的澄清。
- aiXiv 2611.02893 的 Gorenstein symmetry 声称涉及自内射维数，不是左右单模同构类基数；仅索引线索，不适用。

## QX-P-002155｜9bd78f8936d34991｜题面有误

**旧卡 → 本轮变化。** 输入状态为 `open`。应恢复为文献/已知范围询问，不能把无人答帖解释成“最优范围为文献空白”。KMP Theorem C 已核为 GL_n 的整数系数斜率 2/3，Theorem A 的斜率 1 使用 Z[1/2]；均不能直接填入 SL_n(Z) 的答案。本轮未核定 SL_n 的最佳已知精确范围。

**直接证据与定位。**

- [Homological stability for SL_n(Z)](https://mathoverflow.net/questions/509822/homological-stability-for-mathrmsl-n-mathbb-z)：原帖一行问题：best known stable range，integer coefficients。原问询问整数系数的最佳已知稳定范围，没有提出应当证明的精确最优边界猜想。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Kupers–Miller–Patzt, Improved homological stability for certain general linear groups](https://arxiv.org/pdf/2106.12363)：v1，p.2 Theorem A / Theorem C；已刊 Proc. London Math. Soc.125 (2022),511–542，DOI10.1112/plms.12463。明确 GL、系数环、稳定范围和满射/同构之差；不能直接断言同样范围适用 SL。 访问层级：正文相关段落已读；验证层级：读定理假设与界；special linear 检索未获可用定理，不作无依据迁移。

**量词、范围和结论。**

- 题卡标题和任务类型：**题面有误**。所问是 best known homological stability range with integer coefficients，不是未知最小 n 的正式猜想。 
- 相关 GL_n 的可核稳定界：**部分进展**。KMP Theorem C：Euclidean domain 且 R/2 由单位生成；H_d(GL_{n−1};Z)→H_d(GL_n;Z) 在 d≤2(n−1)/3 满射、d≤2(n−1)/3−1 同构。 
- SL_n(Z) 整数系数的最佳已知范围：**暂未找到可验证结果**。本轮未取得精确适用的 SL_n 原始定理，故不补未经核定的 n 与 d 不等式。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `homological stability SL_n Z integral coefficients best range`
2. `Kupers Miller Patzt SLn integers slope 2/3 2106.12363`

GitHub/Lean 网页索引：`site:github.com SLn integers homological stability Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`SLn integers homological stability (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 标题改为 SL_n(Z) 整数同调稳定性的最佳已知范围；删除由标题推断存在未知上下界间隙的内容。
- 相关 GL_n 结果仅列背景，保持系数环和端点。

**仍需复核。**

- 需要继续读 van der Kallen/Charney 等 SL 稳定性原始定理及后续引文，才能报告精确最佳范围。
- 不把检索未找到等同无人知道；本题可能是已知结果的参考文献请求。

## QX-P-002156｜f509310fa8bebc17｜题面有误

**旧卡 → 本轮变化。** 输入状态为 `open`。题面对象须整体修正。基础论文有实质勘误：2026-10-28 corrigendum 新增 Hypothesis V 并删除错误的唯一多项式表示论证；arXiv v3 已反映条件，现 Theorem1.3 给有条件的自守计数式。一般 Selberg 类推广本轮未找到可核全解；不能只记“有勘误”却沿用旧无条件范围。

**直接证据与定位。**

- [Zeros of polynomials in derivatives of L-functions beyond automorphic case](https://mathoverflow.net/questions/506508/zeros-of-polynomials-in-derivatives-of-l-functions-beyond-automorphic-case?r=31)：题面定义 F 为多个 L 函数导数的多项式；询问 Selberg 类中的零点计数推广。核心是零点计数 N_F(T)=alpha1*T*log(T)+alpha2*T+O(log(T))，不是 L-prime 的临界带定位或避开临界线。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Dong–Wattanawanichkul–Zaharescu, Zeros of Polynomials in Derivatives of Automorphic L-functions](https://arxiv.org/html/2512.22451v3)：v3 2026-09-03；§1.1 Hypothesis V、(1.10)，§1.2 Theorem1.3。已包含向量唯一性和非消去条件；原稿版本不能代替 v3 的范围。 访问层级：正文相关段落已读；验证层级：已核 Hypothesis 与 Theorem1.3，不把搜索字面 Hypothesis V 无命中当缺少条件。
- [Corrigendum to Zeros of Polynomials in Derivatives of Automorphic L-functions](https://onlinelibrary.wiley.com/doi/10.1112/mtk.70136)：2026-10-28；修正段落(1)–(3)及定理编号对照。线性独立不能推出代数独立；向 Lemma3.3、Proposition4.1、旧 Theorems1.2/1.3 和 Corollary1.5 增加 Hypothesis V；修正 Lemma4.2。 访问层级：出版社勘误正文由搜索返回，直开 Wiley 重定向失败；验证层级：读取返回的三项完整修正文；旧1.2→v3 1.3，旧1.3→v3 1.6，旧Cor1.5→v3 1.8。

**量词、范围和结论。**

- 题卡误述的零点对象：**题面有误**。F 为有限个 L 函数及其导数的多项式；原问是零点个数的两项渐近，不是所有 L-prime 零点的位置。 
- 修订后的自守函数计数定理：**部分进展**。arXiv2512.22451v3 §1.1 Hypothesis V：J、J-prime 各自的指数向量一致，另须(1.10)非消去；Theorem1.3 的准确条件保留。 
- 推广到一般 Selberg 类：**暂未找到可验证结果**。不能假设所有 GL_m 自守 L 函数都已满足 Selberg 类的 Ramanujan 条件，也不能无条件推广修订定理。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `zeros polynomials derivatives Selberg L functions Dong Wattanawanichkul Zaharescu`
2. `2512.22451 corrigendum mtk.70136 Theorem 1.1 1.2 Selberg`

GitHub/Lean 网页索引：`site:github.com polynomial derivatives Selberg L functions zeros Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`polynomial derivatives Selberg L functions zeros (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 重写题名与人话版，恢复导数多项式和计数函数；删“零点都落临界带/躲开临界线”的错误概括。
- 把 v3 与正式勘误的新增假设写入基础结果，避免仅链接旧版本；REU 评论不作为已解决或时限证据。

**仍需复核。**

- Selberg 类推广仍需实际定理，不能由原帖猜测或引用数量作否定结论。
- 本轮完成版本条件对应但未独立审查全篇证明；正式勘误直链访问受限已明确记录。

## QX-P-002157｜b00158d587d41338｜题面有误

**旧卡 → 本轮变化。** 输入状态为 `open`。人话版把 not virtually residually solvable 弱化成没有有限指数可解子群，改变了问题。有限生成版本已有 Neumann 类型例子，有限表现版本本轮未找到全解。Rauzy 的嵌入障碍只说明某些有限生成 RF 群不能嵌入有限表现 RF 群，不能当普遍不可能或直接反例。

**直接证据与定位。**

- [A finitely presented residually finite group that is not virtually residually solvable?](https://mathoverflow.net/questions/491978/a-finitely-presented-residually-finite-group-that-is-not-virtually-residually-so?noredirect=1)：原题；2026-07-08 更新的 Neumann 构造；YCor 对 G_30 引用的更正。求有限表现且剩余有限的群，使任何有限指数子群都不是剩余可解；“剩余可解”不要求分离商有限。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Rauzy, Obstruction to a Higman embedding theorem for residually finite groups with solvable word problem](https://arxiv.org/abs/2002.02540)：v2 2021-03-17 摘要；J. Group Theory，DOI10.1515/jgth-2020-0030。存在有限生成 RF、字问题可解却不能嵌入任何有限表现 RF 群的例子；障碍是缺乏有效有限商分离。 访问层级：作者摘要已读，证明全文未审；验证层级：核对题面或所述结果范围；未独立重做文献证明。

**量词、范围和结论。**

- 现卡量词/性质：**题面有误**。对每个有限指数子群 H，存在非平凡元素不能被可解商分离；不等于 H 自身不可解。 
- 仅有限生成的版本：**部分进展**。原帖 2026 更新引用 Neumann1937，在交错群乘积中用二生成子群构造。 
- 有限表现且 RF 的所求例子：**暂未找到可验证结果**。f.p. 必须保留；不能只给 f.g. 例子或忘记虚性质的全称量词。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `finitely presented residually finite not virtually residually solvable`
2. `Minasyan Neumann group embedding finitely presented residually finite Rauzy 2002.02540`

GitHub/Lean 网页索引：`site:github.com finitely presented residually finite virtually residually solvable Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`finitely presented residually finite virtually residually solvable (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 将人话版改为没有有限指数剩余可解子群；把有限生成已知与有限表现待核分列。
- 更正 G_30 的单独引文不能充当原问例子；原帖后续改为 Z semidirect R(Z,30)/Theorem8。

**仍需复核。**

- Neumann 例子能否在满足性质的有限表现 RF 超群中实现需要专门构造；不能普遍调用 Higman 嵌入。
- 本轮没有取得满足全部条件的有限表现具体群。

## QX-P-002158｜c3df1c36a2ed7f71｜题面有误

**旧卡 → 本轮变化。** 输入状态为 `open`。恢复非可分范围。Brian 作者稿 §4 Theorem4.2 给 cof(M_{κ^omega})≤cof(NWD_{κ^omega})，Question4.1 询问等式，明确 κ=omega 已知而不可数情况仍待定于该稿。正确刊物是 Topology and its Applications379(2026),109516，旧注记 APAL2025 错误；最终刊稿 PDF 本轮403。

**直接证据与定位。**

- [Can the nowhere dense sets be more complicated than the meager sets?](https://mathoverflow.net/questions/458089/can-the-nowhere-dense-sets-be-more-complicated-than-the-meager-sets)：原问完全可度量、无孤立点 X；非可分 κ^omega 的特例；Polish 情形评论。询问 cof(NWD_X)>cof(M_X) 能否发生；允许非可分完全可度量空间。可分 Polish 情形的已知等式不能直接推广。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Will Brian, Cardinal invariants of a meager ideal](https://wrbrian.wordpress.com/wp-content/uploads/2023/11/uniformity.pdf)：§4 p.11 Question4.1、Theorem4.2。给不等式及 κ^omega 等式问题的准确范围，说明可数 κ 的已知情形。 访问层级：正文相关段落已读；验证层级：已读 §4 关键问题和定理；未重做全部证明。
- [Cardinal invariants of a meager ideal — publication record](https://www.sciencedirect.com/science/article/pii/S0166864125003141)：Topology and its Applications379(2026),109516。纠正期刊卷年和文章号。 访问层级：出版社索引；最终机构稿直链403；验证层级：核对题面或所述结果范围；未独立重做文献证明。

**量词、范围和结论。**

- Polish 特例：**部分进展**。无孤立点可分完全可度量空间的等式，原帖和 Brian 论文指向 Fremlin。 
- 一般非可分 κ^omega 的单向界：**部分进展**。Brian Theorem4.2：cof(M_{κ^omega})≤cof(NWD_{κ^omega})。 
- 存在严格不等式/其一致性：**暂未找到可验证结果**。κ=aleph1 是原问中特别关注的情形；作者稿 Question4.1 未作解决。 
- 现卡范围和书目：**题面有误**。不可把 X 自动限定为 Polish；原刊并非 APAL2025。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `nowhere dense meager ideals cofinality nonseparable completely metrizable Brian`
2. `2311.10209 cof ND cof M omega power aleph one discrete`

GitHub/Lean 网页索引：`site:github.com nowhere dense meager cofinality Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`nowhere dense meager cofinality (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 补 X 不要求可分及 cof 的两个理想；已知 Polish 情形与非可分问题分开。
- 纠正 APAL2025 为 Topology and its Applications379(2026),109516。

**仍需复核。**

- 最终机构稿 https://ninercommons.charlotte.edu/nanna/record/12840/files/briawil_carin_ir_2026.pdf?registerDownload=1&version=1&withMetadata=0&withWatermark=0 返回403；出版最终版与作者稿差异未核。
- 没有找到严格不等式的完整例子或一致性模型，不据此断言绝对不存在。

## QX-P-002159｜fa91d245505d6291｜题面有误

**旧卡 → 本轮变化。** 输入状态为 `open`。人话版“摆球”和 d=1 密度恒为1均错误。d=1 的有限状态方法保证存在最优周期包装，从而密度有理，未保证每个 S 都铺满。高维无理性本轮未找到可核结果；Greenfeld–Tao 的有周期背景输入版本不能直接证明此密度不可计算，原作者已撤回该推论。

**直接证据与定位。**

- [Can the optimal packing density in Z^d be irrational?](https://mathoverflow.net/questions/454946/can-the-optimal-packing-density-in-mathbbzd-be-irrational)：原题有限 S 与平移包装、lower asymptotic density；d=1 有限图方法；Greenfeld–Tao 讨论更新。S 是 Z^d 的有限子集，包装是互不相交的平移 A+S，求并集的最优下渐近密度；不是欧氏等球包装。 访问层级：正文相关段落已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Frankl–Kupavskii–Sagdeev, Solution to a conjecture of Schmidt and Tuller on one-dimensional packings and coverings](https://arxiv.org/abs/2203.03873)：2022 论文索引：一维三点集。解决一维特殊包装问题，不提供高维无理密度。 访问层级：仅作者摘要索引；验证层级：核对题面或所述结果范围；未独立重做文献证明。
- [Natalchenko–Sagdeev, Packing Density of Sets With Only Two Nonmixed Gaps](https://arxiv.org/abs/2407.01101)：v2 2025-06-06；J. Graph Theory110(2025),263–271。一维两类连续差的有限集包装；摘要给下界及特例最优性，不能当高维无理密度例子。 访问层级：作者摘要及版本、期刊元数据已读；验证层级：核对题面或所述结果范围；未独立重做文献证明。

**量词、范围和结论。**

- 现卡几何对象/一维值：**题面有误**。任意有限 S⊂Z^d 的互不交平移，并集密度；一维有理不等于总为1。 
- d=1 有理性：**部分进展**。原帖有限有向图/周期包装论证，周期可界为 2^{diam(S)}；允许任意有限 S。 
- d≥2 是否存在无理最优密度：**暂未找到可验证结果**。需一个有限格点集及其最优密度证明；非周期铺砌可能仍密度1。 

**实际检索路径。** 原帖已打开；学术使用 system1 的两组实际检索词：

1. `irrational optimal packing density finite subset integer lattice`
2. `Sagdeev finite tile Z^d optimal packing density rational computable 2407.01101`

GitHub/Lean 网页索引：`site:github.com integer lattice tile irrational packing density Lean mathlib formal conjectures`。公开 AI/社区联合网页索引：`integer lattice tile irrational packing density (aiXiv OR Zenodo OR EulerSolve OR ProofForum)`。本题全库标题索引已查；参数、日期、直接返回链接和访问限制见逐题 JSONL 的 queries，关键后续原文操作另列。

**卡片建议。**

- 删除摆球叙述，给 finite S、A+S、lower asymptotic density 的定义；把“d=1 有理即1”改为有理。
- 保留 Greenfeld–Tao 推论不成立的原作者更正；不添加“超越数”新目标。

**仍需复核。**

- 高维无理例子本轮未定位；相关不可判定性论文的输入包含周期背景集，不可擅自固定为整个 Z^d。
- GitHub 命中 OpenAI docs/155 的非周期 Z^3 平铺，密度1为有理数，未审其代码且不解决本问。

## 指定对子复核与新线索

12 个指派对子均按双方包内当前版本正文复核；没有建议合并的对子。11 对为对象或目标不同的“相关但不等价”，2139↔41 为“同源不同问”。“相关但不等价”是包内允许的关系枚举，包含仅关键词相近、实质不相关的候选。

| 双方题号及版本 | 关系 | 本轮理由 |
|---|---|---|
| QX-P-002136@8bb1315ed144f7b7 ↔ QX-P-002244@00deda911026386c | 相关但不等价 | 2136 是独立均匀圆周点的随机中点过程，问稳态径向密度；2244 是确定性的圆上蚱蜢跳跃及 OEIS A329230–A329233 数列。样本空间、运动规则和待求量不同；圆关键词不足以合并。 |
| QX-P-002138@4e4aed1935f0ea28 ↔ QX-P-002423@b745d1e8b093b2e3 | 相关但不等价 | 2138 是二次多项式倒数和的有理性，cotangent 指三角函数；2423 核验 cotangent bundle 中附近拉格朗日猜想的高维反例。对象完全不同，是 cotangent 关键词/正文互引误配。 |
| QX-P-002139@80b39c747eee0e48 ↔ QX-P-000041@4e298d20a8406ce9 | 同源不同问 | 2139 问非 Wolstenholme 素数是否无限，涉及模 p^4 的加强性质；41 问合数 n 是否能满足 Wolstenholme 模 n^3 的逆命题。量化对象、模数和目标不同。 |
| QX-P-002141@fd14b036e65b5cbf ↔ QX-P-002423@b745d1e8b093b2e3 | 相关但不等价 | 2141 问交换环 A 的球谱基变换提升 HA≃S_A⊗_S HZ；2423 问辛几何中的附近拉格朗日反例核验。稳定同伦背景或互引不能给两命题等价。 |
| QX-P-002142@703140363ec50ab0 ↔ QX-P-000371@986442c2458f9b82 | 相关但不等价 | 2142 问拓扑 S^4 的 Lipschitz 结构唯一性；371 问 l1 的闭子空间、L1 商与 Lipschitz 补性。流形结构与 Banach 商空间性质不同。 |
| QX-P-002142@703140363ec50ab0 ↔ QX-P-000411@f0d4a56add52572b | 相关但不等价 | 2142 的对象是四球面的 Lipschitz 流形结构；411 是整数 Lipschitz 函数的图是否能避免三项等差。相同 Lipschitz 词不使对象或结论相同。 |
| QX-P-002142@703140363ec50ab0 ↔ QX-P-002180@87d56552cf1abddc | 相关但不等价 | 2142 问 S^4 结构唯一；2180 的原题是 X×R 双 Lipschitz 嵌入 R^n 能否推出 X 嵌入 R^{n−1} 的消去问题。已读其正文及对宽泛 X/Y 草稿的备注，仍不是 S^4 特例的等价命题。 |
| QX-P-002143@b4c93142c191f456 ↔ QX-P-000448@4b01cecc4de09f7e | 相关但不等价 | 2143 问复半单 Hopf 代数能否赋予兼容的正 C* involution；448 问任意有限维 Hopf 代数的 Ext 上同调有限生成。假设与目标均不同。 |
| QX-P-002146@fab839b1925f2409 ↔ QX-P-000590@e57d532ff6c238cb | 相关但不等价 | 2146 问八字结 Dehn 填充非中心 SU2 表示的 H1 无穷小刚性；590 问不同手术斜率能否得到定向保持同胚的三流形。即使同用 Dehn 手术也不能合并。 |
| QX-P-002147@749390830da8e305 ↔ QX-P-000502@cdaba90d88423560 | 相关但不等价 | 2147 是描述复杂性方法与布尔自然证明屏障的适用问题；502 是算术电路中的 VP≠VNP 猜想。不是相同 P/NP 主命题，也非相同量词。 |
| QX-P-002153@c3db20a7d8061003 ↔ QX-P-002277@c71b4fa4ee67c5d5 | 相关但不等价 | 2153 问 dim≥5、截面曲率[−1,1]约束下直径局部极小的具体度量；2277 是 S^2 的最短闭测地线平方与面积的 Calabi–Croke 最优常数。维数、几何泛函和任务均不同。 |
| QX-P-002154@d81b10eba4e703c8 ↔ QX-P-002354@2f5c268dd1be0e4f | 相关但不等价 | 2154 问双侧 Noetherian 环左右单模同构类等势/双射；2354 问 Jacobson 根各次幂的交是否为0。虽共享环类别，结论和检验对象不同。 |

新增索引候选均未取得另一方当前全文，因此保留“待定”，不作同题、特例或合并结论：

- QX-P-002138@4e4aed1935f0ea28 ↔ [QX-P-001736](https://www.qunxingmath.org/p/QX-P-001736/)@babba2a41bd5d2da：索引题名为一般 ∑1/(an²+bn+c) 有理性逆判据；2138 在参数/起始下标调整后似是 A=1、B=2a 的限制特例。已独立读相关 MO498167，但未取得1736当前题卡全文，因此只列待定，不凭索引判特例/强化。
- QX-P-002144@b8119b18201c1692 ↔ [QX-P-000231](https://www.qunxingmath.org/p/QX-P-000231/)@07de824d2e2cf9a9：索引为 Jacobsthal 型 Y(x) / Erdős687，可能是原帖 Jacobsthal 提示的相关文献方向；原卡全文不在本次已读配对中，不能报重复。
- QX-P-002151@bdbbe7ee3e44ce36 ↔ [QX-P-002477](https://www.qunxingmath.org/p/QX-P-002477/)@45caaca857ed42f7：索引为核验2026 Thompson F 非可均性公开声明；2151 是给出显式悖论分解。可能是一题一验/背景与构造分工，2477全文未取得，关系待定。
- QX-P-002151@bdbbe7ee3e44ce36 ↔ [QX-P-002051](https://www.qunxingmath.org/p/QX-P-002051/)@5a09d3d2ff10a284：索引为 Thompson F 可均性的逆向数学强度；与显式分解共享背景但目标不同。只查索引，未读2051正文，不作合并。


---

# QX-NEW-07 d 组：影响状态、题面与查重的发现

核查日期：2026-11-26。范围：QX-P-002160–002186 中分配的 25 题（有跳号），以及 owner 指派的 11 组对子。

25 题均执行原出处核题、两组学术查询、GitHub/Lean 索引查询、公开 AI/社区组合域索引及库内检索。100 条逐题搜索词和真实调用日志索引均在 results.jsonl。这不是逐题深查或独立证明审计；AI 站点组合域检索不等于分别访问各站全文。未运行外部仓库代码、未写线上、未发帖。“原题已证”仅用于已经关闭的原始子问；已知背景单列，受限子类定理标为部分进展。

## 优先改状态或人工复核

### QX-P-002182：两个存在性子问已有更早的肯定答案

版本 49d622b3d4e05824。原出处是 [工作坊 Problem15(a)–(c) 与 Theorem14](https://arxiv.org/html/2507.03972v1)。

- **(a) 肯定。** [Rauzy，Computability of finite quotients of finitely generated groups](https://doi.org/10.1515/jgth-2020-0029)，J. Group Theory 25 (2022), 217–246，Definition1 / §1.1 / Theorem3，构造有限生成、残余有限、有 computable finite quotients（CFQ）、字问题不可解的群。
- **(b) 肯定。** [Rauzy，Obstruction to a Higman embedding theorem for residually finite groups with solvable word problem](https://www.degruyterbrill.com/document/doi/10.1515/jgth-2020-0030/html)，J. Group Theory 24 (2021), 445–452，Theorem2，直接给有限生成、残余有限、字问题可判定但非有效残余有限的群。可判定字问题当然属于 Π⁰₁。
- **(c) 尚未取得可验证结果。** Morozov 型“不嵌入递归置换群 S_rec”的额外要求没有被上述两个例子解决。

**定义桥接是本次推论，不能冒充原论文措辞。** CFQ 判定给定有限群及生成元像是否延拓为真实群同态。因此可有效枚举所有真实有限同态；RF 保证每个非平凡字被其中某个同态分离。搜索分离证据给 e.r.f.，同一搜索只在非平凡字上停机给 WP 补集 c.e.，从而 WP 为 Π⁰₁。这是 **CFQ＋RF 分别推出 e.r.f. 和 Π⁰₁**，没有无条件声称 e.r.f. 自身就推出 Π⁰₁。最后调用 workshop Theorem14，得到该群在某可计算 profinite 群中由有限条可计算路径生成的子群实现。

该嵌入不要求字问题可判定，也不把 co-r.e. 字问题称为可计算离散群呈示。可将有效列出的有限群取全直积、生成元取各有限同态给出的坐标路径；RF 给单射。这里不要求子群闭包可计算，亦不引入额外逆极限兼容条件。

两篇已刊原文的定义和关键定理已读取，群构造未独立逐行重证。第二篇 PDF 请求失败，但出版商 HTML 可读；不能写成 PDF 已核。旧卡的嵌入方向也需修正，详见逐题结果。

### QX-P-002181：三个分离公理存在性问均有 1976 年构造

版本 886a9866f063943e。[原 MO 主问](https://mathoverflow.net/questions/507958/connected-spaces-with-no-nontrivial-open-connected-subsets)问 T₁、T₂、regular T₁ 的非平凡 Γ 空间是否存在。[Brouwer 原始报告 ZW83/76](https://ir.cwi.nl/pub/6862/6862D.pdf) §2，印刷 pp.2–5，尤 p.4 性质(vii)，给非可分可度量弧连通例子，覆盖这三个存在性问。§1 命题/推论排除的是**可分可度量**非退化例子，不能推成所有 regular T₁ 不存在。

旧卡追加的“完整刻画”不是原问，不能因存在性已解就称分类完成。读到了度量定义和(vii)的证明；扫描公式部分 OCR 不清，如需最高验真级别应人工审度量估计。库内另有 QX-P-002192（c40bc86729042511）同题候选，本组只见索引，尚未正文双读，保持“待定”。

### QX-P-002178：出处之间出现蕴含与基底冲突

版本 c0df360e5d34a90f。[工作坊 Problem12](https://arxiv.org/html/2507.03972v1) 将指定 WPHP→FRT²₂ 蕴含列作问题；[Wang 当前 v2](https://arxiv.org/html/2506.17943v2) §7 却把更弱 IΣ_n 基底下 WPHP(Σ_{n+1})→FRTᵉ_k(Σ_{n+1}) 列为已知。原集第一问显示 IΣ_{n+1}，也需核下标。没有定位出支撑该箭头的独立证明，因此记“公开完整结论声明待核”，优先复核，不能直接升整卡已解。第二问 FRT²₂→FRT³₂ 仍未获得可验证结论。Cholak 的无限 Ramsey/bounding 论文不是有限可定义着色原题的替代答案。

### QX-P-002168、002170：公开 AI 声明与范围必须保留

QX-P-002168（bf6f9b9f8fb40525）[MO 当前正文](https://mathoverflow.net/questions/456035/for-which-set-a-alice-has-a-winning-strategy)有明确归因 Claude Opus 5 的策略/计数主张，作者承诺后补详证。状态是“完整声明待核”，未接受其正确性。历史卡中关于旧 Claude 失误的备注不能替代对当前声明的验证；还需按原“先清空集合为胜”的规则审算法。

QX-P-002170（145b00230ac44ec4）[2026-10-29 新稿 2610.39172](https://arxiv.org/abs/2610.39172)给下 K-cone 的部分结果；[可读镜像](https://arxiv.cnoctave.top/pdf/2610.39172) pp.2–3 明示整个下锥仍未解决，pp.24–25 披露 AI 参与。已读关键命题及披露，未独立审完构造。原站全文访问失败、镜像可读，不能写成原站全文已核，也不能把限制的 c-solutions/K-degree 结论当整个下锥反例。

### QX-P-002185、002186：2026 年子类结果，不是全类解决

[2410.02248 当前 v3 全文](https://arxiv.org/html/2410.02248v3)，Theorem1.2、Theorem4.7、Lemma5.4/5.13 及 Corollary5.16，证明某些 Borel 子类的同构关系光滑且 Out(G) 为 profinite，包括无代数性及 essential 子群满足相应有限共轭类条件的类。全类光滑性和全类 Out 紧性仍被文中保留。

对 2186，还应按 §2.3 写 Aut(G) 在开子群陪集上的点态作用拓扑及商拓扑，不能未经证明用一般“紧开拓扑”替代。[Nies–Schlicht 2026 年已刊论文页面](https://www.impan.pl/en/publishing-house/journals-and-series/fundamenta-mathematicae/online/116469/automorphism-groups-of-non-archimedean-groups)本次只核到摘要，给 locally compact，不足以回答 compact。

## 逐项变化、范围与检索路径

表中的链接指向本次核过的证据，访问层级见逐题 JSON。共同的五类路线均已执行；路径栏仅写导致重要发现的检索链，不重复索引零命中。

| 题号 / 版本 | 类型 | 旧卡 → 本次变化 | 链接与定位 | 量词/范围 | 实际关键路径 | 待复核点 |
|---|---|---|---|---|---|---|
| QX-P-002160 / af45a9c9e72f148d | 部分进展 | 旧：Freiling 追加对称公理命运（联合相容性） → 联合相容性仍未取得可验证完整结论；原帖评论仅给连续统等于 aleph_2 时的冲突线索，不能外推任意连续统。 | [来源](https://mathoverflow.net/questions/441396/freilings-question)：主问；Jeon 2023-03-04 评论；[来源](https://doi.org/10.2307/2273955)：JSL 51, 190–200；原帖指 p.194 | 任意适当模型中的联合相容性；不固定 c=aleph_2。；Jeon 社区评论称此附加条件下不能联合成立；没有阅读全文证明，保持声明级。 | 定位 Freiling 1986 原论文书目及原帖讨论；没有把一般对称公理、CH 的单条结论当成两公理联合相容性解答。 日志：logs/card_2160_search.json；原题：logs/003_sources_and_academic.json。 | 取得 Freiling p.194 原始表述并追 Jeon 评论所需基数不变量论证；不能把评论的基数特例作为一般不相容。 |
| QX-P-002161 / 7fc6ae13ef6ef6ed | 题面有误 | 旧：同特征标表异 Brauer 表的群对（⚠️AI 摘要污染风险） → 原题同普通特征标表是否决定 p-Brauer 表未找到可验证答案；题卡把不可约模特征标与投射不可分解特征标混同，应纠正。 | [来源](https://mathoverflow.net/questions/372758/non-isomorphic-groups-with-same-character-tables-and-different-brauer-character)：主问；Robinson 评论；[来源](https://gap-system.github.io/gap/doc/ref/chap71_mj.html)：Brauer character table 相关段落 | 固定 p 及 sufficiently large modular system；表的等价需含适当行列匹配。 | 核对 p-modular system 的原问题与 GAP Brauer 表定义；global representation ring/Knutson index 命中讨论普通表、幂映射/marks，不给本题反例。 日志：logs/card_2161_search.json；原题：logs/card_2161_search.json。 | 若使用相关表计算仓库，需先取得明确群对、素数与不可约 Brauer 表，再锁定提交验证；当前未有这样的对应代码。 |
| QX-P-002162 / 58d8af178fa04aa1 | 题面有误 | 旧：上同调环决定紧对称空间？（2 处摘要幻觉拦截） → 原帖问紧连通对称流形的整数上同调环是否决定微分同胚型；题卡扩成有理系数/同伦型，已失去原题范围。 | [来源](https://mathoverflow.net/questions/363037/does-cohomology-ring-determine-a-compact-symmetric-space)：主问 integral cohomology ring / compact connected / diffeomorphic；评论；[来源](https://doi.org/10.4310/jdg/1214428818)：JDG 3 (1969), 59–68；MO 指引言 corollary | 两个紧连通对称流形，H*(M;Z) 与 H*(N;Z) 分次环同构是否推出微分同胚。 | Wolf 的 real cohomology sphere 论文与积分球推论被定位；有理系数 Wu 流形例不能否定原问。 日志：logs/card_2162_search.json；原题：logs/008_key_sources.json。 | 获取 Wolf 1969 引言推论的可读全文；进一步查一般整数环分类，当前不据无检索结果确认开放。 |
| QX-P-002163 / 46fdfffa9eb62733 | 题面有误 | 旧：Hilbert 方体自同胚群的自动连续性（题面校准） → Hilbert 方体 Homeo(Q) 的自动连续性未取得完整解；Elliott 等 Theorem 6.5 是条件传递及 C(Q) 唯一 Polish 半群拓扑，不能当 Homeo(Q) 已解决。 | [来源](https://mathoverflow.net/questions/348345/does-the-group-of-homeomorphisms-of-the-hilbert-cube-have-automatic-continuity)：主问，compact-open topology；所有到 second-countable topological groups 的同态；[来源](https://academics.uccs.edu/zmesyan/papers/AutomaticContinuity.pdf)：Theorem 6.5，PDF pp.36–37；[来源](https://arxiv.org/abs/1912.07029)：v6, 2023-08-15；Trans. AMS 376 (2023), 8023–8093 | Q=[0,1]^N；源群 compact-open；目标任意 second-countable topological group。 | arXiv:1912.07029 最新 v6 与作者全文 Thm6.5(iii) 已核，前提明确仍假设 H(Q) 自动连续。 日志：logs/card_2163_search.json；原题：logs/003_sources_and_academic.json。 | 继续查 H(Q) 本身的 Steinhaus/自动连续性证明或反例；本次没有独立验证代码。 |
| QX-P-002166 / 239c1cfe9e5e7312 | 仅补出处（已知背景）；问题范围校准 | 旧：EGZ 定理相关加性组合新命题（S1⟺S2+二维 analogue） → S1⇔S2 本身在原帖已由 EGZ 导出，实际未决请求是直接组合证明以及二维类比；不能整体登记为新的等价命题开放。 | [来源](https://mathoverflow.net/questions/383872/around-the-erd%C5%91s-ginzburg-ziv-theorem)：主文 Statements 1/2 后问题；Petrov、Thomas Bloom 评论 | k_i 为正整数、K=Σk_i；S1为0..K全可由子集和实现；S2为任意K整数按各k_i大小分块且块和被k_i整除。；这是原帖实际研究请求；不能由已有等价性回答方法要求。；原帖仅问是否存在合适二维类比，并未固定唯一二维命题，需先定义可验收陈述。 | 查询 EGZ equivalence/subset sums/partitions 两条路径；未获得不隐含 EGZ 证明的新直接解法或具体二维完整结论。 日志：logs/card_2166_search.json；原题：logs/005_sources_2164_2167_open.json。 | 明确“直接”允许的工具，以及二维 analogue 的对象与分块约束；本次未找到相应完整方案。 |
| QX-P-002167 / b18bd1ead5eed57d | 题面有误 | 旧：四维 Gram 矩阵双根恒等式 → 原题为明确参数 Gram 矩阵与多项式重根关系；卡片漏公式并把因 t^4 项抵消后至多三次的差式叫作四次多项式。Murakami–Ushijima 的相邻公式提供出处线索。 | [来源](https://mathoverflow.net/questions/326021/more-mysterious-properties-of-gram-matrix)：主文矩阵 G、P(t) 两四因子乘积之差；[来源](https://arxiv.org/pdf/math/0402087)：§2 z±/Gram 公式；§4 Proposition4.1，PDF p.7 | 须保留六个非零参数、矩阵配置、P(t) 与可能的退化次数；相关体积公式不自动等于全参数版本证明。 | 取得 math/0402087v1 原稿，Prop4.1 给对应倒变量的 z(q2 z²+q1 z+q0) 分解；尚未完成所有参数退化情形的恒等式对应审计。 日志：logs/card_2167_search.json；原题：logs/005_sources_2164_2167_open.json。 | 核 Δ(q)=常数×det(G) 的精确系数、t=0 与 q2=0 等退化情形；原帖 Maple 声明不算独立验证。 |
| QX-P-002168 / bf6f9b9f8fb40525 | 公开声明待核；题面有误 | 旧：数集合博弈 Alice 必胜判据（MSE 交叉帖 1 非完整回答） → 当前 MO 出现明确归因 Claude Opus 5 的策略与渐近计数声明，作者尚承诺将来补详证，应列公开声明待核；不能引用旧备注就认定已被驳倒。 | [来源](https://mathoverflow.net/questions/456035/for-which-set-a-alice-has-a-winning-strategy)：游戏规则；According to Claude Opus 5；作者将来补详细证明的段落；[来源](https://math.stackexchange.com/questions/4775193/for-which-set-a-alice-has-a-winning-strategy)：Tony Mathew answer；n=6 反例讨论 | MO 当前给完整策略/渐近主张但缺详证；限原先清空集合胜规则，不改为不能出牌即输。 | 用 ascending card/set game 与先清空集合的规则检索；原帖/MSE 未取得完整分类证明。 日志：logs/card_2168_search.json；原题：logs/006_remaining_sources.json。 | 获取声明的完整证明/算法；按原规则验证四条策略和计数，尤其过牌及空集边界；旧 Myerson 评论尚需展开评论逐条核对。 |
| QX-P-002169 / d807a40adc752ec7 | 题面有误 | 旧：Hausdorff 测度规范函数值域 I 的四问 → 原 I 是集合 A 对应的“正测度规范函数集合”，不是 h↦H^h(A) 的数值值域；四个子问需分别恢复。新 gauge/strong-dimension 论文不等于任意集合的一般结论。 | [来源](https://arxiv.org/html/2507.03972v1)：Problem 1(1)–(4)；[来源](https://math.berkeley.edu/~slaman/papers/sdim.pdf)：摘要与 strong dimension 设定；作者稿日期 2024-01-13；[来源](https://arxiv.org/abs/2601.20414)：v4, 2026-10-04；摘要 | 是否与 P(R) 等势；保留原文的 GCH 条件线索，不当 ZFC 证明。；Σ⁰₂ 公式中可表示某 I(C) 的公式集合是否 Σ¹₂-complete；源文仅给 Π¹₁-hard 背景。；问其独立性；不能用通常 Borel hierarchy 严格性直接回答。；∀gauge f ∀A，H^f(A)>0 ⇒ ∃B⊆A 0<H^f(B)<∞，是否与 ZFC 相容。 | 名称/gauge ideal range 及公式两组检索；实读 Slaman strong dimension 稿、Goto arXiv2601.20414 v4 摘要和版本；后者特殊 Hausdorff measure 构造未核为原实数子集问题的直接反例。 日志：logs/card_2169_search.json；原题：logs/001_sources.json。 | 对第四问需要严格确认实数空间、任意子集及规范函数的同一性；Goto 论文只读摘要，不能判原题已反驳。 |
| QX-P-002170 / 145b00230ac44ec4 | 部分进展；题面有误 | 旧：K-复杂度 liminf 刻画可数上锥 → 新论文 2610.39172 给下 K-cone 的部分进展且明确全文仍未解决整个下锥；披露 AI 参与。上锥等价式未获新的可验证结论。 | [来源](https://arxiv.org/html/2507.03972v1)：Problem 2(1),(2)；[来源](https://arxiv.org/abs/2610.39172)：2026-10-29；原站 search1 摘要；[来源](https://arxiv.cnoctave.top/pdf/2610.39172)：pp.2–3，Question1.1、Propositions1.2–1.4；pp.24–25 Acknowledgement；[来源](https://arxiv.cnoctave.top/pdf/2610.39172)：PDF pp.24–25，Use of AI | L_x countable iff liminf_n(K(x↾n)-K(n))<∞；新稿局部 c-solutions/K-degree 结论不构成整个 L_x 的反例。；U_x countable iff liminf_n(K(n)+n-K(x↾n))<∞；新稿研究下锥，不能迁移为上锥解决。 | 两组 K-cones/cardinality/liminf 查询命中新预印本；system1 核原站摘要，原站全文 DisabledError，实读 26 页镜像中的 Prop1.2–1.4、Thm1.5 与未解说明。 日志：logs/card_2170_search.json；原题：logs/001_sources.json。 | 获取原站/作者托管全文以交叉镜像；审计 Prop1.2 的 c 解定义与全锥差别；上锥方向另查。 |
| QX-P-002172 / 1dd550788efaf33e | 题面有误 | 旧：Even Number Game k≥4 必胜策略 → 恢复 Even Number Game 的实际规则；旧人话版关于偶数数量奇偶的猜测错误。2026 工作坊 2608.26628 并不含本题，二手 AI 索引混合来源。 | [来源](https://arxiv.org/html/2507.03972v1)：Problem 4；规则定义段；[来源](https://barmpalias.net/oldweb/news_items/sing23.html)：2023 extended abstract, Even number game；[来源](https://arxiv.org/html/2608.26628v2)：§1；全文 find Even 未命中；摘要 11 位署名作者；[来源](https://www.emergentmind.com/papers/2608.26628)：Related/open problem 列表 | 不重复是每位玩家分别对自己的历史；胜负与偶数数量奇偶无关。 | 英文名及 k≥4 特征检索定位作者 2023 讲稿与 2304.03030；2026 问题集 v2 实读并查 Even，无本题。 日志：logs/card_2172_search.json；原题：logs/001_sources.json。 | 取得 2304.03030 最新完整版本并核 k=2,3 原证明；本次未找到 k≥4 全解。 |
| QX-P-002173 / b18b10bdaa3f7547 | 题面有误 | 旧：WF/UB 分离的纯描述集合论重证 → UB 是有唯一无限分支的树；原题求 Goh 的“每个 coanalytic separator 均 complete”结论的描述集合论证明，并非移除决定性公理。 | [来源](https://arxiv.org/html/2507.03972v1)：Problem 5 及其前文；[来源](https://www.impan.pl/shop/publication/transaction/download/product/89210)：Fund. Math.194(2007),267–281；§5，p.279 的 (WF,WF*) 连续归约构造；§1 定义 | 任意 coanalytic 集 C 分离 WF 与 UB，则 C coanalytic-complete；所求是该结论的另一方法证明。 | 两组 WF/unique branch/separator 检索；取得 Saint Raymond 2007 已刊全文，核其 (WF,WF*) complete pair 构造。 日志：logs/card_2173_search.json；原题：logs/001_sources.json。 | 定位 Goh 递归论原始证明的可读稿；本次主要新核对 Saint Raymond 的旧文献，未得所求替代证明。 |
| QX-P-002174 / ac2c9ffe2bbc4590 | 部分进展；题面有误 | 旧：Ωˣ ≥_T 0″ 存在性（2005 著名未决） → Ω^X≡_T X′ 的“标准事实”写错；正确常用相对化公式须加入 X。原问题不因取 X≥0′ 而平凡；Yu–Zhao 结果还带 join 0′。 | [来源](https://arxiv.org/html/2507.03972v1)：Problem6；Proposition7；[来源](https://math.uchicago.edu/~drh/Papers/Papers/omega.pdf)：Proposition3.3，PDF p.7；§5 Question1，PDF p.10；[来源](https://math.uchicago.edu/~drh/Papers/omega.html)：J. Math. Logic5(2005),167–192；abstract | 固定原出处的 Ω 定义与 oracle machine；不能未经证明把 complexity-sum 版本和所有 machine-specific halting Ω 自动等同。；∀y∃x，Ω^x⊕0′≥T y；不能删去额外 oracle 0′。 | 实际检索并取得 Downey–Hirschfeldt–Miller–Nies 作者 preprint；Proposition3.3 精确写 Ω_U^A⊕A≡_T A′。 日志：logs/card_2174_search.json；原题：logs/001_sources.json。 | 精确核对 2025 complexity-sum 定义与 2005 halting-probability 原问题的版本关系；取得 Yu–Zhao 证明全文。 |
| QX-P-002175 / fa0e3df67d14f10a | 题面有误 | 旧：Veličković–Woodin 定理的递归论证明 → 原定理关乎 analytic 集的 hyperdegree 共尾性与四个实数的 join；卡片所谓 Borel 等价关系为错误背景；须保留 (a) 替代证明和 (b) 加强假设两问。 | [来源](https://arxiv.org/html/2507.03972v1)：Theorem8；Problem9(a),(b)；[来源](https://arxiv.org/pdf/math/9501203)：§2，Lemma1 及其证明；pp.6–8 | 原 Theorem8 的四元组 join 结论，求指定方法的新证明，而非定理本身真假。；A∈Σ¹₁(y) 且某x∈A满足ω1^{CK(x)}>ω1^{CK(y)}，是否推出同一四元组结论。 | 作者/名称及 analytic/hyperdegrees/four 两组检索；取得 Velickovic–Woodin math/9501203 原预印本 §2 的 hyperarithmetic 四元组结果。 日志：logs/card_2175_search.json；原题：logs/001_sources.json。 | 原预印本与1998已刊版本 Lemma 编号仍需最终出版核对；本次没有取得新替代证明。 |
| QX-P-002176 / e4b3c7cc4598109a | 部分进展；题面有误 | 旧：RCA₀ 证 P⁻→P（正树三原理缺口） → positive 指二叉树路径集具有正 Lebesgue 测度；新 Wang 2610.25769 处理完美子树跳跃，不直接给 RCA0 中 P−→P 的证明。 | [来源](https://arxiv.org/html/2507.03972v1)：§5 定义；Problem10；[来源](https://arxiv.org/abs/2610.25769)：2026-10-19，v1 官方索引摘要；[来源](https://borowiecki.dev/pdf/2610.25769)：Thm3.1；Cor3.12；§4 Question4.1，PDF p.14 | P− 是同一正二叉树中可数个不同路径的序列；P 要完美子树，不能把经典集合论完美核结论移入 RCA0。；新稿给复杂度受限正树的 jump/low 完美子树结果；未核为原二阶算术蕴含证明。 | 正树/perfect subtree 与 P− 特征两组检索；原站索引核 2610.25769、原站正文不可达，实读镜像 Thm3.1/Cor3.12/§4。 日志：logs/card_2176_search.json；原题：logs/001_sources.json。 | 需要明确在 RCA0 内给出蕴含，或构造 RCA0+P−+¬P 模型；新论文未提供这一直接结论。 |
| QX-P-002177 / 393d712b851e12d0 | 题面有误 | 旧：正树原理的 Hausdorff 维度版 → 原文只是将前述测度原理改为维数的研究提问；卡片关于自相似集合/维数公式的叙述不是原题，不能据此判一个未定义定理的真假。 | [来源](https://arxiv.org/html/2507.03972v1)：Problem11 及 Problem10 前的定义 | 需先固定使用何种维数、阈值、完美子树是否保同维数及形式化；原文为研究方向，未形成唯一可判真假句。 | Hausdorff dimension/perfect subtree 与 positive tree principles dimension 两组检索，没有取得对应明确版本的解；generic fractal/IFS 结果不适用。 日志：logs/card_2177_search.json；原题：logs/001_sources.json。 | 先冻结可验收的维数版本；不能把通常 Hausdorff 空间公理、IFS维数或profinite谱当本题解。 |
| QX-P-002178 / c0df360e5d34a90f | 公开声明待核；题面/出处冲突 | 旧：WPHP 与有限 Ramsey 定理强度关系 → 第一子问与 Wang 最新稿 §7“已知蕴含”列表冲突，且基底下标不同，需优先核原题与证明定位；第二子问的 FRT²₂→FRT³₂ 尚未取得可验证结论。 | [来源](https://arxiv.org/html/2507.03972v1)：Problem12；[来源](https://arxiv.org/html/2506.17943v2)：v2 2026-10-20；§7 已知蕴含显示式；§5 Thm5.1、Cor5.4；[来源](https://arxiv.org/html/2603.23704v3)：v3；摘要、Theorems3–7/§6 | 最新作者稿把更弱 IΣ_n 基底的蕴含列为已知，但工作坊写 IΣ_{n+1} 且列问题；需要核对文本错误/定理出处。；有限域、Σ_{n+1} 可定义着色；保留 e=2 到3、k=2、逻辑基底。 | 两组名称/公式检索，全文核 Wang2506.17943v2（2026-10-20）与 Cholak2603.23704v3（2026-07-12）；Wang§7列已知WPHP→FRT，未找到对应独立定理定位。 日志：logs/card_2178_search.json；原题：logs/001_sources.json。 | 逐项审计2506.17943§7箭头是否笔误，追溯该箭头证明与标准/非标准参数；不能仅凭结论表升整卡 solved。 |
| QX-P-002179 / 90a144c1fb47c376 | 题面有误 | 旧：2-RAN 与 GPHP(Σ₂) 关系 → 2-RAN 是“对每个 X 存在相对 X 的2-random Y”的二阶原则，其一阶后果与 GPHP 的关系；不是两次随机数生成。Wang 最新稿仍明确提出所问方向。 | [来源](https://arxiv.org/html/2507.03972v1)：Problem13；[来源](https://arxiv.org/html/2506.17943v2)：§7 首段；Corollary5.4；[来源](https://www.emergentmind.com/open-problems/gphp-versus-two-randomness)：References 标成2608.26628 / 2025 Section5 | 针对相对算法随机存在原则的一阶后果；最新稿明确仍提问该方向。 | 2-RAN/GPHP 名称与 generalized pigeonhole/randomness 两组查询；Wang v2§7给定义与精确未决方向，Cor5.4给GPHP与相邻原则分离。 日志：logs/card_2179_search.json；原题：logs/001_sources.json。 | 进一步寻找RCA0模型构造或保守性定理；反向关系需明确一阶理论比较方式，而非把二阶句与一阶句无基底直接等同。 |
| QX-P-002180 / 87d56552cf1abddc | 题面有误 | 旧：双 Lipschitz 嵌入消去 R？ → 原问是有限维欧氏嵌入的降一维消去；当前通俗题面把目标改成任意 Y×R。原帖唯一可见回答的切片法仅给 X→Rⁿ，未回答 X→Rⁿ⁻¹；本次未找到精确解答。 | [来源](https://math.stackexchange.com/questions/157576/can-one-cancel-mathbb-r-in-a-bi-lipschitz-embedding)：主问；回答的 f(x,0) 及随后的评论；[来源](https://github.com/openai/math/blob/main/lean/docs/324.md)：搜索摘要；未锁定提交 | ∀度量空间 X、适当整数 n，X×R↪_biLip Rⁿ ⇒ X↪_biLip Rⁿ⁻¹。 | 两组检索围绕 bi-Lipschitz cancellation / X×R embeds R^n；没有把 Banach 空间 Lipschitz 等价或一般倍增嵌入结果当成本题证明。 日志：logs/card_2180_search.json；原题：logs/009_source_details.json。 | 继续查有限维目标消去的原始证明或反例；GitHub 命中未做代码级复核，不能填 verified。 |
| QX-P-002181 / 886a9866f063943e | 原题已解；题面有误 | 旧：无非平凡开连通子集的连通空间（Γ-空间，双向结果） → 原帖的 T₁、T₂、正则 T₁ 三个存在性子问已被 Brouwer 1976 年更强的非可分可度量例子覆盖；原卡增加的“完整刻画”不是原问。可分可度量情形恰有否定结论。 | [来源](https://mathoverflow.net/questions/507958/connected-spaces-with-no-nontrivial-open-connected-subsets)：主问：Γ 空间定义及 T₁、T₂、regular T₁ 三问；[来源](https://ir.cwi.nl/pub/6862/6862D.pdf)：ZW 83/76 (1976)；§1 命题及推论；§2，印刷 pp.2–5，尤 p.4 性质(vii)；[来源](https://ir.cwi.nl/pub/6862)：作者、题名、报告号 ZW 83/76、1976 年元数据 | Brouwer 可度量弧连通非可分例子满足 T₁。；同一 metric 例子满足 Hausdorff。；同一 metric 例子满足 regular T₁。；只限非退化 separable metric 空间；不可推广为所有 regular T₁ 均不存在。 | 取得 CWI 原报告全文，核对 §1 命题/推论及 §2 度量构造性质(vii)；不是依赖旧卡 solved 备注。报告给更强的 metric 例子，蕴含三个分离公理版本均存在。 日志：logs/card_2181_search.json；原题：logs/009_source_details.json。 | 如需最高验真级别，人工复核扫描 PDF 中度量定义及正定性估计。；QX-P-002192（rev c40bc86729042511）仅见索引，未读取该非指派参考卡全文，关系保持待定。 |
| QX-P-002182 / 49d622b3d4e05824 | 原题已解（a、b）；题面有误 | 旧：Π-群嵌入与不可解字问题 → Problem 15(a),(b) 已由 Rauzy 既有文献及明确的定义桥接给出肯定答案；(c) Morozov 型不嵌入 S_rec 的残余有限版本仍未取得解答。当前通俗题面把嵌入方向改写，须恢复三个子问。 | [来源](https://arxiv.org/html/2507.03972v1)：§6 e.r.f. 定义、Theorem 14、Problem 15(a)–(c)；[来源](https://doi.org/10.1515/jgth-2020-0029)：J. Group Theory 25 (2022), 217–246；Definition 1、§1.1、Theorem 3；arXiv:2002.02541v2；[来源](https://www.degruyterbrill.com/document/doi/10.1515/jgth-2020-0030/html)：J. Group Theory 24 (2021), 445–452；Theorem 2 与 effectively residually finite 定义 | Rauzy Theorem3 给有限生成 RF＋CFQ＋不可解 WP 群。枚举有限群及生成元映射，用 CFQ 决定延拓，找到分离非平凡字的有效有限商，故 e.r.f.；同一搜索恰在非平凡字上停机，故 WP 补集 c.e.，WP 为 Π⁰₁。再用 workshop Theorem14 得所需可计算 profinite 嵌入。；Rauzy Theorem2 给更强的 decidable WP＋RF＋非 e.r.f. 群；可判定集合属于 Π⁰₁，故直接满足该存在性子问。；保持不嵌入递归置换群 S_rec 的额外要求；(a) 的 e.r.f. 群及(b) 的可判定字问题群均未证明满足此要求。 | 两组学术检索后以 system1 定位并直接读取 Rauzy 两篇出版商 HTML 的定义和关键定理；核对 arXiv2002.02541 v2 修订历史。没有把 CFQ 失败误当 e.r.f. 失败。 日志：logs/card_2182_search.json；原题：logs/001_sources.json。 | 两篇存在群构造没有做独立逐行数学复证；如需强验证等级需专家复核。；继续追查(c) Morozov 型 RF 构造；现有(a)(b)文献不能填补其额外不嵌入条件。 |
| QX-P-002184 / 07cec84742854f0a | 题面有误 | 旧：profinite 群一阶定义类的 Borel 复杂度 → 原 Problem17 只问一个一阶句子所定义的 profinite 群类可能具有何种复杂度；当前题面扩展到任意理论，且未固定标准 Borel 参数化。本次只取得单句有限可公理化的既有背景，未取得一般复杂度分类。 | [来源](https://arxiv.org/html/2507.03972v1)：§6，Problem 17 及 Nies–Segal–Tent 2021 背景；[来源](https://arxiv.org/abs/1907.02262)：v5, 2021-05-22；摘要/修订历史；已刊 Proc. London Math. Soc.，DOI 10.1112/plms.12420 | 需要明确 profinite 群的编码空间和句子的语义；没有声称任意理论得到同一问题。 | 两组检索及 system1 补查定位 Nies–Segal–Tent 已刊论文、arXiv1907.02262 v5。该文的具体群单句刻画不是任意 φ 所定义的群类复杂度全分类；新 profinite/motive 或动力系统编码命中也未给出同题结果。 日志：logs/card_2184_search.json；原题：logs/001_sources.json。 | 原段未细述参数化；须与提出者工作中的编码约定对齐，再评估 Borel/解析复杂度。；本次 Nies–Segal–Tent 只核摘要和版本，未宣称阅读全文证明或完成分类。 |
| QX-P-002185 / 4c18dc9d62f2726e | 部分进展 | 旧：oligomorphic 群拓扑同构是否光滑 → 2026 年当前 v3 已在无代数性类、有限共轭类 essential 子群等 Borel 子类证明光滑；一般 oligomorphic 群的拓扑同构是否光滑仍被该文明确保留。不能把子类结论升级为全类。 | [来源](https://arxiv.org/html/2507.03972v1)：§6，Problem 19；[来源](https://arxiv.org/html/2410.02248v3)：引言 Theorem1.2、general isomorphism open 段；Theorem4.7(1)；Lemma5.4、Lemma5.13、Corollary5.16；[来源](https://arxiv.org/abs/2410.02248)：v3 submitted 2026-06-18；Beijing J. Pure Appl. Math. 3 (2026), no.2, 387–416；DOI 10.4310/BPAM.260903011500 | 全类尚未由当前文献解决；存在 essentially countable 上界，已得到重要 Borel 子类的 smooth 结论。；仅子类：满足相应性质 P 的 Assumptions4.2，且 P-open subgroups 有限个共轭类；实例包括无代数性、有限 essential 共轭类/弱消去虚元素的有关类。这是全类原问的受限进展，不是全类结论。 | 两组学术查询后读 arXiv2410.02248v3 全文与修订页，重点核 Theorem1.2、Theorem4.7、Lemma5.4、Lemma5.13、Corollary5.16；最新 v3 的受限结论比只引原工作坊更具体。 日志：logs/card_2185_search.json；原题：logs/001_sources.json。 | 一般 oligomorphic 类的 smooth 性仍需新的完整证明/反例；未进行 v3 全文逐行独立审计。 |
| QX-P-002186 / 5b89afebfa698af4 | 部分进展；题面有误 | 旧：oligomorphic 群 Out(G) 是否 profinite → 一般 Out(G) 已知为全不连通局部紧群（t.d.l.c.）；2026 v3 在特定子类证明 profinite。全类紧性仍是原问题；原卡对 Aut(G) 拓扑写成一般紧开拓扑需要校正。 | [来源](https://arxiv.org/html/2507.03972v1)：§6，Theorem 20、Problem 21；[来源](https://arxiv.org/html/2410.02248v3)：§2.3 Aut(G) 的 Polish 拓扑；Theorem1.1；Theorem4.7(3)；Lemma5.4/5.13；引言的 Out(G) 问题；[来源](https://www.impan.pl/en/publishing-house/journals-and-series/fundamenta-mathematicae/online/116469/automorphism-groups-of-non-archimedean-groups)：Fundamenta Mathematicae 275 (2026), 171–196，DOI 10.4064/fm251207-9-6，出版页 2026-10-29；摘要 | 全类已有 t.d.l.c.；compact 尚未由所核资料解决。Theorem4.7 条件下的子类为 profinite。；限满足 Assumptions4.2、P-open subgroups 有限共轭类的情形，包含文中无代数性及 essential 子群相关实例。这是全类原问的受限进展，不是全类结论。 | 逐题两组查询后核 2410.02248v3 的 §2.3、Theorem1.1、Theorem4.7(3) 与实例；另读 2026 年 Nies–Schlicht 论文出版页摘要，后者给 locally compact，未证明全类 compact。 日志：logs/card_2186_search.json；原题：logs/001_sources.json。 | 全类 Out 紧性尚需新证据；Nies–Schlicht PDF 未能取得，本次只做摘要级范围核对。 |

## 指定对子：11/11 已读双方当前正文

只报告，不合并。以下关系全部由本次双正文比较产生，未把历史判断当证据。

| 双方题号与版本 | 关系 | 复核理由 |
|---|---|---|
| QX-P-002164 (9875e0a8e54d92a6) ↔ QX-P-002437 (3d5a42c8263ffe79) | 相关但不等价 | 2164 问每个正整数是否至少有两完全幂之差表示（突出 n=6）；2437 的 Pillai 猜想问每个固定非零差的表示数是否有限。空表示集也有限，有限性不能回答存在性，不能合并。 |
| QX-P-002169 (d807a40adc752ec7) ↔ QX-P-001292 (32bcb69c92a54707) | 相关但不等价 | 1292 问自仿射 IFS/测度的 Hausdorff 维数与 affine dimension/矩阵半群条件；2169 是任意实数集的正测度 gauge 集合 I(A) 的值域、公式复杂度及一致性四问。对象、量词和结论均不同。 |
| QX-P-002169 (d807a40adc752ec7) ↔ QX-P-002177 (393d712b851e12d0) | 同源不同问 | 同源 arXiv2507.03972：2169 为 Problem1 的 gauge 集合值映射四问，2177 为 Problem11 的正树原理 Hausdorff 维数类比。并非同一集合维数计算题，也没有给出逻辑等价。 |
| QX-P-002177 (393d712b851e12d0) ↔ QX-P-002183 (062bfae24d996910) | 同源不同问 | 同源 Problem11 与 Problem16：前者为逆数学树原则的维数类比，后者问增加拓扑有限生成条件的可计算 profinite 群中 Hausdorff 维数可实现值。空间、有效性、量词均不同；不采用 2183 人话版关于度量无关的未核断言。 |
| QX-P-002177 (393d712b851e12d0) ↔ QX-P-002284 (53e30ff5507d6b2b) | 相关但不等价 | 2177 使用 Hausdorff dimension（分形维数）和逆数学树原则；2284 使用 Hausdorff 分离公理，问每个紧 Hausdorff 空间是否是齐性紧空间连续像。同名 Hausdorff 不是等价证据。 |
| QX-P-002177 (393d712b851e12d0) ↔ QX-P-002350 (7ef0f198405d15cc) | 相关但不等价 | 2350 问无限齐性紧 Hausdorff 空间中的非平凡收敛点列；2177 问正树原则的维数替换。分离性质/序列与测度维数/逆数学原则不是同一命题。 |
| QX-P-002177 (393d712b851e12d0) ↔ QX-P-002351 (d45262ebd0ae2e80) | 相关但不等价 | 2351 问齐性 ω-monolithic 紧 Hausdorff 空间是否第一可数；2177 的 Hausdorff 是维数术语，并非紧性、齐性或可数性公理问题。 |
| QX-P-002180 (87d56552cf1abddc) ↔ QX-P-000371 (986442c2458f9b82) | 相关但不等价 | 371 问 ℓ₁ 闭子空间 U 的 L₁ 商与 Lipschitz retraction 反例；2180 问 X×R 双 Lipschitz 嵌入有限维 Rⁿ 能否降一维。Banach 商/回缩条件不能与欧氏目标维数消去互换。 |
| QX-P-002180 (87d56552cf1abddc) ↔ QX-P-000411 (f0d4a56add52572b) | 相关但不等价 | 411 是离散 Lipschitz 函数图中的三项等差结构存在性，2180 是任意度量空间乘积的有限维欧氏双 Lipschitz 嵌入消去；共同 Lipschitz 词不产生同题或特例关系。 |
| QX-P-002182 (49d622b3d4e05824) ↔ QX-P-000867 (e5c996f88d0e3942) | 相关但不等价 | 867 的群必须来自 S⁴ 中 2-纽结补空间，附有几何/有限呈示约束；2182 讨论有限生成群的 Π⁰₁ 字问题、RF/e.r.f. 和可计算 profinite 或 S_rec 嵌入。没有所需几何实现蕴含，不能合并。 |
| QX-P-002185 (4c18dc9d62f2726e) ↔ QX-P-002186 (5b89afebfa698af4) | 同源不同问 | 同源 Problem19 与 Problem21：一个问拓扑同构等价关系是否 smooth，另一个问单个群 Out(G) 是否 profinite。2026 文献同一充分条件推出两个子类结论，不构成两个全局问题的等价。 |

### 新增候选（未完成正文复核）

QX-P-002181（886a9866f063943e）↔ QX-P-002192（c40bc86729042511）：题名/Γ 空间定义索引高度吻合；本次没有获取 2192 非指派正文，关系保持“待定”。不能据索引标题直接合并。

## 交接与验证范围

results.jsonl 为 25 行，保留原 id/card_rev/batch_id，所有 online_write_performed 均为 false。结构校验确认每个数学子问的 evidence_id 均有效，日志路径存在，指定 owner 对子无遗漏。

本组 math_results 中共有 5 条“原题已证”：2181 的三个原始存在性子问，以及 2182 的(a)、(b)。2166 的 EGZ 等价性已移入 background_results，原问的直接证明和二维类比两个请求均未关闭；2185/2186 的受限子类定理统一标为“部分进展”，不计作全类原问已证。另有 1 条“原题已反驳”只描述 2181 的可分可度量受限存在性。所有独立证明或形式化验证均没有冒记为通过。
