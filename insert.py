import pymysql as guj
conn=guj.connect(
      host="localhost", 
      user="root", 
      password="",
      database="college")
mycursor=conn.cursor()
try:
    ins="INSERT INTO student(st_name,st_class,st_email) values(%s,%s,%s)"
    t=[("neha",'12th','nil@gmail.com'),('raj','10th','raj@gmail.com'),('priya','9th','priya@yahoo.com')]
    mycursor.executemany(ins,t)
    conn.commit();
    print("Insert Data")
except:
    print("Data is error..")

