# lambda  : one  liner  function  . 
"""
syntax : 

lambda arg : expression 
"""

# function  : 
"""
def addition(a,b):
    return a+b
print(addition(12,23)) 
"""
# lambda  : 

"""x =lambda a,b : a+b
a=int(input("enter the a  value :"))
b=int(input("enter the a  value :"))
print(x(a,b))
"""

# lambda using built in function  : len min max sorted sum 

"""a= lambda x : sum(x)
print(a("my name is  krithik."))
print(a([19,2,3,4,50,6]))
print(a((17,2,3,4,5,6)))
"""
# conditional  statement  : 

"""def x(a,b):
    if a>b :
        return a
    else :
        return b
print(x(12,45))
"""
"""
x =lambda a,b : print("a is big",a)if a>b else print("b is big",b) 
x(45,78)
"""

# using  for  loop  : 

# ex :1 
"""l1=[] 
for i in range(5): 
    l1.append(lambda x , i=i : x+i) 
    
for j in l1 :
    print(j(10))
    
"""

# ex :2 

# l1= [1,2,3,4,5]  

"""square = lambda x : x *x 
for i in l1 :
    print(square(i))
"""    
"""even = lambda x : x%2==0 
for i in l1 :
    if even(i) :
        print(i)
"""
    
# filter : 
"""
excel  : 
phonpe  ==> history  ==> trans ==> june   
"""
"""
l1=[1,2,3,4,5,6,7,8,9]
even =[] 
odd =[] 

for i in l1 : 
    if i %2 ==0 : even.append(i)
    else : odd.append(i)
print(even)
print(odd)
"""
# filter  ==> lambda  : 
"""
l1=[1,2,3,4,5,6,7,8,9]

a=tuple(filter(lambda x : x %2 ==0,l1)) 
b=list(filter(lambda x : x %2 ==1,l1)) 
print(a)
print(b)
"""
# map : change  the  value  of  a  list

"""
l1=[1,2,3,4,5,6,7,8,9]
l2=[]
for i in l1 :
    l2.append(i*i) 
print(l2)
"""
"""l1=[1,2,3,4,5,6,7,8,9]
a=tuple(map(lambda x : x *x,l1)) 
print(a)

"""

# task  :1  sort the  below  list for second  value .
"""
input  : [[1,2],[2,0],[4,1]] 
output : [[2,0],[4,1],[1,2]]
"""
