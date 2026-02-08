"""
This module provides an example of a Python script with a constant, a function, and a class.
"""

QUOTE = "If Comrade Napoleon says it, it must be right."
NUMBERS = [100, 200, 300]

def print_argument(argument):
    """
    Prints the provided argument.
    """
    print(f'argument = {argument}')

class ExampleClass:
    """
    Example class with two public methods.
    """

    def method_one(self):
        """
        First example method.
        """
        return "Method one executed."

    def method_two(self):
        """
        Second example method.
        """
        return "Method two executed."