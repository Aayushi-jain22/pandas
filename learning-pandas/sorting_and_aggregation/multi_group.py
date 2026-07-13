import pandas as pd

data = {
    "Employee": ["Aayu", "Riya", "Shrey", "Anurag", "Bharat"],
    "Department": ["IT", "HR", "IT", "HR", "Sales"],
    "Salary": [50000, 40000, 60000, 45000, 30000]
}

df = pd.DataFrame(data)

result = df.groupby("Department")["Salary"].sum()

print(result)