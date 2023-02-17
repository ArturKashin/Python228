import pickle
import os


class Movie:
    def __init__(self, film_title, genre, director, year_of_release, duration,
                 studio, actors):
        self.film_title = film_title
        self.genre = genre
        self.director = director
        self.year_of_release = year_of_release
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.film_title}, продолжительность: {self.duration}"


class MovieModel:
    def __init__(self):
        self.db_name = 'db.txt'
        self.movies = self.load_data()    # --> {}

    def add_movie(self, dict_movie):
        movie = Movie(*dict_movie.values())
        self.movies[movie.film_title] = movie

    def get_all_movies(self):
        return self.movies.values()

    def get_single_movie(self, get_movie):
        movie = self.movies[get_movie]
        dict_movie = {
            "Название фильма": movie.film_title,
            "Жанр": movie.genre,
            "Режиссер": movie.director,
            "Год выпуска": movie.year_of_release,
            "Продолжительность фильма": movie.duration,
            "Студия": movie.studio,
            "Актеры": movie.actors
        }
        return dict_movie

    def remove_movie(self, movie):
        return self.movies.pop(movie)

    def save_data(self):
        with open(self.db_name, 'wb') as file:
            pickle.dump(self.movies, file)

    def load_data(self):
        # проверка существует ли файл
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as file:
                return pickle.load(file)
        else:
            return dict()
