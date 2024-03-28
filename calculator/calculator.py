import os
import logging

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
        'delete_history': 'Delete History'
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

        if command == 'add':
            return cls.add(2, 3)
        elif command == 'subtract':
            return cls.subtract(5, 3)
        elif command == 'multiply':
            return cls.multiply(2, 3)
        elif command == 'divide':
            return cls.divide(6, 2)
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


def perform_calculation_from_dataframe(df):
    operation = input("Enter operation (add/subtract/multiply/divide): ")
    if operation not in ['add', 'subtract', 'multiply', 'divide']:
        print("Invalid operation")
        return
    if operation == 'add':
        return df.sum().sum()
    elif operation == 'subtract':
        return df.diff().dropna().sum().sum()
    elif operation == 'multiply':
        return df.product().product()
    elif operation == 'divide':
        return df.iloc[0].div(df.iloc[1]).prod()


# Example usage of Calculator with pandas DataFrame
if __name__ == "__main__":
    import pandas as pd

    # Create a sample DataFrame
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)

    # Perform calculation on DataFrame using Calculator
    result = perform_calculation_from_dataframe(df)
    print("Result of operation on DataFrame elements:", result)

