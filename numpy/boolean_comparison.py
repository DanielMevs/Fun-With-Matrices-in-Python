a = np.matrix(np.arange(12).reshape((3,4)))
print("\nmatrix a:")
print(a)
#using the numpy matrix class
#arrange(n) increments by an interval of 1 the numbers from 0 to n-1
#reshape(x,y) sizes the matrix with x rows  and y columns

b =  a[0]
#b is initialized to the first row of matrix a
print("\nfirst row of a:")
print(b)

#compares each element in each row of matrix a with every item in row b
#and evaluating if each item is equal (True is so and False if not)
a[1,3] = 3
print(a==b)
