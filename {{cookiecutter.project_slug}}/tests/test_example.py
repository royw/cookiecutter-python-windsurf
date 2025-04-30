"""Tests for the example module."""

import pytest

try:
    from {{ cookiecutter.package_name }}.example import Example  # noqa
except ImportError:
    pass  # This will be replaced during project generation


def test_example_initialization():
    """Test Example class initialization."""
    example = Example("test", 42)
    assert example.name == "test"
    assert example.value == 42


def test_example_process():
    """Test Example.process method."""
    example = Example("test", 21)
    result = example.process()
    assert result == 42


def test_example_process_invalid():
    """Test Example.process method with invalid value."""
    example = Example("test", None)
    with pytest.raises(ValueError):
        example.process()
