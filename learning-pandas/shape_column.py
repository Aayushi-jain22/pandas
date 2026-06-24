import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York","Los Angeles", "Chicago", "Houston"],
    "Performance": [90, 85, 95, 80]
}


df = pd.DataFrame(data)
print(df.shape)
print(f"Number of rows columns: {df.shape}")



print(f'Number of columns: {df.columns}')
