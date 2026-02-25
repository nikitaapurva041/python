import pymysql as d
conn=d.connect(host="localhost",user="root",password="",database="college")
mycursor=conn.cursor()
print("{:<15} {:<15} {:<20}".format("Student class","Student Name","Student E-mail ID",))
try:
    sql="SELECT st_class,st_name,st_email FROM student WHERE st_id BETWEEN 2 and 5"
    mycursor.execute(sql)
    data=mycursor.fetchall()
    for a in data:
        print("{:<15} {:<15} {:<20}".format(a[0],a[1],a[2]))
except Exception as e:
    print("Error in data:",e) 
