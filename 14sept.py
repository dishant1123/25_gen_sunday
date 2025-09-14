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

d1={"raj":90,"simran":89,"rohit":88}

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
d1={"raj":90,"simran":89,"rohit":88,"dev":99}

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