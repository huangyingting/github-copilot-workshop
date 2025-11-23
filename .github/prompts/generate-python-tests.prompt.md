---
description: "Generate comprehensive unit tests for Python code with pytest"
mode: 'agent'
---

# Generate Python Unit Tests

Generate comprehensive unit tests for the selected Python code using pytest framework.

## Requirements

- Use `pytest` as the testing framework
- Follow AAA pattern (Arrange, Act, Assert)
- Include both positive and negative test cases
- Test edge cases and boundary conditions
- Use fixtures for common setup
- Add docstrings to test functions explaining what they test
- Mock external dependencies (APIs, databases, file I/O)
- Aim for high code coverage
- Include parametrized tests where appropriate

## Test Structure

```python
import pytest
from unittest.mock import Mock, patch

class TestClassName:
    """Test suite for ClassName."""
    
    @pytest.fixture
    def sample_data(self):
        """Fixture providing sample data for tests."""
        return {...}
    
    def test_method_name_success(self, sample_data):
        """Test method_name with valid input."""
        # Arrange
        # Act
        # Assert
        
    def test_method_name_error(self):
        """Test method_name handles errors correctly."""
        # Arrange
        # Act & Assert
```

## Coverage Goals

- Aim for at least 80% code coverage
- Test all public methods and functions
- Test error handling and exceptions
- Test different input types and values
- Test integration points

## Example Usage

1. Select the Python code you want to test
2. Use this prompt via `Ctrl+/` → `generate-python-tests`
3. Review generated tests and add to `tests/` directory
4. Run tests with: `pytest tests/ -v --cov`
