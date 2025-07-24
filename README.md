# Coding Problem Workspace

A modern, AI-assisted coding problem workspace for interview prep, algorithm mastery, and collaborative learning. This project provides:
- A large, organized set of coding problems (including LeetCode and custom challenges)
- Automated workflows for generating, testing, and documenting problems using AI tools (like Cursor, Copilot, or ChatGPT)
- Scripts and context files for seamless onboarding, code quality, and reproducible practice
- Support for dev containers, Docker, and modern Python tooling

Whether you're preparing for interviews, practicing algorithms, or sharing with friends, this workspace helps you focus on learning and problem-solving—not boilerplate setup.

### 🚀 Onboarding for AI Assistants (Cursor, Copilot, etc.)

To load project context into your AI assistant, you have two options:

1. **Copy and paste the onboarding prompt below** (the code block) into your AI agent when you open this project.
2. **Or run:**
   ```sh
   make print-ai-onboarding
   ```
   This will print the same onboarding prompt below, which you can then copy and paste into your AI agent.

**Onboarding prompt:**
```
Please read `ai_context/README.md` and all referenced files in `ai_context/` before assisting. Use these as your context for all workflows, code generation, and automation in this project.
```

- This ensures the AI understands all project-specific workflows, code style, and automation policies.
- For more details, see [ai_context/README.md](ai_context/README.md).

---

**Note:** The checked-in codebase on GitHub includes solutions implemented by the author (jcranston) as part of his own interview prep and workflow. If you want to start fresh (with only problems and tests, no solutions or explanations), see the [Wipe Solutions Script](#-wipe-solutions-script-for-fresh-starts) below.

---

## Key Features
- **AI Context-Driven Workflow:** Use AI context files to automate and standardize problem creation, solution, testing, and documentation.
- **Flexible LeetCode Problem Addition:**
  - Add problems by LeetCode number (e.g., 217) or by name (e.g., "contains duplicate").
  - The system will map user-supplied names to the correct LeetCode problem number and canonical name (e.g., "triplet sum to zero" → LeetCode 15, "3Sum").
  - The README for each problem will include the LeetCode number, canonical name, and your supplied title.
  - See [ai_context/leetcode_problem_mapping.md](ai_context/leetcode_problem_mapping.md) for details.
- **Scripted Utilities:** Scripts for problem status, batch addition, and more.
- **Consistent Directory Structure:** All problems follow the same structure for easy navigation and automation.

## How to Use This Project

You can use this codebase in several ways:

- **Add new problems:**
  - By LeetCode number or name (see examples above)
  - By running scripts (see below)
  - By using the AI (Cursor, VS Code Copilot, etc.)
- **Generate explanations:**
  - Ask the AI to generate an `EXPLANATION.md` for any problem.
- **Check problem status:**
  - Use the `problem_status.py` script or ask the AI to list unimplemented problems, missing explanations, etc.
- **Run and test solutions:**
  - Use `pytest` or `make test` to run all tests.
- **Work in a container or dev container:**
  - Use the provided scripts or open in Cursor/VS Code for a seamless dev environment.
- **Use Makefile commands:**
  - See below for a list of common commands.

For detailed workflows and advanced usage, see [ai_context/README.md](ai_context/README.md).

## Scripts

| Script                        | Purpose                                      |
|-------------------------------|----------------------------------------------|
| `scripts/add_challenge.sh`    | Scaffold a new problem directory             |
| `scripts/problem_status.py`   | List problems by implementation/explanation status |
| `scripts/run_in_container.sh` | Build and run the dev container              |

## Makefile Commands

| Command                | Description                                  |
|------------------------|----------------------------------------------|
| `make install`         | Install dependencies with Poetry             |
| `make test`            | Run all tests                                |
| `make lint`            | Run flake8 linting                           |
| `make format`          | Format code with black and isort             |
| `make build`           | Build Docker image                           |
| `make run`             | Run container                                |
| `make add-challenge NAME=...` | Add a new challenge                   |
| `make quality`         | Run format, lint, and test                   |
| `make stats`           | Show project statistics                      |
| `make problem-status ARGS="--all"` | Run the problem status utility   |
| ...                    | (see Makefile for more)                      |

## Running in a Container or Dev Container

- **Recommended:** Open the project in Cursor or VS Code and select “Reopen in Container.”
- **Manual:**
  - Build: `make build` or `./scripts/run_in_container.sh build`
  - Run: `make run` or `./scripts/run_in_container.sh run`
- **All dependencies and tools are pre-installed in the container.**

## Using AI Tools (Cursor, VS Code, etc.)

- You can use AI assistants to:
  - Add new problems (by name or number)
  - Generate explanations
  - Refactor or review code
  - Clarify problem statements
- See [ai_context/README.md](ai_context/README.md) for prompt examples and detailed workflows.

## Getting Started
- See [How to Use This Project](#how-to-use-this-project) and [ai_context/README.md](ai_context/README.md) for workflow guidance and context files.
- Use the provided scripts and AI prompts to automate your workflow.

---

Feel free to contribute or suggest improvements!

---

## 🧹 Wipe Solutions Script (For Fresh Starts)

If you want to start with only the problems and tests (no solution implementations or explanations), you can use the provided script:

```sh
# Dry run (shows what would be wiped)
python scripts/wipe_solutions.py --dry-run

# Actually wipe all solution implementations (keeps docstrings, stubs out with 'pass')
python scripts/wipe_solutions.py --yes

# Also remove all EXPLANATION.md files
python scripts/wipe_solutions.py --yes --wipe-explanations

# Backup all wiped files to a .backup directory before deleting
python scripts/wipe_solutions.py --yes --backup

# Combine options as needed
python scripts/wipe_solutions.py --yes --wipe-explanations --backup
```

> **Warning:** This is a destructive operation! Only run it if you want to start fresh.  
> By default, the script runs in dry-run mode and will not delete or overwrite anything unless you use `--yes`.