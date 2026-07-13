import pandas as pd

data = {
    'name': ['Aayu', 'Riya', 'Shrey', 'samayak', 'bharat', 'anurag','aanchal'],
    'age': [25, 30, 35, 40, 28, 32, 29],
    'salary': [50000, 60000, 70000, 80000, 55000, 65000, 58000]
}

df = pd.DataFrame(data)

group = df.groupby('age').sum()
print(group)