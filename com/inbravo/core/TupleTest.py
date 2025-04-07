"""Module providing test of various Python features"""


class TupleTest:
    """ "Module providing a Python Tuple feature test."""

    # Tuple items are ordered, unchangeable, and allow duplicate values.
    # Tuple items are indexed, the first item has index [0], the second item has index [1]

    thistuple = ("apple", "banana", "cherry", "apple", "cherry")
    print(thistuple)

    # To determine how many items a tuple has, use the len() function:
    print(len(thistuple))

    # To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
    thistuple = ("apple",)
    print(type(thistuple))

    # NOT a tuple
    thistuple = "apple"
    print(type(thistuple))

    # String, int and boolean data types:
    tuple1 = ("apple", "banana", "cherry")
    tuple2 = (1, 5, 7, 9, 3)
    tuple3 = (True, False, False)

    # A tuple can contain different data types:
    tuple1 = ("abc", 34, True, 40, "male")

    # Using the tuple() method/constructor to make a tuple:
    thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
    print(thistuple)

    # Print the second item in the tuple
    print(thistuple[1])

    # Print the last item in the tuple
    print(thistuple[-1])

    thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    # Print the range
    print(thistuple[2:5])

    # This example returns the items from the beginning to, but NOT after "kiwi":
    print(thistuple[:4])
    # This example returns the items from "cherry" and to the end:
    print(thistuple[2:])

    # Check if "apple" is present in the tuple:
    if "apple" in thistuple:
        print("Yes, 'apple' is in the fruits tuple")

    # Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
    # But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
    x = ("apple", "banana", "cherry")
    y = list(x)
    y[1] = "kiwi"
    x = tuple(y)

    # Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
    # 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
    y = list(thistuple)
    y.append("orange")
    thistuple = tuple(y)

    # 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
    thistuple = ("apple", "banana", "cherry")
    y = ("orange",)
    thistuple += y
    print(thistuple)

    # Convert the tuple into a list, remove "apple", and convert it back into a tuple:
    thistuple = ("apple", "banana", "cherry")
    y = list(thistuple)
    y.remove("apple")
    thistuple = tuple(y)

    thistuple = ("apple", "banana", "cherry")
    del thistuple
    # print(thistuple) # this will raise an error because the tuple no longer exists

    # Unpacking a tuple
    fruits = ("apple", "banana", "cherry")
    (green, yellow, red) = fruits
    print(green)
    print(yellow)
    print(red)

    fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
    # If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
    (green, yellow, *red) = fruits
    print(green)
    print(yellow)
    # Red will have more than one value
    print(red)
    # Iterating on a tuple
    for x in fruits:
        print(x)

    # Looping on a tuple: Enumerate the fruits
    for fruit in enumerate(fruits):
        print("bucket has ", fruit)

    # Looping on a tuple: Enumerate the fruits at an index
    for i, fruit in enumerate(fruits):
        print("bucket has ", i, fruit)

    # Join two tuples
    tuple1 = ("a", "b", "c")
    tuple2 = (1, 2, 3)
    tuple3 = tuple1 + tuple2
    print(tuple3)

    # Multiply the tuple by double (2) or triple(3) etc.
    fruits = ("apple", "banana", "cherry")
    mytuple = fruits * 4
    print(mytuple)
