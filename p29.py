#Write a Python program that asks the user to enter a username and password. The user should get only 3 attempts. If the correct credentials are entered, display "Login Successful" and stop the loop. If all attempts are used, display "Account Locked".
correct_username = "ankita"
correct_password = "123456"
attempts = 3

while attempts > 0:
    username = input("enter username: ")
    password = input("enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Incorrect username or password. Please try again.")
if attempts == 0:
    print("Account Locked")