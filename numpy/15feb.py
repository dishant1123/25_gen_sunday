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
"""
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

print(a[[0,1,2,3,4],[0,1,2,3,4]])
"""
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

# reshape , arange ,size : 

"""a=np.arange(1,20)
print(a)

b= np.arange(1,21).reshape(5,4)
print(b)

c=np.arange(1,33).reshape(2,2,2,4)
print(c)

import  random 

d= np.random.random(size=(3,4))  # 0-1 value 
d=np.random.random(size =12).reshape(3,4)  # 0-1 value
print(d)

e=np.random.randint(low=-10,high=10,size=12).reshape(4,3)
print(e)

f=np.random.sample(size=12).reshape(4,3)
print(f)
"""

# flatten  vs ravel : convert 2d array  in to  1d array  

"""
a=np.arange(1,10).reshape(3,3)
# print(a)
a1= a.flatten()  # create new  memory 
a[2,2] =99
print("original  matrix  :\n",a)
print(a1)
"""

# ravel : 
"""a=np.arange(1,10).reshape(3,3)
# print(a)
a1= a.ravel()   # it  replace the  memory  
a[2,2] =99
print("original  matrix  :\n",a)
print(a1)
"""

# np.one,np.zeros,full,full_like : 

"""a1=np.ones((3,3),dtype=int)
print(a1)

b1=np.zeros((3,3),dtype=int)
print(b1)   

c1=np.full_like(a1,fill_value=99)
print(c1)

d1=np.full((3,3),fill_value=99)
print(d1)
"""

# tranpose ,eye  ==> identity: 
"""
a=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=int)
print("original  matrix  :\n",a)

print("transpose : \n",np.transpose(a))
print(a.T)

b1 =np.eye(3,3)
print(b1)
"""

# statistical methods : 

"""a=np.array([1,2,3,4,5,6,7,8,9],dtype=int)

print(a)
print(np.mean(a))
print(np.median(a))
print(np.std(a))
print(np.var(a))
print(np.sum(a))
"""

# sum of matrix  : 
"""
axis =0   ==> means   col wise sum 
axis =1   ==> means   row wise sum
"""

"""a=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=int)

print(a)
print(np.sum(a))
print(np.sum(a,axis=0))
print(np.sum(a,axis=1))
"""


"""a= np.arange(1,49).reshape(4,4,3)
print(a)
"""
"""a=np.array([1,2,3,4,5,6,7,8,9])
print(a)
b=np.where(a>5)
print(b)
"""

