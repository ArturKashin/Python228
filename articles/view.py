def decorator(title):
    def inner(func):
        def wrap(*args, **kwargs):
            print(title.center(50, '='))
            ans = func(*args, **kwargs)
            print(f"{'=' * 50}\n")
            return ans
        return wrap
    return inner


class UserInterface:
    @decorator(" Ввод пользовательских данных ")
    def wait_user_answer(self):
        print('Действие со статьями:')
        print('1 - Создание статьи\n'
              '2 - Просмотр статей\n'
              '3 - просмотр определенной статьи\n'
              '4 - удаление статьи\n'
              'q - выход из программы')
        user_answer = input('Выберете вариант действия: ')
        return user_answer

    @decorator(' Создание статьи ')
    def add_user_article(self):
        dict_article = {
            'название': None,
            'автор': None,
            'количество страниц': None,
            'описание': None
        }
        for key in dict_article:
            dict_article[key] = input(f'Введите {key} статьи: ')
        return dict_article

    @decorator(' Список статей ')
    def show_all_articles(self, articles):
        for ind, article in enumerate(articles, start=1):
            print(f"{ind}. {article}")

    @decorator(' Ввод названия статьи ')
    def get_user_article(self):
        user_article = input('Введите название статьи: ')
        return user_article

    @decorator(' Просмотр статьи ')
    def show_single_article(self, article):
        for key in article:
            print(f"{key} статьи - {article[key]}")

    @decorator(' Сообщение об ошибки ')
    def show_incorrect_title_error(self, user_title):
        print(f"Статьи с названием {user_title} не существует")

    @decorator('Удаление статьи')
    def remove_single_article(self, article):
        print(f"Статья {article} была удалена")

    @decorator(' Сообщение об ошибки ')
    def show_incorrect_answer_error(self, answer):
        print(f"Вариант {answer} не существует")
