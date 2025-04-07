"""Class to experiment the different data types in Python"""

class DataTypes:
    # Text Type: 	str
    # Numeric Types: 	int, float, complex
    # Sequence Types: 	list, tuple, range
    # Mapping Type: 	dict
    # Set Types: 	set, frozenset
    # Boolean Type: 	bool
    # Binary Types: 	bytes, bytearray, memoryview
    # None Type: 	NoneType
    x = str("Hello World")
    print(x)

    x = int(20)
    print(x)

    x = float(20.5)
    print(x)

    x = complex(1j)  # complex is made of a real and an imginary number
    print(x)

    real = 10
    imaginary = 7
    complex_number = complex(real, imaginary)
    print("Complex number formed: ", complex_number)

    x = list(
        ("apple", "banana", "cherry")
    )  # a list can be dynamic, not fixed length like tuple
    print(x)

    x = tuple(("apple", "banana", "cherry"))  # a typle is always fixed length
    print("Tuple: ", x)

    x = range(6)
    print("Range: ", x)

    x = dict(name="John", age=36)
    print("Dictionary: ", x)

    x = set(("apple", "banana", "cherry"))
    print("Set: ", x)

    x = frozenset(("apple", "banana", "cherry"))
    print("Frozenset: ", x)

    x = bool(5)
    print("Boolean: ", x)

    x = bytes(5)
    print("Bytes: ", x)

    x = bytearray(5)
    print("Bytearray: ", x)

    x = memoryview(bytes(5))
    print("Memoryview of a byte: ", x)

    x = 1  # int
    y = 2.8  # float

    # convert from int to float:
    a = float(x)

    # convert from float to int:
    b = int(y)

    # convert from int to complex:
    c = complex(x)

    # convert from float to complex:
    d = complex(y)

    print(a)
    print(b)
    print(c)
    print(d)

    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
