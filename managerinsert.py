import pymysql as a
conn=a.connect(host="localhost",user="root",password="",database="manager")
mycursor=conn.cursor()
try:
    i="INSERT INTO manager(ID,name,manager_id) values(%s,%s,%s)"
    t=[("1","Alice","None"),("2","Bob","1"),("3","Charlie","1"),("4","David","2")]
    mycursor.executemany(i,t)
    conn.commit()
    print("Data is inserted")
except Exception as e:
    print("Error in data insertion:",e)