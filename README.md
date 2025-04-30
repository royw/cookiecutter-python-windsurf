# Cookiecutter Python Windsurf

A modern cookiecutter template for Python projects with best practices and development tools.

## Features

### Development Environment
- Python 3.11+ support
- UV for fast dependency management and virtual environments
- Task automation using Taskfile
- Pre-commit hooks for code quality

### Code Quality
- Ruff for fast linting and formatting
- MyPy for strict type checking
- Pytest for testing with coverage requirements
- Minimum test coverage: 90%
- Maximum cyclomatic complexity: 5
- Maximum line length: 100

### Documentation
- MkDocs with Material theme for beautiful documentation
- Automatic API documentation with mkdocstrings
- Google-style docstring support
- Automatic reference page generation

## Usage

### Quick Start
```bash
# Install cookiecutter if you haven't already
pip install cookiecutter

# Create a new project
cookiecutter gh:{{ cookiecutter.github_username }}/cookiecutter-python-windsurf
```

### Development
To develop or test the template itself:
```bash
# Clone the repository
git clone https://github.com/{{ cookiecutter.github_username }}/cookiecutter-python-windsurf.git
cd cookiecutter-python-windsurf

# Test the template
task test  # This will create a test project in ~/tmp/foobar

# Clean up test artifacts
task clean
```

## Project Structure
The generated project follows a src layout with:
```
├── src/              # Source code
├── tests/            # Test files
├── docs/             # Documentation
├── scripts/          # Utility scripts
├── Taskfile.yaml     # Task automation
├── pyproject.toml    # Project configuration
└── mkdocs.yml        # Documentation configuration
```

## Contributing
Contributions are welcome! Please ensure your changes maintain the high code quality standards:
- Follow Google-style docstrings
- Include type hints
- Add tests for new features
- Keep cyclomatic complexity low
- Use task automation for development workflows
- Automatic navigation generation
- Dark/light theme support

### Development

- Task-based workflow using Taskfile
- Code formatting with Black
- Linting with Ruff
- Type checking with MyPy
- Testing with Pytest
- Coverage reporting
- Virtual environment management

### Project Structure

```
├── docs/
│   ├── index.md
│   └── reference/
├── scripts/
│   └── gen_ref_pages.py
├── src/
│   └── your_package/
├── tests/
├── mkdocs.yml
├── pyproject.toml
├── README.md
└── Taskfile.yml
```

## License

MIT
