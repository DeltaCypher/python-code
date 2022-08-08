# print following pattern using for loop
#     *
#    ***
#   *****

n = 5
for x in range(5):
    print(" " * (n-x-1),end="")
    print("*" * (2*x+1),end="")
    print(" " * (n-x-1))

