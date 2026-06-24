import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)

print(df[df['age'] > 30])  # Filter rows where age is greater than 30

# print(df[(df['city'] == "New York") & (df['age'] > 30)])  
# Filter rows where city is "New York" and age is greater than 30

name = df["name"]
print(name)



#OR condition
print(df[(df['city'] == "New York") |(df['age'] > 30)])  