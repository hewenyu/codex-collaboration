---
name: codex-collaboration
description: "Collaborative programming workflow using OpenAI Codex CLI as an expert advisor. Use this skill for ANY programming task including code writing, debugging, refactoring, architecture design, code review, and documentation. This skill establishes a rigorous workflow where Claude executes and Codex advises, with critical thinking and debate at every step. Triggers include implementing features, fixing bugs, writing code, code review requests, technical planning, or any software development task."
---

# Codex Collaboration Skill

## Overview

This skill establishes a rigorous collaborative workflow between Claude (as primary executor) and OpenAI Codex CLI (as expert advisor and reviewer). The workflow emphasizes critical thinking, mutual verification, and continuous improvement through constructive debate.

**Key Principles:**
- **Claude executes, Codex advises** - Claude makes final implementation decisions
- **Critical thinking required** - Never blindly accept suggestions
- **Debate drives quality** - Disagreements lead to better solutions  
- **Verify at every step** - Review, question, and validate continuously
- **Production quality** - Always rewrite code for enterprise standards

**Default Configuration:**
- Model: `gpt-5.2-codex`
- Reasoning: `xhigh`
- Mode: Plan-based with todolist execution

## When to Use This Skill

**ALWAYS use this skill for:**
- Any programming or coding task
- Code review and debugging
- Architecture and design decisions
- Documentation writing (technical)
- Refactoring and optimization
- Feature implementation
- Bug fixing
- Technical analysis

**The workflow applies to ALL programming tasks, regardless of complexity.**

## Core Workflow

### Phase 1: Requirement Analysis & Planning

1. **Receive task from user**
2. **Form initial understanding** of requirements
3. **Consult Codex for requirement analysis:**
   ```bash
   codex exec --model gpt-5.2-codex --reasoning xhigh "
   Analyze this requirement: [USER_REQUEST]
   Provide: clarifications, ambiguities, constraints, criteria, risks
   "
   ```
4. **Critically evaluate Codex's analysis** - Form your own assessment
5. **Debate differences** if your analysis differs from Codex's
6. **Request implementation plan from Codex:**
   ```bash
   codex exec --model gpt-5.2-codex --reasoning xhigh "
   Create implementation plan: phases, todolist, dependencies, blockers
   "
   ```
7. **Develop your own plan** independently
8. **Compare both plans** and debate significant differences
9. **Finalize plan** incorporating best elements from both

### Phase 2: Todo Execution Loop

For each todo in the finalized plan:

1. **Request code prototype from Codex** (unified diff ONLY):
   ```bash
   codex exec --model gpt-5.2-codex --reasoning xhigh "
   Generate ONLY unified diff patch for: [TODO]
   DO NOT make actual file changes
   Include comments and edge case handling
   " > prototype.patch
   ```

2. **Analyze prototype critically:**
   - Does it fully address requirements?
   - Are there potential issues or gaps?
   - Is the approach sound?
   - What alternatives exist?

3. **Rewrite for production** - DO NOT simply apply the patch:
   - Use prototype as logical reference only
   - Write enterprise-quality code from scratch
   - Ensure clean, readable, maintainable code
   - Comprehensive error handling
   - Proper documentation

4. **Immediate code review from Codex:**
   ```bash
   codex exec --model gpt-5.2-codex --reasoning xhigh "
   Review implementation: correctness, bugs, edge cases, 
   performance, security, quality, improvements
   [Include git diff]
   "
   ```

5. **Critical review analysis:**
   - Evaluate each review point
   - Challenge feedback you disagree with
   - Prioritize action items
   - Decide what to fix vs defer

6. **Completeness check:**
   ```bash
   codex exec --model gpt-5.2-codex --reasoning xhigh "
   Check completeness: criteria met, edge cases, errors, 
   tests, documentation, missing functionality
   "
   ```

7. **Debate missing items** if any identified

8. **Reverse code optimization** (if applicable):
   ```bash
   codex exec --model gpt-5.2-codex --reasoning xhigh "
   Analyze reverse code for optimization:
   Our implementation: [DESCRIPTION]
   Reverse reference: reverse_meta/[PATH]
   "
   ```

9. **Apply selective improvements** - Only what makes sense

10. **Generate commit message with Codex:**
    ```bash
    codex exec --model gpt-5.2-codex --reasoning medium "
    Generate conventional commit message for:
    TODO: [DESCRIPTION]
    Changes: $(git diff --staged)
    "
    ```

11. **Commit changes to git:**
    ```bash
    git add .
    git commit -m "[CODEX_GENERATED_MESSAGE]"
    ```

12. **Mark todo complete** after verification

### Phase 3: Final Review

After all todos complete:

```bash
codex exec --model gpt-5.2-codex --reasoning xhigh "
Final project review: requirements, quality, security,
maintainability, documentation, technical debt
[Include complete git diff]
"
```

## Critical Thinking Requirements

Throughout the workflow, ALWAYS:

**Question Codex's suggestions:**
- Why this approach?
- What assumptions are being made?
- Are there better alternatives?
- What is being overlooked?

**Question your own work:**
- Am I following blindly?
- Have I thought independently?
- Am I overcomplicating?
- What would I do without Codex?

**Engage in debate:**
- Have we explored all options?
- Is there a third option?
- What's the real trade-off?
- Are we optimizing for the right thing?

## Handling Disagreements

When you disagree with Codex:

1. **Articulate clearly** - State position and reasoning
2. **Request clarification** - Ask Codex to explain
3. **Present alternatives** - Show your approach
4. **Demand justification** - Request concrete rationale
5. **Make the call** - You have final decision authority

Example:
```bash
codex exec --model gpt-5.2-codex --reasoning xhigh "
I disagree with [CODEX_SUGGESTION] because [REASONS].
I propose [ALTERNATIVE] instead because [RATIONALE].
Address my concerns, critique my alternative, 
provide evidence or acknowledge my point.
"
```

## Quality Standards

Every todo must meet:
- ✓ Correctness - Fully addresses requirements
- ✓ Quality - Production-grade code
- ✓ Maintainability - Clean, documented, readable
- ✓ Robustness - Handles edge cases and errors
- ✓ Performance - Reasonable efficiency
- ✓ Security - No obvious vulnerabilities

## Todo Checklist

For each todo:
- [ ] Codex prototype requested (diff only!)
- [ ] Prototype analyzed critically
- [ ] Production code written from scratch
- [ ] Immediate Codex review obtained
- [ ] Review feedback evaluated critically
- [ ] Completeness verified
- [ ] Missing items debated and resolved
- [ ] Reverse code optimization explored (if applicable)
- [ ] Improvements applied selectively
- [ ] Final verification passed
- [ ] Commit message generated with Codex
- [ ] Changes committed to git
- [ ] Todo marked complete

## Anti-Patterns to Avoid

❌ **Blind acceptance** - Never apply suggestions without critical thought
❌ **Copy-paste coding** - Never directly apply patches without rewriting  
❌ **Skipping debate** - Never avoid disagreement
❌ **Ignoring reverse code** - Always check for optimization opportunities
❌ **Rushing reviews** - Take time to thoroughly analyze
❌ **Missing verification** - Always verify completeness
❌ **Siloed thinking** - Consider the bigger picture

## Helper Script

Use `scripts/codex_helper.py` for convenient Codex interactions:

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

# Check completeness
completeness = helper.check_completeness(todo, summary)

# Analyze reverse code
optimizations = helper.analyze_reverse_code(our_code, reverse_path)
```

## Additional Resources

- **references/workflow-details.md** - Comprehensive step-by-step workflow with examples
- **references/codex-commands.md** - Complete Codex CLI command reference
- **references/reverse-engineering.md** - Guide to analyzing reverse code for optimization
- **scripts/codex_helper.py** - Python helper for Codex CLI interactions

## Quick Start Example

```bash
# User task: "Implement user authentication"

# 1. Analyze with Codex
codex exec --model gpt-5.2-codex --reasoning xhigh \
  "Analyze requirement: Implement user authentication with JWT"

# 2. Get plan
codex exec --model gpt-5.2-codex --reasoning xhigh \
  "Create implementation plan with todolist for JWT authentication"

# 3. For each todo, get prototype
codex exec --model gpt-5.2-codex --reasoning xhigh \
  "Generate unified diff patch ONLY for: Create JWT token service" \
  > prototype.patch

# 4. Review prototype, rewrite for production

# 5. Get review
codex exec --model gpt-5.2-codex --reasoning xhigh \
  "Review this implementation: $(git diff)"

# 6. Continue with next todo...
```

## Remember

- **Codex advises, Claude decides**
- **Debate is essential for quality**
- **Never skip critical thinking**
- **Always rewrite for production standards**
- **Verify at every step**

The goal is not speed, but **high-quality, well-reasoned code through rigorous collaboration**.
