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

# dict : mutable  ==> key value  pair  ==> changes in dict 

"""
d1={"phy":90 ,"maths":99}
# phy ==> key value  ==> 90   maths ==> key  value  ==> 99  

print(d1)
print(type(d1))

d2={90 :78,89 :"chahat"}
print(d2)
print(type(d2))
"""

# add in dict : 

"""
d1={"phy":90 ,"maths":99}
d1["com"] =89 
print(d1)
"""

# built in function  : len min max sorted sum

"""d1={"45":90 ,"maths":99}

print(len(d1))
print(min(d1))
print(max(d1))
print(sorted(d1))  #asc to desc
print(sorted(d1,reverse=True))  # desc to asc
"""
# slicing  : 

"""
d1={"phy":90 ,"maths":99}

print(d1[0])  # not  possible in dict 
"""
# method  : 

d1={"phy":90 ,"maths":99,"com":89}

# d1.clear()
# print(d1)

# d2= d1.copy()
# print(d2)

# print(d1.get("phy")) 

# print(d1.keys())
# print(d1.values())
# print(d1.items())

"""l1=["honey","chahat"]
# {"honey":100,"chahat":100}

d2 =dict.fromkeys(l1,100)
print(d2)

d2["honey"]=200 
print(d2)
"""

"""d1.pop("phy")
print(d1)
"""

"""d1.popitem()  # last key value  remove in pop item. 
print(d1)
"""
"""d1={"phy":90 ,"maths":99,"com":89}

d2={"phy":23 ,"maths":56,"com":88,"eng":77}

d1.update(d2)
print(d1)
"""
"""
d1={"phy":90 ,"maths":99,"com":89}

d1.setdefault("s.s",99)
print(d1)
"""

# task  :1 
"""
ask user  to enter the name and marks and store in to the dict. 

ram 90  sita 89  ravan 88 
output  : {"ram":90,"sita":89,"ravan":88}

"""
"""n=int(input("enter the  number  :"))
d1={}
for i in range(n):
    name =input("enter the  name  :")
    marks =int(input("enter the  marks  :"))
    d1[name] =marks 
print(d1)  #{'ram': 89, 'sita': 56, 'ravan': 99} 
"""
#task :2 above  dict sorted in basic of  marks . 
#output : {"sita":56,"ram":89,"ravan":99,}

"""sorted_marks = sorted(d1.values())  # [56 ,89 , 99] 
d2={}
for i in sorted_marks:  # [56 ,89 , 99]
    for  j ,k in d1.items():#{'ram': 89, 'sita': 56, 'ravan': 99} 
        if i==k :
            d2[j]=k
print(d2)

"""

# task :3 
"""
input  : "missippissi"
output  : {"m":1,"i":4,"s":4,"p":2}

"""


# set : mutable , unordered collection of unique elements , no duplicate elements

"""
s1={1,2,3,3,4,5,6,7,7,8,9,10,7j}
print(s1)
print(type(s1))
"""
# empty set : 

"""s2= set()
print(s2)
print(type(s2))
"""

# built in function  : len min max sorted sum
"""
s1={100,2,3,3,4,5,6,7,7,8,9,10,900}

print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))  #asc to desc
print(sorted(s1,reverse=True))  # desc to asc
print(sum(s1))
"""
# slicing : not possible in set  bcz of unordered collection. 

# s1={10,2,3,3,4,5,6,7,7,8,9,10,900}

# s1.add(290)
# print(s1)

# s1.clear()
# print(s1)

# s2 =s1.copy()
# print(s2)

# s1={1,2,3,4}
# s2={2,4,7,8}
# s3={1,2,3,4,5,6,7,8,9,10}

# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2)) # s1-s2 

# print(s1.symmetric_difference(s2))

"""print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)
"""

"""print(s1.difference(s2))
print(s1)
s1.difference_update(s2)
print(s1)
"""

"""s1.symmetric_difference_update(s2)
print(s1)
"""

# subset , superset , disjoint : 

# s1={1,2,3,4}
# s2={2,7,8}
# s3={1,2,3,4,5,6,7,8,9,10}

# print(s1.isdisjoint(s2))
# print(s3.issuperset(s2))
# print(s2.issubset(s3))

s1={10,2,3,3,4,5,6,7,7,8,9,10,900}

# s1.pop()
# print(s1)

# s1.discard(9000)
# print(s1)

# s1.remove(9000)
# print(s1)

# s2={"honey","chahat","raj","pratham"}
# s1.update(s2)
# print(s1)


# frozenset : immutable , unordered collection of unique elements , no duplicate elements

"""
fz =frozenset({1,2,3,3,4,5,6,7,7,8,9,10,900})
print(fz)
print(type(fz))
"""

# function  : 
"""
type  : 
1. no arg no return 
2. no arg  with return 
3. with arg  no return 
4. with arg  with return
"""
#1 : 
"""def add():  # add ==> funcation  
    a=10 
    b=90     # func intial part 
    c=a+b
    print(c)
add()   # call 
add()
"""

# 3 : 
"""def add(a,b=0):
    c=a+b
    print(c) 
add(12)
add(12,90)
# add("yug","shah")
"""

#2 :
"""def add():
    a=int(input("enter the  number  : "))
    b=int(input("enter the  number  : "))
    c = a+b
    return c  
print(add())
"""
#4 : 
"""def add(a,b):
    return a+b
print(add(12,78))
"""

# local variable  :

"""def x():
    a=100   # local variable 
    print(a)
x()
# print(a)  # not accessible  outside the  function 
"""

# global variable  : 

"""
x=100   # global variable
def a():
    print(x)
a()
print(x)  # accessible  outside the  function bcz of global variable
"""

# modify global variable  :

"""x=100 
def y():
    global x 
    x=900 
    print(x)
y()
print(x)    
"""

# *args : only take num arg. 

"""
def add(*args):
    return sum(args)
print(add(12,90,78,56,45,34,2,14,7,0,78.90,8j,True))
"""

# loop  : 

"""def y(*x):
    sum =0 
    for i in x :
        sum =sum +i 
    print(sum)
y(1,2,3,4,5,6,7,8,9,10)
"""

# **kwargs : 

"""def t(**kwargs):
    for i ,j in kwargs.items():
        print(f"{i} = {j}")
t(name="honey",age=19,clg="GLS")
"""

# amg  using  function  ==> with arg  with return 