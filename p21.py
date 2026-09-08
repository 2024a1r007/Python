#take a password and check length prsence of @ and whether first and last character are different
password = input("Enter password: ")

if len(password) >= 8 and "@" in password and password[0] != password[-1]:
    print("Valid password")
else:
    print("Invalid password")