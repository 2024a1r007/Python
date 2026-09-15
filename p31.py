#Write a Python program to input two numbers and find their greatest common divisor using a loop.
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

num1,num2 = a,b
while b != 0:
    remainder = a % b
    a = b
    b = remainder
print(f"The GCD of {num1} and {num2} is {a}")