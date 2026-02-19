"""Demonstrate basic list operations in Python.

This script is intentionally simple and non-OOP. It shows how to:
- create a list
- insert and append elements
- remove elements
- sort and reverse the list
- use pop to remove the last element
"""

# inbravo@github
# This is a procedural style script, not object-oriented. It focuses on list operations without defining any classes.
# The main function demonstrates various list operations in Python, including insertion, removal, sorting, and reversing. 
# It also shows how to use the pop method to remove the last element of the list. 
# The script is designed to be simple and straightforward, without any object-oriented programming concepts, to focus solely on list manipulation.
# The return type of the main function is None, as it does not return any value. It simply performs operations on the list and prints the results to the console.
def main() -> None:
    # A list is an ordered, mutable collection that allows duplicate elements.
    numbers: list[int] = []

    # Insert elements at specific positions
    numbers.insert(0, 5)   # insert 5 at index 0 -> [5]
    numbers.insert(1, 10)  # insert 10 at index 1 -> [5, 10]
    numbers.insert(0, 6)   # insert 6 at index 0, shift others right -> [6, 5, 10]
    print("After inserts:", numbers)

    # Remove the first occurrence of a value
    numbers.remove(6)      # remove first 6 -> [5, 10]

    # Append elements to the end
    numbers.append(9)      # -> [5, 10, 9]
    numbers.append(1)      # -> [5, 10, 9, 1]

    # Sort the list in ascending order
    numbers.sort()
    print("After remove/append/sort:", numbers)

    # Pop removes and returns the last element
    last = numbers.pop()
    print("Popped value:", last)

    # Reverse the list in-place
    numbers.reverse()
    print("After reverse:", numbers)

# The main function is called when the script is executed directly.
if __name__ == "__main__":
    main()