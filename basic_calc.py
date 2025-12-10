"""Module for a basic calculator that can add and subtract two numbers."""

import logging
import mylib

# Create a logger for this module
logger = logging.getLogger(__name__)


def main():
    """Run the main application logic with logging."""
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')
    mylib.do_something()
    logger.info('Finished')


class BasicCalc:
    """A simple calculator for basic arithmetic operations."""

    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def sub(self, a, b):
        """Return the difference of a and b."""
        return a - b


def add():
    """Prompt user for two numbers, add them using BasicCalc, and print the result."""
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    calc = BasicCalc()
    total = calc.add(num1, num2)

    print(f"{num1} + {num2} = {total}")


def sub():
    """Prompt user for two numbers, subtract them using BasicCalc, and print the result."""
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    calc = BasicCalc()
    total = calc.sub(num1, num2)

    print(f"{num1} - {num2} = {total}")


if __name__ == "__main__":
    main()
