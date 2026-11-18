# library_utils.py

# Calculate fine with default rate
def calculate_fine(overdue_days, rate=5):
    return overdue_days * rate


# Check book availability
def is_available(catalogue, book_title):
    return book_title in catalogue and catalogue[book_title] > 0


# Prepare borrowed books summary
def prepare_summary(borrowed_books):
    if len(borrowed_books) == 0:
        return "No books borrowed."

    return ", ".join(borrowed_books)


# a) Append transaction to file
def save_record(transaction, filename="library_records.txt"):
    with open(filename, "a") as file:
        file.write(transaction + "\n")


# b) Read and display saved records
def read_records(filename="library_records.txt"):
    try:
        with open(filename, "r") as file:
            records = file.readlines()

        print("\n--- Saved Library Records ---")

        if records:
            for record in records:
                print(record.strip())
        else:
            print("No records available.")

    except FileNotFoundError:
        print("Error: Library records file not found!")
        print("Correction: A new file will be created when a transaction is saved.")