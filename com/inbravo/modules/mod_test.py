"""This module demonstrates importing and printing constants from another module."""

# Importing specific constants instead of the entire module
from mod import QUOTE, NUMBERS
# You can also import everything using '*', but it's not recommended
# '*' will place the names of all objects from module into the local symbol table, with the exception of any that begin with the underscore (_) character.
print(QUOTE)
print(NUMBERS)
print("-----")

# Importing the entire module
import mod

print(mod.QUOTE)
print(mod.NUMBERS)
print("-----")