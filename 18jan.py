# polimorphsim : it  means one function or method  name bahaves diffrently  based on the  object or input   ==> many forms 
"""
python polimorphism support  : 

1. duck typing  
2. operator  overloading  
3. method  overloading  (via default arguments ) 
4. method  overriding  (inheritance) 

note  : python does not  support method  overloading in  traditional  way (same name  for different  parameters)
"""

# ex :1 method  overloading (using  default  arg ) 

"""
class calculator:
    def add(self,a,b=0,c=0):
        return a+b+c
    
c=calculator()
print(c.add(10))  # only one arg is given  
print(c.add(10,50))  # only two arg is given  
print(c.add(10,20,40))  # 3  arg is given  

"""    

# ex : 2 using *args  method overloading  :   *args == >take any number of arguments

"""class calculator:
    def add(self, *args): 
        sum =0 
        for i in args:
            sum =sum +i 
        return sum 
c=calculator()
print(c.add(10))    
print(c.add(10,20))    
print(c.add(10,20,80,78,90)) 
"""
# special method : __add__ , __mul__  , __str__, __len__  

# ex :3 method  overriding  (inheritance)
"""
happen when child class provides its own implementation of the method   already defined in parent class
"""

"""class vehicle :
    def speed(self):
        print("two wheeler max speed is 150") 
        
class car(vehicle):
    def speed(self):
        # super().speed()
        print("car max speed is 220")

c=car()
c.speed()
"""

# ex :4 payment system    method  overloading . 
"""
cash , card , UPI , net banking  

action  ==> same  pay 
diffrent input  ==> cash card upi   
"""

"""class payment : 
    def pay(self,amt,method ="cash"):
        if method == "cash":
            print(f"cash payment for rs.{amt}")
        elif method == "card":
            print(f"card payment for rs.{amt}")
        elif method == "upi":
            print(f"upi payment  for rs.{amt}")
            
p=payment()
p.pay(100)
p.pay(9000,"card")
p.pay(10000,"upi")
"""

# ex :5 bank interest  method  overloading .
"""
all bank give interest
but  diffrent bank  interest rate different
"""

"""class bank : 
    def interest(self,amt,rate):
        print(f"normal bank interest for rs.{amt} is rs.{amt*rate}")

class hdfc(bank):
    def interest(self,amt,rate):
        print(f"hdfc bank interest for rs.{amt} is rs.{amt*rate*0.1}")
        
class baroda(bank):
    def interest(self,amt,rate):
        print(f"baroda bank interest for rs.{amt} is rs.{amt*rate*0.2}")
        
h=hdfc()
b=baroda()

h.interest(1000,5)
b.interest(1000,5)
"""
# summary  : 
"""
                method  overloading          method overriding  
inheritance        not required               required
same method name       yes                       yes
parameters             different                 same
python support        using default/*args        fully supported
runtime behaviour      input based                object based 

loading  :  ==> same work different  inputs
riding  :  ==> same work different  objects 
        
"""
# operator  overloading : 
"""
ex :1 
Create a class student with following member attributes: roll no, name, age and total marks. Create suitable methods for reading and printing member variables. Write a python program to overload ‘==’ operator to print the details of students having same marks. in python
"""
"""class student : 
    def __init__(self,rollno,name,age,marks):
        self.rollno = rollno
        self.name = name
        self.age = age
        self.marks = marks
        
    def display(self):
        print(f"roll no : {self.rollno}")
        print(f"name : {self.name}")
        print(f"age : {self.age}")
        print(f"marks : {self.marks}")
    # overload operator  :   ==
    def __eq__(self, other):
        if self.marks == other.marks:
            print(f"both students have same marks")
            self.display()
            other.display()
            return True
        else :
            print(f"both students have different marks")
            return False
        
s1=student(101,"ram",20,100)
s2=student(102,"sita",18,100)
s1==s2
"""       
"""
ex :2 
Write a program to create a class called Data having “value” as its data member. Overload the (>) and the (<) operator for the class. Instantiate the class and compare the objects using _lt_ and _gt_.
"""
"""class data:
    def __init__(self,value):
        self.value = value
        
    def __gt__(self, other):
        return self.value > other.value 
    def __lt__(self, other):
        return self.value < other.value
    
d1=data(25)
d2=data(40)

print("d1 > d2 :",d1 > d2)
print("d1 < d2 :",d1 < d2)

print("__gt__ d1 d2 :",d1 .__gt__(d2))
print("__lt__ d1 d2 :",d1 .__lt__(d2))
"""
"""
task :1 
Write a Python program to find the Net Salary of an Employee using Inheritance, Encapsulation, and Polymorphism.

Create three classes: Employee, Perks, and NetSalary.
Requirements
Employee Class :

Use encapsulation (private data members).
Data members: employee id, name, basic salary.

Methods:
    To get employee details from the user.
    To display employee details.
    To return basic salary.

Create a method calculate_salary() that will be overridden (polymorphism).

Perks Class (inherits Employee) :
Calculate:
    DA = 35% of basic salary
    HRA = 17% of basic salary
    PF = 12% of basic salary
Method to display DA, HRA, PF.
Override calculate_salary() method.

NetSalary Class (inherits Perks) :

Calculate total salary:
    Net Salary = Basic Salary + DA + HRA − PF

Display employee details, perks, and net salary.
Demonstrate method overriding (runtime polymorphism).
It is compulsory to create objects and demonstrate the methods with correct output.
"""