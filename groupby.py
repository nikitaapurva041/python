import pymysql as guj

conn = guj.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

mycursor = conn.cursor()

print("{:<10} {:<15}".format("Class", "Total Students"))
print("-" * 25)

try:
    sql = """
    SELECT st_class, COUNT(*) 
    FROM student
    GROUP BY st_class
    ORDER BY st_class
    """
    
    mycursor.execute(sql)
    data = mycursor.fetchall()

    for row in data:
        print("{:<10} {:<15}".format(row[0], row[1]))

except Exception as e:
    print("Error:", e)

conn.close()
