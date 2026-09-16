#write a pp to print an inverted right-angled triangle using stars
n=int(input("Enter = "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()