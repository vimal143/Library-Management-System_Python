import mysql.connector
import Tables
        
#--------------------------------------------------------------------------------------------------------------------------------        
def displayUser():
    print()
    print("User Records: \n")
    mycursor.execute("""SELECT UserRecord.UserID,UserRecord.UserName,UserRecord.Password,BookRecord.BookName,BookRecord.BookID
                        FROM UserRecord
                        LEFT JOIN BookRecord ON UserRecord.BookID=BookRecord.BookID""")
    records=mycursor.fetchall()
    row_no=0
    for rows in records :
        row_no+=1
        print("******************************","Row no.",row_no,"******************************")
        print("\t             UserID: ", rows[0])
        print("\t           UserName: ", rows[1])
        print("\t           Password: ", rows[2])
        print("\t        Book Issued: ", rows[3])
        print("\t         Its BookID: ", rows[4])
        print()
    x=input("Press any key to return to the User Menu")
    return
#--------------------------------------------------------------------------------------------------------------------------------             
def insertUser():
    while True :
        data=()
        print()
        UserID=input(" Enter UserID: ")
        UserName=input(" Enter User Name: ")
        Password=input(" Enter Password to be Set: ")
        data=(UserID, UserName, Password,None)
        query="INSERT INTO UserRecord VALUES (%s, %s, %s,%s)"
        try:
            mycursor.execute(query,data)
        except mysql.connector.IntegrityError as error:
            print(error) 
            return   
        mydb.commit()
        print()
        ch=input("Do you wish to do add more Users?[Yes/No] : ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
    return
#--------------------------------------------------------------------------------------------------------------------------------             
def deleteUser():
    while True:
        print()
        UserID=input(" Enter UserID whose details to be deleted : ")
        try:  
            mycursor.execute("DELETE from UserRecord where UserID = {0} ".format("\'"+UserID+"\'"))
            if(mycursor.rowcount<=0):
                print("No Row Updated, Please try again with correct details")
                return
        except mysql.connector.Error as e:
            print(e)
            return    
        mydb.commit()
        ch=input("Do you wish to delete more Users?[Yes/No] : ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
    return
#--------------------------------------------------------------------------------------------------------------------------------         
def searchUser():
    while True:
        print()
        Search=input(" Enter UserID to be Searched: ")  
        mycursor.execute("SELECT UserID, UserName, Password , BookName, UserRecord.BookID\
                    FROM Library.UserRecord LEFT JOIN Library.BookRecord\
                    ON BookRecord.BookID=UserRecord.BookID\
                    WHERE UserRecord.UserID={0}".format("\'"+Search+"\'"))
        records=mycursor.fetchall()
        row_no=0
        if records:
            for rows in records :
                row_no+=1
                print("******************************","Searched User Record","******************************")
                print("\t             UserID: ", rows[0])
                print("\t           UserName: ", rows[1])
                print("\t           Password: ", rows[2])
                print("\t        Book Issued: ", rows[3])
                print("\t         Its BookID: ", rows[4])
                print()
        else:
            print("Search Unsuccesfull")
            
        ch=input("Do you wish to Search more Users?[Yes/No] : ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
    return
#--------------------------------------------------------------------------------------------------------------------------------     
def updateUser():
    while True:
        print()
        data=()
        UserID=input(" Enter User ID for whose details need to be updated : ")
        UserName=input(" Enter Updated User Name : ")
        Password=input(" Enter Updated Password : ")
        query="UPDATE UserRecord SET Username = %s, Password = %s WHERE UserID=%s"
        data=(UserName,Password,UserID)
        try:
            mycursor.execute(query,data)
            if(mycursor.rowcount<=0):
                print("No Row Updated, Please try again with correct details")
                return 
        except mysql.connector.Error as e:
            print(e)
            return    
        mydb.commit()
        print("Updated succesfully")
        ch=input("Do you wish to Update more Users?[Yes/No] : ")
        if ch=="no" or ch=="No" or ch=="NO":
            break
    return   
#--------------------------------------------------------------------------------------------------------------------------------     
mydb=mysql.connector.connect(host="localhost",user="root",passwd="54321",database="Library")
mycursor=mydb.cursor()

        
