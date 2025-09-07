# nested  loop  : 
"""
start , end  :  prime  print 

"""
"""
start =int(input("enter the  starting  number  : "))
ending =int(input("enter the  starting  number  : "))

for i in range(start, ending +1) :   # 100 , 10000
    count =0    # 0 
    for j in range(1,i+1) :  # 1,101 
         if  i % j ==0 :
            count +=1 
    if count ==2 :
        print(i,end=" ") 
"""          
# strong number , amg  pelindorme perfect :     : 
"""
145 : 

each factorial  : 1!  4!  5!  ==>1 + 24 +120  ==>145 
"""

"""start =int(input("enter the  starting  number  : "))
ending =int(input("enter the  starting  number  : "))

for i in range(start ,ending+1) : #123 -10000 : 
    temp =i 
    digit = len(str(i))  # digit =3 
    sum=0
    for j in range(digit):  # 3   == > 0 1 2    2,123  
        r = temp % 10   # r= 123 % 10 =3   # r= 1 %10  0 
        fact =1 
        for  k in range(1,r+1) : #1,4 
            fact = fact *k
        sum = sum +fact
        temp  = temp //10 
    if sum ==i:  
        print(i,end=" ")
"""

# pattern  :
"""
1.          2.          3.          4.          5.          6.
* * * * *   *          * * * * *    1           5 4 3 2 1   1 2 3 4 5
* * * * *   * *        * * * *      1 2         5 4 3 2     2 3 4 5 
* * * * *   * * *      * * *        1 2 3       5 4 3       3 4 5
* * * * *   * * * *    * *          1 2 3 4     5 4         4 5
* * * * *   * * * * *  *            1 2 3 4 5   5           5
"""
# 1 : 
"""
c : 

for(i=6; i>1 ;i -- )  # row 
    for(j=i; j<=5 ;j ++)   # col 
        printf("*")
    printf("\n")
"""
# for  i in range(1,6) :
#     for  j in range(1,6):
#         print("*",end=" ")
#     print()

# 2 : 
"""
for  i in range(1,6) :
    for  j in range(1,i+1):
        print("*",end=" ")
    print()
"""
# 3 : 
"""
for  i in range(5,0,-1) :
    for  j in range(1,i+1):
        print("*",end=" ")
    print()

"""

# 4 : 
"""
for  i in range(1,6) :  # 2 
    for  j in range(5,i-1,-1):  #5 , 1   
        print(j,end=" ")     # 5 4 3 2 1
    print()                  # 5 4 3 2
"""

# 6 : 

"""for i in range(1,6) :  # 3 ,6 
    for j in range(i,6): #3,6  
        print(j,end=" ") # 1 2 3 4 5
    print()              # 2 3 4 5
                         # 3 4 5 
"""

"""
7.             8.          9.         10.         11.       
* * * * *      *             *    * * * * *      * 
  * * * *     * *          * *     * * * *      * * 
    * * *    * * *       * * *      * * *      * * * 
      * *   * * * *    * * * *       * *      * * * * 
        *  * * * * * * * * * *        *      * * * * *  
                                              * * * * 
                                               * * *
                                                * * 
                                                 *
"""

# 7 :  
"""
for i in range(1,6):   # 2  
    for k in range(1,i): # 1,2
        print(" ",end=" ")
    for j in range(5,i-1,-1):# 5 ,1 
        print("*",end=" ")   # * * * * * 
    print()                  #   * * * * 
"""

#10 : 
"""
for i in range(1,6):   # 2  
    for k in range(1,i): # 1,2
        print(" ",end="")
    for j in range(5,i-1,-1):# 5 ,1 
        print("*",end=" ")   #
    print()                  #    
"""

# 9:

"""
for i in range(1,6):  # 1 
    for k in range(5,i,-1):  # 5 ,1
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
# 8 : 
"""
for i in range(1,6):  # 1 
    for k in range(5,i,-1):  # 5 ,1
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""

# 11 : 

"""for i in range(1,5):  # 1 
    for k in range(5,i,-1):  # 5 ,1
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,6):   # 2  
    for k in range(1,i): # 1,2
        print(" ",end="")
    for j in range(5,i-1,-1):# 5 ,1 
        print("*",end=" ")   #
    print()                  #    
"""

# while  loop  : 
"""
syntax : 

i =intial value 
while  condition  :
    print()
    i+=1 
"""

# 1-100 : 
"""i=1 
while (i <=100) : 
    print(i,end=" ")
    i+=1  # i = i+1 
"""
# while True :
"""
syntax : 

i= intial value 
while True :
    print()
    i+=1
"""
"""
i=1 
while True :
    print(i,end=" ")
    i+=1
    if i==10 :
        break
"""
"""
* * * * *  
*       *
*       *
*       *
* * * * * 
"""

for  i in range(1,6) :
    for  j in range(1,6):
        if i==1 or i==5 or j==1 or j==5 :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()

