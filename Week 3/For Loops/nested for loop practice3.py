for i in range(4):
    for j in range(0,51,10):
        if j == 0:
            j = str(j) + " "  
        print("outside loop--> " + str(i) + " | " + str(j)+ " <--inside loop")