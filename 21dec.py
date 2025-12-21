# python  oop : object oriented programming
"""
1.public : access from anywhere
2.private : within the class 
3.protected : within the class and its subclasses (inheritance)
"""
# ex :1 
"""class student:   # class name  ==> student 
    name="rohit"   #name  , age  ==> public data member 
    age=21 

s1=student()  # s1 object 
print("before change ")
print("name is  ==> ",s1.name)  # s1.name  ==> public data member 
print("age is  ==> ",s1.age)  # s1.age  ==> public data member
s1.name="meet"
s1.age=22
print("after change ")
print("name is  ==> ",s1.name)
print("age is  ==> ",s1.age)
"""

# ex :2 

"""
class employees :
    name =input("enter name :")
    age =int(input("enter the age : "))
    
    def show(self):  # self : key word ==> refers current  object 
        print("name is  ==> ",self.name)
        print("age is  ==> ",self.age)
e1=employees()
e1.show()  # function call  ==> object 
print("name is : ",e1.name)
print("age is : ",e1.age)
"""

# ex :3

"""
class student :
    l2=[] 
    def input(self):
        for i in range(3):
            name=input("enter name :")
            age=int(input("enter the age : "))
            self.l2.append([name,age])  # d1[name] =age 
    def show(self):
        for i in range(len(self.l2)):
            print(self.l2[i][0],"  ==> ",self.l2[i][1]) 

s1=student()
s1.input()
s1.show()

"""

# ex :4 private :

"""class vehicle :
    __name ="car"   # name , model ==> private data member
    __model ="toyota"
    
    def show(self):
        print("name is  ==> ",self.__name)
        print("model is  ==> ",self.__model)
v=vehicle()
# print(v.__name)  # not accessible  outside the class bcz of  private. 
# print(v.__model)
v.show()
v.__name="honda"  # not change bcz of  private. 
v.__model="civic"
v.show()
"""

# protected : 

"""class student :
    _name ="rohit"   # name , age ==> protected data member
    _age =21 

class teacher(student):
    def show(self):
        print("name is  ==> ",self._name)
        print("age is  ==> ",self._age)
t=teacher()
t.show()
"""

# bank  : 

class bank :
    def info(self):
        self.branch=input("enter branch name : ")
        self.account_number=int(input("enter account number : "))
        self.balance =25000 
    
    def deposit(self,amt):
        self.balance=self.balance+amt
        print(f"after  deposit {amt} and your  balance is  ==> {self.balance}")
    
    def withdraw(self,amt):  # bal =30000  - 28000 ===> min 10000 
        if self.balance- amt >=10000 :
            self.balance=self.balance-amt
            print(f"after  withdraw {amt} and your  balance is  ==> {self.balance}")
        else :
            print("not enough balance min balance required is  ==> rs.10000")
    def check_balance(self):
        print("your  final is balance   ==> ",self.balance)
    
    def display(self):
        print("branch name is  ==> ",self.branch)
        print("account number is  ==> ",self.account_number)
        print("balance is  ==> ",self.balance)
b=bank()
print("BANK DETALIS :\n")
b.info()
b.display()
b.deposit(10000)
b.withdraw(18000)
b.check_balance()

"""
1. log in  pin  ==> 3 attempt 

task  :2 
1. create  ==> user name  password create  
2. login  ==> match 
    1. deposit  
    2. withdraw
    3. check balance 
    4. exit 
    
menu driven  :

"""
