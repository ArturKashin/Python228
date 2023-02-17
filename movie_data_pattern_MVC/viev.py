def my_decorator(title):
    def inner(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, '='))
            ans = func(*args, **kwargs)
            print(f"{'=' * 50}\n")
            return ans
        return wrap
    return inner


class UserInterface:
    @my_decorator('Редактирование данных каталога фильмов:')
    def waiting_user_input(self):
        print("Действие с фильмами:")
        print("1 - добавление фильм\n"
              "2 - каталог фильмов\n"
              "3 - просмотр определенного фильма\n"
              "4 - удаление фильма\n"
              "q - выход из программы")
        user_answer = input("Выберете вариант: ")
        return user_answer

    @my_decorator('Добавление фильма')
    def add_user_movie(self):
        dict_movie = {
            "название фильма": None,
            "жанр": None,
            "режиссер": None,
            "год выпуска": None,
            "продолжительность фильма": None,
            "студия": None,
            "актер": None
        }
        for key in dict_movie:
            dict_movie[key] = input(f"Введите {key} фильма: ")
        return dict_movie

    @my_decorator('Каталог фильмов')
    def show_all_movies(self, movies):
        for ind, movie in enumerate(movies, start=1):
            print(f"{ind}. {movie}")

    @my_decorator('Ввод названия фильма')
    def get_user_movie(self):
        name_movie = input('Введите название фильма: ')
        return name_movie

    @my_decorator('Просмотр определенного фильма')
    def show_single_movie(self, movie):
        for key in movie:
            print(f"{key} фильма - {movie[key]}")

    @my_decorator('Сообщение об ошибки')
    def show_incorrect_get_movie(self, movie):
        print(f"Фильм {movie} отсутствует в списке фильмов")

    @my_decorator('Удаление фильма')
    def show_remove_movie(self, movie):
        print(f"Фильм {movie} успешно удален")

    @my_decorator('Сообщение об ошибки')
    def show_incorrect_answer_error(self, answer):
        print(f"Меню с выбором {answer} не существует")
