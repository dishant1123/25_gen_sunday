# loop  : 
"""
1. for :  entry  control loop    
2.  while  :  exit 
3 . while  True : exit 
"""

'''
syntax : 

for  (variable name) in range(start , stop  , step) : 
    print()
'''

"""
for i in range(1,101,2):
    print(i,end=" ")
"""

# 100 -1 : 

"""for i in range(100,1,-1):
    print(i,end=" ")
"""
#                        -3 -2 -1  0  1 2 3 4 5 6    

"""
for x in range(-90,-2,):
    print(x,end=" ")
"""

# break continue pass :

# break : 
"""   # ouptut : 0 1 2 3 4
for i in range(10):
    if i ==5 :
        break 
    print(i,end=" ")
else :
    print("rishi")
"""
# contunie : 
"""
for i in range(10):
    if i ==5 :
        continue 
    print(i,end=" ")
else :
    print("rishi")  # for  else  == > print  when  you  contunie the  loop 
"""

# pass : 
"""for i in range(10):
    if i ==5 :
        pass 
    print(i,end=" ")
else :
    print("rishi")  # for  else  == > print  when  you  contunie the  loop 

"""

# nested loop  : 

"""
for i in range(10):   #  0  1 
    for j  in range(2,10,2):  # 2 4 6 8  
        print(j)
    print(i)  # 0  1 
"""    

"""
for i in range(10):   #  0  1 
    for j  in range(2,10):  # 2 4 6 8  
        if j==5 :
            break 
        print("j :",j)
    if i==8 :
        break
    print("i :",i)  # 0 -7 
"""

# while  : 

"""
i =intial 
while con : 
    print(i)
    i+=1 
"""

"""i=1 
while i<10 : 
    print(i)
    i+=1
"""

# while true : 
i=1
while True :
    print("rishi")
    i+=1
    if i==10 :
        break
