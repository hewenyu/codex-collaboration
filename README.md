# CC-Agent 多 Agent 协作工作流

> 集成 Codex 审核的自动化开发工作流

## 工作流概览

```
┌─────────────────────────────────────────────────────────────────────┐
│                      Phase 1: 需求设计 (人工干预)                    │
│                                                                     │
│  prd-generator        →  产品需求文档                               │
│  gemini-ui-prototyper →  UI 原型设计                               │
│  visual-designer      →  架构图/流程图                              │
│                                                                     │
│  ⚠️  此阶段需要用户确认后才能进入下一阶段                            │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   Phase 2: 架构规划 (人工确认)                       │
│                                                                     │
│  project-architect-supervisor                                       │
│    ├── 生成完整架构树                                                │
│    ├── 拆分为 3-6 个 Phase                                          │
│    └── 每个 Phase 拆分为可执行的 TODO                                │
│                                                                     │
│  ⚠️  用户确认架构规划后，自动进入执行阶段                            │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    Phase 3: 自动执行 (Plan 模式)                     │
│                                                                     │
│  For each TODO:                                                     │
│    1. code-executor 执行实现                                        │
│    2. deep-code-search 代码分析 (可选)                              │
│    3. Codex Review (必须通过)                                       │
│    4. git commit                                                    │
│    5. 下一个 TODO                                                   │
│                                                                     │
│  🔄 自动循环直到所有 TODO 完成                                       │
└─────────────────────────────────────────────────────────────────────┘
```

## 安装使用

### 1. 复制 Agent 文件

将所有 `.md` 文件复制到:
```
~/.claude/agents/
├── prd-generator.md
├── gemini-ui-prototyper.md
├── visual-designer.md
├── project-architect-supervisor.md
├── code-executor.md
└── deep-code-search.md
```

### 2. 项目配置

将 `CLAUDE.md` 复制到你的项目根目录:
```
your-project/
├── CLAUDE.md          ← 复制这个
├── src/
└── ...
```

### 3. Codex 配置

确保 Codex CLI 已安装且可用:
```bash
codex --version
```

### 4. 开始使用

在项目目录中启动 Claude，它会自动识别 `CLAUDE.md` 并遵循工作流。

## Agent 职责

| Agent | 阶段 | 职责 |
|-------|------|------|
| `prd-generator` | 需求设计 | 产品需求文档 |
| `gemini-ui-prototyper` | 需求设计 | UI 原型 |
| `visual-designer` | 需求设计 | 架构图/流程图 |
| `project-architect-supervisor` | 架构规划 | 架构设计、任务拆分、执行编排 |
| `code-executor` | 代码执行 | 功能实现 + Codex 审核 |
| `deep-code-search` | 代码执行 | 代码分析 |

## 关键特性

### Codex 审核门禁

每个代码变更必须通过 Codex 审核才能提交:

```bash
codex review
# 或
codex exec -m gpt-5.2 "Review: $(git diff)"
```

- **PASS**: 提交代码，继续下一个 TODO
- **FAIL**: 修复问题，重新审核

### 自动执行模式

当 `project-architect-supervisor` 生成规划并获得用户确认后:
1. 自动进入执行循环
2. 逐个完成 TODO
3. 每个 TODO 都经过 Codex 审核
4. 自动更新进度文件

### 上下文恢复

通过 `.claude/ROADMAP.md` 可随时恢复上下文:
- 项目概览
- 架构树
- 当前进度
- 下一个待执行任务

## 触发词

| 用户说 | 触发 Agent |
|--------|-----------|
| "设计功能/写 PRD" | prd-generator |
| "设计 UI/原型" | gemini-ui-prototyper |
| "画架构图/流程图" | visual-designer |
| "开始规划/架构设计" | project-architect-supervisor |
| "确认/开始执行" | 自动执行循环 |

## 许可证

MIT License
