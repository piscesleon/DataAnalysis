import os
import pandas as pd

os.chdir('D:\\Project\\Python\\Data\\ch02\\movielens')

unames=['user_id','gender','age','occupation','zip']
users=pd.read_table('users.dat', sep='::', header=None, names=unames)
print(type(users))

rnames=['user_id', 'movie_id', 'rating', 'timestamp']
ratings=pd.read_table('ratings.dat', sep='::', header=None, names=rnames)

mnames=['movie_id', 'title', 'genres']
movies=pd.read_table('movies.dat', sep='::', header=None, names=mnames)

print(users[:5])
print(ratings[:5])
print(movies[:5])

data=pd.merge(pd.merge(ratings, users), movies)
print(data)
print(data.ix[0])

mean_ratings=data.pivot_table('rating', index='title', columns='gender', aggfunc='mean') #Note: keyword is 'index' and 'columns', not 'rows' and 'cols' as the book writes
print(mean_ratings)

ratings_by_title=data.groupby('title').size()
active_titles=ratings_by_title.index[ratings_by_title>=250]
print(active_titles)