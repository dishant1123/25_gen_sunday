"""
python data type  : 

1. list : mutable  sequence   ==> changes in list 
2. string  : immutable  ==> not changes  in string 
3. tuple : immutable  sequence  ==> not changes in tuple
4. dict : mutable  key value pair  ==> changes in dict
5. set : mutable  unordered collection  ==> changes in set
"""

# list  : mutable  sequence 
"""
int a[50] ={1,2,3,4,5}
index : 
"""
l1=[10,20,30,40,50,60,70,80,90,12.34,100,"kishan",8j,True]
print(l1)
print(type(l1))

# index : start  0 ,1,2,3,4 .....

# print(l1[8])

# update : 
"""l1[2] ="rohit"
print(l1)
"""

# built in function  : len min max sorted sum 
"""
l1=[1,2,9,8,7,6,34,900]

print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1))  # asc to dec 
print(sum(l1))
"""
# slicing : 

"""
index pos : l to  r    : pos  ==> 0 
negtive  index : r to l    ==>   -1
"""
l1=[10,28,92,86,7,62,341,900]
"""
print(l1[4])
print(l1[-3])
print(l1[2:5])  # starting index 2  ending index :5 
print(l1[1:-3])  # starting index 1 ending index :-3 
print(l1[ :7])
print(l1[ 1 : ])
print(l1[2  :6 :2]) # start index 2 end  6 step  2
print(l1[ : : 2])
print(l1[ : : -2])
"""
# print(l1[-3 :-6 :-2 ])  # []r p v r t 
# print(l1[ : : -1])


# methods : 
l1=[10,28,92,86,7,62,341,900,10,789,10]

"""l1.append(1000)
print(l1)
"""
"""l1.insert(2,"kishan")  # index , value
print(l1)"""

"""l1.remove(900)
print(l1)
"""
"""
l1.pop(5)  # index number wise 
print(l1)
"""
"""l2= l1.copy()
print(l2)
"""
"""l2=["apple","banana","cherry","date","mango"]
l1.extend(l2)
print(l1)
"""
# l1.clear()
# print(l1)

l1=[10,28,92,86,7,62,341,900,10,789,10]

# print(l1.index(10))
# print(l1.index(10,1,12))  # start index 1 end index 12

# print(l1.count(10))
"""l1.sort()   # list method  
print(l1)
"""
l1.reverse()  # list method
print(l1)

"""
task :1 
l1=[10,28,92,86,7,62,341,900,10,789,10]

output  desc to asc : 
l1 =[900,789,62,86,92,28,10,10,10,7]

task  :2 

ask user to  enter  the  list element  store in to the list  and seprate the  odd and even element in list.

input  :5 
l1=[1,2,3,4,5] 

odd =[1,3,5]
even =[2,4]

task :3 
ask user to  enter  the  list element  store in to the list  and remove the  duplicate element in list.

input  :10 
l1 = [1,2,2,3,3,4,4,5,6,7]
output  :l1 = [1,2,3,4,5,6,7]

task :4 
ask user to  enter  the  list element  store in to the list  print the second largest element  in list. 
input  :5 
l1=[1,2,3,4,5] 

output :  second largest element  : 4

task  : 5 take list from user append all element in list and print pelindorme num in list 
 
         input : [121 , 131 , 123 ,145 , 789 ]
         output :  [121,131]

task :6 
Write a Python program to find a list of integers with exactly two occurrences of nineteen
	 and at least three occurrences of five.  count 
	Return True otherwise False.
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

task :7 
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

"""
ask user to  enter  the  list element  store in to the list  and seprate the  odd and even element in list.

input  :5 
l1=[1,2,3,4,5] 

odd =[1,3,5]
even =[2,4]

"""
n=int(input("enter the  element  you want  to store in list :"))
l1=[]
for i in range(n):
    ele =int(input("enter the  element  :"))
    l1.append(ele)
print(l1)
# l1=[1,2,3,4,5]
even=[]
odd=[]
for i in l1:
    if i % 2==0:
        even.append(i)
    else :
        odd.append(i)
print(even)
print(odd)