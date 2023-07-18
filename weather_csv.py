import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv()

x1 = df['date']
y1 = df['temperature']

# line polt
plt.plot(x1,y1)

x2 = df['date']
y2 = df['humidity']

# scatter plot
plt.scatter(x2,y2)

plt.show()