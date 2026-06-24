import pandas as pd


# df = pd.read_json("Sample_Data.json")
# print(df.info())

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df = pd.DataFrame(data)

print(df.info())