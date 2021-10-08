#importing different types of modules
import random
import QUICKGAME
import GAME_MENU
import CUSTOMgame
import PASTgame_details
def main():
    GAME_MENU.MENU()
#Allows the user to input their choice
    choice=int(input("\nEnter Your Option:"))
#Checks if the user's input of choice is within range or else prints an error message and prints the menu again to choose the correct option
    while(choice<=0 or choice>4):
        print("*******************************************************")
        print("Invalid Choice")
        print("\nPlease choose the correct choice")
        GAME_MENU.MENU()
#Allows the user to input their choice
        choice=int(input("\nEnter Your Option:"))

    
#Does a program for each of the choice if it is true
    if(choice==1):
        QUICKGAME.quickgame()#Quickgame module
        import replay
        replay.play()
    else:
        if(choice==2):
            CUSTOMgame.CUSTOM()#Customgame module
            import replay
            replay.play()
        else:
            if(choice==3):
                PASTgame_details.det()
                import replay#The module to be imported if you want to go back to the menu
                replay.back()
            else:
                if(choice==4):
                    #Prints these messages and ends the game
                    print("You have chosen the option to exit the game.\nThank you for playing.\nHave a nice day")
                    print("*****************************************************************")


                    
      
