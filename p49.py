#Write a Python program to rotate a list one position to the right.

numbers = [1, 2, 3, 4, 5]
rotated = [numbers[-1]] + numbers[:-1]
print(rotated)