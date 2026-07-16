#KNeighborsClassifier algorithm

from sklearn.neighbors import KNeighborsClassifier
X = [
    [180, 7],
    [200, 7.5],
    [250, 8],
    [300, 8.5],
    [330, 9],
    [360, 9.5]
]

y = ["Apple", "Apple", "Apple", "Orange", "Orange", "Orange"]

model=KNeighborsClassifier(n_neighbors=3)
model.fit(X,y)
prediction=model.predict([[330,9]])
print(prediction)

   
#student fail ya pass by using KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
X = [
    [2, 50],
    [3, 60],
    [4, 65],
    [6, 80],
    [7, 85],
    [8, 95]
]
y = ["Fail", "Fail", "Fail", "Pass", "Pass", "Pass"]

model=KNeighborsClassifier(n_neighbors=3)
model.fit(X,y)
prediction=model.predict([[6,80]])
print(prediction)


#q3)diabets predication dataset
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
df=pd.read_csv("Diabetes_Prediction_Dataset.csv")
print(df)

#checking null values
print("\nNull Values Before Removing:")
print(df.isnull().sum())

#remove null values
df=df.dropna()

#
X=df[["Age","Blood_Sugar","BMI"]]
y=df["Diabetes"]

model=KNeighborsClassifier(n_neighbors=3)
model.fit(X,y)
prediction=model.predict([[35,175,31]])
print(prediction)

if prediction[0]==1:
    print("diabetes")
else:
    print("not diabetes")




