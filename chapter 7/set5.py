# write a program to find a sum of first n natural number using while loop

num = int (input(" Enter the number : "))
count1 = 0
count2 = 0
while count1 < num:
    count1 += 1
    count2 += count1
    print(count2)
