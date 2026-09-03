#take a sentence containing double spaces and unwanted spaces at the beginning or end and clean the sentence
s=input("Enter = ")
s=s.strip()
s=s.replace("  "," ")
print(s) 