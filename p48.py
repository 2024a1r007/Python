#Write a Python program to input numbers in a list and create two separate lists for even and odd numbers.


even_num = []
odd_num = []
n = int(input("Enter the number of elements: "))
for i in n:
    if i%2 == 0:
        even_num.append(i)
    else:
        odd_num.append(i)
print("Even numbers:", even_num)
print("Odd numbers:", odd_num)