# 工作台入口

研发协调使用 [ai-rd-workflow](skills/ai-rd-workflow/SKILL.md)，专项能力按[意图路由](skills/intent-router/references/routes.yaml)选择。执行前读取目标业务仓库的项目规范，确认目标分支、修改范围与验证权限。

跨阶段任务遵循[交付工作流](docs/workflow.md)并按[资料存储约定](docs/storage.md)保存结果。工作台维护通用能力和空白模板。业务项目拥有自己的源码、工程约束和交付证据。
