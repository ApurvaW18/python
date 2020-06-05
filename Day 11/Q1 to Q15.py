import numpy as np
'''
1.Write a NumPy program to create a 3X4 array using and iterate over it.

a=np.arange(1,13).reshape(3,4)
for i in a:
    print(i)

2.Write a NumPy program to create a vector of length 10 with values evenly
distributed between 5 and 50.

print(np.linspace(5,50,10))

3.Write a NumPy program to create a vector with values from 0 to 20 and
change the sign of the numbers in the range from 9 to 15.


4.Write a NumPy program to create a vector of length 5 filled with
arbitrary integers from 0 to 10.

print(np.linspace(0,10,5))

5.Write a NumPy program to multiply the values of two given vectors.


a=np.arange(0,9).reshape(3,3)
b=np.arange(9,18).reshape(3,3)
print(np.multiply(a,b))

6.Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.

print(np.arange(10,22).reshape(3,4))

7.Write a NumPy program to find the number of rows and columns of a given matrix.


8.Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements
are 1, the rest are 0.

print(np.eye(3,3))

9.Write a NumPy program to create a 10x10 matrix, in which the elements on the
borders will be equal to 1, and inside 0.

a=np.full((10,10),1)
a[1:9,1:9]=0

print(a)

10.Write a NumPy program to create a 5x5 zero matrix with elements on the main
diagonal equal to 1, 2, 3, 4, 5.

print(np.diag([1,2,3,4,5]))


11.Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered,
with zeros on the main diagonal.

a=np.zeros((4,4))
a[::2,1::2]=1
a[1::2,::2]=1
print(a)


12.Write a NumPy program to create a 3x3x3 array filled with arbitrary values.

print(np.random.normal(1,6,(3,3,3)))

13.Write a NumPy program to compute sum of all elements, sum of each column
and sum of each row of a given array.

a=np.arange(0,9).reshape(3,3)
print(np.sum(a))
print(np.sum(a,axis=1))
print(np.sum(a,axis=0))


14.Write a NumPy program to compute the inner product of two given vectors.

a=np.arange(0,9).reshape(3,3)
b=np.arange(9,18).reshape(3,3)
print(np.multiply(a,b))



15.Write a NumPy program to add a vector to each row of a given matrix
'''
a=np.arange(0,9).reshape(3,3)
b=np.arange(9,18).reshape(3,3)
print(np.add(a,b))




