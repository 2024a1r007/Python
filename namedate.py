letter = '''
Dear <NAME>,
You are selected!
<DATE>
'''
name = input("enter your name: ")
data = input("enter date: ")
letter = letter.replace("<NAME>", name)
letter = letter.replace("<DATE>", data)
letter = letter.replace("<DATE>", data)
print(letter)
