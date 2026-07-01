import pandas as pd

data = {
    "name": ["Alice", None, "Charlie", "David"],
    "age": [25,None, 35, 40],        
    "salary": [50000, 60000, 70000, 80000],
    "performance": ["A", "B", "C", "D"]
}

df = pd.DataFrame(data)

# df.dropna(inplace=True)  # Remove rows and columns with missing values (axis=0)
# print("DataFrame after removing rows with missing values:")
# print(df)

df.fillna(0, inplace=True)  # Fill missing values with 0
print("DataFrame after filling missing values:")
print(df)


##Fill Calculated Values:


 calculated = df['age'].fillna(df['age'].mean(), inplace=True)  # Fill missing values in 'age' column with the mean of the column
print("DataFrame after filling missing values in 'age' column with mean:")