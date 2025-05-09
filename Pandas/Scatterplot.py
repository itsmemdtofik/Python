
#! Pandas - Scatter Plot
'''
Specify that you want a scatter plot with the kind argument:

kind = 'scatter'

A scatter plot needs an x- and a y-axis.

In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.

Include the x and y arguments like this:

x = 'Duration', y = 'Calories'
'''

import os
import sys
import matplotlib.pyplot as plt
import pandas as pd

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "Csvdata.csv")
df = pd.read_csv(file_path)

df.plot(kind = 'scatter', x = 'Duration', y = "Calories")
plt.show()
plt.savefig('scatter.png')