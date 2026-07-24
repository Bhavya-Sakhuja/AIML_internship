# # data = {
# #     "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
# #     "Marks": [25, 30, 35, 45, 50, 55, 65, 70, 80, 85]
# # }

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [25, 30, 35, 45, 50, 55, 65, 70, 80, 85]
}

# convert in dataframe 

df = pd.DataFrame(data)

# data analyze 

# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.shape)

# x , y 

x = df[['StudyHours']]
y = df['Marks']

# data -- split -- train , test 

X_train,X_test,Y_train,Y_test = train_test_split(
    x,y,
    test_size=0.2,
    random_state=45
)

# model selection 

model = LinearRegression()

model.fit(X_train,Y_train)

# testing -- provide 

y_pred = model.predict(X_test)

input_value = pd.DataFrame({
    "StudyHours" : [8]
})

prediction = model.predict(input_value)

print(prediction)