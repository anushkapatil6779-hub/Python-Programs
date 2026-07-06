import pandas as pd
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,3,figsize=(10,5))
plt.show()


data = {
    "Salary": [50000, 25000, 52000, 55000, 75000, 31000, 75000, 45000, 43000, 30000, 20000, 60000, 39000],
    "dept": ["IT", "HR", "Admin", "HR", "HR", "Admin", "Finance", "IT", "HR", "Admin", "IT", "IT", "Finance"],
    "Age": [22, 23, 23, 24, 26, 29, 32, 32, 33, 34, 35, 36, 37],
    "Experience": [5.0, 1.3, 10.0, 3.0, 6.0, 3.5, 3.0, 4.0, 5.0, 2.0, 2.0, 4.0, 7.0]
}

df=pd.DataFrame(data)
print(df)

fig,axs=plt.subplots(1,3, figsize=(10,5))

#lineplot
axs[0].plot(df["Age"],df["Salary"],color="blue",marker="o",markersize="2",linewidth="2")
axs[0].grid()
axs[0].set_title("line plot")
axs[0].set_xlabel("Age")
axs[0].set_ylabel("Salary")



#histogram
axs[1].hist(df["Salary"])
axs[1].grid()
axs[1].set_title("histogram")
axs[1].set_xlabel("Salary")
axs[1].set_ylabel("Frequency")


#boxplot
axs[2].boxplot(df["Salary"])
axs[2].grid()
axs[2].set_title("boxplot")
axs[2].set_xlabel("Salary")

plt.show()


#3D graph presentation
ax=plt.axes(projection="3d")
ax.scatter(df["Salary"],df["Age"],df["Experience"])
plt.show()


#create a new 3d graph
data = {
    "Year" : [2020,2021,2022,2023],
    "Sales" : [1000,2000,3000,4000],
    "Profit" : [100,200,300,400],
    "Expenses" : [10,20,30,40]

    }

df=pd.DataFrame(data)
print(df)



ax=plt.axes(projection="3d")
ax.scatter(df["Year"],df["Sales"],df["Expenses"])
plt.show()


#
import matplotlib.pyplot as plt

plt.plot(df["Year"],df["Sales"],color="skyblue",label="Sales")
plt.plot(df["Year"],df["Profit"],color="orange",label="Profit")
plt.plot(df["Year"],df["Expenses"],color="green",label="Expenses")

    
plt.title("Financial Analysis")
plt.xlabel("Year")
plt.ylabel("Amount")
plt.legend()
plt.show()

