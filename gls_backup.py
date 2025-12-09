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

"""
for i in range(1,6):
    for  j in range(1,i+1):
        print("*",end=" ")
    print()
"""

#5 :         6 :         7 :  
""" 
* * * * *          *        * 
  * * * *        * *       * * 
    * * *      * * *      * * *
      * *    * * * *     * * * *
        *  * * * * *    * * * * *  
"""
# 5 :

"""for i in range(1,6):  # 2 
    for k in range(1,i):  # 1,2
        print(" ",end=" ")
    for j in range(5,i-1,-1): # 5 ,1 ,-1 
        print("*",end=" ")   # * * * * * 
    print()                  #   * * * * 
"""   
# 8 : 
"""
for i in range(1,6):  # 2 
    for k in range(1,i):  # 1,2
        print(" ",end="")
    for j in range(5,i-1,-1): # 5 ,1 ,-1 
        print("*",end=" ")   # * * * * * 
    print()                  #   * * * * 
"""

# 6 :
"""for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end=" ")
    for  j in range(1,i+1):
        print("*",end=" ")
    print()
"""

# 7 :
"""
for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end="")
    for  j in range(1,i+1):
        print("*",end=" ")
    print()

"""

# diamond : 
"""for i in range(1,5):
    for k in range(5,i,-1):
        print(" ",end="")
    for  j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,6):  # 2 
    for k in range(1,i):  # 1,2
        print(" ",end="")
    for j in range(5,i-1,-1): # 5 ,1 ,-1 
        print("*",end=" ")   # * * * * * 
    print()                  #   * * * * 
"""
"""
* * * * *  
*       *
*       *
*       *
* * * * *
"""

"""for i in range(1,6):
    for j in range(1,6):
        if i==1  or i==5  or j==1 or j==5:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
"""

#  
"""
1. string   
2. list 
3. tuple  
4. dict 
5. set 
"""

# list  : mutable  sequence element ==> change in list 

"""
l1=[1,2,3,4,5,45+9j,"chahat",89.45]

print(l1)
print(type(l1))
"""

# built in function  : len min max sorted sum 

"""
l1=[1,2,3,4,5,89.45,0]

print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1))  #asc to desc 
print(sorted(l1,reverse=True))  # desc to asc  
print(sum(l1))
"""

# slicing  :
l1=[10,20,30,40,50,89.45,123,89,77]
# index start  pos : 0   ==> l to r   
# negative index : -1    ==> r to l 

"""l1[4] ="chahat"
print(l1)
"""

"""print(l1[3])
print(l1[2:6]) # start index 2  end index 6 
print(l1[ :7])
print(l1[2 :])
print(l1[-2])
print(l1[-5 :-2])
print(l1[-2 :-5])

print(l1[2 :6 :2])
print(l1[ : :2])
print(l1[ : :-1])

print(l1[-2 :-5 :-1])
"""

# method  : 

l1=[10,20,30,40,50,89.45,123,89,77,123]

# l1.append(234)
# print(l1)

# l1.clear()
# print(l1)

# l2 =l1.copy()
# print(l2)

# l1.insert(3,"pratham")
# print(l1)

# l1.remove(77)
# print(l1)

# l1.pop(2)
# print(l1)

# print(l1.count(123)) 

"""print(l1.index(123))
print(l1.index(123,7,20))

"""

"""l2=["saumya","pratham","chahat","honey"]

l1.extend(l2)
print(l1)
"""
"""l1.reverse()
print(l1)
"""
"""l1.sort()
print(l1)

l1.sort(reverse=True)
print(l1)
"""

# task 1 : 

"""
ask user to enter the  number  and  store in to the list  and print  odd even sum of  
list element. 
"""
"""n=int(input("enter the  number  :"))
l1=[] 

for i in range(n):
    ele =int(input("enter the  ele  :"))
    l1.append(ele)
print(l1)  # l1 =[1,2,3,4,5]
eve =0 
odd =0 
for i in l1 :
    if i % 2==0:
        eve +=i 
    else :
        odd +=i
print(eve,odd)

"""

#task  :2 
"""
ask user to enter the  number  and  store in to the list  remove  duplicate element in to list. 
user =7 
l1=[1,1,2,2,3,4,5] 
output  : [1,2,3,4,5]
"""
# tuple : immutable  sequence element ==> not change in tuple

"""
t1=(102,2,3,4,5,6,7,8,9,10)
print(t1)
print(type(t1))

t2=12,23,45,678,789,"raj"
print(t2)
print(type(t2))

t3="",
print(t3)
print(type(t3)) 
"""

# built in function  : len min max sorted sum 

"""
t1=(102,2,3,4,5,6,7,8,9,10)
print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))  #asc to desc
print(sorted(t1,reverse=True))  # desc to asc
print(sum(t1))
"""

# slicing  : 

# t1=(102,2,3,4,5,6,7,8,9,10)

"""t1[4] ="chahat"
print(t1)
"""

"""print(t1[3])
print(t1[2:6]) # start index 2  end index 6
print(t1[ 2:7 :2])
print(t1[ : :-2])
print(t1[ : :-1])
"""

# method  : 

"""t1=(102,2,3,4,5,6,7,8,9,10,2)

print(t1.count(2))
print(t1.index(2))
print(t1.index(2,2,20))

"""

# mcq : 

"""t1 =(102,2,3,[4,5,6,7],8,9,10)
#    0   1 2  3 
t1[3]="raj"
print(t1)
"""
"""
a. error   # p ,r
b. (102,2,3,[4,5,6,7],"raj",8,9,10)
c. (102,2,3,[4,5,6,7,"raj"],8,9,10)  # r , h ,v ,c  ,p 
d. (102,2,3,["raj",4,5,6,7],8,9,10)  # y 
"""
# task  : 1 
"""
input  : t1=(102,2,3,4,5,6,7,8,9,10)
output : t1=(102,2,3,4,5,6,7,8,9,10,"honey")
"""

# task  :2  add value in last index .

"""
input  : t1=[(1,2,3),(4,5,6),(7,8,9)]
output : t1=[(1,2,100),(4,5,100),(7,8,100)]
"""
# hw : 
"""
task : 7 Write a Python program to get the second largest number from a list.
	input  : [1,2,3,4,10,9,6,7]
	output : 9

task : 8 
	Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.  count Return True otherwise False.
	Input:
	[19, 19, 15, 5, 3, 5, 5, 2]
	Output:
	True
	Input:
	[19, 15, 15, 5, 3, 3, 5, 2]
	Output:
	False
	Input:
	[19, 19, 5, 5, 5, 5, 5]
	Output:
	True
task : 9 
	Write a Python program that accepts a list of integers and calculates the length and the 
	fifth element. Return true if the 
	length of the list is 8 and the fifth element occurs thrice in the said list.
	Input:
	[19, 19, 15, 5, 5, 5, 1, 2]
	Output:
	True
	Input:
	[19, 15, 5, 7, 5, 5, 2]
	Output:
	False
"""


# dict : 
