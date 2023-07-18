import pandas as pd
import numpy as np

df = pd.read_csv("diamond.csv")

# number of rows and columns
print("Number of columns:",df.shape[1])
print("Number of Rows:",df.shape[0])

# first 5 rows
df.head(5)
