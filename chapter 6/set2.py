# write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33%, in each subject to pass. assume 3 subjects and take marks as an input from the user.
sub1 = int (input (" Enter the subject1 marks : "))
sub2 = int (input (" Enter the subject2 marks : "))
sub3 = int (input (" Enter the subject3 marks : "))

percentage = ((sub1 + sub2 + sub3)/3)
print("percentage = ", percentage)

if sub1 < 33 or sub2 < 33 or sub3 < 33:
    print(" student is fails becouse he/she have less mark in one subject ")
elif percentage > 40:
    print("student is pass")

