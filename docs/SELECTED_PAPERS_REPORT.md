# Statistics × LLM Scholar Research Explorer

核查日期：2026-10-28。主库 40 篇，覆盖截图中的 11 位学者：RLHF 与偏好优化 16、LLM Unlearning 12、水印与 AI 文本检测 12。

## 选择与证据口径

以指定学者为入口，保留能区分重要研究问题、统计方法或评估失败模式的代表文章；不是他们的完整发表目录。合著只计一篇，可同时归属于多位学者。每个人物卡片均提供完整发表列表入口。

所有精选记录均读取 arXiv 原始题名、作者、摘要。正式发表优先依据 proceedings 或期刊记录；作者主页与 arXiv 接收声明单独标记。修回不等于接收。全文定理条件、证明与实验数值未逐项审计。研究建议是待核查提议，不声称已发现无人研究的空白。

研究类型只保留 Method / Theory / Theory + Method。两篇综述的标签表示覆盖内容，不表示同时贡献新算法和新定理。Sharpness-Aware Machine Unlearning 是一般机器遗忘理论补充，不当作已验证的 LLM 专用方法。RLVR 与 RLHF 紧密相关，但不等同于人类反馈学习。

水印检测需要具体机制、密钥和 pivot 假设；通用检测使用模型概率、训练样本或其他统计特征。改写鲁棒保证不涵盖任意语义重写。水印比例是存活信号比例，不能无条件当作 AI 创作比例；定位存活信号也不是逐词真实作者证明。

## 旧库与个人记录

原主库保留 p01（DRPO）、p38（LoCo-RLHF）、n13（GRU），分别代表双重稳健、异质低秩奖励和遗忘—保留冲突。其余 27 篇移入 archive，与原有 28 篇合为 55 篇。转出依据主要是本轮学者与主题范围变化，不意味着论文不存在或质量低。

原主库及 archive 共 58 个 ID 全部保留，没有将旧 ID 用于其他论文。localStorage key 保持兼容，主库与归档笔记可查看、编辑和统一导出。不会读取或修改用户真实浏览器记录。此前选择说明见 [prior_selection_report.md](scholar-explorer-2026-10-28/prior_selection_report.md)。

`papers.json` 是主库唯一权威数据源，CSV 与 HTML 为生成副本。`scholars.json` 仅保存人物资料、主页及推荐 ID；归档原始记录保存在 `papers_archive.json`。

## 需要继续核实

- 统计 RLHF 综述：Sun 主页称 Annual Review，Shi 主页仍列预印本；正式刊页未核实。
- 部分 2026 接收状态依赖作者主页或 arXiv 声明，逐篇注明，未冒充正式发表。
- Human Edits 水印论文以 2026 卷 88(2) 为列表年份，同时注明 2025 在线发表。
- 部分出版社及 OpenReview 自动访问受 403/挑战页限制，保留原始链接并使用可访问的 arXiv 版本分析。详见 publication_http_checks.json。
- 未核实 CCF 官方目录，不给会议标注未经确认的等级；Findings 与 workshop 不标成主会。
- 本轮没有运行论文复现实验或证明审计。

## 七个探索性研究问题

网站为每项列出意义、统计方法、难度、代表论文和未验证条件：错设与覆盖不足下的偏好评价；标注预算与奖励置信区间；RLVR 采样预算和共享；遗忘评价的不确定性；优化几何与抗恢复；改写后水印检测与定位；通用检测的低误报和分布偏移。

## Scholar coverage and first reads

| Scholar | Official homepage | Count | Recommended |
|---|---|---:|---|
| Chengchun Shi | [LSE](https://callmespring.github.io/) | 9 | [Doubly Robust Alignment for Large Language Models](https://arxiv.org/abs/2506.01183); [Dual Active Learning for Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2410.02504); [Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic](https://arxiv.org/abs/2603.01162) |
| Jiancong Xiao | [NUS](https://jiancongxiao.github.io/) | 3 | [On the Algorithmic Bias of Aligning Large Language Models with RLHF: Preference Collapse and Matching Regularization](https://arxiv.org/abs/2405.16455); [Statistical Impossibility and Possibility of Aligning LLMs with Human Preferences: From Condorcet Paradox to Nash Equilibrium](https://arxiv.org/abs/2503.10990); [Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach](https://arxiv.org/abs/2505.01997) |
| Will Wei Sun | [Purdue](https://web.ics.purdue.edu/~sun244/) | 5 | [Low-Rank Contextual Reinforcement Learning from Heterogeneous Human Feedback](https://arxiv.org/abs/2412.19436); [Uncertainty Quantification for Large Language Model Reward Learning under Heterogeneous Human Feedback](https://arxiv.org/abs/2512.03208); [Dual Active Learning for Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2410.02504) |
| Tong Zhang | [UIUC / ML theory](https://www.tongzhang-ml.org/) | 3 | [Iterative Preference Learning from Human Feedback: Bridging Theory and Practice for RLHF under KL-Constraint](https://arxiv.org/abs/2312.11456); [Online Iterative Reinforcement Learning from Human Feedback with General Preference Model](https://arxiv.org/abs/2402.07314); [RM-R1: Reward Modeling as Reasoning](https://arxiv.org/abs/2505.02387) |
| Sijia Liu | [MSU / OPTML](https://lsjxjtu.github.io/) | 5 | [Rethinking Machine Unlearning for Large Language Models](https://arxiv.org/abs/2402.08787); [Simplicity Prevails: Rethinking Negative Preference Optimization for LLM Unlearning](https://arxiv.org/abs/2410.07163); [Towards LLM Unlearning Resilient to Relearning Attacks: A Sharpness-Aware Minimization Perspective and Beyond](https://arxiv.org/abs/2502.05374) |
| Haoran Tang | [Purdue CS](https://haorantang.github.io/) | 2 | [Contrastive Representation Shaping for LLM Unlearning](https://arxiv.org/abs/2601.22028); [Sharpness-Aware Machine Unlearning](https://arxiv.org/abs/2506.13715) |
| Qizhou Wang | [RIKEN AIP](https://qizhouwang.github.io/homepage/) | 5 | [Towards Effective Evaluations and Comparisons for LLM Unlearning Methods](https://arxiv.org/abs/2406.09179); [Rethinking LLM Unlearning Objectives: A Gradient Perspective and Go Beyond](https://arxiv.org/abs/2502.19301); [GRU: Mitigating the Trade-off between Unlearning and Retention for LLMs](https://arxiv.org/abs/2503.09117) |
| Puning Yang | [MBZUAI](https://puning97.github.io/) | 3 | [Exploring Criteria of Loss Reweighting to Enhance LLM Unlearning](https://arxiv.org/abs/2505.11953); [Distinguishable Deletion: Unifying Knowledge Erasure and Refusal for Large Language Model Unlearning](https://arxiv.org/abs/2605.16776); [Towards Effective Evaluations and Comparisons for LLM Unlearning Methods](https://arxiv.org/abs/2406.09179) |
| Guangsheng Bao | [Fuyao / formerly Westlake](https://baoguangsheng.github.io/) | 3 | [Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature](https://arxiv.org/abs/2310.05130); [Glimpse: Enabling White-Box Methods to Use Proprietary Models for Zero-Shot LLM-Generated Text Detection](https://arxiv.org/abs/2412.11506); [Decoupling Content and Expression: Two-Dimensional Detection of AI-Generated Text](https://arxiv.org/abs/2503.00258) |
| Chenwang Wu | [HKBU / USTC](https://daftstone.github.io/) | 2 | [Beyond Raw Detection Scores: Markov-Informed Calibration for Boosting Machine-Generated Text Detection](https://arxiv.org/abs/2602.08031); [Advancing Machine-Generated Text Detection from an Easy to Hard Supervision Perspective](https://arxiv.org/abs/2511.00988) |
| Xiang Li | [Penn DBEI](https://lx10077.github.io/) | 5 | [A Statistical Framework of Watermarks for Large Language Models: Pivot, Detection Efficiency and Optimal Rules](https://arxiv.org/abs/2404.01245); [Robust Detection of Watermarks for Large Language Models Under Human Edits](https://arxiv.org/abs/2411.13868); [Optimal Watermark Localization in Mixed-Source Large Language Model Texts](https://arxiv.org/abs/2608.14906) |

## Selected bibliography

| ID | Paper | Venue / year | Publication evidence | Selection rationale |
|---|---|---|---|---|
| p01 | [Doubly Robust Alignment for Large Language Models](https://arxiv.org/abs/2506.01183) | NeurIPS 2025 | [已发表：正式会议页核查](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0a226473989931ec6f6ced7343542f86-Abstract-Conference.html) | 把半参数双重稳健思想用于偏好评价和优化，放宽两类模型同时正确的要求。 |
| s250403784 | [Robust Reinforcement Learning from Human Feedback for Large Language Models Fine-Tuning](https://arxiv.org/abs/2504.03784) | AoAS 2026 | [作者主页列入 accepted manuscripts；正式刊页未核实](https://callmespring.github.io/publication) | 将奖励错设与估计方差联系起来，并据此改进优化。 |
| s241002504 | [Dual Active Learning for Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2410.02504) | Operations Research 2026 | [作者主页列为 2026 已接收/发表；正式刊页未核实](https://web.ics.purdue.edu/~sun244/research.html) | 把数据选择和标注者选择组成双重主动学习。 |
| s260402507 | [Reinforcement Learning from Human Feedback: A Statistical Perspective](https://arxiv.org/abs/2604.02507) | Annual Review / 待核实 2026 | [Sun 主页称 Annual Review；Shi 主页仍列预印本，正式刊页未核实](https://web.ics.purdue.edu/~sun244/research.html) | 提供综述与教学示例；不是宣称提出一个新的统一最优算法。 |
| s260301162 | [Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic](https://arxiv.org/abs/2603.01162) | arXiv 2026 | [预印本；未核实正式发表](https://arxiv.org/abs/2603.01162) | 为 MSE、有限样本误差、渐近分布及组大小选择提供统一分析视角。 |
| s260428005 | [Kernelized Advantage Estimation: From Nonparametric Statistics to LLM Reasoning](https://arxiv.org/abs/2604.28005) | arXiv 2026 | [预印本；未核实正式发表](https://arxiv.org/abs/2604.28005) | 用经典非参数估计在有限 rollout 预算下共享信息。 |
| s260527293 | [BASIS: Batchwise Advantage Estimation from Single-Rollout Information Sharing for LLM Reasoning](https://arxiv.org/abs/2605.27293) | EMNLP Findings 2026 | [作者主页称已接收；正式 proceedings 页未核实](https://callmespring.github.io/publication) | 提出不训练 critic、每提示单 rollout 的后训练算法。 |
| p38 | [Low-Rank Contextual Reinforcement Learning from Heterogeneous Human Feedback](https://arxiv.org/abs/2412.19436) | JASA 2026 | [已发表：期刊记录核查](https://www.tandfonline.com/doi/abs/10.1080/01621459.2026.2674413) | LoCo-RLHF 将个性化上下文结构与低秩统计估计结合。 |
| s251203208 | [Uncertainty Quantification for Large Language Model Reward Learning under Heterogeneous Human Feedback](https://arxiv.org/abs/2512.03208) | arXiv 2025 | [预印本；未核实正式发表](https://arxiv.org/abs/2512.03208) | 把异质偏好下的奖励估计与 UQ、奖励比较和 BoN 决策连接起来。 |
| s260322563 | [Privacy-Preserving Reinforcement Learning from Human Feedback via Decoupled Reward Modeling](https://arxiv.org/abs/2603.22563) | SLADS / 作者报告 2026 | [作者主页列为 SLADS 2026；正式刊页未核实](https://web.ics.purdue.edu/~sun244/research.html) | 把隐私预算配置与奖励/策略阶段的结构区分开来。 |
| s240516455 | [On the Algorithmic Bias of Aligning Large Language Models with RLHF: Preference Collapse and Matching Regularization](https://arxiv.org/abs/2405.16455) | JASA 2025 | [已接收：arXiv 注释及作者主页；期刊链接保留](https://www.tandfonline.com/doi/abs/10.1080/01621459.2025.2555067) | 区分奖励最大化与偏好分布匹配，提出明确的匹配目标。 |
| s250310990 | [Statistical Impossibility and Possibility of Aligning LLMs with Human Preferences: From Condorcet Paradox to Nash Equilibrium](https://arxiv.org/abs/2503.10990) | Annals of Statistics 2026 | [已接收：arXiv 注释及作者主页；正式刊页未核实](https://jiancongxiao.github.io/publications/) | 给出对齐可表示性与多样偏好保留的限制和可能性。 |
| s250501997 | [Restoring Calibration for Aligned Large Language Models: A Calibration-Aware Fine-Tuning Approach](https://arxiv.org/abs/2505.01997) | ICML 2025 | [已发表：正式会议页核查](https://proceedings.mlr.press/v267/xiao25b.html) | 把对齐、任务性能和校准误差一起分析。 |
| s231211456 | [Iterative Preference Learning from Human Feedback: Bridging Theory and Practice for RLHF under KL-Constraint](https://arxiv.org/abs/2312.11456) | ICML 2024 | [已发表：正式会议页核查](https://proceedings.mlr.press/v235/xiong24a.html) | 把探索与数据覆盖显式纳入 RLHF 理论及算法。 |
| s240207314 | [Online Iterative Reinforcement Learning from Human Feedback with General Preference Model](https://arxiv.org/abs/2402.07314) | NeurIPS 2024 | [已发表：正式会议页核查](https://papers.nips.cc/paper_files/paper/2024/hash/94d13c2401fe119e57ba325b6fe526e0-Abstract-Conference.html) | 绕开潜在标量奖励存在的假设，分析离线及在线可学习性。 |
| s250502387 | [RM-R1: Reward Modeling as Reasoning](https://arxiv.org/abs/2505.02387) | ICLR 2026 | [已发表：正式会议页核查](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8e3b8de251afd887fb4589c1e3a3c793-Abstract-Conference.html) | 将奖励建模改写为可解释的生成式推理任务。 |
| s240208787 | [Rethinking Machine Unlearning for Large Language Models](https://arxiv.org/abs/2402.08787) | Nature Machine Intelligence 2025 | [已发表：期刊记录核查](https://www.nature.com/articles/s42256-025-00985-0) | 建立概念地图并提示容易被忽视的多面评估问题；属于综述。 |
| s241007163 | [Simplicity Prevails: Rethinking Negative Preference Optimization for LLM Unlearning](https://arxiv.org/abs/2410.07163) | NeurIPS 2025 | [已发表：正式会议页核查](https://proceedings.neurips.cc/paper_files/paper/2025/hash/02443e4e008231e0af0855f3cc70ed17-Abstract-Conference.html) | 揭示 reference bias 和难度不均带来的权重问题。 |
| s250205374 | [Towards LLM Unlearning Resilient to Relearning Attacks: A Sharpness-Aware Minimization Perspective and Beyond](https://arxiv.org/abs/2502.05374) | ICML 2025 | [已发表：正式会议页核查](https://proceedings.mlr.press/v267/fan25e.html) | 把 relearning attack 与损失景观平滑联系起来。 |
| s251009007 | [LLM Unlearning on Noisy Forget Sets: A Study of Incomplete, Rewritten, and Watermarked Data](https://arxiv.org/abs/2510.09007) | AISec Workshop 2025 | [已接收：arXiv 注释与作者主页；不是 CCS 主会论文](https://lsjxjtu.github.io/publications.html) | 把真实可获得的遗忘数据质量纳入评估。 |
| s240609179 | [Towards Effective Evaluations and Comparisons for LLM Unlearning Methods](https://arxiv.org/abs/2406.09179) | ICLR 2025 | [已发表：正式会议页核查](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3a91841d2bcc0b13a3d0d5d60c9f0581-Abstract-Conference.html) | 强调指标可靠性及比较基准的可比性。 |
| n13 | [GRU: Mitigating the Trade-off between Unlearning and Retention for LLMs](https://arxiv.org/abs/2503.09117) | ICML 2025 | [已发表：正式会议页核查](https://proceedings.mlr.press/v267/wang25de.html) | 将保留损害控制纳入遗忘更新规则。 |
| s250511953 | [Exploring Criteria of Loss Reweighting to Enhance LLM Unlearning](https://arxiv.org/abs/2505.11953) | ICML 2025 | [已发表：正式会议页核查](https://proceedings.mlr.press/v267/yang25ak.html) | 通过可分解实验研究权重的目标、平滑度和粒度。 |
| s260516776 | [Distinguishable Deletion: Unifying Knowledge Erasure and Refusal for Large Language Model Unlearning](https://arxiv.org/abs/2605.16776) | ICML 2026 | [已发表：正式会议页核查](https://proceedings.mlr.press/v306/yang26dc.html) | 把知识分离与拒答连接为可操作框架。 |
| s260122028 | [Contrastive Representation Shaping for LLM Unlearning](https://arxiv.org/abs/2601.22028) | NeurIPS 2026 | [已接收：arXiv 注释和作者主页；正式 proceedings 未核实](https://haorantang.github.io/) | 将表征纠缠作为遗忘算法的可测诊断和改进目标。 |
| s250613715 | [Sharpness-Aware Machine Unlearning](https://arxiv.org/abs/2506.13715) | ICLR 2026 | [已发表：正式会议页核查](https://proceedings.iclr.cc/paper_files/paper/2026/hash/815d50638e46b7f3bdaaae2158c68d54-Abstract-Conference.html) | 把遗忘集和保留集的优化几何分开讨论。 |
| s250219301 | [Rethinking LLM Unlearning Objectives: A Gradient Perspective and Go Beyond](https://arxiv.org/abs/2502.19301) | ICLR 2025 | [已发表：正式会议页核查](https://proceedings.iclr.cc/paper_files/paper/2025/hash/9ad307ab459fb93163248a0a56959307-Abstract-Conference.html) | 提供分析和诊断遗忘目标的工具。 |
| s251000761 | [Downgrade to Upgrade: Optimizer Simplification Enhances Robustness in LLM Unlearning](https://arxiv.org/abs/2510.00761) | ICLR 2026 | [作者主页列为 ICLR；正式论文 PDF 核查](https://openreview.net/pdf/a78c8e7458c059eb2cd9237d4af803b102afba7b.pdf) | 把优化器从目标函数之外单独作为鲁棒性的研究变量。 |
| s251001268 | [AdaDetectGPT: Adaptive Detection of LLM-Generated Text with Statistical Guarantees](https://arxiv.org/abs/2510.01268) | NeurIPS 2025 | [已发表：正式会议页核查](https://proceedings.neurips.cc/paper_files/paper/2025/hash/808bc5e3d076c1125a87f81b42d5e52d-Abstract-Conference.html) | 把检测规则学习与错误率分析结合起来。 |
| s260503723 | [Segmenting Human-LLM Co-authored Text via Change Point Detection](https://arxiv.org/abs/2605.03723) | STAI-X 2026 | [作者主页列为 STAI-X；正式会议页未核实](https://callmespring.github.io/publication) | 从整篇二分类走向片段定位。 |
| s240401245 | [A Statistical Framework of Watermarks for Large Language Models: Pivot, Detection Efficiency and Optimal Rules](https://arxiv.org/abs/2404.01245) | Annals of Statistics 2025 | [已发表：arXiv journal reference 与期刊 DOI 核查](https://doi.org/10.1214/24-AOS2468) | 给水印机制与检测规则提供统计比较框架。 |
| s241113868 | [Robust Detection of Watermarks for Large Language Models Under Human Edits](https://arxiv.org/abs/2411.13868) | JRSS B 2026 | [期刊记录：2025 在线发表；2026 卷 88(2), 491 起](https://academic.oup.com/jrsssb/article-abstract/88/2/491/8261309) | 在特定 Gumbel-max 水印及编辑渐近区间，建立自适应稳健检测分析。 |
| s250622343 | [Optimal Estimation of Watermark Proportions in Hybrid AI-Human Texts](https://arxiv.org/abs/2506.22343) | arXiv 2025 | [预印本；未核实正式发表](https://arxiv.org/abs/2506.22343) | 建立比例识别条件、估计器及 minimax 界。 |
| s251003944 | [On the Empirical Power of Goodness-of-Fit Tests in Watermark Detection](https://arxiv.org/abs/2510.03944) | NeurIPS 2025 | [已发表：正式会议论文核查](https://proceedings.neurips.cc/paper_files/paper/2025/file/1b19bf73c2f341a350f9bd05c204d97b-Paper-Conference.pdf) | 为经典统计检验提供有针对性的水印实证比较。 |
| s260814906 | [Optimal Watermark Localization in Mixed-Source Large Language Model Texts](https://arxiv.org/abs/2608.14906) | arXiv 2026 | [预印本；未核实正式发表](https://arxiv.org/abs/2608.14906) | 区分整篇检测、发现部分位置与一致分类的统计难度。 |
| s231005130 | [Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature](https://arxiv.org/abs/2310.05130) | ICLR 2024 | [已发表：正式会议论文与 arXiv camera version](https://openreview.net/pdf?id=Bpcgcr8E8Z) | 提供高效的概率统计检测基线。 |
| s241211506 | [Glimpse: Enabling White-Box Methods to Use Proprietary Models for Zero-Shot LLM-Generated Text Detection](https://arxiv.org/abs/2412.11506) | ICLR 2025 | [已发表：正式会议页核查](https://proceedings.iclr.cc/paper_files/paper/2025/hash/806e8e4ea77000a1486eeddeb1b90a6e-Abstract-Conference.html) | 连接 API 概率信息与原本需要更多模型访问的检测方法。 |
| s250300258 | [Decoupling Content and Expression: Two-Dimensional Detection of AI-Generated Text](https://arxiv.org/abs/2503.00258) | arXiv 2025 | [预印本；未核实正式发表](https://arxiv.org/abs/2503.00258) | 将 AI 参与写作的不同程度及表面编辑放在同一检测框架中。 |
| s251100988 | [Advancing Machine-Generated Text Detection from an Easy to Hard Supervision Perspective](https://arxiv.org/abs/2511.00988) | NeurIPS 2025 | [已发表：正式会议页核查](https://proceedings.neurips.cc/paper_files/paper/2025/hash/dce5d66bf88b7b7d0f11fbd9c9f16620-Abstract-Conference.html) | 把检测边界模糊与不精确监督纳入方法设计。 |
| s260208031 | [Beyond Raw Detection Scores: Markov-Informed Calibration for Boosting Machine-Generated Text Detection](https://arxiv.org/abs/2602.08031) | ICLR 2026 | [已发表：正式会议页核查](https://proceedings.iclr.cc/paper_files/paper/2026/hash/50b4eb974283cf1a7a60980ed06cf1be-Abstract-Conference.html) | 给现有 metric-based 检测器添加轻量分数校准模块。 |

## Additional inspected preprints (not selected)

These remain discovery candidates; overlap, recency and a bounded main collection informed selection. See the raw primary metadata for authors and abstracts.

- [Invariance Makes LLM Unlearning Resilient Even to Unanticipated Downstream Fine-Tuning](https://arxiv.org/abs/2506.01339)
- [LLM Unlearning with LLM Beliefs](https://arxiv.org/abs/2510.19422)
- [Unlearning Deceptive Behaviors in LLMs with Contrastive Forget Sets](https://arxiv.org/abs/2609.38909)
- [Detecting LLM-Generated Text with Performance Guarantees](https://arxiv.org/abs/2601.06586)
- [READER: Reasoning-Enhanced AI-Generated Text Detection](https://arxiv.org/abs/2605.25281)
- [Hidden Human-Like Nature of Machine-Generated Texts: Theory and Detection Enhancement](https://arxiv.org/abs/2605.23190)
