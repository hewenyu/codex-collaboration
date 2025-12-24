# Codex-Collaboration Skill 总览

## ✅ Skill创建完成！

我已经为您创建了一个完整的Codex协作skill，它建立了Claude与OpenAI Codex CLI之间严格的协作工作流程。

## 📦 包含的文件

### 核心文件
- **codex-collaboration.skill** - 打包的skill文件（可直接导入使用）
- **USAGE_GUIDE.md** - 详细使用指南（中文）

### Skill内部结构

```
codex-collaboration/
├── SKILL.md (主文档)
│   ├── 触发条件：任何编程任务
│   ├── 核心原则：批判性思考、辩论、验证
│   ├── 工作流程：3个主要阶段
│   ├── 质量标准
│   └── 快速开始示例
│
├── scripts/
│   └── codex_helper.py (Python辅助脚本)
│       ├── CodexHelper类
│       ├── 封装所有Codex交互
│       ├── 命令行接口
│       └── 便捷方法（分析、规划、原型、审查等）
│
└── references/
    ├── workflow-details.md (详细工作流程)
    │   ├── 5个主要阶段详解
    │   ├── 每个步骤的具体指导
    │   ├── 批判性思考提示
    │   ├── 处理分歧的方法
    │   └── 反模式和成功指标
    │
    ├── codex-commands.md (Codex命令参考)
    │   ├── 基本用法
    │   ├── 模型选择
    │   ├── 沙盒模式
    │   ├── 6种常见任务模式
    │   ├── 高级用法
    │   └── 错误处理
    │
    └── reverse-engineering.md (逆向代码分析指南)
        ├── 逆向代码的用途
        ├── 4阶段分析工作流
        ├── 5种常见模式
        ├── 与工作流的集成
        ├── 道德考虑
        └── 分析清单
```

## 🎯 核心特性

### 1. 严格的协作工作流
- **阶段1：需求分析与规划**
  - 与Codex共同分析需求
  - 批判性评估和辩论
  - 制定详细的todolist

- **阶段2：Todo执行循环**
  - 请求代码原型（仅diff）
  - 重写为生产级代码
  - 立即代码审查
  - 完整性检查
  - 逆向代码优化
  - 选择性改进应用
  - **生成提交信息（使用Codex）**
  - **提交到Git（保存阶段性进度）**

- **阶段3：最终审查**
  - 全面的项目审查
  - 质量和安全评估

### 2. 批判性思考强制执行
- 质疑Codex的每个建议
- 质疑自己的实现
- 通过辩论达到最佳方案
- 永远不盲目接受

### 3. 生产质量保证
- 永远不直接应用patch
- 始终重写为企业级代码
- 全面的错误处理
- 完整的文档
- 严格的验证

### 4. 逆向代码优化
- 从成熟实现中学习
- 识别优化机会
- 发现边缘情况
- 验证方法

### 5. 便捷工具支持
- Python辅助脚本
- 命令行接口
- 预定义任务模式
- 结构化输出

### 6. Git提交管理
- 每个todo完成后自动提交
- 使用Codex生成专业提交信息
- Conventional Commit格式
- 清晰的开发历史
- 便于回滚和审查
- 阶段性进度保存

## 🔧 技术规格

- **默认模型**: gpt-5.2-codex
- **推理级别**: xhigh
- **工作模式**: Plan-based with todolist
- **语言**: Python 3.x
- **依赖**: OpenAI Codex CLI

## 📋 工作流程清单

每个todo的执行：
- [ ] Codex原型请求（仅diff！）
- [ ] 原型批判性分析
- [ ] 从头编写生产代码
- [ ] 获取Codex即时审查
- [ ] 批判性评估反馈
- [ ] 验证完整性
- [ ] 辩论并解决遗漏项
- [ ] 探索逆向代码优化
- [ ] 选择性应用改进
- [ ] 最终验证
- [ ] **使用Codex生成提交信息**
- [ ] **提交变更到Git**
- [ ] 标记完成

## 🎓 使用示例

### 基本用法
```bash
# 分析需求
codex exec --model gpt-5.2-codex --reasoning xhigh \
  "分析需求：实现用户认证"

# 创建计划
codex exec --model gpt-5.2-codex --reasoning xhigh \
  "创建实施计划和todolist"

# 请求原型
codex exec --model gpt-5.2-codex --reasoning xhigh \
  "生成unified diff patch ONLY" > prototype.patch

# 审查代码
codex exec --model gpt-5.2-codex --reasoning xhigh \
  "审查实现：$(git diff)"
```

### 使用Python辅助脚本
```python
from scripts.codex_helper import CodexHelper

helper = CodexHelper()
analysis = helper.analyze_requirements("实现用户登录")
plan = helper.create_implementation_plan(refined_requirements)
helper.request_code_prototype(todo, reqs, files)
review = helper.review_code(todo, git_diff)

# 生成提交信息
commit_msg = helper.generate_commit_message(todo_description)
```

### Git提交工作流
```bash
# 1. 完成todo后，生成提交信息
python scripts/codex_helper.py commit "实现JWT令牌服务"

# 2. 提交变更
git add .
git commit -m "feat(auth): implement JWT token service

实现JWT令牌生成和验证服务...
"

# 3. 可选：标记里程碑
git tag -a "todo-003-complete" -m "完成用户认证"
```

## ⚠️ 关键原则

1. **Codex提供建议，Claude做决定** - 最终决策权在Claude
2. **辩论是必需的** - 分歧导致更好的解决方案
3. **永远不要跳过批判性思考** - 质疑一切
4. **始终重写为生产标准** - 不要复制粘贴
5. **每一步都要验证** - 信任但验证

## ❌ 要避免的反模式

- ❌ 盲目接受建议
- ❌ 直接应用patch
- ❌ 跳过辩论
- ❌ 忽略逆向代码
- ❌ 仓促审查
- ❌ 缺少验证
- ❌ 孤立思考

## 📚 参考资料

skill包含3个详细的参考文档：
1. **workflow-details.md** - 250+行详细工作流程
2. **codex-commands.md** - 完整的Codex CLI参考
3. **reverse-engineering.md** - 逆向代码分析完整指南

## 🚀 下一步

1. **导入skill** - 将 `codex-collaboration.skill` 导入到Claude
2. **安装Codex** - `npm install -g @openai/codex`
3. **配置认证** - `codex login`
4. **阅读使用指南** - 查看 `USAGE_GUIDE.md`
5. **开始使用** - 任何编程任务都使用这个workflow

## 💡 设计理念

这个skill的设计基于以下理念：
- **AI应该协作，而非独裁** - 人类保持控制
- **质量源于辩论** - 不同观点产生更好方案
- **批判性思考不可或缺** - 永远质疑和验证
- **生产级别是标准** - 不接受低于企业质量的代码
- **持续改进** - 从逆向代码和审查中学习

## 📊 预期效果

使用这个skill，您将获得：
- ✅ 更高质量的代码
- ✅ 更好的架构决策
- ✅ 更全面的错误处理
- ✅ 更深思熟虑的实现
- ✅ 更强的可维护性
- ✅ 通过辩论得到验证的方案

## 🎉 总结

您现在拥有一个完整的、生产就绪的Codex协作skill，它：
- 为所有编程任务建立严格的工作流程
- 强制执行批判性思考和辩论
- 确保生产级代码质量
- 提供便捷的工具和文档
- 支持逆向代码优化
- 包含完整的参考资料

**目标不是速度，而是通过严格协作实现高质量、深思熟虑的代码！**
