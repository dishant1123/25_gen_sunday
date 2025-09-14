# list  : mutable  sequence  ==> changes in  list  ==> mutable  ==> changes 

"""
l1=[1,2,3,4,5,6,"raj",90.67,True,9j]

print(l1)
print(type(l1))
"""

# list  : access index 
"""
index start with  : 0 ,1,2 ,3  .....  ==> l to r 
neg index start with  : -1 ,-2 ,-3  ==>  r to  l 
"""

"""
l1=[1,2,3,4,5,6,"raj",90.67,True,9j]

print(l1[3])   #==> print   3 index number  element : 4 
# list  update  ==>  using  index number  
l1[4]="simran"   # ==> value  update 
print(l1)
"""

# built  in function  : len  min  max sorted sum 

"""
l1=[1,2,3,4,5,6,90,78,65,34]

print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1)) # asc to desc 
print(sum(l1))

# desc to asc : reverse 
print(sorted(l1,reverse=True))
"""

# slicing  : 

"""
l1=[10,20,30,40,50,60,90,78,65,34]
#   0  1  2  3  4  5  6  7  8  9
# index start with  : 0 ,1,2 ,3  .....  ==> l to r 
# neg index start with  : -1 ,-2 ,-3  ==>  r to  l 

print(l1[4])  # index number   ===> output  element 
print(l1[ 2 :5])  # start index 2   ending  index 5 
print(l1[ : 8])   # start  ==> default  0 
print(l1[2 : ])   # ending  ==> last  

print(l1[-2])
print(l1[-6 : -2])

print(l1[2 :8 :2])   # start index =2  end index= 8 step= 2
print(l1[1 :8 :3])   # start index =1  end index= 8 step= 3
print(l1[ : : 2])  # start  end  step  ==>2 
print(l1[ : :-2])  # start  end  step  ==>-2 
print(l1[ : :-1])  # start  end  step  ==>- 1
"""

# method  : 

l1=[10,90,20,30,40,50,60,90,78,65,34,90]

# l1.append(900)  # aapend ==> add in  last 
# print(l1)

"""l1.insert(3,"raj")  # 2 arg  ==> index ,  value 
print(l1)
"""
"""l1.remove(90)  # specific value 
print(l1)
"""
"""l1.pop(4)  # index number wise 
print(l1)
"""

"""print(l1.index(90) ) # arg ==> element  ==> print ==> index 
print(l1.index(90,2,20))
print(l1.index(90,8,20))
"""

l1=[10,90,20,30,40,50,60,90,78,65,34,90]

# print(l1.count(90))

"""
l2=["raj","simran"]
l1.extend(l2)
print(l1)
"""
"""l1.clear()
print(l1)
"""
"""l2=l1.copy()
print(l2)"""

"""l1.sort()  # asc to desc 
print(l1)
"""
"""l1.reverse()
print(l1)
"""


# advanced   list  / list comprehension  :

"""l1=[[1,2,3], 
    [4,5,6],
    [7,8,9]]

print(l1)"""
"""
for i in l1: 
    print(i)
"""
"""
l1=[[1,2,3],   ==> row 0  ==> 1 2 3  
    [4,5,6],   ==> row 1 ==> 4 5 6 
    [7,8,9]]   == > row 2 ==> 7 8 9
#r c 
(0,0)1 (0,1)2 (0,2)3
(1,0)4 (1,1)5 (1,2)6
(2,0)7 (2,1)8 (2,2)9
"""
"""l1=[[1,2,3,89], 
    [4,5,6,90],
    [7,8,9,91]]


print(l1[0])
print(l1[0][2])
# l1.insert(2,[100,200,300])
# print(l1)

print(l1[1][1 :3])
"""

# tuple  : immutable  ==> not  changes in tuple  

"""t1=(1,2,3,4,5,6,7,8,9,10,"raj",6j,True)
print(t1)
print(type(t1))

t2 =1,2,3,4,5,56
print(t2)
print(type(t2))
"""

# built in function  : len min max sorted sum

"""
t2 =18,2,3,4,5,56
print(len(t2))
print(min(t2))
print(max(t2))
print(sorted(t2))  # asc to dec
print(sum(t2))
"""
# t2[2] ="raj"  # tuple  immutable  not  changes in tuple. 
# print(t2)

# slicing  : 
"""t2 =18,2,3,4,5,56
print(t2[4])
"""
# method  : 
"""t2 =18,2,3,4,5,56,56

print(t2.count(56))
print(t2.index(56))
"""
"""
MCQ : 

t1=(1,2,3,4,[67,89,90],99)
t[4].append("saloni")
print(t1) 

a.error    
b.(1,2,3,4,[67,89,90],"saloni",99)
c.(1,2,3,4,[67,89,90,"saloni"],99)
d.none 
"""
t1=(1,2,3,4,[67,89,90],99)
#   0 1 2 3 4 

t1[4].append("saloni")
print(t1) 
print(t1[4][1])