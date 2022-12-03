# class Ghost():
#     def __init__(self, color, nicname):
#         self.color = color
#         self.nicname = nicname
#
#     def print_info(self):
#         print('Цвет персонажа: ', self.color)
#         print('Ник: ', self.nicname)
#
#
# character = Ghost('оранжевый', 'Clyde')
# character.print_info()
#
# character1 = Ghost('розовый', 'Nic')
# character1.print_info()

# class Animal():
#     def __init__(self, species, voice):
#         self.species = species
#         self.voice = voice
#
#     def make_voice(self):
#         print(self.voice)
#
# animal = input('Какое животное будем программировать? ')
# voice = input("Как животное отвечает на команду голос? ")
#
# my_animal = Animal(animal,voice)
#
# print('Обьект ', my_animal.species, 'создан')
#
# answer = input('Подать команду? да/нет ')
# if answer == 'да':
#     my_animal.make_voice()

# class People():
#     def __init__(self, name, date_of_born, phone, country,city, address):
#         self.name = name
#         self.date_of_born = date_of_born
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def change_info(self):
#         self.name = input('Имя: ')
#         self.date_of_born = input('День рождения: ')
#         self.phone = input('Номер телефона: ')
#         self.country = input('Страна: ')
#         self.city = input('Город: ')
#         self.address = input('Адрес: ')
#
#     def print_info(self):
#         print(f'Имя: {self.name}')
#         print(f'Дата родления: {self.date_of_born}')
#         print(f'Телефон: {self.phone}')
#         print(f'Страна: {self.country}')
#         print(f'Город: {self.city}')
#         print(f'Адрес: {self.address}')
#
# person = People('','','','','','')
# person.change_info()
# person.print_info()

# class Student():
#     def __init__(self, full_name = '', group_number = 0, progress = []):
#         self.full_name = full_name
#         self.group_number = group_number
#         self.progress = progress
#
#     def print_infp(self):
#         txt = 'Студент ' + self.full_name + 'Группа ' + self.group_number
#         txt += 'Оценки: '
#         for x in self.progress:
#             txt += ' ' + str(x)
#
# def SortParam(st):
#     return st.full_name
#
# st_size = int(input('Введите количество студнетов: '))
# students = []
# for i in range(st_size):
#     print('Введите полное имя студента: ')
#     full_name = input()
#     print('Введите номер группы: ')
#     group_number = input()
#     n = int(input('Сколько оценок у студента? '))
#     print(f'Введите {n} оценок в столбик')
#     progress = []
#     for i in range(n):
#         score = int(input())
#         progress.append(score)
#     st = Student(full_name, group_number, progress)
#     st.print_infp()
#     students.append(st)
#
# print('Лист студента')
# for st in students:
#     st.print_infp()
#
# students = sorted(students, key=SortParam)
# print('Отсортированный список: ')
# for st in students:
#     st.print_infp()
#
# print('Неуспевающие студенты: ')
# n = 0
# for st in students:
#     for val in st.progress:
#         if val < 3:
#             st.print_infp()
#             n += 1
#             break
# if n == 0:
#     print('Нет студентов с плохой оценкой')

# class Data():
#     def __init__(self, info):
#         self.info = info
#
#     def __getitem__(self, item):
#         return self.info[item]
#
# class Teacher():
#     def __init__(self):
#         self.work = 0
#     def teach(self, info, pupil):
#         for i in pupil:
#             i.take(info)
#             self.work += 1
#
# class Pupil():
#     def __init__(self):
#         self.knowledge = []
#     def take(self, info):
#         self.knowledge.append(info)
#
# lesson = Data(['циклы','массивы','строки','ооп'])
# marIvanna = Teacher()
# vasy = Pupil()
# pety = Pupil()
#
# marIvanna.teach(lesson[2], [vasy,pety])
# marIvanna.teach(lesson[1], [pety])
#
# print(vasy.knowledge)
# print(pety.knowledge)

# import time
# import random
#
#
# class Card:
#     NumList = ['Джокер', '2', '3', '4', '5', '6',
#                '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
#     MastList = ['пик', 'крестей', 'бубей', 'черви']
#
#     def __init__(self, i, j):
#         self.Mastb = self.NumList[i - 1]
#         self.Num = self.MastList[j - 1]
#
#
# class DeckOfCards:
#     def __init__(self):
#         self.deck = [None] * 56
#         k = 0
#         for j in range(1, 5):
#             for i in range(1, 13):
#                 self.deck[k] = Card(i, j)
#                 k += 1
#
#     def shuffle(self):
#         random.shuffle(self.deck)
#
#     def get(self, i):
#         if 0 <= i <= 55:
#             answer = self.deck[i].Num
#             answer += ' '
#             answer += self.deck[i].Mastb
#         else:
#             answer = 'В колоде только 56 карт'
#         return answer
#
#
# deck = DeckOfCards()
#
# deck.shuffle()
# print('Выбирите карту из колоды в 56 карт: ')
# n = int(input())
# if n <= 56:
#     card = deck.get(n - 1)
#     print('Вы взяли карту ', card, end='\n')
# else:
#     print("В колоде только 56 карт")


# class Bird:
#     birdsCount = 0
#     birdClass = "Птица"
#
#     def __init__(self, name, age, weight):
#         self._name = name
#         self.age = age
#         self.weight = weight
#         Bird.birdsCount += 1
#
#     def BirdInto(self):
#         print(self._name)
#         print(f'Возраст {self.age}')
#         print(f'Вес {self.weight}')
#
#     def gate_name(self):
#         return self._name
#
#     def set_name(self, n):
#         self._name = n
#
#
# b1 = Bird('Петух', '2-года', '1-кг')
# b2 = Bird('Цапля', '4-года', '2-кг')
# b3 = Bird(b1._name, b2.age, b1.weight)
#
#
# class Duck(Bird):
#     birdClass = "Утка"
#
#     def __init__(self, name, age, weight, fly_speed, fly_height):
#         super().__init__(name, age, weight)
#         self.fly_speed = fly_speed
#         self.fly_height = fly_height
#
#     def BirdInto(self):
#         super().BirdInto()
#         print('Вид', Duck.birdClass)
#         print(self.fly_speed)
#         print(self.fly_height)
#
#
# d1 = Duck('Шварц', '2-года', '100кг', '100-км', '10-см')
#
# d1.BirdInto()
#
#
# class GalaBacklane(Bird):
#     birdClass = "Баклан галапогосский"
#
#     def __init__(self, name, age, weight, population):
#         super().__init__(name, age, weight)
#
#         self.population = population
#
#     def BirdInto(self):
#         super().BirdInto()
#         print(GalaBacklane.birdClass)
#         print(self.population)
#
#
# bac1 = GalaBacklane('Луи', '10-года', '5-кг', '11')
#
# bac1.BirdInto()


# import random
# import time
#
#
# class Hero:
#     def __init__(self, name, health, armor, power, weapon):
#         self.name = name
#         self.health = health
#         self.armor = armor
#         self.power = power
#         self.weapon = weapon
#
#     def print_info(self):
#         print(f'Приветствуйте героя -> {self.name}')
#         print(f'Уровень здоровья -> {self.health}')
#         print(f'Класс брони -> {self.armor}')
#         print(f'Сила удара -> {self.power}')
#         print(f'Оружие -> {self.weapon}')
#
#     def strike(self, enemy):
#         print('-> УДАР!')
#         print(self.name, 'атакует', enemy.name, 'используя', self.weapon, '\n')
#         enemy.armor -= self.power
#         if enemy.armor < 0:
#             enemy.health += enemy.armor
#             enemy.armor = 0
#
#         print(enemy.name, 'повысил уровень')
#         print('Класс брони упал до ', enemy.armor)
#         print('Количество HP снизился до ', enemy.health, '\n')
#
#
# knight = Hero('Ричард', 50, 25, 20, 'меч')
# rescal = Hero('Хелен', 100, 10, 15, 'лук')
#
# knight.print_info()
# rescal.print_info()
#
# print('Да начнется битва!')
#
# play = True
#
# while play:
#     if random.randint(0, 1) == 1:
#         fighters = [knight, rescal]
#     else:
#         fighters = [rescal, knight]
#
#     fighters[0].strike(fighters[1])
#     if fighters[1].health <= 0:
#         play =False
#         print(fighters[1].name, 'пал в бою.')
#         time.sleep(1)


# class Soda:
#
#     def __init__(self, ingredient=None):
#         if isinstance(ingredient, str):
#             self.ingredient = ingredient
#         else:
#             self.ingredient = None
#
#     def show_my_drink(self):
#         if self.ingredient:
#             print(f'Газировка и {self.ingredient}')
#         else:
#             print('Обычная газировка')
#
#
# drink1 = Soda()
# drink2 = Soda("Малина")
# drink3 = Soda(5)
#
# drink1.show_my_drink()
# drink2.show_my_drink()
# drink3.show_my_drink()


# class Triangle:
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if isinstance(self.a, str) or isinstance(self.b, str) or isinstance(self.c, str):
#             print('Нужно вводить только числа')
#         elif self.a < 0 or self.c < 0 or self.b < 0:
#             print('С отрицательными ничего не выйдет')
#         elif self.a + self.b > self.c or self.a + self.c > self.b or self.c + self.b > self.a:
#             print('Треугольник существует')
#         else:
#             print("Очень жаль но из этого треугольник не сделать")
#
#
# tre1 = Triangle(1, 2, 3)
# tre2 = Triangle(-1, 2, 3)
# tre3 = Triangle(1, "2", 3)
# tre4 = Triangle(4, 5, 6)
# tre5 = Triangle(0, 0, 0)
#
# tre1.is_triangle()
# tre2.is_triangle()
# tre3.is_triangle()
# tre4.is_triangle()
# tre5.is_triangle()

# Задача 3. Напишите программу с классом Math. Создайте два атрибута — a и b.
# Напишите методы addition — сложение, multiplication — умножение, division — деление, subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.


# class Math:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def addition(self):
#         print(self.a + self.b)
#
#     def multiplication(self):
#         print(self.a * self.b)
#
#     def division(self):
#         print(self.a / self.b)
#
#     def subtraction(self):
#         print(self.a - self.b)
#
#
# s = Math(5, 6)
#
# s.addition()
# s.multiplication()
# s.division()
# s.subtraction()


# Задача 4. Напишите программу с классом Car.
# Создайте конструктор класса Car. С
# оздайте атрибуты класса Car — color (цвет), type (тип), year (год).
# Напишите пять методов.
# Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# Третий — присвоение автомобилю года выпуска.
# Четвертый метод — присвоение автомобилю типа.
# Пятый — присвоение автомобилю цвета.

# class Car:
#     def __init__(self, color, type, year):
#         self.color = color
#         self.type = type
#         self.year = year
#
#     def car_info(self):
#         print(f'Цвет авто: {self.color}')
#         print(f'Тип авто: {self.type}')
#         print(f'Год авто: {self.year}')
#
#     def start(self):
#         print(f'Автомобиль заведен')
#
#     def stop(self):
#         print(f'Автомобиль заглушен')
#
#     def changes_year(self, i):
#         self.year = i
#
#     def change_type(self, i):
#         self.type = i
#
#     def change_color(self, i):
#         self.color = i
#
# audi = Car('Red', 'Cabriolet', 2020)
#
# audi.car_info()
# print()
#
# audi.start()
# audi.stop()
# print()
#
# audi.changes_year(2015)
# audi.change_type('Sedan')
# audi.change_color('Blue')
# audi.car_info()

# 1.	Создать класс, описывающий человека. Должны быть поля для имени, фамилии и возраста. Создать экземпляр и вывести информацию о человеке.
# 2.	Добавить метод greet, вызов которого будет выводить в консоль информацию о человеке в формате "Привет! Меня зовут Петров Василий, мне 12 лет".
# 3.	Добавить поле grades, в котором будет храниться список оценок. Создать список учеников, заполняя оценки каждого случайными числами.


# import random
#
# last_grades = [2, 3, 4, 5]
# human_grades = random.choices(last_grades, k=5)
#
#
# class human:
#
#     def __init__(self, name, surname, age, grades):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.grades = grades
#
#     def human_info(self):
#         print(f'Имя: {self.name}')
#         print(f'Фамилия: {self.surname}')
#         print(f'Возраст: {self.age}')
#
#     def greet(self):
#         if self.age in [22, 23, 24]:
#             print(f'Привет! Меня зовут {self.name} {self.surname}, мнe {self.age} года')
#         else:
#             print(f'Привет! Меня зовут {self.name} {self.surname}, мнe {self.age} лет')
#
#     def grades_human(self):
#         print(f'Оценки ученика:', end='| ')
#         for i in self.grades:
#             print(i, end=' | ')
#         print()
#
#
# person1 = human('Антон', 'Сидоров', 20, human_grades)
# person2 = human('Игорь', 'Попонов', 18, human_grades)
# person3 = human('Алена', 'Смирнова', 23, human_grades)
#
# spis_human = [person1, person2, person3]
#
# for i in spis_human:
#     i.human_info()
#     i.greet()
#     i.grades_human()
#     print()

# Создай класс Student для хранения данных об ученике.
# При инициализации нового объекта ему должны автоматически устанавливаться свойства, хранящие имя,
# фамилию и пол ученика (буквой «м» или «ж»). Добавь в класс метод academic_performance(),
# в котором запрашиваются оценки ребёнка (в строку через пробел) и выводится словесное описание его успеваемости:
# «отличник», «хорошист», «троечник» или «неуспевающий» с учётом пола ученика («отличник»/«отличница», «хорошист»/«хорошистка» и т. д.).
# Создай список, содержащий заданное пользователем количество объектов класса Student.
# Запроси оценки всех учеников в той последовательности, в которой ученики были добавлены в программу,
# и выведи словесное описание успеваемости каждого ученика.

# class Student:
#     def __init__(self, name, surname, gender, evaluations=None):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.evaluations = evaluations
#
#     def academic_performance(self):
#         self.evaluations = input(f'Введите оценки ученика {self.name} {self.surname} от 2 до 5 через пробел: ').split()
#         self.evaluations = list(map(int, self.evaluations))
#         # Средний балл
#         average_rating = sum(self.evaluations) / len(self.evaluations)
#         if self.gender == "м":
#             if average_rating == 5:
#                 print("Отличник")
#             if 4 <= average_rating < 5:
#                 print('Хорошист')
#             if 3 <= average_rating < 4:
#                 print('Троечник')
#             else:
#                 print('Двоечник')
#         elif self.gender == "ж":
#             if average_rating == 5:
#                 print("Отличница")
#             if 4 <= average_rating < 5:
#                 print('Хорошистка')
#             if 3 <= average_rating < 4:
#                 print('Троечница')
#             else:
#                 print('Двоечница')
#
#
# human1 = Student('Артем', 'Иванов', 'м')
# human2 = Student('Ирина', 'Петрова', 'ж')
# human3 = Student('Петр', 'Сидоров', 'м')
# human = [human1, human2, human3]
#
# for i in human:
#     i.academic_performance()

# 6.	Создайте класс прямоугольник — Rectangle.
# Метод __init__ принимает две точки — левый нижний и правый верхний угол.
# Каждая точка представлена экземпляром класса Point.
# Реализуйте методы вычисления площади и периметра прямоугольника.
# 7.	Добавьте в класс Rectangle метод contains.
# Метод принимает точку и возвращает True,
# если точка находится внутри прямоугольника и False в противном случае.


# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def info(self):
#         print(f'Координаты левый нижний угол: {self.a}')
#         print(f'Координаты правый верхний угол: {self.b}')
#
#     def square_perimeter(self):
#         side_a = abs((self.a[1] - self.b[1]))
#         side_b = abs((self.a[0] - self.b[0]))
#         print(f'Площадь прямоугольника равна: {side_a * side_b}')
#         print(f'Периметр прямоугольника равен: {2 * side_a + 2 * side_b}')
#
#     def contains(self, point_c):
#         self.point_c = point_c
#         print(f'Координаты точки: {self.point_c}')
#         if self.a[0] <= self.point_c[0] <= self.b[0] and self.a[1] <= self.point_c[1] <= self.b[1]:
#             print(True)
#         else:
#             print(False)
#
#
#
# rec1 = Rectangle([0, 0], [4, 5])
# rec1.info()
# rec1.square_perimeter()
# print()
#
# rec1.contains([1, 0])
# rec1.contains([0, 5])
# rec1.contains([-1, 5])