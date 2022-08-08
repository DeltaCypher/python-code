# type a message and find out whether it is spam or not

text = input (" Enter the text : ")

if "make lot of money" in text:
    print("spam")
elif "buy now" in text:
    print("spam")
elif "click this" in text:
    print("spam")
else:
    print(text)