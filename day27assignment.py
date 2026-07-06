# Q1. Create a 1D NumPy array containing numbers from 1 to 10.
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)

# Q2. Create a 2D array of shape (3,4).
import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr)

# Q3. Create a 3×3 matrix filled with zeros.
import numpy as np
arr = np.zeros((3,3))
print(arr)

# Q4. Create a 4×4 matrix filled with ones.
import numpy as np
arr = np.ones((4,4))
print(arr)

# Q5. Create an empty array of size 6.
import numpy as np
arr = np.empty(6)
print(arr)

# Q6. Generate numbers from 10 to 100 using arange().
import numpy as np
arr = np.arange(10,101)
print(arr)

# Q7. Generate 8 equally spaced numbers between 1 and 5 using linspace().
import numpy as np
arr = np.linspace(1,5,8)
print(arr)

# Q8. Generate logarithmically spaced numbers from 10¹ to 10⁴ using logspace().
import numpy as np
arr = np.logspace(1,4,4)
print(arr)

# Q9. Generate a 3×3 array of random floating-point numbers.
import numpy as np
arr = np.random.rand(3,3)
print(arr)

# Q10. Generate ten random integers between 50 and 100.
import numpy as np
arr = np.random.randint(50,101,10)
print(arr)

# Q11. Find the dimension (ndim) of an array.
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr.ndim)

# Q12. Find the shape of a 3D array.
import numpy as np
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr.shape)

# Q13. Find the total number of elements using size.
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr.size)

# Q14. Find the data type of an array.
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.dtype)

# Q15. Find the memory occupied by each element using itemsize.
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.itemsize)

# Q16. Create an integer array and convert it to float.
import numpy as np
arr = np.array([1,2,3,4,5])
float_arr = arr.astype(float)
print(float_arr)

# Q17. Convert a float array into integers.
import numpy as np
arr = np.array([1.2,2.5,3.8,4.1])
int_arr = arr.astype(int)
print(int_arr)

# Q18. Convert an integer array into strings.
import numpy as np
arr = np.array([1,2,3,4,5])
str_arr = arr.astype(str)
print(str_arr)
"""
# Q19. Try converting ["10","20","Hello"] into integers. What happens?
import numpy as np
arr = np.array(["10","20","Hello"])
int_arr = arr.astype(int)
print(int_arr)
"""
# Q20. Create a string array and display its data type.
import numpy as np
arr = np.array(["Python","NumPy","Pandas"])
print(arr)
print(arr.dtype)

# Q21. Perform addition between two arrays.
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(arr1+arr2)

# Q22. Perform subtraction between two arrays.
import numpy as np
arr1=np.array([10,20,30])
arr2=np.array([1,2,3])
print(arr1-arr2)

# Q23. Multiply an array by 5.
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr*5)

# Q24. Divide every element by 2.
import numpy as np
arr=np.array([10,20,30,40,50])
print(arr/2)

# Q25. Find the square of every element.
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr**2)

# Q26. Find the square root of an array.
import numpy as np
arr=np.array([1,4,9,16,25])
print(np.sqrt(arr))

# Q27. Find the cube of every element.
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr**3)

# Q28. Find the absolute values.
import numpy as np
arr=np.array([-10,-20,30,-40,50])
print(np.abs(arr))

# Q29. Find the exponential values.
import numpy as np
arr=np.array([1,2,3])
print(np.exp(arr))

# Q30. Find the natural logarithm.
import numpy as np
arr=np.array([1,2,3,4,5])
print(np.log(arr))

# Q31. Print the first element.
import numpy as np
arr=np.array([10,20,30,40,50])
print(arr[0])

# Q32. Print the last element.
import numpy as np
arr=np.array([10,20,30,40,50])
print(arr[-1])

# Q33. Print elements from index 2 to 6.
import numpy as np
arr=np.array([10,20,30,40,50,60,70,80,90])
print(arr[2:7])

# Q34. Print alternate elements.
import numpy as np
arr=np.array([10,20,30,40,50,60,70,80,90])
print(arr[::2])

# Q35. Reverse the array.
import numpy as np
arr=np.array([10,20,30,40,50])
print(arr[::-1])

# Q36. Access the second row of a matrix.
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[1])

# Q37. Access the third column.
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[:,2])

# Q38. Print the last row.
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[-1])

# Q39. Print a 2×2 sub-matrix.
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[0:2,0:2])

# Q40. Modify the middle element.
import numpy as np
arr=np.array([1,2,3,4,5])
arr[2]=100
print(arr)

# Q41. Convert a 1D array into a 2×5 matrix.
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr.reshape(2,5))

# Q42. Flatten a matrix using ravel().
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr.ravel())

# Q43. Flatten a matrix using flat.
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(list(arr.flat))

# Q44. Convert a 3×2 matrix into a 2×3 matrix.
import numpy as np
arr=np.array([[1,2],[3,4],[5,6]])
print(arr.reshape(2,3))

# Q45. Create an array containing np.nan.
import numpy as np
arr=np.array([1,2,np.nan,4,5])
print(arr)

# Q46. Identify missing values using isnan().
import numpy as np
arr=np.array([1,2,np.nan,4,5])
print(np.isnan(arr))

# Q47. Create an array containing np.inf.
import numpy as np
arr=np.array([1,2,np.inf,4,5])
print(arr)

# Q48. Check infinite values using isinf().
import numpy as np
arr=np.array([1,2,np.inf,4,5])
print(np.isinf(arr))

# Q49. Check finite values using isfinite().
import numpy as np
arr=np.array([1,2,np.inf,4,5])
print(np.isfinite(arr))

# Q50. Add 10 to every element of an array using broadcasting.
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr+10)

# Q51. Multiply every element by 3 using broadcasting.
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr*3)

# Q52. Add a 1D array to a 2D array using broadcasting.
import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([10,20,30])
print(arr1+arr2)

# Q53. Display elements greater than 20.
import numpy as np
arr=np.array([10,20,30,40,50])
print(arr[arr>20])

# Q54. Display even numbers.
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr[arr%2==0])

# Q55. Display elements between 10 and 30.
import numpy as np
arr=np.array([5,10,15,20,25,30,35,40])
print(arr[(arr>=10)&(arr<=30)])

# Q56. Use logical_and().
import numpy as np
arr=np.array([5,10,15,20,25,30,35,40])
print(arr[np.logical_and(arr>=10,arr<=30)])

# Q57. Use logical_or().
import numpy as np
arr=np.array([5,10,15,20,25,30,35,40])
print(arr[np.logical_or(arr<10,arr>30)])

# Q58. Display only non-zero elements.
import numpy as np
arr=np.array([0,1,2,0,3,4,0,5])
print(arr[arr!=0])

# Q59. Find the sum of all elements.
import numpy as np
arr=np.array([1,2,3,4,5])
print(np.sum(arr))

# Q60. Find row-wise sum.
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.sum(arr,axis=1))

# Q61. Find column-wise sum.
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.sum(arr,axis=0))

# Q62. Find cumulative sum.
import numpy as np
arr=np.array([1,2,3,4,5])
print(np.cumsum(arr))

# Q63. Find cumulative product.
import numpy as np
arr=np.array([1,2,3,4,5])
print(np.cumprod(arr))

# Q64. Find the mean.
import numpy as np
arr=np.array([10,20,30,40,50])
print(np.mean(arr))

# Q65. Find the median.
import numpy as np
arr=np.array([10,20,30,40,50])
print(np.median(arr))

# Q66. Find the standard deviation.
import numpy as np
arr=np.array([10,20,30,40,50])
print(np.std(arr))

# Q67. Find the maximum value.
import numpy as np
arr=np.array([10,20,30,40,50])
print(np.max(arr))

# Q68. Find the minimum value.
import numpy as np
arr=np.array([10,20,30,40,50])
print(np.min(arr))

# Q69. Concatenate two arrays.
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(np.concatenate((arr1,arr2)))

# Q70. Join two arrays using vstack().
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(np.vstack((arr1,arr2)))

# Q71. Join two arrays using hstack().
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(np.hstack((arr1,arr2)))

# Q72. Find the transpose of a matrix.
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr.T)

# Q73. Swap axis 0 and axis 1.
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(np.swapaxes(arr,0,1))

# Q74. Find the dot product of two arrays.
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(np.dot(arr1,arr2))

# Q75. Iterate through a 1D array using nditer().
import numpy as np
arr=np.array([10,20,30,40,50])
for i in np.nditer(arr):
    print(i)

# Q76. Iterate through a 2D array.
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
for i in np.nditer(arr):
    print(i)

# Q77. Display index and value using ndenumerate().
import numpy as np
arr=np.array([10,20,30,40,50])
for index,value in np.ndenumerate(arr):
    print(index,value)

# Q78. Create a view of an array.
import numpy as np
arr=np.array([1,2,3,4,5])
view_arr=arr.view()
print(view_arr)

# Q79. Modify the view and observe the original array.
import numpy as np
arr=np.array([1,2,3,4,5])
view_arr=arr.view()
view_arr[0]=100
print("View Array:",view_arr)
print("Original Array:",arr)

# Q80. Create a copy of an array.
import numpy as np
arr=np.array([1,2,3,4,5])
copy_arr=arr.copy()
print(copy_arr)

# Q81. Modify the copied array and verify that the original array remains unchanged.
import numpy as np
arr=np.array([1,2,3,4,5])
copy_arr=arr.copy()
copy_arr[0]=100
print("Copied Array:",copy_arr)
print("Original Array:",arr)
