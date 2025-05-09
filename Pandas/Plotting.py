
#! Pandas - Plotting
'''
Pandas uses the plot() method to create diagrams.
We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.
Read more about Matplotlib in our Matplotlib Tutorial.
'''
import pandas as pd
import matplotlib.pyplot as mat
import os
import sys

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "Csvdata.csv")
df = pd.read_csv(file_path)

df.plot()
mat.show()

#Two lines to make our compiler able to draw
mat.savefig("plot.png")