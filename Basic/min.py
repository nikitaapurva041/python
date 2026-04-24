import pymysql as guj 
conn=guj.connect(host="localhost",user="root",password="",database="college") 
mycursor=conn.cursor() 
print("{:<25}".format("Lowest Qualification")) 
try: 
    # for MAX 
    #sql="SELECT MAX(st_class) from student" 
    # for MIN
    sql1="SELECT MIN(st_class) from student" 
    mycursor.execute(sql1) 
    data=mycursor.fetchall() 
    for a in data: 
        print("{:<25}".format(a[0])) 
except Exception as e: 
    print(f"Error in the code: {e}") 
    conn.close()
