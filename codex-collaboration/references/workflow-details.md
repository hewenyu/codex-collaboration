# Detailed Collaboration Workflow

## Workflow Overview

This document describes the detailed step-by-step process for collaborating with Codex on programming tasks. The workflow emphasizes critical thinking, mutual verification, and continuous improvement.

## Core Philosophy

**Claude and Codex Relationship:**
- Claude: Primary executor, responsible for final implementation and decision-making
- Codex: Expert advisor, code reviewer, and thought partner
- Both: Engage in constructive debate to reach the best solution

**Critical Principles:**
1. **Codex provides reference, not gospel** - Always think critically about Codex's suggestions
2. **Question everything** - Challenge assumptions, including Codex's recommendations
3. **Seek truth through debate** - Disagreements lead to better solutions
4. **Maintain autonomy** - Claude makes final decisions on implementation
5. **Verify at every step** - Don't trust, verify

## Phase 1: Initial Requirement Analysis

### Step 1.1: Receive User Request
When user provides a programming task request.

### Step 1.2: Initial Understanding
Form preliminary understanding of:
- What user wants to accomplish
- Technical constraints
- Success criteria
- Potential approaches

### Step 1.3: Consult Codex for Requirement Analysis
Ask Codex to analyze and refine requirements:

```bash
codex exec --model gpt-5.2-codex --reasoning xhigh "
Analyze this requirement:
[USER_REQUEST]

Provide:
1. Requirement clarification questions
2. Potential ambiguities or missing information
3. Technical constraints to consider
4. Suggested success criteria
5. Risk assessment
"
```

### Step 1.4: Synthesize and Critique
- Review Codex's analysis critically
- Identify points of agreement and disagreement
- Form your own assessment
- **If you disagree with Codex, articulate why**

### Step 1.5: Refine Requirements
Based on combined analysis:
- Clarify ambiguities with user if needed
- Document refined requirements
- Establish clear acceptance criteria

## Phase 2: Planning and Todo Generation

### Step 2.1: Request Implementation Plan from Codex
Get Codex's perspective on implementation approach:

```bash
codex exec --model gpt-5.2-codex --reasoning xhigh "
Create detailed implementation plan for:
[REFINED_REQUIREMENTS]

Provide:
1. High-level architecture approach
2. Phase breakdown with clear boundaries
3. Ordered todolist with dependencies
4. Estimated complexity for each task
5. Potential blockers and mitigation strategies
6. Testing strategy
"
```

### Step 2.2: Develop Your Own Plan
Before accepting Codex's plan:
- Create your own implementation approach
- Consider alternative strategies
- Identify potential issues Codex may have missed

### Step 2.3: Comparative Analysis
Compare both plans:
- Where do they align?
- Where do they differ?
- What are the trade-offs?
- Which approach is better for this specific case?

### Step 2.4: Debate and Refinement
If significant differences exist, engage Codex in discussion:

```bash
codex exec --model gpt-5.2-codex --reasoning xhigh "
I propose a different approach for [ASPECT]:

My approach: [YOUR_APPROACH]
Your suggestion: [CODEX_APPROACH]

Debate:
1. Pros/cons of each approach
2. Which better addresses [SPECIFIC_REQUIREMENT]
3. Trade-offs in complexity vs maintainability
4. Performance implications
5. Recommendation with strong rationale
"
```

### Step 2.5: Finalize Plan and Todolist
Create final plan incorporating best elements:
- Todolist with clear tasks
- Dependencies between tasks
- Priority ordering
- Success criteria for each todo

**Todo Format:**
```
TODO-001: [Task Name]
Priority: High|Medium|Low
Dependencies: TODO-XXX, TODO-YYY
Acceptance Criteria:
- Criterion 1
- Criterion 2
Estimated Complexity: 1-10
```

## Phase 3: Todo Execution Loop

For each todo in the list, follow this process:

### Step 3.1: Todo Preparation
- Review todo details
- Understand acceptance criteria
- Check for dependencies
- Identify relevant reverse code (if any)

### Step 3.2: Request Code Prototype from Codex
**CRITICAL: Codex must provide unified diff patch, NOT actual changes**

```bash
codex exec --model gpt-5.2-codex --reasoning xhigh "
Generate a code prototype for:
TODO: [TODO_DESCRIPTION]
Requirements: [SPECIFIC_REQUIREMENTS]

IMPORTANT CONSTRAINTS:
- Provide ONLY unified diff patch format
- DO NOT make any actual file changes
- Include comments explaining key decisions
- Consider edge cases and error handling
- Reference reverse code insights if relevant: reverse_meta/[PATH]

Files that may need changes: [FILE_LIST]
" > todo_prototype.patch
```

### Step 3.3: Analyze Prototype
Review Codex's prototype critically:
- Does it address all requirements?
- Are there potential issues?
- Is the approach sound?
- Are there simpler alternatives?
- What edge cases might be missed?

### Step 3.4: Rewrite for Production
**DO NOT simply apply the patch**. Instead:
1. Use prototype as logical reference
2. Write production-grade code from scratch
3. Ensure:
   - Clean, readable code
   - Comprehensive error handling
   - Proper documentation
   - Maintainable structure
   - Enterprise-quality standards

### Step 3.5: Immediate Code Review
After implementing, immediately get Codex review:

```bash
codex exec --model gpt-5.2-codex --reasoning xhigh "
Review this implementation for TODO-XXX:

Original requirement: [TODO_DESCRIPTION]
Implementation: 
$(git diff)

Provide comprehensive review:
1. Correctness vs requirements
2. Potential bugs or issues
3. Edge cases not handled
4. Performance considerations
5. Security concerns
6. Code quality and maintainability
7. Comparison with my original prototype
8. Specific improvement suggestions
"
```

### Step 3.6: Critical Review Analysis
- Evaluate Codex's review points
- **Challenge feedback you disagree with**
- Prioritize action items
- Decide what to fix vs what to defer

### Step 3.7: Completeness Check
Verify nothing is missing:

```bash
codex exec --model gpt-5.2-codex --reasoning xhigh "
Check implementation completeness:

Original TODO: [TODO_DESCRIPTION]
Current implementation: [SUMMARY]

Verify:
1. All acceptance criteria met
2. Edge cases handled
3. Error handling complete
4. Tests needed/written
5. Documentation adequate
6. Any missing functionality
"
```

### Step 3.8: Debate Missing Items
If Codex identifies missing items:
- Assess if truly missing or intentionally deferred
- Debate priority and necessity
- **Argue your case if you disagree**
- Reach consensus on what to address now vs later

### Step 3.9: Reverse Code Optimization
If relevant reverse code exists:

```bash
codex exec --model gpt-5.2-codex --reasoning xhigh "
Analyze optimization opportunities:

Our implementation: [DESCRIPTION/DIFF]
Reverse code reference: reverse_meta/[PATH]

Compare and suggest:
1. Algorithmic improvements
2. Performance optimizations
3. Better patterns or structures
4. Edge case handling from reverse code
5. Specific code changes to consider
"
```

### Step 3.10: Apply Improvements
- Review optimization suggestions critically
- Implement improvements that make sense
- **Reject suggestions that don't fit our context**
- Document why certain optimizations were not applied

### Step 3.11: Final Verification
- Run tests
- Verify acceptance criteria met
- Ensure code quality standards maintained
- Document any trade-offs or decisions

### Step 3.12: Generate Commit Message with Codex

Before committing, ask Codex to generate a meaningful commit message:

```bash
codex exec --model gpt-5.2-codex --reasoning medium "
Generate a git commit message for this todo completion:

TODO: [TODO_DESCRIPTION]
Changes made: $(git diff --staged)

Provide a conventional commit message with:
- Type (feat/fix/refactor/docs/test/chore)
- Scope (if applicable)
- Brief description (50 chars max)
- Detailed body explaining what and why
- Any breaking changes or notes

Format:
type(scope): brief description

Detailed explanation of changes...
"
```

### Step 3.13: Commit Changes

Commit the completed todo to preserve the stage:

```bash
# Stage all changes
git add .

# Commit with the generated message
git commit -m "[COMMIT_MESSAGE_FROM_CODEX]"

# Optionally tag important milestones
git tag -a "todo-XXX-complete" -m "Completed TODO-XXX: [description]"
```

**Why commit after each todo:**
- Preserves incremental progress
- Allows easy rollback if needed
- Creates clear history of development
- Enables code review of individual todos
- Provides checkpoint for testing

### Step 3.14: Mark Todo Complete
- Update todo status
- Document completion notes
- Note any follow-up items
- Verify git commit successful
- Prepare for next todo

## Phase 4: Inter-Todo Activities

Between todos:
- Review overall progress
- Verify integration points
- Refactor if needed
- Update documentation
- Adjust remaining todos if needed

## Phase 5: Project Completion

### Final Review
After all todos complete:

```bash
codex exec --model gpt-5.2-codex --reasoning xhigh "
Final project review:

Original requirements: [INITIAL_REQUIREMENTS]
All implemented changes: $(git diff main)

Comprehensive assessment:
1. Requirement fulfillment
2. Code quality across the project
3. Consistency and coherence
4. Performance considerations
5. Security analysis
6. Maintainability assessment
7. Documentation completeness
8. Potential technical debt
9. Recommended improvements
"
```

### Critical Final Analysis
- Review Codex's final assessment
- Perform your own comprehensive review
- **Debate any major disagreements**
- Create action plan for any issues found

### Documentation
- Update project documentation
- Document architecture decisions
- Create usage guides
- Note future improvement areas

## Critical Thinking Prompts

Throughout the workflow, constantly ask:

**About Codex's Suggestions:**
- "Why did Codex suggest this approach?"
- "What assumptions is Codex making?"
- "Are there better alternatives?"
- "What is Codex not considering?"

**About Your Own Work:**
- "Am I following Codex blindly?"
- "Have I thought through this independently?"
- "What would I do differently without Codex?"
- "Am I making this more complex than needed?"

**About the Debate:**
- "Have we explored all alternatives?"
- "Is there a third option we're missing?"
- "What's the real trade-off here?"
- "Are we optimizing for the right thing?"

## Handling Disagreements

When you disagree with Codex:

1. **Articulate clearly** - State your position and reasoning
2. **Request clarification** - Ask Codex to explain its reasoning
3. **Present alternatives** - Show your proposed approach
4. **Demand justification** - Request concrete rationale
5. **Make the call** - Ultimately, you decide

Example disagreement dialogue:
```bash
codex exec --model gpt-5.2-codex --reasoning xhigh "
I disagree with your suggestion to [CODEX_SUGGESTION].

My reasoning:
1. [YOUR_REASON_1]
2. [YOUR_REASON_2]

I propose [YOUR_ALTERNATIVE] instead because [RATIONALE].

Respond:
1. Address my specific concerns
2. Explain why your approach is better
3. Critique my alternative
4. Provide concrete evidence or examples
5. Make a stronger case OR acknowledge my point
"
```

## Quality Standards

Every todo completion must meet:
- **Correctness**: Fully addresses requirements
- **Quality**: Production-grade code
- **Maintainability**: Clean, documented, readable
- **Robustness**: Handles edge cases and errors
- **Performance**: Reasonable efficiency
- **Security**: No obvious vulnerabilities

## Workflow Checklist

For each todo:
- [ ] Initial understanding formed
- [ ] Codex prototype requested (diff only!)
- [ ] Prototype analyzed critically
- [ ] Production code written from scratch
- [ ] Immediate review from Codex obtained
- [ ] Review feedback evaluated critically
- [ ] Completeness verified with Codex
- [ ] Missing items debated and resolved
- [ ] Reverse code optimization explored
- [ ] Improvements applied selectively
- [ ] Final verification passed
- [ ] Commit message generated with Codex
- [ ] Changes committed to git
- [ ] Todo marked complete

## Git Commit Best Practices

### Why Commit After Each Todo

Committing after each todo completion provides:
- **Incremental progress preservation** - Each completed task is saved
- **Easy rollback capability** - Can revert to any previous todo state
- **Clear development history** - Shows logical progression of work
- **Individual todo review** - Each commit can be reviewed separately
- **Testing checkpoints** - Can test at each stage
- **Collaboration support** - Team can see progress in detail
- **Debugging aid** - Easier to identify when issues were introduced

### Conventional Commit Format

Use conventional commits for consistency:

```
type(scope): brief description (50 chars max)

Detailed body explaining:
- What was implemented
- Why it was done this way
- Any important decisions or trade-offs
- Breaking changes if any

Refs: #issue-number (if applicable)
```

**Types:**
- `feat`: New feature or functionality
- `fix`: Bug fix
- `refactor`: Code restructuring without behavior change
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements
- `style`: Code style changes (formatting, etc.)

**Scope (optional):**
- Component or module affected (e.g., auth, api, ui, db)

### Generating Commit Messages with Codex

Always use Codex to generate professional commit messages:

```bash
codex exec --model gpt-5.2-codex --reasoning medium "
Generate a conventional commit message for:

TODO: [TODO_DESCRIPTION]
Changes made: $(git diff --staged)

Requirements:
- Use conventional commit format
- First line max 50 chars
- Body explains what and why (not how)
- Professional and clear
- Focus on business/technical value

Output ONLY the commit message.
"
```

### Commit Workflow

1. **Review changes before staging:**
   ```bash
   git status
   git diff
   ```

2. **Stage changes:**
   ```bash
   git add .
   # Or selectively:
   git add src/auth.py tests/test_auth.py
   ```

3. **Generate commit message:**
   ```bash
   # Using helper script
   python scripts/codex_helper.py commit "Implement JWT token service"
   
   # Or directly with Codex
   codex exec --model gpt-5.2-codex --reasoning medium "..."
   ```

4. **Commit with message:**
   ```bash
   # For single-line message:
   git commit -m "feat(auth): implement JWT token service"
   
   # For multi-line message:
   git commit -m "feat(auth): implement JWT token service

   Implemented JWT token generation and validation service with:
   - HS256 algorithm for signing
   - Configurable expiration times
   - Secure secret key management
   - Comprehensive error handling for invalid tokens
   
   This provides the foundation for user authentication."
   
   # Or use editor for longer messages:
   git commit
   ```

5. **Optional: Tag important milestones:**
   ```bash
   git tag -a "todo-003-complete" -m "Completed user authentication"
   ```

6. **Verify commit:**
   ```bash
   git log -1 --stat
   ```

### Commit Message Examples

**Feature implementation:**
```
feat(auth): implement JWT token service

Created JWTService class with token generation and validation.
Used HS256 algorithm for signing with configurable expiration.
Implemented secure secret key management via environment variables.
Added comprehensive error handling for malformed/expired tokens.

This establishes the core authentication mechanism for the API.
```

**Bug fix:**
```
fix(api): handle null user ID in request context

Fixed NullPointerException when user ID is missing from context.
Added validation check before accessing user ID.
Returns 401 Unauthorized if user ID is null.

Resolves issue where unauthenticated requests crashed the server.
```

**Refactoring:**
```
refactor(db): extract connection pooling to separate module

Moved database connection pool logic from main app to db/pool.py.
Created ConnectionPool class with configurable pool size.
Improved testability by isolating connection management.

No functional changes, purely organizational improvement.
```

**Documentation:**
```
docs(api): add authentication endpoint documentation

Added comprehensive API documentation for:
- POST /auth/login
- POST /auth/refresh
- POST /auth/logout

Included request/response examples and error codes.
```

### Common Mistakes to Avoid

❌ **Vague messages:**
```
git commit -m "fix stuff"
git commit -m "updates"
git commit -m "wip"
```

❌ **Too much in one commit:**
```
feat: implement auth, fix db bug, update docs, refactor utils
```

❌ **Messages that don't explain why:**
```
refactor: changed function signature
# Why? What benefit does this provide?
```

✅ **Good messages:**
```
feat(auth): implement JWT token service
# Clear what was added

fix(db): prevent connection leak on query timeout
# Clear what problem was solved

refactor(utils): extract validation to separate module for reusability
# Clear what changed and why
```

### Interactive Commit Review

Before committing, ask yourself:
- Does this commit represent one complete todo?
- Is the message clear and professional?
- Would someone reviewing this understand what and why?
- Are there any uncommitted changes that should be in a separate commit?
- Is the commit message generated by Codex accurate?

### Pushing Commits

After completing several todos:
```bash
# Review commit history
git log --oneline -10

# Push to remote
git push origin feature-branch

# Or push with tags
git push origin feature-branch --tags
```

## Anti-Patterns to Avoid

1. **Blind acceptance** - Never apply Codex's suggestions without critical thought
2. **Copy-paste coding** - Never directly apply patches without rewriting
3. **Skipping debate** - Never avoid disagreement; it leads to better code
4. **Ignoring reverse code** - Always check for optimization opportunities
5. **Rushing reviews** - Take time to thoroughly analyze each step
6. **Missing verification** - Always verify completeness and correctness
7. **Siloed thinking** - Continuously consider the bigger picture

## Success Metrics

A successful collaboration achieves:
- High-quality, maintainable code
- Comprehensive requirement fulfillment
- Well-reasoned architectural decisions
- Robust error handling
- Optimized where it matters
- Clear documentation
- Confidence in the solution through rigorous debate
