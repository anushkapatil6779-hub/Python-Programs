'''
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
x=[[1],[2],[3],[4],[5]]
y=[0,0,1,1,1]
model=LogisticRegression()
model.fit(x,y)
result=model.predict([[2]])
result=model.predict([[3]])
result=model.predict([[5]])
print(result)
plt.scatter(x,y)
plt.plot()
plt.show()



from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
x=[[30],[35],[40],[50],[65]]
y=[0,0,1,1,1]
model=LogisticRegression()
model.fit(x,y)
result=model.predict([[50]])
result=model.predict([[60]])
result=model.predict([[5]])
print(result)
plt.scatter(x,y)
plt.plot()
plt.show()


#q3) age eligibility oe not
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
x = [[10],[15],[20],[25],[30],[35],[45]]  #age
y = [0,0,1,1,1,1,1]  #eligibility 0=Not Eligible, 1=Eligible
age=LogisticRegression()
age.fit(x,y)
result=age.predict([[25]])
result=age.predict([[10]])
result=age.predict([[25]])
print(result)
plt.scatter(x,y)
plt.plot()
plt.show()

#by using if-else
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
x = [[10],[15],[20],[25],[30],[35],[45]]  #age
y = [0,0,1,1,1,1,1]  #eligibility 0=Not Eligible, 1=Eligible
age=LogisticRegression()
age.fit(x,y)

result=int(input("enter your age"))

if result == 1:
    print("person is eligible for voting")
else:
     print("person is not eligible for voting")
print(result)     

plt.scatter(x,y)
plt.plot()
plt.show()


#email spam ya not spam
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

#1.sample data
emails=[
    "Congratulationa!You Won a free lottery prize ticket now",
    "We have meeting at 2 PM",
    "URGENT:Click this link to claim your cash reward immediately",
    "Please find attached the project documentation and notes",
    "Get cheap loans and fast cash deals today without verification",
    "Can you review the python code before the submission?",
    "Let me know when you are free to check the proect assignment",
    "Free entry ticket to win cash prizes now1"
]

#labels:1=spam 0=safe
labels=[1,0,1,0,1,0,0,1]

vectorizer=CountVectorizer()
x=vectorizer.fit_transform(emails)
y=np.array(labels)

model=LogisticRegression()
model.fit(x,y)

#test the model
new_emails=["Congratulations!You own laptop",
            "Last date to submit assignment"
            ]
new_x=vectorizer.fit_transform(new_emails)

#make predications
predictions=model.predict(new_x)
print("predictions:",predictions)
'''

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# STEP 1: Create Dataset
data = {
    "Glucose": [80, 85, 90, 95, 100, 110, 120, 130, 140, 150],
    "Diabetes": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Dataset:")
print(df)

# STEP 2: Separate X and y
X = df[["Glucose"]]      # Independent Variable
y = df["Diabetes"]       # Dependent Variable

# STEP 3: Split the Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)

# STEP 4: Train Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nPredictions:")
print(predictions)

plt.scatter(X_train, y_train, color="blue", label="Actual")
plt.scatter(X_test, y_test, color="blue")
plt.scatter(X_test, predictions, color="red", label="Predicted")

plt.xlabel("Glucose")
plt.ylabel("Diabetes")
plt.legend()
plt.show()
















    
