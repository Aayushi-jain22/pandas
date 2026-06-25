import pandas as pd

data= {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "salary": [50000, 60000, 70000, 80000],
    "performance": ["A", "B", "C", "D"]

}

df = pd.DataFrame(data)

df.loc[0, "age"] = 26  # Update age for Alice
print("Updated age for Alice:")
print(df)