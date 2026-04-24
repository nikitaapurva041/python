import pymysql as q
conn=q.connect(host="localhost",user="root",password="",database="manager")
mycursor=conn.cursor()
print("{:<12}{:<15}{:<20} ".format("ID","Name","Manager id"))
try:
    query = """SELECT e.id AS employee_id,e.name AS employee_name,m.name AS manager_name
                FROM manager e INNER JOIN manager m ON e.manager_id = m.id"""
    mycursor.execute(query)
    data=mycursor.fetchall()
    for a in data:
        print("{:<12}{:<15}{:<20} ".format(a[0],a[1],a[2]))
except Exception as e:
    print("Error in data:",e)
