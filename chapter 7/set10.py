# write a program to d multiplication table of n number in reverse order

num = int(input ("Enter the num : "))
count = 10
for x in range(1,11):
    y = num*count
    count -= 1
    print(y)