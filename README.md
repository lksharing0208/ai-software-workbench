# AI 软件工程与研发协作工作台

一套可在 ChatGPT、Claude、Codex 等客户端复用的研发工作台。需求、设计、实现、审查和交付共用一份 Skill 源码。业务项目通过项目适配器提供自己的工程规范、源码入口和执行约束。

## 从一个任务开始

1. 在[客户端接入说明](clients/README.md)选择入口。直接使用仓库的客户端先读 [AGENTS.md](AGENTS.md)。
2. 提供目标业务仓库、基线、涉及模块与验收条件。新项目从[项目适配器模板](projects/adapter-template.md)登记真实路径。
3. 单项任务按[能力路由](skills/intent-router/references/routes.yaml)选择一个主 Skill。跨会话任务把[任务单](templates/task.md)和[检查点](templates/checkpoint.md)放在业务仓库的任务目录。
4. 审查时交接实际 diff、调用链和验收条件。将发现、整改提交和验证结果记入同一个任务，按[资料存储约定](docs/storage.md)归档。

例如，已有 PR 需要代码审查时，给出仓库、基础提交、待审提交和关联需求，直接使用 [code-review](skills/code-review/SKILL.md)。跨模块功能开发则从[研发协调器](skills/ai-rd-workflow/SKILL.md)进入，按[阶段工作流](docs/workflow.md)推进。

## 项目目录

| 目录 | 内容及维护入口 |
|---|---|
| [skills/](skills/) | 15 个能力入口。主控配置随 ai-rd-workflow 维护，意图映射随 intent-router 维护 |
| [clients/](clients/) | ChatGPT 插件配置、Claude Project 指令、Codex 所用 provider 与 MCP 样例 |
| [.codex/agents/](.codex/agents/) | 调研、架构、实现、审查、测试五类角色 |
| [.claude-plugin/](.claude-plugin/) | Claude Code 安装清单，复用根目录 skills/ |
| [projects/](projects/) | 新业务项目接入模板，具体项目按自己的可见范围保存实例 |
| [templates/](templates/) | 需求、任务、检查点、执行者报告、审查、发布表单 |
| [prompts/](prompts/) | 测试补充、外部技术核查、故障排查提示词 |
| [.github/](.github/) | 功能需求与缺陷 Issue 表单、PR 模板 |
| [scripts/](scripts/) | Skill 校验及多客户端打包 |
| [docs/](docs/) | 交付流程、项目资料存储、复盘指标和迁移记录 |
| [notices/](notices/) | 引入的 Codex + DeepSeek 素材的原始许可声明 |

## 本地校验与打包

在仓库根使用 Python 3.10 或更高版本执行：

```sh
python3 scripts/validate_skills.py
python3 scripts/package_clients.py
```

产物写入本地 dist/。客户端安装方式和包格式见[接入说明](clients/README.md)。四个来源的基线、保留范围和合并规则见[迁移记录](docs/migration.md)。

## 行业插件与交付手册

[Codex 多场景插件](plugins/codex-deepseek/README.md)覆盖编程、金融、法律、写作和短剧。它有独立插件清单、项目安装器、场景规则、领域 Skills 和本地验证脚本。根目录的 15 个研发 Skills 继续供多客户端共用。

新业务仓库可按[接入与质量门禁](docs/project-onboarding.md)登记验证命令。准备上线时使用[发布与回滚手册](docs/release-and-rollback.md)。

各项能力的验证范围见[核心能力复核](docs/capability-review.md)。
