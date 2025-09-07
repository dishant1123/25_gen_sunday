# nested  loop  : 
"""
user  2 range : 

starting  ending :

for i in range(start,end):
    for j in range(1,i):
"""

# prime  , perfect , amg , strong  , twin  , pelidrome : 

"""
start = int(input("enter the starting number  : "))
end = int(input("enter the ending number  : "))

for i in range(start,end+1) :   # 10 -100
    count =0    # 0 
    for j in range(1,i+1):  # 1,11
        if i % j==0  :   # 10 % 1
            count +=1
    if count ==2 :
        print(i,end=" ")
"""

# strong number  : 

"""
start = int(input("enter the starting number  : "))
end = int(input("enter the ending number  : "))

for i in range(start ,end+1) :   # 123 -1000
    sum = 0 
    digit = len(str(i))
    temp = i 
    for j in range(digit):
        r=  temp %10 
        fact =1 
        for k in range(1,r+1):
            fact = fact *k
        sum =sum +fact
        temp = temp //10 
    if sum == i : 
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
for i in range(1,6): 
    for j in range(1,6):
        print("*",end=" ")
    print()
"""
# 2 : 
"""
for i in range(1,6): 
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
# 3 : 
"""
for i in range(1,6): 
    for j in range(6,i,-1):
        print("*",end=" ")
    print()

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
for i in range(1,6): 
    for k in range(1,i):
        print(" ",end=" ")
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()
"""
# 10 : 
"""
for i in range(1,6): 
    for k in range(1,i):
        print(" ",end="")
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()
"""

#9:
"""
for i in range(1,6): 
    for k in range(5,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
#8: 
"""
for i in range(1,6): 
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""

#11:
"""for i in range(1,6): 
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,6): 
    for k in range(1,i):
        print(" ",end="")
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()
"""
"""
12 :       13 :         14 :             15 :           16 :         17 :
 
* * * * *   *           * * * * *         *           * * * * *      * 
*       *   * *         *     *          * *           *     *      * *
*       *   *   *       *   *           *   *           *   *      *   * 
*       *   *     *     * *            *     *           * *      *     * 
* * * * *   * * * * *   *             * * * * *           *      *       *
                                                                  *     *
                                                                   *   *
                                                                    * *
                                                                     *
"""  
#12 : 
"""for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5 :
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
"""
# 13 : 

"""
for i in range(1,6): 
    for j in range(1,i+1):
        if i==1 or  i==j or i==5 or  j==1: 
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
"""
#14 :
"""for i in range(5,0,-1): 
    for j in range(1,i+1):
        if  i==j or j==1  or i==1  or j==5 or i==5: 
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
"""

# 15 : 

"""
for i in range(1,6): 
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        if i==1 or i==j or i==5 or j==1:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
"""

# 16 :

"""
for i in range(5,0,-1): 
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        if i==1 or i==j or i==5 or j==1:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
"""
# 17 : 
"""for i in range(1,5): 
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        if i==1 or i==j or j==1:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
for i in range(5,0,-1): 
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        if i==1 or i==j or j==1:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
"""

# while: 
"""
syntax : 

i = intial value
while con : 
    statement
    i = i+1  # i+=1
"""

# 1-100 : 

"""
i=1 
while i<=100 :
    print(i,end=" ")
    i+=1
"""

# while true  : 

"""
syntax : 

i=intial value
while True :
    statement
    i = i+1  # i+=1
    break 
"""

# 1-100 : 
"""
i=1 
while True :
    print(i,end=" ")
    i+=1
    if i==100 :
        break 
"""

a=int(input("enter the  number  1: ")) 
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
in this  code  you have to given 2 more choice  : 

1. exit 
2. add new  number 
"""