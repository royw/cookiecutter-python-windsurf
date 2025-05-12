"""Post-generation script for cookiecutter-python-windsurf."""

import os
import subprocess
from pathlib import Path


def main():
    """Run post-generation tasks."""
    # Create empty __init__.py files
    src_dir = Path("src") / "{{ cookiecutter.package_name }}"
    tests_dir = Path("tests")
    
    src_dir.mkdir(parents=True, exist_ok=True)
    tests_dir.mkdir(parents=True, exist_ok=True)
    
    (src_dir / "__init__.py").touch()
    (tests_dir / "__init__.py").touch()
    (tests_dir / "test_example.py").touch()

    # Initialize git repository
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "config", "commit.gpgsign", "false"], check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit from cookiecutter-python-windsurf"], check=True)

    # Initialize pre-commit
    try:
        subprocess.run(["pre-commit", "install"], check=True)
        subprocess.run(["pre-commit", "autoupdate"], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\nSkipping pre-commit initialization. Please run 'pip install pre-commit && pre-commit install' after setting up your virtual environment.")

    print("\nProject {{ cookiecutter.project_name }} created successfully!")
    print("\nNext steps:")
    print("1. Change to the project directory:")
    print("   cd {{ cookiecutter.project_slug }}")
    print("\n2. Run CI tasks:")
    print("   task ci")


if __name__ == "__main__":
    main()
