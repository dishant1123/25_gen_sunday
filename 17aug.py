# 8. What is the output of the following for loop and  range() function
"""for num in range(-5,2,2):
    print(num, end=", ")
"""
"""  a 
a.-2, -1, -3, -4     ==> 
b.-2, -1, 0, 1, 2, 3, ==> 
c.-2, -1, 0      ==> 
d.-2, -3, -4,   ==> r h p r c  d d  t  m p  v  d 


"""
# 11. What will be the output of the following Python code?
"""
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print(0)
"""
""" c 
a. 0 1 2 3 0 
b. 0 1 2 0   ==> p h r r c t d d v p  
c. 0 1 2    
d. error ===> 
"""
# 13.What will be the output of the following Python code?
"""
for i in range(10):
    # if i == 5:
        # break
    # else :
    print(i)
else:
    print("Here")
"""
"""
a. 0 1 2 3 4 Here  ==> r r c d p r v
b. 0 1 2 3 4 5 Here  ==>  h p 
c. 0 1 2 3 4   ==>  t d 
d. 1 2 3 4 5   ==> 

"""

"""for i in range(10):
    if i==5 :
        break
    else :
        print(i)  
"""

# prime  : 
# 2 factors : 1, num it self 
"""
n=int(input("enter the  number  : "))
count =0  

for i in range(1,n+1): 
    if n % i ==0 :
        count +=1    # 
if count ==2 :
    print(n,"is a prime number")

"""

# armstrong number  : 
"""
153 : 3 digit 

1 **3  5 **3  3**3 
1      125     27 
sum = 1+125 +27 =153   amg 

1634 : 4 digit 

1**4  6**4  3**4  4**4
1     1296  81    256 
sum = 1634  amg 


"""
# built in function  : len  min  max sorted  sum 

"""n =int(input("enter the  number  : "))  # 153 
digit = len(str(n)) 
temp=n 
sum=0
for i in range(digit):  # 
    r =temp % 10  
    sum =sum +pow(r,digit)
    temp  = temp  // 10 

if (sum==n):
    print(n,"is an armstrong number")
else :
    print(n,"is not an armstrong number")
"""

# twin number  : 
"""
123 ,22: 

each digit sum = 1+2+3 =6 
each  multiply =1*2*3 =6 
sum == mul   ==> twin  number  
"""

# strong number :   145 : 
n=int(input("enter the number  : "))
digit=len(str(n))
temp =n   #temp =145 
sum= 0 
for i in range(digit):
    r=  temp %10      # r = 1 %10 =1 
    fact =1  # fact =1  
    for j in range(1,r+1):   #1!=0 
        fact = fact *j    # fact=1    
    sum =sum +fact   # sum = 144  +1 =145 
    temp  =  temp //10   # temp = 1  //10 =0  
if sum ==n : 
    print(n,"is a strong number")
else :
    print(n,"is not a strong number")

# next :  nested loop  ,  pattern  