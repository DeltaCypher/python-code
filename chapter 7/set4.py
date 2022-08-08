# write a program to find out the given number is prime number or not
num = int(input ("Enter the number : "))
prime = True
for x in range(2,num):
    if (num%x) == 0:
        prime = False
        break
    
if prime:
    print(str(num) + " is a prime number")
else:
    print(str(num) + " is not a prime number")    