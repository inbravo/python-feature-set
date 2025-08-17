"""
RegExpUtils.py
This module provides utility functions for applying regular expressions.
It includes methods to split strings based on whitespace, commas, periods, and punctuations.
"""

import re


class Reg_Exp_Utils:
    """Class to provide utility functions for applying Regular Expressions"""

    @staticmethod
    def split_on_whitespace(text):
        """Splits the input text on whitespace."""
        return re.split(r"(\s)", text)

    @staticmethod
    def split_on_comma_whitespace(text):
        """Splits the input text on commas and whitespace."""
        return re.split(r"([,]|\s)", text)

    @staticmethod
    def split_on_comma_period_whitespace(text):
        """Splits the input text on commas, periods, and whitespace."""
        return re.split(r"([,.]|\s)", text)
    
    @staticmethod
    def split_on_punctuations(text):
        """Splits the input text on various punctuations and whitespace."""
        result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        result = [item.strip() for item in result if item.strip()]
        return result


if __name__ == "__main__":
    # Example usage
    print(Reg_Exp_Utils.split_on_whitespace("Hello, world. This, is a test."))
    print(Reg_Exp_Utils.split_on_comma_whitespace("Hello, world. This, is a test."))
    print(Reg_Exp_Utils.split_on_comma_period_whitespace("Hello, world. This, is a test."))
    print(Reg_Exp_Utils.split_on_punctuations("Hello, world. Is this-- a test?"))
