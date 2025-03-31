
class DataTypes:

    # Casting in Python is done using constructor functions:
    # int()     - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
    # float()   - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
    # str()     - constructs a string from a wide variety of data types, including strings, integer literals and float literals
    x = 1
    y = 2.8
    z = "3"

    # Use of "type"
    print(type(x))
    print(type(y))
    print(type(z))

    # Use of "isinstance"
    print(isinstance(x, int))
    print(isinstance(y, float))
    print(isinstance(z, str))

    # 
    x = int(x)      # x will be 1
    y = int(y)      # y will be 2ß
    z = int(z)      # z will be 3

    print(x)
    print(y)
    print(z)