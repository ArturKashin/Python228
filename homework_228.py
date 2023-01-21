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
