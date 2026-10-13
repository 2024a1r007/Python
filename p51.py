#Write a Python program to count how many times a particular element appears in a list. 
a = [10, 20, 30, 40]

element = 30
count = 0

for num in a:
    if num == element:
        count += 1

print(f"The element {element} appears {count} times in the list.")
