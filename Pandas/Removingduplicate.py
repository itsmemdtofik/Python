# ! Pandas - Removing Duplicate

"""
By taking a look at our test data set, we can assume that row 11 and 12 are duplicates.

To discover duplicates, we can use the duplicated() method.

The duplicated() method returns a Boolean values for each row:
"""

import pandas as pd
import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "Duplicatesdata.csv")
df = pd.read_csv(file_path)

print("Before removing the duplicates the data frame is : ")
print(df.to_string())

print("")
print("Displaying every row that is a duplicate True, Otherwise False:")
print(df.duplicated())
print("")

# ! Removing the duplicate now
df.drop_duplicates(inplace=True)
print("After removing the duplicate:")
print(df.to_string())

# Remember: The (inplace = True) will make sure that the method does NOT return
# a new DataFrame, but it will remove all duplicates from the original DataFrame.
