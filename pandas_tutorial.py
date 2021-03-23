# tutorial for working with excel files in python

import pandas as pd
import numpy as np

excel_file = "Pandas_Workbook.xlsx" # create a variable to hold a reference to our excel file
df = pd.read_excel(excel_file) # create a dataframe variable for the excel file
# print(df)
# print(df.head(5)) # Using the head function we can view a certain amount depending on what we pass it
# we can also pull out index, columns and datatypes using the following functions
# print(df.index)
# print(df.columns)
# print(df.dtypes)

# we can also pull out specific columns based on column names using square brackets
# print(df['Name'])

# a series contains individual scalars, a datafram contains series of things so we can access each of these using square brackets with some value
names = df['Name']
# print(names[5]) # this yields an individual name in this case name number 6 at index 5

# label based access
# print(df.at[0, "Name"])

df2 = pd.read_excel(excel_file, index_col = "Name")
# print(df2)
# print(df2.at["Beth", "Occupation"])
# integer based access in this case the values in the square brackets are used based on multidimensional array location
# print(df2.iat[1, 1])
# we can select or deselect a range of values in this case using the loc function
# we can also use a logical value to select info as well such as in the case of the Identifier
# print(df.loc[[0,2,4,6], "Age" : "Occupation"])
# print(df.loc[df["Identifier"] == True])
print(df.iloc[0 : 5 : 1, [0, 1]])
