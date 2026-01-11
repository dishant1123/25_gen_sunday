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
