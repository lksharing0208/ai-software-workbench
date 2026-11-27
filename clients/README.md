# 客户端接入

| 使用环境 | 从哪里开始 | 如何交接 |
|---|---|---|
| ChatGPT 网页端 | 在仓库根运行 `python3 scripts/package_clients.py`，使用 `dist/ai-software-workbench-chatgpt.zip` 接入支持该格式的插件环境。也可直接读取根目录 AGENTS.md 与目标 Skill | 提供仓库、提交与任务单。仓库访问取决于连接授权 |
| Claude 网页端 / Desktop | 同一命令生成 `dist/claude/<skill>.zip`。逐个选择所需 Skill，将 [Project 指令](claude/project-instructions.md)放入项目 | 每个包仅包含一个顶层 Skill 目录。主控与路由需分别启用 |
| Claude Code | 仓库有根级插件清单与 marketplace。使用下方命令，或在工作区读取 CLAUDE.md | 所有 Skill 均来自根目录 skills/ |
| Codex / DeepSeek | 从仓库根打开工作区，读取 AGENTS.md。按任务选择 .codex/agents/ 的 explorer、architect、implementer、reviewer、tester | 角色配置与 provider 分开。用 [Worker 报告](../templates/worker-report.md)回传证据 |
| Gemini / Grok 等网页端 | 将[补充测试](../prompts/test-gaps.md)或[技术核查](../prompts/technical-research.md)提示词与相关材料一起提供 | 回传定位、来源版本、未验证项；由主执行者处理变更 |

Claude Code 安装入口

```text
/plugin marketplace add lksharing0208/ai-software-workbench
/plugin install ai-software-workbench@ai-software-workbench
```

[DeepSeek provider](codex/deepseek-provider.example.toml) 与 [GitHub MCP](codex/github-mcp.example.json) 为源项目配置示例。实际模型 ID、传输协议和认证由使用方根据当前运行环境确认。启用连接前单独验证能否读取指定文件。工作台提供指令与配置，模型调用、委派和远端写入由已授权的客户端执行。

Codex 的五类行业场景、安装命令及现有项目冲突处理见[多场景插件](../plugins/codex-deepseek/README.md)。
