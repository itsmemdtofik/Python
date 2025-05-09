
#! Data Frame in Pandas
'''
#! What is dataframe?
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
Series is like a column, a DataFrame is the whole table.
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
'''
#* Creating the data frame here
import pandas as pd
data = {
    'Calories':[420, 380, 390],
    'Duration':[50, 40, 45]
}
#Load data into the DataFrame object
df = pd.DataFrame(data)
print("DataFrame are:")
print(df)

#! Locate Row
'''
As you can see from the result above, the DataFrame is like a table with rows and columns.
Pandas use the loc attribute to return one or more specified row(s)
'''
print(f"Return the value of Rows Zero is: ")
print(df.loc[0])

print("Return row 0 and 1 is:")
print(df.loc[[0, 1]])

#!You can make your own index name
data = pd.DataFrame(data, index=['day1','day2','day3'])
print("New Index are :")
print(data)

#! Locate named index
print("Locate name index is: ")
print(data.loc['day2'])