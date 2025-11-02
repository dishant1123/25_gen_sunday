# string  : immutable   ==> no changes in  original string ==> can  modify  

"""
s1="my name is rohit."
print(s1)
print(type(s1))
"""

# built in  function  :   len min max  sorted 
"""
s1="my name is rohit."

print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))
"""
# slicing  : 
"""
s1="my name is rohit."

print(s1[0])
print(s1[2:5])
print(s1[ :5])
print(s1[1 :])
print(s1[-1])
print(s1[3 :-5])
print(s1[-5 :-3])
print(s1[2 :8:2])
print(s1[  : :2])
print(s1[  : :-2])
print(s1[  : :-1])
"""
# task :1 
"""
input  :"dishant dipakkumar shah"
output :d.d.shah
"""

# task  :2 
"""
ask user to enter the two  string  and  interchange  the  first 3 characters of both  strings and print  the new  strings.

input  a : color 
input  b : full 

output a :fulor
output b : coll

"""

"""s1=input("enter the  string  1: ")  # color 
s2=input("enter the string  2 : ")  # full 

first = s2[0 :3] +s1[3:]
second =s1[0 :3] +s2[3:] 
print(first)
print(second)
"""

# method  : 

s1="My NAme is rohit."

"""print(s1.capitalize())
print(s1.upper())
print(s1.lower())
print(s1.title())
print(s1.casefold())
print(s1.swapcase())
"""
s2="happy diwali"
"""print(s2)
print(s2.center(50,"*"))
print(s2.ljust(50,"-"))
print(s2.rjust(50,"-"))
"""

# index , rindex , find , rfind  : 
s1="my name is rohit."

"""print(s1.index("m"))
print(s1.index("i"))
print(s1.index("i",9))
print(s1.index("name"))
print(s1.index("ame"))

print(s1.find("m"))
print(s1.find("i"))
print(s1.find("i",9))
"""

"""print(s1.rindex("m"))  # r to  l 
print(s1.rindex("m",0,4))  # r to  l  ==> 0 start index 4 end index number 

print(s1.rfind("i"))
print(s1.rfind("m"))
print(s1.rfind("m",0,4))
"""

# using  index r index : 

# task  :3 
"""
input : "i am going to goa next month." 
output  : o index 

"""
