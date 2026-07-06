
'''
#chart representation
import matplotlib.pyplot as plt
x=[1,2,3]
y=[4,5,6]
plt.plot(x,y)
plt.grid()
plt.show()


#linechart
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Salary" : [25000,45000,30000,50000,75000,39000,52000,55000,31000,60000,75000,43000,20000]
                
}

df=pd.DataFrame(data)
print(df)

from matplotlib.lines import lineStyles
plt.plot(df['Salary'],color="red",marker="*",linestyle="--",linewidth="2")
plt.grid()
plt.show()
       
#histogram
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Salary" : [25000,45000,30000,50000,75000,39000,52000,55000,31000,60000,75000,43000,20000]
                
}

df=pd.DataFrame(data)
print(df)

plt.hist(df)
plt.show()

plt.hist(column="Salary",bins=5,color="black")
plt.show()
'''
#boxplot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Salary" : [25000,45000,30000,50000,75000,39000,52000,55000,31000,60000,75000,43000,20000]
                
}

df=pd.DataFrame(data)
print(df)

df["dept"]= ["HR","IT","Admin","IT","HR","Finance","Admin","HR","Admin","IT","Finance","HR","IT"]
print(df)
count=df["dept"].value_counts()
print(count)

plt.pie(count,labels=count.index,autopct="%2.0f",explode=[0,0,0.2,0.2],shadow="True")
plt.show()

plt.bar(count.index,count,color=["red","blue","pink"])
plt.show()
        












