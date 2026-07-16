from sklearn.tree import DecisionTreeClassifier,plot_tree
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = [
    [80, 1, 5],    
    [90, 1, 6],    
    [85, 1, 4],    
    [95, 1, 5],    
    [150, 0, 9],   
    [160, 0, 10],  
    [170, 0, 8],   
    [180, 0, 9]    
]


labels = [
    "Apple",
    "Apple",
    "Apple",
    "Apple",
    "Mango",
    "Mango",
    "Mango",
    "Mango"
]

model = DecisionTreeClassifier(max_depth=2)

model.fit(data, labels)

new_data = [[50, 1, 5],[90, 1, 6],[140, 0, 8]]

result = model.predict(new_data)

print(result)

plot_tree(model,
          feature_names=["weight","color","sweetness"],
          class_names=["Apple","Mango"]
          )
plt.show()


#movie recommentation
data = np.array([
    [25,1,4],       #age , liked or not like movie, rated
    [35,0,2],
    [20,1,5],
    [40,1,3],
    [28,0,1]
    ])-

labels = np.array([1,0,1,1,0])     #1 = recommends movie 0 = not recommend

model = DecisionTreeClassifier(max_depth=2)

model.fit(data, labels)

new_data = [[40, 1, 5],[90, 1, 6],[140, 0, 8]]

result = model.predict(new_data)
print(result)

###
df=pd.read_csv("Movie_Recommendation.csv")
print(df)

x=df[["Age","Likes_Action","Rating"]]
y=df["Recommend"]

#EDA
print(df.head())
print(df.head(2))
print(df.tail())
print(df.tail(2))
print(df.shape)
print(df.size)
print(df.ndim)
print(df.info())
print(df.describe())



