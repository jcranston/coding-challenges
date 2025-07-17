# Coding Challenges

A modern, containerized environment for practicing Python coding challenges—perfect for interview prep, algorithm mastery, and leveraging AI tools like Cursor for rapid problem generation and solution review.

---

## Features

- **Isolated Python 3.11 environment** (via Docker/dev containers)
- **Poetry** for dependency management
- **pytest** for testing, **black** and **flake8** for code quality
- **Easy challenge generation** with scripts
- **AI/LLM (e.g., Cursor) integration** for generating new problems, solutions, and explanations
- **Ready-to-use in Cursor, VS Code, or any Docker-compatible IDE**

---

## Getting Started

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd coding_challenges
```

### 2. Build and Start the Dev Container

**Recommended:** Use [Cursor](https://www.cursor.so/) or VS Code Dev Containers for a seamless experience.

Or, use the provided scripts:

```sh
./scripts/run_in_container.sh build   # Build the Docker image
./scripts/run_in_container.sh run     # Start the container
```

This will drop you into a shell inside the container, with all dependencies installed.

### 3. Install Dependencies (if not using Docker)

```sh
poetry install
```

---

## Developing Inside the Container

The recommended way to develop in this project is to use **Dev Containers** (supported by [Cursor](https://www.cursor.so/) and VS Code). This provides a seamless, fully-configured development environment with all dependencies, linters, and tools pre-installed.

### **Recommended: Using Dev Containers (Cursor or VS Code)**
1. **Open the project folder in Cursor or VS Code.**
2. If prompted, select "Reopen in Container" (or use the Command Palette: `Dev Containers: Reopen in Container`).
3. The editor will build and connect to the container automatically. You can now:
   - Edit code with full Python support
   - Run and debug tests
   - Use integrated terminals and linters
   - Leverage AI features (in Cursor)

### **Alternative: Manual Docker Access**
If you prefer, you can connect to the running container using the terminal:

1. **Start the container:**
   ```sh
   ./scripts/run_in_container.sh run
   ```
2. **Open a shell in the container (if not already inside):**
   ```sh
   docker exec -it coding_challenges_dev /bin/zsh
   ```
3. **Develop as usual:**
   - Edit files in your local editor (changes are synced via the mounted volume)
   - Run tests and scripts inside the container shell

---

## Code Quality: Auto-Linting and Pre-Commit Hooks

This project enforces industry best practices for Python code quality:
- **Auto-formatting** with [black](https://github.com/psf/black)
- **Linting** with [flake8](https://github.com/pycqa/flake8)
- **Import sorting** with [isort](https://github.com/PyCQA/isort)
- **Tests must pass** with [pytest](https://github.com/pytest-dev/pytest)

All of these checks run automatically before every commit via [pre-commit](https://pre-commit.com/).

### **How to Set Up Pre-Commit Hooks**

1. **Install dependencies (already done in the container):**
   ```sh
   poetry install
   ```
2. **Install the pre-commit hooks:**
   ```sh
   pre-commit install
   ```
   (This is already set up if you are using the dev container.)

### **How It Works**
- On every `git commit`, the following will run automatically:
  - `black` (auto-formats code)
  - `flake8` (lints for errors and style)
  - `isort` (sorts imports)
  - `pytest` (runs all tests)
- If any check fails, the commit is blocked until you fix the issues.

### **Manual Linting/Formatting**
You can also run these tools manually:
```sh
black .
flake8 .
isort .
pytest
```

---

## Running and Testing Challenges

- **Run all tests:**
  ```sh
  pytest
  ```
- **Run tests for a specific challenge:**
  ```sh
  pytest challenges/<challenge_name>/
  ```

---

## Adding New Challenges

### **Automatically (Recommended)**
Use the helper script to scaffold a new problem:
```sh
./scripts/add_challenge.sh <challenge_name>
```
This creates a new folder in `challenges/` with:
- `README.md` (problem description, approach, notes)
- `solution.py` (user and canonical solution stubs)
- `test_solution.py` (tests for both solutions)
- `__init__.py`

### **Manually**
Copy the template:
```sh
cp -r challenges/template challenges/my_new_problem
```

---

## Challenge Structure

Each challenge directory contains:
- `README.md` — Problem statement, approach, and notes
- `solution.py` — Two methods: user-submitted and canonical solution, both with descriptive names and docstrings
- `test_solution.py` — Tests that import both solution methods and check correctness

**Example `README.md` template:**
```
# Problem Title

## Problem
Describe the problem here.

## Approach
Describe your approach and thought process.

## Notes
Add any notes, edge cases, or learnings here.
```

---

## Using AI (e.g., Cursor) to Accelerate Your Practice

This project is designed to work seamlessly with AI coding assistants like Cursor. You can:
- **Generate new problems**: Ask the AI to run `./scripts/add_challenge.sh <name>` and fill in the README, solution, and tests.
- **Refactor or review code**: Ask for hints, canonical solutions, or code reviews.
- **Clarify problem statements**: Request the AI to expand on constraints, edge cases, or provide sample test cases.

**Sample AI Prompts:**
- “Generate a new challenge for ‘minimum spanning tree’ and update the README and solution stubs accordingly.”
- “Write canonical and user solution stubs for the ‘find median in data stream’ problem.”
- “Add real test cases to the test_solution.py for the ‘longest palindromic substring’ challenge.”
- “Clarify the assumptions for the ‘merge intervals’ problem in the README.”

---

## Directory Structure

```
coding_challenges/
├── README.md
├── docker/
│   └── Dockerfile
├── scripts/
│   ├── add_challenge.sh
│   └── run_in_container.sh
├── challenges/
│   ├── <challenge_name>/
│   │   ├── README.md
│   │   ├── solution.py
│   │   ├── test_solution.py
│   │   └── __init__.py
│   └── template/
├── pyproject.toml
├── poetry.lock
└── .gitignore
```

---

## Contributing

- Use descriptive function names and docstrings.
- Keep challenge READMEs clear, with all assumptions and edge cases.
- Prefer adding both user and canonical solutions for each problem.
- Tests should cover edge cases and constraints.

---

## License

MIT

---

## Using Make Commands

This project includes a `Makefile` with convenient commands for common development tasks:

### **Quick Commands**
```sh
make help          # Show all available commands
make install       # Install dependencies
make test          # Run all tests
make format        # Format code with black and isort
make lint          # Run flake8 linting
make clean         # Clean up cache and temporary files
```

### **Development Workflow**
```sh
make quality       # Run format + lint + test (all quality checks)
make test-watch    # Run tests in watch mode (auto-rerun on file changes)
make format-check  # Check formatting without making changes
```

### **Docker Commands**
```sh
make build         # Build Docker image
make run           # Run container
```

### **Project Management**
```sh
make add-challenge NAME=my_new_problem  # Add a new challenge
make stats         # Show project statistics
make setup-hooks   # Install pre-commit hooks
make pre-commit-all # Run pre-commit on all files
```

### **Examples**
```sh
# Quick development cycle
make format && make test

# Add a new challenge
make add-challenge NAME=merge_k_sorted_lists

# Check everything before committing
make quality
```

---