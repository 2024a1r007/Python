# library_account.py

class LibraryAccount:

    library_name = "Central Library"

    def __init__(self, member_id, student_name):
        self.member_id = member_id
        self.student_name = student_name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(book, "borrowed successfully.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(book, "returned successfully.")
            return True
        else:
            print("Book not found in borrowed books.")
            return False

    def display_account(self):
        print("Member ID:", self.member_id)
        print("Student Name:", self.student_name)
        print("Borrowed Books:", self.borrowed_books)

    def __str__(self):
        return (f"Member: {self.student_name}, "
                f"Books Borrowed: {len(self.borrowed_books)}")