# Sample program to demonstrate the use of f-strings in Python

def main():
    # Basic usage of f-strings
    name = "Alice"
    age = 30
    print(f"My name is {name} and I am {age} years old.")

    # Using expressions inside f-strings
    num1 = 10
    num2 = 20
    print(f"The sum of {num1} and {num2} is {num1 + num2}.")

    # Formatting numbers
    pi = 3.14159
    print(f"The value of pi rounded to 2 decimal places is {pi:.2f}.")

    # Using f-strings with dictionaries
    person = {"name": "Bob", "age": 25}
    print(f"{person['name']} is {person['age']} years old.")

    # Multiline f-strings
    greeting = f"""
    Hello, {name}!
    Welcome to the world of Python.
    """
    print(greeting)

if __name__ == "__main__":
    main()