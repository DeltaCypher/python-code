# write a program to draw following pattern
# ***
# * *
# ***


side = int (input("Enter number of sides : "))

for i in range(side):
    for j in range(side):
        if(i==0 or i==side-1 or j==0 or j==side-1):
            print("*", end=' ')
        else:
            print(' ', end=' ')
    print()