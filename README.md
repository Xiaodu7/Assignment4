# Assignment 4 - Professional Calculator

## Overview

This project is a command-line calculator application written in Python.

The calculator uses object-oriented programming concepts and supports addition, subtraction, multiplication, and division. It also includes a REPL interface, calculation history, help commands, input validation, and error handling.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- `help` command
- `history` command
- `exit` command
- Input validation
- Division-by-zero error handling
- Calculation history
- Calculation Factory design pattern
- LBYL (Look Before You Leap)
- EAFP (Easier to Ask Forgiveness than Permission)
- Unit and parameterized testing with pytest
- 100% test coverage
- GitHub Actions for automated testing

## Project Structure

```text
Assignment4/
├── app/
│   ├── calculation/
│   │   └── __init__.py
│   ├── calculator/
│   │   └── __init__.py
│   └── operation/
│       └── __init__.py
├── tests/
│   ├── conftest.py
│   ├── test_calculation.py
│   ├── test_calculator.py
│   └── test_operations.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── .coveragerc
├── .gitignore
├── main.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the Calculator

Run the calculator using:

```bash
python main.py
```

The calculator will start in the terminal and wait for user input.

## Example Commands

```text
add 10 5
subtract 15 3
multiply 4 6
divide 20 4
history
help
exit
```

Example:

```text
>> add 10 5
Result: AddCalculation: 10.0 Add 5.0 = 15.0
```

## Special Commands

### help

Displays instructions, supported operations, and example commands.

```text
help
```

### history

Displays calculations performed during the current session.

```text
history
```

### exit

Exits the calculator.

```text
exit
```

## Error Handling

The calculator handles invalid input and unexpected situations without crashing the program.

For example, division by zero:

```text
>> divide 10 0
Cannot divide by zero.
Please enter a non-zero divisor.
```

The project demonstrates two common Python error-handling approaches:

- **LBYL (Look Before You Leap):** checks certain conditions before processing input.
- **EAFP (Easier to Ask Forgiveness than Permission):** uses `try` and `except` blocks to attempt an operation and handle errors if they occur.

## Object-Oriented Design

The project uses object-oriented programming to organize the calculator into separate components.

The `Operation` class contains the basic arithmetic methods:

- Addition
- Subtraction
- Multiplication
- Division

The `Calculation` class is an abstract base class used by the following calculation classes:

- `AddCalculation`
- `SubtractCalculation`
- `MultiplyCalculation`
- `DivideCalculation`

Each calculation class implements its own `execute()` method.

The `CalculationFactory` is responsible for creating the correct calculation object based on the operation entered by the user.

For example:

```text
add
```

is connected to:

```text
AddCalculation
```

through the `CalculationFactory`.

## Testing

The project uses `pytest` for unit and parameterized testing.

Run the complete test suite with:

```bash
pytest
```

The tests cover:

- Arithmetic operations
- Calculation classes
- Calculation Factory
- Calculator REPL behavior
- Special commands
- Input validation
- Error handling
- Division by zero
- Positive test cases
- Negative test cases

## Test Coverage

The project is configured to maintain 100% test coverage.

Running:

```bash
pytest
```

also generates the coverage report.

The expected test result is:

```text
67 passed
100% coverage
```

An HTML coverage report is also generated in the `htmlcov` directory.

## GitHub Actions

GitHub Actions is configured to automatically run the test suite when code is pushed to the repository.

The workflow requires 100% test coverage.

If test coverage drops below 100%, the GitHub Actions workflow will fail.

## Author

Xiao Du