import sys
import readline
from typing import List

from app.calculation import Calculation, CalculationFactory


def display_help() -> None:
    """Display calculator usage instructions and available commands."""
    help_message = """
Calculator REPL Help
--------------------
Usage:
    <operation> <number1> <number2>
    - Perform a calculation with the specified operation and two numbers.
    - Supported operations:
        add       : Adds two numbers.
        subtract  : Subtracts the second number from the first.
        multiply  : Multiplies two numbers.
        divide    : Divides the first number by the second.

Special Commands:
    help      : Display this help message.
    history   : Show the history of calculations.
    exit      : Exit the calculator.

Examples:
    add 10 5
    subtract 15.5 3.2
    multiply 7 8
    divide 20 4
    """
    print(help_message)


def display_history(history: List[Calculation]) -> None:
    """Display calculations performed during the current session."""
    if not history:
        print("No calculations performed yet.")
    else:
        print("Calculation History:")
        for idx, calculation in enumerate(history, start=1):
            print(f"{idx}. {calculation}")


def calculator() -> None:
    """Run the calculator command-line REPL."""
    history: List[Calculation] = []

    print("Welcome to the Professional Calculator REPL!")
    print("Type 'help' for instructions or 'exit' to quit.\n")

    while True:
        try:
            user_input: str = input(">> ").strip()

            # LBYL: check for empty input before processing it.
            if not user_input:
                continue  # pragma: no cover

            command = user_input.lower()

            # LBYL: check known commands before treating the input as a calculation.
            if command == "help":
                display_help()
                continue

            if command == "history":
                display_history(history)
                continue

            if command == "exit":
                print("Exiting calculator. Goodbye!\n")
                sys.exit(0)

            # EAFP: attempt to parse input and handle formatting errors.
            try:
                operation, num1_str, num2_str = user_input.split()
                num1: float = float(num1_str)
                num2: float = float(num2_str)
            except ValueError:
                print(
                    "Invalid input. Please follow the format: "
                    "<operation> <num1> <num2>"
                )
                print("Type 'help' for more information.\n")
                continue

            # EAFP: ask the factory to create the requested calculation.
            try:
                calculation = CalculationFactory.create_calculation(
                    operation,
                    num1,
                    num2,
                )
            except ValueError as error:
                print(error)
                print("Type 'help' to see the list of supported operations.\n")
                continue

            # EAFP: execute the calculation and handle runtime errors.
            try:
                result = calculation.execute()
            except ZeroDivisionError:
                print("Cannot divide by zero.")
                print("Please enter a non-zero divisor.\n")
                continue
            except Exception as error:
                print(f"An error occurred during calculation: {error}")
                print("Please try again.\n")
                continue

            result_str: str = f"{calculation}"
            print(f"Result: {result_str}\n")
            history.append(calculation)

        except KeyboardInterrupt:
            print("\nKeyboard interrupt detected. Exiting calculator. Goodbye!")
            sys.exit(0)

        except EOFError:
            print("\nEOF detected. Exiting calculator. Goodbye!")
            sys.exit(0)


if __name__ == "__main__":
    calculator()  # pragma: no cover