# Codex Collaboration Skill - 使用指南

## 概述

这个skill建立了Claude与OpenAI Codex CLI之间严格的协作工作流程，用于所有编程任务。

## 核心理念

- **Claude执行，Codex提供建议** - Claude是主要执行者，Codex是专家顾问
- **批判性思考** - 永远不要盲目接受建议
- **通过辩论提升质量** - 分歧会带来更好的解决方案
- **每一步都要验证** - 审查、质疑、验证
- **生产级质量** - 始终重写代码以达到企业标准

## 前置要求

1. **安装Codex CLI**
   ```bash
   npm install -g @openai/codex
   ```

2. **配置Codex**
   ```bash
   codex login
   # 使用ChatGPT账号或API key登录
   ```

3. **验证安装**
   ```bash
   codex --version
   ```

## 何时使用此Skill

**所有编程任务都应该使用这个workflow：**
- 编写代码、实现功能
- 代码审查和调试
- 架构和设计决策
- 技术文档编写
- 重构和优化
- Bug修复
- 技术分析

## 工作流程概览

### 阶段1：需求分析与规划

1. **接收用户任务**
2. **初步理解需求**
3. **咨询Codex进行需求分析**
4. **批判性评估Codex的分析**
5. **如有分歧则进行辩论**
6. **请求Codex制定实施计划**
7. **独立开发自己的计划**
8. **对比两个计划并辩论**
9. **最终确定计划**（包含最佳元素）

### 阶段2：Todo执行循环

对于计划中的每个todo：

1. **向Codex请求代码原型**（仅unified diff格式）
2. **批判性分析原型**
3. **重写为生产级代码**（不要直接应用patch）
4. **立即从Codex获取代码审查**
5. **批判性分析审查反馈**
6. **完整性检查**
7. **辩论遗漏项**
8. **逆向代码优化**（如适用）
9. **选择性应用改进**
10. **生成提交信息**（使用Codex）
11. **提交到Git**（保存阶段性进度）
12. **验证后标记todo完成**

### 阶段3：最终审查

所有todo完成后进行最终项目审查。

## 关键原则

### 必须质疑Codex的建议

- 为什么采用这个方法？
- 做了什么假设？
- 有没有更好的替代方案？
- 遗漏了什么？

### 必须质疑自己的工作

- 我是否在盲目跟从？
- 我有没有独立思考？
- 我是否过度复杂化了？
- 如果没有Codex我会怎么做？

### 必须进行辩论

- 我们探索了所有选项吗？
- 有第三个选项吗？
- 真正的权衡是什么？
- 我们在优化正确的东西吗？

## 处理分歧

当你与Codex意见不一致时：

1. **清晰表达** - 陈述立场和理由
2. **要求澄清** - 让Codex解释
3. **提出替代方案** - 展示你的方法
4. **要求论证** - 要求具体理由
5. **做出决定** - 你有最终决定权

## 质量标准

每个todo必须满足：
- ✓ 正确性 - 完全满足需求
- ✓ 质量 - 生产级代码
- ✓ 可维护性 - 整洁、有文档、可读
- ✓ 健壮性 - 处理边缘情况和错误
- ✓ 性能 - 合理的效率
- ✓ 安全性 - 没有明显漏洞

## 快速开始示例

```bash
# 用户任务："实现用户认证"

# 1. 使用Codex分析
codex exec --model gpt-5.2-codex --reasoning xhigh \
  "分析需求：使用JWT实现用户认证"

# 2. 获取计划
codex exec --model gpt-5.2-codex --reasoning xhigh \
  "为JWT认证创建包含todolist的实施计划"

# 3. 对于每个todo，获取原型
codex exec --model gpt-5.2-codex --reasoning xhigh \
  "仅生成unified diff patch：创建JWT令牌服务" \
  > prototype.patch

# 4. 审查原型，重写为生产代码

# 5. 获取审查
codex exec --model gpt-5.2-codex --reasoning xhigh \
  "审查此实现：$(git diff)"

# 6. 继续下一个todo...
```

## 使用辅助脚本

skill包含Python辅助脚本简化Codex交互：

```python
from scripts.codex_helper import CodexHelper

helper = CodexHelper(project_dir="/path/to/project")

# 分析需求
analysis = helper.analyze_requirements(user_request)

# 创建计划
plan = helper.create_implementation_plan(requirements)

# 请求原型
helper.request_code_prototype(todo, requirements, files)

# 审查代码
review = helper.review_code(todo, git_diff)

# 检查完整性
completeness = helper.check_completeness(todo, summary)

# 分析逆向代码
optimizations = helper.analyze_reverse_code(our_code, reverse_path)

# 生成提交信息
commit_msg = helper.generate_commit_message(todo_description)
```

## Git提交最佳实践

### 为什么每个Todo完成后都要提交

- **保存增量进度** - 每个完成的任务都被保存
- **便于回滚** - 可以回退到任何之前的todo状态
- **清晰的开发历史** - 展示工作的逻辑进展
- **独立审查** - 每个提交可以单独审查
- **测试检查点** - 可以在每个阶段测试
- **团队协作** - 团队可以详细看到进度
- **调试辅助** - 更容易识别问题引入的时间点

### 生成提交信息

使用Codex生成专业的提交信息：

```bash
# 使用辅助脚本
python scripts/codex_helper.py commit "实现JWT令牌服务"

# 或直接使用Codex
codex exec --model gpt-5.2-codex --reasoning medium "
为以下todo生成conventional commit信息：
TODO: 实现JWT令牌服务
变更：$(git diff --staged)

要求：
- 使用conventional commit格式
- 第一行最多50字符
- 正文解释做了什么和为什么
- 专业清晰
"
```

### 提交工作流程

```bash
# 1. 查看变更
git status
git diff

# 2. 暂存变更
git add .

# 3. 生成提交信息
python scripts/codex_helper.py commit "实现用户认证"

# 4. 提交
git commit -m "feat(auth): implement JWT token service

实现JWT令牌生成和验证服务，包括：
- 使用HS256算法签名
- 可配置的过期时间
- 安全的密钥管理
- 全面的错误处理

为用户认证提供了基础。"

# 5. 可选：标记重要里程碑
git tag -a "todo-003-complete" -m "完成用户认证"

# 6. 验证提交
git log -1 --stat
```

### Conventional Commit格式

```
类型(范围): 简短描述 (最多50字符)

详细正文解释：
- 实现了什么
- 为什么这样做
- 任何重要决策或权衡
- 如有破坏性变更需说明

参考: #issue编号 (如适用)
```

**类型：**
- `feat`: 新功能
- `fix`: Bug修复
- `refactor`: 重构
- `docs`: 文档
- `test`: 测试
- `chore`: 维护任务
- `perf`: 性能改进
- `style`: 代码风格

**范围（可选）：**
- 受影响的组件或模块（如：auth, api, ui, db）

## 逆向代码分析

如果你有逆向工程的代码，可以用于优化：

1. **将逆向代码放在 `reverse_meta/` 目录**
2. **在实现过程中参考逆向代码**
3. **使用Codex分析逆向代码的模式和优化**
4. **提取学习点应用到你的实现**

示例：
```bash
codex exec --model gpt-5.2-codex --reasoning xhigh "
分析优化机会：
我们的实现：[描述]
逆向代码参考：reverse_meta/[路径]
"
```

## 反模式（要避免）

❌ **盲目接受** - 不要不经批判性思考就应用建议
❌ **复制粘贴编码** - 不要直接应用patch而不重写
❌ **跳过辩论** - 不要回避分歧
❌ **忽略逆向代码** - 始终检查优化机会
❌ **仓促审查** - 花时间彻底分析
❌ **缺少验证** - 始终验证完整性
❌ **孤立思考** - 考虑大局

## Skill文件结构

```
codex-collaboration/
├── SKILL.md                          # 主skill文档
├── scripts/
│   └── codex_helper.py              # Python辅助脚本
└── references/
    ├── workflow-details.md          # 详细工作流程
    ├── codex-commands.md            # Codex命令参考
    └── reverse-engineering.md       # 逆向代码分析指南
```

## 常见问题

**Q: 我必须为每个编程任务都使用这个workflow吗？**
A: 是的。这个workflow确保高质量和深思熟虑的代码。

**Q: 如果我不同意Codex的建议怎么办？**
A: 很好！提出你的观点，进行辩论，然后做出你认为最好的决定。

**Q: 我可以直接应用Codex的diff patch吗？**
A: 不可以。始终将其作为逻辑参考，然后重写为生产级代码。

**Q: 如果没有逆向代码怎么办？**
A: 没关系。逆向代码是可选的优化步骤。

**Q: 我应该使用什么Codex模型？**
A: 默认使用 `gpt-5.2-codex` 配合 `xhigh` 推理模式。

## 记住

- **Codex提供建议，Claude做决定**
- **辩论对质量至关重要**
- **永远不要跳过批判性思考**
- **始终重写为生产标准**
- **每一步都要验证**

目标不是速度，而是**通过严格协作实现高质量、深思熟虑的代码**。
