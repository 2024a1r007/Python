# Milestone 1: Basic Data Handling for a Book Loan

# a) Input book loan details
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
book_title = input("Enter book title: ")

days_kept = int(input("Enter days kept: "))
allowed_days = int(input("Enter allowed days: "))
fine_rate = float(input("Enter daily fine rate (Rs.): "))

# b) Display data types
print("\n--- Data Types ---")
print("Type of days kept:", type(days_kept))
print("Type of fine rate:", type(fine_rate))

# c) Calculate overdue days and total fine
overdue_days = days_kept - allowed_days
total_fine = overdue_days * fine_rate

# d) String operation: Convert student name to uppercase
formatted_name = student_name.upper()

# Display results
print("\n--- Book Loan Details ---")
print("Student Name:", formatted_name)
print("Roll Number:", roll_number)
print("Book Title:", book_title)
print("Days Kept:", days_kept)
print("Allowed Days:", allowed_days)
print("Overdue Days:", overdue_days)
print("Daily Fine Rate: Rs.", fine_rate)
print("Total Fine: Rs.", total_fine)