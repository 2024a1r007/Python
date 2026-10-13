#Write a Python program to input two lists and create a third list containing common elements.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_elements = [element for element in list1 if element in list2]
print("Common elements:", common_elements)  