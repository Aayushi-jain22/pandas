import pandas as pd

data= {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "salary": [50000, 60000, 70000, 80000],
    "performance": ["A", "B", "C", "D"]

}


df = pd.DataFrame(data)

print("Removing some columns from the DataFrame:")
df.drop(columns= ["performance"], inplace=True)  # Remove 'performance' and 'salary' columns

print(df)