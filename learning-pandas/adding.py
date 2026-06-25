import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],   
    "age": [25, 30, 35, 40],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)

print(df)

df["Bonus"] = df["age"] * 1000  # Adding a new column 'Bonus' based on 'age'
print("bonus column added")
print(df)

#insert method

df.insert(1, "Country", ["USA", "Canada", "UK", "Australia"])  # Inserting a new column 'Country' at index 2
print("Country column inserted")
print(df)