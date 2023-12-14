import pandas as pd
import matplotlib.pyplot as plt
import lasio

las = lasio.read("15-9-19_SR_COMP.LAS")

df = las.df()
df.describe()

df.head(10)

# Set up the scatter plot
plt.scatter(x='NEU', y='DEN', data=df)

plt.show()