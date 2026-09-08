#write a python program to determine a student eligible for scholarship . the scholarship shuld be granted if the student satisfy either of the following conditions:
#1. the student has a cgpa of 8.5 or above and attendance of 85 percent or above
#2. the student has won a national level competition
#the program should takr cgpa attendence percentage and national level competition status as input and then display whether the student is eligible for scholarship .
cgpa = float(input("Enter CGPA: "))
attendance = float(input("Enter attendance percentage: "))
competition = input("Won national level competition? (yes/no): ")

if (cgpa >= 8.5 and attendance >= 85) or competition == "yes":
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")