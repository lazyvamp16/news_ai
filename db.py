import mysql.connector
from prettytable import PrettyTable


def connect():
    
    try:
      mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        #password="mysqlroot",
        password="root",
        database="NewsVectors"
      )
    except Exception as e:
        print("Problem in connecting to database",e)
        exit(1)
    return mydb



def insertNews(entity, news):
  
  mydb = connect()
  insert_stmt_ob = (
   "INSERT INTO news(Entity, NEWS)"
   "VALUES (%s, %s)"
  )
  rowOb = (entity,news)

  try:
    mycursor = mydb.cursor()
    mycursor.execute(insert_stmt_ob,rowOb)   
    mydb.commit()
    #print(mycursor.lastrowid)  
  except Exception as e:
    print(e)
    mydb.rollback()
  mydb.close()


def updateNews(id, sentiment):
  
  mydb = connect()
  insert_stmt_ob = (
   "UPDATE NEWS set SENTIMENT = '" + sentiment + "' where ID = " + str(id) 
  )
  #rowOb = (sentiment)

  try:
    mycursor = mydb.cursor()
    mycursor.execute(insert_stmt_ob)   
    mydb.commit()
    #print(mycursor.lastrowid)  
  except Exception as e:
    print(e)
    mydb.rollback()
  mydb.close()






def deleteAllData():
  mydb = connect()
  delete_stmt_news = (
   "DELETE from NEWS"   
  )
 
  try:
    mycursor = mydb.cursor()
    mycursor.execute(delete_stmt_news)   
    mydb.commit()
        
  except Exception as e:
    print(e)
    mydb.rollback()

  mydb.close()
  



def getNews2():
  Inputdata=[]
  data=[]
  mydb = connect()
  #print("connected")
  select_stmt = ("SELECT N.id, N.time, N.entity, N.news FROM NEWS N ")
  try:
    mycursor = mydb.cursor()
    mycursor.execute(select_stmt)   
    myresult = mycursor.fetchall()    
    for x in myresult:   
       Inputdata.append((x[3]))
       l=[]  
       l.append(x[0])
       l.append(x[1])
       l.append(x[2])
       l.append(x[3])
       data.append(l)

  except Exception as e:
    mydb.rollback()
  mydb.close()
  #print(d)
  return(Inputdata,data)





def showNews(interval):
  mydb = connect()
  select_stmt = (
   "SELECT N.id, N.news, N.entity, N.SENTIMENT, N.time FROM NEWS N where "
   " N.time >= NOW() - INTERVAL " + interval + 
   " order by N.time desc"
  )

  
  try:
    mycursor = mydb.cursor()
    mycursor.execute(select_stmt)   
    myresult = mycursor.fetchall()    
    t = PrettyTable(['Id', 'News', 'Entity', 'Sentiment','Time'])   
    for x in myresult:     
     t.add_row([x[0],x[1],x[2],x[3],x[4]])
    print(t) 
  except Exception as e:
    print(e)
    mydb.rollback()

  mydb.close()



if __name__ == "__main__":
    #deleteAllData()
    insertNews("TataMotors", "Price increased 3 percent in last 30 days")
    insertNews("TataMotors", "TataMotor stock hits 52 week low")
    insertNews("TataMotors", "5 lakh registrations for Tata Nexon in 2023")
    #updateNews("1", "POSITIVE")
    #updateNews("2", "NEGATIVE")
    #showNews('10 DAY')
