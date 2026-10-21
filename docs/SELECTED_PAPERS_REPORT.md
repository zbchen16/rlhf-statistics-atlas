# Statistics × LLM Alignment Research Explorer：精选文献报告

更新：2026-10-21。主库 **30 篇**：RLHF & Preference Alignment **15**，Other Alignment Methods **9**，Machine Unlearning **6**。第一方向以 RLHF 为核心，也包含 DPO 等直接偏好优化方法；两者相关，但算法流程并不相同。

## 选择标准与证据边界

优先选择重要路线的奠基论文、近期有实质方法或理论贡献的正式论文、统计联系明确的工作，以及能揭示评估失效的论文。旧 A/B/C/S 阅读优先级没有作为去留规则。同一问题的密集小变体、主要提供观点的 Position 文章和与 LLM 对齐距离较远的参照工作放入归档。

发表信息和研究问题主要核查自 [PMLR](https://proceedings.mlr.press/)、[NeurIPS proceedings](https://proceedings.neurips.cc/)、[ICLR proceedings](https://proceedings.iclr.cc/)、[ACL Anthology](https://aclanthology.org/)、JASA 出版页及 arXiv 原文。每条记录的 `verification` 说明核查深度。本轮**没有逐篇复核全文定理、证明和实验表格**，因此六问分析不声称具体常数、实验幅度或已验证的 research gap。[CCF 官方人工智能目录](https://www.ccf.org.cn/Academic_Evaluation/AI/) 用于会议分类参考；网站显示会议名称，不给论文贴未经核定的 CCF 等级。

## 三方向研究格局

### 1. RLHF 与偏好优化（15）

从 InstructGPT 的 SFT→奖励模型→RLHF 流程进入，再读 DPO 与其条件边界；随后关注 BT 假设、奖励模型质量、噪声、错设、在线探索、分布式奖励和异质反馈。最值得先读：[InstructGPT](https://proceedings.neurips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract.html)、[DPO](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract.html)、[Doubly Robust Alignment](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0a226473989931ec6f6ced7343542f86-Abstract-Conference.html)、[Beyond Bradley-Terry Models](https://proceedings.mlr.press/v267/zhang25de.html)、[Unbiased Alignment with Noisy Preferences](https://proceedings.mlr.press/v306/wang26fa.html)。

### 2. Other Alignment Methods（9）

少量论文覆盖 SFT/self-instruction、RLAIF/Constitutional AI、RLVR/GRPO、自合成对齐、安全微调、多目标偏好及推理时引导解码。优先读 [RLAIF vs. RLHF](https://proceedings.mlr.press/v235/lee24t.html)、[GRPO’s Loss](https://proceedings.mlr.press/v306/mroueh26a.html)、[Fully Self-Synthetic Data](https://aclanthology.org/2026.acl-long.1595/)、[Nudging](https://aclanthology.org/2025.acl-long.623/)。Constitutional AI 仅标为 arXiv 预印本。

### 3. Machine Unlearning（6）

集中于真正涉及语言模型的遗忘—保留权衡、评估基准、文本泄漏、概率解码和可逆性。优先读 [MUSE](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4556f5398bd2c61bd7500e306b4e560a-Abstract-Conference.html)、[GRU](https://proceedings.mlr.press/v267/wang25de.html)、[Textual Unlearning Gives a False Sense of Unlearning](https://proceedings.mlr.press/v267/du25d.html)、[Leak@$k$](https://proceedings.mlr.press/v306/reisizadeh26a.html)。没有为了覆盖 certified unlearning 而塞入传统 ML 论文；本站也不声称这些 LLM 方法提供严格删除保证。

## 原 41 篇中保留的 13 篇

| ID | 论文 | 保留原因 |
|---|---|---|
| p01 | Doubly Robust Alignment for Large Language Models | 错设下的双重稳健偏好优化 |
| p02 | Understanding the Performance Gap in Preference Learning | RLHF 与 DPO 的理论对照 |
| p03 | Beyond Bradley-Terry Models | BT 之外的偏好表达 |
| p04 | DisPPO | 分布式奖励与分位数路线 |
| p05 | Unbiased Alignment for Large Language Models with Noisy Preferences | 带噪偏好校正 |
| p06 | Distortion of AI Alignment | 偏好优化与群体福利目标差异 |
| p07 | Conditional Equivalence of DPO and RLHF | 等价条件与失败模式 |
| p08 | Avoiding exp(R) scaling in RLHF | 在线 RLHF 样本效率 |
| p09 | What Makes a Reward Model a Good Teacher? | 奖励模型与优化信号 |
| p11 | On the Robustness of Reward Models | 奖励模型稳健性 |
| p14 | Unintentional Unalignment | DPO 目标的失效诊断 |
| p15 | COMAL | 一般偏好与非传递结构 |
| p38 | Low-Rank Contextual Reinforcement Learning from Heterogeneous Human Feedback | 异质人类反馈的统计建模 |

这些旧论文保留原 ID；其正式链接在 [`papers.json`](../public/data/papers.json) 中。

## 未入选的 28 篇：逐组删除理由

原始记录逐字保存于 [`papers_archive.json`](../public/data/papers_archive.json)，主库筛除不表示这些论文不真实或无价值。

| 旧 ID | 主库未入选原因 |
|---|---|
| p10, p16 | 一般偏好和博弈路线已由 p03、p15 代表；留作扩展阅读。 |
| p12, p13, p29 | 在线 RLHF 与数据筛选方向已由 p08 及奖励模型论文提供主要入口。 |
| p17, p18, p19, p20, p21, p27, p33 | 奖励建模、shortcut 和诊断工作丰富，但与 p09、p11 所覆盖的核心问题相近；限额下归档。 |
| p22, p23, p34, p39 | 多目标和公平主题移至 Other Alignment 路线，以 n11 等代表工作建立入口。 |
| p24, p25, p26 | 群体福利、公理和个性化具有价值，但与 p06、p38 的阅读主线部分重复。 |
| p28, p30, p31, p32 | DPO 数据/目标/token 级变体；主库优先 DPO 原论文及核心理论和失败诊断。 |
| p35 | 解释型 RLHF 暂未成为本轮三方向的核心代表路线，留作专题扩展。 |
| p36, p37 | 前者为 arXiv 参照，后者研究分布式 OPE 而非直接 LLM RLHF；不与 p04 混同。 |
| p40, p41 | Position 文章提供动机；本轮主库优先有方法、理论或实证贡献的论文。 |

## 新增 17 篇与选择理由

| ID | 论文 | 理由 |
|---|---|---|
| n01 | InstructGPT | 奠定 LLM RLHF 工程与研究问题的共同起点。 |
| n02 | DPO | 直接偏好优化的代表方法。 |
| n03 | RLAIF vs. RLHF | AI 反馈相对人工反馈的代表性对照。 |
| n04 | Constitutional AI | 原则驱动 AI 反馈的基础预印本。 |
| n05 | Self-Instruct | 自生成指令与 SFT 的代表路线。 |
| n06 | GRPO’s Loss, Dynamics, and Success Amplification | RLVR/GRPO 理论分析入口。 |
| n07 | Spurious Rewards | RLVR 奖励信号有效性的关键问题。 |
| n08 | Fully Self-Synthetic Data | 近期全自合成对齐路线。 |
| n09 | Nudging | 推理时对齐路线。 |
| n10 | Safeguarding LLM Fine-tuning | 安全微调和分布偏移问题。 |
| n11 | Self-Guided Alignment | 多目标偏好适应。 |
| n12 | MUSE | LLM unlearning 的多维评估基准。 |
| n13 | GRU | 遗忘—保留权衡的方法。 |
| n14 | Textual Unlearning Gives a False Sense of Unlearning | 成员推断与重建泄漏审计。 |
| n15 | Context-Aware Unlearning | 条件化遗忘与保留。 |
| n16 | Leak@$k$ | 随机解码下的泄漏评估。 |
| n17 | Unlearning Isn’t Deletion | 可逆性评估。 |

每篇的来源链接、六问分析及核查程度见主数据文件。上述选择不按标题或引用量直接排序。

## 可能的统计研究切入点

1. 偏好模型错设时的稳健策略估计。
2. 带噪、异质标注的反馈融合与可识别性。
3. 奖励模型诊断量与下游策略收益。
4. RLVR 组内采样与伪奖励信号。
5. 自生成及 AI 反馈的测量偏差。
6. 多目标安全对齐的不确定性。
7. LLM 遗忘的可检验性、泄漏与恢复攻击。

以上均为**初步研究假设**，不是已证实的文献空白。网站 Research Opportunities 页列出相关论文、可用统计方法、理论与实验难度，以及尚未验证的问题。

## 数据维护与个人记录

`public/data/papers.json` 是唯一权威主库。编辑后运行 `python3 scripts/sync_papers.py` 和 `python3 scripts/verify_site.py`；脚本生成 HTML 内嵌数据与 CSV。旧论文重新入选时恢复原 ID；新增论文使用新 ID。浏览器继续使用原 `rlhf_stats_atlas_v1` 存储键，筛除论文的收藏、已读和笔记仍在本地，并可在论文探索器的“我的收藏与笔记”中查看、导出。本站不跨设备同步私人记录。
