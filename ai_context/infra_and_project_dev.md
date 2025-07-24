# Infra and Project Development Context

## Files to Read for Infra/Project Work

- `Dockerfile`, `docker-compose.yml`: Container build and orchestration
- `pyproject.toml`, `requirements.txt`: Python dependencies and tool config
- `Makefile`: Common project commands
- `.env`: Environment variables (do not commit secrets)
- `.flake8`, `.pre-commit-config.yaml`: Linter and pre-commit hooks
- `scripts/`: Project automation scripts
- `.github/`, `.devcontainer/`: CI/CD and dev container config
- `README.md`: Project overview and onboarding

## Conventions

- Always use poetry for Python dependency management.
- Dev containers must match the Dockerfile.
- All scripts should be runnable in the dev container.
- Update documentation if infra changes affect onboarding or workflow.

## Example Prompts

- “Update the Dockerfile to use Python 3.12 and ensure poetry still works.”
- “Add a Makefile command to run all pre-commit hooks.”
- “Diagnose why the dev container build is failing.”

## See Also

- [ai_context/README.md](README.md)
- [ai_context/code_generation.md](code_generation.md) 