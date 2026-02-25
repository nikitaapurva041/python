import sqlite3
conn=sqlite3.connect("store.db")

conn.execute(''' UPDATE  student set st_name='Nibha',st_email='nibha@gmail.com' WHERE st_id=2
             ''')
print("Data is updated")
conn.commit()
conn.close()
