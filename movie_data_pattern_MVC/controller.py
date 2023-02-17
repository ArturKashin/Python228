from viev import UserInterface
from model import MovieModel


class Controller:
    def __init__(self):
        self.user_interface = UserInterface()
        self.movie_model = MovieModel()

    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_interface.waiting_user_input()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == '1':
            movie = self.user_interface.add_user_movie()
            self.movie_model.add_movie(movie)

        elif answer == '2':
            movies = self.movie_model.get_all_movies()
            self.user_interface.show_all_movies(movies)

        elif answer == '3':
            movie = self.user_interface.get_user_movie()
            try:
                get_movie = self.movie_model.get_single_movie(movie)
            except KeyError:
                self.user_interface.show_incorrect_get_movie(movie)
            else:
                self.user_interface.show_single_movie(get_movie)

        elif answer == '4':
            movie = self.user_interface.get_user_movie()
            try:
                get_movie = self.movie_model.remove_movie(movie)
            except KeyError:
                self.user_interface.show_incorrect_get_movie(movie)
            else:
                self.user_interface.show_remove_movie(get_movie)

        elif answer == 'q':
            self.movie_model.save_data()

        else:
            self.user_interface.show_incorrect_answer_error(answer)
