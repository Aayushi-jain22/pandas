import pandas as pd


data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df = pd.DataFrame(data)

print(df)

df.to_csv("output.csv")


#created new file output as excel 

df.to_excel("output.xlsx", index=False, engine="openpyxl")

df.to_json("output.json", index=False)
