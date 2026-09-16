#write a pp to print floyd's triangle
#1
#2 3
#4 5 6
#7 8 9 10
n = int(input("Enter = "))
start = 1
for i in range(1, n+1):
    for j in range(start, start+i):
        print(j, end=" ")
    print()
    start += i