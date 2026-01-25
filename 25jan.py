# abstraction  : 
"""
it means hiding implementation details and exposing only the functionality required.
==> in python abstraction is manily achieved by  class  and  function  .
    1.abstract base class  ==> from abc import ABC  
    2.abstracts  method    ==> @abstractmethod

==> class abstract  class declare ==> can't be  created object 
==> @abstractmethod  ==> can't be  intialized. 

"""

# ex :1 
from abc import ABC, abstractmethod

"""class bank(ABC) :
    def __init__(self,name,balance):
        self.name =name
        self._balance =balance  # protected data member
        self.__pin = 1211 # private data member
        
    @abstractmethod
    def calculated_interest(self):
        pass 
    
    def get_pin(self):
        return self.__pin 

class savingsaccount(bank):
    def calculated_interest(self):
            return self._balance * 0.05
        
s=savingsaccount("rohit",100000)
print("account holder name  : ",s.name)
print("account balance  : ",s._balance)
print("interest  : ",s.calculated_interest())
print("pin  : ",s.get_pin())
"""
# print(s.__pin)  # error  private data member

# ex 2 : 

"""class vehicle(ABC):
    def __init__(self,fuel,brand):
        self.brand =brand
        self._fuel =fuel
        self.__engine_no="ENG123"
        
    @abstractmethod
    def mileage(self):
        pass 
    
    def get_engine_no(self):
        return self.__engine_no
    
class car(vehicle):
    def __init__(self, fuel, brand):
        super().__init__(fuel, brand)
    
    def mileage(self):
        return "15 km/l"
    
c=car(1000,"BMW")
print("car brand  : ",c.brand)
print("car fuel  : ",c._fuel)
print("car engine no  : ",c.get_engine_no())
print("car mileage  : ",c.mileage())
"""
# ex :3  inheritance , encapsulation , polymorphism , abstraction

"""class bank (ABC):
    def __init__(self,name,balance):
        self.name=name
        self._balance =balance
        self.__pin =1211 

    @abstractmethod
    def calculated_interest(self):
        pass 
    
    def get_pin(self):
        return self.__pin
    
    def deposit(self,amt):
        self._balance +=amt
        print("deposited  amount  :",amt)
    
    def get_balance(self):
        return self._balance

class savingsaccount(bank):
    
    def calculated_interest(self):
        return self._balance * 0.05

class currentaccount(bank):
    
    def calculated_interest(self):
        return self._balance * 0.02
    
s=savingsaccount("rohit",100000)
c=currentaccount("dhruv",200000)

accounts =[s,c]

for i in accounts:
    print("account holder name  : ",i.name)
    print("account balance  : ",i.get_balance())
    print("interest  : ",i.calculated_interest())
    print("pin  : ",i.get_pin())
"""

# class method  : 

"""
uses @classmethod   ==>decorator
take a first parameter  ==> cls
can access and  modify class variables
"""

"""class student : 
    school_name="Apple wood school"
    
    def __init__(self,name):
        self.name =name 
        
    @classmethod
    def change_school(cls,new_school):
        cls.school_name =new_school
        
s1=student("rohit")
s2=student("kishan")

print("before change  :",student.school_name) 

student.change_school("Delhi Public school")

print("after change  :",s1.school_name)
print("after change  :",s2.school_name)
"""

# static  method  : 
"""
it behaves like  normal function . 
can't modify 
take a  no self  and  no cls 
"""

"""class calulations :
    
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def sub(a,b):
        return a-b
    
c1=calulations()
print(c1.add(10,20))
print(c1.sub(10,20))

"""

# task  : 
"""
Create a program to simulate a Call Handling System using Object-Oriented Programming (OOP) concepts in Python.
The program must demonstrate the use of the following OOP principles:

1.Abstraction
2.Inheritance
3.Encapsulation
4.Polymorphism

Requirements:
1. Employee Classes
Create three classes named:
	Respondent
	Manager
	Director

Each class should have a constructor that accepts id and name.
The constructor should initialize:

	==>rank
		3 for Respondent
		2 for Manager
		1 for Director

	==>free → a boolean variable initialized to True

2. Common Methods (Demonstrating Abstraction & Inheritance)
Implement the following methods in all three classes:

	receive_call()
	Prints:
	"call received by <employee name>" and sets free to False

	end_call()
	Prints:
	"call ended"
	and sets free to True

	is_free()
	Returns the value of free

	get_rank()
	Returns the value of rank

3. Call Class
Create a class Call with a constructor that accepts:
	id
	name of the caller
It should initialize a variable assigned to False.

4. CallHandler Class
Create a class CallHandler with three class variables:
	respondents
	managers
	directors

5. Employee Management (Encapsulation)

Implement an add_employee() method in CallHandler that:
	Accepts an employee object
	Adds it to the appropriate list based on their rank

6. Call Dispatching (Polymorphism)

Implement a dispatch_call() method in CallHandler that:

Accepts a Call object
Assigns the call to the first available employee, checking in the order:

	Respondent → Manager → Director

Calls receive_call() on the assigned employee
Sets the call's assigned variable to True
If no employee is free, prints:
"Sorry! All employees are currently busy."

7. Object Creation
Create:
	3 Respondent objects
	2 Manager objects
	1 Director object
Add them to the system using add_employee().

8. Call Assignment

Create a Call object and demonstrate how it is assigned to an employee using the dispatch_call() method.
.
"""
