#!/usr/bin/env python3
"""
Codex Helper Script

This script provides convenient wrapper functions for calling Codex CLI
with appropriate parameters for the collaboration workflow.
"""

import subprocess
import json
import sys
from pathlib import Path
from typing import Optional, Dict, Any, List


class CodexHelper:
    """Helper class for Codex CLI interactions"""
    
    DEFAULT_MODEL = "gpt-5.2-codex"
    DEFAULT_REASONING = "xhigh"
    
    def __init__(self, project_dir: Optional[str] = None):
        """
        Initialize CodexHelper
        
        Args:
            project_dir: Project root directory (default: current directory)
        """
        self.project_dir = Path(project_dir) if project_dir else Path.cwd()
        
    def _build_command(
        self,
        task: str,
        model: str = DEFAULT_MODEL,
        reasoning: str = DEFAULT_REASONING,
        json_output: bool = False,
        output_file: Optional[str] = None,
        sandbox: str = "workspace-write"
    ) -> List[str]:
        """Build Codex command with appropriate flags"""
        cmd = [
            "codex", "exec",
            "--model", model,
            "--reasoning", reasoning,
            "--directory", str(self.project_dir),
            "--sandbox", sandbox
        ]
        
        if json_output:
            cmd.append("--json")
        
        if output_file:
            cmd.extend(["-o", output_file])
        
        cmd.append(task)
        return cmd
    
    def execute(
        self,
        task: str,
        capture_output: bool = True,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Execute Codex command
        
        Args:
            task: Task description for Codex
            capture_output: Whether to capture and return output
            **kwargs: Additional arguments for _build_command
            
        Returns:
            Dict with 'stdout', 'stderr', 'returncode'
        """
        cmd = self._build_command(task, **kwargs)
        
        print(f"🤖 Executing Codex: {' '.join(cmd[:6])}... (see full command in debug)")
        print(f"📝 Task: {task[:100]}{'...' if len(task) > 100 else ''}")
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=capture_output,
                text=True,
                cwd=self.project_dir
            )
            
            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode,
                "success": result.returncode == 0
            }
        except FileNotFoundError:
            print("❌ Error: Codex CLI not found. Please install it first.")
            print("   npm install -g @openai/codex")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Error executing Codex: {e}")
            return {
                "stdout": "",
                "stderr": str(e),
                "returncode": 1,
                "success": False
            }
    
    def analyze_requirements(self, user_request: str) -> str:
        """
        Phase 1: Analyze and refine requirements
        
        Args:
            user_request: User's original request
            
        Returns:
            Codex's analysis output
        """
        task = f"""
Analyze this requirement:
{user_request}

Provide:
1. Requirement clarification questions
2. Potential ambiguities or missing information
3. Technical constraints to consider
4. Suggested success criteria
5. Risk assessment
"""
        result = self.execute(task)
        return result["stdout"] if result["success"] else result["stderr"]
    
    def create_implementation_plan(
        self,
        refined_requirements: str,
        output_file: Optional[str] = None
    ) -> str:
        """
        Phase 2: Create implementation plan and todolist
        
        Args:
            refined_requirements: Refined requirements from Phase 1
            output_file: Optional file to save plan
            
        Returns:
            Implementation plan
        """
        task = f"""
Create detailed implementation plan for:
{refined_requirements}

Provide:
1. High-level architecture approach
2. Phase breakdown with clear boundaries
3. Ordered todolist with dependencies
4. Estimated complexity for each task (1-10 scale)
5. Potential blockers and mitigation strategies
6. Testing strategy

Format todolist as:
TODO-XXX: [Task Name]
Priority: High|Medium|Low
Dependencies: TODO-YYY (if any)
Acceptance Criteria:
- Criterion 1
- Criterion 2
Complexity: N
"""
        result = self.execute(task, output_file=output_file)
        return result["stdout"] if result["success"] else result["stderr"]
    
    def request_code_prototype(
        self,
        todo_description: str,
        requirements: str,
        files: List[str],
        reverse_code_path: Optional[str] = None,
        output_file: str = "prototype.patch"
    ) -> str:
        """
        Phase 3: Request code prototype (unified diff only!)
        
        Args:
            todo_description: TODO task description
            requirements: Specific requirements for this task
            files: List of files that may need changes
            reverse_code_path: Optional path to reverse code reference
            output_file: File to save the diff patch
            
        Returns:
            Path to prototype patch file
        """
        reverse_note = ""
        if reverse_code_path:
            reverse_note = f"\n- Reference reverse code insights: {reverse_code_path}"
        
        task = f"""
Generate a code prototype for:
TODO: {todo_description}
Requirements: {requirements}

IMPORTANT CONSTRAINTS:
- Provide ONLY unified diff patch format
- DO NOT make any actual file changes
- Include comments explaining key decisions
- Consider edge cases and error handling{reverse_note}

Files that may need changes: {', '.join(files)}
"""
        result = self.execute(task, output_file=output_file)
        if result["success"]:
            print(f"✅ Prototype saved to: {output_file}")
            return output_file
        else:
            print(f"❌ Failed to generate prototype: {result['stderr']}")
            return ""
    
    def review_code(
        self,
        todo_description: str,
        git_diff: str,
        output_file: Optional[str] = None
    ) -> str:
        """
        Phase 3: Review implemented code
        
        Args:
            todo_description: Original TODO description
            git_diff: Git diff of changes
            output_file: Optional file to save review
            
        Returns:
            Review output
        """
        task = f"""
Review this implementation:

Original requirement: {todo_description}
Implementation:
{git_diff}

Provide comprehensive review:
1. Correctness vs requirements
2. Potential bugs or issues
3. Edge cases not handled
4. Performance considerations
5. Security concerns
6. Code quality and maintainability
7. Specific improvement suggestions with examples
"""
        result = self.execute(task, output_file=output_file)
        return result["stdout"] if result["success"] else result["stderr"]
    
    def check_completeness(
        self,
        todo_description: str,
        implementation_summary: str,
        json_output: bool = True
    ) -> Dict[str, Any]:
        """
        Phase 3: Check implementation completeness
        
        Args:
            todo_description: Original TODO description
            implementation_summary: Summary of implementation
            json_output: Return structured JSON
            
        Returns:
            Completeness analysis
        """
        task = f"""
Check implementation completeness:

Original TODO: {todo_description}
Current implementation: {implementation_summary}

Verify:
1. All acceptance criteria met (list which are met, which are missing)
2. Edge cases handled (list handled cases and missing ones)
3. Error handling complete (identify gaps)
4. Tests needed/written
5. Documentation adequate
6. Any missing functionality

{"Format as JSON with structure: {'criteria_met': [], 'criteria_missing': [], 'edge_cases_handled': [], 'edge_cases_missing': [], 'missing_functionality': [], 'overall_complete': bool}" if json_output else ""}
"""
        result = self.execute(task, json_output=json_output)
        
        if json_output and result["success"]:
            try:
                return json.loads(result["stdout"])
            except json.JSONDecodeError:
                return {"error": "Failed to parse JSON", "raw": result["stdout"]}
        
        return result["stdout"] if result["success"] else result["stderr"]
    
    def analyze_reverse_code(
        self,
        our_implementation: str,
        reverse_code_path: str,
        output_file: Optional[str] = None
    ) -> str:
        """
        Phase 3: Analyze reverse code for optimization opportunities
        
        Args:
            our_implementation: Description or diff of our implementation
            reverse_code_path: Path to reverse code in reverse_meta/
            output_file: Optional file to save analysis
            
        Returns:
            Optimization analysis
        """
        task = f"""
Analyze optimization opportunities:

Our implementation: {our_implementation}
Reverse code reference: {reverse_code_path}

Compare and suggest:
1. Algorithmic improvements (be specific with examples)
2. Performance optimizations (concrete techniques)
3. Better patterns or structures (show code examples)
4. Edge case handling from reverse code (what are we missing?)
5. Specific code changes to consider (provide diff snippets)

For each suggestion, provide:
- Description of improvement
- Why it's better
- Estimated impact (high/medium/low)
- Effort to implement (small/medium/large)
"""
        result = self.execute(task, output_file=output_file)
        return result["stdout"] if result["success"] else result["stderr"]
    
    def debate_approach(
        self,
        aspect: str,
        your_approach: str,
        codex_suggestion: str,
        context: str
    ) -> str:
        """
        Engage Codex in debate about different approaches
        
        Args:
            aspect: What aspect is being debated
            your_approach: Your proposed approach
            codex_suggestion: Codex's suggestion
            context: Additional context
            
        Returns:
            Codex's debate response
        """
        task = f"""
I propose a different approach for {aspect}:

My approach: {your_approach}
Your suggestion: {codex_suggestion}

Context: {context}

Debate:
1. Pros/cons of each approach
2. Which better addresses the specific requirements
3. Trade-offs in complexity vs maintainability
4. Performance implications
5. Provide strong rationale for your recommendation

Challenge my approach - point out flaws I may not see.
If my approach is better, acknowledge it.
If yours is better, convince me with concrete evidence.
"""
        result = self.execute(task)
        return result["stdout"] if result["success"] else result["stderr"]
    
    def final_review(self, requirements: str, git_diff_all: str) -> str:
        """
        Phase 4: Final project review
        
        Args:
            requirements: Original requirements
            git_diff_all: Complete git diff of all changes
            
        Returns:
            Final review output
        """
        task = f"""
Final project review:

Original requirements: {requirements}
All implemented changes:
{git_diff_all[:10000]}  # Limit for context

Comprehensive assessment:
1. Requirement fulfillment (complete analysis)
2. Code quality across the project
3. Consistency and coherence
4. Performance considerations
5. Security analysis
6. Maintainability assessment
7. Documentation completeness
8. Potential technical debt
9. Recommended improvements (prioritized)

Be thorough and critical. Point out real issues.
"""
        result = self.execute(task)
        return result["stdout"] if result["success"] else result["stderr"]
    
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
            Commit message
        """
        # Get staged diff if not provided
        if git_diff_staged is None:
            try:
                result = subprocess.run(
                    ["git", "diff", "--staged"],
                    capture_output=True,
                    text=True,
                    cwd=self.project_dir
                )
                git_diff_staged = result.stdout
            except Exception as e:
                print(f"Warning: Could not get git diff: {e}")
                git_diff_staged = ""
        
        task = f"""
Generate a git commit message for this todo completion:

TODO: {todo_description}
Changes made:
{git_diff_staged[:5000]}  # Limit for context

Provide a conventional commit message following this format:

type(scope): brief description (50 chars max)

Detailed explanation of changes, including:
- What was implemented
- Why it was done this way
- Any important decisions or trade-offs

Types: feat, fix, refactor, docs, test, chore, perf, style
Scope: optional, e.g., auth, api, ui, db

Requirements:
- First line is concise (50 chars max)
- Body explains what and why (not how - code shows how)
- Professional and clear
- Focus on the business/technical value

Output ONLY the commit message, no preamble.
"""
        result = self.execute(task, reasoning="medium")  # Medium is fine for commit messages
        
        if result["success"]:
            # Clean up the output
            commit_msg = result["stdout"].strip()
            # Remove any markdown code fences if present
            commit_msg = commit_msg.replace("```", "").strip()
            return commit_msg
        else:
            # Fallback to simple message
            return f"chore: complete {todo_description}"


# CLI interface for the helper script
def main():
    """Command-line interface for CodexHelper"""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python codex_helper.py analyze <requirements_file>")
        print("  python codex_helper.py plan <requirements_file> [output_file]")
        print("  python codex_helper.py prototype <todo> <requirements> <files...>")
        print("  python codex_helper.py review <todo_file> <diff_file>")
        print("  python codex_helper.py completeness <todo_file> <summary>")
        print("  python codex_helper.py reverse <our_code> <reverse_path>")
        print("  python codex_helper.py commit <todo_description>")
        print("  python codex_helper.py final <requirements_file>")
        sys.exit(1)
    
    command = sys.argv[1]
    helper = CodexHelper()
    
    if command == "analyze":
        with open(sys.argv[2]) as f:
            requirements = f.read()
        print(helper.analyze_requirements(requirements))
    
    elif command == "plan":
        with open(sys.argv[2]) as f:
            requirements = f.read()
        output = sys.argv[3] if len(sys.argv) > 3 else None
        print(helper.create_implementation_plan(requirements, output))
    
    elif command == "prototype":
        todo = sys.argv[2]
        requirements = sys.argv[3]
        files = sys.argv[4:]
        helper.request_code_prototype(todo, requirements, files)
    
    elif command == "review":
        with open(sys.argv[2]) as f:
            todo = f.read()
        with open(sys.argv[3]) as f:
            diff = f.read()
        print(helper.review_code(todo, diff))
    
    elif command == "completeness":
        with open(sys.argv[2]) as f:
            todo = f.read()
        summary = sys.argv[3]
        result = helper.check_completeness(todo, summary)
        print(json.dumps(result, indent=2))
    
    elif command == "reverse":
        our_code = sys.argv[2]
        reverse_path = sys.argv[3]
        print(helper.analyze_reverse_code(our_code, reverse_path))
    
    elif command == "commit":
        todo = sys.argv[2]
        commit_msg = helper.generate_commit_message(todo)
        print("\n📝 Generated commit message:")
        print("=" * 60)
        print(commit_msg)
        print("=" * 60)
        print("\nTo commit, run:")
        print(f'  git add . && git commit -m "{commit_msg.split(chr(10))[0]}"')
        if "\n\n" in commit_msg:
            # Multi-line commit
            print("\nOr for full message:")
            print(f'  git add . && git commit -F- <<EOF\n{commit_msg}\nEOF')
    
    elif command == "final":
        with open(sys.argv[2]) as f:
            requirements = f.read()
        # Get git diff
        result = subprocess.run(
            ["git", "diff", "main"],
            capture_output=True,
            text=True
        )
        print(helper.final_review(requirements, result.stdout))
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
