# function  : 
"""
def ==> def keyword ==> function  

4 type  : 

1. no arg  no return 
2. no arg  with  return 
3. with arg  no return
4. with arg  with  return
"""
#1: 
"""
def addition():  # def keyword ==> addition  ==>name  
    a=10 
    b=20    # function  intialization  
    c=a+b
    print(c)
addition()   # function calling  
"""
#3: 
"""
def addition(a,b=90):  # def keyword ==> addition  ==>name  
    c=a+b
    print(c)
addition(12)   # function calling ==>  b value  is taken by  90  because we set default value.
"""
#2: 
"""
def addition():  # def keyword ==> addition  ==>name  
    a=int(input("enter the  num : "))
    b=int(int(input("enter the  num : ")))
    c=a+b
    return c 
print(addition())   # function calling  
"""
#4 : 
"""
def adition(a,b=90):
    c =a+b
    return c 
print(adition(12))
"""

# local variable  : 
"""
def x():
    a=10     # local variable   ==> within  function  print 
    print(a)
x()"""
# print(a)  # bcz of local variable  you can't print  outside the function .

# global variable  :
"""
a=12 
def x():
    print(a)
x() 
print(a)  # it is global variable  so you can print it outside the function .
"""

# global variable  modify : 
"""x=100 
def y():
    global x 
    x=900 
    print(x)
y()
print(x)
"""

# *args  : only take a numberic value. 

"""
def x(*args):
    return sum(args)   # sum ==> built in function  
print(x(12,4,34,56,78,90,89,90,34,56.78))
"""
"""def y(*x):
    sum =0 
    for i in x :
        sum = sum +i 
    return sum 
print(y(12,34,56,778,90))

"""
# **kwargs  : use in dict  
"""
def c(**kwargs):
    for i, j in kwargs.items():
        print(f"{i} : {j}")
c(name="rohit",age=21,city="mumbai")
"""

# app  : 
"""
employess management system

1.add employee
2.delete employee
3.update employee
4.display employee
5. search employee
"""
d1={}

def add_emp():
    id =int(input("enter the  id : "))
    name =input("enter the  name : ")
    salary =int(input("enter the  salary : "))
    d1[id]={name,salary}
    print("employee added successfully")

def delete_emp():
    del_id= int(input("enter the id you want to delete : "))  #2 
    
    if del_id in d1 :
        del d1[del_id]
        print("employee deleted successfully")
    else :
        print("employee not found")

def update_emp():
    update_id= int(input("enter the id you want to update : "))  #2
    if update_id in d1 :
        name=input("enter the name : ")
        salary=int(input("enter the salary : "))
        d1[update_id]={name,salary}
        print("employee updated successfully")
    else :
        print("employee not found")
    
# add_emp()
# add_emp()
# delete_emp()
# update_emp()
# print(d1)

def main():
    while True :
        print("1.add employee")
        print("2.delete employee")
        print("3.update employee")
        print("4.display employee")
        print("5. search employee")
        print("6.exit")
        choice =int(input("enter the choice : "))
        
"""
id  name  salary
1   ram  9000 
2   sita 8000 
3   ravan 7000 
"""
"""
menu driven  : 

1.add employee
2.delete employee
3.update employee
4.display employee
5. search employee

choice : 
"""