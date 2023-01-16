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
#     def __add__(self, other):
#         if self.sex == other.sex:
#             print('Невозможно разводить котят с родителями одинаковых полов')
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




