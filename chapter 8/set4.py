# write a recursive function to calculate the sum of first n natural number
def fun(num):
    if num == 1 or num == 0:
        return 1
    else:
        return (num + fun(num - 1))

number = int (input(" enter the number = "))
f = fun(number)
print("Sum is " + str(f))