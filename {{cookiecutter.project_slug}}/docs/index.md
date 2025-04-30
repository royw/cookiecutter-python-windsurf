# Welcome to {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Installation

```bash
pip install {{ cookiecutter.project_slug }}
```

## Development

This project uses [Task](https://taskfile.dev) for task automation.

### Setup

```bash
task setup
```

This will:
1. Create a virtual environment
2. Install the package in editable mode with development dependencies

### Available Tasks

- `task format` - Format code with black
- `task lint` - Run linters (ruff)
- `task typecheck` - Run type checking with mypy
- `task test` - Run tests with pytest
- `task docs` - Build and serve documentation
- `task check` - Run all checks (format, lint, typecheck, test)

## API Reference

See the [API Reference](reference/) for detailed documentation of all modules and classes.
