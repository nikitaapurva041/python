import pymysql as pet
# Connect to the database
conn=pet.connect(host="localhost",user="root",password="",database="company")
mycursor=conn.cursor()

# STEP 1: Entering the data for department

try:
    ins="INSERT INTO department(dept_id,dept_name,location) values(%s,%s,%s)"
    d=[("1","Accounts","Ahemdabad"),("2","KAM","Surat"),("3","Support","Varodra")]

# STEP 2: Entering the data for employee

    i="INSERT INTO employee(emp_id,emp_name,salary,dept_id) values(%s,%s,%s,%s)"
    n=[("101","Nisha","20,000","1"),("102","Niraj","30,000","2"),("103","Nazia","40,000","3")]

# Execute the first table creation

    mycursor.executemany(ins,d)
    
# Execute the second table creation
    mycursor.executemany(i,n)
    conn.commit();
    print("Data is inserted")
except Exception as e:
  print("Error in data insert")