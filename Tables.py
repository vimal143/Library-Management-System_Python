import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="54321")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS Library")
mycursor.execute("USE Library")

mycursor.execute("SHOW TABLES LIKE 'BookRecord' ")
result=mycursor.fetchone()
if result : 
    pass
else : #if Table doesn't exists then it will be created
    mycursor.execute("""CREATE TABLE BookRecord(BookID varchar(10) PRIMARY KEY , BookName varchar(35) , Author varchar(30) , Publisher varchar(30)) """)


mycursor.execute("SHOW TABLES LIKE 'UserRecord' ")
result=mycursor.fetchone()
if result : 
    pass
else : #if Table doesn't exists then it will be created
    mycursor.execute("""CREATE TABLE UserRecord(UserID varchar(15) PRIMARY KEY, UserName varchar(20),
                            Password varchar(20), BookID varchar(10),FOREIGN KEY (BookID) REFERENCES BookRecord(BookID))""")
    data1=("101","Barad Sneha","Sneha@1",None)
    query1="INSERT INTO UserRecord VALUES(%s, %s, %s, %s)"
    mycursor.execute(query1,data1)
    mydb.commit()
    
mycursor.execute("SHOW TABLES LIKE 'AdminRecord' ")
result=mycursor.fetchone()
if result : 
    pass
else: #if Table doesn't exists then it will be created
    mycursor.execute("""CREATE TABLE AdminRecord(AdminID varchar(15) PRIMARY KEY, Password varchar(20))""")
    data4=("Sneha211","Sneha&1")
    query2="INSERT INTO AdminRecord VALUES(%s, %s)"
    mycursor.execute(query2,data4)
    mydb.commit()
    
    
mycursor.execute("SHOW TABLES LIKE 'Feedback' ")
result=mycursor.fetchone()
if result : 
    pass
else : #if Table doesn't exists then it will be created
    mycursor.execute("""CREATE TABLE Feedback(Feedback varchar(100) PRIMARY KEY, Rating varchar(10))""")


    

