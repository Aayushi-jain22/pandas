import pandas as pd

data = {
    "name": ["Bob", "Alice", "Charlie", "David"],
    "age": [30, 25, 35, 40],
}
df = pd.DataFrame(data)


df.sort_values(by="age", ascending=True, inplace=True)
print("DataFrame sorted by age in ascending order:",df)    