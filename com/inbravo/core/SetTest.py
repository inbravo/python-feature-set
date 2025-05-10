# File: /Users/inbravo/Documents/GitHub/python-feature-set/com/inbravo/core/SetTest.py
class SetTest:
    """ "Module providing a Python Set feature test."""

    # A set is a collection which is unordered, unchangeable*, and unindexed.
    # Sets are written with curly brackets.
    # Set items are unordered, unchangeable, and do not allow duplicate values.
    # Set items are unchangeable, but you can remove items and add new items.
    # Set items are indexed, the first item has index [0], the second item has index [1]
    # Duplicate values will be ignored:
    # Set items are unordered, so you cannot be sure in which order the items will appear.
    # To determine how many items a set has, use the len() function:

def test_set_operations():
    """ "Method providing a Python Set feature test."""

    # Create a set
    my_set = {1, 2, 3, 4, 5}
    print("Original Set:", my_set)

    # Add an element
    my_set.add(6)
    print("After Adding 6:", my_set)

    # Remove an element
    my_set.remove(3)
    print("After Removing 3:", my_set)

    # Check membership
    print("Is 4 in the set?", 4 in my_set)
    print("Is 10 in the set?", 10 in my_set)

    # Union of sets
    another_set = {4, 5, 6, 7, 8}
    union_set = my_set.union(another_set)
    print("Union of Sets:", union_set)

    # Intersection of sets
    intersection_set = my_set.intersection(another_set)
    print("Intersection of Sets:", intersection_set)

    # Difference of sets
    difference_set = my_set.difference(another_set)
    print("Difference of Sets:", difference_set)

    # Symmetric difference of sets
    symmetric_difference_set = my_set.symmetric_difference(another_set)
    print("Symmetric Difference of Sets:", symmetric_difference_set)

    # Clear the set
    my_set.clear()
    print("After Clearing the Set:", my_set)

    # A set can contain different data types
    my_set = {"abc", 34, True, 40, "male"}
    print("A set with different data types:", my_set)
    # What is the set type
    print(type(my_set))

    # Create another set with True and 1 together
    # my_set = {True, 1, 2, 3, 4, 5}  # True and 1 is considered the same value and hence Set wont be able to add True

    print("Set with Boolean and Integer:", my_set)
    if __name__ == "__main__":
        test_set_operations()
