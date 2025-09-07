# operator : 
"""
1.airthematic operator  : + - * / % //  
2.comparison  operator  : < > <= >= == !=     ==> bool value ==> true or false
3.assignment operator  = += -= *= /= %= //=
4.logical operator  : and or not 
5.membership operator : in not in

"""
# a=125
# b=20
# print(a%b)  # modular operator 
# print(a/b)  # divison operator 
# print(a//b)  # floor  divison operator 

# print(a<b) 

# a=a+b  
# a+=b   # a-=b a*=b a/=b a%=b a//=b
# print(a)

# a=125
# b=20

# print(a<b and a!=b)   # and 
# print(a<b or a!=b)   # and 

"""
l1 =["raj","param",3,4,5,6,9]
print(3 in l1)
print("kishan"  not in l1)
"""

# conditional statement  : 
"""
if else : 

syntax : 

if condition :
    print()
else :
    print()

"""
"""
a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))

if a>b:
    print("a is  big")
else :
    print("b is  big")
"""

# ladder if : 
"""
syntax : 

if con : 
    print()
elif con : 
    print()
else :
    print()
"""

# task  : 1 ask user to enter the three number  anc check which one is  big.
"""
a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))
c=int(input("enter the  number  : "))

if a>b and a>c :
    print("a is  big")
elif b>a and b>c :
    print("b is  big")
elif c>a and c>b :
    print("c is  big")
else :
    print("same")
"""

# nested  if : 
"""
syntax : 

if con : 
    if (con) :
        print()
    else :
        print()
elif con : 
    if (con) :
        print()
    else :
        print() 
else :
    ...

"""
"""a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))
c=int(input("enter the  number  : "))

if a>b : 
    if a>c :
        print("a is  big") 
    else :
        print("c is  big")
elif b>a : 
    if b>c :
        print("b is big")
    else :
        print("c is  big")
else :
    print("same")
"""
"""
task :2 
ask user to enter the  character and check whether it is vowel  ,consonant ,digit or special character.

input  : a  ==> vowel
input  : b ==> consonant
input  :12 ==> digit
input  :+ ==> special character
"""

# ch=input("enter the character :  ")   # i

# if ch =='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' :
#     print("vowel")
# elif ch >'a' and ch <='z':   # r > a and r <=z  
#     print("consonant")
# elif ch >='0'  and ch <='9' : 
#     print("digit") 
# else :
#     print("special character")

"""
task :3 
ask user to enter the character convert into upper and vice versa .

input  : a 
output :A   

input :A 
output:a 

"""
"""
c : 

scanf ("%c",&ch)   # a ascci value : 97   A ascci value  65  diff :32  

if ch >='A' and ch <='Z' :
    ch =ch +32
else :
    ch =ch-32 
"""


"""
ch=input("enter the character :  ")  

if ch >='A' and ch <='Z' :
    ch =ord(ch) +32 
    print("converted  lower character is :", chr(ch))
else :
    ch =ord(ch)-32
    print("converted  upper character is :", chr(ch))
"""
# ord :

# task :4 
"""
ask user to  enter the three number and  check  it is  small ,medium or large.
input a :10 
input b :20 
input c :30

output : a small  b medium  c large 
 10  10  20 : 

"""

#task  : 5 
"""
ask user to enter the  salary  and calculate the gross salary  . 
gross salary  = salary  + hra + da 

range           HRA    DA 
< 10000         20%    80 %
10000-25000     30%    85 %
25000 above     33%    90 % 

ex : 
input : 9000 
hra = salary * 0.2   = 9000 * 0.2 = 1800
da = salary * 0.8   = 9000 * 0.8 = 7200
gross salary  = salary  + hra +da = 9000 +1800 +7200 =18000 
"""

# match : 
