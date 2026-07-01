import pandas as pd

data = {
    "name": ["Alice", None, "Charlie", "David"],
    "age": [25, 30, 35, 40],        
    "salary": [50000, 60000, 70000, 80000],
    "performance": ["A", "B", "C", "D"]
}

df = pd.DataFrame(data)

removed_missing= df.dropna(axis=0, inplace=False)  # Remove rows with missing values (axis=0)
print("DataFrame after removing rows with missing values:",
 removed_missing)

