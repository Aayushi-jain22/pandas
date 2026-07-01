import pandas as pd


data= {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, None,35, 40],
    "salary": [50000, 60000, None, 80000],
    "performance": ["A", "B", "C", "D"]

}

df = pd.DataFrame(data)

print(df.isnull())  # Check for missing values in the DataFrame Return True if any missing

counts = df.isnull().sum()  # Count the number of missing values in each column
print(counts)
