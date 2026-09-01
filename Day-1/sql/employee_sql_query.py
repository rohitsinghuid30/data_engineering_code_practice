import pandas as pd
import sqlite3


# create sqlite db
conn=sqlite3.connect("employees")
cursor=conn.cursor()

# get sample data frame
employees = [
    {"id": 101, "name": "rohit", "department": "it", "salary": 40000},
    {"id": 102, "name": "amit", "department": "hr", "salary": None},
    {"id": 103, "name": "suresh", "department": "finance", "salary": 24000},
    {"id": 104, "name": "neha", "department": "IT", "salary": 55000},
]


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