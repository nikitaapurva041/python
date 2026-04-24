import pymysql as guj

conn = guj.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

mycursor = conn.cursor()

print("{:<20}".format("Total Sum of Classes"))
print("-" * 25)

try:
    sql = "SELECT SUM(st_class) FROM student"
    mycursor.execute(sql)
    data = mycursor.fetchone()

    print("{:<20}".format(data[0]))

except Exception as e:
    print("Error:", e)

conn.close()
