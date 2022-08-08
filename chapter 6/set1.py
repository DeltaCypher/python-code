# enter 4 number and print which one is gratest

num1 = int (input ("Enter the number1 : "))
num2 = int (input ("Enter the number2 : "))
num3 = int (input ("Enter the number3 : "))
num4 = int (input ("Enter the number4 : "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print(" num1 is gratest")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(" num2 is gratest")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(" num3 is gratest")
else:
    print(" num4 is gratest")