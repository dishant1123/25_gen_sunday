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

class bank : 
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
