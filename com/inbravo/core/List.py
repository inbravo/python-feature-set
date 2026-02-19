# Not a class; just a script to demonstrate List in Python

# List in Python is a collection which is ordered and changeable. Allows duplicate members.
# List is one of 4 built-in data types in Python used to store collections of data
# The other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
List = [] 

# List is Muteable; means value can be change
List.insert(0, 5)  # insertion takes place at mentioned index
List.insert(1, 10) # insertion takes place at mentioned index
List.insert(0, 6) # insertion takes place at mentioned index; existing element will be shifted to right
print(List)

List.remove(6) # removes first occurrence of element; if element is not found, it raises a ValueError
List.append(9)  # insertion takes place at last
List.append(1)
List.sort()  # arranges element in ascending order
print(List)

List.pop() # removes and returns last element; if index is specified, it removes and returns element at that index
List.reverse() # reverses the order of the list
print(List)