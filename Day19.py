#create an 1-d empty array
import numpy as np
arr=np.empty(5)
print(arr)

#2-d
a=np.empty([2,3])
print(a)


arr[:]=[10,20,30,40,50]
print(arr)

#perform random numbers by using function (rand fun define only 0 to 1 range )
import numpy as np
arr=np.random.rand(5)
print(arr)

a=np.random.rand(2,3)
print(a)

b=np.random.rand(3,3)
print(b)

c=np.random.rand(4,4)
print(c)

#find an random number between 1 to 50 by using randint function
import numpy as np
arr=np.random.randint(1,50)
print(arr)

a=np.random.randint(1,50,5)
print(a)

b=np.random.randint(1,50,(4,4))
print(b)

c=np.random.randint(1,50,(3,3))
print(c)


#array reshaping(he function one dimensional ch multi dimensional madhe conversion kart)
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
print(a.ndim)

b=a.reshape(3,3)
print(b)

#array revel (he function multi dimensional ch one dimensional madhe conversion kart)
import numpy as np
a=np.array([[1,2],[3,4]])
print(a.ndim)

b=a.ravel()
print(b)
print(b.ndim)

print(a)


b[0]=90
print(b)
print(a)

#by using flatten function
import numpy as np
a=np.array([[1,2],[3,4]])
print(a.ndim)

b=a.flatten()
print(b)
print(b.ndim)

print(a)

b[0]=90
print(b)
print(a)


#array data type
import numpy as np
a=np.array([1,2,3,5,67,8,9])
print(a)
print(a.dtype)

#convert interger to float
b=np.array([1,2,3,4],dtype=np.float16)
print(b)
print(b.dtype)

#by using second method covert float to int
a=np.array([90.5,60.9,24.4,23.2])
print(a)
print(a.dtype)

b=a.astype(np.int64)
print(b)

fruits=np.array(["apple","banana","grapes","kajuu","guava"])
print(fruits)
print(fruits.dtype)

a=np.array(["a","b","c","d","e"])
print(a)
print(a.dtype)


#convert integer to string data type
import numpy as np
a=np.array([12,56,70,85])
print(a)
print(a.dtype)

b=a.astype(str)
print(b)

#create an 2 by 6 array
a=np.array([[1,10,20,49,7,6],[1,2,3,4,5,6]])
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.itemsize)

b=np.array([["a","b","c","d","e","f"],["g","h","i","j","k","l"]])
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.itemsize)





















































































