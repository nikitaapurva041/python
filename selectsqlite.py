import sqlite3
conn=sqlite3.connect("store.db")
# using select query with limit data(enter limit and numner with value)
data=conn.execute("SELECT * FROM student ")
print("Student id","Student name","Student class","Student email")
for n in data:
     print(n[0],n[1],n[2],n[3])