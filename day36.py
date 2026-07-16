'''
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
x=np.array([[1],[2],[3],[4],[5]])
y=np.array([40,50,60,70,80])
model=LinearRegression()
model.fit(x,y)
print(model.predict([[6]]))
print(model.predict([[7]]))                      
print(model.predict([[3]]))                     
plt.scatter(x,y)
plt.show()


#by giving input 
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
x=np.array([[1],[2],[3],[4],[5]])
y=np.array([40,50,60,70,80])
model=LinearRegression()
model.fit(x,y)
n=int(input("enter experience"))
predication=model.predict([[n]])
print("predicated salary=",predication[0])
plt.scatter(x,y)
plt.plot(x,model.predict(x))
plt.show()

#year of experience data
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
X = np.array([[1], [2], [3], [5], [7]]) #year of exp
y = np.array([4, 5, 7, 10, 14])  #salary
model=LinearRegression()
model.fit(x,y)
n=int(input("enter experience"))
predication=model.predict([[n]])
print("predicated salary=",predication[0])
plt.scatter(x,y)
plt.plot(x,model.predict(x))
plt.show()


#random state he argument aaplya data ch spliting constant rahyanasathi use kartat
'''

#model training
# Step 1: Import Libraries
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Step 2: Create Sample Data
data = {
    "Hours Studied": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Exam Score": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
}

df = pd.DataFrame(data)

print("Sample Data:\n")
print(df)

# Step 3: Define Variables
X = df[["Hours Studied"]]
y = df["Exam Score"]

# Step 4: Split Data into Training and Testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Make Predictions
y_pred = model.predict(X_test)

# Step 7: Check Results
m = model.coef_[0]
c = model.intercept_

print(f"\nBest Fit Line Equation: Exam Score = {m:.2f} x Hours + {c:.2f}")

# Step 8: Predict for New Student
hours_new = pd.DataFrame({"Hours Studied": [7.5]})

predicted_score = model.predict(hours_new)

print(f"If a student studies 7.5 hours, Predicted Score = {predicted_score[0]:.2f}")

# Step 9: Visualize Results
plt.scatter(
    df["Hours Studied"],
    df["Exam Score"],
    color="blue",
    edgecolor="black",
    label="Actual Students"
)

plt.plot(
    df["Hours Studied"],
    model.predict(X),
    color="red",
    linewidth=2,
    label="Best Fit Line"
)

plt.title("Student Performance Prediction")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.legend()
plt.grid(True)
plt.show()


#second question
# Step 1: Import Libraries
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Step 2: Create Sample Data
data = {
    "Car_Age": [1,2,3,4,5,6,7,8,9,10],
    "Resale_Price": [9.5,8.8,8.1,7.4,6.7,6.0,5.4,4.8,4.2,3.7]
}

df = pd.DataFrame(data)

print("Sample Data:\n")
print(df)

# Step 3: Define Variables
X = df[["Car_Age"]]
y = df["Resale_Price"]

# Step 4: Split Data into Training and Testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Make Predictions
y_pred = model.predict(X_test)

# Step 7: Check Results
m = model.coef_[0]
c = model.intercept_

print(f"\nBest Fit Line Equation: Resale Price = {m:.2f} x Car Age + {c:.2f}")

# Step 8: Predict for New Car
car_age_new = pd.DataFrame({"Car_Age": [5.5]})

predicted_price = model.predict(car_age_new)

print(f"If a car is 5.5 years old, Predicted Resale Price = {predicted_price[0]:.2f} Lakhs")

# Step 9: Visualize Results
plt.scatter(
    df["Car_Age"],
    df["Resale_Price"],
    color="blue",
    edgecolor="black",
    label="Actual Data"
)

plt.plot(
    df["Car_Age"],
    model.predict(X),
    color="red",
    linewidth=2,
    label="Best Fit Line"
)

plt.title("Car Resale Price Prediction")
plt.xlabel("Car Age (Years)")
plt.ylabel("Resale Price (Lakhs)")
plt.legend()
plt.grid(True)
plt.show()
  
