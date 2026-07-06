#by using nditer function and ndenumerrate function
import numpy as np
a=np.array([[1,2],[3,4]])
for x in np.nditer(a):   #array madhil each and every element access krun print karto
    print(x)

for ind,x in np.ndenumerate(a):
    print(ind,x)


#by using view and copy function
import numpy as np
a=np.array([1,2,3,4])
print(a)
view=a[1:3]
print(view)
view[0]=200
print(view)
print(a)
#copy function
copy=a[1:3].copy()
print(copy)
copy[0]=2
print(copy)
print(a)

#by using transpose function
import numpy as np
arr=np.array([[1,2],[3,4]])
print(arr)
print(arr.transpose())

#concatnation
import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
print(arr1+arr2)
print(np.concatenate((arr1,arr2)))
b=np.vstack((arr1,arr2))
print(b)
print(np.hstack((arr1,arr2)))

#split function
import numpy as np
a=np.array([[1,2],[3,4],[5,6],[7,8]])
print(np.split(a,2))
print(np.split(a,4))
print(np.vsplit(a,4))
print(np.hsplit(a,4))

#repeat and tile function
import numpy as np
arr=np.array([[1,2,3,4]])
print(np.repeat(arr,2))
print(np.tile(arr,2))

import numpy as np
arr=np.array([1,2,3,4])
np.where(arr<2,"low","high")
?
?
?


import numpy as np
arr=np.array[0,1,2,0,,3,4])
print(arr)






import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr+1)
print(arr-1)
print(arr*1)
print(arr%1)
print(arr/1)

import numpy as np
arr=([1,2,np.nan,4,np.inf,5,6])
print(arr)
print(np.isnan(arr))
print(np.isinf(arr))
print(np.isfinite(arr))











































               
