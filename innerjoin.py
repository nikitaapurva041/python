import pymysql as pet
conn=pet.connect(host="localhost",user="root",password="",database="company")
mycursor=conn.cursor()
print("{:<15} {:20} {:<20} {:<20}".format("emp_id","emp_name","salary","dept_id"))
try:
    sql="SELECT * FROM employee inner join department on employee.dept_id= department.dept_id "
    mycursor.execute(sql)
    data=mycursor.fetchall()
    for s in data:
        print("{:<15} {:20} {:<20} {:<20}".format(s[0],s[1],s[2],s[3]))
except Exception as e:
    print("Error in data")

