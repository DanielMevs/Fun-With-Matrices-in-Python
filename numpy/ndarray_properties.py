import numpy as np
x = np.array([[2,3],[1,4],[5,7]])
print(x)

#returns a tuple with the size of the array
#here shape is synonomous with size
shape = x.shape
print(shape, "\n")

#reshapes the array to a 2 by 3
new_x = x.reshape(2,3)
print(new_x)
shape = new_x.shape
print(shape)

x[0][1] = 9
print(x)



