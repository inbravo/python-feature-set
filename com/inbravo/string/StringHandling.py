# A class to test the Python String features
# Amit Dixit 
# inbravo@outlook.com

class StringHandling:
    
    # A class variable. quote or double quote, both are acceptable for string
    testString = "i am a string"
    testString = 'i am also a string'

    def __str__(self):
        return f"{self.testString}"

    def __init__(self, string):
        print("__init__ invoked")
        self.testString = string
    
    def printString(string):
        print(string)

    def main():
        print("i am in the main method")
        st = StringHandling()
        st.printString("passed variable")

    main()