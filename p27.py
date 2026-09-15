#write a pp to input 4 numbers from the user and find the gratest number among them
a = int(input("enter 1st no:"))
b = int(input("enter 2st no:"))
c = int(input("enter 3st no:"))
d = int(input("enter 4st no:"))
if a>= b and a >= c and a>=d:
    print("greatest no: ")
elif b>= a and b>= c and b>=d:
    print("greatest no: ")
elif c>= a and c>= b and c>=d:
    print("greatest no: ")
else:
    print("greatest no: ", d)

