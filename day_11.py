import pandas as pd

df = pd.read_csv('drinks.csv')

# print(df)

# head 

# print(df.head(1))

# tail

# print(df.tail(3))

# print(df.columns)

# print(df.shape)

# print(df.info())

# print(df.describe())

# print(df[['beer_servings','wine_servings']])

# print(df.iloc[2:5])

# print(df[df['total_litres_of_pure_alcohol'] > 5])

df['names'] = 0

print(df)

