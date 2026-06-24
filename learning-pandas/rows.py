import pandas as pd

df = pd.read_json("Sample_Data.json")

print(df.head(10)) 
# print(df.head()) #By default 5 rows from first


print(df.tail(10))
# print(df.tail()) #By deafukt 5 rows from last