import mysql.connector
import sys
from prettytable import PrettyTable


if (len(sys.argv) != 2):
  print("Please pass the root password as line arugment!")
  print("test checkin")
  exit(1)



def version():
    try:
        mydb = connect()       
        cur = mydb.cursor()
        cur.execute("SELECT VERSION()")
        data = cur.fetchone()   
        print("Database version : %s " % data)
       
    except Exception as e : 
        print("Error %d: %s",e.args[0],e.args[1])
        sys.exit(1)
   
    finally:           
        if mydb:     
            mydb.close()



def connect():


  mydb = mysql.connector.connect(
    host="localhost",
    user="root",   
    password = sys.argv[1],
    auth_plugin = 'caching_sha2_password'    
    #password="mysqlroot",
    #password="root",
    #database="NewsVectors"
  )
  return mydb;



def createDatabase():
   mydb = connect()
   try:
    create_stmt = (  
    "CREATE DATABASE NewsVectors")   
    
    mycursor = mydb.cursor()
    mycursor.execute(create_stmt) 
    
   except Exception as e:
    print(e)
    mydb.rollback()
    
   mydb.close()

def dropUser():
   mydb = connect()
   try:
    drop_stmt = (  
    "DROP User \'iouser@localhost\' ")     
    mycursor = mydb.cursor()
    mycursor.execute(drop_stmt) 
    print("dropped user")
    
   except Exception as e:
    print(e)
    mydb.rollback()
   

   mydb.close()


def createUser():
   mydb = connect()
   try:
    create_stmt = (  
    "CREATE User \'iouser@localhost\' IDENTIFIED BY \'io123456\' ")   
    print(create_stmt)
    mycursor = mydb.cursor()
    mycursor.execute(create_stmt) 
    
    
    grant_stmt_1 = (  
    "GRANT ALL PRIVILEGES ON NewsVectors.IMAGE TO iouser@localhost ")
    
    grant_stmt_2 = (  
    "GRANT ALL PRIVILEGES ON NewsVectors.OBJECT TO iouser@localhost ")
    
    flush_stmt_3 = (
    "FLUSH PRIVILEGES")
    
    mycursor.execute(grant_stmt_1) 
    mycursor.execute(grant_stmt_2) 
    mycursor.execute(flush_stmt_3) 
    print("created user iouser")
   except Exception as e:
    print(e)
    mydb.rollback()
   
   mydb.close()



def deleteDatabase():
   mydb = connect()
   try:
    create_stmt = (  
    "DROP DATABASE NewsVectors")   
    
    mycursor = mydb.cursor()
    mycursor.execute(create_stmt) 
    print("Deleted Database NewsVectors")
   except Exception as e:
    print(e)
    mydb.rollback()
    
   mydb.close()


def createNewsTable():

   mydb = connect()
   try:
    create_stmt = (  
    "CREATE TABLE NewsVectors.News ("
    "id int NOT NULL PRIMARY KEY AUTO_INCREMENT, "
    "time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, "
    "entity varchar(45) DEFAULT NULL, "
    "news varchar(45) DEFAULT NULL, "
    "sentiment varchar(45) DEFAULT NULL, "
    "numvalue varchar(45) DEFAULT NULL, "
    "currency varchar(45) DEFAULT NULL )" )
    mycursor = mydb.cursor()
    mycursor.execute(create_stmt) 
    print("Created news Table")
   except Exception as e:
    print(e)
    mydb.rollback()
    
   mydb.close()



def createImageTable():

   mydb = connect()
   try:
    create_stmt = (  
    "CREATE TABLE NewsVectors.Image ("
    "id int NOT NULL PRIMARY KEY AUTO_INCREMENT, "
    "name varchar(45) DEFAULT NULL, "
    "location varchar(45) DEFAULT NULL, "
    "time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP)")   
    
    mycursor = mydb.cursor()
    mycursor.execute(create_stmt) 
    print("Created Image Table")
   except Exception as e:
    print(e)
    mydb.rollback()
    
   mydb.close()
  
def createObjectTable():

   mydb = connect()
   try:
    create_stmt = (         
    "CREATE TABLE NewsVectors.Object ("
    "id int NOT NULL PRIMARY KEY AUTO_INCREMENT, "
    "imageid int NOT NULL, "
    "confidence varchar(45) DEFAULT NULL, "
    "type varchar(45) DEFAULT NULL, "
    "location varchar(45) DEFAULT NULL, "
    "time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP) "
    )

    mycursor = mydb.cursor()
    mycursor.execute(create_stmt) 
    print("Created Object Table")
    
   except Exception as e:
    print(e)
    mydb.rollback()
    
   mydb.close()
 
version()
dropUser()
deleteDatabase() 
createDatabase()
createUser()
createNewsTable()
#createImageTable()
#createObjectTable()


