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

class vehicle :
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
