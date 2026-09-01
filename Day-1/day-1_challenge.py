import pandas as pd


'''
# Question (do not use group by)
1. Average salary by department
2. maximum salary by department
3. Number of employees in each department
4. Employee with the highest salary in the entire company
'''


df = pd.DataFrame([
    {"id": 101, "name": "rohit", "department": "it", "salary": 40000},
    {"id": 102, "name": "amit", "department": "hr", "salary": 30000},
    {"id": 103, "name": "suresh", "department": "finance", "salary": 24000},
    {"id": 104, "name": "neha", "department": "it", "salary": 55000},
    {"id": 105, "name": "priya", "department": "hr", "salary": 45000},
])

print(df)

# Average salary
average_salary=df["salary"].mean()
print("\naverage_salary")
print(average_salary)

print()
# Maximum Salary
Max_salary=df["salary"].max()
print("\nMax_Salary")
print(Max_salary)

print()
# no of employee in each department
nos_of_employee=df["department"].value_counts()
print("\nNos_of_Employee")
print(nos_of_employee)

print()
# highest salary per department
df_sorted=df.sort_values(["department", "salary"], ascending=[True, False])
highest_salary_per_dept=df_sorted.drop_duplicates(subset=["department"], keep="first")
print("\nhighest salary per dept")
print(highest_salary_per_dept)