---
name: codex-collaboration
description: "Multi-agent development workflow with Codex quality gates. Orchestrates prd-generator, gemini-ui-prototyper, visual-designer, project-architect-supervisor, code-executor, and deep-code-search agents. Use for ANY software development project. Phases: (1) Requirements/UI design with human intervention, (2) Architecture planning with user confirmation, (3) Automatic code execution with mandatory Codex review. Triggers: any programming task, project planning, feature implementation, code writing."
---

# Codex Multi-Agent Development Workflow

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                      Phase 1: 需求设计 (人工干预)                    │
│                                                                     │
│  prd-generator        →  产品需求文档                               │
│  gemini-ui-prototyper →  UI 原型设计                               │
│  visual-designer      →  架构图/流程图                              │
│                                                                     │
│  ⚠️  需要用户确认后才能进入下一阶段                                   │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   Phase 2: 架构规划 (人工确认)                       │
│                                                                     │
│  project-architect-supervisor                                       │
│    ├── 生成完整架构树 (ROADMAP.md)                                  │
│    ├── 拆分为 3-6 个 Phase                                          │
│    └── 每个 Phase 拆分为可执行的 TODO (PHASE_PLAN.md)               │
│                                                                     │
│  ⚠️  用户确认后自动进入执行阶段                                      │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    Phase 3: 自动执行 (Plan 模式)                     │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  For each TODO in PHASE_PLAN:                                │  │
│  │                                                              │  │
│  │  1. code-executor 执行实现                                   │  │
│  │           │                                                  │  │
│  │           ▼                                                  │  │
│  │  2. deep-code-search 代码分析 (可选)                         │  │
│  │           │                                                  │  │
│  │           ▼                                                  │  │
│  │  3. codex review ══════════════════════════════════════════ │  │
│  │           │                                                  │  │
│  │      ┌────┴────┐                                             │  │
│  │    PASS      FAIL → Fix → Re-review                          │  │
│  │      │                                                       │  │
│  │      ▼                                                       │  │
│  │   git commit → Next TODO                                     │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  🔄 自动循环直到所有 TODO 完成                                       │
└─────────────────────────────────────────────────────────────────────┘
```

## Agent Responsibilities

| Agent | Phase | Responsibility | Automation |
|-------|-------|----------------|------------|
| `prd-generator` | Requirements | PRD creation | ❌ Human |
| `gemini-ui-prototyper` | Requirements | UI prototypes | ❌ Human |
| `visual-designer` | Requirements | Diagrams/flows | ❌ Human |
| `project-architect-supervisor` | Planning | Architecture, task breakdown | ❌ Confirm |
| `code-executor` | Execution | Implementation | ✅ Auto |
| `deep-code-search` | Execution | Code analysis | ✅ Auto |
| `Codex (gpt-5.2)` | Execution | Code review | ✅ Auto |

## Workflow Execution

### Starting a New Project

1. **Gather Requirements** (Human Phase)
   ```
   User: "我想做一个视频脚本生成平台"
   → Delegate to prd-generator for PRD
   → Delegate to gemini-ui-prototyper for UI mockup
   → Delegate to visual-designer for architecture diagram
   ```

2. **Architecture Planning** (Confirmation Required)
   ```
   User: "开始规划"
   → Delegate to project-architect-supervisor
   → Generate ROADMAP.md with architecture tree
   → Generate PHASE_PLAN.md with TODOs
   → Present plan and WAIT for user confirmation
   ```

3. **Automatic Execution** (After Confirmation)
   ```
   User: "确认" or "开始执行"
   → Enter automatic execution loop
   → Execute each TODO via code-executor
   → Mandatory Codex review before commit
   → Update progress after each TODO
   → Continue until all TODOs complete
   ```

## Codex Integration

### Review Command
```bash
# Standard review
codex review

# Detailed review
codex exec -m gpt-5.2 "
Review implementation for: [TASK_DESCRIPTION]
$(git diff)
Check: correctness, bugs, security, quality, edge cases
Verdict: PASS or FAIL with specific issues
"
```

### Review Gate Logic
```python
def codex_review_gate(task):
    while True:
        result = codex_review(task)
        if result.passed:
            git_commit(task)
            return
        else:
            fix_issues(result.issues)
            # Re-submit automatically
```

### No Exceptions
- **EVERY** code change must pass Codex review
- **NEVER** skip review, even for "small" changes
- **NEVER** commit without PASS verdict

## File Structure

```
project/
├── CLAUDE.md                    # Workflow configuration
├── .claude/
│   ├── ROADMAP.md               # Project roadmap + architecture
│   └── phases/
│       ├── phase-1_xxx/
│       │   ├── PHASE_PLAN.md    # Phase plan
│       │   └── TASK-001_xxx.md  # Task specs
│       └── phase-N_xxx/
├── issues/
│   └── phase-N_xxx/
│       ├── PHASE_SUMMARY.md     # Phase summary
│       └── TASK-001_xxx.md      # Task reports
├── docs/
│   ├── PRD-xxx.md               # PRDs
│   └── UI-xxx.html              # UI prototypes
└── src/                         # Source code
```

## Progress Tracking

After each TODO completion:
```
═══════════════════════════════════════════════════
📊 Progress Update
═══════════════════════════════════════════════════
Phase: 2/4 - Core Features
Task:  3/5 - TASK-003 Complete ✅

Overall: ████████░░░░░░░░ 45%

Codex Reviews: 3 passed, 1 retry
═══════════════════════════════════════════════════
```

## Trigger Words

| User Says | Triggers | Phase |
|-----------|----------|-------|
| "设计功能/写 PRD" | prd-generator | Requirements |
| "设计 UI/原型" | gemini-ui-prototyper | Requirements |
| "画架构图/流程图" | visual-designer | Requirements |
| "开始规划/架构设计" | project-architect-supervisor | Planning |
| "确认/开始执行" | Automatic loop | Execution |
| "继续执行/下一步" | Continue loop | Execution |

## Context Recovery

If context is lost:
1. Read `.claude/ROADMAP.md` for project state
2. Read current `PHASE_PLAN.md` for task status
3. Locate first non-completed task
4. Resume execution from there

## Key Principles

1. **Human gates for design decisions** - Don't automate requirements/architecture
2. **Automatic execution after confirmation** - Minimize human intervention
3. **Codex review is mandatory** - Quality gate for every commit
4. **Atomic commits** - One TODO = one commit
5. **Progress persistence** - Always recoverable from documentation
