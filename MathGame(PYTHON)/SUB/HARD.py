import random
import mysql.connector
def hard():
    C=0
    W=0
    #Inputs your name and stores it in a variable called NAME.
    NAME=input("\nType Your Name:")
    print("GOODLUCK",NAME)
    print("The difficulty of the game is HARD")
    Q=int(input("\nEnter The Number Of Questions You Wish To Answer"))
    questions=[]
    #Prints the questions for the user to be answered in a loop
    for i in range(1,Q+1):
        print("\n")
        s=random.choice(['+','-','*'])
        q=str(random.randrange(100)) + s + str(random.randrange(100))
        USERans=int(input(q+ "="))
        questions.append((q,USERans))

    print("\n--------------------------------RESULTS-----------------------------------")
    #Prints the results for each questions and also prints the final score
    for q,a in questions:
        print("\n")
        correct_answer=eval(q)
        if correct_answer == a:
            print(q, "correct")
            C+=1
        else:
            print(q,"[","Incorrect","]","[","The actual answer is",correct_answer,"]")
            W+=1    
    
        
    P=int((C/Q)*100)
    print("\n-------------------------------------FINAL RESULTS---------------------------------------")
    print("\nYour name is",NAME)
    print("\nThe number of questions you have answered correctly is",C)
    print("\nThe number of questions you have answered incorrectly is",W)
    print("\nThe final score is:",P,"%")
    print("\n----------------------------------------------------------------------------")

    #Opens a database connectiona and inputs the record into the selected table
    conDict={'host':'localhost',
             'database':'past_game_details',
             'user':'root',
             'password':''}

    db=mysql.connector.connect(**conDict)
    
    cursor=db.cursor()
    
    Insert=("INSERT INTO custom_game(Name, CORRECT_questions, TOTAL_questions, PERCENTAGE, LEVEL) VALUES (%s,%s,%s,%s,'HARD')")
    val=NAME, C, Q, P,
    cursor.execute(Insert,val)
    

    db.commit()

    print(cursor.rowcount, "Record Added")
    db.close()
    print("----------------------------------------------------------------------------")

    
