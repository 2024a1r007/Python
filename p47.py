#write a pp to input numbers in a list and create a new list containing only unique elements

a = []
unique_num  = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input("Enter element: "))
    a.append(element)
for element in a:
    if a not in unique_num:
        unique_num.append(element)
print("Unique elements:", unique_num)