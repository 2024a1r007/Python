#write a pp to input marks of 10 students. store only valid marks between 0 and 100 in a list. skip invalid marks.

marks = []
for i in range(1, 11):
    marks.append(int(input(f"Enter marks for student {i}: ")))
valid_marks = [mark for mark in marks if 0 <= mark <= 100]
print("Valid marks:", valid_marks)
