# write a program to generate multiplication table from 2 to 20 and write it to the different files. 

def table():
    global count

    for x in range (2,21):       
        for y in range(1,12):
            with open ("table1.txt","w") as f:
                if  y == 11:
                    print("\n")
                else:    
                    f.write(str (x*y))
     
table()