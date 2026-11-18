# main.py

import time

from library_utils import (
    calculate_fine,
    is_available,
    prepare_summary,
    save_record,
    read_records
)

from library_account import LibraryAccount


# Create catalogue
catalogue = {
    "Python Basics": 2,
    "Data Structures": 1,
    "Computer Networks": 2,
    "Operating Systems": 0
}

# Create library account
account = LibraryAccount("M101", "Riya Sharma")

# Display previously saved records
read_records()

# Transaction menu
while True:

    print("\n--- Library Management System ---")
    print("1. Borrow Book")
    print("2. Return Book")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        book = input("Enter book name: ").strip()

        if is_available(catalogue, book):

            try:
                days_kept = int(input("Enter days kept: "))
                fine_rate = float(input("Enter fine rate: "))

                if days_kept < 0 or fine_rate < 0:
                    raise ValueError("Values cannot be negative.")

            except ValueError:
                print("Error: Please enter valid positive numeric values.")
                continue

            account.borrow_book(book)
            catalogue[book] -= 1

            overdue_days = max(0, days_kept - 14)
            fine = calculate_fine(overdue_days, rate=fine_rate)

            transaction_time = time.strftime(
                "%d-%m-%Y %H:%M:%S"
            )

            record = (
                f"{transaction_time} | BORROW | "
                f"{account.student_name} | {book} | "
                f"Fine: Rs. {fine}"
            )

            save_record(record)

            print("Overdue Days:", overdue_days)
            print("Total Fine: Rs.", fine)
            print("Transaction saved successfully.")

        else:
            print("Book unavailable or not found.")

    elif choice == "2":

        book = input("Enter book name to return: ").strip()

        if account.return_book(book):

            catalogue[book] += 1

            transaction_time = time.strftime(
                "%d-%m-%Y %H:%M:%S"
            )

            record = (
                f"{transaction_time} | RETURN | "
                f"{account.student_name} | {book}"
            )

            save_record(record)

            print("Return transaction saved successfully.")

    elif choice == "3":
        break

    else:
        print("Invalid choice. Please try again.")


# Display account summary
print("\n--- Account Summary ---")
account.display_account()

print("Borrowed Books:", prepare_summary(account.borrowed_books))

# Display saved records
read_records()