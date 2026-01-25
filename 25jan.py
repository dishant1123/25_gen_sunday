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

class calulations :
    
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def sub(a,b):
        return a-b
    
c1=calulations()
print(c1.add(10,20))
print(c1.sub(10,20))

