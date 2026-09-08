#take student full name and roll number. generate email using first 3 letters of first name , first 3 letters of last name and last 3 character of roll number.
name = input("Enter full name: ")
roll = input("Enter roll number: ")

n = name.split()

email = n[0][:3] + n[-1][:3] + roll[-3:] + "@gmail.com"

print("Email:", email)