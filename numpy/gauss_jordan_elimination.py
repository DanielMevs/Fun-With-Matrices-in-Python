import numpy as np
import random 
variables = ['a','b','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z']
print("this program computes an n by m matrix")
n = 4
m = 5

#a = np.zeros(shape=(n,m))
a = np.array([[1,1,1,5],[2,3,5,8],[4,0,5,2]])
print(a)


##creates a matrix with random values
##for i in range(n):
##    for j in range(m):
##        a[i][j] = b[i][j]
##print(a)
#print(2*a[:1])
pivot = 0
search = 0

for i in range(m-2):
    for j in range(n-1):
        print(a[j][i])
        #searches the jth column for a non-zero entry in the case that pivot = zero
        if a[j][i] == 0 and j ==pivot:
            search = j
            while(a[-search][i] != 0 and search <= m):
                search+=1
            if search == m:
                #in the event that an entire column consists of zeros
                raise Exception('there is a lack of linear independence, no unique solution') 
            a[[j,search]] = a[[search,j]] #swaps rows
        if a[j][i] != 0 and j==pivot:
            a[pivot][i] = 1 #initializes the new pivot to equal 1
        if a[j][i] != 0 and j!=pivot:
            a[j] -= (a[j][i])*a[pivot]
    pivot+=1
print(a)
##np.transpose(a)

##for i in range(m-1):
##    for j in range(n):
##        #searches the jth column for a non-zero entry in the case that pivot = zero
##        if a[j][i] == 0 and j ==pivot:
##            search = j
##            while(a[-search][i] != 0 and search <= m):
##                search+=1
##            if search == m:
##                #in the event that an entire column consists of zeros
##                raise Exception('there is a lack of linear independence, no unique solution') 
##            a[[j,search]] = a[[search,j]] #swaps rows
##        if a[j][i] != 0 and j==pivot:
##            a[pivot][i] = 1 #initializes the new pivot to equal 1
##        if a[j][i] != 0 and j!=pivot:
##            a[j] -= (a[j][i])*a[pivot]
##    pivot+=1
             
             
             
            




        

