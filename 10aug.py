# match  : 
"""
c  : 
switch (choice)
{
    case 1 :
        printf()
        break ;
}

python  : 

match choice :
    case 1:
        print()
"""
"""a=int(input("enter the  number  1: ")) 
b=int(input("enter the  number  2: "))

print("1. addition ")
print("2. subtraction ")
print("3. multiplication ")
print("4. division ")
print("5. modulus ")
print("6. floor division ")

choice = int(input("enter the choice : "))
match choice :
    case 1 :
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4 :
        print(a/b)
    case 5:
        print(a%b)
    case 6 :
        print(a//b)
    case _:
        print("invalid choice")

"""

# nested match : 

"""
print("1. FRUITS")
print("2. VEGETABLES")

choice = int(input("enter the choice :"))
match choice :
    case 1 :
        print("you selected  FRUITS")
        print("1. APPLE :rs 100")
        print("2. BANANA :rs 50")
        print("3. ORANGE :rs 150")
        subchoice =int(input("enter the subchoice :"))
        match subchoice :
            case 1:
                print("you selected APPLE")
                qty =int(input("enter the  quntity :"))
                print("your total bill is  rs:",qty *100)
            case 2:
                print("you selected BANANA")
                qty =int(input("enter the  quntity :"))
                print("your total bill is  rs:",qty *50)
            case 3:
                print("you selected ORANGE")
                qty =int(input("enter the  quntity :"))
                print("your total bill is  rs:",qty *150)
    case 2 :
        print("you selected VEGETABLES")
        print("1. POTATO:rs 50")
        print("2. CARROT:rs 40")
        print("3. METHI :rs 10")
        subchoice =int(input("enter the subchoice :"))
        match subchoice :
            case 1:
                print("you selected POTATO")
                qty =int(input("enter the  quntity :"))
                print("your total bill is  rs:",qty *50)
            case 2:
                print("you selected CARROT")
                qty =int(input("enter the  quntity :"))
                print("your total bill is  rs:",qty *40)
            case 3:
                print("you selected METHI")
                qty =int(input("enter the  quntity :"))
                print("your total bill is  rs:",qty *10)
"""

# match with  if else : 

"""ch=input("enter the character : ")

match ch :
    case 'a':
        print("vowel")
    case 'e':
        print("vowel")
    case 'i':
        print("vowel")
    case 'o':
        print("vowel")
    case 'u':
        print("vowel")
    case _ : 
        if ch >='0' and ch <='9' :
                print("digit")
        elif ch >='a' and ch <='z' :
            print("capital letter")
        else :
            print("special character")
"""

"""
task  : 1 :  nested match 
hotel  menu  : 

1. breakfast   : 2 op     
2. lunch       :2 op 
3. dinner      :2 op 

"""

# loop  : 
"""
1. for  loop  : 
2. while loop :
3 . while  True: 
"""

"""
c : 

for(start ; condition; inc / dec)
{
    print()
}

python : 

for (variable name) in range(start,end,step):
    print(varibable name )
"""

# 1-100 print: 

"""
for i in range(1,101):
    print(i,end=" ") 
"""

# 100-1 : 

"""
for i in range(100,0,-1):
    print(i,end=" ") 
"""
# odd : 
"""
for i in range(1,101,2):
    print(i,end=" ") 
"""
# even : 
"""
for i in range(0,101,2):
    print(i,end=" ") 
"""

# user input : 

"""
n=int(input("enter the  number  : "))
for x in range(1,n+1):
    print(x,end=" ")
"""

"""start=int(input("enter the  start  : "))
end=int(input("enter the  end  : "))

for y in range(start,end+1,2):
    print(y,end=" ")
"""

# break contunie  pass :
"""for i in range(1,20):
    if i==15:
        break
    # print(i,end=" ")  # 1-14  d d r m v k  k p  # 1-15  r t c p    
print(i)
"""
# option : 
"""
mera ans : c 
a. 1-15 
b. 15   d d r p v b c  k m r b    
c. 1-14  t d k 
"""
# contunie :
"""for i in range(1,20) : # 1,10 ==> 1 start  10  end == >1-9   
    if i==15 :
        continue
    # print(i,end=" ")
print(i)
"""
# t ==> 19
# v ==> 19
# ri ==>  19
# raj ==> 20  
# ch ==> 19  
# pra ==>  19 
# m ==> 19  

"""
for (i=1; i<10; i++)   # 
"""

# pass : 
"""for  i in range(1,10) : 
    if i==5 :
        pass
    print(i,end=" ")
"""

# while  : 
"""
i = intial 

while con :
    print()
    i=i+1   // i+=1 
"""

"""
complete calculator  and  put  1 option for  exit   :

7 . exit  

10 
3 

"""

