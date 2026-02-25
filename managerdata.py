import pymysql as a
obj=a.connect(host="localhost",user="root",password="",)
mycursor=obj.cursor()
try:
    database="CREATE DATABASE manager"
    mycursor.execute(database)
    print("Database is created")
except Exception as e:
    print("Error in database creation")
obj.commit()
obj.close()


