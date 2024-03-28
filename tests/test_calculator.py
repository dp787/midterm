import os
import pytest
from calculator.calculator import Calculator

# Configure environment variables for logging
os.environ['LOG_LEVEL'] = 'DEBUG'
os.environ['LOG_FILE'] = 'app.log'

@pytest.mark.parametrize("num1, num2, expected", [
    (1, 2, 3),
    (4, 5, 9),
    (-1, -2, -3),  # Test with negative numbers
    (0, 0, 0),    # Test with zeros
    (0.5, 0.5, 1), # Test with floating-point numbers
    (-1, 1, 0),   # Test with numbers that sum to zero
    (100, 200, 300),  # Additional test cases
    (-10, 10, 0),
    (0, -100, -100),
])
def test_add(num1, num2, expected):
    """Test addition operation."""
    assert Calculator.add(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 2),
    (10, 4, 6),
    (-5, -3, -2),  # Test with negative numbers
    (0, 0, 0),     # Test with zeros
    (1, 2, -1),    # Test with numbers that result in negative values
    (-10, -5, -5),  # Additional test cases
    (10, -5, 15),
])
def test_subtract(num1, num2, expected):
    """Test subtraction operation."""
    assert Calculator.subtract(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (2, 3, 6),
    (7, 8, 56),
    (-2, 3, -6),   # Test with a negative number
    (0, 5, 0),     # Test with zero
    (1.5, 2, 3),   # Test with floating-point numbers
    (0, 10, 0),   # Additional test cases
    (-5, 5, -25),
])
def test_multiply(num1, num2, expected):
    """Test multiplication operation."""
    assert Calculator.multiply(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (6, 2, 3),
    (9, 3, 3),
    (-6, 2, -3),   # Test with negative numbers
    (0, 5, 0),     # Test with zero as numerator
    (1.5, 2, 0.75), # Test with floating-point numbers
    (10, 2, 5),    # Additional test cases
    (-10, -2, 5),
])
def test_divide(num1, num2, expected):
    """Test division operation."""
    assert Calculator.divide(num1, num2) == expected

def test_divide_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError):
        Calculator.divide(1, 0)

@pytest.mark.parametrize("command", [
    'add',
    'subtract',
    'multiply',
    'divide',
    'menu',
])
def test_valid_commands(command, capsys):
    """Test valid commands."""
    Calculator.display_menu()  # Display menu for reference
    captured = capsys.readouterr()
    assert command in captured.out

@pytest.mark.parametrize("invalid_command", [
    'sin', 'cos', 'tan',  # Unsupported commands
    'exp', 'log',         # Additional unsupported commands
])
def test_invalid_commands(invalid_command):
    """Test invalid commands."""
    with pytest.raises(ValueError, match="Invalid command"):
        Calculator.execute_command(invalid_command)