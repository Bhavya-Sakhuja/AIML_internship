# data = {
#     "CGPA": [6.5, 7.2, 8.1, 6.8, 8.5, 7.8, 6.2, 9.0, 7.5, 8.3],
#     "Internship": [0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
#     "Projects": [1, 2, 3, 1, 4, 3, 0, 4, 2, 3],
#     "Placement": [0, 1, 1, 0, 1, 1, 0, 1, 0, 1]
# }

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = {
    "CGPA": [6.5, 7.2, 8.1, 6.8, 8.5, 7.8, 6.2, 9.0, 7.5, 8.3],
    "Internship": [0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    "Projects": [1, 2, 3, 1, 4, 3, 0, 4, 2, 3],
    "Placement": [0, 1, 1, 0, 1, 1, 0, 1, 0, 1]
}

# convert teh data in dataframe using pandas 

df = pd.DataFrame(data)

# data analyze head , tail , info , columns , describe 

# print(df.head())

# print(df.tail())

# print(df.info())

# input and output values x,y 

x = df[['CGPA','Internship','Projects']]
y = df['Placement']

# split test training 

X_train,X_test,Y_train,Y_test = train_test_split(
    x,y,
    test_size=0.2,
    random_state= 42
)

# model selection 

model = LogisticRegression()

model.fit(X_train,Y_train)

# testing data -- predictions 

Y_predict = model.predict(X_test)

# input 

input_values = pd.DataFrame(
    [[9,1,4]],
    columns=['CGPA','Internship','Projects']   
)

prediction = model.predict(input_values)

# print(prediction)

if prediction[0] == 1:
    print("Yes")
else:
    print("No")