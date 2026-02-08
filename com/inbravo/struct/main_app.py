### Step 3: The Script (The **"Director"**)

# You can notice that both the "Class" and the "Function" can be imported. This is the beauty of modular programming - reuse code without duplication.
# Like Java, you dont need to have a full path like ""com.inbravo.struct.book.Book". You can just use "from book import Book" because both the "book.py" and "library_utils.py" are in the same directory.
from book import Book
from library_utils import format_book_name

def run_inventory() -> None:
    """Run a simple inventory demonstration."""
    my_book = Book("The Hobbit", "J.R.R. Tolkien")
    my_book.toggle_checkout()
    print(format_book_name(my_book))

if __name__ == "__main__":
    run_inventory()