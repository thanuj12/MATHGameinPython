import mysql.connector
def det():
    print("1) Print Quick Game past details")
    print("2) Print Custom Game past details")
    print("3) Delete Custom Game record")
    print("4) Delete Quick Game record")


    OPT=int(input("Enter your option"))
    if(OPT==1):
        count=0
        conDict={'host':'localhost',
                 'database':'past_game_details',
                 'user':'root',
                 'password':''}

        db=mysql.connector.connect(**conDict)

        cursor=db.cursor()

        cursor.execute("SELECT * FROM quick_game")
    
        data = cursor.fetchall()
        print(": RECORD NO :       NAME        : CORRECT QUESTIONS : TOTAL QUESTIONS : PERCENTAGE :")
    
        for item in data:
            print(":",item[0]," "*(8-len(str(item[0]))),":",
                  item[1]," "*(16-len(item[1])),":",
                  item[2]," "*(16-len(str(item[2]))),":",
                  item[3]," "*(14-len(str(item[3]))),":",
                  item[4]," "*(9-len(str(item[4]))),":")
            print("\n")

        db.close()
        
    else:
        if(OPT==2):
            count=0
            conDict={'host':'localhost',
                     'database':'past_game_details',
                     'user':'root',
                     'password':''}

            db=mysql.connector.connect(**conDict)

            cursor=db.cursor()

            cursor.execute("SELECT * FROM custom_game")
            data=cursor.fetchall()
            print(": RECORD NO :       NAME        : CORRECT QUESTIONS : TOTAL QUESTIONS : PERCENTAGE :   LEVEL   :")
    
            for item in data:
                print(":",item[0]," "*(8-len(str(item[0]))),":",
                      item[1]," "*(16-len(item[1])),":",
                      item[2]," "*(16-len(str(item[2]))),":",
                      item[3]," "*(14-len(str(item[3]))),":",
                      item[4]," "*(9-len(str(item[4]))),":",
                      item[5]," "*(8-len(item[5])),":")
                print("\n")

            db.close()
        else:
            if(OPT==3):
                conDict={'host':'localhost',
                         'database':'past_game_details',
                         'user':'root',
                         'password':''}

                db=mysql.connector.connect(**conDict)

                cursor=db.cursor()

                uNo=input("Enter the record")
                cursor.execute("DELETE FROM custom_game WHERE RECORD_NO = "+ uNo +"")

                db.commit()

                print(cursor.rowcount, "Record Deleted")

                db.close()
            else:
                if(OPT==4):
                    conDict={'host':'localhost',
                             'database':'past_game_details',
                             'user':'root',
                             'password':''}

                    db=mysql.connector.connect(**conDict)

                    cursor=db.cursor()

                    uNo=input("Type the record number : ")

                    cursor.execute("DELETE FROM quick_game WHERE RECORD_NO = "+ uNo +"")

                    db.commit()

                    print(cursor.rowcount, "Record Deleted")

                    db.close()



               
    
    
    
