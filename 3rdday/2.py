# Write a python prog to fill the given letter template with name and date. 
n=input("Enter ur name : ")
date=input("Enter Date : ")
letter='''Dear <n>, You are selected! <date>'''
letter=letter.replace("<n>",n)
letter=letter.replace("<date>",date)

print(letter)
print(f'''Dear {n}, You are selected! {date}''')
