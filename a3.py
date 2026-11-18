# Milestone 3: Object-Oriented Programming

class LibraryAccount:

    # Class variable
    library_name = "Central Library"

    # Constructor
    def __init__(self, member_id, student_name):
        self.member_id = member_id
        self.student_name = student_name
        self.borrowed_books = []

    # Borrow a book
    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(book, "borrowed successfully by", self.student_name)

    # Return a book
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(book, "returned successfully by", self.student_name)
        else:
            print(book, "not found in borrowed books")

    # Display account details
    def display_account(self):
        print("\nLibrary Name:", LibraryAccount.library_name)
        print("Member ID:", self.member_id)
        print("Student Name:", self.student_name)
        print("Borrowed Books:", self.borrowed_books)

    # String representation
    def __str__(self):
        return (f"Member: {self.student_name}, "
                f"ID: {self.member_id}, "
                f"Books Borrowed: {len(self.borrowed_books)}")


# Creating two objects
account1 = LibraryAccount("M101", "Riya Sharma")
account2 = LibraryAccount("M102", "Rahul Verma")

# Demonstrating borrowing operations
account1.borrow_book("Python Basics")
account1.borrow_book("Data Structures")

account2.borrow_book("Computer Networks")

# Demonstrating return operation
account1.return_book("Python Basics")

# Display account details
print("\n--- Account 1 ---")
account1.display_account()

print("\n--- Account 2 ---")
account2.display_account()

# Display string representation
print("\n--- Account Summary ---")
print(account1)
print(account2)