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
