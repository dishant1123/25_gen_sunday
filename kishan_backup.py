# loop  : 

# prime  , perfect , amg , rev, pelindrome , twin  ,strong   :
# twin number  : 
"""
123 : 
each digit  sum  = 1+2+3 =6
multiply  = 1*2*3 =6
"""
"""
n=int(input("enter the  number  : "))
sum =0 
mul =1 
temp= n
for i in range(len(str(n))):  #123  == >2 ,3    
    r = n %10    # r =1 %10 =1 
    sum =sum +r   # sum =5  +1 =6 
    mul = mul *r  # mul =6  
    n = n//10     # n =1 //10 =0 

if sum ==mul :
    print(temp,"is a twin number")

"""

# while  : 
"""n=int(input("enter the  number  : "))
sum =0 
mul =1 
temp =n
while  n >0 : 
    r= n %10  # r =1 %10 =1
    sum=sum +r  # sum =5  +1 =6
    mul=mul *r  # mul =6
    n=n//10

if sum ==mul :
    print(temp,"is a twin number")
"""

# strong number  :
"""
145 : 
each digit  : factorial  : 1! = 1   4! =24  5 !=120 
sum = 1+24 +120 =145   strong  number 

"""
