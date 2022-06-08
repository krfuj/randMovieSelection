# Printing out a random movie from the top 20 movies.
import imdb
import random

# Creating a new instance of the IMDb class.
moviesDB = imdb.IMDb()


# Creating a list of the top 20 movies.
top = moviesDB.get_top250_movies()
movie_selection = []
print("Top 20 movies: ")
for movie in top[0:5]:
    movie_selection.append(movie)

# Printing out a random movie from the top 20 movies.
print(random.choice(movie_selection))




