# MLOps Development Environment Setup Guide

## Overview

This repository provides a standardized development environment using Visual Studio Code and Docker containers, ensuring consistent development experience across team members.

## Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

## Development Container Configuration

The `.devcontainer/devcontainer.json` defines our development environment:

```plaintext
.devcontainer/
├── devcontainer.json    # Main configuration file
└── Dockerfile           # Custom container definition (if used)
```

```devcontainer.json``` Configuration
Base Container Settings

### Base Image & Build

- Uses Python 3.11 Debian Bullseye base image
- Installs essential build tools and development packages
- Configures Poetry for Python package management

### VSCode Settings

- Pre-installed extensions for:
  - Python development
  - Docker management
  - Git integration
  - Code formatting & linting
- Customized editor settings for consistent coding standards

### Environment Features

- Poetry for dependency management
- Pre-commit hooks for code quality
- Automated package installation
- Customized shell configuration (zsh)
- Git configuration and credentials

## Getting Started

- Clone the repository:

```bash
git clone <repository-url>
```

- Open in Vscode

```bash
code <repository-name>
```

- When prompted, click "Reopen in Container"

- VSCode will:
  - Build the development container
  - Install all dependencies
  - Configure the development environment

### Development Workflow

1. The container automatically installs project dependencies using Poetry
2. Pre-commit hooks are set up for code quality checks
3. Python environment is configured with standard tools
4. Git is configured for collaboration

### Customization

The development environment can be customized by modifying:

- devcontainer.json - Container configuration
- pyproject.toml - Python dependencies
- .pre-commit-config.yaml - Code quality checks

### Troubleshooting

1. If container fails to build:
    - Check Docker is running
    - Try rebuilding container: Command Palette → "Rebuild Container"
2. If dependencies fail to install:
    - Check Poetry configuration
    - Verify pyproject.toml syntax
