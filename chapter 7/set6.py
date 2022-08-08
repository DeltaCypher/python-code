# write a program to find out factorial of a number using for loop
num = int(input(" Enter the num : "))
count = 1
for x in range(1,num):
        x = x + 1
        count = count * x
print(" \nFactorial of",str(num),"is",str (count))