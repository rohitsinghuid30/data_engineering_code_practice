import pandas as pd
import sqlite3

conn=sqlite3.connect("employees")

cursor=conn.cursor()

# create table employees 2
'''
cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees_2 (
                id INT,
                name VARCHAR(50),
                department VARCHAR(50),
                salary NUMERIC(10,2)
            );
        """)

print("Table created")

# Add employees
cursor.execute("""
        INSERT INTO employees_2 (id, name, department, salary)
        VALUES
        (101, 'rohit', 'it', 40000),
        (102, 'amit', 'hr', 30000),
        (103, 'suresh', 'finance', 24000),
        (104, 'neha', 'it', 55000),
        (105, 'priya', 'hr', 45000);
""")
print()
print("Employee Inserted")

conn.close()

'''

'''
Questions 
1. Find employees whose salary > 40000
2. Find average salary by department
3. Find number of employees in each department
4. Find highest-paid employee in each department
5. Bonus -⭐Rank employees by salary within each department
'''


# query 1 ~ salary > 40000
query1=cursor.execute("Select * from employees_2 where salary > 40000;")
result1=query1.fetchall()
print("") 
print("\nSalary > 40000")
print(result1)

# query 2 ~ AVG salary by department
query2=cursor.execute("Select department, AVG(salary) from employees_2 group by department;")
result2=query2.fetchall()
print("") 
print("\nAGG Salary by department")
print(result2)