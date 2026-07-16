import pandas as pd
import numpy as np

# Create Dataset
student = {
    "ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Rahul", "Sneha", "Amit", "Priya", "Karan", "Neha"],
    "Age": [20, 21, np.nan, 22, 20, 21],
    "Branch": ["AI", "CSE", "AI", "IT", "CSE", "AI"],
    "Marks": [85, 92, 78, np.nan, 65, 88]
}

# Q1 Create DataFrame
df = pd.DataFrame(student)
print("\nQ1 DataFrame")
print(df)

# Q2 First 5 rows
print("\nQ2 First 5 Rows")
print(df.head())

# Q3 Last 3 rows
print("\nQ3 Last 3 Rows")
print(df.tail(3))

# Q4 Column Names
print("\nQ4 Column Names")
print(df.columns)

# Q5 Shape
print("\nQ5 Shape")
print(df.shape)

# Q6 Data Types
print("\nQ6 Data Types")
print(df.dtypes)

# Q7 Info
print("\nQ7 Info")
print(df.info())

# Q8 Statistical Summary
print("\nQ8 Describe")
print(df.describe())

# Q9 Missing Values
print("\nQ9 Missing Values")
print(df.isnull().sum())

# Q10 Fill Missing Values with Mean
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nQ10 After Filling Missing Values")
print(df)

# Q11 Name and Marks
print("\nQ11 Name and Marks")
print(df[["Name", "Marks"]])

# Q12 Marks Greater Than 80
print("\nQ12 Marks > 80")
print(df[df["Marks"] > 80])

# Q13 AI Branch Students
print("\nQ13 AI Students")
print(df[df["Branch"] == "AI"])

# Q14 Sort by Marks Descending
print("\nQ14 Sort by Marks")
print(df.sort_values(by="Marks", ascending=False))

# Q15 Marks as NumPy Array
marks = df["Marks"].to_numpy()
print("\nQ15 NumPy Array")
print(marks)

# Q16 Maximum, Minimum, Average
print("\nQ16 Statistics")
print("Maximum =", np.max(marks))
print("Minimum =", np.min(marks))
print("Average =", np.mean(marks))

# Q17 Above Average Marks
average = np.mean(marks)
print("\nQ17 Above Average Students")
print(df[df["Marks"] > average])

# Q18 Highest Marks
print("\nQ18 Highest Marks Student")
print(df.loc[df["Marks"].idxmax()])

# Import Libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Model
model = DecisionTreeClassifier()

# Train Model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Predicted Values:")
print(y_pred)

print("\nActual Values:")
print(y_test)

print("\nAccuracy:", accuracy)
