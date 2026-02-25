import pymysql as guj
conn=guj.connect(host="localhost",user="root",password="",database="college")
mycursor=conn.cursor()
st_id=input("Enter the student id")
# for deleting the data user will provide the index
sql="DELETE from Student WHERE st_id=%s"
try:
    mycursor.execute(sql,st_id)
    conn.commit()
    print("STUDENT DATA DELETED")
except:
    print("Error in deletion of the data")

    