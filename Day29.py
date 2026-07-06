import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Salary" : [25000,45000,30000,50000,75000,39000,52000,55000,31000,60000,75000,43000,20000]
                
}

df=pd.DataFrame(data)
print(df)
sort_Salary=df.sort_values("Salary")

df["Experience"] = [1.3,4,2,5,6,7,10,3,3.5,4,3,5,2,]


df["dept"]= ["HR","IT","Admin","IT","HR","Finance","Admin","HR","Admin","IT","Finance","HR","IT"]
print(df)
HR_Salary=df[df["dept"]=="HR"]["Salary"]
HR_Salary=df[df["dept"]=="IT"]["Salary"]
IT_Salary=df[df["dept"]=="Admin"]["Salary"]
Admin_Salary=df[df["dept"]=="Finance"]["Salary"]
Finance_Salary=df[df["dept"]=="IT"]["Salary"]

plt.boxplot([HR_Salary,IT_Salary,Admin_Salary,Finance_Salary],label=["HR","IT","Admin","Finance"])
plt.show()


df["Age"] = [23,32,34,22,26,37,23,24,29,36,32,33,35]
sort_Age=df.sort_values("Age")
print(df)

plt.scatter(df["Salary"],df["Age"],color="orange")
plt.show()

plt.plot(sort_Salary["Salary"],sort_Age["Age"],marker="*")
plt.show()

plt.plot(df["Salary"],df["Age"],linestyle=":",marker="o")
plt.grid()
plt.show()

#by using bar graph
plt.bar(sort_Age["Age"],sort_Salary["Salary"],align="center")
plt.show()


sal_by_dept=df.groupby("dept")["Salary"].sum()
plt.pie(sal_by_dept,labels=sal_by_dept.index,autopct="1.of",explode=[0,0,0.2,0.2])
plt.show()

#bubble plot


plt.scatter(df["Salary"],df["Age"],s=df["Experience"]*100,color="red",edgecolors="black")
plt.title("Salary VS Age VS Experience")
plt.xlabel("Salary")
plt.ylabel("Age")
plt.show()

#categorical data represents in plots
plt.scatter(df["Salary"],df["Age"],c=df["dept"].map({"HR":"red","IT":"blue","Finance":"black","Admin":"yellow"}))
plt.title("Salary VS Age VS dept")
plt.xlabel("Salary")
plt.ylabel("Age")
plt.show()
            





