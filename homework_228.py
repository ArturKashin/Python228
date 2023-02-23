# ======================================================
# Написать программу разведения котов и кошек, с предполагаемым количеством котят
# import random
#
#
# class Cat:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def __str__(self):
#         sex = 'неизвестно'
#         if self.sex == 'F':
#             sex = 'girl'
#         if self.sex == 'M':
#             sex = 'boy'
#         return f"{self.name} is good {sex}!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age='{self.age}', sex='{self.sex}')"
#
#     def __add__(self, other):
#         if self.sex == other.sex:
#             raise ValueError('Невозможно разводить котят с родителями одинаковых полов')
#         if self.age < 1 or other.age < 1:
#             raise ValueError('Возраст котят меньше года')
#         else:
#             list_cats = []
#             for i in range(random.randint(1, 5)):
#                 list_cats.append(Cat('No name', 0, random.choice(['F', 'M'])))
#             return list_cats
#
#
# cat1 = Cat('Tom', 4, 'M')
# print(cat1)
# cat2 = Cat('Elsa', 4, 'F')
# print(cat2)
# cat3 = cat1 + cat2
# print(cat3)


# ======================================================
# Создать класс Shape и три дочерних класса: Square, Rectangle, Triangle

# from abc import ABC, abstractmethod
#
# import math
#
#
# class Shape:
#     def __init__(self, color):
#         self.color = color
#
#     @abstractmethod
#     def perimeter(self):
#         raise "В одном из классов отсутствует метод perimeter"
#
#     @abstractmethod
#     def area(self):
#         raise "В одном из классов отсутствует метод area"
#
#     @abstractmethod
#     def print_shapes(self):
#         raise "В одном из классов отсутствует метод print_shapes"
#
#     @abstractmethod
#     def print_info(self):
#         raise "В одном из классов отсутствует метод print_info"
#
#
# class Square(Shape):
#     def __init__(self, side, color):
#         super().__init__(color)
#         self.side = side
#
#     def perimeter(self):
#         return self.side * 4
#
#     def area(self):
#         return self.side ** 2
#
#     def print_shapes(self):
#         for i in range(self.side):
#             print('*' * self.side)
#
#     def print_info(self):
#         print('===Квадрат===')
#         print(f"Сторона: {self.side}\nЦвет: {self.color}\nПлощадь: {self.area()}\nПериметр: {self.perimeter()}")
#         self.print_shapes()
#         print()
#
#
# class Rectangle(Shape):
#     def __init__(self, length, width, color):
#         super().__init__(color)
#         self.length = length
#         self.width = width
#
#     def perimeter(self):
#         return (self.width + self.length) * 2
#
#     def area(self):
#         return self.width * self.length
#
#     def print_shapes(self):
#         for i in range(self.length):
#             print('*' * self.width)
#
#     def print_info(self):
#         print('===Прямоугольник===')
#         print(f"Длина: {self.length}\nШирина: {self.width}\nЦвет: {self.color}\nПлощадь: {self.area()}"
#               f"\nПериметр: {self.perimeter()}")
#         self.print_shapes()
#         print()
#
#
# class Triangle(Shape):
#     def __init__(self, side_1, side_2, side_3, color):
#         super().__init__(color)
#         self.side_1 = side_1
#         self.side_2 = side_2
#         self.side_3 = side_3
#
#     def perimeter(self):
#         return self.side_1 + self.side_2 + self.side_3
#
#     def area(self):
#         height_triangle = (self.side_2**2 - (self.side_1 / 2)**2)**0.5
#         return round(0.5 * self.side_1 * height_triangle, 2)
#
#     def print_shapes(self):
#         s = 1
#         a = math.floor(self.side_1 / 2)
#         for i in range(self.side_2):
#             print(' ' * a, '*' * s)
#             s += 2
#             a -= 1
#
#     def print_info(self):
#         print('===Треугольник===')
#         print(f"Сторона 1: {self.side_1}\nСторона 2: {self.side_2}\nСторона 3: {self.side_3}\nЦвет: {self.color}"
#               f"\nПлощадь: {self.area()}\nПериметр: {self.perimeter()}")
#         self.print_shapes()
#         print()
#
#
# list_shapes = [Square(3, 'red'), Rectangle(3, 7, 'green'), Triangle(11, 6, 6, 'yellow')]
# for i in list_shapes:
#     i.print_info()


# ======================================================
# Создать класс Power, который будет декорировать функцию. Функция возвращает результат умножения двух чисел
# (a = 2, b = 2), а класс возводит их в степень, которую принимает декоратор.


# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, function):
#         def wrap(*args, **kwargs):
#             res = function(*args, **kwargs)
#             return res ** self.arg
#         return wrap
#
#
# @Power(3)
# def multiplication(a, b):
#     return a * b
#
#
# print(multiplication(2, 2))


# ======================================================
# Создать класс "Треугольник", свойства - длины трех сторон. Правильность задания свойств должны
# проверяться через дескриптор на ввод положительных целых числовых значений. Предусмотреть в классе
# методы проверки существования треугольника


# class DescriptTriangle:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError(f"Стороны треугольника должны быть больше нуля")
#         instance.__dict__[self.name] = value
#
#
# class Triangle:
#     a = DescriptTriangle()
#     b = DescriptTriangle()
#     c = DescriptTriangle()
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def check_triangle(self):
#         a, b, c = self.a, self.b, self.c
#         if a + b > c and b + c > a and c + a > b:
#             print(f'Треугольник со сторонами ({a}, {b}, {c}) существует.')
#         else:
#             print(f'Треугольник со сторонами ({a}, {b}, {c}) не существует.')
#
#
# t1 = Triangle(2, 5, 6)
# t2 = Triangle(5, 2, 8)
# t3 = Triangle(7, 3, 6)
#
# t1.check_triangle()
# t2.check_triangle()
# t3.check_triangle()


# ======================================================
# Создать класс (любой). Свойства класса сохранить в JSON объект

# import json
#
#
# class Bird:
#     def __init__(self, clas, kingdom, family, genus):
#         self.clas = clas
#         self.kingdom = kingdom
#         self.family = family
#         self.genus = genus
#
#     def __str__(self):
#         return f"Класс: {self.clas}\nЦарство: {self.kingdom}\nСемейство: {self.family}\n" \
#                f"Род: {self.genus}"
#
#
# # Экземпляр класса Bird
# bird_1 = Bird("Птицы", "Животные", "Ястребиные", "Орлы")
# print(f"{'=' * 50}\nСписок свойств экземпляра bird_1, класса Bird")
# print(f"{bird_1.__dict__}\n{'=' * 50}")
#
# # Сохранения в файл формата JSON
# with open("instance_classes.json", "w") as file:
#     json.dump(bird_1.__dict__, file, ensure_ascii=False)
#
# # Декодирование словаря из формата JSON в Python
# with open("instance_classes.json", "r") as file:
#     data = json.load(file)
#
# # Создание нового экземпляра класса Bird со свойствами декодированными из JSON формата
# bird_2 = Bird(**data)
# print(f"Метод __str__ класса Bird для экземпляра bird_2\n\n{bird_2}")


# ======================================================
# Вложенный словарь JSON


# import json
# from random import choice
#
#
# def get_person():
#     name = ""
#     tel = ""
#
#     letter = ['ф', 'в', 'а', 'п', 'р', 'е', 'к', 'у']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letter)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {'name': name, 'tel': tel}
#     return person
#
#
# def write_json(person_dict):
#     try:
#         date = json.load(open('persons.json'))
#     except FileNotFoundError:
#         date = {}
#
#     key = ""
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(key) != 9:
#         key += choice(nums)
#
#     date[key] = person_dict
#     with open('persons.json', 'w') as file:
#         json.dump(date, file, indent=2)
#
#
# for i in range(5):
#     write_json(get_person())


# ======================================================
# Есть некоторый словарь который хранит название стран и столиц


# import json
#
#
# class Country:
#     @staticmethod
#     def print_info():
#         print(
#             f"{'*' * 30}\nВыбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
#             f"4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы")
#
#     # Проверка на тип данных
#     @staticmethod
#     def str_data(text):
#         if not text.isalpha():
#             print(f"Ввод должен быть строчным типом данных")
#             return False
#         else:
#             return True
#
#     # Добавление данных
#     @staticmethod
#     def add_country():
#         country = input('Введите название страны (с заглавной буквы): ').capitalize()
#         capital = input('Введите название столицы страны (с заглавной буквы): ').capitalize()
#
#         if Country.str_data(country) and Country.str_data(capital):
#             try:
#                 data = json.load(open('country.json', encoding='utf-8'))
#             except FileNotFoundError:
#                 data = {}
#
#             data[country] = capital
#             with open('country.json', 'w', encoding='utf-8') as file:
#                 json.dump(data, file, indent=2, ensure_ascii=False)
#             print('Файл сохранен')
#
#     # Удаление данных
#     @staticmethod
#     def del_country():
#         try:
#             data = json.load(open('country.json', encoding='utf-8'))
#             del_country = input('Какую страну вы хотите удалить (с заглавной буквы): ').capitalize()
#             if del_country in data:
#                 data.pop(del_country)
#                 print(f"Страна {del_country} успешно удалена")
#
#                 with open('country.json', 'w', encoding='utf-8') as file:
#                     json.dump(data, file, indent=2, ensure_ascii=False)
#                     print('Файл сохранен')
#             else:
#                 print(f'Страна {del_country} отсутствует в списке стран')
#
#         except FileNotFoundError:
#             print('Файл не найден!')
#
#     # Поиск данных
#     @staticmethod
#     def data_search():
#         try:
#             data = json.load(open('country.json', encoding='utf-8'))
#             data_search = input('Введите страну или столицу для поиска: ').capitalize()
#             for key, val in data.items():
#                 if key == data_search:
#                     print(f"Результат найден -->> {data_search}: {val}")
#                     break
#                 elif val == data_search:
#                     print(f"Результат найден -->> {key}: {data_search}")
#                     break
#             else:
#                 print(f"'{data_search}' отсутствует в словаре")
#         except FileNotFoundError:
#             print('Файл не найден!')
#
#     # Редактирование данных
#     @staticmethod
#     def data_edit():
#         try:
#             data = json.load(open('country.json', encoding='utf-8'))
#             data_edit = input("Введите страну для редактирования данных: ").capitalize()
#             for key, val in data.items():
#                 if key == data_edit:
#                     print(f"Результат найден -->> {data_edit}: {val}")
#                     new_capital = input('Введите новое название столицы страны (с заглавной буквы): ').capitalize()
#                     if Country.str_data(new_capital):
#
#                         data[data_edit] = new_capital
#
#                         with open('country.json', 'w', encoding='utf-8') as file:
#                             json.dump(data, file, indent=2, ensure_ascii=False)
#                             print('Файл сохранен')
#                         break
#                     else:
#                         break
#             else:
#                 print(f"'{data_edit}' отсутствует в словаре")
#         except FileNotFoundError:
#             print('Файл не найден!')
#
#     # Просмотр данных
#     @staticmethod
#     def viewing_data():
#         try:
#             data = json.load(open('country.json', encoding='utf-8'))
#             print(data)
#         except FileNotFoundError:
#             print('Файл не найден!')
#
#
# def menu():
#     Country.print_info()
#     input_number = int(input('Ввод: '))
#
#     while input_number != 6:
#         if input_number == 1:
#             Country.add_country()
#
#         if input_number == 2:
#             Country.del_country()
#
#         if input_number == 3:
#             Country.data_search()
#
#         if input_number == 4:
#             Country.data_edit()
#
#         if input_number == 5:
#             Country.viewing_data()
#
#         Country.print_info()
#         input_number = int(input('Ввод: '))
#
#
# menu()
# print('Программа закрыта')


# ======================================================
# Считать данные из файла data2.csv

# import csv
#
# with open('data2.csv', 'r', encoding='utf-8') as file:
#     data2 = csv.reader(file, delimiter=';')
#     for i in data2:
#         print(i)


# ======================================================
# Реализовать парсинг данных из любого интернет ресурса с однотипными данными

# import csv
# import requests
# from bs4 import BeautifulSoup


# def get_html(url):
#     request = requests.get(url)
#     return request
#
#
# # функция записи в csv файл
# def write_csv(data):
#     with open('exchange_rate.csv', 'a') as file:
#         writer = csv.writer(file, lineterminator='\r', delimiter=';')
#         writer.writerow((data['code'],
#                          data['nominal'],
#                          data['currency'],
#                          data['course'],
#                          data['changes'],
#                          data['%']))
#
#
# def get_data(html):
#     # запись заголовков
#     with open('exchange_rate.csv', 'a') as file:
#         writer = csv.writer(file, lineterminator='\r', delimiter=';')
#         writer.writerow(("Код", "Номинал", "Валюта", "Курс ЦБ", "изменения", "%"))
#
#     # создание объекта для парсинга
#     soup = BeautifulSoup(html.text.encode('utf-8'), "lxml")
#     exchange_rates = soup.find_all('a', class_='finance-currency-table__tr')
#
#     for i in exchange_rates:
#         object_currency = i.find_all('div', class_='finance-currency-table__cell')
#
#         data = {'code': object_currency[0].text.strip(),
#                 'nominal': object_currency[1].text.strip(),
#                 'currency': object_currency[2].text.strip(),
#                 'course': object_currency[3].text.strip(),
#                 'changes': object_currency[4].text.strip(),
#                 '%': object_currency[5].text.strip(),
#                 }
#
#         write_csv(data)
#
#
# if __name__ == '__main__':
#     get_data(get_html('https://finance.rambler.ru/currencies/'))


# ======================================================
# Числовая змейка, по заданным параметрам
#
# n1, n2, n3 = 5, 6, 1
#
# for i in range(n1):
#     sp = []
#     for j in range(n2):
#         if len(str(n3)) == len(str(n1 + n2)):
#             sp.append(str(n3))
#         else:
#             sp.append(' ' + str(n3))
#         n3 += 1
#     if i % 2 == 1:
#         sp = reversed(sp)
#     print(*sp)
#
#
# m = int(input()) # строка
# n = int(input()) # столбец
# a = 0            # счетчик
#
# ln = len(str(m*n))
# for i in range(m):
#     lst = []
#     for j in range(n):
#         a += 1
#         lst.append(a)
#     if i % 2 == 0:
#         lst = reversed(lst)
#     for z in lst:
#         print(f"{z:>{ln}d}", end=' ')
#     print()
