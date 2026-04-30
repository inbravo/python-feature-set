"""
String Methods
Goal: get comfortable with the most common string operations in Python.
Run this file, read the output, then try the exercises at the bottom.
"""
# String methods are functions that operate on string objects. They allow you to manipulate and analyze strings in various ways, such as splitting, joining, changing case, finding substrings, and more. Here are some of the most common string methods in Python:
# 1. split() — splits a string into a list of substrings based on a specified separator (default is any whitespace).
# 2. join() — takes a list of strings and concatenates them into a single string, using the string it is called on as the separator.
# 3. strip() — removes leading and trailing whitespace (or specified characters) from a string.
# 4. replace() — replaces occurrences of a specified substring with another substring.
# 5. upper(), lower(), title(), swapcase() — change the case of letters in a string.
# 6. find(), index() — search for a substring and return its index (or -1 if not found).
# 7. in — a keyword to check if a substring exists within another string.
# These methods are essential for cleaning, formatting, and analyzing text data in Python. They can be combined in various ways to achieve complex string manipulations.
# Note: all string methods return a new string and do not modify the original string (strings are immutable in Python).
def demonstrate_split():
    print("\n=== method invoked:" +__name__ + "===")
    sentence = "  Python is simple, slow, and effective  "

    # split on a character — returns a list
    words = sentence.split()          # splits on any whitespace, strips edges
    csv_line = "alice,30,engineer"
    fields = csv_line.split(",")      # splits on a specific separator

    print("=== split ===")
    print(words)    # ['Python', 'is', 'simple,', 'slow,', 'and', 'effective']
    print(fields)   # ['alice', '30', 'engineer']


def demonstrate_join():
    print("\n=== method invoked:" +__name__ + "===")
    words = ["Python", "is", "easy"]

    # join takes a list and glues it with the separator string
    result_space = " ".join(words)
    result_dash  = "-".join(words)
    result_none  = "".join(words)

    print("\n=== join ===")
    print(result_space)   # Python is easy
    print(result_dash)    # Python-is-easy
    print(result_none)    # Pythoniseasy

def demonstrate_strip():
    print("\n=== method invoked:" +__name__ + "===")
    messy = "   hello world   "
    tab_messy = "\t\nsome text\n\t"

    print("\n=== strip / lstrip / rstrip ===")
    # 'repr' is part of 'object' (the most fundamental base class from which all other classes are derived)
    # it returns a string that represents the object, often with quotes and escape characters, which is useful for debugging and showing the exact content of a string (including whitespace).
    print(repr(messy.strip()))    # 'hello world'
    print(repr(messy.lstrip()))   # 'hello world   '  (left only)
    print(repr(messy.rstrip()))   # '   hello world'  (right only)
    print(repr(tab_messy.strip()))  # 'some text'  (tabs and newlines too)


def demonstrate_replace():
    print("\n=== method invoked:" +__name__ + "===")
    text = "I like cats. Cats are great. cats cats cats."

    # replace is case-sensitive
    print("\n=== replace ===")
    print(text.replace("cats", "dogs"))        # replaces all occurrences
    print(text.replace("cats", "dogs", 2))     # replace only the first 2
    print(text.replace("Cats", "Dogs"))        # 'Cats' is different from 'cats'


def demonstrate_case():
    print("\n=== method invoked:" +__name__ + "===")
    word = "hello WORLD"

    print("\n=== case methods ===")
    print(word.upper())       # HELLO WORLD
    print(word.lower())       # hello world
    print(word.title())       # Hello World  (each word capitalised)
    print(word.swapcase())    # HELLO world

    # useful for case-insensitive comparison
    user_input = "YES"
    if user_input.lower() == "yes":
        print("User said yes")


def demonstrate_find_and_in():
    print("\n=== method invoked:" +__name__ + "===")
    sentence = "The quick brown fox jumps over the lazy dog"

    print("\n=== find / in / startswith / endswith ===")
    print(sentence.find("fox"))         # 16  (index of first match)
    print(sentence.find("cat"))         # -1  (not found)
    print(sentence.index("fox"))        # 16  (same as find, but raises ValueError if missing)

    print("fox" in sentence)            # True   — preferred over find() for existence checks
    print("cat" in sentence)            # False

    print(sentence.startswith("The"))   # True
    print(sentence.endswith("dog"))     # True
    print(sentence.count("the"))        # 1  (case-sensitive — misses 'The')
    print(sentence.lower().count("the"))  # 2  (case-insensitive)


def demonstrate_practical():
    print("\n=== method invoked:" +__name__ + "===")
    """Combine several methods to clean and process a real-world-ish string."""
    raw = "  Alice , 30 , Software Engineer  "

    # strip the whole line, split on comma, strip each field
    fields = [field.strip() for field in raw.strip().split(",")]
    name, age, role = fields

    summary = f"{name.title()} is {age} years old and works as a {role.lower()}."
    print("\n=== practical example ===")
    print(summary)

# “__name__” is a special variable and it will automatically set its value to “__main__” if the script is being run directly
if __name__ == "__main__":
    demonstrate_split()
    demonstrate_join()
    demonstrate_strip()
    demonstrate_replace()
    demonstrate_case()
    demonstrate_find_and_in()
    demonstrate_practical()

    # ------------------------------------------------------------------
    # EXERCISES — write your answers below each comment, then run the file
    # ------------------------------------------------------------------

    # 1. Take the string "  learn python every day  " and print it with no leading/trailing spaces and every word capitalised.
    print(repr("  learn python every day  ".strip()))    # 'learn python every day'

    # 2. Given csv = "delhi,mumbai,bangalore,chennai", split it into a list, sort it alphabetically, then join it back with " | " as the separator.
    csv = "delhi,mumbai,bangalore,chennai" 
    cities = csv.split(",")  # ['delhi', 'mumbai', 'bangalore', 'chennai']
    cities.sort()            # ['bangalore', 'chennai', 'delhi', 'mumbai']
    result = " | ".join(cities)  # 'bangalore | chennai | delhi | mumbai'
    print(result)

    # 3. Count how many times the letter "a" (case-insensitive) appears in:
    #    text = "A data analyst analyses data daily"

    # 4. Replace every occurrence of "bad" in the string below with "good",
    #    but only if it appears as a whole word (hint: use replace carefully
    #    or look ahead to the regexp module you already have).
    #    text = "bad badminton is not a bad sport for a bad day"
