"""
# ! Pandas - Histogram
Use the kind argument to specify that you want a histogram:

kind = 'hist'

A histogram needs only one column.

A histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?

In the example below we will use the "Duration" column to create the histogram:
"""

import os
import sys
import matplotlib.pyplot as plt
import pandas as pd

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "Csvdata.csv")

df = pd.read_csv(file_path)
df["Duration"].plot(kind='hist')

plt.show()
