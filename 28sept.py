# index , rindex , find , rfind : 

s1="my name is rohit thakkar."
# index method  : l  to r 
"""
print(s1.index("r"))
print(s1.index("a"))
print(s1.index("a",5,20))  # 5 index number end  20  end index number  
print(s1.index("a",20,30))  # 20 index number end  30  end index number 

print(s1.index("name"))
print(s1.index("ame"))
"""
# r  to  l :
"""
print(s1.rindex("a"))
print(s1.rindex("rohit"))
print(s1.rindex("a",6,20))
"""
# find : index number  
"""print(s1.find("r"))
print(s1.find("a"))
print(s1.find("a",5,20))  # 5 index number end  20  end index number  
print(s1.find("a",20,30))  # 20 index number end  30  end index number 

"""
"""print(s1.rfind("a"))
print(s1.rfind("rohit"))
print(s1.rfind("a",6,20))
"""

# spilt  , rspilt , partition , rpartition :

s1="my name is rohit thakkar."

"""print(s1.split())
print(s1.split("a"))
print(s1.split("name"))
"""
# hw :  diff between split and rsplit ==> 
"""print(s1.rsplit("a"))
"""

"""
print(s1.partition("a"))  # string divide into 3 parts
print(s1.partition("rohit"))  

print(s1.rpartition("a"))  
print(s1.rpartition("k"))
"""  

# task :1 
"""
print all "o" index number .
input  : "i am going to goa next month."

ouput  : first  o index number  :6 
         second  o index number  :12
         third  o index number  :15 
         fourth  o index number  :24
"""