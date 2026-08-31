import  pandas as pd


def employee_transform(df):

    df=df.copy()

    # 1 Clean employee name
    df["name"]=df["name"].str.strip().str.title()
    print("\nProper Name")
    print(df)
    print()

    # 2 Normalize department
    df["department"]=df["department"].str.strip().str.lower()
    print("\ndept lower case")
    print(df)
    print()

    # 3 Check missing salary
    missing_salary=df["salary"].isnull().sum()
    if missing_salary > 0:
        print(f"Warning: {missing_salary} employee(s) have missing salary")

    # Calculate Average salary
    print()
    average_salary=df["salary"].mean()
    print("\nAvarage Salary")
    print(average_salary)

    # valid and invalid employee
    valid_records=df["salary"].notna()
    print()
    valid_df=df[valid_records]
    invalid_df=df[~valid_records]

    print("\nValid employees:")
    print(valid_df)

    print("\nInvalid employees:")
    print(invalid_df)

    return df, valid_df, invalid_df


employees = [
    {"id": 101, "name": "rohit", "department": "it", "salary": 40000},
    {"id": 102, "name": "amit", "department": "hr", "salary": None},
    {"id": 103, "name": "suresh", "department": "finance", "salary": 24000},
    {"id": 104, "name": "neha", "department": "IT", "salary": 55000},
]


df = pd.DataFrame(employees)
# df.head()

df, valid_df, invalid_df=employee_transform(df)
print()

# salary > 40000
high_salary=df["salary"] > 40000
employee_salary=df[high_salary]
print("\nEmployees with salary > 40000:")
print(employee_salary)
