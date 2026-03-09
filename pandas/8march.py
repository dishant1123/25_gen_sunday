import  pandas as pd
import numpy as np
"""
use : 
1. read csv  ==> create  update delete rename 
2. data cleaning
3. data manipulation

"""
# seris  : 

"""a=pd.Series([1,23,45,67,89,90])
print(a)

b=pd.Series([1,23,45,67,89,90],index=['a','b','c','d','e','f'])
print(b)

print(a.min())
print(a.max())
print(a.mean())
print(a.median())
print(a.std())
print(a.size)
print(a.dtype)
print(a.shape)
print(a.values)
print(a.keys())
"""

# seris : drop dropna fillna head tail update add

"""
a=pd.Series([1,23,None,67,89,90],index=['a','b','c','d','e','f'])
print(a)
print(a.drop(index=['a','b','c']))  # col drop  
print(a.dropna())  # missing  value  drop  
print(a.fillna(value=99))  # missing  value  fill
print(a.head(2))  # first  2  row
print(a.tail(2))  # last  2  row
a['g']=100
a['b'] =10
print(a)
"""

# dataframe  : 

"""a=pd.DataFrame([
    ['rahul',23,90000],
    ['ramesh',45,10000],
    ['ravi',67,12000]
],columns=['name','age','salary'])

print(a)"""

"""b=pd.DataFrame({
    'name' : ['rahul',None,'ravi'],
    'age':[23,45,67],
    'salary':[90000,10000,None]
})
print(b)
print(b.dtypes)
b.rename(columns={"name":"first_name"},inplace=True)
b.drop(columns=['age'],inplace=True)
b['city']=['delhi','mumbai','bangalore']
b.drop(['age','city'],axis =1,inplace=True)
b.drop(0,axis =0,inplace=True)
b.drop([0,2],axis =0,inplace=True)
print(b.dropna())
print(b.fillna({'name':"ravish",'salary':100000}))
print(b.isnull().sum())  # count null value
print(b)
"""

# read csv  :

# df =pd.read_csv("pandas\mckinsey.csv")
"""
print(df)
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df.isnull().sum())
"""
# specific  column print  : 

# print(df['country'])
# print(df[['year','country']])

"""
df['next_year'] =df['year'] +3
print(df.head())

"""

# loc : explicit index 
# iloc  :  implicit index  

df =pd.read_csv("pandas\mckinsey.csv")

"""print(df.loc[1])
print(df.iloc[1])

slicing  : 
print(df.loc[5:13])
print(df.iloc[5:13])  # last excluded 

print(df.iloc[2:5,1:4])
print(df.loc[2:5,'year':'continent'])
print(df.loc[2:5,['year','continent','population']])

print(df.iloc[[1,4,6,8],[0,3,4]])
print(df.iloc[1:10:2])
print(df.loc[2:10:2])
print(df.iloc[[2,7]])
print(df.loc[[2,7]])

print(df.iloc[-1])  # last  row  print  
print(df.loc[-1])  # error 

"""

# set_index : 
"""df.index =np.arange(1,1705)
print(df)
temp =df.set_index('country')
print(temp)
"""

# year ==2002    ==> print  infomation 

"""df= df.loc[df['year']==2002]
print(df)
"""

# sorting : 

# df= df.sort_values(by="life_exp")  # by default  : asc  to desc 
# df= df.sort_values(by="gdp_cap",ascending=False)   
# df= df.sort_values(by=['year','life_exp'])   
# df= df.sort_values(by=['year','population'],ascending=False)
df= df.sort_values(by=['year','gdp_cap'],ascending=[True,False])   


# print(df.head(50))
print(df.tail(50))

