# MIDTERM
# Advanced Python Calculator

## Overview
This project is an advanced Python-based calculator application developed as a midterm assignment for a software engineering graduate course. The calculator integrates clean, maintainable code, design patterns, comprehensive logging, dynamic configuration via environment variables, sophisticated data handling with Pandas, and a command-line interface (REPL) for real-time user interaction.

## Core Functionalities
### Command-Line Interface (REPL)
- Supports execution of arithmetic operations (Add, Subtract, Multiply, and Divide).
- Manages calculation history.
- Accesses extended functionalities through dynamically loaded plugins.

### Plugin System
- Provides a flexible plugin system for seamless integration of new commands or features.
- Dynamically loads and integrates plugins without modifying the core application code.
- Includes a REPL "Menu" command to list all available plugin commands for user discoverability.

### Calculation History Management with Pandas
- Utilizes Pandas for managing a robust calculation history.
- Implements functionalities to load, save, clear, and delete history records through the REPL interface.

### Professional Logging Practices
- Establishes a comprehensive logging system to record detailed application operations, data manipulations, errors, and informational messages.
- Differentiates log messages by severity (INFO, WARNING, ERROR) for effective monitoring.
- Configures dynamic logging settings through environment variables for levels and output destinations.

### Advanced Data Handling with Pandas
- Employs Pandas for efficient data reading and writing to CSV files.
- Manages calculation history efficiently.

### Design Patterns for Scalable Architecture
- Incorporates key design patterns such as Facade, Command, Factory Method, Singleton, and Strategy to address software design challenges.
- Enhances the application's code structure, flexibility, and scalability.

## Setup Instructions
1. Clone the repository to your local machine.
2. Install the required dependencies by running: `pip install -r requirements.txt`.
3. Configure environment variables as needed for logging levels and output destinations.
4. Run the application using Python: `python calculator.py`.
5. Follow the command-line prompts to perform calculations and interact with the calculator.

## Usage Examples
- To perform addition: `add`.
- To perform subtraction: `subtract`.
- To perform multiplication: `multiply`.
- To perform division: `divide`.
- To display the menu: `menu`.

## Architectural Analysis
### Design Patterns Implementation
- Facade Pattern: Provides a simplified interface for complex Pandas data manipulations.
- Command Pattern: Structures commands within the REPL for effective calculation and history management.
- Factory Method, Singleton, and Strategy Patterns: Enhance the application's code structure, flexibility, and scalability.

### Configuration via Environment Variables
- Environment variables are utilized for dynamic logging configuration, allowing users to specify logging levels and output destinations without modifying the code.

### Logging Implementation
- Comprehensive logging is implemented to record detailed application operations, data manipulations, errors, and informational messages.
- Log messages are differentiated by severity for effective monitoring.
- Logging settings can be configured dynamically through environment variables.

### Handling Exceptions (LBYL and EAFP)
- Both "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP) approaches are utilized for handling exceptions.
- LBYL is applied to check for potential errors before performing operations, while EAFP is used to catch and handle exceptions gracefully.

## Code Illustration
- [Environment Variables Configuration](link_to_code): Demonstrates the use of environment variables for configuration.
- [Logging Implementation](https://github.com/dp787/midterm/blob/main/calculator/calculator.py): Illustrates the implementation of logging with dynamic configuration. Documentation that is being used to showcase the iteration of Logging are the files within the "Calculator" folder. 
- [Exception Handling](link_to_code): Shows examples of both LBYL and EAFP approaches for handling exceptions.

## Contributors
- [Devendra Pitam](https://github.com/dp787) - Project Manager
- [Additional Contributor] - No Additional Contributor 

## License
This project is licensed under the [MIT License](link_to_license).
