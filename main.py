# 69 Урок

# class Goods:
#     def __init__(self, name, weight, price):
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self, name, weight, price):
#         super().__init__(name, weight, price)
#         print("Init MixinLog")
#         MixinLog.ID += 1
#         self.id = self.ID
#         self.goods = Goods(name, weight, price)
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 {self.goods.name}")
#
#
# class NoteBook(MixinLog, Goods):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()
# print(NoteBook.mro())


# Перегрузка операторов

# 24 * 60 * 60 = 86400 (число секунд в одном дне)

# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60)
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):     # оператор сравнения
#         if self.sec == other.sec:
#             return True
#         return False
#
#     def __gt__(self, other):
#         return self.sec > other.sec
#
#     def __ge__(self, other):
#         return self.sec >= other.sec
#
#
# c1 = Clock(300)
# c2 = Clock(200)
# print(c1.get_format_time())
# print(c2.get_format_time())
# if c1 == c2:
#     print("Время равно")
# else:
#     print("Время разное")
# c1 += c2
# print(c1.get_format_time())
# c1 -= c2
# print(c1.get_format_time())
# c1 *= c2
# print(c1.get_format_time())
# c1 = c1 // c2
# print(c1.get_format_time())


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item <= len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым неотрицательным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Сергей", [5, 5, 3, 4, 5])
# print(s1[2])
# s1[2] = 4
# s1[10] = 4
# print(s1.marks)
# del s1[4]
# print(s1.marks)
# print(s1.marks[2])


# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.sec // 3600) % 24
#
#         if item == "min":
#             return (self.sec // 60) % 60
#
#         if item == "sec":
#             return self.sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int):
#             raise ValueError("Значения должно быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#
#         if key == "min":
#             self.sec = s + 60 * value + h * 3600
#
#         if key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# c1["hour"] = 10
# c1["min"] = 21
# c1["sec"] = 15
# print(c1["hour"], c1["min"], c1["sec"])
# print(c1.get_format_time())


# 71 урок Полиморфизм

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
# shape = [r1, r2, s1, s2, t1, t2]
#
# for i in shape:
#     print(i.get_perimetr())
#     # if isinstance(i, Rectangle):
#     #     print(i.get_per_rect())
#     # else:
#     #     print(i.get_per_sq())


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text("Python")
#
# print(t1.total(35))
# print(t2.total(35))


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         return f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}"
#
#     def make_sound(self):
#         return f"{self.name} мяукает."
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         return f"Я собака. Меня зовут {self.name}. Мой возраст {self.age}"
#
#     def make_sound(self):
#         return f"{self.name} гавкает."
#
#
# sp = [Cat("Пушок", 2.5), Dog("Мухтар", 4)]
#
#
# for i in sp:
#     print(i.print_info())
#     print(i.make_sound())


# class Human:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"{self.surname} {self.name} {self.age}", end=' ')
#
#
# class Student(Human):
#     def __init__(self, surname, name, age, v1, group, ball):
#         self.v1 = v1
#         self.group = group
#         self.ball = ball
#         super().__init__(surname, name, age)
#
#     def info(self):
#         super().info()
#         print(self.v1, self.group, self.ball)
#
#
# class Teacher(Human):
#     def __init__(self, surname, name, age, sub,  rating):
#         super().__init__(surname, name, age)
#         self.sub = sub
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(self.sub, self.rating)
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, v1, group, ball, top):
#         self.top = top
#         super().__init__(surname, name, age, v1, group, ball)
#
#     def info(self):
#         super().info()
#         print(self.top)
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in group:
#     i.info()


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)


# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(5, 7)
# print(len(p))


# import math
#
# class Point:
#
#     __slots__ = ("x", "y", "__length")
#
#     def __init__(self, x, y):
#         self.y = y
#         self.x = x
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# pt = Point(1, 2)
# print(pt.length)
# pt.z = 3
# print(pt.__dict__)


# class Point:
#
#     __slots__ = ("x", "y", "__length")
#
#     def __init__(self, x, y):
#         self.y = y
#         self.x = x
#
#
# class Point3D(Point):
#     __slots__ = "z",
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt = Point(1, 2)
# pt3 = Point3D(10, 20, 30)
# # pt3.z = 30
# print(pt3.x, pt3.y, pt3.z)
# # print(pt3.__dict__)


# Функторы

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#
#
# c1 = Counter()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()
# c2()
# c2()
# c1()


# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, args):
#         if not isinstance(args, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return args.strip(self.__chars)
#
#
# s1 = StripChars("!@#$%^&* ")
# print(s1(" Hello word!"))
#
#
# def strip_chars(chars):
#     def wrap(*args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return args[0].strip(chars)
#
#     return wrap
#
#
# s1 = strip_chars("!@#$%^&* ")
# print(s1(" Hello word!"))


# Класс как декоратор


# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self):
#         print('перед вызовом функции')
#         self.func()
#         print('после вызова функции')


# def MyDecorator(fn):
#     def wrap():
#         print('перед вызовом функции')
#         fn()
#         print('после вызова функции')
#
#     return wrap
#
#
# @MyDecorator
# def func():
#     print('func')
#
#
# func()


# class Power:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, *args, **kwargs):
#         return self.fn(*args, **kwargs) ** 2


# @Power
# def fn(a, b):
#     return a * b
#
#
# @Power
# def fn1(a, b, c):
#     return a * b * c
#
#
# print(fn(2, 3))
# print((fn1(2, 5, 2)))


# class Power:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, fn):
#         def wrap(a, b):
#             print('до функции')
#             print(self.name, end=': ')
#             fn(a, b)
#             print('после функции')
#         return wrap
#
#
# @Power("test2")
# def fn(a, b):
#     print(a, b)
#
#
# fn(2, 5)


# Декорирование методов


# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()


# Дескрипторы
# __get__, __set__, __delete__

# class StringD:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = StringD(name)
#         self.surname = StringD(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, new_name):
#     #     self.__name = new_name
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, new_surname):
#     #     self.__surname = new_surname
#
#
# p = Person("Ivan", "Petrov")
# p.name.set("Ashot")
# print(p.name.get(), p.surname.get())


# class ValidateString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidateString()
#     surname = ValidateString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Ivan", "Petrov")
# p.name = "Oleg"
# p.surname = "Sidor"
# print(p.name)
# print(p.surname)


# 75 Пара Дескрипторы


# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError(f'Значение {self.name} должно быть положительным')
#         instance.__dict__[self.name] = value
#
#
# class Order:
#     price = NonNegative()
#     quantity = NonNegative()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# a = Order("apple", 5, 10)
# print(a.total())
# a.price = 20
# print(a.total())


# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f'Координата {coord} должно быть целым числом')
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         instance.__dict__[self.name] = value


# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f'Координата {coord} должно быть целым числом')
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
#     def __delete__(self, instance):
#         delattr(instance,  self.name)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# del p1.x
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# print(getattr(p1, "x"))
# setattr(p1, "x", 6)
# print(p1.__dict__)
# print(p1.x)
# print(hasattr(p1, "z"))


# class Integer:
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# print(p1.__dict__)
# print(p1.y)


# ======================================================
# Создание модулей

# import geometry.rect
# import geometry.sq
# import geometry.trian
# from geometry import rect, sq, trian
# # from geometry import *
#
# r1 = rect.Rectangle(1, 2)
# r2 = rect.Rectangle(3, 4)
#
# s1 = sq.Square(10)
# s2 = sq.Square(20)
#
# t1 = trian.Triangle(1, 2, 3)
# t2 = trian.Triangle(4, 5, 6)
#
# shape = [r1, t2, s1, s2, t1, t2]
#
# for i in shape:
#     print(i.get_perimetr())


# ======================================================
# 77 пара

# from car import electrocar
#
#
# def run():
#     e_car = electrocar.ElectroCar("Tesla", "T", 2020, 50000)
#     e_car.show_car()
#     e_car.description_battery()
#
#
# if __name__ == '__main__':
#     run()


# ======================================================
# Упаковка данных, Кодирование,  Декодирование


# import pickle
#
#
# filename = "basket.txt"
#
# shop_list = {
#     "фрукты": ["яблоки", "манго"],
#     "овощи": ["морковь"],
#     "бюджет": 1000
# }
#
#
# with open(filename, "wb") as fh:
#     pickle.dump(shop_list, fh)
#
# with open(filename, "rb") as fh:
#     shop = pickle.load(fh)
#
# print(shop)


# ======================================================
# import pickle
#
#
# class Test:
#     num = 35
#     st = "Привет"
#     lst = [1, 2, 3]
#     d = {"first": "a", "second": 2}
#     tpl = (22, 33)
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}" \
#                f"\nСловарь: {Test.d}"
#
#
# obj = Test()
# my_obj = pickle.dumps(obj)
# print(f"Сериализация в строку:\n{my_obj}\n")
#
# l_obj = pickle.loads(my_obj)
# print(f"Десериализация в строку:\n{l_obj}\n")


# ======================================================
# import pickle
#
#
# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
#
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)


# ======================================================
# JSON

# import json
#
#
# data = {
#     'name': "Игорь",
#     'hobbies': ['running', 'sky diving'],
#     'age': 20,
#     'children': [{'firstname': 'Alice', 'age': 5}, {'firstname': 'Bob', 'age': 8}]
# }

# Сохранение в файл-------------------------------

# with open('data_file.json', 'w') as fw:
#     json.dump(data, fw, indent=4)
#
#
# with open('data_file.json', 'r') as fw:
#     data = json.load(fw)
#     print(data)

# Сохранение в переменную--------------------------

# json_string = json.dumps(data, ensure_ascii=False)
# print(json_string)
# data = json.loads(json_string)
# print(data)


# ======================================================

# import json
# from random import choice
#
#
# def get_person():
#     name = ""
#     tel = ""
#
#     letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
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
#         date = []
#
#     date.append(person_dict)
#     with open('persons.json', 'w') as file:
#         json.dump(date, file, indent=4)
#
#
# for i in range(5):
#     write_json(get_person())

# ======================================================

# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         s = ', '.join(map(str, self.marks))
#         return f"Студент: {self.name} {s}"
#
#     def add_marks(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def aver_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     @staticmethod
#     def dump_ti_json(stud, filename):
#         try:
#             data =json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#
#         data.append({"name": stud.name, "marks": stud.marks})
#
#         with open(filename, 'w') as file:
#             json.dump(data, file)
#
#     @staticmethod
#     def load_to_file(filename):
#         with open(filename, 'r') as file:
#             print(json.load(file))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = '\n'.join(map(str, self.students))
#         return f"Группа: {self.group}\n{a}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     @staticmethod
#     def dump_group(file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = []
#
#         with open(file, 'w') as file:
#             stud_list = []
#             for i in group.students:
#                 stud_list.append([i.name, i.marks])
#
#             data.append(stud_list)
#             json.dump(data, file, indent=2)
#
#     @staticmethod
#     def upload_journal(file):
#         with open(file, 'r') as file:
#             print(json.load(file))
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# # Student.dump_ti_json(st1, 'student.json')
# # Student.load_to_file('student.json')
# st2 = Student('Nikolaenko', [2, 3, 5, 4])
# st3 = Student('Birukov', [3, 4, 5, 2, 5, 4])
# # Student.dump_ti_json(st2, 'student.json')
# # Student.load_to_file('student.json')
# sts = [st1, st2]
# my_group = Group(sts, 'ГК Python')
# print(my_group)
# print()
# my_group.add_student(st3)
# # print(my_group)
# # print()
# my_group.remove_student(1)
# print(my_group)
# group22 = [st2]
# # print()
# my_group2 = Group(group22, 'ГК Web')
# Group.dump_group('group.json', my_group)
# Group.dump_group('group.json', my_group2)
# Group.upload_journal('group.json')
# print(my_group2)
# Group.change_group(my_group, my_group2, 1)
# print()
# print(my_group)
# print()
# print(my_group2)
# print(st1)
# st1.add_marks(9)
# print(st1)
# st1.delete_mark(2)
# print(st1)
# st1.edit_mark(1, 5)
# print(st1)
# print(st1.aver_mark())


# ======================================================

# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# # print(todos[:10])
# # print(type(todos))
#
# todos_by_user = {}
#
# for i in todos:
#     if i['completed']:
#         try:
#             todos_by_user[i['userId']] += 1
#         except KeyError:
#             todos_by_user[i['userId']] = 1
#
# print(todos_by_user)
#
# top_user = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
#
# print(top_user)
#
# max_completed = top_user[0][1]
# print(max_completed)
#
# users = []
# for user, num_complete in top_user:
#     if num_complete < max_completed:
#         break
#     else:
#         users.append(str(user))
#
# print(users)
# max_users = " and ".join(users)
# s = 's' if len(max_users) > 1 else ''
# print(f"user{s} {max_users} completed {max_completed} TODOs")
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_complete and has_max_count

#
# with open('filtered_dada_file.json', 'w') as file:
#     filtered_todos = list(filter(keep, todos))
#     json.dump(filtered_todos, file, indent=2)
#
# with open('filtered_dada_file.json', 'r') as file:
#     data = json.load(file)
#     print(data)


# ======================================================

# csv (Comma Separated Values) Переменные, разделенный запятыми

# import csv

# with open('data.csv', 'r', encoding='utf-8') as r_file:
#     file_reader = csv.reader(r_file, delimiter=';')
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"   {row[0]} - {row[1]}. Родился в {row[2]} году")
#         count += 1
#     print(f"Всего в файлу {count} строки.")


# ======================================================
# метод csv.DictReader()

# with open('data.csv', 'r', encoding='utf-8') as r_file:
#     field_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(r_file, delimiter=';', fieldnames=field_names)
#     count = 0
#     for row in file_reader:
#         # print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"   {row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году")
#         count += 1
#     print(f"Всего в файлу {count} строки.")


# with open('student.csv', mode='w') as file:
#     writer = csv.writer(file, delimiter=';', lineterminator="\r")
#     writer.writerow(['Имя', "Класс", "Возраст"])
#     writer.writerow(['Женя', "9", "15"])
#     writer.writerow(['Саша', "5", "12"])


# ======================================================
# метод csv.writer()

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('data_sw.csv', mode='w') as file:
#     writer = csv.writer(file, delimiter=';', lineterminator='\r')
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
# with open('data_sw.csv') as file:
#     print(file.read())


# ======================================================
# Метод csv.DictWriter()

# import csv

# with open('stud.csv', 'w') as file:
#     names = ['Имя', 'Возраст']
#     file_writer = csv.DictWriter(file, delimiter=';', lineterminator='\r', fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Саша", "Возраст": "6"})
#     file_writer.writerow({"Имя": "Маша", "Возраст": "15"})
#     file_writer.writerow({"Имя": "Вова", "Возраст": "14"})


# ======================================================

# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]


# with open('dictwriter.csv', 'w') as file:
#     writer = csv.DictWriter(file, delimiter=';', lineterminator='\r', fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)


# ======================================================
# Парсинг

# from bs4 import BeautifulSoup
# import re


# def get_copywriter(tag):
#     whois = tag.find("div", class_="whois").text.strip()
#     if "Copywriter" in whois:
#         return tag
#     return None

# def get_salary(s):
#     pattern = r"\d+"
#     res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)


# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, "html.parser")

# salary = soup.find_all("div", {"data-set": "salary"})
# for i in salary:
#     get_salary(i.text)


# copywriter = []
# row = soup.find_all('div', class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)

# print(copywriter)

# row = soup.find('div', class_="name").text
# row = soup.find_all('div', class_="name")
# print(row)

# row = soup.find_all("div", class_="row")[1].find("div", class_="links")
# print(row)

# row = soup.find_all("div", {"data-set": "salary"})
# print(row)

# row = soup.find("div", string="Alena").parent.parent
# row = soup.find("div", string="Alena").find_parent(class_="row")
# print(row)

# row = soup.find("div", id="whois3")  # Текущий элемент
# print(row)
# row = soup.find("div", id="whois3").find_next_sibling()  # Следующий элемент
# print(row)
# row = soup.find("div", id="whois3").find_previous_sibling()  # Пред идущий элемент
# print(row)


# ======================================================
# Парсинг с сайта

# import requests

# r = requests.get("https://ru.wordpress.org/")
# print(r.headers)
# print(r.headers['Content-Type'])
# print(r.content)
# print(r.text)

# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find('header', id='masthead').find('p', class_='site-title').text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()


# ======================================================
# import csv
# import requests
# from bs4 import BeautifulSoup
# import re
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r'\D+', '', s)
#     return res
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as file:
#         writer = csv.writer(file, lineterminator='\r', delimiter=';')
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all('section', class_='plugin-section')[3]
#     plugins = p1.find_all('article')
#
#     for plugin in plugins:
#         name = plugin.find('h3').text
#         url = plugin.find('h3').find('a').get('href')
#         rating = plugin.find('span', class_='rating-count').find('a').text
#         r = refined(rating)
#         data = {'name': name, "url": url, "rating": r}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


#======================================================
# import csv
# import requests
# from bs4 import BeautifulSoup
# import re
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refine_snippet(s):
#     return re.sub(r"[🐰✅❤🇨🇳🎬🧱👏]", '', s)
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def write_scv(data):
#     with open('plugins1.csv', 'a') as file:
#         writer = csv.writer(file, lineterminator='\r', delimiter=';')
#         writer.writerow((data['name'],
#                          data['url'],
#                          data['snippet'],
#                          data['cy']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     elements = soup.find_all('article', class_='plugin-card')
#     for el in elements:
#         try:
#             name = el.find('h3').text
#         except ValueError:
#             name = ''
#
#         try:
#             url = el.find('h3').find("a").get("href")
#         except ValueError:
#             url = ''
#
#         try:
#             snippet = el.find('div', class_='entry-excerpt').text.strip()
#             snippet1 = refine_snippet(snippet)
#         except ValueError:
#             snippet1 = ''
#
#         try:
#             c = el.find('span', class_="tested-with").text.strip()
#             cy = refine_cy(c)
#         except ValueError:
#             cy = ''
#
#         deta = {'name': name, 'url': url, 'snippet': snippet1, 'cy': cy}
#
#         write_scv(deta)
#
#
# def main():
#     for i in range(0, 25):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()
#

# ======================================================
# from parsers import Parser
#
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/news/", "new.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()


# import sqlite3 as sq
#
# # con = sq.connect('profile.db')
# # cur = con.cursor()
# #
# # # открывается соединения
# # cur.execute("""""")
# #
# #
# # # закрывается соединения
# # con.close()
#
#
# with sq.connect('profile.db') as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     summa REAL,
#     data BLOB
#     )""")

#     # удаление таблицы из базы
#     cur.execute('DROP TABLE users')


# ======================================================
# РАБОТА С БАЗОЙ ДАННЫХ
import sqlite3 as sq

with sq.connect('user.db') as con:
    cur = con.cursor()

    # СОЗДАНИЕ БАЗЫ ДАННЫХ
    # cur.execute("""
    # CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT '+79090000000',
    # age INTEGER NOT NULL CHECK(age>15 AND age<70),
    # email TEXT UNIQUE
    # )""")

    # Переименовать таблицу
    # cur.execute("""
    # ALTER TABLE person
    # RENAME TO person_table;
    # """)

    # Внесение изменения в таблицу (добавление столбца)
    # cur.execute("""
    # ALTER TABLE person_table
    # ADD COLUMN address TEXT NOT NULL DEFAULT "street"
    # """)

    # Переименовать столбца
    # cur.execute("""
    # ALTER TABLE person_table
    # RENAME COLUMN address TO home_address
    # """)

    # Удаление столбца
    # cur.execute("""
    # ALTER TABLE person_table
    # DROP COLUMN home_address
    # """)

    # Удаление таблицы
    # cur.execute("""
    # DROP TABLE person_table
    # """)


