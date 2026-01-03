"""
2. multiple  inheritance  : 
class  a : 
class b :
class c :(a,b)    # MRO  : method resolution order

"""

"""class father : 
    def __init__(self,f_name):
        self.f_name = f_name

class mother :
    def __init__(self,m_name):
        self.m_name = m_name

class son(father,mother):
    def __init__(self, f_name,m_name,c_name,c_age):
        father.__init__(self,f_name)
        mother.__init__(self,m_name)
        self.c_name = c_name
        self.c_age = c_age
    def show(self):
        print("Family Information  :") 
        print("father's name is  :",self.f_name)
        print("mother's name is  :",self.m_name)
        print("son's name is  :",self.c_name)
        print("son's age is  :",self.c_age)

s=son("ramesh","sunita","ramu",10)
s.show()
"""

# 3: multi level inheritance

"""
class a :
class b(a):    b ==>a 
class c(b) :   c ==> b  == >a 
"""

class employees :
    def __init__(self,name,position):
        self.name =name 
        self.position = position
    def show(self):
        print("Employee's name is  :",self.name)
        print("Employee's position is  :",self.position)
        
class manager(employees):
    def __init__(self, name, position,salary):
        super().__init__(name, position)
        self.salary = salary
    
    def show(self):  # virtual function    ==> override () 
        employees.show(self)
        print("salary of manager is  : ",self.salary)
        print("show function of manager class.")
        
class senior_manager(manager):
    def __init__(self, name, position, salary,bonus):
        super().__init__(name, position, salary)
        self.bonus = bonus
        
    def show(self):
        manager.show(self)
        print("bonus of senior manager is  : ",self.bonus)
        print("show function of senior manager class.")

s=senior_manager("dev","data analysis",90000,30000)
s.show()

m=manager("daksh","pytho developer",70000)
m.show()

"""
task  :1 

Implement the following hierarchy . 
The Book function has name, n (number of authors), authors (list of authors), 
publisher, ISBN, and year as its data members and the derived class has course as its data member. The derived class 
method overrides (extends) the methods of the base
class. 

hint  : self.authors =[]    
class book : 

class tex_book(book) :  course 
"""