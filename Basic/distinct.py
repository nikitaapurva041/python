import pymysql as guj

conn = guj.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

mycursor = conn.cursor()
print(" {:<15}".format("Class"))
print("-" * 25)
try:
    sql = """
    SELECT DISTINCT (st_class)
    FROM student
    """
    
    mycursor.execute(sql)
    data = mycursor.fetchall()

    for row in data:
        print(" {:<15}".format(row[0]))

except Exception as e:
    print("Error:", e)

conn.close()
