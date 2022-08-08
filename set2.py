# the game() function in a program lets a user play a game and returns the score as an integer.
# you need to read a file "history.txt" which is either blank or contains the previous highscore.
#  you need to write a program to update the highscore whenever game() breaks the highscore.

from turtle import clear


def game():
    a = int (input (" Enter the new score : "))
    return a

score = game()
with open ("highscore.txt","r") as f:
    highscore = int (f.read())

if highscore == ' ':
    with open ("highscore.txt","w") as f:
        f.write(str(score))

elif highscore < score :
    with open ("highscore.txt","w") as f:
        f.write(str(score))



