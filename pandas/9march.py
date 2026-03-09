import pandas as pd 
import numpy as np

# join  : 

"""
users =pd.DataFrame({
    "user_id" :[1,2,3], 
    "name" :["ravi","raj","rahul"]
    
})
"""
# print(users)

"""msgs = pd.DataFrame({
    "user_id" :[1,1,2,4], 
    "msgs" : ["hi","hey","hello","hmm"]
})
"""
# print(msgs)

# result =pd.concat([users,msgs])
# result =pd.concat([users,msgs],axis=1)
# print(result)

# merge :  inner join  

"""result = users.merge(msgs)
print(result)

users.rename(columns={"user_id":"id"},inplace=True)
print(users)

result =users.merge(msgs,right_on="user_id",left_on="id")
result =users.merge(msgs,right_on="user_id",left_on="id",how="left")
result =users.merge(msgs,right_on="user_id",left_on="id",how="right")
result =users.merge(msgs,right_on="user_id",left_on="id",how="outer")
print(result)
"""

# with data set : 

movies = pd.read_csv("pandas\movies.csv")
directors = pd.read_csv("pandas\directors.csv")

movies.drop(columns ="Unnamed: 0",inplace=True)
directors.drop(columns ="Unnamed: 0",inplace=True)
# print(movies.head())
# print(directors.head())

df =movies.merge(directors,right_on="id",left_on="director_id")
# print(df.head())
# print(df.info())
# print(df.isnull().sum())

"""
1.select title, director_name, revenue from movies where vote_average > 7 
2.Get me the movies which were released in or after 2015 and having vote_average more than 7
3.Print title, vote_average and revenue of movies released on weekends . 
4. Print title, vote_average and director_name of top 10 popular movies

"""
# a= df.loc[df["vote_average"] > 7,['title','director_name','revenue']]
# print(a)

# b= df.loc[(df['vote_average'] > 7) & (df['year']>=2015),['title','director_name','vote_average','year']]
# print(b)

# c= df.loc[(df['day']=="Saturday") |(df['day']=="Sunday"),['title','director_name','vote_average','day'] ]
# print(c)

d=df.sort_values(by="popularity",ascending=False)[['title','popularity','vote_average',"director_name"]].head(10)

print(d)

"""
1.Top 10 popular movies
2.Highest rated (vote_average) movies
3.Number of movies released in a year
4.Movie with the highest budget in a year
5.Most popular director
6.Director producing high budget movies
7.Highest & lowest budget movies every month
8.Directors who did not directed any movie  
9.Top 10 most profitable movies
10.Print the titles of the movies directed by Christopher Nolan. Also print their count
Print number of movies directed by each director


"""
