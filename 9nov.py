# diff find , index : 
s1="my name is rohit thakkar."

# print(s1.find("z"))
# print(s1.index("z"))

"""s2="rohit12"
print(s2.isalnum())  # a to z or  number 

s3="rohiT@"
print(s3.isalpha())  # a to  z chareacter 
"""
# isdigit  : 

"""s4="1234"
print(s4.isdigit())  # number   only  number  0-9  ==>10²  ==> true 

s5="12345a6"
s6="10²"
s7="½"
# print(s5.isdecimal())
print(s7.isdecimal())


s8="12345"    # or : ==>10²  ==> true  "½" ==> true  "XIV" ==> true 
print(s8.isnumeric())
"""
# join  : 

"""l1=["my","name","is","rohit"]
# my name is  rohit. 
s9=" ".join(l1)
print(s9)
"""

# removeprefix, removesuffix :

"""
s10 ="my name is kiran."

print(s10.removeprefix("my"))
print(s10.removesuffix("."))
"""

# startwith , endswith :
s10 ="my name is kiran."

"""print(s10.startswith("my"))
print(s10.startswith("my "))
print(s10.startswith("my n"))
print(s10.startswith("My"))

print(s10.endswith("."))
print(s10.endswith("kiran."))
print(s10.endswith(" ."))
"""
# mcq : 
"""
S = "1234567890"
S = S[-3] + S[2:4] + S[-2:-5] + S[ : -4:-2] + S[1: :2]
#   8     + 34     + +0 8  + 24680  ==> 8340824680
print(S[ : : 3] * 2)8040  
"""
"""
a.80408040   # p t d d  c  a a 
b.86068606   # r 
c.14701470
d. None    # r 
"""
"""
task :1 Write a Python program to check if a string is palindrome or not. 
task  :2 Write a Python program to Find length of a string in python.
task :3  Write a Python function to find length of a string in python without using len function. 
task:4 Write a Python function that accepts a string and calculate the number of uppercase letters and lowercase letters.
"""

"""
task  :5 
Write a program to remove I'th character from string in python. 
Enter a string: python
Enter the index (position) to remove: 2
String after removing character: pyhon
"""

"""s=input("enter the string  : ")
word_index=int(input("enter the index : "))

# my name is  chahat.
l1 =list(s)
l2 =l1.pop(word_index)
l3 ="".join(l1)
print(l3)

"""

# task  : 6 
"""
Write a program to calculate the sum and average of the digits present in a string. 
input  : py123th5on9 
Sum of digits: 20
Average of digits: 4.0
""" 

# task  :7 
"""
Write a Python program to capitalize the first and last character of each word in a string.
input  : welcome to python
output : WelcomE TO PythoN 
"""

# task  :8 
"""
Write a python program to check the validity of a Password.
 Primary conditions for password validation:
 1. Minimum 8 characters.
 2. The alphabet must be between [a-z]
 3. At least one alphabet should be of Upper Case [A-Z]
 4. At least 1 number or digit between [0-9]
 5. At least 1 character from [ _ or @ or $]
 Examples:
 Input: Ram@_f1234
 Output: Valid Password
 
 Input: Rama_fo$ab
 Output: Invalid Password
 Explanation: Number is missing
 
 Input: Rama#fo9c
 Output: Invalid Password
 Explanation: Must consist from _ or @ or $
"""

