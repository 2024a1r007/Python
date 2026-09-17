#write a pp to input marks of n students in a list. display highest marks,lowest marks,average marks, and number of student who passed.

marks = []
n = int(input("Enter the number of students: "))
for i in range(n):
    marks.append(int(input(f"Enter marks for student {i+1}: ")))
highest_marks = max(marks)
lowest_marks = min(marks)
average_marks = sum(marks) / n
passed_students = sum(1 for mark in marks if mark >= 40)
print(f"Highest marks: {highest_marks}")
print(f"Lowest marks: {lowest_marks}")
print(f"Average marks: {average_marks}")
print(f"Number of passed students: {passed_students}")