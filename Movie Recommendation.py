import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def combine_features(row):
    try :
        return row['keywords']+ ' '+ row['cast']+ ' '+ row['genres']+ ' '+ row['director']
    except :
        print('Error:', row)

def get_index_from_title(title):
    return df[df.title == title]['index'].values[0]

def get_title_from_index(index):
    return df[df.index == index]['title'].values[0]

df = pd.read_csv('movie_dataset.csv')
features = ['cast', 'genres', 'director', 'keywords']
for feature in features:
    df[feature] = df[feature].fillna('')

df['combined_features'] = df.apply(combine_features, axis =1)

cv = CountVectorizer()
cv_fit = cv.fit_transform(df['combined_features'])
count_matrix = cv_fit.toarray()
similarity = cosine_similarity(count_matrix)
movie_user_likes = 'Gone Girl'
movie_index = get_index_from_title(movie_user_likes)

similar_movies = list(enumerate(similarity[movie_index]))
sorted_similar_movies = sorted(similar_movies, key = lambda x : x[1], reverse =True)

i = 0
for movie in sorted_similar_movies:
    print(get_title_from_index(movie[0]))
    i+= 1
    if i == 10 :
        break
