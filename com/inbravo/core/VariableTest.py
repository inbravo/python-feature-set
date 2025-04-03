# Python has no command for declaring a variable type
x = 4  # x is of type int
y = "inbravo"  # y is now of type str
print(x)
print(y)

# You can get the data type of a variable with the type() function
print(type(x))
print(type(y))

x = "inbravo"  # x is now of type str
print(x)

# Type casting is available in Python
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

# Valid variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Invalid variable names
# my-var = "John"
# my var = "John"
# 2myvar = "John"

# Assign multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Assign array to variables
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Print multiple variables using a single print statement
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
# print(x + " " + y + " " + z)
