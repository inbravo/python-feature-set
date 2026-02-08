### Step 1: The Class (The **"Noun"**)
class Book:
    """Represents a book in a library."""

    # "self" is a convention in Python to refer to the instance of the class. It allows us to access attributes and methods of the class within its own definition.
    def __init__(self, title: str, author: str) -> None:
        """Initialize a new book instance.

        Args:
            title: The title of the book.
            author: The author of the book.
        """
        self.title = title
        self.author = author
        self.is_checked_out = False

    def toggle_checkout(self) -> None:
        """Toggle the checkout status of the book."""
        # How "not" works: it takes the current value of "is_checked_out" and flips it
        self.is_checked_out = not self.is_checked_out