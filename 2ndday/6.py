# Write a prog to swap two numbers without using a third variable.
a=int(input("Enter 1: "))
b=int(input("Enter 2: "))
t=a-b
a=a-t
b=a+t
print(a)
print(b)

