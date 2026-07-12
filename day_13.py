import pandas as pd 

df = pd.read_csv('surat_uncleaned.csv')

# display first five rows 
# print(df.head())

# display last five rows
# print(df.tail())

# find the shape of dataset 
# print(df.shape)

# find column names
# print(df.columns)

# check the datatype of every column 
# print(df.dtypes)

# find basic info about dataset
# print(df.info())

# find statical summary 
# print(df.describe())

# check any null value exists 
# print(df.info())

# count of null values 
# print(df.isnull().sum())

# find percentage of every column (contain null value)

# percentage = (df.isnull().sum() / len(df)) * 100 

# # print(percentage)

# # find the column that contain highest null value 

# max_value = percentage.max()
# print(max_value)

# remove rows that contain missing values 

# print(df.shape)

# df = df.dropna()

# print(df.shape)

# remove column 

# print(df.columns)

# percentage = (df.isnull().sum() / len(df)) * 100 

# morethanfifty = percentage[percentage > 20].index

# df.drop(
#     columns=morethanfifty,
#     inplace=True
# )


# print(df.columns)


# statuscolumn null values fill with mode 

print(df['status'].isnull().sum())

modeevalue = df['status'].mode()[0]

df['status'] = df['status'].fillna(
   value = modeevalue
)

print(df['status'].isnull().sum())




