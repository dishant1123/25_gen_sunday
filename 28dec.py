# constructor  : automatically call when object is  created. 
"""
type  : 
1. default  
2. parameter
3. non parameter
4. constructor overloading 
"""
# default  : 
"""class student :
    def __init__(self):  # def ==> func  __init__() ==>special method / constructor 
        print("hello  rohit")
        print("live in ahm.")
        
s=student()
"""
# non parameter  :

"""class employees :
    def __init__(self):
        self.name ="rohit"
        self.age=20
        print("rohit information")
    def show(self):
        print(self.name)
        print(self.age)

e=employees()
e.show()
print(e.name)
e.name ="krishna"
e.show()
"""

# parameter  :

"""class student: 
    def __init__(self,name,age):
        self.name =name 
        self.age=age
        print("hello  rohit")

s=student("rohit",20)
print(s.name)
print(s.age)
"""

#constructor overloading :
"""class vehicle :
    def __init__(self):
        print("vehicle class constructor.")
    
    def __init__(self):
        self.name ="four wheeler"
        print("vehicle class constructor ==>non parameter.")
    
    def show(self):
        print("vehicle class show method")
    
    def show(self):
        print("vehicle class show method ==>non parameter.")
        print(self.name)

v=vehicle()
v.show()
"""

# 4 pillar  of  oop :
"""
1.inheritance
2.polymorphism
3.encapsulation
4.abstraction
"""

# types of inheritance : 
"""
1.single inheritance
2. multiple inheritance
3. multi level inheritance
4. hirearchy inheritance
5. hybrid inheritance
"""

# single  inheritance : to inherit all the properties of a  base class. 
#1 :
'''
class student :
    def show(self):
        print("student class show method")

class teacher(student):
    """
    def display(self):
        print("teacher class display method")
    """
    def show(self):
        student.show(self)
        print("teacher class show method")
t=teacher()
t.show()
'''
#2: 

"""
class employees :
    def __init__(self):
        self.name ="rohit"
        self.salary =99000 

class manager(employees):
    def __init__(self):
        self.m_name ="vyom"
        # employees.__init__(self) # base class constructor call
        super().__init__()  # base class constructor call
    def show(self):
        print("manager class show method")
        print(self.name)
        print(self.salary)
        print(self.m_name)
m=manager()
m.show()
"""

# ex:3 

"""class employees :
    def __init__(self,name,salary):
        self.name =name
        self.salary =salary
        print("employees class constructor")

class manager(employees):
    def __init__(self,name,salary):
        # super().__init__(name,salary)
        employees.__init__(self,name,salary)
    def show(self):
        print("manager class show method")
        print(self.name)
        print(self.salary)
        
m=manager("rohit",100000)
m.show()

"""
# mcq : 
"""
1.
class Test:
    def __init__(self):
        self.x = 0

class Derived_Test(Test):
    def __init__(self):
        self.y = 1
b = Derived_Test()
print(b.x,b.y)

# ans : error 
2. 

class A():
    def disp(self):
        print("A disp()")
class B(A):
    pass
obj = B()
obj.disp() 

asnwer : A disp()
3.
class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        Test.__init__(self)
        self.y = 1
b = Derived_Test()
print(b.x,b.y)

4. 
class A:
    def __init__(self,x):
        self.x = x
    def count(self,x):
        self.x = self.x+1
class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y
    def count(self):
        self.y += 1     
obj = B()
obj.count()
print(obj.x, obj.y)

answer :3 1 

5. 
class Demo:
    def __init__(self):
        self.x = 1
    def change(self):
        self.x = 10
class Demo_derived(Demo):
    def change(self):
        self.x=self.x+1
        return self.x
obj = Demo_derived()
print(obj.change())

6. 
class Demo:
    def check(self):
        return " Demo's check "  
    def display(self):
        print(self.check())

class Demo_Derived(Demo):
    def check(self):
        return " Derived's check "

Demo().display()
Demo_Derived().display() 

asnwer : demo check , derived check 

7.
class A:
    def __init__(self,x=3):
        self._x = x        
class B(A):
    def __init__(self):
        super().__init__(5)
    def display(self):
        print(self._x)
obj = B()
obj.display() 
"""
class A:
    def __init__(self,x=3):
        self._x = x        
class B(A):
    def __init__(self):
        super().__init__(5)
    def display(self):
        print(self._x)
obj = B()
obj.display() 