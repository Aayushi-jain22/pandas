import pandas as pd

data ={
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [50000, 60000, 70000]
}


df = pd.DataFrame(data)
avg_sal = df['salary'].mean()

print("Average salary:", avg_sal)