import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

dict = {
    "Hours_Studied" : [1,2,3,8,5,6,7,4,10],
    "Result" : [0,0,0,1,1,1,1,0,1]
}

# convert the dict into dataframe by the use of pandas 

df = pd.DataFrame(dict)

# Analyze the data 

# head  - first 5 rows 
# print(df.head())

# tail  - last 5 rows
# print(df.tail())

# shape
# print(df.shape)

# info 
# print(df.info())

# describe 
# print(df.describe())

# columns 
# print(df.columns)

# distribute the data in x,y

x = df[['Hours_Studied']]
y = df['Result']

# Split the data for test and train 

x_train,x_test,y_train,y_test = train_test_split(
    x,
    y,
    random_state=42,
    test_size=0.2
)

# select the model 

model = LogisticRegression()

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

# prediction

ques = float(input("Enter Study Hours: "))

new_data = pd.DataFrame({
    "Hours_Studied" : [ques]
})

prediction = model.predict(new_data)

if(prediction == 0):
    print("Fail")
else:
    print("Pass")
