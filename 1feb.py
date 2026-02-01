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

# task :1 
"""
ask user to enter the string  and seprate the vowel and consonant in two different file like vowel.txt and  consonant.txt

input  : "my name is rohit"
output :
    vowel.txt  ==>   ae i oi 
    consonant.txt  ==>  my nm s rht
"""