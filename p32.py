#Write a Python program to check whether a number is a perfect number. A number is perfect if the sum of its proper divisors is equal to the number itself.
 
num = int(input("Enter a number: "))

sum = 0

# Find proper divisors
for i in range(1, num):
    if num % i == 0:
        sum = sum + i

# Check the sum of proper divisors
if sum == num:
    print("Perfect number")
else:
    print("Not a perfect number")