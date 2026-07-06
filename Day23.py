import pandas as pd
#series
s=pd.Series([10,20,30,40,50])
print(s)

#by using values function
import pandas as pd
s=pd.Series([20,40,60,80,100])
print(s)
print(s.values)
#index function
print(s.index)
#shape function
print(s.shape)
#size function
print(s.size)
#dtype function
print(s.dtype)
#ndim function
print(s.ndim)
#unique function
print(s.unique())
#sum function
print(s.sum())
#min function
print(s.min())
#max function
print(s.max())

#by using unique & value_count function
import pandas as pd
s=pd.Series([20,40,60,80,60,100,20,])
print(s)
print(s.unique())
print(s.value_counts())

#assign name 
import pandas as pd
s=pd.Series([10,20,30,40,50])
print(s)
s.name="marks"
print(s)

#indexing 
import pandas as pd
s=pd.Series([10,20,30,40,50])
print(s[1])
print(s[3])
print(s[4])

#slicing
import pandas as pd
s=pd.Series([10,20,30,40,50])
print(s[0:3])
print(s[2: ])
print(s[1:4])

#ioc,iloc function
import pandas as pd
s=pd.Series([10,20,30,40,50])
print(s.iloc[3])   #integer indexing sathi use kartat


#index function
import pandas as pd
s=pd.Series([10,20,30,40,50])
print(s)
index=["a","b","c","d","e"]
s.index=index
print(s)


#loc function used for character indexing,slicing
import pandas as pd
s=pd.Series([10,20,30,40,50])
print(s)
index=["a","d","c","z","w"]
s.index=index
print(s)
print(s.loc["w"])
print(s.loc["d"])
print(s.loc[["d","z","w"]])
print(s.loc["a":"w"])


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

s=pd.Series(fruit_protein)
print(s)

s.name="fruit_protein"
print(s)




























