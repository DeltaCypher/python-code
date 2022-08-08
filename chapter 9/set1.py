# write a program to read the text from a given file "poems.txt" and 
# find out whether it contains the word "twinkle".


a = open ('poems.txt','r')
b = a.read()
if "twinkle" in b: 
    print(" twinkle is present ")
else:
    print(" twinkle is not present ")
a.close()