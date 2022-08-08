# write a program to create table for any number using while loop
num = int(input (" Enter the number : "))
count = 1
table = 0 
while count <= 10:
    table = num * count
    count += 1
    print(table)