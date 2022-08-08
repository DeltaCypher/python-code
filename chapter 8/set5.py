# write a python function to print first n lines of the following pattern.
# * * *    &      *               
# * *             * *
# *               * * *



def fun1(n):
    if n == 0:
        return 
    else:    
        print("*" * n)
        fun1(n-1)

def fun2(n):
    if n == 0:
        return 
    else:    
        fun2(n-1)
        print("*" * n)

num = int(input(" Enter the num : "))
fun1(num)
fun2(num)