# write a program to accept marks of 6 students and display them in a sorted manner
m1 = int (input (" enter the subject 1 marks : "))
m2 = int (input (" enter the subject 2 marks : "))
m3 = int (input (" enter the subject 3 marks : "))
m4 = int (input (" enter the subject 4 marks : "))
list1 = [m1,m2,m3,m4]
print(list1)
list1.sort()
print("Sorted list : ",list1)
