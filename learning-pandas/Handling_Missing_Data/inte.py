import pandas as pd

data = {
    "name": ["Alice", None, "Charlie", "David"],
    "age": [25,None, 35, 40],        
    "salary": [50000, 60000, 70000, 80000],
    "performance": ["A", "B", "C", "D"]
}

df = pd.DataFrame(data)
# Interpolate missing values in the DataFrame

df.interpolate(method = 'linear',axis= 0, inplace=True)
print(df)


# Pandas tries to interpolate every column, 
# including "name" and "performance", 
# but linear interpolation only works on numeric data.