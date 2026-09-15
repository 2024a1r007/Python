#write a python program to detect whether a comment is spam or not. a comment should be treated as spam if it contains of the keywords: "make a lot of  money", "buy now", "subscribe this" or "click this".

comment=input("Enter a comment: ")
spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

for keyword in spam_keywords:
    if keyword in comment.lower():
        print("Comment is spam")
        break
else:
    print("Comment is not spam")