import pandas as pd

data = {
    "name": ["Bob", "Alice", "Charlie", "David"],
    "age": [30, 25, 35, 40],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"],
    "salary": [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)


# df.sort_values(by="age", ascending=True, inplace=True)
# print("DataFrame sorted by age in ascending order:",df)    


####For multiple columns

df.sort_values(by=["age", "salary"], ascending=[True, True], inplace=True)
print("DataFrame sorted by age and salary in ascending order:",df)    