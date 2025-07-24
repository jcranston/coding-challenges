# Coding Problem Workspace

This project provides a standardized, AI-assisted workflow for adding, solving, and documenting coding problems, including LeetCode problems and custom challenges.

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