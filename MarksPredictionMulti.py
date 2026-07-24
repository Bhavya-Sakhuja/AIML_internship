
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "StudyHours": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Attendance": [60, 65, 70, 75, 78, 80, 85, 88, 90, 95],
    "PreviousMarks": [45, 50, 55, 60, 65, 68, 72, 75, 80, 85],
    "Assignments": [3, 4, 5, 6, 6, 7, 8, 8, 9, 10],
    "Marks": [40, 45, 52, 58, 65, 70, 76, 82, 88, 94]
}


# convert in dataframe 

df = pd.DataFrame(data)

# data analyze 

# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.shape)

# x , y 

x = df[['StudyHours','Attendance','PreviousMarks','Assignments']]
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

input_value = pd.DataFrame(
    [[4,97,87,8]],
    columns=['StudyHours','Attendance','PreviousMarks','Assignments']
)

prediction = model.predict(input_value)

print(prediction)