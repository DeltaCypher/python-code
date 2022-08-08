# write a program using function to find greatest of three number

def fun1(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(str (num1) + " is greatest ")
    elif num2 > num1 and num2 > num3:
        print(str (num2) + " is greatest")
    else:
        print(str(num3) + " is greatest")


num1 = int (input (" Enter the number 1 : "))
num2 = int (input (" Enter the number 2 : "))
num3 = int (input (" Enter the number 3 : "))
fun1(num1,num2,num3)