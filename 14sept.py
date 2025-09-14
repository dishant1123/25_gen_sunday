# dict : mutable  ==> key value  pair  ==> changes in dict 

"""
d1={"raj":90,"simran":89,"rohit":88}
# raj ==> key 90 ==> value 90   simran ==> key ==> 89 value 

print(d1)
print(type(d1))
"""

"""
d2={90 :67, 67 :"phy"}
print(d2)
print(type(d2))
"""

# built in function  : len  min max sorted sum 

"""
d1={"raj":90,"simran":89,"rohit":88}

print(len(d1))
print(min(d1))
print(max(d1))
print(sorted(d1))  # asc to desc
# print(sum(d1)) # error 
"""

# slicing  :   no  poss in dict. 

"""
d1={"raj":90,"simran":89,"rohit":88}
print(d1[0])
"""

# add : 
"""
d1={"raj":90,"simran":89,"rohit":88}

d1["kishan"]=99
d1["raj"]=100
print(d1)
"""

# method  : 

# d1={"raj":90,"simran":89,"rohit":88}

"""d1.clear()
print(d1)
"""

"""print(d1.keys())
print(d1.values())
print(d1.items())"""

# print(d1.get("raj"))  # arg  ==> key output  ==> value 

"""
l2=["vidhya","riya"]
# {"vidhya":100, "riya":100}
d2 = dict.fromkeys(l2,100)
d2["riya"] =900
print(d2)
"""
"""d2={"riya":90,"vidhya":89}

d1.update(d2)
print(d1)
"""
# d1={"raj":90,"simran":89,"rohit":88,"dev":99}

"""d1.pop("raj")  # key ==> remove  
print(d1)
"""

"""d1.popitem()  # last key value  delete 
print(d1)
"""
"""
d1.setdefault("raj",99)
print(d1)
"""

"""
task  :1 
ask user to  enter the  5 student  name  and  marks  store in to the dict. 

ram 90  sita  88  laxman 78 baldev 56  bhudev 23
output  :d1={"ram":90,"sita":88,"laxman":78,"baldev":56,"bhudev":23}

"""

d1={}

for i in range(3) :
    name =input("enter the  name :")
    marks =int(input("enter the  marks :"))
    d1[name] =marks
print(d1)   # {'dev': 90, 'daksh': 67, 'rohit': 99}

sorted_marks =sorted(d1.values())
print(sorted_marks)   # [67 90, 99]

d2={} 
for j in sorted_marks:   # # [67 90, 99]  # j =67 
    for name , marks in d1.items() :  ## {'dev': 90, 'daksh': 67, 'rohit': 99}
        if j ==marks : 
            d2[name]=j
print(d2)


"""
HW :

3. Make a Python program to count letters of the word: MISSISSIPPI. 
Your program should store them in a dictionary as: {"M":1, "I":4, "S":4, "P":2}. Next, generalize this program for any word entered by user."""

# 4.result = {'Science': [88, 89, 62, 95, 50], 'Language': [77, 78, 84, 80, 60]}
# Expected Output: [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]

