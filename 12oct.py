# set :mutable,no repeation allowed in set , unordered collection  

"""
s1={100,1,2,3,4,4,5,5,6,7,8,9,"harpal"}   

print(s1)
print(type(s1))
"""
# empty set : 

"""
s1=set()
print(s1)
print(type(s1))
"""

# built in function  : min max sorted sum  

"""
s1={100,1,2,3,4,4,5,5,6,7,8,9,99}   

print(len(s1))
print(min(s1))
print(max(s1))
print(sum(s1))
print(sorted(s1))  # asc to desc 
print(sorted(s1,reverse=True))  # desc to asc
"""
# slicing  : not  poss in set  because set is unordered collection

"""
s1={100,1,2,3,4,4,5,5,6,7,8,9,99}   

print(s1[3 ])
print(s1[3 :5 ])
"""
# method  : 
# s1={10,1,2,3,4,4,5,5,6,7,8,9,99}   

"""s1.add(900)
print(s1)

s1.clear()
print(s1)
"""
"""s2 =s1.copy()
print(s2)
"""
# s1.remove(110)
# print(s1)

# s1.discard(909)
# print(s1)

# s1.pop()
# print(s1)

"""s2={"triputi","om","harpal"}
s1.update(s2)
print(s1)
"""

# set theory  : union , intersection , difference , symmetric difference

s1 ={2,3,4}
s2={1,2,4,6,7}
s3={1,2,3,4,5,6,7} 

"""
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))  # s1-s2  ==> s1 remaining element after removing s2 element from s1
print(s2.difference(s1))  # s2-s1 

print(s1.symmetric_difference(s2))  # all element except common element
"""
"""s1.intersection_update(s2)
print(s1)
"""

"""s1.difference_update(s2)
print(s1)
"""
"""s1.symmetric_difference_update(s2)
print(s1)
"""

# subset ,superset ,disjoint :  
"""s1 ={2,3,4}
s2={1,2,3,4,6,7}
s3={1,2,3,4,5,6,7} 

print(s1.issubset(s2))
print(s1.isdisjoint(s2))

print(s3.issuperset(s2))
"""

#list duplicate element : 
"""l1=[1,2,2,3,34,4,5,6,6,7,8,8,9,9]

l2 =set(l1)
print(list(l2))
"""

# frozen set : immutable 

fz = frozenset({1,2,3,4,55,55,6})
print(fz)

print(type(fz))