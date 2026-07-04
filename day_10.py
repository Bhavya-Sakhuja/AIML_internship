import pandas as pd

# series dataframes 

s1 = pd.Series([1,2,3,4,5],
                index = ['A','B','C','D','E']) #1D

print(s1)

print(s1['B'])

# Two dimensions means row and column

# dataframe = row + columsn (structured fromat = table)                                

# name rollno age 
# bahvay 123  17 
# manu 234  17 
# xyz 498 19

# record = {
#     "Name" : ["Aman","Priya","Raj"],
#     "Role" : ['Software developer','data scientist','hr'],
#     "Age" : [19,23,45]
# }

# print(record)

# df = pd.DataFrame(record)

# print(df)