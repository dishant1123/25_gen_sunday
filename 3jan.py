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

"""
Create a class called Student, having name and email as its data members and _init_(self, name, email) and putdata(self) 
as bound methods. The _init_ function should assign the values passed as parameters to the requisite variables. The 
putdata function should display the data of the student. Create another class called PhDguide having name, email, and 
students as its data members. Here, the students variable is the list of students under the guide. The PhDguide class 
should have four bound methods: _init_, putdata, add, and remove. The _init_ method should initialize the variables, the 
putdata should show the data of the guide, include the list of students, the add method should add a student to the list of 
students of the guide and the remove function should remove the student (if the student exists in the list of students of 
that guide) from the list of students.
"""