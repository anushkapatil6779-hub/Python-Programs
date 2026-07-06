#check time for perform operation of numpy
import time
import numpy as np

l=[1,2,3,4,5,6,7,8,9,10]*1000

start=time.time()

for i in range(len(l)):
    l[i]=l[i]*2
    
print("time for list:",start)
a=np.array(l)
start=time.time()
a=a*2
print("time for numpy array:",start)

#checking space
import sys
import numpy as np
a=[1,2,3,4,5]
print("memory for list:",sys.getsizeof(a))
arr=np.array(a)
print("size of array",arr.nbytes)

import sys
import numpy as np
list=["anu",23,True,1,"mrunaa","kpit",90,53,12]
print("memory for list:",sys.getsizeof(list))
arr=np.array(list)
print("size of array",arr.nbytes)
print(list)
print(arr)

#vectorization
import numpy as np
a=np.array([1,2,3,4,5])
a=a*2
print(a)

l=[1,5,6,7,8]
for i in range(len(l)):
    l=l*2
print(l)

#dimension check
import numpy as np
a=np.array([1,2,3,4,5])
print(a.ndim)

b=np.array(26)
print(b.ndim)

c=np.array([[1,2],[3,4]])
print(c.ndim)

d=np.array([[1,2],[3,4]])
print(d.ndim)

e=np.array([[[[1,2],[3,4]]]])
print(e.ndim)
print(e)

#shape checking
d=np.array([[1,2],[3,4]])
print(d.ndim)
(d.shape)

#list comparsion
import numpy as np
l=[i for i in range(1,101)]
a=np.arange(1,101)
print(a)

b=np.arange(1,101,2)
print(b)

#linespace function
import numpy as np
arr=np.linspace(1,10),(0,1),(1,3),(0,1,3),(1,10,5),(1,10,10)
print(arr)

#logspace function
logspace(1,5,4)
print(logspace)

#zeros function
import numpy as np
a=np.zeros(10)
print(a)

b=np.zeros([2,3])
print(b)

#one's function
c=np.ones(10)
print(c)

#full function(to give other than 0,1
d=np.full(5,3)
print(d)

e=np.full([3,3],2.5)
print(e)

f=np.full([5,7],2.9)
print(f)
























