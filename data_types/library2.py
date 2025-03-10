class Book:
    def __init__(hero, book_title, author, book_id):
        hero.book_title = book_title
        hero.author = author
        hero.book_id = book_id
        hero.is_available = True  # Book is available by default
    
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

class Member:
    def __init__(hero, member_name, member_id):
        hero.member_name = member_name
        hero.member_id = member_id
        hero.borrowed_books = []  # Initialize as an empty list

    def borrow_book(hero, book):
        if len(hero.borrowed_books) < 2:  # Limit borrowing to 2 books
            if book.borrow():
                hero.borrowed_books.append(book)
                return True 
        return False

    def return_book(hero, book_id):
        for book in hero.borrowed_books:
            if book.book_id == book_id:
                book.return_book()
                hero.borrowed_books.remove(book)
                return True
        return False
    
    def display_details(hero):
        print(f"Member_ID: {hero.member_id}, Name: {hero.member_name}")
        print("Borrowed Books:")
        for book in hero.borrowed_books:
            book.display_details()

class Library:
    def __init__(hero):
        hero.books = []  # List to store books
        hero.members = []  # List to store members

    def add_book(hero, book_title, author):
        book_id = len(hero.books) + 1  # Assign unique ID based on list length
        book = Book(book_title, author, book_id)
        hero.books.append(book)
        print(f"Book '{book_title}' has been added successfully with ID: {book_id}")

    def add_member(hero, member_name, member_id):
        member = Member(member_name, member_id)
        hero.members.append(member)
        print(f"Member '{member_name}' has been added successfully with ID: {member_id}")

    