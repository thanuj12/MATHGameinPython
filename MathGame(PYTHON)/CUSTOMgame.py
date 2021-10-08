import SUB.EASY
import SUB.MEDIUM
import SUB.HARD
def CUSTOM():
    print("                 GAMEPLAY                 ")
#Prints what game mode it is
    print("The game mode you have chosen is:CUSTOM GAME")
    LEVEL=int(input("\n1=Easy\n2=Medium\n3=Hard\nType Your Difficulty Level:"))
    print("----------------------------------------------------------------------")
    C=0
    W=0
#CHECKS WHETHER THE ENTERED DIFFICULTY LEVEL IS IN RANGE ELSE PRINTS AN ERROR MESSGAGE AND DISPLAYS THE OPTION AGIN TO TYPE THE CORRECT LEVEL
    while(LEVEL==0 or LEVEL>3):
        print("Invalid Choice\nPlease choose the corrrect level ")
        LEVEL=int(input("\n1=Easy\n2=Medium\n3=Hard\nType Your Difficulty Level:"))
        print("----------------------------------------------------------------------")
        continue
#IF THE CHOSEN DIFFICULTY LEVEL IS TRUE IT CALLS A SUB MODULE ACCORDING TO THE CHOSEN LEVEL 
    if(LEVEL==1):
        SUB.EASY.easy()
    else:
        if(LEVEL==2):
            SUB.MEDIUM.medium()
        else:
            if(LEVEL==3):
                SUB.HARD.hard()


    

    
