import pymysql as a
conn=a.connect(host="localhost",user="root",password="",database="manager")
mycursor=conn.cursor()
database="CREATE TABLE manager(ID INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(50),manager_id INT)"
try:
 mycursor.execute(database)
 print("Data is inserted ")
except Exception as e:
 print("Tables are created")
