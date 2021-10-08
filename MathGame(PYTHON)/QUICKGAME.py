import random
import mysql.connector
def quickgame():
    print("\n")
    print("                GAMEPLAY                 ")
    print("The game mode you have chosen is:QUICK GAME")#PRINTS THE GAME MODE
    NAME=input("\nEnter your name:")#ALLOWS USER TO ENTER THEIR NAME
    print("GOODLUCK",NAME)
    C=0
    W=0
    questions=[]
    for i in range(5):
        print("\n")
        q=str(random.randrange(10)) + "+" + str(random.randrange(10))
        USERans=int(input(q+ "="))
        questions.append((q,USERans))

    print("\n--------------------------------RESULTS-----------------------------------")
    for q,a in questions:
        print("\n")
        correct_answer=eval(q)
        if correct_answer == a:
            print(q, "correct")
            C+=1
        else:
            print(q,"Incorrect","[","The actual answer is",correct_answer,"]")
            W+=1


    P=int((C/5)*100)#Calculating percentage of the final score
    #Printing the final results
    print("\n-------------------------------------FINAL RESULTS---------------------------------------")
    print("\nYour name is",NAME)
    print("\nThe number of questions you have answered correctly is",C)
    print("\nThe number of questions you have answered incorrectly is",W)
    print("\nThe final score out of 5 is:",C)
    print("Percentage of the final score",P)
    print("\n----------------------------------------------------------------------------")
    #Connecting to a database and entering the records 
    conDict={'host':'localhost',
             'database':'past_game_details',
             'user':'root',
             'password':''}

    db=mysql.connector.connect(**conDict)
    
    cursor=db.cursor()
    
    Insert=("INSERT INTO quick_game(Name, CORRECT_questions, TOTAL_questions, PERCENTAGE) VALUES (%s,%s,%s,%s)")
    val=NAME, C, 5, P
    cursor.execute(Insert,val)
    

    db.commit()

    print(cursor.rowcount, "Record Added")

    db.close()
    print("----------------------------------------------------------------------------")



