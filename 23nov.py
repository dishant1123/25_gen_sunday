# lambda  : one  liner  function  . 
"""
syntax : 

lambda arg : expression 
"""

# function  : 
"""
def addition(a,b):
    return a+b
print(addition(12,23)) 
"""
# lambda  : 

"""x =lambda a,b : a+b
a=int(input("enter the a  value :"))
b=int(input("enter the a  value :"))
print(x(a,b))
"""

# lambda using built in function  : len min max sorted sum 

"""a= lambda x : sum(x)
print(a("my name is  krithik."))
print(a([19,2,3,4,50,6]))
print(a((17,2,3,4,5,6)))
"""
# conditional  statement  : 

"""def x(a,b):
    if a>b :
        return a
    else :
        return b
print(x(12,45))
"""
"""
x =lambda a,b : print("a is big",a)if a>b else print("b is big",b) 
x(45,78)
"""

# using  for  loop  : 

# ex :1 
"""l1=[] 
for i in range(5): 
    l1.append(lambda x , i=i : x+i) 
    
for j in l1 :
    print(j(10))
    
"""

# ex :2 

# l1= [1,2,3,4,5]  

"""square = lambda x : x *x 
for i in l1 :
    print(square(i))
"""    
"""even = lambda x : x%2==0 
for i in l1 :
    if even(i) :
        print(i)
"""
    
# filter : 
"""
excel  : 
phonpe  ==> history  ==> trans ==> june   
"""
"""
l1=[1,2,3,4,5,6,7,8,9]
even =[] 
odd =[] 

for i in l1 : 
    if i %2 ==0 : even.append(i)
    else : odd.append(i)
print(even)
print(odd)
"""
# filter  ==> lambda  : 
"""
l1=[1,2,3,4,5,6,7,8,9]

a=tuple(filter(lambda x : x %2 ==0,l1)) 
b=list(filter(lambda x : x %2 ==1,l1)) 
print(a)
print(b)
"""
# map : change  the  value  of  a  list

"""
l1=[1,2,3,4,5,6,7,8,9]
l2=[]
for i in l1 :
    l2.append(i*i) 
print(l2)
"""
"""l1=[1,2,3,4,5,6,7,8,9]
a=tuple(map(lambda x : x *x,l1)) 
print(a)

"""

# task  :1  sort the  below  list for second  value .
"""
input  : [[1,2],[2,0],[4,1]] 
output : [[2,0],[4,1],[1,2]]
"""

"""
l1 = [[1,2],[-2,0],[4,1]]
l1.sort(key =lambda x :x[1])
print(l1)
"""

# reduce  : 

from  functools import reduce 

# sum of all elements : 

"""
numbers =[1,2,3,4,5,6,7,8,9]

result =reduce(lambda x ,y : x +y ,numbers)
multiply = reduce(lambda x ,y : x *y ,numbers)
print(result)
print(multiply)
"""

# find maximun value to list  without using  built in function max 

"""max_n =0 

for i in l1 : 
    if i > max_n : 
        max_n =i 
print(max_n)
"""
"""l1=[5,12,3,8,7]

max_n= reduce(lambda a,b : a if a>b else b ,l1)   
print(max_n)
"""

#  ex :4 

# s1 = ["my","name", "is","chahat"] 
# my name is chahat

"""x= reduce(lambda x,y : x +" "+y,s1)
print(x)
"""
# print(" ".join(s1))

"""
1. Write a Python program to sort a list of tuples using Lambda.

Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

2. Write a Python program to sort a list of dictionaries using Lambda.

Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}] 

3. Write a Python program to filter the height and width of students, which are stored in a dictionary using lambda.

Original Dictionary:
{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
Height> 6ft and Weight> 70kg:
{'Cierra Vega': (6.2, 70)}

4. Write a Python program to remove all elements from a given list present in another list using lambda.

Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]
Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]

5. Write a Python program to reverse strings in a given list of string values using lambda.

Original lists:
['Red', 'Green', 'Blue', 'White', 'Black']
Reverse strings of the said given list:
['deR', 'neerG', 'eulB', 'etihW', 'kcalB'] slicing  

"""