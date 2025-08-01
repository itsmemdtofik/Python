
#! Pandas Read CSV
'''
A simple way to store big data sets is to use CSV files (comma separated files).
CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
In our examples we will be using a CSV file called 'Csvdata.csv'.
'''
import pandas as pd
df = pd.read_csv('/Users/itsmemdtofik/Downloads/Python/Pandas/Csvdata.csv')
print(df.to_string())

#We used to_string() to print entire data frame.
#If we dont want to print then bydefault it print first 5 rows and last 5 rows.
print("Printing first 5 rows and last 5 rows are: ")
print(df)


#! We can check our system return how many rows and we set other wise.
print(f"Number of display row size:{pd.options.display.max_rows}")

pd.options.display.max_rows = 9999
df = pd.read_csv('/Users/itsmemdtofik/Downloads/DSA-In-Python/Pandas/Csvdata.csv')
print("After setting the custome number of rows as 9999 : ")
print(df)