# hierarchy  inheritance  : 
"""
class a : 

class b(a) : 

class c(a):  

one  base class is  inherited by multiple derived class. 
"""

# ex : 

"""class employees : 
    def __init__(self,name):
        self.name =name 

    def show(self):
        print(self.name)

class manager(employees):
    def role(self):
        print(" role :manager")
        
class developer(employees):
    def role(self):
        print(" role :developer")
        
m=manager("rohit")
m.show()
m.role()

d=developer("dev")
d.show()
d.role()
"""

# hybrid inheritance  : 
"""
it is  combination of  one  or  more than  inheirtance . 
combination  multi ple  and  multi  level inheritance . 

class a :
class b(a) :
class c(a) : 

class d(b,c) :  MRO  : method  resoultion order 
"""
"""
class Person:
    def __init__(self, name, **kwargs):
        self.name = name
        print("Person constructor")


class Teacher(Person):
    def __init__(self, subject, **kwargs):
        self.subject = subject
        print("Teacher constructor")
        super().__init__(**kwargs)


class Researcher(Person):
    def __init__(self, field, **kwargs):
        self.field = field
        print("Researcher constructor")
        super().__init__(**kwargs)


class Professor(Teacher, Researcher):
    def __init__(self, name, subject, field):
        print("Professor constructor")
        super().__init__(name=name, subject=subject, field=field)

    def show(self):
        print("Name   :", self.name)
        print("Subject:", self.subject)
        print("Field  :", self.field)


p = Professor("Rohit", "Java", "IT")
p.show()
"""
# encapsulation  : 
"""
data variable +methods (functions) wrapped together in single unit and direct access to data is restricted to the methods.

private modify  using encapsulation. 
1.get  method  : data print 
2. set method : data print  
"""

class bank : 
    def __init__(self,name,acnum):
        self.__name =name 
        self.__acnum =acnum
        self.__balance =25000 

    def deposit(self,amt):
        self.__balance +=amt
        print("deposited  amount  :",amt)
    
    def withdraw(self,amt):
        self.__balance -=amt
        print("withdrawn  amount  :",amt)
        
    def get_method(self):
        print("name  :",self.__name)
        print("acnum :",self.__acnum)
        print("balance :",self.__balance)
        
    def set_method(self,new_balance):
        self.__balance =new_balance

    def get_balance(self):
        return self.__balance

b=bank("rohit",1234567890)
# b.get_method()
# b.deposit(20000)
# b.withdraw(15000)
# print(b.get_balance())

# b.set_method(50000)
# print(b.get_balance())
# b.deposit(20000)
# b.withdraw(15000)
# print(b.get_balance())

"""
task  :1 
Write a Python program to create a Vehicle class and a Bus child class that inherits from it.
    In the Vehicle class, make vehicle name, mileage, and seating capacity encapsulated (private data members).

    Provide getter methods to access these data members.

    The default fare charge of any vehicle is:
    fare = seating capacity × 100

If the vehicle is a Bus instance, add an extra 10% maintenance charge to the fare.
Display the final fare for both Bus and Vehicle (Car) objects.

output  : 
The bus seating capacity is 50. so, the final fare amount should be 5500
The car seating capacity is 5. so, the final fare amount should be 500

"""

        
