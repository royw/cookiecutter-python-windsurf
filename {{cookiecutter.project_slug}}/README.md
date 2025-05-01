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
1. Create a virtual environment
2. Install the package in editable mode with development dependencies
3. Set up pre-commit hooks

### Available Tasks

- `task format` - Format code with ruff
- `task lint` - Run linters (ruff)
- `task typecheck` - Run type checking with mypy
- `task test` - Run tests with pytest
- `task docs` - Build and serve documentation
- `task check` - Run all checks (format, lint, typecheck, test)

### Continuous Integration

GitHub Actions will automatically:
- Run tests and upload coverage to Codecov
- Run type checking
- Build and test documentation
- Deploy documentation to GitHub Pages (on main branch)

### Publishing to PyPI

To publish a new version:

1. Update the version in `pyproject.toml`:
   ```toml
   [project]
   version = "x.y.z"
   ```

2. Create and push a new tag:
   ```bash
   git tag vx.y.z
   git push origin vx.y.z
   ```

3. Create a new release on GitHub:
   - Go to Releases -> Draft a new release
   - Choose the tag you just pushed
   - Title it "vx.y.z"
   - Describe the changes
   - Publish the release

The release workflow will automatically:
- Build the package
- Upload it to PyPI
- Create a new documentation version

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
