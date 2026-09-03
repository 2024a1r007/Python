#write a pp to take a word and print it in reverse order using slicing. also check whether it is the same forward and backward
word=input("Enter a word: ")
print(word[::-1])
print(word==word[::-1])