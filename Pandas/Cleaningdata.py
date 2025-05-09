
#! Pandas Cleaning Data
'''
Data cleaning means fixing bad data in your data set.
Bad data could be:
1. Empty cells
2. Data in wrong format
3. Wrong data
4. Duplicates

The data set contains some empty cells ("Date" in row 22, and "Calories" in row 18 and 28).

The data set contains wrong format ("Date" in row 26).

The data set contains wrong data ("Duration" in row 7).

The data set contains duplicates (row 11 and 12).
'''

#! Empty Cells - They can give wrong result when you analyze it.
#One way to deal with empty cells is to remove rows that contains empty cells.

import pandas as pd
import os

current_dir = os.path.dirname(__file__)  # gets current file's directory
file_path = os.path.join(current_dir, "Baddataset.csv")

df = pd.read_csv(file_path)
new_df = df.dropna()
print(new_df.to_string())

#! Note : Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
#If you want to change the original DataFrame, use the inplace = True argument:

df.dropna(inplace=True)
print(df.to_string())

#Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.


#! Replace Empty Values
#Another way of dealing with empty cells is to insert a new value instead.
#This way you do not have to delete entire rows just because of some empty cells.
#The fillna() method allows us to replace empty cells with a value:

df.fillna(130, inplace=True)
print(df.to_string())
##Notice in the result: empty cells got the value 130 (in row 18, 22 and 28).

#! Replace only for specified Columns
#The example above replaces all empty cells in the whole Data Frame.
#To only replace empty values for one column, specify the column name for the DataFrame:

df.fillna({"Calories": 130}, inplace=True)
print(df.to_string())
#This operation inserts 130 in empty cells in the "Calories" column (row 18 and 28).


#! Replace Using Mean, Median, or Mode
'''
A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:
'''

x = df["Calories"].mean()

df.fillna({"Calories": x}, inplace=True)

print(df.to_string())

#As you can see in row 18 and 28, the empty values from "Calories" was replaced with the mean: 304.68

x = df["Calories"].median()

df.fillna({"Calories": x}, inplace=True)

print(df.to_string())

#As you can see in row 18 and 28, the empty values from "Calories" was replaced with the median: 291.2

x = df["Calories"].mode()[0]

df.fillna({"Calories": x}, inplace=True)

print(df.to_string())

#As you can see in row 18 and 28, the empty value from "Calories" was replaced with the mode: 300.0