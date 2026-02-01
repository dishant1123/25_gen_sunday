"""
file handling  :  txt file 

1. read   ==> r:  file  read , exiting  file 
2. write  ==> w:  file  write + new file  create + exiting  file ==> overwrite 
3. append ==> a:  file  write + exiting  file ==> last add (append) 

function : open(), close() ,seek() 

 ==> with  open("file_name","mode") as f 
 ==> f.open() 
 ==> f.close() 
 ==> f.seek() ==> cursor  move 
"""

# write :  new file  create + exiting  file ==> overwrite
"""
with  open("Rohit.txt","w") as f : 
    f.write("my name is  rohit.\n")
    f.write("my age is  21.\n")
    f.write("my hobby is  playing cricket.\n")
    f.write("live in dehgam.\n")
    f.close()
"""
    
# write  mode  : exiting  file  ==> overwrite 

"""
with  open("Rohit.txt","w") as f :
    f.write("study in royal.\n")
    f.write("dream is to meet narendra modi.\n")
    f.close()
"""
# append mode :     new file  create + exiting  file ==> last add 

"""with  open("dev.txt","a") as f : 
    f.write("my name is  dev.\n")
    f.write("my age is  20.\n")
    f.write("my hobby is  playing football.\n")
    f.write("live in ahemadabad.\n")
    f.close()
"""
# append mode :     exiting  file ==> last add
"""with  open("dev.txt","a") as f : 
    f.write("study in royal.\n")
    f.write("dream is to meet narendra modi.\n")
    f.close()

"""

# read : exiting  file . 

"""with open("Rohit.txt","r") as f :
    # context= f.read()  # read all file
    # context= f.readline()  # read line by line only  first  line 
    context= f.readlines()  # read line by line  store in  to the list
    
    print(context)
"""
# task :1 
"""
ask user to enter the string  and seprate the vowel and consonant in two different file like vowel.txt and  consonant.txt

input  : "my name is rohit"
output :
    vowel.txt  ==>   ae i oi 
    consonant.txt  ==>  my nm s rht
"""

"""
4. r+ : read + write  ==> exiting file  
5. w+ : read + write ==> new create file  ==> exiting file  ==> overwrite
6. a+ : read + write ==> new create file  ==> exiting file  ==> last add

"""

# r+ : 
"""with open("Rohit.txt","r+") as f :
    f.write("my name is rohit thakkar.\n")
    f.write("age is 20.")
    f.seek(0)
    r= f.read()
    print(r)
    f.close()
# my name in royal
"""

# w+ :
"""
with open("Rohit.txt","w+") as f :
    f.write("favorite cricketer is  virat kohli.\n")
    f.write("favorite footballer is  neymar.\n")
    f.write("live in dehgam.\n")
    f.writelines(["study in royal.","dream is to meet narendra modi."])
    f.seek(0)
    r= f.read()
    print(r)
    f.close()
"""

# a+ :
with open("Rohit.txt","a+") as f :
    # f.write("invest in stock market.\n")
    # f.write("best frnd name is dev.\n")
    f.seek(0)
    r= f.read()
    print(r)
    f.close()

"""
task :2 

 Write a Python program to read a text file and do following: 
    1. Print no. of words 2. Print no. statements . 
    friends.txt.
Friends are crazy, Friends are naughty !
Friends are honest, Friends are  best !
Friends are like keygen, friends are like license key !
We are nothing without friends, Life is not possible without friends !
"""

"""
task :3 

Write a Python program to reverse the content of a one file and store it in second file and also convert content of second 
file into uppercase and store it in third file and also count number of Vowels in third file and also print only 2nd line from 
the content of third file.
Examples:
If data file one contains the following data:
Friends are crazy, Friends are naughty !
Friends are honest, Friends are  best !

Output 1:
! tseb  era sdneirF ,tsenoh era sdneirF
! ythguan era sdneirF ,yzarc era sdneirF

Output 2:
! TSEB  ERA SDNEIRF ,TSENOH ERA SDNEIRF
! YTHGUAN ERA SDNEIRF ,YZARC ERA SDNEIRF

Output 3:
Vowels = 22

Output 4:
! YTHGUAN ERA SDNEIRF ,YZARC ERA SDNEIRF
"""