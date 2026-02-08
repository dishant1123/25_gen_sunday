# csv module  : 

# reading  from  csv file  : 

import csv 

"""with  open('student.csv','r') as  f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        print(i)
"""        
# reading from  csv as dictionary  :

"""with open('student.csv','r') as  f:
    csv_dict = csv.DictReader(f)
    
    for i in csv_dict :
        print(i)
"""

# writing to  csv file  :

"""with open('student.csv','w') as  f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['name','age','city'])
    csv_writer.writerow(['daksh',20,'mumbai'])
    csv_writer.writerow(['taksh',21,'dubai'])
    csv_writer.writerow(['moksh',24,'chennai'])
    csv_writer.writerow(['yash',27,'delhi'])
    
"""

"""with  open("production.csv","w") as  f:
    fieldname = ["product","quantity","price"]
    
    writer = csv.DictWriter(f,fieldnames=fieldname)
    writer.writeheader()
    
    # writer.writerow({"product":"apple","quantity":10,"price":1})
    # writer.writerow({"product":"banana","quantity":5,"price":2})
    # writer.writerow({"product":"orange","quantity":7,"price":3})
    # writer.writerow({"product":"mango","quantity":12,"price":4})
    
    writer.writerows([{"product":"apple","quantity":10,"price":1},
                      {"product":"banana","quantity":5,"price":2},
                      {"product":"orange","quantity":7,"price":3},
                      {"product":"mango","quantity":12,"price":4}])
"""

# append : 

"""with  open("production.csv","a",newline="") as  f:
    writer = csv.writer(f)
    writer.writerow(["chiku",10,1])
"""

# exception  handling  : 

"""
try : 
    print
except error  :
    print
"""

# ex :1 

"""try : 
    a=int(input("enter the number  : "))
    b=int(input("enter the number  : "))
    result = a/b 
    print(result)
except ZeroDivisionError: 
    print("you can't divide by zero")
except ValueError :
    print("enter a valid number")
""" 

# class : 

"""class invalidmarks(Exception):
    pass 

marks = int(input("enter the marks  : "))

if marks < 0 or marks >100 :
    raise invalidmarks("enter a valid marks")

print(marks)

"""

# file   :

"""
try :
    with  open("sd.txt","r") as  f:
        context = f.read()
        print(context)
except FileNotFoundError :
        print("file not found")
"""

# connection  :  python  to SQL  

# pip install mysql-connector-python   / pgadmin == > pip install psycopg2

import mysql.connector 

conn = mysql.connector.connect(
    user ="root",
    host ="localhost",  # or "127.0.0.1" 
    port = 3306, 
    password ="root",
    database = "25_sunday_python"
)

cursor = conn.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS 25_sunday_python")
# print("database created")

'''cursor.execute("""
               CREATE TABLE IF NOT EXISTS student(
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   name VARCHAR(50),
                   age INT,
                   department VARCHAR(50)
               )
               
               """)
'''
# print("table created")

cursor.execute("INSERT INTO student(name,age,department)VALUES ('rohit',20,'IT')")
cursor.execute("INSERT INTO student(name,age,department)VALUES ('dev',21,'Finance')")
cursor.execute("INSERT INTO student(name,age,department)VALUES ('Daksh',21,'Research')")
cursor.execute("INSERT INTO student(name,age,department)VALUES ('Krithik',22,'AI-ML')")
cursor.execute("INSERT INTO student(name,age,department)VALUES ('Mohit',25,'Accounting')")
cursor.execute("INSERT INTO student(name,age,department)VALUES ('Jainam',26,'Audit')")

conn.commit()
print("data inserted")

cursor.close()
conn.close()