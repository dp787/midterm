import argparse
import logging
from calculator.calculator import Calculator

# Configure logging settings
logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum logging level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log format
    filename='app.log',  # Specify the log file name
    filemode='a'  # Specify the file mode ('a' for append)
)

OPERATIONS = ["add", "subtract", "multiply", "divide"]

def perform_operation(op, num1, num2):
    """Performs a calculation based on the operation provided."""
    operations = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': lambda a, b: Calculator.divide(a, b) if b != 0 else float('nan')
    }

    if op in operations:
        return operations[op](num1, num2)
    else:
        logging.error(f"Unknown operation: {op}")
        raise ValueError(f"Unknown operation: {op}")

def parse_and_validate_numbers(num1, num2):
    """Attempts to convert inputs to floats and validates them."""
    try:
        num1 = float(num1)
        num2 = float(num2)
        return num1, num2
    except ValueError:
        logging.error(f"Invalid number input: {num1} or {num2} is not a valid number.")
        raise ValueError(f"Invalid number input: {num1} or {num2} is not a valid number.")

def main():
    parser = argparse.ArgumentParser(description="Simple calculator program")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")
    parser.add_argument("operation", choices=OPERATIONS, help="Operation to perform")

    args = parser.parse_args()

    try:
        num1, num2 = parse_and_validate_numbers(args.num1, args.num2)
        result = perform_operation(args.operation, num1, num2)
        logging.info(f"Performed operation: {num1} {args.operation} {num2} = {result}")
        print(f"The result of {num1} {args.operation} {num2} is equal to {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
