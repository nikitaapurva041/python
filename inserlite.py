import sqlite3
conn=sqlite3.connect("store.db")
ins='''
        insert into student (st_id,st_name,st_class,st_email)
        VALUES ('3','Nilam','11th','nilam@gmail.com') '''
print("Data inserted")
conn.execute(ins)
conn.commit()
conn.close()