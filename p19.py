#take a roll number and extract admission year program code and roll number digit using slicing
roll = input("Enter roll number: ")

admission_year = roll[:4]
program_code = roll[4:7]
roll_digit = roll[7:]

print("Admission Year:", admission_year)
print("Program Code:", program_code)
print("Roll Number Digit:", roll_digit)