import pymysql as pet

# Connect to the database
conn = pet.connect(host="localhost", user="root", password="", database="company")
mycursor = conn.cursor()

# STEP 1: Fixed Department Table (Added closing parenthesis at the end)
database = """
CREATE TABLE IF NOT EXISTS department (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(50),
    location VARCHAR(50)
)
"""

# STEP 2: Fixed Employee Table (Added closing parenthesis at the end)
database1 = """
CREATE TABLE IF NOT EXISTS employee (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(50),
    salary DECIMAL(10,2),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES department(dept_id)
)
"""
try:
    # Execute the first table creation
    mycursor.execute(database)
    
    # Execute the second table creation
    mycursor.execute(database1)
    
    print("Tables created successfully!")
    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    conn.close()