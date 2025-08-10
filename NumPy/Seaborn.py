"""
Seaborn in Python:
Visualize Distributions With Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.
"""
import matplotlib.pyplot as plt
import seaborn

plot = seaborn.displot([0, 1, 2, 3, 4, 5])
plt.show()

# Plotting a Dis plot without a histogram

plot1 = seaborn.displot([0, 1, 2, 3, 4, 5], kind="kde")
plt.show()
