### Step 2: The Module (The **"Toolbox"**)
from book import Book

def format_book_name(book: Book) -> str:
    """Return a human-readable string description of a book.

    Args:
        book: A Book-like object with ``title``, ``author``, and
            ``is_checked_out`` attributes.

    Returns:
        A formatted string containing the book's title, author, and status.
    """
    status = "Checked Out" if book.is_checked_out else "Available"
    return f"'{book.title}' by {book.author} [{status}]"