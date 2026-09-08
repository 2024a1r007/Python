student_name = input("Enter student name: ")
branch_name = input("Enter branch name: ")
year = input("Enter year: ")
code_name = student_name[:3] + "-" + branch_name[:3] + "-" + year[-2:]
print("*" * 30)
print("Code Name:", code_name)
print("*" * 30)