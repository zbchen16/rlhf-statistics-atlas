# Codex task: publish the prepared RLHF × Statistics research atlas as a public GitHub Pages site

你是我的 Codex 工程执行助手。请在我指定并打开的 `rlhf_statistics_github_site` 项目根目录内工作，目标是将现有网站发布为**可公开访问的 GitHub Pages 项目网站**。请实际执行可执行的代码、测试和发布操作；不要只给我教程或设计方案。

## 目标与事实

- 输入已整理：`public/index.html` 是**现有可交互网站**；`public/data/papers.json` 是**唯一权威论文数据源**；`public/data/papers.csv` 是导出副本；`docs/screenshots/` 是参考截图；`scripts/` 内有同步及一致性检查代码；`.github/workflows/pages.yml` 已包含静态发布工作流。
- 这份数据来自 2026-10-21 的人工整理，共 41 篇；不得把阅读优先级 A/B/C/S 当成 CCF 会议等级，也不得宣称论文综述已独立核验全部科学结论。
- 优先采用**纯静态 HTML/CSS/JS + GitHub Pages**。不要为了工程复杂度引入 React、Next.js、后端、数据库、收费云服务、LLM API、Agent 或用户登录。
- 网站定位：供统计学研究者探索 2025–2026 RLHF / preference learning / alignment 文献，保留中文 UI 和原有深色侧栏布局。

## 范围与工作步骤

1. 首先读取 `README.md`、`public/index.html`、`public/data/papers.json`、`.github/workflows/pages.yml`、`scripts/`；检查 git 状态与现有 repository/remote。**不得扫描或修改本项目根目录外的文件**，不得影响其他正在运行的 VS Code 窗口、Jupyter kernel、训练任务或仓库。
2. 运行 `python scripts/verify_site.py`。只有在发现实际问题时才做最小化修复。若修改论文数据，只编辑 `public/data/papers.json`，随后运行 `python scripts/sync_papers.py` 和一致性验证；不可凭印象编造论文标题、会议年份、链接或作者。
3. 保留并检查以下交互：检索；年份/会议/方向/统计技术/优先级筛选；论文详情及外部原文；四周阅读路线；六个研究切口；比较；收藏、阅读状态及笔记；CSV/笔记导出；移动端侧栏。
4. 重点检查 **GitHub Pages 子路径兼容**（`https://<owner>.github.io/<repo>/`），不要使用会在项目站点上 404 的绝对根路径。检索、导出和笔记应在公网网址正常运行；笔记明确为浏览器本地保存、不能跨设备同步。
5. 补充必要的自动化验证或轻量浏览器冒烟测试（如本机具备 Playwright/Chromium）。至少覆盖：首页加载；41 条论文；组合筛选；打开详情；本地持久化；路线和研究切口；无明显 JS 异常；窄屏无溢出。禁止把只通过 `python` 静态检查描述为“浏览器测试通过”。
6. 如果 GitHub CLI (`gh`) 已登录且具备权限，在**我的 GitHub 账号**新建**public** repository，建议名称 `rlhf-statistics-atlas`（若已存在同名仓库，先检查 remote/内容并避免覆盖；不允许强制推送或删除）。推送此项目的最小必要代码文件到 `main`，配置 GitHub Pages 为 **GitHub Actions**，并使用已存在的 `.github/workflows/pages.yml` 部署。
7. 如需交互式登录、权限确认或 GitHub 无法访问，请完成所有本地准备并列出**恰好还缺少的授权或操作**；不得捏造发布成功、仓库地址或公网链接。不要要求我把 GitHub token 复制到聊天中，也不要把 secret 写入仓库。
8. 发布后检查 GitHub Actions `verify` 和 `deploy` 的执行结果，并**通过浏览器或可靠的 HTTP 检查真实公网 URL**。若部署 404，先检查 Pages 发布源、Actions 日志、entry file、权限、repo path，然后修复并重试。
9. 改善公开仓库展示：保留简洁 README、数据来源/编辑方法、更新日期、局限性说明，以及 1–2 张截图。不要把学术上的“候选研究切口”描述为已经证实的创新贡献。

## 交付格式

最后请按下列顺序报告：

- 本地项目路径和实际修改的文件（简述原因）；
- 验证命令及真实执行结果（区分源一致性、浏览器检查、HTTP/线上检查）；
- GitHub public 仓库 URL；
- GitHub Pages 公开访问 URL；
- 未解决问题、权限阻碍与需要我手动做的单步操作（如有）。

**核心要求：保留已可用的交互体验，优先直接发布，避免不必要的大重构。**
