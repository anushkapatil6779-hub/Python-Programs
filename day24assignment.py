#q1)display all values greater than 30
import pandas as pd
s=pd.Series([10,20,30,40,50,60])
print(s[s>30])

#q2)display all values less than 40
import pandas as pd
s=pd.Series([10,20,30,40,50,60])
print(s[s<40])

#q3)display all values between 20 and 50
import pandas as pd
s=pd.Series([10,20,30,40,50,60])
print(s[1:5])

#q4)display all even values from the series
import pandas as pd
s=pd.Series([10,20,30,40,50,60])
print(s[s%2==0])

#q5)display values greaterthan 20 and less than 50
import pandas as pd
s=pd.Series([10,20,30,40,50,60])
print(s[(s>20)&(s<50)])

#q6)display values less than 20 or greater than 50
import pandas as pd
s=pd.Series([10,20,30,40,50,60])
print(s[(s<20)|(s>50)])

#q7)predict the output
import pandas as pd
s=pd.Series([10,20,30,40,50,60])
print(s[(s>10)&(s<50)])

#q8)find the sum of all values
import pandas as pd
s=pd.Series([10,20,30,40,50])
print(s.sum())

#q9)find the mean of all values
import pandas as pd
s=pd.Series([10,20,30,40,50])
print(s.mean())

#q10)find the max value
import pandas as pd
s=pd.Series([10,20,30,40,50])
print(s.max())

#q11)find the minimum value 
import pandas as pd
s=pd.Series([10,20,30,40,50])
print(s.min())

#q12)find the difference between maximum value and minimum value
import pandas as pd
s=pd.Series([10,20,30,40,50])
print(s.max()-s.min())

#q13)find all unique values
import pandas as pd
s=pd.Series([1,2,2,3,3,3,4,4,5])
print(s.unique())

#q14)find the frequency of each value usinf value counts()
import pandas as pd
s=pd.Series([1,2,2,3,3,3,4,4,5])
print(s.value_counts())

#Q15)find how many times the value 3 occur
import pandas as pd
s=pd.Series([1,2,2,3,3,3,4,4,5])
print((s==3).sum())

#q16)find the total number of unique value
import pandas as pd
s=pd.Series([1,2,2,3,3,3,4,4,5])
print(s.nunique())

#q17)sort the series in ascending order
import pandas as pd
s=pd.Series([50,10,80,20,30])
print(s.sort_values())

#q18)sort the series in dscending order
import pandas as pd
s=pd.Series([50,10,80,20,30])
print(s.sort_values(ascending =False))

#q19)create the following series and following operations
import pandas as pd
s=pd.Series([15,25,35,45,55,65,75])
#find shape
print(s.shape)

#find size
print(s.size)

#find data type
print(s.dtype)

#find 1st element
print(s[0])

#find last element
print(s[6])

#print elements greater than 40
print(s[s>40])

#print sum
print(s.sum())

#print mean
print(s.mean())

#print maximum values
print(s.max())

#print minimum value
print(s.min())

#sort the series
print(s.sort_values())

#create a custom index
s.index=["A","B","C","D","E","F","G"]
print(s)

#access values using loc()
print(s.loc["C"])

#access values using iloc()
print(s.iloc[2])

#q20)create dataframe from following dictionary
import numpy as np
import pandas as pd
std={
    "Name":["T","N","L","M","R","F"],
    "Age":[20,19,20,np.nan,18,21],
    "Department":["CSE","AI","DS","ML","AI","DS"],
    "Marks":[60,60,70,62,np.nan,50]
    }
print(std)
df=pd.DataFrame(std)
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
print(df.loc[1:4,["Name","Marks"]])
print(df.loc[1:4,["Name","Department","Marks"]])
print(df["Age"])
print(df.drop("Age",axis=1))
print(df)
print(df["Marks"])

#rename function inplace argument permantly data madhe change karte
print(df.rename(columns={"Department":"Dept"},inplace=True))
print(df)















































