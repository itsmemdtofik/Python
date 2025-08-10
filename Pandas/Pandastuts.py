
#! Pandas in Python

'''
#! What is Pandas?
Pandas is a python library which is used for working with data sets.
It has fucntions for analyzing, cleaning, exploring, and manipulating data.
The name pandas has reference to both #!Panel Data and Python Data Analysis.
It was created by Wes McKinney in 2008.
'''
import pandas as pd
dataset = {
    'cars':['BMW','Volvo','Ford'],
    'Passings':[3,7,2]
}

var1 = pd.DataFrame(dataset)
print(var1)

#!Checking the pandas version
print("Pandas version is: ", pd.__version__)
