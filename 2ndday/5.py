# Write a prog to take two inputs a  and b, swap their values using a temp variable and print updated values
a=int(input("Enter 1: "))
b=int(input("Enter 2: "))
temp=0
temp=b
b=a
a=temp
print(a)
print(b)

