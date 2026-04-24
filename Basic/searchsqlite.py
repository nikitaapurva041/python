import sqlite3
conn=sqlite3.connect("store.db")
data=conn.execute("SELECT * FROM student WHERE st_name=" "+st_name=" " ")
for a in data:
    print(a[0]," ",a[1]," ",a[2])
conn.commit()
conn.close()
