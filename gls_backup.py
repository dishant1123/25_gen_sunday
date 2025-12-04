# loop  : 
"""
1. for loop  
2. while  
3. while  True 
"""
"""
for loop  :

syntax : 

for variable name in range(start , stop , step) :
    print(variable name)
"""

#1-100 : 

"""
for i in range(1,100):  # start ==> 1 , stop  ==>100 
    print(i,end=" ")
"""

#100- 1 : 

"""for i in range(100,1,-1):
    print(i,end=" ")
"""

"""for i in range(1,101,3):  # start ==> 1 , stop  ==>100 
    print(i,end=" ")
"""

# user  : start  ,end 

"""a=int(input("enter the  number  :"))
b=int(input("enter the  number  :"))

for i in range(a,b+1,2):
    print(i,end=" ")
"""

# prime : 
"""
2 factors  : 

5 ==> 1,5 
4 ==>1,2,4  
"""
"""n=int(input("enter the  number  :"))  # 4 
count =0 
for i in range(1,n+1):  # 4, 5 
    if n % i ==0 :   # 4 %4 ==0 
        count +=1   # 3
if count ==2 :
    print(n,"is a prime number")
"""

# break , contunie , pass : 

"""for i in range(1,10):
    if i==5 :
        break
    # print(i,end=" ")
print(i)

"""

"""
for i in range(1,10):
    if i==5 :
        continue
    print(i,end=" ")
    # print(i)

"""

"""for i in range(1,10):
    if i==5 :
        pass
    print(i,end=" ")
"""
# print(i)

"""def add():
    pass 
"""

#amg : 
"""
built  in function  :  len min max sorted sum 
"""
"""
s1=122342345678
print((len(str(s1))))  # "12234
"""

#logic : 
""" 
3 digit    153 
temp =n 

while  temp >0 :
    r = temp %10 
    sum =sum +pow(r,digit)
    temp = temp //10 
"""

"""
n=int(input("enter the  number  :"))
digit= len(str(n))
sum =0 
temp =n 
for i in range(digit) :  # 4
      r = temp %10
      sum =sum +pow(r,digit)
      temp = temp //10
if sum ==n :
    print(n,"is a amg number")
"""
# print  1-1000000 amg  print  . 

"""start =int(input("enter the start : "))
end =int(input("enter the end : "))

for i in range(start,end+1):  #1-100000
    sum =0 
    digit =len(str(i))
    temp =i
    for j in range(digit):
        r=  temp %10 
        sum =sum +pow(r,digit)
        temp = temp //10 
    if sum ==i :
        print(i,end=" ")
"""

# pattern  : 

"""
1.         2.         3.         4.

* * * * *  *          * * * * *  1 2 3 4 5
* * * * *  * *        * * * *    2 3 4 5
* * * * *  * * *      * * *      3 4 5
* * * * *  * * * *    * *        4 5
* * * * *  * * * * *  *          5

"""
#1 :
"""for i in range(1,6):
    for  j in range(1,6):
        print("*",end=" ")
    print()
"""    
#2: 

for i in range(1,6):
    for  j in range(1,i+1):
        print("*",end=" ")
    print()
