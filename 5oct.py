# fibonacci series : 
"""

0 1 1 2 3 5 8   
"""

"""n=int(input("enter the number of fibonacci series : "))  # 10 
a=0   # a,b =0,1
b=1 
count =0   # 0 

while count <n :  # 4 < 10 
    print(a,end=" ")  # 0 1 1 2 3    
    c=a+b   # c =2+3 =5   
    a=b   # a=3  
    b=c   #b=5  
    count +=1   # 4 
"""

# strong number  : 
"""
145 : 
each factorial  : 1! = 1
4! = 1*2*3*4 =24 
5! =!*2*3*4*5 =120 

sum = 1+120 +24  = 145   ==> strong number

"""
"""n=int(input("enter the number : "))  # 145 
sum =0 
temp =n 
while n >0 :   # 145 > 0 
    r = n % 10  # r = 145 %10 =5 
    fact =1   # reset 
    while r >0 :  
        fact = fact *r 
        r= r-1
    sum = sum +fact 
    n = n //10 
if sum ==temp :
    print("strong number")
"""

# twin  : 
"""
123 :
each sum 1+2+3 = 6 
each mul 1*2*3 = 6 

"""
"""n=int(input("enter the number : "))  

sum =0 
mul =1 

while n >0 : 
    r = n %10 
    sum = sum +r 
    mul =mul *r 
    n =n //10 
if sum ==mul :
    print("twin")
"""

# perfect : 
"""
28 factors  :1 2 4 7 14 28 
sum = 1+2+4+7+14 = 28 perfect 
"""
"""n=int(input("enter the number : "))  # 6
sum =0 
i=1 
while i < n :  # 1 <6 
    if n % i ==0 :  # 6 
        sum +=i 
    i+=1 
if sum ==n : 
    print("perfect")
"""

# string  : 

s1="my name is  param patel."

"""
s2=["my","name","is","param","patel."]
# "my name is  param patel."

s3 =" ".join(s2)
print(s3)
"""

"""s2="happydiwali20oct"

print(s2.isalpha())
print(s2.isalnum())
"""

"""s3="123456"
print(s3.isdigit())
print(s3.isdecimal())
print("٠".isdecimal()) 

print(s3.isnumeric())
print("12345".isnumeric())
print("²³".isnumeric())
print("½".isnumeric())
"""

# task  :1 
"""
ask user to enter the  string  store in to  list  and seprate  pelindrome string in another  list. 

input  : ["121", "maam" , "php","my","raj"]
output  : ["121", "maam" , "php"]

task  : 6 Write a Python program to count the number of strings from a given list of strings. 
	The string length is 2 or more and the first and last characters are the same.
	
	Sample List : ['abc', 'xyz', 'aba', '1221']
	Expected Result : 2

"""
# adv  list / list  comprehensive  : 

"""
l1= [[[1,2],
     [3,4],
     [5,6]]] # 2*3 matrix : 
print(l1)

for i in l1 : 
    print(i)
"""

# numpy : python  ==> use matrix , array  == > pip install  numpy 

import numpy as np    # ==> np access  

"""l1= [[1,2,3],
     [4,5,6],
     [7,8,9]] # 3*3 matrix : 
print(l1)
"""
"""
matrix :
R  C
(0,0) 1 (0,1)2 (0,2)3 
(1,0) 4 (1,1)5 (1,2)6 
(2,0) 7 (2,1)8 (2,2)9
"""
"""print(l1[0])
print(l1[0] [1:3])
print(l1[2] [2:3])
print(l1[1] [-2])
"""

# creating array  with numpy : 
# 1 d array  : 
"""
a= np.array([1,2,3,4,5,6,7,8,9])
print("array :",a)
"""
# a=[10,20]
# print(a)

"""print(a)
print(a[2:4])
print(a[1:-1])
print(a[-1])
print(a[2:8:2])
"""
# matrix  using  numpy :

a= np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""
"""
print(a[0])
print(a[ :,1])
print(a[1,:])
"""
# print(a[1:2,0:3:2])
# c 5 6  r    v    r    t    r 5 

"""b= np.array([True,False,True,False,True],dtype=int)
print(b)
"""

a= np.array([[1,2],[3,4]])
print(a)
b= np.array([[5,6],[7,8]])
print(b)

print(a+b)
print(a*b)

print(np.min(a))
print(np.min(b))
print(np.sum(a))

"""
a            b 
[[1 2]      [[5,6]]
 [3 4]]      [7,8]]  
"""

# c = np.array((2,3))
# print(c)

c= np.zeros((2,3))
print(c)

d= np.ones((3,3))
print(d)

f=np.eye(3,dtype=int)  # identity matrix 
print(f)

"""
g = np.arange(1,7).reshape((2,3))
h = np.arange(11,20).reshape((3,3))
print(g)
print(h)
"""
"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]
[[11 12 13]
 [14 15 16]
 [17 18 19]]
"""
# print(g+h)
# print(np.matmul(g,h))

e = np.array([1,2,3,4,5,6])

g =np.where(e>5)  # condition 
print(g)

t =np.linspace(1,10,5)
print(t)
# 10-1 / 5-1  = 

# end -start / number - start  

