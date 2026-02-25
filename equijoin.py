import pymysql as pet
conn=pet.connect(host="localhost",user="root",password="",database="company")
mycursor=conn.cursor()
print("{:<12} {:<15} {:<18} {:<20}".format("Dept. ID","Dept. Name","Location","Salary"))
try:
    i="SELECT department.dept_id,department.dept_name,department.location,employee.salary FROM department,employee WHERE department.dept_id=employee.dept_id"
    mycursor.execute(i)
    data=mycursor.fetchall()
    for a in data:
        print("{:<12} {:<15} {:<18} {:<20}".format(a[0],a[1],a[2],a[3]))
except Exception as e:
    print("Error in data")
 