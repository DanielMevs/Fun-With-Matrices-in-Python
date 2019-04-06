import numpy as np
n = 4
m = 6
a = np.array([[1,3,-2,0,2,0],[2,6,-5,-2,4,-3],[0,0,5,10,0,15],[2,6,0,8,4,18]])
print(a)
a[1] -= 2*a[0]
print(a)
a[3] -= 2*a[0]
print(a)
a[1] *= -1
print(a)
a[2] += -5*a[1]
print(a)
a[3] -= 4*a[1]
print(a)

