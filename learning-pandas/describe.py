import pandas as pd

data ={
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "city": ["New York","Los Angeles", "Chicago", "Houston"],
    "Performance": [90, 85, 95, 80]
}

df = pd.DataFrame(data)

print(df.describe())