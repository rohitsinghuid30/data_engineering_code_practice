import  pandas as pd


def employee_transform(df):

    df=df.copy()

    # employee name proper case or clean name
    df["name"]=df["name"].str.strip().str.title()
    print("\nProper Name")
    print(df)
    print()

    # department name lowercase
    df["department"]=df["department"].str.strip().str.lower()
    print("\ndept lower case")
    print(df)
    print()

    # employee missing salary
    missing_salary=df["salary"].isnull().sum()
    if missing_salary > 0:
        print(f"Warning: {missing_salary} employee(s) have missing salary")

    # Average salary for valid employee
    print()
    valid_emp_df=df["salary"].notna()
    print(valid_emp_df/len(valid_emp_df))

    # valid and invalid employee
    valid_records=df["salary"].notna()
    print()
    valid_df=df[valid_records]
    Invalid_df=df[~valid_records]
    print("Valid_df")
    print(valid_df)
    print()
    print("InValid_df")
    print(Invalid_df)

    return df


employees = [
    {"id": 101, "name": "rohit", "department": "it", "salary": 40000},
    {"id": 102, "name": "amit", "department": "hr", "salary": None},
    {"id": 103, "name": "suresh", "department": "finance", "salary": 24000},
    {"id": 104, "name": "neha", "department": "IT", "salary": 55000},
]


df=pd.DataFrame(employees)
# df.head()

df=employee_transform(df)
print()

# salary > 40000
salary=df["salary"] > 40000
employee_salary=df[salary]
print(employee_salary)
