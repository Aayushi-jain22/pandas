import pandas as pd


# df = pd.read_csv("financial-data.csv")
# print(df)


df = pd.read_excel("SampleSuperstore.xlsx", engine="openpyxl")
print(df)


# df = pd.read_json("sample_Data.json")
# print(df)