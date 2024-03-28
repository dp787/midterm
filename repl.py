import logging
from calculator.calculator import Calculator

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log format
    filename='repl.log',  # Specify the log file name
    filemode='a'  # Specify the file mode ('a' for append)
)

class REPL:
    def __init__(self):
        self.calculator = Calculator()
        self.calculation_history = []

    def display_prompt(self):
        logging.info("Prompt displayed.")  # Log prompt display
        print("\n--- Calculator REPL ---")
        print("Enter an arithmetic expression or type 'exit' to quit.")
        print("Supported operations: +, -, *, /")

    def handle_input(self, user_input):
        logging.info(f"Input received: {user_input}")  # Log user input
        if user_input.lower() == 'exit':
            logging.info("Exiting REPL.")  # Log exiting REPL
            print("Exiting REPL. Goodbye!")
            return False
        else:
            try:
                result = eval(user_input)  # Evaluate arithmetic expression
                self.calculation_history.append((user_input, result))
                print("Result:", result)
                logging.info(f"Calculation result: {result}")  # Log calculation result
            except Exception as e:
                print("Error:", e)
                logging.error(f"Error occurred: {e}")  # Log error
        return True

    def run(self):
        logging.info("REPL started.")  # Log REPL start
        self.display_prompt()
        while True:
            user_input = input(">>> ")
            if not self.handle_input(user_input):
                break

if __name__ == "__main__":
    repl = REPL()
    repl.run()
