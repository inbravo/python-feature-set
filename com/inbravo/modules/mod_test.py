# trunk-ignore-all(black)
"""This module demonstrates importing and printing constants from another module."""

# Importing specific constants instead of the entire module
from mod import NUMBERS, QUOTE

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

# Importing the class from the module
from mod import ExampleClass

example_instance = ExampleClass()
print(example_instance.method_one())
print(example_instance.method_two())
print("-----")

# Importing the entire module and using the class
import mod

example_instance2 = mod.ExampleClass()
print(example_instance2.method_one())
print(example_instance2.method_two())
print("-----")

# Importing the function from the module        
from mod import print_argument

print_argument("Hello from mod_test.py")
print("-----")