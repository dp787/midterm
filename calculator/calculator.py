import os
import logging
import math  # Import math module for trigonometric functions

# Configure logging settings using environment variables
logging.basicConfig(
    level=os.getenv('LOG_LEVEL', 'DEBUG'),  # Set the minimum logging level, default to DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log format
    filename=os.getenv('LOG_FILE', 'app.log'),  # Specify the log file name, default to app.log
    filemode='a'  # Specify the file mode ('a' for append)
)

class Calculator:
    commands = {
        'add': 'Addition',
        'subtract': 'Subtraction',
        'multiply': 'Multiplication',
        'divide': 'Division',
        'menu': 'Display Menu',
        'load_history': 'Load History',
        'save_history': 'Save History',
        'clear_history': 'Clear History',
        'delete_history': 'Delete History',
        'sin': 'Sine',
        'cos': 'Cosine',
        'tan': 'Tangent',
        'exp': 'Exponential',
        'log': 'Logarithm'
    }

    history = []

    @staticmethod
    def add(a: float, b: float) -> float:
        result = a + b
        Calculator.history.append({'Operation': 'Addition', 'Result': result})
        logging.info(f"Performed addition: {a} + {b} = {result}")
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        result = a - b
        Calculator.history.append({'Operation': 'Subtraction', 'Result': result})
        logging.info(f"Performed subtraction: {a} - {b} = {result}")
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        result = a * b
        Calculator.history.append({'Operation': 'Multiplication', 'Result': result})
        logging.info(f"Performed multiplication: {a} * {b} = {result}")
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            logging.error("Attempted to divide by zero.")
            raise ValueError("Cannot divide by zero.")
        result = a / b
        Calculator.history.append({'Operation': 'Division', 'Result': result})
        logging.info(f"Performed division: {a} / {b} = {result}")
        return result

    @staticmethod
    def sin(x: float) -> float:
        result = math.sin(x)
        Calculator.history.append({'Operation': 'Sine', 'Result': result})
        logging.info(f"Performed sine calculation: sin({x}) = {result}")
        return result

    @staticmethod
    def cos(x: float) -> float:
        result = math.cos(x)
        Calculator.history.append({'Operation': 'Cosine', 'Result': result})
        logging.info(f"Performed cosine calculation: cos({x}) = {result}")
        return result

    @staticmethod
    def tan(x: float) -> float:
        result = math.tan(x)
        Calculator.history.append({'Operation': 'Tangent', 'Result': result})
        logging.info(f"Performed tangent calculation: tan({x}) = {result}")
        return result

    @staticmethod
    def exp(x: float) -> float:
        result = math.exp(x)
        Calculator.history.append({'Operation': 'Exponential', 'Result': result})
        logging.info(f"Performed exponential calculation: exp({x}) = {result}")
        return result

    @staticmethod
    def log(x: float) -> float:
        result = math.log(x)
        Calculator.history.append({'Operation': 'Logarithm', 'Result': result})
        logging.info(f"Performed logarithm calculation: log({x}) = {result}")
        return result

    @classmethod
    def display_menu(cls):
        logging.info("Displayed menu.")
        print("Available Commands:")
        for command, description in cls.commands.items():
            print(f"{command}: {description}")

    @classmethod
    def execute_command(cls, command):
        if command not in cls.commands:
            logging.error(f"Invalid command: {command}")
            raise ValueError("Invalid command")

        if command in ('add', 'subtract', 'multiply', 'divide'):
            return getattr(cls, command)(2, 3)  # Example usage with default values
        elif command == 'menu':
            cls.display_menu()
        elif command == 'load_history':
            cls.load_history()
        elif command == 'save_history':
            cls.save_history()
        elif command == 'clear_history':
            cls.clear_history()
        elif command == 'delete_history':
            cls.delete_history()
        else:
            logging.error(f"Invalid command: {command}")
            raise ValueError("Invalid command")

    @classmethod
    def load_history(cls):
        try:
            with open('calculation_history.txt', 'r') as file:
                cls.history = eval(file.read())
                logging.info("Loaded calculation history.")
        except FileNotFoundError:
            logging.warning("No calculation history file found.")

    @classmethod
    def save_history(cls):
        with open('calculation_history.txt', 'w') as file:
            file.write(str(cls.history))
        logging.info("Saved calculation history.")

    @classmethod
    def clear_history(cls):
        cls.history = []
        logging.info("Cleared calculation history.")

    @classmethod
    def delete_history(cls):
        try:
            import os
            os.remove('calculation_history.txt')
            cls.history = []
            logging.info("Deleted calculation history.")
        except FileNotFoundError:
            logging.warning("No calculation history file found.")
