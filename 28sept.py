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

# replace : 

"""s1="my name is is rohit thakkar."

print(s1.replace("is"," "))
print(s1.replace("is"," ",1))
print(s1.replace("is"," ",2))
print(s1.replace("is"," "))
"""

# task  : 2 
"""
second "r" replace with "@"
input :  restart 
output : resta@t

"""
#task  :3 
"""
ask user to enter the string  replace the firs space with "_" and  last space  with "_". 

input  : my nam is yash patel. 
output : my_name is yash_patel.

"""

"""
s1="my name is yash patel."

modify_string =s1.replace(" ","_",1)[: : -1].replace(" ","_",1)[ : : -1]
print(modify_string)
"""

s2="my name is yash patel."

"""print(s2.count("a"))
print(s2.count("a",5,20))
"""

# task  :4 
"""
input : i love python programming language.

output  : count of letter :35 
          count of words : 5 
          longest word: programming  
"""
"""
s3="i love python programming language."
count_letter= len(s3)
count_words = len(s3.split())  # ["i","love","python","programming","language."] 
logest_word =max(s3.split(),key=len)

print("count of letter :",count_letter)
print("count of words :",count_words)
print("longest word :",logest_word)

"""

