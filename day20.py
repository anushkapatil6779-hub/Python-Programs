
#perform arthmatic operations on array
import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)

a=np.array([1,2,3])
b=np.array([4,5,6])
print(a-b)

a=np.array([1,2,3])
b=np.array([4,5,6])
print(a*b)

a=np.array([1,2,3])
b=np.array([4,5,6])
print(a/b)

a=np.array([1,2,3])
b=np.array([4,5,6])
print(b/a)

a=np.array([1,2,3])
b=np.array([4,5,6])
print(a%b)

a=np.array([1,2,3])
b=np.array([4,5,6])
print(b%a)

a=np.array([1,2,3])
b=np.array([4,5,6])
print(a**2)

a=np.array([1,2,3])
b=np.array([4,5,6])
print(a**3)

a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+5)

a=np.array([1,2,3])
b=np.array([4,5,6])
print(a-5)

#
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(a @ b)   #1st formula to print multiplication of 2 dimension array
print(np.matmul(a,b)) #2nd formula to print multiplication of 2 dimension array

#to find value of sin,cos,tan 
import numpy as np
print(np.exp([1,2]))

arr=np.array([0,np.pi/2,np.pi])
print(np.sin([arr]))


import numpy as np
arr=np.array([1,4,9,1,4,9,1])
print(arr.sum()) #prints addition of all elements
print(arr.mean()) #prints sum divided of all elements
print(arr.max()) #print maximum values of given array
print(arr.min()) #print minimum values of given array
print(arr.argmin()) #print index of minimum value
print(arr.argmax()) #print index of maximum value
print(np.sort(arr)) #print ascending order
print(np.unique(arr)) #print unique value of the given array
print(np.sqrt(arr))  #print square roots
print(np.square(arr)) #print square of every element in the given array

#perform indexing on array
import numpy as np
arr=np.array([1,4,9,1,4,9,1])
print(arr[2])
print(arr[-1])
print(arr[4])
print(arr[-3])
print(arr[-7])

#perform slicing on one dimensional array
import numpy as np
arr=np.array([5,6,5,1,2,3,4])
print(arr[0:6])
print(arr[2:5])
print(arr[-4:-2])
print(arr[-5:-3])
print(arr[-6:-2])

print(arr[2:6:1])
print(arr[0:5:2])


#perform indexing on 2d array
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[0:2])
print(arr[0:2,0:1])
print(arr[1: ,:2])
print(arr[1: , 1:])










































