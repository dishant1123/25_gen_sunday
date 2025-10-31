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
# amg : 

"""n=int(input("enter the  number  : "))  # 1634 
sum = 0 
temp =n 
digit = len(str(temp))   #4
while temp > 0 :   # 1634 >0 
    r = temp %10   # r = 4 
    sum = sum + pow(r,digit)  # sum = 0 + 256 
    temp = temp //10   
if sum ==n :
    print(n,"is an amg number")
"""

# nested for  loop  : 
"""start = int(input("enter the start  : "))
end = int(input("enter the end  : "))


for i in range(start,end+1):  # 100  10000 
    digits = len(str(i))
    temp =i 
    sum =0 

    for j in range(digits):
        r= temp %10
        fact =1 
        while r >0 :
            fact =fact *r
            r-=1
        sum =sum +fact
        temp   = temp //10 
    if sum ==i :
        print(i,"is a strong number")
"""
# pattern  : 

"""
1.          2.          3.            4.          5.           6. 

* * * * *   *           * * * * *     1           5 4 3 2 1    1 2 3 4 5  
* * * * *   * *         * * * *       1 2         5 4 3 2      2 3 4 5 
* * * * *   * * *       * * *         1 2 3       5 4 3        3 4 5 
* * * * *   * * * *     * *           1 2 3 4     5 4          4 5
* * * * *   * * * * *   *             1 2 3 4 5   5            5 
"""

# 1: 
"""
for i in range(5):  
    for j in range(5):
        print("*",end=" ")
    print()
"""
#2: 

"""
for i in range(1,6):  
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
#3: 
"""
for i in range(5):  
    for j in range(5,i,-1):
        print("*",end=" ")
    print()
"""
#4 : 
"""for i in range(1,6):  
    for j in range(i,6):
        print(j,end=" ")
    print()
"""

"""
5. 
a 
a b 
a b c 
a b c d 
a b c d e
"""
#5 :
"""
ch='a'
for i in range(1,6): 
    for j in range(i):
        print(chr(ord('a')+j),end=" ")
    print()
    
"""

"""
6:          7 :         8:         9: 

* * * * *  * * * * *         *       * 
  * * * *   * * * *        * *      * * 
    * * *    * * *       * * *     * * * 
      * *     * *      * * * *    * * * * 
        *      *     * * * * *   * * * * * 
"""

# 6: 
"""for i in range(1,6):
    for k in range(1,i): 
        print(" ",end=" ") 
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()
"""
# 7 : 
"""
for i in range(1,6):
    for k in range(1,i): 
        print(" ",end="") 
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()
"""

# 8: 
"""
for i in range(1,6): 
    for k in range(5,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""

#9: 
"""
for i in range(1,6): 
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""

# 10 : full pyramid

"""for i in range(1,6): 
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,6):
    for k in range(1,i): 
        print(" ",end="") 
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()
"""


# 11 :        12 :       13 :           14 : 
"""
* * * * *     *            * * * * *         *
*       *     * *          *     *          * * 
*       *     *   *        *   *           *   * 
*       *     *     *      * *            *     * 
* * * * *     * * * * *    *             * * * * *
"""

#11 : 
"""for i in range(5):  
    for j in range(5):
        if i==0 or i==4  or j==0 or j==4 :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
"""

#12 : 
"""
for i in range(1,6):  
    for j in range(1,i+1):
        if j==1 or i ==5 or i==j:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
"""

#13 : 

"""
for i in range(5,0,-1):  
    for j in range(1,i+1):
        if i==1 or j==1 or i==j or i==5:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
"""

# string  : immutable  ==> no change in  string  . 

"""
s1="my name is kishan."
print(s1)
print(type(s1))
"""

# built in function  : len min max sorted sum 

"""
s1 = "my name is kishan."
print(len(s1))
print(min(s1))  # ascci value  
print(max(s1))  # ascci value
print(sorted(s1))  # list
"""

# slicing  : 
s1 = "my name is kishan."
#index: 012     
"""
s1[0] ="patel"
print(s1)  # immutable  not changes in string 
"""
"""print(s1[0])
print(s1[2])
print(s1[2 :5])

print(s1[ :9])
print(s1[2 :])  # l to r 

print(s1[-2])  # r to  l 
print(s1[-5 :-1])
print(s1[5 :-1])
print(s1[-5 :1]) # no  output 

print(s1[1 :10 :2])
print(s1[  :  :-1])
"""

# method : 

s1="my name is kishan."

"""print(s1.capitalize())
print(s1.lower())
print(s1.upper())
print(s1.title())
print(s1.casefold())
print(s1.swapcase())
"""

"""s2="happy diwali"
print(s2.center(50,"*"))
print(s2.rjust(50,"*"))
print(s2.ljust(50,"*"))
"""
"""print(s1.count("i"))
print(s1.count("i",10,20))
"""

# task  :1 
"""
input  : dishant dipakkumar shah 
ouptut : d.d.shah
"""

# task :2 
"""
ask user  to enter the two string and swap the  first three character of second  string with first three character of first string. 

input  a : color 
input  b : full 
output a : fulor 
output b : coll
"""

# index ,find  : 

s1="my name is kishan."

"""print(s1.index("i"))
print(s1.index("a"))
print(s1.index("name"))
print(s1.index("ame"))
print(s1.index("a",5,20))

print(s1.find("i"))
print(s1.find("a"))
print(s1.find("name"))
print(s1.find("ame"))
print(s1.find("a",5,20))"""

# rindex , rfind  : r to l  ==> pos 
print(s1.rindex("a"))
print(s1.rindex("i"))
print(s1.rindex("a",2,15))

print(s1.rfind("a"))
print(s1.rfind("i"))

# task  :3 
"""
input : i am going to goa next month. 
ouptut : first "o" index number is  :6
        second "o" index number is  :12
        third "o" index number is  :15
        fourth "o" index number is  :24

"""