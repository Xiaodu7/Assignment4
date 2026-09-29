from abc import ABC, abstractmethod

from app.operation import Operation


class Calculation(ABC):
    """Base class for all calculator operations."""

    def __init__(self, a: float, b: float) -> None:
        """Initialize a calculation with two operands."""
        self.a: float = a
        self.b: float = b

    @abstractmethod
    def execute(self) -> float:
        """Execute the calculation."""
        pass  # pragma: no cover

    def __str__(self) -> str:
        """Return a readable representation of the calculation."""
        result = self.execute()
        operation_name = self.__class__.__name__.replace("Calculation", "")
        return (
            f"{self.__class__.__name__}: "
            f"{self.a} {operation_name} {self.b} = {result}"
        )

    def __repr__(self) -> str:
        """Return a developer-friendly representation of the calculation."""
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"


class CalculationFactory:
    """Create calculation objects based on a registered operation name."""

    _calculations = {}

    @classmethod
    def register_calculation(cls, calculation_type: str):
        """Register a calculation subclass with the factory."""
        def decorator(subclass):
            calculation_type_lower = calculation_type.lower()

            if calculation_type_lower in cls._calculations:
                raise ValueError(
                    f"Calculation type '{calculation_type}' "
                    "is already registered."
                )

            cls._calculations[calculation_type_lower] = subclass
            return subclass

        return decorator

    @classmethod
    def create_calculation(
        cls,
        calculation_type: str,
        a: float,
        b: float,
    ) -> Calculation:
        """Create and return the requested calculation object."""
        calculation_type_lower = calculation_type.lower()
        calculation_class = cls._calculations.get(calculation_type_lower)

        if not calculation_class:
            available_types = ", ".join(cls._calculations.keys())
            raise ValueError(
                f"Unsupported calculation type: '{calculation_type}'. "
                f"Available types: {available_types}"
            )

        return calculation_class(a, b)


@CalculationFactory.register_calculation("add")
class AddCalculation(Calculation):
    """Represent an addition calculation."""

    def execute(self) -> float:
        """Perform addition."""
        return Operation.addition(self.a, self.b)


@CalculationFactory.register_calculation("subtract")
class SubtractCalculation(Calculation):
    """Represent a subtraction calculation."""

    def execute(self) -> float:
        """Perform subtraction."""
        return Operation.subtraction(self.a, self.b)


@CalculationFactory.register_calculation("multiply")
class MultiplyCalculation(Calculation):
    """Represent a multiplication calculation."""

    def execute(self) -> float:
        """Perform multiplication."""
        return Operation.multiplication(self.a, self.b)


@CalculationFactory.register_calculation("divide")
class DivideCalculation(Calculation):
    """Represent a division calculation."""

    def execute(self) -> float:
        """Perform division and prevent division by zero."""
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return Operation.division(self.a, self.b)