import pymysql as guj
conn=guj.connect(
      host="localhost", 
      user="root", 
      password="",
      database="college")
mysqlcur=conn.cursor()
tc="create table student(st_id INT primary key auto_increment,st_name varchar(50),st_class varchar(10),st_email varchar(50))"
mysqlcur.execute(tc)