import pymysql as guj
conn=guj.connect(host="localhost",user="root",password="",database="college")
mycursor=conn.cursor()
print("{:<17} {:<12} {:<20} {:<20}".format("st_id","st_name","st_class","st_email"))
try:
    st_name=input("Enter the Student Name:- ")
    sql="SELECT * FROM student WHERE st_name=%s"
    mycursor.execute(sql, (st_name,)) 
    data=mycursor.fetchall()
    if data:
     for a in data:
        print("{:<17} {:<12} {:<20} {:<20}".format(a[0],a[1],a[2],a[3]))
    else:
        print("No record found")
except Exception as e:
    print(f"Error in the code: {e}")

conn.close()
