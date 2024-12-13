favorite_movies = ["Inception", "The Dark Knight", "Pulp Fiction", "The Matrix", "Interstellar"]
def display_movies():
    print("Favorite Movies:")
    for index, movie in enumerate(favorite_movies, 1):
        print(f"{index}. {movie}")
def add_movie(movie):
    favorite_movies.append(movie)
    print(f"'{movie}' has been added to the list!")
    def find_movie_index(movie):
    if movie in favorite_movies:
        return favorite_movies.index(movie)
    else:
        return -1
