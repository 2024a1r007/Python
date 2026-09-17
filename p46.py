#write a pp to input numbers in a list and find the second largest number.

a = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    a.append(element)
a.sort()
print("Second largest number is:", a[-2])