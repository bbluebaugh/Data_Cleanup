# import excel
# clean excel data
# write back to file

import pandas as pd

excel_workbook = 'data_cleanup.xlsx'
sheet1 = pd.read_excel(excel_workbook, sheet_name = 'Sheet1')
# print(sheet1.head(10))

first_names_list = []
last_names_list = []

excel_names = sheet1['First Name, Last Name']
# print(excel_names)

# go through each row in the first name last name column
# grab each one and append it to its preffered list
for name in excel_names:
	first_name, last_name = name.split(' ', 1) # separate first name from last name using the space character
	first_names_list.append(first_name.upper())
	last_names_list.append(last_name.upper()) # we wish to make them all uppercase as well

# print(first_names_list)

# insert our newly created list as rows into our excel file
# passing the list variable as required with the 
# value of the index we wish to insert it into
# and delete the row that has them both together
sheet1.insert(0, "First Name", first_names_list)
sheet1.insert(1, "Last Name", last_names_list)
del sheet1['First Name, Last Name']

# print(sheet1.head(10))

# these could be strings or character and not numbers
# in this case we will force them to be numerics
Important_numbers = sheet1['Important Number']
pd.to_numeric(Important_numbers)

# print(Important_numbers)

Edited_Important_Number = Important_numbers * 2
sheet1['Important Number'] = Edited_Important_Number

print(sheet1.head(10))

# write back
sheet1.to_excel("output.xlsx")
