from calculator.calculator import Command  # Adjust import statement
import logging
import pandas as pd

class DataCommand(Command):
    def execute(self):
        # Demonstrating Lists
        calculator_operations = ['add', 'subtract', 'multiply', 'divide']
        logging.info(f'Calculator operations: {calculator_operations}')
        # Lists are ordered and mutable, making them ideal for storing a collection of items that may change over time.
        logging.info(f'Selected operation: {calculator_operations[0]}')
        calculator_operations.append('exponentiation')  # Adding an item to the list
        logging.info(f'Updated calculator operations: {calculator_operations}')

        # Demonstrating Tuples
        supported_operators = ('+', '-', '*', '/')
        logging.info(f'Supported operators tuple: {supported_operators}')
        # Tuples are ordered and immutable, suitable for storing a collection of items that should not change.
        logging.debug(f'First operator: {supported_operators[0]}')

        # Demonstrating Sets
        calculator_modes = {'basic', 'scientific', 'programming'}
        logging.info(f'Calculator modes set: {calculator_modes}')
        logging.info(f'Different modes: {calculator_modes.difference({"basic"})}')
        # Sets are unordered, mutable, and do not allow duplicate values, ideal for unique collections without specific order.

        calculator_modes.add('financial')  # Adding an item to the set
        logging.info(f'Updated calculator modes set: {calculator_modes}')

        # Demonstrating Dictionaries
        operation_descriptions = {
            'add': 'Addition',
            'subtract': 'Subtraction',
            'multiply': 'Multiplication',
            'divide': 'Division'
        }
        logging.info(f'Operation descriptions dictionary: {operation_descriptions}')
        # Dictionaries store data in key-value pairs. They are mutable and unordered. Ideal for fast lookups where each value is associated with a unique key.

        operation_descriptions['exponentiation'] = 'Exponentiation'  # Adding a new key-value pair
        logging.info(f'Updated operation descriptions dictionary: {operation_descriptions}')

        # Demonstrating dictionary iteration
        for operation, description in operation_descriptions.items():
            logging.info(f"Operation: {operation}, Description: {description}")

        # Advanced use case: Nested Dictionaries
        operation_info = {
            'add': {
                'operation': 'addition',
                'syntax': 'a + b',
                'description': 'Adds two numbers together'
            },
            'subtract': {
                'operation': 'subtraction',
                'syntax': 'a - b',
                'description': 'Subtracts one number from another'
            },
            'multiply': {
                'operation': 'multiplication',
                'syntax': 'a * b',
                'description': 'Multiplies two numbers together'
            },
            'divide': {
                'operation': 'division',
                'syntax': 'a / b',
                'description': 'Divides one number by another'
            }
        }
        for operation, info in operation_info.items():
            logging.info(f"Operation: {operation}")
            print(f"Operation: {operation}")

            # Iterate through each property of the operation and print/log it
            for property_name, property_value in info.items():
                property_info = f"    {property_name.capitalize()}: {property_value}"
                print(property_info)
                logging.info(property_info)
