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

# count  : 

s1="my name is rohit thakkar."

"""print(s1.count("a"))
print(s1.count("a",6))  # 3 arg  :  letter  strart stop  
"""

# spilt  ,  rspilt , partition , rpartiton : 

s1="my name is rohit thakkar."
"""
print(s1.split())  # list 
print(s1.split("a"))
print(s1.split("is"))

print(s1.rsplit("a"))
print(s1.rsplit("is"))
"""
# hw  : diff between split  and  rspilt : 

"""print(s1.partition(" ")) # tuple  ==> 3 part
print(s1.partition("r")) 
print(s1.partition("a")) 

print(s1.rpartition("a"))
"""

# task  :4 
"""
Write a python program that take one input string and in output count the no of words,
Find No of letters in String,Find the longest word in the String.
For Example:-
Input:-This is the python program
Output:-No of Words=5
	    No of letters=26(including whitespace)
	    Longest Word=program
"""
"""
s1="This is the python program"

split_string  = s1.split()  # ['This', 'is', 'the', 'python', 'program']
longest_word =max(split_string,key=len) 
print(longest_word)
"""
# key =   ==> buit  in function  ==> len min max sorted 
"""
longest_wrod =""   
for i in split_string:  # ['This', 'is', 'the', 'python', 'program'] 
    if len(i)  > len(longest_word) :
        longest_word =i 
print(longest_word)
"""