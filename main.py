import sys
import logging
import math  # Import the math module for trigonometric and logarithmic functions
from calculator.calculator import Calculator

# Configure logging settings
logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum logging level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log format
    filename='app.log',  # Specify the log file name
    filemode='w'  # Specify the file mode ('w' for write)
)

def perform_operation(op, num1, num2=None):
    """Performs a calculation based on the operation provided."""
    operations = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide,
        'sin': math.sin,   # Trigonometric sine function
        'cos': math.cos,   # Trigonometric cosine function
        'tan': math.tan,   # Trigonometric tangent function
        'log': math.log    # Natural logarithm function
    }

    if op in operations:
        if num2 is not None:
            return operations[op](num1, num2)
        else:
            return operations[op](num1)
    else:
        raise ValueError(f"Unknown operation: {op}")

def parse_and_validate_numbers(num1, num2):
    """Attempts to convert inputs to floats and validates them."""
    try:
        num1 = float(num1)
        if num2 is not None:
            num2 = float(num2)
        return num1, num2
    except ValueError:
        logging.error(f"Invalid number input: {num1} or {num2} is not a valid number.")
        raise ValueError(f"Invalid number input: {num1} or {num2} is not a valid number.")

def main():
    if len(sys.argv) < 3:
        logging.error("Not enough arguments provided.")
        print("Usage: python main.py <number1> [<number2>] <operation>")
        print("Operations are 'add', 'subtract', 'multiply', 'divide', 'sin', 'cos', 'tan', 'log'")
        return

    _, arg_num1, *rest_args = sys.argv
    if len(rest_args) == 2:
        arg_num2, operation = rest_args
    else:
        arg_num2 = None
        operation, = rest_args

    try:
        num1, num2 = parse_and_validate_numbers(arg_num1, arg_num2)
        result = perform_operation(operation, num1, num2)
        logging.info(f"Performed operation: {num1} {operation} {num2} = {result}")
        print(f"The result of {num1} {operation} {num2 if num2 is not None else ''} is equal to {result}")
    except ValueError as e:
        logging.error(str(e))
        print(e)

if __name__ == "__main__":
    main()
