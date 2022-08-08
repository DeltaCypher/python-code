# write a python function to remove a given word form a string and strip it at the same time.
def replace_and_strip(string,word):
    newstring = string.replace (word,"")
    return newstring.strip()

this = "  kiran, hello and good morning "
n = replace_and_strip(this,"kiran")
print(n)