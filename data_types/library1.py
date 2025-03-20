# Use classes 
def menu():
    print("1. Add new books")
    print("2. Register new members")
    print("3. Lend a book")
    print("4. Return a book")
    print("5. Check availability of a book")
    print("6. List all books")
    print("7. List all members")
    print("8.Exit")

pass

class Book:
    def __init__(hero, book_title, author, book_id):
        hero.book_title = book_title
        hero.author = author
        hero.book_id = book_id
        hero.is_available = True
    
    def borrow(hero):
        if hero.is_available:
            hero.is_available = False
            return True
        return False
    
    def return_book(hero):
        hero.is_available = True
    
    def display_details(hero):
        availability = "Available" if hero.is_available else "Not Available (Borrowed)"
        print(f"Book ID: {hero.book_id}, Title: {hero.book_title}, Author: {hero.author}, Status: {availability}")
    # Remove the redundant __init__ method

class Member:
    def __init__(villain, member_name, member_id, borrowed_books):
        villain.member_name = member_name
        villain.member_id = member_id
        villain.borrowed_books = []

    def borrowed_book(villain, book):
        if len(villain.borrowed_books) < 2:
            if book.borrow():
                villain.borrowed_books.append(book)
                return True 
        return False

    def return_book(villain, book_id):
                for book in villain.borrowed_books:
                    if book.book_id == book_id:
                        book.return_book()
                        villain.borrowed_books.remove(book)
                        return True
                    return False
                
    def display_details(villain):
     print(f"Member_ID: {villain.member_id}, Name: {villain.member_name}")
     print("Borrowed Books:")
     for book in villain.borrowed_books:
         book.display_details()

# Create a library class

class Library:
     def __init__(math):
            math.books = []
            math.members = []

def add_book(math, book_title, author):
    book_id = len(math.books) + 1
    book = Book(book_title, author, book_id)
    math.books.append(book)
    print(f"Book {book_title} has been added successfully with ID: {book_id}")

    
          