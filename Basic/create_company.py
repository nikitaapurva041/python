import pymysql as pet
myobj = pet.connect(
    host="localhost",
    user="root",
    password="")

cursorobj = myobj.cursor()

try:
    database = "CREATE DATABASE company"
    database1= "CREATE DATABASE employee"
    
    cursorobj.execute(database)
    cursorobj.execute(database1)
    print("Database created for company")
    print("Database created for employee ")
except Exception as e:
    print("Database error:", e)

myobj.close()
myobj.close()
