# values = []
# s = input()
# while s != '':
#     num = float(s)
#     values.append(num)
#     s = input()
# retval = sorted(values)
# print(values)
# print(retval[1:-1])

# import random
# kolod_name = []
# kolod = []
# for i in ['Двойка', 'Тройка', 'Четверка', 'Пятерка', 'Шестерка', 'Семерка', 'Восьмерка', 'Девятка', 'Десятка', 'Валет', 'Дама', 'Король', 'Туз']:
#     for j in ['пики', 'трефы', 'бубны', 'черви']:
#         kolod_name.append(i + ' ' + j)
# for i in ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']:
#     for j in ['s', 'h', 'd', 'c']:
#         kolod.append(i + j)
# print(kolod)
# print(kolod_name)

# В стандартной библиотеке языка Python присутствует функция count, позволяющая подсчитать,
# сколько раз определенное значение встречается
# в списке. В данном упражнении вы создадите новую функцию countRange,
# которая будет подсчитывать количество элементов в  списке, значения
# которых больше или равны заданному минимальному порогу и  меньше максимального. Функция
# должна принимать три параметра: список,
# минимальную границу и максимальную границу. Возвращать она будет
# целочисленное значение, большее или равное нулю. В основной программе реализуйте демонстрацию вашей
# функции для нескольких списков
# с разными минимальными и максимальными границами. Удостоверьтесь,
# что программа будет корректно работать со списками, содержащими как
# целочисленные значения, так и числа с плавающей запятой.


# spis = [1, 2, 4, 5, 7, 8, 9, 0, 3, 2, 3, 4, 5, 7, 57, 56, 757, 5.4, 3, 2, 0.1]
# def countRange(spis, max_g, min_g):
#     sum = 0
#     for i in spis:
#         if min_g <= i <= max_g:
#             sum +=1
#     return sum
# print(countRange(spis, 3, 1))

# spisok = []
# my_shelf = {}
# autor = input("Введите автора ")
# while autor != '':
#     if autornot in my_shelf:
#         spisok = input('Введите книги через пробел ').split()
#         my_shelf[autor] = spisok

# s = input('Введите строку: ')
# characters = {}
# for ch in s:
#     characters[ch] = True
# print((len(characters)))

# def shop(n):
#     return 10.95 + (n - 1) * 2.95
# print(shop(3))

# def median(a, b, c):
#     if a < b and b < c or a > b and b > c:
#         return b
#     if b < a and a < c or b > a and a > c:
#         return a
#     if c < a and b < c or c > a and b > c:
#         return c
#
#
# def alternate(a, b, c):
#     return a + b + c - min(a, b, c) - max(a, b, c)
#
#
# x = float(input("Введите число: "))
# y = float(input("Введите число: "))
# z = float(input("Введите число: "))
#
# print(median(x, y, z))
# print(alternate(x, y, z))
#
# Создайте программу, хранящую информацию о великих баскетболистах.
# Нужно хранить ФИО баскетболиста и
# его рост. Требуется реализовать возможность добавления,
# удаления, поиска, замены данных. Используйте словарь
# для хранения информации.

# baz = {"Георге Мурешан": 231, "Мануте Бол": 230, "Славко Вранеш": 230}
# zapros = input("Рост какого баскетболиста вы хотите найти: ")
# if zapros in baz:
#     print(baz[zapros])
# if zapros not in baz:
#     baz[zapros] = int(input("Спортсмен отсутствует в списке, добавить рост запрашиваемому баскедболисту: "))
#     print('Данные успешно добавлены')
# redact = input(
#     "Если хотите удалить из списка, напишите удалить, если изменить, напишите изменить если нет оставьте пустой ввод: ")
# if redact == "удалить":
#     baz_del = input("Кого хотите удалить?: ")
#     if baz_del in baz:
#         del baz[baz_del]
#         print("Успешно")
#     else:
#         print('Такого спортсмена нету в списку')
# if redact == "изменить":
#     baz_zam = input("Рост какого спортсмена хотите заменить?: ")
#     if baz_zam in baz:
#         baz[baz_zam] = int(input("Введите рост: "))
#         print("Успешно")
# print(baz)

# Создайте программу «Англо-французский словарь».
# Нужно хранить слово на английском языке и его перевод
# на французский. Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте
# словарь для хранения информации.

# dictionary = {"hello": "bonjour", "world": "monde"}
# word = input("Введите слово на английском: ")
# if word in dictionary:
#     print("На французском это будет: ", dictionary[word])
# if word not in dictionary:
#     print("Слово отсутствует в словаре")
#     dictionary[word] = input("Введите перевод для этого слова: ")
#     print("Успешно")
# print(dictionary)

# symbols = {"ABC": 1, "DEF": 2}
# zap = ["A","B","B","A"]
# print(zap)
# for i in symbols:
#     for j in range(len(i)):
#         if i[j] in zap:
#             print(j + 1)

# alphavit = {
#     'A':'2', 'B':'22', 'C':'222', 'D':'3', 'E':'33', 'F':'333', 'G':'4', 'H':'44', 'I':'444',
#     'J':'5', 'K':'55', 'L':'555', 'M':'6', 'N':'66', 'O':'666', 'P':'7', 'Q':'77', 'R':'777', 'S':'7777',
#     'T':'8', 'U':'88', 'V':'888', 'W':'9', 'X':'99', 'Y':'999', 'Z':'9999', ' ':'0'
# }
# txt = list(input("Введите слово: ").upper())
# sp =[]
# for i in txt:
#     sp.append(alphavit[i])
# print(*sp, sep='')

# import random
#
# def loto():
#     kart_loto = {}
#     kol_b = [i for i in range(1, 77)]
#     kart_loto["B"] = random.choices(kol_b[:16], k=5)
#     kart_loto["I"] = random.choices(kol_b[16:31], k=5)
#     kart_loto["N"] = random.choices(kol_b[31:46], k=5)
#     kart_loto["G"] = random.choices(kol_b[46:61], k=5)
#     kart_loto["O"] = random.choices(kol_b[61:76], k=5)
#     return kart_loto
#
# num = loto()
#
# def kart_loto():
#     print("Карточка в словаре: ", num)
#     print("\n")
#     print(" " * 12, "Лотерейный билет")
#     print("-" * 44)
#     for i in num:
#         print(" |  ", i, end='  ')
#     print("  |")
#     print("-" * 44)
#
#     n = 0
#     for i in range(len(num)):
#         for i in num:
#             for j in num[i]:
#                 if num[i][n] < 10:
#                     print(" |  ", num[i][n], end='  ')
#                 else:
#                     print(" |  ", num[i][n], end=' ')
#                 break
#         n += 1
#         print("  |")
#     print("-" * 44)
#
# kart_loto()


# province = {"Ньюфаундленд": "A", "Новая Шотланди": "B", "Остров Принца Эдуарда": "C", "Нью-Брансуик": "E",
#             "Квебек": ["G", "H", "J"], "Онтарио": ["K", "L", "M", "N", "P"], "Манитоба": "R", "Саскачеван": "S",
#             "Альберта": "T", "Британская колумбия": "V", "Нунавт": "X", "Северо_западные территории": "X",
#             "Юкон": "Y"}
# index = input("Введите индекс отправления из 6и символов, пример(T2N1N4): ").upper()
# if len(index) != 6:
#     print("Неверно введен индекс отправления")
# else:
#     index_1, index_2 = False, False
#     for i in province:
#         if index[0] in province[i]:
#             index_1 = True
#     if index[1].isdigit():
#         index_2 = True
#     if index_1 == True and index_2 == True:
#         [print("Сельская местность", end=' ') if int(index[1]) == 0 else print("Город", end=' ')]
#         [print("На территории провинции", i) for i in province if index[0] in province[i]]
#     else:
#         print("Ошибка, индекс не корректный")

# collection = {"Война и мир": ["Лев Николаевич Толстoй", "Роман", "1863", "1274", "Эксмо"]}
# def book_collection():
#     zapros = input(
#         "Выполнить поиск книги по названию или по любому другому её атрибуту \nЕсли хотите добавить книгу в коллекцию, нажмите 1 \nЕсли хотите удалить книгу, нажмите 2 "
#         "\nЕсли хотите изменить данные в коллекции книг, нажмите 3 \nЧтобы показать всю коллекцию нажмите 4: ")
#     for i in collection:
#         if zapros in collection[i]:
#             print(f"Книга: {i} \nАвтор: {collection[i][0]} \nЖанр: {collection[i][1]} \nГод издания: {collection[i][2]} \nКоличество страниц: {collection[i][3]} \nИздательство: {collection[i][4]}")
#             book_collection()
#     if int(zapros) == 1:
#         collection_book_add = input("Введите название книги которую вы хотите добавить: ")
#         collection[collection_book_add] = [input("Введите имя автора книги: "), "", "", "", ""]
#         collection[collection_book_add][1] = input("Введите жанр: ")
#         collection[collection_book_add][2] = input("Введите год издания: ")
#         collection[collection_book_add][3] = input("Введите количество страниц: ")
#         collection[collection_book_add][4] = input("Введите Издательство: ")
#         print("Добавлено успешно \n")
#         book_collection()
#     if int(zapros) == 2:
#         collection_book_delit = input("Какую книгу вы хотите удалить: ")
#         if collection_book_delit in collection:
#             del collection[collection_book_delit]
#             print("Успешно \n")
#             book_collection()
#         else:
#             print("Такой книги не найдено \n")
#             book_collection()
#     if int(zapros) == 3:
#         collection_change = input("Данные какой книги вы хотите изменить: ")
#         if collection_change in collection:
#             collection[collection_change][0] = input("Введите имя автора книги: ")
#             collection[collection_change][1] = input("Введите жанр: ")
#             collection[collection_change][2] = input("Введите год издания: ")
#             collection[collection_change][3] = input("Введите количество страниц: ")
#             collection[collection_change][4] = input("Введите Издательство: ")
#             print("Успешно \n")
#             book_collection()
#         else:
#             print("Такой книги не найдено \n")
#             book_collection()
#     if int(zapros) == 4:
#         print(collection)
#     else:
#         print("Запрос не корректный")
#
# book_collection()

