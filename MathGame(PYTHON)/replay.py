import MAIN_2
def play():
    print("---------------------------------------------------------------")
    print("\nDo u want to play again?\nY=YES\nN=NO")
    print("REPLY WITH CAPITAL LETTERS")
    choice=input("\nEnter your choice Y or N = ")
    if(choice=="Y" or choice=="y"):
        MAIN_2.main()
    else:
        if(choice=="N" or choice=="n"):
            print("--------------------------------")
            print("You are about to exit the game""\nThank you for playing.\nHave a nice day")
            print("--------------------------------")

def back():
    print("---------------------------------------------------------------")
    print("\nDo you want to go back?\nY=YES\nN=NO")
    print("REPLY WITH CAPITAL LETTERS")
    choice=input("\nEnter your choice Y or N = ")
    if(choice=="Y" or choice=="y"):
        MAIN_2.main()
    else:
        if(choice=="N" or choice=="n"):
            print("--------------------------------")
            print("You are about to exit the game""\nThank you for playing.\nHave a nice day")
            print("--------------------------------")
    
    
    
    

