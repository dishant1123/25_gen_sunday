#1 : 
"""a = [10, 20]
b = a # swapping  == > shallow  copy ==> numpy 
b += [30, 40]
print(a)
print(b)
"""
"""
a=[10,20]
b =a.copy()  # list   ==> deep copy 
b+=[30,40]
print(b) 
print(a)"""

"""a= [1,2,3,4]
a.append([5,6])
print(len(a))
"""

"""i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        pass
else:
    print(0)"""
# 0 1 2 4 0  ==>raj , T , C , R  

"""for num in range(-5,-2,0): # -2 start  stop  step : default  : +1   
    print(num, end=", ")  # -5 
"""
# -5+1 -4
# start  con     
"""
for i in range(0,5):
    print(i) 
"""
"""
           -7 -6 -5 -4  -3  -2 -1  0   1 2 3 4 5 6 7 8 9
"""

"""
sytax : 

i =intial  value  

while (con) : 
    print () 
    assignemnt  i+=1 
"""

"""
i=-5 
while i <-2 :
    print(i)
    i+=1    
"""

"""tup = (1, 2, (3, 4, (5, 6)))

#     0   1  2 
print(tup[2][2][1])
"""

# string  :  immutable   ==> no changes  in string . 

"""
s1= "my name is rohit."
print(s1)
print(type(s1))

"""
# built in function  :  len min max sorted sum 
"""
s1= "my name is rohit."

print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))
"""

# slicing  : 
s1= "my name is rohit."

"""s1[2] ="sharma"
print(s1)
"""
"""
print(s1[3])
print(s1[2 :5])
print(s1[-2])
print(s1[2 : 8 :2])
print(s1[  :  :2])
print(s1[  :  :-2])
print(s1[  :  :-1])
"""

# task  : 1 
"""
input  : dishant dipakkumar shah 
output  : d.d.shah

"""
# task :2 
"""
ask user to enter the  2  string  and swap  the  first  3 letter. 
input  1 : color 
input  2 : full

output 1 : fulor 
output 2 : coll

"""

"""
s1=input("enter the string  1 :")  # color 
s2= input("enter the  string  2 :") # full 

modify_string = s1[ : 3]  +s2[3 :] 
modify_string2 = s2[ :3]  +s1[3 : ]
print(modify_string)
print(modify_string2)

"""

# method  : 
s1= "my Name Is Rohit."

# case related method  : 
"""print(s1.capitalize())
print(s1.upper())
print(s1.lower())
print(s1.title())
print(s1.casefold())
print(s1.swapcase())
"""

s2="happy diwali"
"""
print(s2)
print(s2.center(100,"="))
print(s2.ljust(100,"="))
print(s2.rjust(100,"="))
"""
