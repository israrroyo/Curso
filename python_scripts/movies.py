# First import urllib for downloading and uncompress the file
import urllib.request
import zipfile
import os
import pandas as pd

DEBUG = True

# This is the URL for the public data
url = "http://files.grouplens.org/datasets/movielens/ml-latest-small.zip"

# This is the working directory
working_dir = "../data/movies/"

# Destination filename
file_name = working_dir + "movies.zip"

# Download the file from `url` and save it locally under `file_name`:
if os.path.isfile(file_name):
    if DEBUG:
        print('Data is already downloaded')
else:
    if DEBUG:
        print("Downloading file")
    urllib.request.urlretrieve(url, file_name)

# We already know the expected files so:
expected_files = [
    'links.csv',
    'movies.csv',
    'ratings.csv',
    'README.txt',
    'tags.csv']

# There's an extra dir level in thwe extracted files
inner_dir = "ml-latest-small/"
# I want to know the names of the extracted files
file_names = os.listdir(working_dir + inner_dir)

if file_names == expected_files:
    print("You already have the data files, check it!")
else:
    # This is the code for uncompress hte zipfile
    path_to_zip_file = working_dir + "movies.zip"
    # Reference to zipfile
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    print("Extracting files")
    zip_ref.extractall(working_dir)
    # Is important to use .close()
    zip_ref.close()

# movie.ID mv.ID MV.ID MV_ID
movie_names = ['movie_id', 'title', 'genres']
rating_names = ['user_id', 'movie_id', 'rating', 'timestamp']

# Reading the files needed for this analysis
movies = pd.read_csv(
    working_dir +
    inner_dir +
    expected_files[1],
    sep=',',
    names=movie_names)
ratings = pd.read_csv(
    working_dir +
    inner_dir +
    expected_files[2],
    sep=',',
    names=rating_names)


# Let's print the first lines of each dataframe
if DEBUG:
    print(movies.head())
    print(ratings.head())

print("The names of our new data frames are:")
print(list(movies.columns.values))
print(list(ratings.columns.values))

print("The dimension of the dataframes are:")
print(movies.count())
print(ratings.count())

rated_movies = pd.merge(movies, ratings, on='movie_id')
rated_movies = rated_movies.sort_values('rating', ascending=False)

# Number of movies: 9126
# Number of evaluations: 100005

top20 = rated_movies.head(20)
print(top20)
#print(top20)
# Rated movies names:
# ['movie_id', 'title', 'genres', 'user_id', 'rating', 'timestamp']

# top5_dict = {}

# for i in range(5):
#     title = top20[i]['title']
#     for j in rated_movies:
#         if rated_movies[j]['title'] == title:
#             top5_dict[title] = rated_movies[j]


top5 = top20.drop_duplicates('movie_id').head(5)
print(top5)

dataset_array = []

for i in top5['title']:
	    dataset_array.append(i)
print(dataset_array)

res = rated_movies[rated_movies['title'].isin(dataset_array)]
agrupacion = res.groupby('title')['rating'].count()
print(agrupacion)
suma = agrupacion.sum()
print(suma)




# print(rated_movies.head(20))
# if DEBUG:
#     print(list(rated_movies.columns.values

# print(rated_movies.head(20))
# if DEBUG:
#     print(list(rated_movies.columns.values))















