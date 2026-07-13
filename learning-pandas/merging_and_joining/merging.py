import pandas as pd

##1st table
employees = pd.DataFrame({
    "emp_id": [1, 2, 3, 4],
    "name": ["Aayu", "Riya", "Shrey", "Anurag"]
})

##2nd table
salaries = pd.DataFrame({
    "emp_id": [1, 2, 3],
    "salary": [50000, 60000, 70000]
})

result = pd.merge(employees, salaries, on="emp_id" , how = "inner")
print(result)