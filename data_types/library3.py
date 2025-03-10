# Library Management System
# This script implements a simple library management system for IM Library
# It allows for book management, member registration, borrowing, and returning of books

class Book:
    """
    Book class to represent a book in the library.
    
    Attributes:
        book_title (str): Title of the book
        author (str): Author of the book
        book_id (str): Unique identifier for the book
        is_available (bool): Availability status of the book (True if available, False if borrowed)
    """
    
    def __init__(self, book_title, author, book_id):
        """
        Initialize a new Book object.
        
        Args:
            book_title (str): Title of the book
            author (str): Author of the book
            book_id (str): Unique identifier for the book
        """
        self.book_title = book_title
        self.author = author
        self.book_id = book_id
        self.is_available = True  # Initially, all books are available
    
    def borrow(self):
        """Mark the book as borrowed (not available)."""
        if self.is_available:
            self.is_available = False
            return True
        return False  # Book is already borrowed
    
    def return_book(self):
        """Mark the book as returned (available)."""
        if not self.is_available:
            self.is_available = True
            return True
        return False  # Book is already available
    
    def display_details(self):
        """Display the details of the book."""
        status = "Available" if self.is_available else "Borrowed"
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.book_title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print("-" * 30)


class Member:
    """
    Member class to represent a library member.
    
    Attributes:
        member_name (str): Name of the member
        member_id (str): Unique identifier for the member
        borrowed_books (list): List of book IDs borrowed by the member
    """
    
    def __init__(self, member_name, member_id):
        """
        Initialize a new Member object.
        
        Args:
            member_name (str): Name of the member
            member_id (str): Unique identifier for the member
        """
        self.member_name = member_name
        self.member_id = member_id
        self.borrowed_books = []  # Initially, member has no borrowed books
    
    def borrow_book(self, book_id):
        """
        Add a book ID to the member's borrowed books list.
        
        Args:
            book_id (str): ID of the book to borrow
            
        Returns:
            bool: True if successfully added, False if already borrowed
        """
        if book_id not in self.borrowed_books:
            self.borrowed_books.append(book_id)
            return True
        return False  # Member already has this book
    
    def return_book(self, book_id):
        """
        Remove a book ID from the member's borrowed books list.
        
        Args:
            book_id (str): ID of the book to return
            
        Returns:
            bool: True if successfully removed, False if not in borrowed list
        """
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        return False  # Member doesn't have this book
    
    def display_borrowed_books(self):
        """Display all books borrowed by the member."""
        if not self.borrowed_books:
            print(f"{self.member_name} has not borrowed any books.")
        else:
            print(f"Books borrowed by {self.member_name}:")
            for book_id in self.borrowed_books:
                print(f"- Book ID: {book_id}")


class Library:
    """
    Library class to manage books and members.
    
    Attributes:
        books (dict): Dictionary to store all books with book_id as key
        members (dict): Dictionary to store all members with member_id as key
    """
    
    def __init__(self, library_name="IM Library"):
        """
        Initialize a new Library object.
        
        Args:
            library_name (str, optional): Name of the library. Defaults to "IM Library".
        """
        self.library_name = library_name
        self.books = {}  # Dictionary to store books (key: book_id, value: Book object)
        self.members = {}  # Dictionary to store members (key: member_id, value: Member object)
    
    def add_book(self, book_title, author, book_id):
        """
        Add a new book to the library.
        
        Args:
            book_title (str): Title of the book
            author (str): Author of the book
            book_id (str): Unique identifier for the book
            
        Returns:
            bool: True if added successfully, False if book_id already exists
        """
        if book_id not in self.books:
            self.books[book_id] = Book(book_title, author, book_id)
            return True
        return False  # Book ID already exists
    
    def register_member(self, member_name, member_id):
        """
        Register a new member to the library.
        
        Args:
            member_name (str): Name of the member
            member_id (str): Unique identifier for the member
            
        Returns:
            bool: True if registered successfully, False if member_id already exists
        """
        if member_id not in self.members:
            self.members[member_id] = Member(member_name, member_id)
            return True
        return False  # Member ID already exists
    
    def borrow_book(self, member_id, book_id):
        """
        Allow a member to borrow a book.
        
        Args:
            member_id (str): ID of the member
            book_id (str): ID of the book
            
        Returns:
            bool: True if borrowed successfully, False otherwise
        """
        # Check if member and book exist
        if member_id not in self.members or book_id not in self.books:
            return False
        
        # Check if book is available
        book = self.books[book_id]
        if not book.is_available:
            return False
        
        # Borrow the book
        member = self.members[member_id]
        if book.borrow() and member.borrow_book(book_id):
            return True
        return False
    
    def return_book(self, member_id, book_id):
        """
        Allow a member to return a book.
        
        Args:
            member_id (str): ID of the member
            book_id (str): ID of the book
            
        Returns:
            bool: True if returned successfully, False otherwise
        """
        # Check if member and book exist
        if member_id not in self.members or book_id not in self.books:
            return False
        
        # Return the book
        member = self.members[member_id]
        book = self.books[book_id]
        if member.return_book(book_id) and book.return_book():
            return True
        return False
    
    def display_all_books(self):
        """Display all books in the library with their availability."""
        print(f"\n--- {self.library_name} Book Catalog ---")
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books.values():
                book.display_details()
    
    def display_all_members(self):
        """Display all registered members."""
        print(f"\n--- {self.library_name} Member List ---")
        if not self.members:
            print("No registered members.")
        else:
            for member_id, member in self.members.items():
                print(f"Member ID: {member_id}")
                print(f"Name: {member.member_name}")
                member.display_borrowed_books()
                print("-" * 30)


def main():
    """Main function to run the library management system."""
    library = Library()  # Create a library object
    
    # Add some initial books and members for testing
    library.add_book("Python Programming", "John Smith", "B001")
    library.add_book("Data Structures", "Jane Doe", "B002")
    library.add_book("Algorithms", "Robert Johnson", "B003")
    
    library.register_member("Alice", "M001")
    library.register_member("Bob", "M002")
    
    while True:
        print("\n=== IM Library Management System ===")
        print("1. Add a new book")
        print("2. Register a new member")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Check availability of a book")
        print("6. List all books")
        print("7. List all members")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == '1':
            # Add a new book
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            book_id = input("Enter book ID: ")
            
            if library.add_book(title, author, book_id):
                print(f"Book '{title}' added successfully!")
            else:
                print(f"Book ID '{book_id}' already exists!")
                
        elif choice == '2':
            # Register a new member
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            
            if library.register_member(name, member_id):
                print(f"Member '{name}' registered successfully!")
            else:
                print(f"Member ID '{member_id}' already exists!")
                
        elif choice == '3':
            # Borrow a book
            member_id = input("Enter member ID: ")
            book_id = input("Enter book ID: ")
            
            if library.borrow_book(member_id, book_id):
                print("Book borrowed successfully!")
            else:
                print("Failed to borrow book. Check member ID, book ID, and availability.")
                
        elif choice == '4':
            # Return a book
            member_id = input("Enter member ID: ")
            book_id = input("Enter book ID: ")
            
            if library.return_book(member_id, book_id):
                print("Book returned successfully!")
            else:
                print("Failed to return book. Check member ID and book ID.")
                
        elif choice == '5':
            # Check availability of a book
            book_id = input("Enter book ID: ")
            
            if book_id in library.books:
                book = library.books[book_id]
                status = "Available" if book.is_available else "Borrowed"
                print(f"Book '{book.book_title}' is currently {status}.")
            else:
                print(f"Book ID '{book_id}' not found!")
                
        elif choice == '6':
            # List all books
            library.display_all_books()
            
        elif choice == '7':
            # List all members
            library.display_all_members()
            
        elif choice == '8':
            # Exit the program
            print("Thank you for using IM Library Management System!")
            break
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()