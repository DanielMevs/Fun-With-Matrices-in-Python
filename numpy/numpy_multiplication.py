import numpy as np

#multiplication of a 2x2 matrix
a = np.array([[2,3],[1,3]])
b = np.array([[2,2],[1,0]])
c = np.dot(a,b)
print(a)
print(b)
print(c)


a = np.matrix(np.arange(12).reshape((3,4)))
print(a)
#using the numpy matrix class
#arrange(n) increments by an interval of 1 the numbers from 0 to n-1
#reshape(x,y) sizes the matrix with x rows  and y columns

b =  a[0]
#b is initialized to the first row of matrix a


