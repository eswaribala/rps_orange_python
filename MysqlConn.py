'''
Created on 18-Jul-2017

@author: BALASUBRAMANIAM
'''
import pymysql

def getConnection():
    global db
    db=pymysql.connect(host="localhost",
                   user='root',passwd='vignesh',
                   db='orangedb')
    return db

def readAll():
    cursor=db.cursor()
    query = 'select * from employee'
    cursor.execute(query)
    return cursor.fetchall()

def getEmployeeById(id):
    cursor=db.cursor()
    cursor.execute("""select * from Employee where 
    Employee_Id='%s'""" %(id))
    return cursor.fetchall()
 
def insertEmployee(id,fname,lname):
    cursor=db.cursor()
    try:
        
        cursor.execute("""INSERT INTO Employee
        (Employee_Id,
        First_Name,Last_Name)
        VALUES ('%d','%s','%s')""" %(id,fname,lname))
      
        db.commit()
    except :
          
        db.rollback()
    finally:
        db.close()

getConnection()
insertEmployee(43568,'Sunil','Sharma')



'''
rows=getEmployeeById(1234)
for row in rows:
    for col in row:
        print(col,end='\t') 
'''
#db.close()