# What is Poetry?

1. Poetry is a modern dependency management and packaging tool for Python
2. Handles dependencies, virtual environments, and package building in one tool

## Key Features

1. Dependency resolution
2. Virtual environment management
3. Project packaging/publishing
4. Lock file for reproducible environments
5. Project scaffolding

## Basic Usage

Here are the essential Poetry commands:

```yaml
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Create new project
poetry new my-project

# Initialize existing project
poetry init

# Add dependencies
poetry add requests
poetry add pytest --dev  # dev dependency

# Install dependencies
poetry install

# Run commands in virtual environment
poetry run python script.py
poetry run pytest

# Activate virtual environment
poetry shell

# Update dependencies
poetry update

# Export dependencies to requirements.txt
poetry export -f requirements.txt --output requirements.txt
```

## Example pyproject.toml

```yaml
[tool.poetry]
name = "my-project"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.28.0"

[tool.poetry.dev-dependencies]
pytest = "^7.1.0"
```
