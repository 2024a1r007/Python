# Milestone 2: Catalogue, Decisions and Loops

# a) Create book catalogue using dictionary
catalogue = {
    "Python Basics": 2,
    "Data Structures": 1,
    "Computer Networks": 2,
    "Operating Systems": 0
}

# Create an empty list for borrowed books
borrowed_books = []

# Maximum borrowing limit
maximum_books = 3

# b) Accept book choices repeatedly
while len(borrowed_books) < maximum_books:

    book_choice = input("\nEnter book name (or DONE to finish): ").strip()

    if book_choice.upper() == "DONE":
        break

    # c) Check book availability
    elif book_choice not in catalogue:
        print("Book not found in catalogue!")

    elif catalogue[book_choice] == 0:
        print("Book unavailable! No copies left.")

    # d) Successful borrowing
    else:
        borrowed_books.append(book_choice)
        catalogue[book_choice] -= 1

        print("Book borrowed successfully!")

# e) Display borrowed books and updated catalogue
print("\n--- Borrowed Books ---")

if len(borrowed_books) == 0:
    print("No books borrowed.")
else:
    for book in borrowed_books:
        print(book)

print("\n--- Updated Catalogue ---")

for book, copies in catalogue.items():
    print(book, ":", copies)