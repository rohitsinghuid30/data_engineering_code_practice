import pandas as pd
import sqlite3
from sqlalchemy import create_engine


# Connection Strings
engine=create_engine("sqlite:///employees")
# conn=sqlite3.connect("employees")
# cursor=conn.cursor()


df=pd.read_sql_query("select * from employees_2", engine)

print(df)
print()

# query-1 ROW_Number()
query="select id, name, department, salary, ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as 'rn' FROM employees_2"
df2=pd.read_sql(query, engine)
print("\nROW_NUMBER Result")
print(df2)


# query-2 RANK()
query2="select id, name, department, salary, RANK() OVER (PARTITION BY department ORDER BY salary DESC) as 'rank' FROM employees_2"
df3=pd.read_sql_query(query2, engine)
print("\nRANK Result")
print(df3)


# query-3 DENSE_RANK()
query3="select id, name, department, salary, DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) as 'dens_rank' FROM employees_2"
df4=pd.read_sql(query3, engine)
print("\nDense_Rank Result")
print(df4)

# find duplicates in data frame
df5=df4[df4.duplicated()]
print(df5)

# new_employee = pd.DataFrame([
#     {
#         "id": 106,
#         "name": "karan",
#         "department": "it",
#         "salary": 55000
#     }
# ])

# new_employee.to_sql("employees_2", con=engine, if_exists='append', index=False)
# print(f"{new_employee} has been added.")