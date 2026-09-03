# write a program to take a word and count the number of vowels a,e,i,o,u
word = input("Enter a word: ")
count = sum(1 for char in word if char.lower() in "aeiou")
print("Number of vowels:", count)
