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
# bank  :
"""
Royal Kids Bank :

Design a Banking App in c  that has the following functionalities:-
User can:-
◆OPEN ACCOUNT by username and password of his choice. On Opening account, his initial balance will be ₹ 25,000/-. 
Once he opens account, he can login by re-entering the same username & password.
◆LOGIN is compulsory to perform any task such as withdrawal, deposit or balance check. If the user name or password do 
not match, he can not Login. Once he is logged in, he can do as many transactions as he wants. He needs to Logout after 
he finishes all the transactions
◆DEPOSIT will enable user to deposit amount of money of his choice. His balance should be updated after the task 
completes.
◆WITHDRAW will enable user to withdraw amount of money of his choice. The only condition is that his balance at any 
point can not go less than ₹10,000/-. If this can happen after his withdrawal, your program must not allow that
transaction. His balance should be updated after the task completes.
◆CHECK BALANCE will show the latest updated balance to user.
◆LOGOUT will exit the user from the program
You should use these functions in your program: login(), deposit(), withdraw(), checkBalance()

"""

# hint  : 
"""

creat  username , password : us = d123 ,pass =d@123 
1. login : us pass : match   :   ac =25000 
    1. deposit  
    2. withdraw  :condition  : min  10000   ===> bal =25000 with  ==>19000  ==> no
        con  : balance - withdraw >=10000 :
            balance = balance -with_amt
    else :
        print("insufficient balance , and  you have required min 10000 rs in your account")
    3.check balance 
2.exit 

"""
# next topic : lambda , map , filter , reduce ==> random 
