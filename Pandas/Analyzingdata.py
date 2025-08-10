"""
#! Pandas Analyzing DataFrame
One of the most used method for getting a quick overview of the DataFrame, is the head() method.
The head() method returns the headers and a specified number of rows, starting from the top.
"""

import pandas as pd

df = pd.read_csv("/Users/itsmemdtofik/Downloads/Python/Pandas/Csvdata.csv")
print("The head() print 10 rows of the DataFrame are:")
print(df.head(10))

# If the number of rows is not specified then it returns top 5 rows.
print(f"The top 5 rows : {df.head()}")

# ! tail() viewing the last rows of the dataframe
print(f"The last 5 rows from the ending: {df.tail()}")
print(f"Last 20 rows of the dataframe: {df.tail(20)}")

# ! Info about the data
# The DataFrames object has a method called info(),
# that gives you more information about the data set.
print("Information about the dataframe: \n")
print(df.info())
