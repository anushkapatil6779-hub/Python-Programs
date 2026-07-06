#dictionary
import pandas as pd
fruit_protein = {
"Avocado":2.0,                    
"Guava":2.6,
"Blackberries": 2.0,
"Oranges": 0.9,
"Banana":1.1,
"Apples":0.3,
"Kiwi":1.1,
"Pomegranate":1.7,
"Mango":0.8,
"Cherries":1.0
}
print(fruit_protein)

s2=pd.Series(fruit_protein)
print(s2)

#and,or gate
print(s2>2)
print(s2[s2>2])
print(s2[(s2>0.5)&(s2<2)])
print(s2[(s2>0.5)|(s2<2)])
print(s2[~(s2<2)])

#drop&update function
s2.drop("Kiwi")
print(s2)

s2["Mango"]=1.6
print(s2)      


import numpy as np
ser=pd.Series(["a",np.nan,1,np.nan,2])
print(ser)

ser.notnull()
print(ser)
ser.notnull().sum()
print(ser)

#dictionary convert in dataframe
import numpy as np
import pandas as pd
data = {
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Age": [25, 30, 35, np.nan, 29, 25],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 70000, 62000, np.nan, 50000]
    }
print(data)
df=pd.DataFrame(data)
print(df)
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

print(df.iloc[0:4])
print(df.iloc[0:4,0:2])
print(df.iloc[1:4,1: ])
print(df.loc[1:4,["Name","Salary"]])
print(df.loc[1:4,["Name","Department","Salary"]])
print(df["Age"])
print(df.drop("Age",axis=1))
print(df)
print(df["Salary"])

#rename function inplace argument permantly data madhe change karte
print(df.rename(columns={"Department":"Dept"},inplace=True))
print(df)

#unique function
print(df["Dept"].unique())

print(df["Dept"].value_counts())

df["promoted_salary"]=df["Salary"]*2
print(df)

#null value handling
print(df.isnull())
print(df.isnull().sum())

print(df.dropna())
print(df)

print(df.dropna(how="any"))
print(df.dropna(how="all"))

print(df.fillna(0))
print(df)

print(df["Age"].fillna(df["Age"].mean()))

print(df["Salary"].fillna(df["Salary"].median()))
print(df)


#forward fill,backward fil 
print(df["Salary"].ffill())

#backward  fill
print(df["promoted_salary"].bfill())






















