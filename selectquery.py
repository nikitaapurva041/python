import pymysql as guj
conn=guj.connect(
      host="localhost", 
      user="root", 
      password="",
      database="college")
mycursor=conn.cursor()
print("{:<17} {:<12} {:<20} {:<20}".format("st_id","st_name","st_class","st_email"))
try:
    # for all getting data
    sql= "SELECT * FROM student"
    mycursor.execute(sql)
    data=mycursor.fetchall()
    for a in data:
     print("{:<17} {:<12} {:<20} {:<20} ".format(a[0],a[1],a[2],a[3]))
     # for single id getting data
    sql= "SELECT st_id,st_name FROM student WHERE st_id=2"
    mycursor.execute(sql)
    data=mycursor.fetchone()
    print("{:<17} {:<12} ".format(data[0],data[1]))
except:
     print("Error in Data")
      

