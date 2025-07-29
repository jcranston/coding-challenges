.PHONY: help install test lint format clean build run add-challenge quality setup-hooks pre-commit-all stats docformat problem-status print-ai-onboarding audit-tags

help:
	@echo "Available commands:"
	@echo "  make install         # Install dependencies with Poetry"
	@echo "  make test            # Run all tests"
	@echo "  make test-watch      # Run tests in watch mode (auto-rerun on changes)"
	@echo "  make lint            # Run flake8 linting"
	@echo "  make format          # Format code with black and isort"
	@echo "  make format-check    # Check formatting without making changes"
	@echo "  make clean           # Clean up cache and temporary files"
	@echo "  make build           # Build Docker image"
	@echo "  make run             # Run container"
	@echo "  make add-challenge NAME=my_new_problem  # Add a new challenge"
	@echo "  make problem-status ARGS=\"--all\"   # Run the problem status utility with arguments"
	@echo "  make quality         # Run format + lint + test (all quality checks)"
	@echo "  make setup-hooks     # Install pre-commit hooks"
	@echo "  make pre-commit-all  # Run pre-commit on all files"
	@echo "  make stats           # Show project statistics"
	@echo "  make print-ai-onboarding # Print AI onboarding prompt"
	@echo "  make audit-tags      # Run the audit_tags.py script to check for missing or extra tags"

install:
	poetry install

test:
	poetry run pytest --import-mode=importlib

test-watch:
	poetry run pytest-watch

lint:
	poetry run flake8 .

format:
	poetry run docformatter --in-place --wrap-summaries 80 --wrap-descriptions 80 $$(find . -name "*.py" -not -path "./.venv/*" -not -path "./__pycache__/*")
	poetry run black .
	poetry run isort .

format-check:
	poetry run docformatter --check --wrap-summaries 80 --wrap-descriptions 80 $$(find . -name "*.py" -not -path "./.venv/*" -not -path "./__pycache__/*")
	poetry run black . --check
	poetry run isort . --check-only

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type d -name ".tox" -exec rm -rf {} +

build:
	./scripts/run_in_container.sh build

run:
	./scripts/run_in_container.sh run

add-challenge:
	@if [ -z "$(NAME)" ]; then \
		echo "Error: NAME parameter is required"; \
		echo "Usage: make add-challenge NAME=challenge_name"; \
		exit 1; \
	fi; \
	./scripts/add_challenge.sh $(NAME)

quality: format lint test

setup-hooks:
	poetry run pre-commit install

pre-commit-all:
	poetry run pre-commit run --all-files

stats:
	@echo "Project Statistics:"
	@echo "==================="
	@echo "Total challenges: $$(find challenges -mindepth 1 -maxdepth 1 -type d | wc -l)"
	@echo "Python files: $$(find . -name '*.py' | wc -l)"
	@echo "Test files: $$(find . -name 'test_*.py' | wc -l)"
	@echo "Lines of code: $$(find . -name '*.py' -exec wc -l {} + | awk '{total += $$1} END {print total}')" 

docformat:
	poetry run docformatter --in-place --wrap-summaries 80 --wrap-descriptions 80 . 

problem-status:
	python scripts/problem_status.py $(ARGS) 

print-ai-onboarding:
	@echo "Please read \`ai_context/README.md\` and all referenced files in ai_context/ before assisting. Use these as your context for all workflows, code generation, and automation in this project." 

audit-tags:
	python scripts/audit_tags.py 