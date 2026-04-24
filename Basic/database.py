import pymysql as guj

myobj = guj.connect(
    host="localhost",
    user="root",
    password=""
)

cursorobj = myobj.cursor()

try:
    db = "CREATE DATABASE college"
    cursorobj.execute(db)
    print("Database created")
except Exception as e:
    print("Database error:", e)

myobj.close()
