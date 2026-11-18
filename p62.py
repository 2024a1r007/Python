#Write a Python program that allows a librarian to add several books to a library. For each book, ask the user to enter its title and the number of copies. Store each book and its available copy count in a dictionary.
#After the books have been added, display a menu that lets the user issue a book, return a book, display all books, or exit the program.
#Apply these conditions:
#Book titles should be compared without distinguishing uppercase and lowercase letters.
#A book can be issued only if it exists in the library and at least one copy is available.
#Issuing a book decreases its available copy count by one.
#A book can be returned only if it exists in the library and at least one copy has already been issued.
#Returning a book increases its available copy count by one.
#Display an appropriate message for an unavailable book, an invalid choice, or an invalid number of copies.
class Library:
    def __init__(self):
        self.books = {}
    def add_book(self, title, copies):
        key = title.lower()
        self.books[key]=[title,copies,copies]
    def issue_book(self, title):
        key = title.lower()
        if key not in self.books:
            print("Book not found.")
        elif self.books[key][1] == 0:
            print("No copies are available")
        else:
            self.books[key][1] -= 1
            print("Book issued successfully.")
    def return_book(self, title):
        key = title.lower()
        if key not in self.books:
            print("Book not found.")
        elif self.books[key][1] == self.books[key][2]:
            print("No copy of this book is currently issued")
        else:
            self.books[key][1] += 1
            print("Book returned successfully.")
    def display_books(self):
        print("\nlibrary Books")
        for details in self.books.values():
            title = details[0]
            available_copies = details[1]
            print(title, "-Available copies:", available_copies)

library = library()
number_of_books = int("How many different books do you want to add?")
for i in range(number_of_books):
    title = input("Enter book title: ").strip()
    copies = int(input("Enter number of copies: "))
if copies <= 0:
    print("Number of copies must be greater than zero.")
else:
    library.add_book(title, copies)
    print("Book added successfully.")
while True:
    print("\n1. Issue book")
    print("2. Return book")
    print("3. Display all books")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == 1:
        title = input("Enter book title: ").strip()
        library.issue_book(title)
    elif choice == 2:
        title = input("Enter book title: ").strip()
        library.return_book(title)
    elif choice == 3:
        library.display_books()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please enter 1,2,3, or 4.")

