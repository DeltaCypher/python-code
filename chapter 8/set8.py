# write a python function to print multiplication table of a given number


def fun(num):
    global count
    for x in range(1,11):
        count = num * x
        print(count)


number = int(input(" Enter the number : "))
print("table of "+str(number)+" is")
fun(number)
