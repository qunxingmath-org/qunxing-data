# 待复核清单 · QX-NEW-06

由 `evidence.py import` 生成。提议结案用 `evidence.py review` 记二审结论；题卡改动走题卡修订流程；查重的合并要二审。

## 提议结案（要二审）（1）

| 题号 | 提议 | 说明 |
|---|---|---|
| QX-P-002031 | 原题已证明 |  |

## 题卡改动建议（134）

| 题号 | 建议 |
|---|---|
| QX-P-001966 | {"priority": "P1", "action": "提出修卡建议，未实施线上写入", "old": "人话版把表示数问题泛化成研究方法，并未保留无界性和满射性两个子问。", "new": "对素数 p，以原文的完全幂约定计数 p=a+b、0<a<b 的表示数 f(p)；问 f(p) 是否无界，以及若无界是否取遍所有自然数。 两个子问均未找到可验证全解。新检出的 arXiv:2509.11558 已撤回，且其目标整数不要求为素数，不能用于本题。", "evidence_ids": ["E1966-01", "E1966-02"]} |
| QX-P-001967 | {"priority": "P1", "action": "提出修卡建议，未实施线上写入", "old": "Ω 是停机概率，不是 Lambert W 的常数；一般正规数、Martin-Löf 随机数和某台机器的 Ω 不可混同。", "new": "Chaitin Ω 的二进制前缀整数 floor(2^n Ω) 是否有无穷多个为素数；须保留通用前缀机及其 Ω 的约定。 原帖没有给出全解。发现十进制正规数全部前缀合数的 Lean 仓库，但它不涉及二进制 Chaitin Ω，不能反驳原题。", "evidence_ids": ["E1967-01", "E1967-02"]} |
| QX-P-001968 | {"priority": "P1", "action": "提出修卡建议，未实施线上写入", "old": "不是任意图类的集合包含偏序；顶点数固定，元素是图同构类。", "new": "P_n 为 n 个顶点的无标号图同构类，按子图关系排序；问每个 n≥5 时 Aut(P_n) 是否只有恒等。 未找到所有 n≥5 的证明或反例。新增直接同题的 UQ/GPT-5 公开回答，但页面要求人工验证，不能作为已解或确认开放的依据。", "evidence_ids": ["E1968-01", "E1968-02"]} |
| QX-P-001969 | {"priority": "P1", "action": "提出修卡建议，未实施线上写入", "old": "原题输入是整系数多项式，不是给定有限初始段；按原序周期集是尾部型集合，可能为无限集。", "new": "输入 f∈Z[x]，作为 R→R 的动力系统，算法判定实周期集在 Sharkovskii 序中的四类截断及相应参数。 未找到原四类截断的统一判定算法。整数周期点算法、Sharkovskii 定理形式化与连续半代数函数迭代终止性均不能直接代替此题。", "evidence_ids": ["E1969-01", "E1969-02", "E1969-03", "E1969-04"]} |
| QX-P-001970 | {"priority": "P1", "action": "提出修卡建议，未实施线上写入", "old": "U 的分布在原文已明确，不应写成任意噪声；主要问密度不动点，不只是抽象收敛。", "new": "T 作用于支撑在 (0,φ) 的连续概率密度，(Tf)(x)=2x(f*1_(0,1))(x²)，求其不动点；对应独立 U_n∼Uniform(0,1) 的 X_{n+1}=sqrt(U_{n+1}+X_n)。 恢复原题全文，确认历史所引密度方程与 mercio 的仿射段评论。未找到完整显式不动点；离散噪声的嵌套根式帖子不适用。", "evidence_ids": ["E1970-01", "E1970-02"]} |
| QX-P-001971 | {"priority": "P0", "action": "提出修卡建议，未实施线上写入", "old": "同胚和作为 X 的子集相等是不同子问；半正则空间不能定义为每个开集都正则开。", "new": "对开 U⊂X，何种条件保证 U 同胚于 int(cl U)；又在何种条件下同胚能推出二者相等。X 可假定局部紧可度量。 第二子问在 X=R 已有显式反例，旧卡的 R 情形判断需纠正；一般条件刻画未找到全解。", "evidence_ids": ["E1971-01"]} |
| QX-P-001972 | {"priority": "P1", "action": "提出修卡建议，未实施线上写入", "old": "这是存在性命题，并要求 N 合数；给出一个素数值不能反驳该存在性。", "new": "是否存在偶数 b、b 不是 2 的幂，使合数 N=b^4+1 满足 2^(N−1)≡1 mod N。 已核 MSE 与 MO 交叉原帖。MO 回答给条件性启发式，没有构造可验实例或证明不存在。", "evidence_ids": ["E1972-01", "E1972-02"]} |
| QX-P-001973 | {"priority": "P0", "action": "提出修卡建议，未实施线上写入", "old": "人话版若要求延拓域包含整条实轴便加入原点，改变问题；原帖用稳定分布解释这个区别。", "new": "求概率特征函数/Levy 特征指数在原点之外延拓到非带状复域（如扇形）的充分条件；原文允许实轴非零点附近，特意排除在 0 邻域全纯的要求。 关键变化是补回原点排除和具体域。检出的大量条带解析/指数矩结果不自动回答该非带状延拓问题。", "evidence_ids": ["E1973-01"]} |
| QX-P-001974 | {"priority": "P0", "action": "提出修卡建议，未实施线上写入", "old": "不是无限维 l1 的另问；坐标轴上的四点是 l1 等距构型，普通轴对齐正方形的顶点不是。", "new": "固定有限维 l1 度量，最多能有多少两两等距点；原帖具体问 R³ 能否放 8 点、R⁴ 能否放 16 点，并问 ±e_i/2 的 2d 构型是否最优。 具体三、四维子问由旧文献已知最大 6、8 排除；一般 d 的 2d 猜想仍未取得全解。旧卡把 p=1 的 O(d log d) 称为 2026 新界不准确，2020 原稿已归于 Alon–Pudlak。", "evidence_ids": ["E1974-01", "E1974-02", "E1974-03", "E1974-04"]} |
| QX-P-001975 | {"priority": "P1", "action": "提出修卡建议，未实施线上写入", "old": "z 可取任意整数时 +z³ 和 −z³ 给同一表示集，不构成数学勘误；正定并不表示沿每个坐标绝对值逐项单调。", "new": "整数多项式 Q(x,y)−z³，Q=4x²+2xy+7y²，是否恰好漏掉指定 ±2m³、±32m³ 例外族；x,y,z∈Z。 重新定位 AMM 11539 已刊非表示证明，印刷 pp.884–885。它仅证明例外族不表示，未证明族外全部可表示；原两帖未取回，改用作者2014交叉说明校准。", "evidence_ids": ["E1975-01", "E1975-02", "E1975-03"]} |
| QX-P-001976 | {"priority": "P0", "action": "提出修卡建议，未实施线上写入", "old": "人话版换成了 f(x)=∫_0^x f(x−f(t))dt；零函数也不满足严格正条件。旧记录把 C1 存在性列为残余开放，需修正。", "new": "存在非常数、全局连续、严格正的 f:R→(0,∞)，使 f(x)=∫_(x−f(x))^(x+f(x)) f(t)dt 吗。 原帖 Simd 的连续构造可直接验算。相同支撑间隔论证允许取零均值光滑小扰动，因此 C∞ 非常数解亦存在；这是本轮对旧构造的明确推论，不是新文献声明。", "evidence_ids": ["E1976-01", "E1976-02"]} |
| QX-P-001977 | {"priority": "P1", "action": "提出修卡建议，未实施线上写入", "old": "不是任意拓扑域都满足该性质的断言；离散域已被排除，非阿基米德微分定义不能省略。", "new": "C 是否是唯一非离散拓扑域 K，使每个 C1 的标量函数 K→K 自动为 C∞；要明确所采用的拓扑域微分定义。 恢复原问唯一性量词。公开评论的超幂想法未给全部函数提升证明，检出的非阿基米德微积分文献不直接解决唯一性。", "evidence_ids": ["E1977-01", "E1977-02"]} |
| QX-P-001978 | {"priority": "P1", "action": "提出修卡建议，未实施线上写入", "old": "原问是整个紧定义域的像，不能换成任意 Borel 子集之像。", "new": "紧伪度量空间 X 上的下半连续实函数 f，整个像 f(X) 是否一定 Borel。 已读 MSE 的已解决更新和 MO Gro-Tsen 完整反例；旧卡已解结论可保留，但应明确否定回答的对象。", "evidence_ids": ["E1978-01", "E1978-02"]} |
| QX-P-001979 | {"priority": "P0", "action": "提出修卡建议，未实施线上写入", "old": "人话版把子群区间换成整个子群格；Palfy–Pudlak 是普遍量词等价，不能直接逐格互推。", "new": "小有限格（特别七/八元及指定七元例）能否作为有限群的完整子群区间 [H,G]；与有限代数的整个同余格表示须分开。 发现指定例 L7 的 2026 完整群表示稿和 DeMeo 作者仓库复算，旧‘此例未解决’已过时。广义否定/不可判定论文另有声明，但公开 Lean 206 只覆盖图刻画；不据此判整题全解。", "evidence_ids": ["E1979-01", "E1979-02", "E1979-03", "E1979-04", "E1979-05"]} |
| QX-P-001980 | {"priority": "P0", "action": "提出修卡建议，未实施线上写入", "old": "不是小倍增和集基数是否为2的幂；核心是最短表示唯一性及两项间隔条件。", "new": "正整数真子集 S={a1<a2<…} 满足 a_(n+1)≤2a_n、相邻差无界、每个正整数都有按加数最少且忽略排列唯一的 S 表示（允许重复），是否必为2的幂集。 MSE/MO 同源主问已核。作者局部检验到128与附加引理没有替代全称证明；未找到后续完整解。", "evidence_ids": ["E1980-01", "E1980-02"]} |
| QX-P-001981 | {"priority": "P0", "action": "提出修卡建议，未实施线上写入", "old": "finitely presentable 是范畴论性质，不是有限生成 sigma 代数、sigma 有限性或标准 Borel 性。", "new": "在可测空间及可测映射构成的 Meas 中，哪些对象 X 的 Hom(X,−) 保持滤过余极限；是否仅有限离散可测空间。 原帖给出有限离散的充分方向；一般逆向未找到可验证证明。相邻滤过余极限不交换有限极限的反例不能直接完成分类。", "evidence_ids": ["E1981-01", "E1981-02", "E1981-03"]} |
| QX-P-001982 | {"priority": "P1", "action": "提出修卡建议，未实施线上写入", "old": "不能把存在 Lorentz 度量、Riemann 完备或仅因果类完备当作全测地完备。", "new": "S² 去掉 n≥3 个点的非紧曲面，是否存在所有测地线按仿射参数完整的 Lorentz 度量。 原帖与 n=1,2 的背景例已检索到；未找到 n≥3 的可验证全解。", "evidence_ids": ["E1982-01"]} |
| QX-P-001983 | {"priority": "P0", "action": "提出修卡建议，未实施线上写入", "old": "不是唯一铺砌是否可判定这一宽问；按面积 n 的线性算法已是背景，所求是周长复杂度。", "new": "以边界/周长 p 为输入，能否在 O(p log p) 或更好时间判定单连通格区域的多米诺铺砌唯一性。 Pak–Sheffer–Tassy Theorem1.2 只给 tileability；Theorem1.3 给极大铺砌的点查询。它们不直接宣布唯一性判定达到原复杂度。", "evidence_ids": ["E1983-01", "E1983-02", "E1983-03"]} |
| QX-P-001984 | {"priority": "P0", "action": "提出修卡建议，未实施线上写入", "old": "当前人话版在主特征值简单、全谱简单、开稠和稠密Gδ间混用；必须回到原文后决定。", "new": "旧卡声称原问题为 Ruelle 算子谱单性的 C1 通有性；本轮未取回 MSE4753404/MO452567，故不确认其精确函数空间、势函数、主特征值/全谱及开稠/剩余量词。 已实际执行原址、API、StackPrinter、题名及公式查询，指定两帖未恢复。相邻 Ruelle 文献不据标题套用；原题数学状态暂不判断。", "evidence_ids": ["E1984-01", "E1984-02", "E1984-03"]} |
| QX-P-001985 | {"priority": "P0", "action": "提出修卡建议，未实施线上写入", "old": "旧卡把 x+z 误写为 xz，继而把原题排除为无解；原帖标题和正文都含加号。", "new": "正整数 0<a<b<c，ab+1=x²、ac+1=y²、bc+1=z²，且 x+z=2y；问是否所有解都来自给定 Pell 递推族。 必须撤销对原题的‘恒空解’排除。样例(2,4,12;3,5,7)及 Pell 无限族满足原式；族的穷尽性本轮未找到可验证证明。", "evidence_ids": ["E1985-01", "E1985-02", "E1985-03"]} |
| QX-P-001986 | {"priority": "P1", "action": "提出修卡建议，未实施线上写入", "old": "是固定坐标下的定义域下降，不是仅存在某个抽象同构模型；不可把旧无回答标记压过交叉帖证明。", "new": "在固定仿射嵌入下，复代数集含 Zariski 稠密的代数坐标点，是否能由 Qbar 系数方程定义；一般化为域扩张 K/F。 已重新读到 Sawin 完整基展开证明，结论更一般，对任意域扩张成立。与2015同源同题，双方当前正文已复核。", "evidence_ids": ["E1986-01", "E1986-02"]} |
| QX-P-001987 | {"priority": "P0", "action": "提出修卡建议，未实施线上写入", "old": "棋盘和合法步集合无限；‘固定深度逐层枚举’不能直接给终止算法。普通无限象棋的 Presburger 证明不覆盖素数跳跃。", "new": "Trappist-1 无限棋含 Huygens 以任意素数格数正交跳跃；问 mate-in-1 或固定 n 的 mate-in-n 是否不可判定。 已核原问和普通无限棋邻题；未取得该变体的可判定/不可判定证明。新搜索命中支持 Huygens 的棋引擎，但有限机器坐标/启发搜索不是判定定理。", "evidence_ids": ["E1987-01", "E1987-02", "E1987-03"]} |
| QX-P-001988 | {"priority": "P1", "action": "提出修卡建议，未实施线上写入", "old": "长度2与半径1是固定常数；对路径的 Moser worm 覆盖结果不能自动推广到有分叉树。", "new": "任意平面树总长度2，能否经刚体移动放入半径1的闭半圆盘；不是任意最小半径的开放估计。 原问和分叉障碍已核。2026 新的 unit arcs/凸覆盖面积论文及代码只涉及路径，未找到原树问题的完整解。", "evidence_ids": ["E1988-01", "E1988-02", "E1988-03"]} |
| QX-P-001989 | {"priority": "P0", "action": "提出修卡建议，未实施线上写入", "old": "人话版却讨论多边形等面积三角剖分和 Monsky，和同卡历史的幂和/Thue–Morse内容冲突。", "new": "包内历史线索指 Prouhet–Tarry–Escott 型整数分拆最大等幂指数 s_n；指定 MSE4075536 本轮未恢复，故不补造其精确定义和端点约定。 必须先恢复原题后修复人话版。已检索到 Littlewood 多项式/等幂分拆文献，但不能在未知 s_n 精确定义时宣称覆盖原题。", "evidence_ids": ["E1989-01", "E1989-02"]} |
| QX-P-001990 | {"priority": "P0", "action": "提出修卡建议，未实施线上写入", "old": "笼是四面体1-骨架六根杆，不是四个支撑平面组成的外切四面体；可外切不等于不能逃逸。", "new": "任意 R³ 的凸紧体（有非空内部），能否被某四面体的六条棱组成的固定笼困住，无法经允许旋转的连续刚体运动逃到远处而不让棱穿入体内部。 原作者定义已核。Schramm 的 midscribing 与二维圆盘的 cage 结果不能直接当作任意三维凸体的动态困笼定理。", "evidence_ids": ["E1990-01", "E1990-02", "E1990-03"]} |
| QX-P-001993 | {"priority": "P0", "field": "title/statement/human_version", "old": "无有理点光滑真 Z-概形维数上限；最多能到几", "proposed": "无截面光滑真 Z-概形的最小相对维数；注明 Spec Z 截面及 2≤d≤5", "reason": "最大/最小颠倒；乘射影空间说明上限问法平凡无界。", "execution": "仅建议；未改线上"} |
| QX-P-001994 | {"priority": "P0", "field": "statement/human_version", "old": "每个方向的单位线段；圆环总面积能否很小", "proposed": "恢复所有中心、半径区间趋近 1、整圆包含与补集正测度命题", "reason": "两类几何对象、量词、结论均不相同。", "execution": "仅建议；未改线上"} |
| QX-P-001994 | {"priority": "P1", "field": "notes/subquestions", "old": "弱化变体 open", "proposed": "记录 Eberhard 的弱版归约及非可测性保留；强版维持评论草图级证据", "reason": "现卡漏记来源中直接针对弱版的实质评论。", "execution": "仅建议；未改线上"} |
| QX-P-001995 | {"priority": "P1", "field": "statement", "old": "只有“多项式正系数”主题", "proposed": "补全 P_n 公式、n 的范围、非负系数结论及 q-Pochhammer 记号", "reason": "缺公式会把本题混同为任何正系数/Borwein 命题。", "execution": "仅建议；未改线上"} |
| QX-P-001996 | {"priority": "P1", "field": "statement/scope", "old": "笼统的群离散化和集合论影响", "proposed": "明确固定 Lie 群、离散化拓扑、指定系数及具体待判性质", "reason": "防止把改变群本身或系数的独立性例子误当解答。", "execution": "仅建议；未改线上"} |
| QX-P-001997 | {"priority": "P0", "field": "statement/human_version", "old": "在 BSS 模型刻画 P、NP 或 P=NP 的结构条件", "proposed": "寻找无明显经典 Turing 对应物的自然、有用的 BSS 复杂度类", "reason": "必须保留原问题的开放式范围和示例资源。", "execution": "仅建议；未改线上"} |
| QX-P-001998 | {"priority": "P0", "field": "statement/human_version", "old": "全部复根同一直线及完整分类", "proposed": "恢复四个编号子问和排除条件", "reason": "原卡把部分根的存在性问题替换成全部根分类。", "execution": "仅建议；未改线上"} |
| QX-P-001998 | {"priority": "P1", "field": "notes/residuals", "old": "2 的幂猜想仅被 3×6 实例削弱", "proposed": "注明 338213 无附加限制版本被六次 Eisenstein 反例否定；保留斜率分类及更严格版本的区别", "reason": "已有明确反例但作用范围必须写清。", "execution": "仅建议；未改线上"} |
| QX-P-001999 | {"priority": "P0", "field": "statement/human_version", "old": "复环面、按高度或判别式计数", "proposed": "改为 F_q、Frobenius 特征多项式、主极化及 Σ1/\|Aut(A,λ)\|", "reason": "对象和计数口径错误。", "execution": "仅建议；未改线上"} |
| QX-P-001999 | {"priority": "P1", "field": "evidence/partial_progress", "old": "只概括 Howe 2020/simple ordinary", "proposed": "增加 2023 Theorem A，并细分 fixed order、极化同源类及一般上界", "reason": "新公式有严格范围，不能当成一般上界的证明。", "execution": "仅建议；未改线上"} |
| QX-P-002000 | {"priority": "P0", "field": "statement/parameter_regularities", "old": "参数也光滑依赖", "proposed": "恢复连续参数族，注明 Diff 的 C^0 拓扑、D^n 与相对边界条件", "reason": "参数正则性提高会改变命题。", "execution": "仅建议；未改线上"} |
| QX-P-002001 | {"priority": "P2", "field": "terminology", "old": "笼统正系数", "proposed": "保留非负实系数、子集无重复及固定 n", "reason": "零系数允许，不能替换成严格正系数或多重集。", "execution": "仅建议；未改线上"} |
| QX-P-002006 | {"priority": "P0", "field": "statement/human_version", "old": "猜出递推即可由有限数据验证；未列具体序列", "proposed": "恢复 G_n、r、k、P_n 与 ν_k 公式", "reason": "目标不是一般的生成函数猜测验证方法。", "execution": "仅建议；未改线上"} |
| QX-P-002006 | {"priority": "P1", "field": "claim_scope", "old": "D. Ray 证明线索笼统待核", "proposed": "将 k-bonacci/模 m 变体和原题精确系数计数分列，记录 SSRN 不可达、ProbXiv 无人工检查", "reason": "两处量词变化阻止直接覆盖原题。", "execution": "仅建议；未改线上"} |
| QX-P-002007 | {"priority": "P0", "field": "human_version", "old": "1/ζ 是整函数；ζ 的零点被抵消", "proposed": "1/ζ 为亚纯函数；单零点产生简单极点，残数为 1/ζ′", "reason": "基本解析事实写反。", "execution": "仅建议；未改线上"} |
| QX-P-002007 | {"priority": "P0", "field": "notes/2409.02106", "old": "RH+单性条件有效上界", "proposed": "补 v10、Cor.1/2 的相关式右端为负条件；标出负性只有数值支持而非已证", "reason": "最新原稿不支持旧卡省略条件的表述。", "execution": "仅建议；未改线上"} |
| QX-P-002008 | {"priority": "P0", "field": "statement/human_version", "old": "full exceptional collection，未注明向量丛", "proposed": "补向量丛，不要求 strong；区分任意复形与线丛版本", "reason": "省略核心限制改变问题状态。", "execution": "仅建议；未改线上"} |
| QX-P-002008 | {"priority": "P1", "field": "partial_progress", "old": "未列该已刊特例", "proposed": "增加 Cor.1.4 及适用范围和域约定", "reason": "存在直接匹配向量丛的受限结果。", "execution": "仅建议；未改线上"} |
| QX-P-002009 | {"priority": "P0", "field": "statement/human_version", "old": "对发散谱序列作虚拟化/正则化", "proposed": "按原文定义 virtual：X 的足够高连通部分；补高度 d 和收敛目标", "reason": "原卡解释替换了技术含义。", "execution": "仅建议；未改线上"} |
| QX-P-002010 | {"priority": "P0", "field": "statement/human_version", "old": "多一个变量能否消去；A 自身作为 A-模平坦整", "proposed": "B=k[x_1,…,x_n] 是有限平坦 A-模，问 A 是否为多项式环", "reason": "原卡改问另一问题并误置模主体。", "execution": "仅建议；未改线上"} |
| QX-P-002010 | {"priority": "P1", "field": "bibliography/scope", "old": "Gurjar 2024 J. Algebra 相关进展", "proposed": "Gurjar–Miyanishi, JPAA 228(8),107655；Theorem 6 三变量且含坐标的正则 cofinite 情形", "reason": "刊物与适用范围需修正。", "execution": "仅建议；未改线上"} |
| QX-P-002012 | {"priority": "P0", "field": "statement/human_version", "old": "约 0.7731 的 Flajolet–Martin φ 是否无理/超越", "proposed": "以 α 的精确无穷乘积为题面；φ 只作背景并写清关系", "reason": "两个常数的算术性不是已知等价命题。", "execution": "仅建议；未改线上"} |
| QX-P-002013 | {"priority": "P0", "field": "statement/human_version", "old": "一族群与生成集共同正下界", "proposed": "固定群 Γ 的全部有限生成集；单列 S_{p,q}", "reason": "量词错置。", "execution": "仅建议；未改线上"} |
| QX-P-002013 | {"priority": "P0", "field": "title/status_claim", "old": "题名写否定解决；2608.03561 作者/题名当作已完全核定", "proposed": "一般版本保留完整声明待核；特殊族不宣告解决；登记官方索引与其他条目版本元数据冲突", "reason": "来源不可达与冲突限制了本轮可靠性。", "execution": "仅建议；未改线上"} |
| QX-P-002014 | {"priority": "P0", "field": "statement/human_version", "old": "连续满射、每点纤维可数稠密或 Q^ω 可数", "proposed": "恢复 f^{-1}(Q^ω)=Q_0^ω 及最终为零定义；删除满射/逐纤维限制", "reason": "原卡同时改变映射条件和目标集合基数。", "execution": "仅建议；未改线上"} |
| QX-P-002015 | {"priority": "P1", "field": "metadata.sources/external_refs", "old": "MO#4475853", "proposed": "MSE#4475853；对应 MO#428384，Sawin 答案 #428394", "reason": "来源站点编号混用。", "execution": "仅建议；未改线上"} |
| QX-P-002015 | {"priority": "P1", "field": "duplicates", "old": "关联线索未逐正文核清", "proposed": "与 QX-P-001986@00b8701da1d461f7 标记同题", "reason": "本轮已读两卡与原证明；仅报告，不在线合并。", "execution": "仅建议；未改线上"} |
| QX-P-002016 | {"priority": "P0", "field": "notes/counts/status", "old": "S(4)=17、S(5)=237、S(6)=9892 是全等类计数；已独立验证", "proposed": "保留它们为立方体对称轨道数据，撤回 n≥5 时与欧氏全等计数等同；不得沿用旧“独立验证”", "reason": "Ziegler 全维五维反例使两种分类严格不同。", "execution": "仅建议；未改线上"} |
| QX-P-002016 | {"priority": "P0", "field": "AI_claim_assessment", "old": "AI 说不在 OEIS 已被 A126776 推翻", "proposed": "撤回基于错误等价关系的 AI 错误判定，真实欧氏全等序列是否另在 OEIS 待核", "reason": "题目和序列定义错配，不能据此评价答案对错。", "execution": "仅建议；未改线上"} |
| QX-P-002016 | {"priority": "P1", "field": "human_version/algorithm", "old": "枚举边长多重集即可核类别", "proposed": "比较带顶点关联的完整距离矩阵，并对顶点置换取等价类", "reason": "边长多重集不是一般的全等完备不变量。", "execution": "仅建议；未改线上"} |
| QX-P-002017 | {"priority": "P0", "field": "statement/human_version", "old": "分类所有 G≅L(G) 图的度或度序列", "proposed": "存在可数连通 G≅L(G)，其有限度集合包含所有 n≥N_0", "reason": "原卡扩大了目标且容易将无限度例子误当有限度解答。", "execution": "仅建议；未改线上"} |
| QX-P-002018 | {"priority": "P0", "field": "notes/free_factor_status", "old": "自由群因子问题本身仍 open", "proposed": "新增 OpenAI 2026-09-23 的 L(F_2)≅L(F_3) 完整声明，锁定 commit；状态仍为声明待核", "reason": "有直接覆盖原存在性题的新作者原稿与形式化候选，旧卡遗漏。", "execution": "仅建议；未改线上"} |
| QX-P-002018 | {"priority": "P0", "field": "formal_verification", "old": "未列可定位代码或容易把 comparator 当证明", "proposed": "分别登记 comparator、solution、配置和依赖；明确代码已取得未重跑", "reason": "含 sorry 的比较器不是 proof；未审依赖不能宣称形式化通过。", "execution": "仅建议；未改线上"} |
| QX-P-002019 | {"priority": "P0", "field": "human_version/Cauchy", "old": "Cauchy 已说凸多面体由边长唯一决定", "proposed": "Cauchy 要对应面全等；仅在已给三角面等条件下可用边长确定面", "reason": "原卡的解释会把研究问题误写成已有平凡结论。", "execution": "仅建议；未改线上"} |
| QX-P-002020 | {"priority": "P1", "field": "statement/scope", "old": "非 Schottky 构造或无法用乒乓引理的自由群", "proposed": "自由离散 Γ，而两个投影各自不同时自由且离散", "reason": "把构造方法排除替换为可检验的原始性质。", "execution": "仅建议；未改线上"} |
| QX-P-002021 | {"priority": "P0", "field": "statement/human_version", "old": "选一些互不相交对角线，使最大块最优", "proposed": "画全部对角线；边长 1；奇数排中心；求 nA_n 的全 n 界", "reason": "划分方式、优化变量及归一化都改变了原题。", "execution": "仅建议；未改线上"} |
| QX-P-002025 | {"priority": "P1", "field": "题面/人话版/查新备注", "from_value": "人话版称“给定几个共轭类看一串特征标值”", "to_value": "改为对每个 V，问是否存在一个 C，使 \|C\|χ_V(C)/dim(V) 与所有其他不可约表示的对应值不同；单类同时分离全部表示作为另一个更强问题。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2025-01", "E2025-02"]} |
| QX-P-002026 | {"priority": "P1", "field": "题面/人话版/查新备注", "from_value": "人话版对 exotic twisted double 的构造和比较对象失真", "to_value": "写明 DX=X∪id(−X)、DXτ=X∪τ(−X)，τ 可延拓成同胚而不可延拓成微分同胚；比较两者微分同胚类型。原作者应为 Kyle Hayden。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2026-01", "E2026-02"]} |
| QX-P-002027 | {"priority": "P1", "field": "题面/人话版/查新备注", "from_value": "人话版把问题改为素数的行列式表示", "to_value": "逐项写回 n=(p−1)/2，首行 a₁ⱼ=(j/p)，其余 aᵢⱼ=((i²+j²)/p)，问 −det A_p 为奇平方。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2027-01"]} |
| QX-P-002028 | {"priority": "P1", "field": "题面/人话版/查新备注", "from_value": "“良好 forcing”未明确链条件及需要同时满足的条件", "to_value": "题面写回 V₁ 中 κ 不可达、V₂ 为 κ⁺-cc 扩张、κ 在 V₂ 中为 ℵω、κ 以下 GCH 与 κ 处失败；不能用 κ⁺⁺-cc 替换。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2028-01", "E2028-02"]} |
| QX-P-002029 | {"priority": "P1", "field": "题面/人话版/查新备注", "from_value": "题名/人话版侧重存在一对或无穷多对", "to_value": "明确“每个 n>1”及 m=1 允许，并将任何数值范围写为作者报告而非本轮复算。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2029-01", "E2029-02"]} |
| QX-P-002030 | {"priority": "P1", "field": "题面/人话版/查新备注", "from_value": "A 型结论与一般有限 Coxeter 群表述容易混列；“三篇独立论文”未核实", "to_value": "保留 A 型已证，并将一般 W 单列；书目写全作者与正式期刊版本。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2030-01", "E2030-02"]} |
| QX-P-002031 | {"priority": "P0", "field": "题面/人话版/查新备注", "from_value": "三维数值非消失已证，而线性有效性仍 open；人话版 klt/伪有效，遗漏第二问", "to_value": "更新为 Müller 2025 三维实际线性非消失已证；保留一般维数条件范围。恢复原问光滑射影且 −KX nef，并列出 ample divisor 限制子问；2026 光滑度量半正定声明单列为加强假设。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2031-01", "E2031-02", "E2031-03", "E2031-04"]} |
| QX-P-002032 | {"priority": "P1", "field": "题面/人话版/查新备注", "from_value": "人话版弱化/误写自同构与对跖的关系", "to_value": "明确完整面格组合自同构以及 f∘(−id)=(−id)∘f；不得以边图反例或逐点 ±v 替代。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2032-01", "E2032-02"]} |
| QX-P-002033 | {"priority": "P0", "field": "题面/人话版/查新备注", "from_value": "部分解决；1、Q₈ 与 1、Q₈、I* 两种转述冲突；余维二", "to_value": "原题按 smooth 分类更新为已证：仅 S³ 和 S³/Q₈；locally flat TOP 变体另含 S³/I*。修正余维为一，原问无穷多个子问为否。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2033-01", "E2033-02", "E2033-03"]} |
| QX-P-002035 | {"priority": "P1", "field": "题面/人话版/查新备注", "from_value": "人话版只展示可数递增链并当作原问", "to_value": "恢复 α<δ 的任意序数链；将已知短链结果与附加商群条件单列。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2035-01", "E2035-02"]} |
| QX-P-002036 | {"priority": "P1", "field": "题面/人话版/查新备注", "from_value": "人话版以普通 Hausdorff 维数实现问题取代对子群谱的限制", "to_value": "写明 dim_H G=1，∀H≤G，dim_H H∈{0,1}，并区分 ZFC 与 CH 条件结果、加法子群与子环。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2036-01", "E2036-02"]} |
| QX-P-002037 | {"priority": "P1", "field": "题面/人话版/查新备注", "from_value": "人话版把 monotone embedding 当成树的边嵌入", "to_value": "改为单射 f，若 v 为 u 的子节点，则 supp f(u) 严格包含于 supp f(v)；保留一次可增加多个坐标。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2037-01"]} |
| QX-P-002038 | {"priority": "P1", "field": "题面/人话版/查新备注", "from_value": "只固定体积并泛称低维投影", "to_value": "恢复协方差归一化及 inf_u \|proj_{u⊥}B\|/\|B\|；问题是所得 c_d 能否一致有界。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2038-01"]} |
| QX-P-002039 | {"priority": "P0", "field": "题面/人话版/查新备注", "from_value": "只保留普通 Dirichlet 级数延拓，并把自然边界作为确定事实", "to_value": "恢复两问及 digamma 归一化；将“Estermann 已处理”改为待核文献线索，区分 κ、log κ 与 prime zeta。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2039-01", "E2039-02"]} |
| QX-P-002041 | {"priority": "P1", "field": "题面/人话版/查新备注", "from_value": "旧备注“Ok 2016 部分区域稠密”未给实坐标、定理与区域定位", "to_value": "补 Ok–Perrett Theorem 1.2 p.3 的实 (q,v) 坐标范围；与复 C² 主问分列。正实象限的排除只解释实域，不自动排除复稠密。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2041-01", "E2041-02"]} |
| QX-P-002042 | {"priority": "P1", "field": "题面/人话版/查新备注", "from_value": "旧题意混入一般仿射情形/连通性", "to_value": "按 Hartshorne I.2.17：P³ 中闭不可约曲线，是否是两曲面的集合论交；保留原帖请求 2020 年后文献的意图。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2042-01"]} |
| QX-P-002043 | {"priority": "P1", "field": "题面/人话版/查新备注", "from_value": "人话版可能将 can 改为必然，或混用 weak Kurepa", "to_value": "题面保留存在性与原始树定义，并把一般 size κ 的子问单列。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2043-01", "E2043-02"]} |
| QX-P-002045 | {"priority": "P1", "field": "题面/人话版/查新备注", "from_value": "“几乎一样”被解读为近似谱/全谱等谱", "to_value": "恢复阈值以上完全相同、以下不同；补核是否按带重数谱计数，原帖集合写法未完全消除此细节。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2045-01"]} |
| QX-P-002046 | {"priority": "P0", "field": "题面/人话版/查新备注", "from_value": "仅有 jvvk 未验证回答；具体比值缺失；AI 暴露=无", "to_value": "补 Sra 2026 原稿、精确 Theorem 1.1/Cor.1.2 和特殊矩形分拆常数情形；维持声明待核，AI 来源分别记录 Claude 和 OpenAI GPT Pro 自述。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2046-01", "E2046-02", "E2046-03", "E2046-04"]} |
| QX-P-002047 | {"priority": "P1", "field": "题面/人话版/查新备注", "from_value": "把软问题标成具体有限生成分类难题", "to_value": "恢复原帖不限有限生成的范围，标为待明确的综述型问法；若要形成数学卡需另写可判定命题，不能直接替用户创造。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2047-01"]} |
| QX-P-002049 | {"priority": "P0", "field": "题面/人话版/查新备注", "from_value": "仅摘要层未知公式是否等于 OP 的 2(n−2)!；计数方向未明", "to_value": "记录 Cor.3 的精确公式、n≥6 范围、极值图与方向因子 2；补本轮 n=3..5 的独立有限穷举。维持一般证明的预印本待核层级。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2049-01", "E2049-02", "E2049-03"]} |
| QX-P-002050 | {"priority": "P1", "field": "题面/人话版/查新备注", "from_value": "现版题面正确，备注列出 Danzer 相邻背景", "to_value": "保留题面；把 Danzer/Alon 的相邻结果与本题的状态依据分开。本轮未取得本题完整证明，亦不证明其开放。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2050-01", "E2050-02"]} |
| QX-P-002051 | {"priority": "P0", "field": "题面/人话版/查新备注", "from_value": "Thompson F 仍 open；标题预设逆向数学；旧 AI 暴露中", "to_value": "背景状态更新为 2026 非 amenability 完整声明待核；交叉链接 2477，原宽问和背景定理分列。明确取得 Lean 代码但未重跑，不借第三方 verified 标签升格。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2051-01", "E2051-02", "E2051-03", "E2051-04", "E2051-05", "E2051-06"]} |
| QX-P-002052 | {"priority": "P0", "field": "题面/人话版/查新备注", "from_value": "最终问题缺失；N 与 Tango 都 c₁=0", "to_value": "写回 F 的序列 0→O→Λ²T(−2)→F→0 和问题 F≅N(1)；c₁(F)=2h，区分 F 与 F(−1)，保留截面/辛形式选择。", "reason": "以本轮读取的原始题面及所列原稿核对，不把旧卡备注本身作为新成果。", "evidence_ids": ["E2052-01"]} |
| QX-P-002053 | {"text": "将旧卡“无标准范畴结论”改为文献已有标准对应，并明确 cocycle 的等价与箭头。"} |
| QX-P-002053 | {"text": "主分类与 concordance 分类分开写；原引用书名与本次取得论文题名分别登记。"} |
| QX-P-002054 | {"text": "重写题面，补回 x0，注明 φ 的值域维数和允许的双变量形式。"} |
| QX-P-002054 | {"text": "将允许双变量的存在性与给定内函数只改权重的限制问题分为子问。"} |
| QX-P-002055 | {"text": "保留已有否定解状态；补回答直接链接，不把其称为本轮新定理。"} |
| QX-P-002055 | {"text": "区分局部定义与全局延拓；AI 一栏只登记可证的二手转述。"} |
| QX-P-002056 | {"text": "保留统一命题未核状态；所有计算范围标为作者报告。"} |
| QX-P-002056 | {"text": "逐项保留回答冲突及纠正，不把相邻截断指数/Taylor 多项式的 Galois 结果套用。"} |
| QX-P-002057 | {"text": "补解析粗界与较大模拟报告，注明数值不是证明。"} |
| QX-P-002057 | {"text": "AI 暴露增加 UQ260 的可核链接及评审状态。"} |
| QX-P-002058 | {"text": "把 m≤50000 作为带日期的作者计算报告补入，不标为独立验证。"} |
| QX-P-002059 | {"text": "补 Pierce expansion 同题入口及 k 与 P(P,x) 的步数约定。"} |
| QX-P-002059 | {"text": "新增2026 AI幂界声明，保留 O(log P) 子问待核，绝不写原题已解。"} |
| QX-P-002059 | {"text": "纠正阶乘例的差1。"} |
| QX-P-002060 | {"text": "不把已有例子作为本轮新发现；保留无穷性子问。"} |
| QX-P-002060 | {"text": "OEIS可达状态和1978原文未取得情况如实登记。"} |
| QX-P-002061 | {"text": "状态按子问拆分；不将C4反例作为本轮新发现。"} |
| QX-P-002062 | {"text": "维持特定谱问题未核；不要把一般Gödel或Chaitin证明当本题答案。"} |
| QX-P-002062 | {"text": "评论的Claude猜测不升级为已确认AI生成。"} |
| QX-P-002063 | {"text": "补回常结构、\|A\|<κ与good情形的全套已写条件，删除“原文不明确”的失实说明。"} |
| QX-P-002063 | {"text": "Final case单列作者声明并标投影满射缺口；不据此宣称一般问题已否定。"} |
| QX-P-002064 | {"text": "补有限图假设；保留claimed与“未独立重跑”限制。"} |
| QX-P-002064 | {"text": "形式化元数据更新为固定提交、主定理路径、精确依赖缺失情况。"} |
| QX-P-002065 | {"text": "将命题真伪和方法限制分列，保留现有题面“非分类”校准。"} |
| QX-P-002066 | {"text": "保留旧卡已校正的四连通约束；有限条带结果标作者计算。"} |
| QX-P-002067 | {"text": "按原MO重写量词与紧性条件。"} |
| QX-P-002067 | {"text": "Younsi的“似为开放”仅作稿件当时的状态证据；不将其类比性结果作一般等式。"} |
| QX-P-002068 | {"text": "纠正发表日期与年龄；保留原始评论的精确证据级别。"} |
| QX-P-002068 | {"text": "不写已知独立；ZFA与ZF转移须有正式依据。"} |
| QX-P-002068 | {"text": "公开AI查询返回的Partition Principle内容仅作不适用线索，不作同题结论。"} |
| QX-P-002069 | {"text": "原题不共线子问更新为已证，并附三条边平方与首次跳跃检查。"} |
| QX-P-002069 | {"text": "缺失面积谱保持独立子问；明确Theorem2的姐妹初值和不同版本。"} |
| QX-P-002070 | {"text": "保留Fibonacci与Lucas两子问；下标为a的连续幂，不是相邻Fibonacci数。"} |
| QX-P-002070 | {"text": "三项指定查重只登记相关但不等价，不合并。"} |
| QX-P-002070 | {"text": "计算界证据标摘要/记录级，不能写成代码证书通过。"} |
| QX-P-002071 | {"text": "登记viXra完整声明及具体缺口，不据其关题。"} |
| QX-P-002071 | {"text": "Zenodo记录按最新v1.1.0部分进展登记；59/83只标作者声称。"} |
| QX-P-002071 | {"text": "删除“原文代码截断所以无法对照”的失实摘要；补凸性/内交范围。"} |
| QX-P-002072 | {"text": "保留“猜测”而非已证/已反驳，明确数值与启发式的证据级别。"} |
| QX-P-002073 | {"text": "补S²的Euler0例；保留主丛假设和齐性作用的实际要求。"} |
| QX-P-002074 | {"text": "将“代数由向量生成”与“每元素是一个向量积”区分；删除后者。"} |
| QX-P-002074 | {"text": "补n≥2或明确允许标量前因子的约定。"} |
| QX-P-002074 | {"text": "退化例定位为原帖R^{1,1,1}计算；原卡所链3952133未在本轮打开核证，不维持其“采纳自答否证”的断言。"} |
| QX-P-002074 | {"text": "指定对子2276仅Clifford名称碰撞，相关但不等价，不合并。"} |
| QX-P-002075 | {"text": "在固定通常拓扑、固定加法的原范围下更新为否定解并附完整定理定位。"} |
| QX-P-002075 | {"text": "保留上述双向恒等映射应用，避免把只存在抽象微分同胚误写为题面结论。"} |
| QX-P-002076 | {"text": "保持允许自交范围；明确内二面角/无向两平面夹角以及自交点处的定义。"} |
| QX-P-002077 | {"text": "保留已解；补Theorem1精确条件及归一化应用。"} |
| QX-P-002077 | {"text": "不要误用仅中心区的Theorem2替代全系数结论；修正MO回答日期。"} |

## 查重（28）

| 题号 | 关系 |
|---|---|
| QX-P-001969 | {"pair_id": "QX-P-001969\|QX-P-001984", "owner_id": "QX-P-001969", "owner_card_rev": "c47be1c369c0c520", "other_id": "QX-P-001984", "other_card_rev": "4ad33dee4272b9b8", "relation": "相关但不等价", "basis": "1969 是整数系数实多项式的 Sharkovskii 周期截断可判定性；1984 当前正文指 Ruelle 谱单性通有性。问题对象、拓扑与输出不同。1984 原帖未取回，判断限于所提供现版正文。", "assigned": true, "review_scope": "随包双方现版正文已读并逐项比较；没有仅凭索引标题判同题", "action": "仅报告，不合并、不改线上"} |
| QX-P-001974 | {"pair_id": "QX-P-001974\|QX-P-002433", "owner_id": "QX-P-001974", "owner_card_rev": "1373906686a7095d", "other_id": "QX-P-002433", "other_card_rev": "598219f36b33f8d5", "relation": "相关但不等价", "basis": "1974 固定 ℓ¹ 范数，问最大等距集是否为 2d；2433 量化所有六维实赋范空间，问至少七个等距点。上界/下界、固定范数/全部范数均不同。", "assigned": true, "review_scope": "随包双方现版正文已读并逐项比较；没有仅凭索引标题判同题", "action": "仅报告，不合并、不改线上", "reference_card_note": "参考2433正文的 ℓ∞⁶ 立方体有64个顶点却写 e=12，及七顶点称正七单形，属于可见笔误；本轮仅作为查重参考提示，不新增该题查新任务。"} |
| QX-P-001979 | {"pair_id": "QX-P-001024\|QX-P-001979", "owner_id": "QX-P-001979", "owner_card_rev": "22150e30c616758a", "other_id": "QX-P-001024", "other_card_rev": "ec089c286914f879", "relation": "特例/强化", "basis": "1979 的小规模格及指定 L7 群区间问题是1024所有有限格量词下的特例；不得以有限代数整个同余格的逐例表示替代群区间表示。", "assigned": false, "review_scope": "1979随包现版正文；1024随包索引版本与2026-11-26只读取得的作者仓库正文比较。未核实实时正文对应的meta.card_rev，故版本对应列为待复核。", "action": "仅报告，不合并、不改线上", "other_body_source": "https://github.com/qunxingmath-org/qunxing-data/blob/main/problems/001/QX-P-001024.text.md", "other_body_blob_sha": "45dd14d0b1735a305b29ffaa2335f77cd0468912", "version_caveat": "other_card_rev保留包内索引值；实时正文与此rev是否一致未确认。"} |
| QX-P-001986 | {"pair_id": "QX-P-001986\|QX-P-002015", "owner_id": "QX-P-001986", "owner_card_rev": "00b8701da1d461f7", "other_id": "QX-P-002015", "other_card_rev": "0f78ce001d7fc0e8", "relation": "同题", "basis": "两卡当前正文均为固定坐标中代数点 Zariski 稠密推出在代数数域上定义，追溯到同一MO428384及Sawin回答；一般域下降为同一证明的强化。", "assigned": false, "review_scope": "随包双方现版正文已读并逐项比较；没有仅凭索引标题判同题", "action": "仅报告，不合并、不改线上"} |
| QX-P-001990 | {"pair_id": "QX-P-001990\|QX-P-002038", "owner_id": "QX-P-001990", "owner_card_rev": "431df874aac63e3f", "other_id": "QX-P-002038", "other_card_rev": "f90af92266bbd252", "relation": "相关但不等价", "basis": "1990 固定三维、以六条杆的连续刚体逃逸定义困笼；2038 是高维凸体的投影面积数量级，原帖固定二阶矩归一化。维数、动力学条件及目标量完全不同。", "assigned": true, "review_scope": "随包双方现版正文已读并逐项比较；没有仅凭索引标题判同题", "action": "仅报告，不合并、不改线上"} |
| QX-P-001993 | {"pair_id": "QX-P-001666\|QX-P-001993", "owner_id": "QX-P-001993", "owner_card_rev": "6949d1d8e146bbda", "other_id": "QX-P-001666", "other_card_rev": "dc92111bc5da9521", "relation": "相关但不等价", "basis": "1993 求无截面光滑真 Z-概形的最小相对维数；1666 问处处局部点但无整体点的存在性，另加局部条件且不求最小维数。", "source": "指定对子；已读双方随包现版正文", "owner_source": "tasks.jsonl", "other_source": "../查重参考题卡.jsonl", "online_merge_performed": false, "assigned": true, "action": "仅报告；不合并、不改线上"} |
| QX-P-001994 | {"pair_id": "QX-P-001994\|QX-P-002271", "owner_id": "QX-P-001994", "owner_card_rev": "ce94070932e4310e", "other_id": "QX-P-002271", "other_card_rev": "bd4740ab518c054b", "relation": "相关但不等价", "basis": "1994 是平面整圆/圆环在所有中心的满测度问题；2271 是高维 Bochner–Riesz 傅里叶乘子的估计，命题、维数和结论均不同。", "source": "指定对子；已读双方随包现版正文", "owner_source": "tasks.jsonl", "other_source": "../查重参考题卡.jsonl", "online_merge_performed": false, "assigned": true, "action": "仅报告；不合并、不改线上"} |
| QX-P-001994 | {"pair_id": "QX-P-001994\|QX-P-002358", "owner_id": "QX-P-001994", "owner_card_rev": "ce94070932e4310e", "other_id": "QX-P-002358", "other_card_rev": "4109c92b03d006f9", "relation": "相关但不等价", "basis": "1994 是 R² 中所有中心的整圆及满 Lebesgue 测度；2358 是 n≥4 的方向线段 Kakeya 集满 Minkowski 维数，几何对象及测度/维数结论不等价。", "source": "指定对子；已读双方随包现版正文", "owner_source": "tasks.jsonl", "other_source": "../查重参考题卡.jsonl", "online_merge_performed": false, "assigned": true, "action": "仅报告；不合并、不改线上"} |
| QX-P-001995 | {"pair_id": "QX-P-001995\|QX-P-002500", "owner_id": "QX-P-001995", "owner_card_rev": "e1c8bf77ee00052b", "other_id": "QX-P-002500", "other_card_rev": "18f9bcef315b745a", "relation": "相关但不等价", "basis": "1995 是具体 q-多项式系数非负性；2500 是 ζ(5) 无理性及相关声明。即使出现共同作者名也不构成同题。", "source": "指定对子；已读双方随包现版正文", "owner_source": "tasks.jsonl", "other_source": "../查重参考题卡.jsonl", "online_merge_performed": false, "assigned": true, "action": "仅报告；不合并、不改线上"} |
| QX-P-002015 | {"pair_id": "QX-P-001986\|QX-P-002015", "owner_id": "QX-P-002015", "owner_card_rev": "0f78ce001d7fc0e8", "other_id": "QX-P-001986", "other_card_rev": "00b8701da1d461f7", "relation": "同题", "basis": "两卡均为 C 中仿射代数集含 Zariski 稠密 Q̄ 点则定义于 Q̄；原始交叉题均指向 MO428384/Sawin428394，现版正文均已读。", "source": "全库索引触发的新候选；双方现版全文与原证明复核", "owner_source": "tasks.jsonl", "other_source": "../任务.jsonl", "online_merge_performed": false, "assigned": false, "action": "仅报告；不合并、不改线上"} |
| QX-P-002019 | {"pair_id": "QX-P-002019\|QX-P-002254", "owner_id": "QX-P-002019", "owner_card_rev": "f896657197e906d5", "other_id": "QX-P-002254", "other_card_rev": "6688a12aee6911d6", "relation": "相关但不等价", "basis": "2019 要固定边图、边长、角亏下的凸多面体唯一性；2254 要单面型凸多面体的分类，所给数据和结论均不同。", "source": "指定对子；已读双方随包现版正文", "owner_source": "tasks.jsonl", "other_source": "../查重参考题卡.jsonl", "online_merge_performed": false, "assigned": true, "action": "仅报告；不合并、不改线上"} |
| QX-P-002021 | {"pair_id": "QX-P-001373\|QX-P-002021", "owner_id": "QX-P-002021", "owner_card_rev": "ec137200b146945b", "other_id": "QX-P-001373", "other_card_rev": "88778bbd4eedaa49", "relation": "相关但不等价", "basis": "2021 研究全部对角线分割的最大单元面积；1373 研究正多边形边向量随机排列形成简单多边形的概率，与该固定排列面积问题不同。", "source": "指定对子；已读双方随包现版正文", "owner_source": "tasks.jsonl", "other_source": "../查重参考题卡.jsonl", "online_merge_performed": false, "assigned": true, "action": "仅报告；不合并、不改线上"} |
| QX-P-002025 | {"pair_id": "QX-P-002025\|QX-P-002115", "owner_id": "QX-P-002025", "owner_card_rev": "6162792a082e281f", "other_id": "QX-P-002115", "other_card_rev": "a3b0771e26a17812", "relation": "相关但不等价", "basis": "2025 是有限群类和在不可约表示上的标量分离；2115 是 Riemannian covering 的 Laplace 谱间隙。仅“特征值”共同词，量词、对象和结论不同。", "review_scope": "已比较随包两卡现版题面/原文摘录；不重复深审参考卡全部历史附件。", "source": "查重参考题卡.jsonl", "action": "仅报告；未合并、未改线上", "assigned": true} |
| QX-P-002026 | {"pair_id": "QX-P-002026\|QX-P-002080", "owner_id": "QX-P-002026", "owner_card_rev": "1a5ebabaf613134c", "other_id": "QX-P-002080", "other_card_rev": "284ef83bf653d0c9", "relation": "相关但不等价", "basis": "2080 问 S²×S² 的 exotic 光滑结构存在性；2026 要同一 X 的标准/扭接 double 并满足边界延拓条件，不能从一般 exotic 结构存在直接推出。", "review_scope": "已比较随包两卡现版题面/原文摘录；不重复深审参考卡全部历史附件。", "source": "查重参考题卡.jsonl", "action": "仅报告；未合并、未改线上", "assigned": true} |
| QX-P-002026 | {"pair_id": "QX-P-002026\|QX-P-002469", "owner_id": "QX-P-002026", "owner_card_rev": "1a5ebabaf613134c", "other_id": "QX-P-002469", "other_card_rev": "cc4ede605134dba2", "relation": "相关但不等价", "basis": "2469 核 smooth 4D Poincaré 的全称声明；2026 允许一般 4-manifold 的 doubles。AC cork 子类由 Cor.1.17 与同伦球相连，但不构成一般两题等价。", "review_scope": "已比较随包两卡现版题面/原文摘录；不重复深审参考卡全部历史附件。", "source": "查重参考题卡.jsonl", "action": "仅报告；未合并、未改线上", "assigned": true} |
| QX-P-002026 | {"pair_id": "QX-P-002026\|QX-P-002471", "owner_id": "QX-P-002026", "owner_card_rev": "1a5ebabaf613134c", "other_id": "QX-P-002471", "other_card_rev": "6a19322796118183", "relation": "相关但不等价", "basis": "2471 为 smooth Schoenflies：S³⊂S⁴ 两侧是否标准 B⁴；2026 是预先指定 X 及边界 τ 的双倍光滑类型比较。", "review_scope": "已比较随包两卡现版题面/原文摘录；不重复深审参考卡全部历史附件。", "source": "查重参考题卡.jsonl", "action": "仅报告；未合并、未改线上", "assigned": true} |
| QX-P-002032 | {"pair_id": "QX-P-002032\|QX-P-002360", "owner_id": "QX-P-002032", "owner_card_rev": "f80f27afc7d1fa2d", "other_id": "QX-P-002360", "other_card_rev": "3d372a96094424a0", "relation": "相关但不等价", "basis": "2360 是中心对称 d-polytope 的 Kalai 3^d 面数下界；2032 问面格自同构是否与对跖交换，数量不等式与群作用性质不同。", "review_scope": "已比较随包两卡现版题面/原文摘录；不重复深审参考卡全部历史附件。", "source": "查重参考题卡.jsonl", "action": "仅报告；未合并、未改线上", "assigned": true} |
| QX-P-002036 | {"pair_id": "QX-P-002036\|QX-P-002169", "owner_id": "QX-P-002036", "owner_card_rev": "9d659963adbc713b", "other_id": "QX-P-002169", "other_card_rev": "d807a40adc752ec7", "relation": "待定", "basis": "2169 的参考卡仅称 Hausdorff gauge 函数取值的四个问题，未给四问完整形式。可见内容与实加法子群谱不同，但材料不足以作严格同题/不同题最终判定。", "review_scope": "已比较随包两卡现版题面/原文摘录；不重复深审参考卡全部历史附件。", "source": "查重参考题卡.jsonl", "action": "仅报告；未合并、未改线上", "assigned": true} |
| QX-P-002036 | {"pair_id": "QX-P-002036\|QX-P-002177", "owner_id": "QX-P-002036", "owner_card_rev": "9d659963adbc713b", "other_id": "QX-P-002177", "other_card_rev": "393d712b851e12d0", "relation": "待定", "basis": "2177 为某树原则的 Hausdorff dimension 版本，参考题面缺少完整原则及量词。标题相似不足以判与实加法子群的中间维排除等价。", "review_scope": "已比较随包两卡现版题面/原文摘录；不重复深审参考卡全部历史附件。", "source": "查重参考题卡.jsonl", "action": "仅报告；未合并、未改线上", "assigned": true} |
| QX-P-002036 | {"pair_id": "QX-P-002036\|QX-P-002183", "owner_id": "QX-P-002036", "owner_card_rev": "9d659963adbc713b", "other_id": "QX-P-002183", "other_card_rev": "062bfae24d996910", "relation": "相关但不等价", "basis": "2183 讨论 profinite 群的维数类实现及描述复杂度；2036 是 R 的加法子群及其所有子群维数。ambient 群、度量和目标性质不同；参考卡细节未外部深核。", "review_scope": "已比较随包两卡现版题面/原文摘录；不重复深审参考卡全部历史附件。", "source": "查重参考题卡.jsonl", "action": "仅报告；未合并、未改线上", "assigned": true} |
| QX-P-002039 | {"pair_id": "QX-P-002039\|QX-P-002478", "owner_id": "QX-P-002039", "owner_card_rev": "4c9986227a01d647", "other_id": "QX-P-002478", "other_card_rev": "75ff62b0e87f0fe1", "relation": "相关但不等价", "basis": "2478 为有限三项复指数和 2^(−1−it)+3^(−1−it)+5^(−1−it) 的实 t 零点；2039 为无限 Euler product 的解析延拓。有限/无限、零点/边界延拓不同。", "review_scope": "已比较随包两卡现版题面/原文摘录；不重复深审参考卡全部历史附件。", "source": "查重参考题卡.jsonl", "action": "仅报告；未合并、未改线上", "assigned": true} |
| QX-P-002051 | {"pair_id": "QX-P-002051\|QX-P-002151", "owner_id": "QX-P-002051", "owner_card_rev": "5a09d3d2ff10a284", "other_id": "QX-P-002151", "other_card_rev": "bdbbe7ee3e44ce36", "relation": "相关但不等价", "basis": "2151 要 F 的具体悖论分解，属于非 amenability 后的显式构造问题；2051 原帖宽问假设 amenability 的后果。非 amenability 的存在性声明不自动提供指定显式分解。", "review_scope": "已比较随包两卡现版题面/原文摘录；不重复深审参考卡全部历史附件。", "source": "查重参考题卡.jsonl", "action": "仅报告；未合并、未改线上", "assigned": true} |
| QX-P-002051 | {"pair_id": "QX-P-002051\|QX-P-002386", "owner_id": "QX-P-002051", "owner_card_rev": "5a09d3d2ff10a284", "other_id": "QX-P-002386", "other_card_rev": "ce0de649f367f1eb", "relation": "相关但不等价", "basis": "2386 为 Thompson F 是否 automatic（Kourovka 21.143）；自动结构与 amenability 的问题不同。", "review_scope": "已比较随包两卡现版题面/原文摘录；不重复深审参考卡全部历史附件。", "source": "查重参考题卡.jsonl", "action": "仅报告；未合并、未改线上", "assigned": true} |
| QX-P-002051 | {"pair_id": "QX-P-002051\|QX-P-002477", "owner_id": "QX-P-002051", "owner_card_rev": "5a09d3d2ff10a284", "other_id": "QX-P-002477", "other_card_rev": "45caaca857ed42f7", "relation": "相关但不等价", "basis": "2477 已记录 OpenAI 2026 非 amenability 证明声明及核验；2051 原问是假设 amenability 的后果。应交叉链接并同步背景，不能合并软问题与“一题一验”的证明审查。", "review_scope": "已比较随包两卡现版题面/原文摘录；不重复深审参考卡全部历史附件。", "source": "查重参考题卡.jsonl", "action": "仅报告；未合并、未改线上", "assigned": true} |
| QX-P-002070 | {"other_id": "QX-P-001390", "other_card_rev": "13c0b3969485f865", "other_title": "Somer广义Fibonacci商的同余", "relation": "相关但不等价", "basis": "对方G_n=F_dn/F_n研究奇素数模下的同余。取d=a,n=a^k仅让表达式相接，不能把同余问题等同于本题商为素数的分类。", "source": "指定查重配对.jsonl 与 查重参考题卡.jsonl", "comparison_scope": "已读指定对子的随包完整题卡；未另作对方全题联网查新", "merge_recommended": false, "owner_id": "QX-P-002070", "owner_card_rev": "926d417463a2889d", "pair_id": "QX-P-001390\|QX-P-002070", "assigned": true, "action": "仅报告；不合并、不改线上"} |
| QX-P-002070 | {"other_id": "QX-P-001776", "other_card_rev": "071ff71fc9a3787c", "other_title": "两个Fibonacci数的平方和", "relation": "相关但不等价", "basis": "对方问F_n²+F_m²是否为平方；本题问幂指标商的素性。没有双向归约证据。", "source": "指定查重配对.jsonl 与 查重参考题卡.jsonl", "comparison_scope": "已读指定对子的随包完整题卡；未另作对方全题联网查新", "merge_recommended": false, "owner_id": "QX-P-002070", "owner_card_rev": "926d417463a2889d", "pair_id": "QX-P-001776\|QX-P-002070", "assigned": true, "action": "仅报告；不合并、不改线上"} |
| QX-P-002070 | {"other_id": "QX-P-002242", "other_card_rev": "d26ae49dfc6a4c8a", "other_title": "Fibonacci倒数展开最终周期性", "relation": "相关但不等价", "basis": "对方为有理数的展开周期性；本题为整除商素性，仅共享Fibonacci词。", "source": "指定查重配对.jsonl 与 查重参考题卡.jsonl", "comparison_scope": "已读指定对子的随包完整题卡；未另作对方全题联网查新", "merge_recommended": false, "owner_id": "QX-P-002070", "owner_card_rev": "926d417463a2889d", "pair_id": "QX-P-002070\|QX-P-002242", "assigned": true, "action": "仅报告；不合并、不改线上"} |
| QX-P-002074 | {"other_id": "QX-P-002276", "other_card_rev": "2c5ba57d07cebb99", "other_title": "Clifford/Chekanov单调Lagrange环面", "relation": "相关但不等价", "basis": "对方是C²中Hamilton同痕分类；Clifford名称不构成Clifford代数乘积还原问题的等价。参考卡正文还明确排除002074。", "source": "指定查重配对.jsonl 与 查重参考题卡.jsonl", "comparison_scope": "已读指定对子的随包完整题卡；未另作对方全题联网查新", "merge_recommended": false, "owner_id": "QX-P-002074", "owner_card_rev": "ff0421039a708e76", "pair_id": "QX-P-002074\|QX-P-002276", "assigned": true, "action": "仅报告；不合并、不改线上"} |

## 降级和冲突说明（32）

| 题号 | 说明 |
|---|---|
| QX-P-001971 | 子问 X=R 时 U≅int(cl U) 是否迫使相等：提议"原题已推翻"，待二审 |
| QX-P-001974 | 子问 R³ 的 8 点、R⁴ 的 16 点等距构型存在性：提议"原题已推翻"，待二审 |
| QX-P-001975 | 子问 m∈E 时 ±2m³、±32m³ 不可表示：提议"原题已证明"，待二审 |
| QX-P-001976 | 证据 本轮支撑间隔核算：缺直接链接或原文定位，不进摘要 |
| QX-P-001976 | 子问 原问连续严格正非常数解存在性：提议"原题已证明"，待二审 |
| QX-P-001976 | 子问 旧卡所谓残余 C1 存在性：提议"原题已证明"，待二审 |
| QX-P-001978 | 子问 紧伪度量空间的下半连续实像必 Borel：提议"原题已推翻"，待二审 |
| QX-P-001985 | 证据 本轮整数及代数核算：缺直接链接或原文定位，不进摘要 |
| QX-P-001986 | 证据 本包2015当前正文：缺直接链接或原文定位，不进摘要 |
| QX-P-001986 | 子问 稠密 F 点强制代数集定义于 F：提议"原题已证明"，待二审 |
| QX-P-001998 | 子问 相关变体：若 N_p(α)>1，是否必为 2 的幂：提议"原题已推翻"，待二审 |
| QX-P-002015 | 子问 稠密 Q̄ 点推出 Q̄ 定义：提议"原题已证明"，待二审 |
| QX-P-002016 | 子问 旧卡 S(n)=A126776(n) 的识别：提议"原题已推翻"，待二审 |
| QX-P-002030 | 子问 W=Sₙ 的 hard Lefschetz 性质：提议"原题已证明"，待二审 |
| QX-P-002033 | 子问 球面三维空间形式光滑嵌入 S⁴ 的分类：提议"原题已证明"，待二审 |
| QX-P-002033 | 子问 是否有无穷多个此类光滑嵌入空间形式：提议"原题已推翻"，待二审 |
| QX-P-002033 | 子问 允许 locally flat TOP 嵌入的变体：提议"原题已证明"，待二审 |
| QX-P-002035 | 子问 长度小于 cov(B)，特别是可数链的子情形：提议"原题已推翻"，待二审 |
| QX-P-002049 | 证据 本轮自写枚举：n=3,4,5 的非 Hamilton 简单图：缺直接链接或原文定位，不进摘要 |
| QX-P-002049 | 子问 n=3,4,5 的 ordered Hamilton 路径最大数：提议"原题已证明"，待二审 |
| QX-P-002053 | 子问 按标准群胚 cocycle 定义，Haefliger 结构与主 Γ^q 丛的对应：提议"原题已证明"，待二审 |
| QX-P-002054 | 子问 允许向量值双变量 φ(x0,xp) 时是否存在连续表示：提议"原题已证明"，待二审 |
| QX-P-002055 | 子问 互素实多项式在原点同有孤立零点，商能否在原点 C∞ 延拓：提议"原题已推翻"，待二审 |
| QX-P-002060 | 子问 除6和10外是否有例子：提议"原题已证明"，待二审 |
| QX-P-002061 | 子问 所有I是否均可实现，及可允许I是否成布尔代数：提议"原题已推翻"，待二审 |
| QX-P-002063 | 子问 κ完备、常结构、\|A\|<κ的情形：提议"原题已证明"，待二审 |
| QX-P-002063 | 子问 原帖Final case中 π0 导出的映射为满射：提议"原题已推翻"，待二审 |
| QX-P-002065 | 子问 阶4的指定非自逆类元素满足\|C_G(x)\|为平方：提议"原题已证明"，待二审 |
| QX-P-002069 | 子问 初值(0,0),(2,0),(4,1)经规定90°跳跃能否共线：提议"原题已证明"，待二审 |
| QX-P-002074 | 子问 n=1不允许标量前因子的字面命题：提议"原题已推翻"，待二审 |
| QX-P-002075 | 子问 通常R^n拓扑上是否存在不同/异域光滑结构仍使加法和取负光滑：提议"原题已推翻"，待二审 |
| QX-P-002077 | 子问 全部系数正的多项式所有足够高次幂的系数是否单峰：提议"原题已证明"，待二审 |

