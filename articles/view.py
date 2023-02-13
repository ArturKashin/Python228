class UserInterface:
    def decorator(*args):
        def inner(func):
            print(str(*args).center(50, '='))
            func(*args)
            print(f"{'=' * 50}\n")
        return inner

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





