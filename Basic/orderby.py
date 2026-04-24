import pymysql as guj
conn=guj.connect(host="localhost",user="root",password="",database="college")
mycursor=conn.cursor()
print("{:<15} {:<20} {:<20}".format("st_id","st_name","st_class","st_email"))
try:
    # Here using order by with ASC,DESC and limit 
    sql="SELECT * FROM student  order by st_name ASC LIMIT 2,4"
    mycursor.execute(sql)
    data=mycursor.fetchall()
    for a in data:
        print("{:<15} {:<20} {:<20}".format(a[0],a[1],a[2]))
except:
    print("Error in Data")
