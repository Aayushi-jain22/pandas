import pandas as pd

data ={
    "Time": [1, 2, None, 4, 5],
    "Value": [10, 20, 30, None, 50]
}

 # Interpolate missing values in the 'Value' column
df = pd.DataFrame(data)
df["Value"] = df["Value"].interpolate(method='linear') 
print(df)
