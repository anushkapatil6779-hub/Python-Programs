
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

#rename function
print(df.rename(columns={"Department":"Dept"},inplace=True))
print(df)

#replace function
df["promoted_salary"]=df["Salary"]*2
print(df)

print(df["Name"].replace("F","A"))

#removes duplicate rows
print(df[df.duplicated()])
print(df[df.duplicated(keep="first")])
print(df[df.duplicated(keep="last")])
df=df.drop_duplicates()

print(df[df.duplicated(subset=["Dept"])])

'''
#jr valid numbers nastil trr
df.loc[ : ,["Age"]]=df["Age"]
appy(lamba:x/10 if x>120 else x)
'''


import numpy as np
import pandas as pd
department_info = {
    "Dept": ["HR", "IT", "Finance", "Admin"],
    "Location": ["Pune", " Bengaluru " , " Mumbai ", "Goa"],
    "Manager " : ["Nina" , "Rakesh ","Manoj", "Nisha"]
}
print(department_info)
df2=pd.DataFrame(department_info)
print(df2)

inner_join=pd.merge(df,df2,on="Dept",how="inner")

print(inner_join)

print(pd.concat([df,df2],axis=1))

#jrr kadhi kadhi ekyadya table madhe double columns yetat te merge kryasathi
print(pd.merge(df,df2,on="Dept"))





