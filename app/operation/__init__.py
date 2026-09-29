class Operation:
    """Provide basic arithmetic operations for the calculator."""

    @staticmethod
    def addition(a: float, b: float) -> float:
        """Return the sum of two numbers."""
        return a + b

    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """Return the difference between two numbers."""
        return a - b

    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """Return the product of two numbers."""
        return a * b

    @staticmethod
    def division(a: float, b: float) -> float:
        """Return the quotient of two numbers.

        Raises:
            ValueError: If the divisor is zero.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")

        return a / b