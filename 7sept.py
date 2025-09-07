# list  comprehesive  :  mutable   , changes in list . 

"""l1=[1,2,3,4,5,6]   # ==> 1 d array  : 
print(l1)
"""

# list in  list  : 

"""l1=[[1,2],[3,4],[5,6]]    # ==>  2d array  ==> matrix :  ==> (3,2)

print(l1)

for i in l1 :
    print(i)
"""

# 3*3 matrix  : 

l1= [[1,2,3], 
     [4,5,6], 
     [7,8,9]]

# component :
"""
 r c
(0,0)1 (0,1)2 (0,2)3 
(1,0)4 (1,1)5 (1,2)6
(2,0)7 (2,1)8 (2,2)9
"""
"""
for i in l1:
    print(i)
"""

# slicing  : 

"""
l1= [[1,2,3,67], 
     [4,5,6,78], 
     [7,8,9,90],
     [90,91,92,94]]
        #r
print(l1[0])  #  row  ==> 
print(l1[0][1:3])
#param ==>   2,3     raj ==> 1,2,3 67  2,3,67   vidhya ==>2,3,67   kishan ==>2,3                       

# [0] ==> [1,2,3,67] ==> 1==>0  2 ==>1 3 ==>2  67 ==>3 

print(l1[1][1:-1])
# pratham  5,6,78   dev 5,6     kishan 5,6   rohit =5,6 

print(l1[2][0 :3: 2])
print(l1[3][  : : -1])

# param :    rohit      
"""

# task :1 convert  in to trasnpose matrix :  
"""
input  : 
l1= [[1,2,3], 
     [4,5,6], 
     [7,8,9]]

ouput : 

[1,4,7]
[2,5,8]
[3,6,9]
"""

"""
l1= [[1,2,3],    # 1 2 3 
     [4,5,6], 
     [7,8,9]]

for i in range(len(l1[0])) :   # 1 2 3 
    l2=[] 
    for j in range(len(l1)):   # 0  3 
        l2.append(l1[j][i])   # l1[0][1]
    print(l2)                  # 1  4  7   
"""

# task :2 print rowise and col wise sum :  

"""
l1= [[1,2,3],    
     [4,5,6], 
     [7,8,9]]

1 row sum : 6 
2 row sum : 15
3 row sum : 24 
1 col sum : 12 
2 col sum : 15 
3 col sum : 18
"""

"""
for i in range(len(l1[0])) :   # 1 2 3 
    sum =0
    rowsum =0  
    for j in range(len(l1)):   # 0  3 
        sum =sum + (l1[j][i])   # l1[0][1] 
        rowsum =rowsum + l1[i][j]   # l1[0][1]
    print(sum)
    print(rowsum)
"""

# tuple : immutable  not changes  in tuple . 


"""t1=(1,2,3,4,5,6,7,8,9,10,"kishan",6j,True)

print(t1)
print(type(t1))

t2= 1,2,3,4,5,6,7,8,9,10,"kishan",6j,True
print(t2)
print(type(t2))
"""

# built in function  : len min max sorted sum 
"""
t1=(100,2,9,8,7,6,34,900)
print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))  # asc to dec
print(sum(t1))
"""
# slicing  : 

t1=(100,2,9,8,7,6,34,900)

# print(t1[4])

"""
t1[2] ="kishan"  error   bcz of  tuple is  immutable 
print(t1)  
"""
"""print(t1[2:5])
print(t1[2:6 :2])
print(t1[ : : -1])
"""

# method  : 
"""
t1=(100,2,9,8,7,6,34,100)

print(t1.count(100))
print(t1.index(2))
print(t1.index(100))
print(t1.index(100,1,9))  # 1 start index 9 end  index 
"""

# task  :1 
"""
input  : t1=(100,2,9,8,7,6,34,100)
output : t1=(100,2,9,8,7,6,34,100,"kishan")
"""
"""
t1=(100,2,9,8,7,6,34,100)

l2 =(list(t1))
l2.append("kishan")
print(tuple(l2))
"""

# mcq : 
"""
t1=(1,2,3,4,[67,89,90],99)
t[4].append("saloni")
print(t1) 

a.error   # r v a a   
b.(1,2,3,4,[67,89,90],"saloni",99)
c.(1,2,3,4,[67,89,90,"saloni"],99)   # c d d m  c c  
d.none 
""" 
t1=(1,2,3,4,[1,2,3],99)
#   0 1 2 3  4          5 

t1[4].append("saloni")
print(t1) 
# 1,2,3,4 ,99  ==> tuple    [1,2,3]


# raj    vidhya  kishan    rohit      dev    daksh   meet   
# pari   pratham  riya      param 