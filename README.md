# Codex Collaboration Skill

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Claude](https://img.shields.io/badge/Claude-Skill-orange.svg)

一个为Claude设计的严格协作编程工作流skill，通过与OpenAI Codex CLI的深度协作，实现高质量、深思熟虑的代码开发。

[English](#english) | [中文](#中文)

---

## 中文

### 📖 简介

Codex-Collaboration 是一个专业的Claude skill，建立了Claude与OpenAI Codex CLI之间严格的协作工作流程。它强制执行批判性思考、相互验证和持续改进，确保每一行代码都经过深思熟虑和充分验证。

### ✨ 核心特性

- 🤝 **严格的协作工作流** - Claude执行，Codex提供建议，通过辩论达到最佳方案
- 🧠 **强制批判性思考** - 质疑每个建议，永不盲目接受
- 🏗️ **计划模式开发** - 基于todolist的结构化开发流程
- ✅ **生产级质量保证** - 始终重写为企业级代码，不直接应用patch
- 🔄 **逆向代码优化** - 从成熟实现中学习和优化
- 📝 **Git提交管理** - 每个todo完成后自动生成专业commit message并提交
- 🛠️ **便捷工具支持** - Python辅助脚本和CLI工具

### 🎯 使用场景

**所有编程任务都应该使用这个workflow：**
- 代码编写和功能实现
- 代码审查和调试
- 架构和设计决策
- 技术文档编写
- 代码重构和优化
- Bug修复
- 技术分析

### 🚀 快速开始

#### 1. 前置要求

```bash
# 安装 OpenAI Codex CLI
npm install -g @openai/codex

# 登录 Codex
codex login
```

#### 2. 安装Skill

**方法1：直接下载.skill文件**
1. 从 [Releases](../../releases) 下载 `codex-collaboration.skill`
2. 在Claude中导入该skill文件

**方法2：从源码构建**
```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/codex-collaboration.git
cd codex-collaboration

# 打包skill（需要安装skill-creator）
python /path/to/skill-creator/scripts/package_skill.py codex-collaboration ./
```

#### 3. 基本使用

一旦导入skill，任何编程任务都会自动触发这个工作流：

```bash
# 示例：实现用户认证
# Claude会自动：
# 1. 与Codex分析需求
# 2. 制定详细计划和todolist
# 3. 对每个todo执行严格的开发循环
# 4. 生成commit message并提交
```

### 📋 工作流程

#### 阶段1：需求分析与规划
1. 接收用户任务
2. 与Codex共同分析和完善需求
3. 批判性评估和辩论
4. 制定详细的实施计划和todolist

#### 阶段2：Todo执行循环（每个todo）
1. 向Codex请求代码原型（仅unified diff）
2. 批判性分析原型
3. 重写为生产级代码（不直接应用patch）
4. 立即从Codex获取代码审查
5. 批判性评估审查反馈
6. 完整性检查和遗漏项辩论
7. 逆向代码优化（如适用）
8. 选择性应用改进
9. 使用Codex生成提交信息
10. 提交到Git保存进度
11. 标记todo完成

#### 阶段3：最终审查
- 全面的项目审查
- 质量和安全评估

### 🛠️ 辅助工具

#### Python辅助脚本

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

# 生成提交信息
commit_msg = helper.generate_commit_message(todo_description)
```

#### CLI工具

```bash
# 分析需求
python scripts/codex_helper.py analyze requirements.txt

# 创建计划
python scripts/codex_helper.py plan requirements.txt plan.txt

# 生成commit message
python scripts/codex_helper.py commit "实现用户认证"
```

### 💡 核心原则

1. **Codex提供建议，Claude做决定** - 最终决策权在Claude
2. **辩论是必需的** - 分歧导致更好的解决方案
3. **永远不要跳过批判性思考** - 质疑一切
4. **始终重写为生产标准** - 不要复制粘贴
5. **每一步都要验证** - 信任但验证
6. **每个todo都要提交** - 保存阶段性进度

### 📁 项目结构

```
codex-collaboration/
├── SKILL.md                          # 主skill文档
├── scripts/
│   └── codex_helper.py              # Python辅助脚本
└── references/
    ├── workflow-details.md          # 详细工作流程（250+行）
    ├── codex-commands.md            # Codex CLI命令参考
    └── reverse-engineering.md       # 逆向代码分析指南
```

### 📚 文档

- [使用指南](USAGE_GUIDE.md) - 详细的使用说明
- [Skill概览](SKILL_OVERVIEW.md) - 功能和特性概览
- [更新说明](UPDATE_NOTES.md) - 最新更新内容

### ⚙️ 配置

默认配置：
- **模型**: `gpt-5.2-codex`
- **推理级别**: `xhigh`
- **工作模式**: Plan-based with todolist

### 🤝 贡献

欢迎贡献！请：
1. Fork 这个仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交变更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

### 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

### 🙏 致谢

- [OpenAI Codex](https://openai.com/codex/) - 强大的编程助手
- [Anthropic Claude](https://www.anthropic.com/) - 优秀的AI助手平台

### 📧 联系方式

有问题或建议？欢迎：
- 提交 [Issue](../../issues)
- 发起 [Discussion](../../discussions)

---

## English

### 📖 Introduction

Codex-Collaboration is a professional Claude skill that establishes a rigorous collaborative workflow between Claude and OpenAI Codex CLI. It enforces critical thinking, mutual verification, and continuous improvement to ensure every line of code is well-thought-out and thoroughly validated.

### ✨ Key Features

- 🤝 **Rigorous Collaborative Workflow** - Claude executes, Codex advises, debate to reach optimal solutions
- 🧠 **Mandatory Critical Thinking** - Question every suggestion, never blindly accept
- 🏗️ **Plan-based Development** - Structured development process based on todolist
- ✅ **Production Quality Assurance** - Always rewrite to enterprise-grade code, never directly apply patches
- 🔄 **Reverse Code Optimization** - Learn and optimize from mature implementations
- 📝 **Git Commit Management** - Auto-generate professional commit messages and commit after each todo
- 🛠️ **Convenient Tool Support** - Python helper scripts and CLI tools

### 🎯 Use Cases

**This workflow should be used for ALL programming tasks:**
- Code writing and feature implementation
- Code review and debugging
- Architecture and design decisions
- Technical documentation
- Code refactoring and optimization
- Bug fixing
- Technical analysis

### 🚀 Quick Start

#### 1. Prerequisites

```bash
# Install OpenAI Codex CLI
npm install -g @openai/codex

# Login to Codex
codex login
```

#### 2. Install Skill

**Option 1: Download .skill file**
1. Download `codex-collaboration.skill` from [Releases](../../releases)
2. Import the skill file in Claude

**Option 2: Build from source**
```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/codex-collaboration.git
cd codex-collaboration

# Package skill (requires skill-creator)
python /path/to/skill-creator/scripts/package_skill.py codex-collaboration ./
```

#### 3. Basic Usage

Once imported, any programming task will automatically trigger this workflow:

```bash
# Example: Implement user authentication
# Claude will automatically:
# 1. Analyze requirements with Codex
# 2. Create detailed plan and todolist
# 3. Execute rigorous development loop for each todo
# 4. Generate commit message and commit
```

### 📋 Workflow

#### Phase 1: Requirement Analysis & Planning
1. Receive user task
2. Analyze and refine requirements with Codex
3. Critical evaluation and debate
4. Create detailed implementation plan and todolist

#### Phase 2: Todo Execution Loop (per todo)
1. Request code prototype from Codex (unified diff only)
2. Critical analysis of prototype
3. Rewrite to production-grade code (don't directly apply patch)
4. Get immediate code review from Codex
5. Critical evaluation of review feedback
6. Completeness check and debate missing items
7. Reverse code optimization (if applicable)
8. Apply selective improvements
9. Generate commit message with Codex
10. Commit to Git to save progress
11. Mark todo complete

#### Phase 3: Final Review
- Comprehensive project review
- Quality and security assessment

### 🛠️ Helper Tools

#### Python Helper Script

```python
from scripts.codex_helper import CodexHelper

helper = CodexHelper(project_dir="/path/to/project")

# Analyze requirements
analysis = helper.analyze_requirements(user_request)

# Create plan
plan = helper.create_implementation_plan(requirements)

# Request prototype
helper.request_code_prototype(todo, requirements, files)

# Review code
review = helper.review_code(todo, git_diff)

# Generate commit message
commit_msg = helper.generate_commit_message(todo_description)
```

#### CLI Tool

```bash
# Analyze requirements
python scripts/codex_helper.py analyze requirements.txt

# Create plan
python scripts/codex_helper.py plan requirements.txt plan.txt

# Generate commit message
python scripts/codex_helper.py commit "Implement user authentication"
```

### 💡 Core Principles

1. **Codex advises, Claude decides** - Final decision authority with Claude
2. **Debate is essential** - Disagreements lead to better solutions
3. **Never skip critical thinking** - Question everything
4. **Always rewrite to production standards** - No copy-paste
5. **Verify at every step** - Trust but verify
6. **Commit after each todo** - Save incremental progress

### 📁 Project Structure

```
codex-collaboration/
├── SKILL.md                          # Main skill documentation
├── scripts/
│   └── codex_helper.py              # Python helper script
└── references/
    ├── workflow-details.md          # Detailed workflow (250+ lines)
    ├── codex-commands.md            # Codex CLI command reference
    └── reverse-engineering.md       # Reverse code analysis guide
```

### 📚 Documentation

- [Usage Guide](USAGE_GUIDE.md) - Detailed usage instructions
- [Skill Overview](SKILL_OVERVIEW.md) - Feature overview
- [Update Notes](UPDATE_NOTES.md) - Latest updates

### ⚙️ Configuration

Default settings:
- **Model**: `gpt-5.2-codex`
- **Reasoning Level**: `xhigh`
- **Working Mode**: Plan-based with todolist

### 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### 📄 License

MIT License - See [LICENSE](LICENSE) file for details

### 🙏 Acknowledgments

- [OpenAI Codex](https://openai.com/codex/) - Powerful programming assistant
- [Anthropic Claude](https://www.anthropic.com/) - Excellent AI assistant platform

### 📧 Contact

Questions or suggestions? Feel free to:
- Submit an [Issue](../../issues)
- Start a [Discussion](../../discussions)

---

**Star ⭐ this repository if you find it helpful!**
