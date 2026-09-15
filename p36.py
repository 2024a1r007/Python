#Write a Python program to repeatedly calculate the sum of digits of a number until the result becomes a single digit.

num = int(input("Enter a number: "))

while num > 9:
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num = num // 10
    num = sum