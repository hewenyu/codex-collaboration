# 贡献指南 | Contributing Guide

感谢您对 Codex-Collaboration Skill 的关注！我们欢迎所有形式的贡献。

Thank you for your interest in contributing to Codex-Collaboration Skill! We welcome all forms of contributions.

[中文](#中文) | [English](#english)

---

## 中文

### 🤝 如何贡献

我们欢迎以下类型的贡献：
- 🐛 Bug 报告
- 💡 功能建议
- 📝 文档改进
- 🔧 代码优化
- 🌐 翻译改进
- 📖 使用案例分享

### 📋 贡献流程

#### 1. Fork 仓库

点击右上角的 "Fork" 按钮，将仓库 fork 到您的账号下。

#### 2. 克隆到本地

```bash
git clone https://github.com/hewenyu/codex-collaboration.git
cd codex-collaboration
```

#### 3. 创建分支

```bash
# 创建并切换到新分支
git checkout -b feature/your-feature-name

# 或修复bug
git checkout -b fix/bug-description
```

**分支命名规范：**
- `feature/xxx` - 新功能
- `fix/xxx` - Bug 修复
- `docs/xxx` - 文档更新
- `refactor/xxx` - 代码重构
- `perf/xxx` - 性能优化

#### 4. 进行修改

- 保持代码风格一致
- 添加必要的注释
- 更新相关文档
- 确保修改符合项目目标

#### 5. 测试您的修改

```bash
# 如果修改了 Python 代码，测试脚本
python scripts/codex_helper.py --help

# 如果修改了 skill，重新打包测试
python /path/to/skill-creator/scripts/package_skill.py codex-collaboration ./
```

#### 6. 提交修改

```bash
# 暂存修改
git add .

# 提交（使用 Conventional Commits 格式）
git commit -m "feat: add new optimization feature"

# 或
git commit -m "fix: correct typo in documentation"
```

**提交信息格式：**
```
类型(范围): 简短描述

详细描述（可选）
```

**类型：**
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `refactor`: 代码重构
- `perf`: 性能优化
- `test`: 测试相关
- `chore`: 构建/工具相关

#### 7. 推送到 GitHub

```bash
git push origin feature/your-feature-name
```

#### 8. 创建 Pull Request

1. 访问您 fork 的仓库页面
2. 点击 "Compare & pull request"
3. 填写 PR 标题和描述：
   - 清晰说明改动内容
   - 解释为什么需要这个改动
   - 列出相关的 Issue（如有）
4. 点击 "Create pull request"

### 📝 代码规范

#### Python 代码

- 遵循 PEP 8 规范
- 使用有意义的变量名
- 添加类型提示（Type Hints）
- 编写清晰的文档字符串

**示例：**
```python
def generate_commit_message(
    self,
    todo_description: str,
    git_diff_staged: str = None
) -> str:
    """
    Generate a conventional commit message for the completed todo
    
    Args:
        todo_description: The TODO that was completed
        git_diff_staged: Optional git diff of staged changes
        
    Returns:
        Commit message in conventional format
    """
    # 实现...
```

#### Markdown 文档

- 使用清晰的标题层级
- 添加代码示例
- 保持中英文双语（如适用）
- 使用表格和列表提高可读性

#### Skill 内容

- 保持简洁明了
- 提供具体示例
- 引用相关的 references 文件
- 遵循 skill-creator 的最佳实践

### 🐛 报告 Bug

在提交 Bug 报告前：
1. 搜索现有的 Issues，确保未被报告过
2. 使用最新版本测试
3. 准备最小可复现示例

**Bug 报告应包含：**
- 问题描述
- 复现步骤
- 预期行为
- 实际行为
- 环境信息（OS、Python版本、Codex版本等）
- 截图或错误日志（如有）

**模板：**
```markdown
### 问题描述
简要描述问题...

### 复现步骤
1. 执行命令 `...`
2. 观察到 `...`
3. 预期应该 `...`

### 环境
- OS: macOS 14.0
- Python: 3.11.0
- Codex CLI: 1.2.0
- Skill Version: 1.0.0

### 错误信息
```
粘贴错误日志...
```
```

### 💡 功能建议

在提交功能建议前：
1. 检查是否已有类似建议
2. 考虑是否符合项目目标
3. 思考实现方案

**功能建议应包含：**
- 功能描述
- 使用场景
- 预期收益
- 可能的实现方案
- 可能的替代方案

### 📚 改进文档

文档改进非常重要！您可以：
- 修正错别字
- 改进措辞
- 添加示例
- 翻译文档
- 更新过时信息

### 🧪 测试

如果添加新功能，请：
1. 编写测试用例
2. 确保所有测试通过
3. 测试边缘情况
4. 更新相关文档

### 📦 重新打包 Skill

修改 skill 内容后：

```bash
# 验证 skill 结构
python /path/to/skill-creator/scripts/validate_skill.py codex-collaboration

# 打包 skill
python /path/to/skill-creator/scripts/package_skill.py codex-collaboration ./

# 测试打包的 skill
# 在 Claude 中导入测试
```

### ⚖️ 许可协议

- 所有贡献将在 MIT License 下发布
- 提交 PR 即表示您同意这一点
- 确保不包含受版权保护的内容

### 🤔 需要帮助？

- 查看 [README.md](README.md)
- 阅读 [USAGE_GUIDE.md](USAGE_GUIDE.md)
- 查看现有的 [Issues](../../issues)
- 在 [Discussions](../../discussions) 提问

### 🎯 项目目标

贡献时请记住项目的核心目标：
1. **批判性思考** - 强制质疑和验证
2. **生产质量** - 企业级代码标准
3. **严格流程** - 结构化的开发工作流
4. **协作验证** - Claude和Codex相互验证
5. **持续改进** - 从反馈中学习优化

### 📊 PR 审核标准

您的 PR 将被审核：
- ✅ 代码质量和风格
- ✅ 功能完整性
- ✅ 文档完整性
- ✅ 测试覆盖
- ✅ 无破坏性变更（或有充分说明）
- ✅ 符合项目目标

### 🙏 致谢

所有贡献者将被列入：
- README.md 的贡献者部分
- CHANGELOG.md 中的版本记录

---

## English

### 🤝 How to Contribute

We welcome the following types of contributions:
- 🐛 Bug reports
- 💡 Feature suggestions
- 📝 Documentation improvements
- 🔧 Code optimizations
- 🌐 Translation improvements
- 📖 Use case sharing

### 📋 Contribution Process

#### 1. Fork the Repository

Click the "Fork" button in the upper right corner.

#### 2. Clone Locally

```bash
git clone https://github.com/hewenyu/codex-collaboration.git
cd codex-collaboration
```

#### 3. Create a Branch

```bash
# Create and switch to new branch
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b fix/bug-description
```

**Branch Naming Convention:**
- `feature/xxx` - New features
- `fix/xxx` - Bug fixes
- `docs/xxx` - Documentation updates
- `refactor/xxx` - Code refactoring
- `perf/xxx` - Performance optimizations

#### 4. Make Changes

- Keep code style consistent
- Add necessary comments
- Update related documentation
- Ensure changes align with project goals

#### 5. Test Your Changes

```bash
# If modified Python code, test scripts
python scripts/codex_helper.py --help

# If modified skill, repackage and test
python /path/to/skill-creator/scripts/package_skill.py codex-collaboration ./
```

#### 6. Commit Changes

```bash
# Stage changes
git add .

# Commit (use Conventional Commits format)
git commit -m "feat: add new optimization feature"

# Or
git commit -m "fix: correct typo in documentation"
```

**Commit Message Format:**
```
type(scope): brief description

Detailed description (optional)
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation update
- `refactor`: Code refactoring
- `perf`: Performance optimization
- `test`: Test related
- `chore`: Build/tool related

#### 7. Push to GitHub

```bash
git push origin feature/your-feature-name
```

#### 8. Create Pull Request

1. Visit your forked repository page
2. Click "Compare & pull request"
3. Fill in PR title and description:
   - Clearly describe the changes
   - Explain why the change is needed
   - List related Issues (if any)
4. Click "Create pull request"

### 📝 Code Standards

#### Python Code

- Follow PEP 8
- Use meaningful variable names
- Add type hints
- Write clear docstrings

**Example:**
```python
def generate_commit_message(
    self,
    todo_description: str,
    git_diff_staged: str = None
) -> str:
    """
    Generate a conventional commit message for the completed todo
    
    Args:
        todo_description: The TODO that was completed
        git_diff_staged: Optional git diff of staged changes
        
    Returns:
        Commit message in conventional format
    """
    # Implementation...
```

#### Markdown Documentation

- Use clear heading hierarchy
- Add code examples
- Maintain bilingual content (if applicable)
- Use tables and lists for readability

#### Skill Content

- Keep it concise and clear
- Provide specific examples
- Reference relevant reference files
- Follow skill-creator best practices

### 🐛 Report Bugs

Before submitting bug reports:
1. Search existing Issues to ensure it hasn't been reported
2. Test with the latest version
3. Prepare minimal reproducible example

**Bug Report Should Include:**
- Problem description
- Reproduction steps
- Expected behavior
- Actual behavior
- Environment info (OS, Python version, Codex version, etc.)
- Screenshots or error logs (if any)

### 💡 Feature Suggestions

Before submitting feature suggestions:
1. Check for similar suggestions
2. Consider if it aligns with project goals
3. Think about implementation

**Feature Suggestion Should Include:**
- Feature description
- Use cases
- Expected benefits
- Possible implementation
- Possible alternatives

### 📚 Improve Documentation

Documentation improvements are very important! You can:
- Fix typos
- Improve wording
- Add examples
- Translate documentation
- Update outdated information

### ⚖️ License

- All contributions will be released under MIT License
- Submitting a PR indicates your agreement
- Ensure no copyrighted content is included

### 🤔 Need Help?

- Check [README.md](README.md)
- Read [USAGE_GUIDE.md](USAGE_GUIDE.md)
- View existing [Issues](../../issues)
- Ask in [Discussions](../../discussions)

---

**Thank you for contributing! 🎉**
