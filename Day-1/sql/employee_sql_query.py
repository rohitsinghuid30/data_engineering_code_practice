import pandas as pd
import sqlite3


#===========================================
# Employee SQL Practice - Day 1
#===========================================


"""
Write SQL to:

Find employees whose salary is greater than 40000.
Find the average salary by department.
Find the highest-paid employee in each department.
Find employees whose salary is NULL.
Rank employees by salary within each department.
"""

# create sqlite db
conn=sqlite3.connect("employees")
cursor=conn.cursor()

# get sample data frame
employees = [
    {"id": 101, "name": "rohit", "department": "it", "salary": 40000},
    {"id": 102, "name": "amit", "department": "hr", "salary": None},
    {"id": 103, "name": "suresh", "department": "finance", "salary": 24000},
    {"id": 104, "name": "neha", "department": "it", "salary": 55000},
]

# Read
df = pd.DataFrame(employees)

print(df)


# add data into sqlite db tables
# df.to_sql("employees", con=conn, if_exists="append", index=False)
# print("data Inserted")


# query-1 (salary > 40000)
query1=cursor.execute("select * from employees where salary > 40000;")
result1=query1.fetchall()
print()
print("\nsalary > 40000")
print(result1)


# query-2 (Average Salary by department)
query2=cursor.execute("select department, AVG(salary) from employees group by department")
result2=query2.fetchall()
print()
print("\nAverage Salary by department")
print(result2)


# query-3 (Highest Paid employee in each department)
query3=cursor.execute(
    """
    select department, name, salary FROM (select department, name, salary, ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) as rn FROM employees) t
    where rn=1;
    """
)

result3=query3.fetchall()
print()
print("\nHighest paid employee in each dept")
print(result3)


# query-4 (Employee whose salary is NULL)
query4=cursor.execute("select * from employees where salary is NULL")
result4=query4.fetchall()
print()
print("\nEmployee Salary is NULL")
print(result4)