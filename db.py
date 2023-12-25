import mysql.connector
from prettytable import PrettyTable


def connect():
    
    try:
      mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysqlroot",
        database="NewsVectors"
      )
    except Exception as e:
        print("Problem in connecting to database",e)
        exit(1)
    return mydb;

def insertObject(imageId, obtype,location):
  
  mydb = connect()
  insert_stmt_ob = (
   "INSERT INTO object(IMAGEID, TYPE, CONFIDENCE)"
   "VALUES (%s, %s, %s)"
  )
  rowOb = (imageId,obtype,location)

  try:
    mycursor = mydb.cursor()
    mycursor.execute(insert_stmt_ob,rowOb)   
    mydb.commit()
    print(mycursor.lastrowid)  
  except Exception as e:
    print(e)
    mydb.rollback()
  mydb.close()

def insertNews(imageId, obtype,location):
  
  mydb = connect()
  insert_stmt_ob = (
   "INSERT INTO news(IMAGEID, TYPE, CONFIDENCE)"
   "VALUES (%s, %s, %s)"
  )
  rowOb = (imageId,obtype,location)

  try:
    mycursor = mydb.cursor()
    mycursor.execute(insert_stmt_ob,rowOb)   
    mydb.commit()
    print(mycursor.lastrowid)  
  except Exception as e:
    print(e)
    mydb.rollback()
  mydb.close()



def deleteAllData():
  mydb = connect()
  delete_stmt_image = (
   "DELETE from IMAGE"   
  )
  delete_stmt_object = (
   "DELETE from OBJECT"   
  )

  try:
    mycursor = mydb.cursor()
    mycursor.execute(delete_stmt_image)   
    mycursor.execute(delete_stmt_object)   
    mydb.commit()
        
  except Exception as e:
    print(e)
    mydb.rollback()

  mydb.close()
  

def insertImage(name,location):
  mydb = connect()
  insert_stmt = (
   "INSERT INTO IMAGE(NAME, LOCATION)"
   "VALUES (%s, %s)"
  )

  row = (name,location)
  id = -1
  try:
    mycursor = mydb.cursor()
    mycursor.execute(insert_stmt,row)   
    mydb.commit()
    print(mycursor.lastrowid)
    insertedId = mycursor.lastrowid
  except Exception as e:
    print(e)
    mydb.rollback()

  mydb.close()
  return insertedId;


def getNews(interval):
  mydb = connect()
  select_stmt = (
   "SELECT N.id, N.news, N.entity, N.time FROM NEWS N where "
   " N.time >= NOW() - INTERVAL " + interval + 
   " order by N.time desc"
  )
  
  try:
    mycursor = mydb.cursor()
    mycursor.execute(select_stmt)   
    myresult = mycursor.fetchall()    
    t = PrettyTable(['Id', 'News', 'Entity', 'Time'])   
    for x in myresult:     
     t.add_row([x[0],x[1],x[2],x[3]])
    print(t) 
  except Exception as e:
    print(e)
    mydb.rollback()

  mydb.close()


#imageId = insertImage('key1.jpg','Bedroom')
#id2 = insertObject(imageId,'key','70%')
#showObjects('2 DAY')
#deleteAllData()
#showObjects('10 DAY')
getNews('10 DAY')
