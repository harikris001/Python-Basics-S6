import pandas as pd
import numpy as np

df = pd.read_csv("employee.csv")

# first 7 records from csv
print(df.head(7))

# print all employee names in alphabetical order
print(df['name'].sort_values(ascending=True))

# name of employee with highest salary
indexvalue = df['salary'].idxmax
print(df.loc[indexvalue,'name'])

# male employees
df1 = df['gender']=='male'
print(df1['name'])

# teams of employees
print(df['teams'].unique())