import pymysql as guj
conn=guj.connect(host="localhost",user="root",password="",database="college")
mycursor=conn.cursor()
# taking the data from user
"""st_name=input("Enter the student name")
st_class=input("Enter the class name")
st_email=input("Enter the email id")
st_id=input("Enter the student id")
sql="UPDATE student set st_name=%s,st_class=%s,st_email=%s WHERE st_id=%s"""
# update the data through code
st_name="sneha"
st_class="11th"
st_email="sneha@gmail.com"
st_id=3
sql="UPDATE student SET st_name=%s,st_class=%s,st_email=%s WHERE st_id=%s"
data=(st_name,st_class,st_email,st_id)
try:
    mycursor.execute(sql,data)
    conn.commit()
    print("Your database is updated")
except:
    print("Error in your data")
