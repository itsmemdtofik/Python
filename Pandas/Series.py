# ! Pandas Series in Python

"""
#? What is a Series?
A pandas series is like a column in a table.
It is one-dimensional array holding data of any type.
"""

# ! Creating a series from List
import pandas as pd

series = [1, 2, 3, 4, 5]
var = pd.Series(series)
print("The Pandas Series is : \n")
print(var)

# ! What is Label

'''
If nothing else is specified, the values are labeled with their index number. 
First value has index 0, second value has index 1 etc.
This label can be used to access a specified value.
'''
print(f"Return the first values of the series: {var[0]}")

# !Create a labels
# *With index argument, you can name your own labels

labels = pd.Series(series, index=['first', 'second', 'third', 'fourth', 'five'])
print("Now my own index is : ")
print(labels)

print(f"Return the value of fourth is: {labels['fourth']}")

# ! Key/Value Objects as Series
# *You can also  use a key/value objects, like a dictionary, when creating a Series.

details = {
    'Name': 'Mohammad Tofik',
    "Age": 26,
    "Address": "Bengaluru",
    "Company": "Sandisk"
}

details = pd.Series(details)
print("Key value objects as a series : ")
print(details)
