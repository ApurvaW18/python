import numpy as np

'''
1.Write a NumPy program to get the numpy version and show numpy build configuration.

print(np.__version__)

2.Write a NumPy program to test element-wise for complex number,
real number of a given array.
Also test whether a given number is a scalar type or not.


c=2+5.25j
print(np.real(c))
print(np.imag(c))
print(np.isscalar(c))

3.Write a NumPy program to test whether none of the elements of a
given array is zero.

n=np.array([56,78,92,0,60])
print(np.all(n))

4.Write a NumPy program to test whether any of the
elements of a given array is non-zero.

n1=np.array([51,40,20,60,80])
print(np.all(n1))

5.Write a NumPy program to test element-wise for NaN of a given array.
n=np.array([56,78,92,0,60])
print(np.isnan(n))


6.Write a NumPy program to create an element-wise comparison
(greater, greater_equal, less and less_equal) of two given arrays.

x = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
print(np.greater(x,y))
print(np.greater_equal(x,y))
print(np.less(x,y))
print(np.less_equal(x,y))

7.Write a NumPy program to create an element-wise comparison(equal,
equal within a tolerance) of two given arrays.
Input:
x = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])

x = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
print(np.equal(x,y))



8.Write a NumPy program to create an array with the values 1, 7, 13, 105 and
determine the size of the memory occupied by the array.

x=np.array([1,7,13,105])
print(x.ndim,x.shape,x.size,x.itemsize,x.data)

9.Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives.

print(np.zeros(10),np.ones(10),np.full(10,5))

10.Write a NumPy program to create an array of the integers from 30 to 70.

print(np.arange(30,71))
11.Write a NumPy program to create an array of all the even integers
from 30 to 70.

print(np.arange(30,71,2))


12.Write a NumPy program to create a 3x3 identity matrix.

print(np.eye(3))

13.Write a NumPy program to generate a random number between 0 and 1.

print(np.random.rand(3,3))

14.Write a NumPy program to generate an array of 15
random numbers from a standard normal distribution.

print(np.random.normal(0,1,15))


15. Write a NumPy program to create a vector with values ranging
from 15 to 55 and print all values except the first and last.

'''
a=np.arange(15,56)
print(a[1:-1])



