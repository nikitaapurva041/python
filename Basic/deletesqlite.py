import sqlite3
conn=sqlite3.connect("store.db")
st_id=input("Enter the student id:-")
conn.execute("DELETE FROM student WHERE st_id="+st_id)
print("Data is deleted")
conn.commit()
conn.close()
