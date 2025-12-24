# Codex CLI Command Reference

## Basic Usage

### Interactive Mode (for consultation and planning)
```bash
codex
# Opens interactive TUI for discussion and planning
```

### Exec Mode (for getting specific outputs)
```bash
codex exec "<task description>"
# Non-interactive mode - completes task and outputs result
# Streams progress to stderr, final message to stdout
```

### Model Selection
```bash
# Use gpt-5.2-codex model (default for this skill)
codex exec --model gpt-5.2-codex "<task>"

# Use with xhigh reasoning effort
codex exec --model gpt-5.2-codex --reasoning xhigh "<task>"
```

### Sandbox and Approval Modes
```bash
# Auto mode (default) - can read, edit, run commands in workspace
codex exec --sandbox workspace-write "<task>"

# Full access mode (be careful!)
codex exec --sandbox danger-full-access "<task>"

# Read-only mode (for analysis only)
codex exec --sandbox read-only "<task>"
```

### JSON Output Mode
```bash
# Get structured JSON output for parsing
codex exec --json "<task>" > output.jsonl

# With output schema for structured responses
codex exec --output-schema schema.json -o result.json "<task>"
```

### Working Directory
```bash
# Specify working directory
codex exec --directory /path/to/project "<task>"
```

## Common Task Patterns

### 1. Requirement Analysis
```bash
codex exec --model gpt-5.2-codex --reasoning xhigh "
Analyze the following requirement and provide:
1. Requirement clarification and potential ambiguities
2. Technical approach recommendations
3. Potential risks and considerations
4. Suggested implementation phases

Requirement: [USER_REQUIREMENT]
"
```

### 2. Implementation Plan Generation
```bash
codex exec --model gpt-5.2-codex --reasoning xhigh "
Create a detailed implementation plan with todolist for:
[REQUIREMENT_DESCRIPTION]

Provide:
1. Phase breakdown
2. Ordered todolist with dependencies
3. Estimated complexity for each task
4. Potential blockers
"
```

### 3. Code Prototype Request
```bash
codex exec --model gpt-5.2-codex --reasoning xhigh "
Generate a unified diff patch for implementing:
[TASK_DESCRIPTION]

Requirements:
- DO NOT make actual file changes
- Provide ONLY the unified diff patch format
- Include comments explaining key decisions
- Consider edge cases

Files to modify: [FILE_LIST]
" > prototype.patch
```

### 4. Code Review
```bash
codex exec --model gpt-5.2-codex --reasoning xhigh "
Review the following code changes and provide:
1. Correctness analysis
2. Potential bugs or issues
3. Performance considerations
4. Security concerns
5. Code quality and maintainability assessment

Diff:
$(git diff)

Original requirement: [REQUIREMENT]
"
```

### 5. Completeness Check
```bash
codex exec --model gpt-5.2-codex --reasoning xhigh "
Analyze whether the implementation meets all requirements:

Original requirement: [REQUIREMENT]
Implementation: [DESCRIPTION_OR_DIFF]

Check for:
1. Missing functionality
2. Edge cases not handled
3. Error handling completeness
4. Documentation needs
"
```

### 6. Reverse Engineering Analysis
```bash
codex exec --model gpt-5.2-codex --reasoning xhigh "
Analyze the reverse-engineered code in reverse_meta/ directory:

1. Identify implementation patterns and techniques
2. Extract optimization opportunities
3. Compare with our implementation approach
4. Suggest concrete improvements

Our implementation: [DESCRIPTION]
Reverse code location: reverse_meta/[PATH]
"
```

### 7. Commit Message Generation
```bash
codex exec --model gpt-5.2-codex --reasoning medium "
Generate a conventional commit message for:
TODO: [TODO_DESCRIPTION]
Changes: $(git diff --staged)

Format:
type(scope): brief description (50 chars max)

Detailed explanation of what was implemented,
why it was done this way, and any trade-offs.

Types: feat, fix, refactor, docs, test, chore
Output ONLY the commit message.
"
```

## Advanced Usage

### Capturing Structured Output
```bash
# Create schema file
cat > analysis_schema.json << 'EOF'
{
  "type": "object",
  "properties": {
    "issues": {"type": "array", "items": {"type": "string"}},
    "suggestions": {"type": "array", "items": {"type": "string"}},
    "risk_level": {"type": "string", "enum": ["low", "medium", "high"]}
  },
  "required": ["issues", "suggestions", "risk_level"]
}
EOF

# Use schema for structured response
codex exec --output-schema analysis_schema.json -o analysis.json "Review this code..."
```

### Chaining Multiple Codex Calls
```bash
# Step 1: Get plan
codex exec "Create implementation plan for X" > plan.txt

# Step 2: Get prototype based on plan
codex exec "Generate code prototype for: $(cat plan.txt)" > prototype.patch

# Step 3: Review the prototype
codex exec "Review this prototype: $(cat prototype.patch)"
```

## Important Notes

1. **Always specify model**: Use `--model gpt-5.2-codex` for this skill
2. **Use xhigh reasoning**: Add `--reasoning xhigh` for complex analysis
3. **Capture output**: Use redirection or `-o` flag to save results
4. **Working directory**: Always set `--directory` to project root
5. **Sandbox mode**: Use appropriate sandbox level for the task
6. **Parse output**: For programmatic use, use `--json` flag

## Error Handling

If Codex command fails:
```bash
# Check Codex status
codex --version

# Check authentication
codex login status

# View logs for debugging
# Codex streams progress to stderr, so check error messages there
```
