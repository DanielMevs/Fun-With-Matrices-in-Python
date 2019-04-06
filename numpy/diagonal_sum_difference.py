'''
code that gets the absolute value of the the difference between the left-to-right
diagonal and a right-to-left diagonal of an nxn matrix
'''
import numpy as np

def diagonalDifference(arr):
    off_set = len(arr) - 1
    lr_sum = 0
    rl_sum = 0
    for i in range(len(arr)):
        lr_sum += arr[i][i]
        rl_sum += arr[i][off_set - i]
    return abs(lr_sum - rl_sum)

arr = np.arange(1,10)
arr = np.resize(arr,(3,3))
arr[2][0] = 9
#print(arr)

print(diagonalDifference(arr))

