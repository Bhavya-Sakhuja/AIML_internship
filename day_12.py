import pandas as pd 

df = pd.read_csv('drinks.csv')

# single column 

# print(df['country']) -- series 

# print(df[['country','continent']]) dataframes 

# df['result'] = "approved" add new column

# print(df.head())

# rename 

# df.rename(columns = {
#     "spirit_servings" : "spirit"
# },inplace=True)

# drop tbable axis = 0 / 1

# df.drop('spirit_servings',axis=1,inplace=True)

# print(df.head())

# data clean 

# print(df['continent'].unique())

# count of unique value 

# print(df['continent'].nunique())

# print(df['continent'].value_counts())

# numeric value  -- sort (ascending,descending)

# print(df['beer_servings'].sort_values(ascending=False))

# mean,median,sum,mode,max,min

# print(df['beer_servings'].median())
# print(df['beer_servings'].mean())
# print(df['beer_servings'].mode())
# print(df['beer_servings'].min())
# print(df['beer_servings'].max())
# print(df['beer_servings'].sum())

# print(df.isnull())

# print(df.isnull().sum())

# df.fillna("Africa",inplace=True)

# print(df.isnull().sum())

# df['beer_servings'].fillna(
#     df['beer_servings'].mean(),
#     inplace=True
# )

# dropna

# df.dropna(
#     subset = ['beer_servings'],
#     inplace=True
# )

# print(df.drop_duplicates())

# filtering 

# logical operators -- and or 

# print(df[(df['beer_servings']>5) & (df['beer_servings']<10)])

# group by 

# print(df.groupby('continent')['beer_servings'].mean())4

# apply

df['beer_servings'] = df['beer_servings'].apply(lambda x:x+5)

print(df['beer_servings'])

# df.to_csv('drinks_1.csv',index=True)