import pymysql as guj

conn = guj.connect(host="localhost", user="root", password="", database="college")
mycursor = conn.cursor()

print("{:<17} {:<12} {:<20} {:<20}".format("st_id", "st_name", "st_class", "st_email"))

try:
    search_term = input("Search for a Student Name (or part of it):- ")
    search_term1 = input("Search for a Student Class (or part of it):- ")
    
    # STEP 1: Prepare the filter with wildcards
    # This will search for the term anywhere in the name
    filter_value = f"%{search_term}%"
    filter_class=f"%{search_term1}%"
    
    # STEP 2: Fixed SQL syntax (added LIKE %s for the second condition)
    #sql = "SELECT * FROM student WHERE st_name LIKE %s AND st_class LIKE %s"
    # STEP 2: Filter using OR condition
    sql = "SELECT * FROM student WHERE st_name LIKE %s OR st_class LIKE %s"
        
   # STEP 3: Pass BOTH variables inside ONE tuple
    mycursor.execute(sql, (filter_value,filter_class)) 
    
    data = mycursor.fetchall()
    
    if data:
        for a in data:
            print("{:<17} {:<12} {:<20} {:<20}".format(a[0], a[1], a[2], a[3]))
    else:
         print(f"No records matching '{search_term}'and Class: '{search_term1}' found.")
except Exception as e:
    print(f"Error in the code: {e}")
finally:
 conn.close()
