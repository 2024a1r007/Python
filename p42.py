#write a pp to print a centered pyramid using stars

n = int(input("enter number"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()