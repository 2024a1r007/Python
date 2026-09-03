name = input("Enter the student's name: ")
roll_number = input("Enter the student's roll number: ")


name_initials = name[:3]


roll_number_last_digits = roll_number[-2:]


username = name_initials + roll_number_last_digits


print("Username:", username)