# 迁移基线与取舍

2026-11-27 按四个来源各自 main 的提交读取。文件数统计 Git 树中的文件，含原有包和示例，用于界定盘点范围。

| 来源与固定快照 | 范围 | 在工作台中的归属 |
|---|---:|---|
| [ai-rd-assistant · f729213](https://github.com/lksharing0208/ai-rd-assistant/tree/f72921372c13573aa10adfc8b2782c07632ab42e) | 全仓 38 个文件 | 12 个研发 Skill 的基础能力、S0–S3 分级和意图路由、客户端包格式及元数据校验 |
| [ai-software-delivery-workbench · 5770b30](https://github.com/lksharing0208/ai-software-delivery-workbench/tree/5770b30c7e6f51e5d011fda8f6e61db9a4054790) | 全仓 51 个文件 | Issue/PR 入口、从需求到发布的证据、审查/发布表单、模型分工、故障排查和复盘指标 |
| [codex-deepseek-agent-workbench · 2bb93c8](https://github.com/lksharing0208/codex-deepseek-agent-workbench/tree/2bb93c88d4eb8dc351f8a33201eac6a7cc81d262) | 全仓 77 个文件 | 编程角色 TOML、provider 与 MCP 配置样例、Worker 报告和执行证据。原始许可单独随附 |
| [ai-recruitment-assistent / ai-agent · 720b5b9](https://github.com/lksharing0208/ai-recruitment-assistent/tree/720b5b987392c199c684cc051307b02dc737a368/ai-agent) | 指定子树 97 个文件 | 归纳阶段审查、人工决策、项目适配、检查点、恢复和归档。业务代码、私有规范、历史任务留在来源项目 |

## 多个来源描述同一能力时

| 原有入口或差异 | 统一后的维护位置 | 合并方式 |
|---|---|---|
| 主 Agent、workbench-orchestrator、Coordinator | skills/ai-rd-workflow | 主控分级并组织交接；路由表只维护在 intent-router 包内 |
| req-clarify、requirement-architecture、design-outline | requirement-analysis、architecture-design | 分开产出可验收需求和模块设计。API 与数据细节继续由已有专项能力提供 |
| design-detail、design-review、human-gate | 同名的三个通用 Skill | 保留详细规格、设计独立审查和决策恢复三类独立产出 |
| implementation、code-implement、feature-delivery | code-implementation、project-delivery | 前者修改和验证代码，后者交接提交、证据及遗留事项 |
| 多个 code-review、review-testing、编程检查清单 | code-review、test-design、templates/review.md | 审查基于差异和证据；实测单列。等级统一为 Blocker、Major、Minor、Info |
| 重复的 ChatGPT / Claude 插件源码和压缩包 | skills/、clients/、scripts/package_clients.py | 插件、场景启动指令不再各自维护通用 Skill 副本，两种 ZIP 从同一源目录生成 |
| 固定执行者、必经 CI、仅做静态审查等来源约定 | 项目适配器、任务单 | 业务仓库决定分支与验证范围，任务记录实际执行结果。工作台未启用 CI 或发布工作流 |
| 多场景脚本、业务 Skill、个案记录、旧安装/推送脚本 | 对应来源快照 | 第一轮保留来源索引；多场景插件与安装流程随后按下节迁入，业务历史任务仍留在业务仓库 |

## 后续同步

先比较来源固定提交与准备引入的新提交，再按本表定位工作台资产。修改共享能力时只编辑对应 Skill，修改客户端格式时只编辑适配器或打包脚本。项目专属约定由对应业务仓库维护。

## 第二轮迁移

Codex 源 main 的五类场景、插件清单、角色、Skills、安装与验证脚本、环境指南和两张架构图迁入 [Codex 扩展](../plugins/codex-deepseek/README.md)，保留单独的插件边界和 MIT 许可。额外分支 d39713f 的文件逐项包含在 main 中。安装脚本补齐场景规则、提示词、校验和运行资源；自动化工作流由实际使用项目配置。

交付仓的存量项目接入、分层测试、发布与回滚操作已纳入[项目接入](project-onboarding.md)及[发布手册](release-and-rollback.md)。旧仓初始化推送脚本、固定账号额度与模型路由、旧目录 CI 和重复的插件适配由来源记录追溯。
