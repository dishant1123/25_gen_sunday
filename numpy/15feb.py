# pip install numpy

import numpy as np 

"""
use : 
1. matrix 
2. statistical analysis 
3. linear algebra
4. array 1d 2d 3d  also convert 
"""

# create a array 1d    : 
"""
a=np.array([1,2,3,4,5,6,7,8,9],dtype=int)

print(a)
print(type(a))
print(a.size)   # total number  of elements  of array 
print(a.shape)   # row  col  
print(a.ndim)  # number  of  dimensions 
print(a.dtype)  # data type  
print(a.itemsize)  # size  of  each  element
print(a.nbytes)  # total  number  of  bytes

"""
#built in function  : 
"""
a=np.array([1,2,3,4,5,6,7,8,9],dtype=int)

print(len(a))
print(min(a))
print(max(a))
print(sum(a))
print(sorted(a))  # asc to desc 
print(sorted(a,reverse=True))  # desc to asc
print(np.sort(a))
"""

# slicing  : 

"""a=np.array([1,22,13,84,35,46,7,87,90],dtype=int)

print(a)
print(a[0])
print(a[1:4])
print(a[1:6:2])
print(a[: : -1])
"""

# 2d array  : 

"""a=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=int)

print(a)
print(a.shape)
print(a.ndim)
print(a.size)
"""

# slicing  in  2d array  : 

a=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
])
print(a)
print(a[0])
print(a[1:3])  #  row  slice 

print(a[1:4,1:3])  # 1:4 row slice ,  1:3  col slice 
print(a[:,1:5])
print(a[1:5, : :-1])

# task : 
"""
1. print  corners : 
     output  :  [[1,5],
                [21,25]]

2. print  diagonals :
    output  : [1,7,13,19,25]
    
3. print  like  this  : 
    output : [[4,5],
            [19,20],
            [24,25]]
"""