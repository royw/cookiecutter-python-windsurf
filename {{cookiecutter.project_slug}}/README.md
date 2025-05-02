# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

[![CI](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/ci.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/ci.yml)
[![Documentation](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/ci.yml/badge.svg)](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/)
[![PyPI version](https://badge.fury.io/py/{{ cookiecutter.project_slug }}.svg)](https://badge.fury.io/py/{{ cookiecutter.project_slug }})
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})

## Installation

```bash
pip install {{ cookiecutter.project_slug }}
```

## Development

This project uses [Task](https://taskfile.dev) for task automation and GitHub Actions for CI/CD.

### Setup

```bash
task setup
```

This will:
1. Install required Python versions (3.11, 3.12, 3.13)
2. Create virtual environments for each Python version
3. Install the package in editable mode with development and documentation dependencies
4. Set up pre-commit hooks
5. Create a symlink from `.venv` to the development Python version (3.12)

### Available Tasks

#### Environment Management
- `task setup` - Set up development environments for all supported Python versions
- `task update:env` - Update all virtual environments with latest dependencies
- `task update:dev-env` - Update only development environment
- `task upgrade-env` - Upgrade all dependencies to latest versions
- `task clean` - Clean build artifacts and caches

#### Testing
- `task test` - Run tests using development Python version
- `task test:coverage` - Run tests with coverage report
- `task test:pythons` - Run tests across all supported Python versions

#### Code Quality
- `task lint` - Run code quality checks (ruff, mypy, pre-commit)
- `task format` - Format code with ruff
- `task metrics` - Run code quality metrics (radon)
- `task spell` - Run codespell checks

#### Documentation
- `task docs` - Serve documentation locally
- `task docs:build` - Build documentation

#### Build and Publish
- `task build` - Build package distribution (wheel and sdist)
- `task publish:pypi` - Publish to PyPI
- `task publish:test-pypi` - Publish to Test PyPI

#### CI/CD
- `task ci` - Run all CI checks (lint, test, coverage, docs, build)

Run `task --list-all` to see all available tasks with descriptions.

### Continuous Integration

GitHub Actions will automatically:
- Run tests across all supported Python versions
- Upload coverage reports to Codecov
- Run code quality checks (ruff, mypy)
- Run security checks (bandit)
- Build and test documentation
- Deploy documentation to GitHub Pages (on main branch)
- Publish package to PyPI (on release)

### Publishing to PyPI

To publish a new version:

1. Update the version using the version bump task:
   ```bash
   task version:bump -- patch  # For patch version (0.0.x)
   task version:bump -- minor  # For minor version (0.x.0)
   task version:bump -- major  # For major version (x.0.0)
   ```

2. Create and push a tag (automated):
   ```bash
   task version:tag
   ```

3. Publish to Test PyPI first:
   ```bash
   task publish:test-pypi
   ```

4. Verify the package on Test PyPI, then publish to PyPI:
   ```bash
   task publish:pypi
   ```

The CI/CD workflow will automatically:
- Run all checks (lint, test, coverage)
- Build and verify the package
- Build and deploy documentation
- Create a GitHub release

## Documentation

The documentation is built using MkDocs with the Material theme and mkdocstrings for API documentation.

To view the documentation locally:

```bash
task docs
```

Then open http://127.0.0.1:8000 in your browser.

The documentation is automatically deployed to GitHub Pages when changes are pushed to the main branch: https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/

## License

MIT
