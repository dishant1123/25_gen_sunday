# function  : 
"""
int sum(int a, int b ) 
{
   return c  
}
void main()
{
    sum();
}

def  ==>  define   ==>  def  function  name (arg)

1.no arg no return 
2.no arg  with return 
3. with arg no return 
4. with arg with return 

use / purpose  : 

1. repeatly  use  the  function
"""

# 1.no arg no return 

"""def x():  # def  keyword  x ==> func name  ==>decalration 
    a=int(input("a : "))
    b=int(input("b: "))   # func  intialization  
    c=a+b 
    print(c)
x()   # func calling 
"""

# 2.with arg no return 
"""def y(a=90,b=0):
    c=a+b
    print(c)
    
# a=int(input("a : "))
# b=int(input("b: "))   # func  intialization  
y(12)
y(0,56)
"""

# 3.no arg  with return 
"""def z():
    a=int(input("a : "))
    b=int(input("b: "))
    c = a+b 
    return c 
print(z())
"""

# 4 :with arg with return

"""def z(a,b):
    c = a+b 
    return c 
print(z(45,78))

"""

"""def prime(n):
    count =0 
    for i in range(1,n+1):
        if n % i ==0 :
            count +=1 
    if count ==2 :
        return 1
    else :
        return 0 
# print(prime(50))

if prime(5) ==1 :
    print("prime")
else :
    print("not prime")
"""

# local variable  : 

"""def a ():
    c =100   # local variable
    print(c)
a()
# print(c) # local variable can't be accessed outside the function
"""

# global variable  :

"""a =100 
def v(): 
    print(a) 
v()
print(a)  # bcz  of  global  you can access outside the function also. 
"""

# modify golbal variable  :

"""a=100 
def n():
    global a 
    a=900 
    print(a) 
n()
print(a)# bcz  you modify the global variable outside the function . 
"""

# *args : only take  numberic arg 

"""def a(*args):
    return sum(args) 
print(a(12,12,33,56,78,90,23,45,67))
"""

"""def x (*y):
    sum =0 
    for i in y : 
        sum =sum +i 
    print(sum)
x(12,23,45,67,90.78,True,8j,10j)
"""

# **kwargs : take args  with key and  value . 

"""
def h(**kwargs):
    for i ,j in kwargs.items():
        print(f"{i} = {j}")
h(name="chahat",age=18,city="gandhinagar",pincode=380013)
"""

# emp manag system : 

"""
1.add
2.delete
3.update
4.search
5.display
"""

d1={} 

def add():
    id =int(input("enter the id : "))
    name =input("enter the name : ")
    salary =int(input("enter the salary : "))
    d1[id]={name,salary}
    print("emp added")

def delete_emp():
    del_id= int(input("enter the  id you want to delete : "))
    if del_id in d1: 
        del d1[del_id]
        print("emp deleted")
    else :
        print("emp not found")

def update_emp ():
    update_id= int(input("enter the  id you want to update : "))
    if update_id in d1: 
        name =input("enter the new name : ")
        salary =int(input("enter the new salary : "))
        d1[update_id]={name,salary}
        print("emp updated")
    else :
        print("emp not found")
        
add()
add()
print(d1)
delete_emp()
print(d1)  # {1: {900000, 'chahat'}, 2: {700000, 'sita'}}
update_emp()
print(d1)
