#Write a Python program to input a number and check whether it is prime or not. A number is prime if it has no divisor other than 1 and itself.

num = int(input("Enter a number: "))

is_prime = True
if (num <= 1):
    is_prime = False
else:
    for i in range(2, num):
        if (num % i == 0):
            is_prime = False
            break

if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")