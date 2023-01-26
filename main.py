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

