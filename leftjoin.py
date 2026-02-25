import pymysql as pet
conn=pet.connect(host="localhost",user="root",password="",database="company")
mycursor=conn.cursor()
print("{:<15} {:<17} {:<20} {:<20}".format("Emp id","Emp name","Dept id","Location"))
try:
    sql="SELECT employee.emp_id,employee.emp_name,employee.dept_id,department.location from employee left join department on employee.dept_id=department.dept_id"
    mycursor.execute(sql)
    data=mycursor.fetchall()
    for a in data:
        print("{:<15} {:<17} {:<20} {:<20}".format(a[0],a[1],a[2],a[3]))
except Exception as e:
    print("Error in data")