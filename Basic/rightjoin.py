import pymysql as pet
conn=pet.connect(host="localhost",user="root",password="",database="company")
mycursor=conn.cursor()
print("{:<12}{:<15}{:<20} {:<20}".format("Dept. id","Dept. name","location","Emp.name"))
try:
    sql="SELECT department.dept_id,department.dept_name,department.location,employee.emp_name from department right join employee on employee.dept_id=department.dept_id"
    mycursor.execute(sql)
    data=mycursor.fetchall()
    for a in data:
     print("{:<12}{:<15}{:<20} {:<20}".format(a[0],a[1],a[2],a[3]))
except Exception as e:
    print("Error in Data") 
