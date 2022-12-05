# Первое и последнее вхождение
# s = input()
# if s.count('f') == 1: print(s.find('f'))
# if s.count('f') >= 2: print(s.find('f'), s.rfind('f'))
# if s.count('f') == 0: print('NO')

# Удаление фрагмента
# s = input()
# print(s[:s.find('h')] + s[s.rfind('h') + 1:])

# Символы в диапазоне
# a, b = int(input()), int(input())
# for i in range(a, b + 1): print(chr(i), end=" ")

# Простой шифр
# s = input()
# for i in s: print(ord(i), end=" ")

# Шифр Цезаря
# a, s = int(input()), input()
# for i in s: print(chr(122 - (96 - (ord(i) - a))), end="") if (ord(i) - a) < 97 else print(chr(ord(i) - a), end="")

# Переворот внутри строки
# s = input()
# print(s[:s.find('h')] + s[s.rfind('h'):s.find('h'):-1] + s[s.rfind('h'):])

# замена элементов в списке
# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3] = 'Зеленый'
# rainbow[-1] = "Фиолетовый"
# print(rainbow)

# Реверс списка
# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# print(languages[::-1])


# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
# print(numbers1 * 2 + numbers2 * 9 + numbers3)

# создание списка через цикл
# n = int(input())
# sp = []
# for i in range(n):
#     sp.append(input())
# print(sp)

# s = 1
# sp = []
# for i in range(26):
#     sp.append(chr(97 + i) * s)
#     s += 1
# print(sp)

# делители числа в список
# n = int(input())
# sp = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         sp.append(i)
# print(sp)

# Суммы двух
# n = int(input())
# sp = []
# for i in range(n):
#     sp.append(int(input()))
# sp1 = sp[:-1]
# sp2 = sp[1:]
# print(sp1)
# print(sp2)
# tot = []
# for i in range(len(sp1)):
#     tot.append(sp1[i] + sp2[i])
# print(tot)

# Удалите нечетные индексы
# n = int(input())
# sp = []
# for i in range(n):
#     a = int(input())
#     sp.append(a)
# print(sp[::2])

# n = int(input())
# s = []
# for i in range(n):
#     s.append(input())
# k = int(input())
# for i in range(n):
#     x = []
#     x.extend(s[i])
#     if k <= len(x):
#         print(x[k - 1], end='')

# Значение функции
# n = int(input())
# sp = []
# for i in range(n):
#     x = int(input())
#     sp.append(x)
#     print(x)
# print()
# for i in sp:
#     print(i**2 + 2 * i + 1)

# Remove outliers
# n = int(input())
# sp = []
# for i in range(n):
#     sp.append(int(input()))
# for i in sp:
#     if i != max(sp) and i != min(sp):
#         print(i)

# n, sp = int(input()), []
# for i in range(n):
#     sp.append(input())
#
# k, zap = int(input()), []
# for i in range(k):
#     zap.append(input().lower())

# Поисковый запрос
# n, sp = int(input()), []
# for i in range(n):
#     sp.append(input())
# k, zap = int(input()), []
# for i in range(k):
#     zap.append(input())
# for i in range(len(sp)):
#     count = 1
#     for j in range(len(zap)):
#         if zap[j].lower() in sp[i].lower():
#             count += 1
#     if count == len(zap):
#         itog.append(sp[i])
# print(*itog, sep='\n')

# numbers = [8, 9, 10, 11]
# numbers.remove(10)
# numbers.insert(2, 17)
# numbers.append(4)
# numbers.append(5)
# numbers.append(6)
# del numbers[0]
# numbers *= 2
# numbers.insert(3, 25)
# print(numbers)

# import time
#
# start = time.time()
# end = time.time()
# t = (end - start) * 10 ** 3
# print(f"Время выполнения: {t:.04f} мс")

# import random
#
# game_ellements = ["Камень", "Ножницы", "Бумага", "Ящерица", "Спок"]
# gamer_1 = random.choice(game_ellements)
# gamer_2 = random.choice(game_ellements)
# print(f"Игрок 1 выкинул: {gamer_1} \nИгрок 2 выкинуо: {gamer_2}")
# if gamer_1 == "Камень" and (gamer_2 == "Ножницы" or gamer_2 == "Ящерица"): print(f"Победил игрок 1")
# elif gamer_1 == "Ножницы" and (gamer_2 == "Бумага" or gamer_2 == "Ящерица"): print(f"Победил игрок 1")
# elif gamer_1 == "Бумага" and (gamer_2 == "Камень" or gamer_2 == "Спок"): print(f"Победил игрок 1")
# elif gamer_1 == "Ящерица" and (gamer_2 == "Спок" or gamer_2 == "Бумага"): print(f"Победил игрок 1")
# elif gamer_1 == "Спок" and (gamer_2 == "Ножницы" or gamer_2 == "Камень"): print(f"Победил игрок 1")
# elif gamer_1 == gamer_2: print(f"Ничья")
# else: print(f"Победил игрок 2")

# list_digit = (1, 46, 43, 27, 57, 414, 45, 21, 70, 231, 1 ,5)
#
# def sortng_number_digit(list):
#     one_digit, two_digit, three_digit = 0, 0, 0
#     for i in list:
#         if len(str(i)) == 1:
#             one_digit += 1
#         if len(str(i)) == 2:
#             two_digit += 1
#         if len(str(i)) == 3:
#             three_digit += 1
#     print(f"Одна цифра: {one_digit} элемента; \nДве цифры: {two_digit} элемента; \nТри цыфры: {three_digit} элемента.")
# sortng_number_digit(list_digit)

# list_digit = [1, 46, 43, 27, 57, 414, 45, 21, 70, 231, 1 ,5]
#
# def sortng_number_digit(list):
#     one_digit = len([i for i in list if len(str(i)) == 1])
#     two_digit = len([i for i in list if len(str(i)) == 2])
#     three_digit = len([i for i in list if len(str(i)) == 3])
#     print(f"Одна цифра: {one_digit} элемента; \nДве цифры: {two_digit} элемента; \nТри цыфры: {three_digit} элемента.")
# sortng_number_digit(list_digit)

# list_cars = ["BMW", "ВАЗ", "MMC", "ЗИЛ", "Firetruck", "Trashmaster", " ГАЗ", "MMC", "Lada",
#              "ИЖ", "ПАЗ", "ЛиАЗ-5256", "Cheetah", "Ambulance", "Leviathan", "ПАЗ", "Moonbeam", "Esperanto", "ГАЗ",
#              "Washington", "УАЗ", "Hunter", "ЗИЛ", "Газель", "Firetruck" "Инкасатор", "ПАЗ", "ГАЗ", "Predator", "ЛиАЗ",
#              "Firetruck" "Rhino", "ЗИЛ"]
#
# name_car = input("Введите название автомобиля и чем его заменить через пробел: ").lower().split()
# def redact_list_car(list_cars, name_car):
#     for i in range(len(list_cars)):
#         if list_cars[i].lower() == name_car[0]:
#             list_cars[i] = name_car[1]
#     print(f"Измененный список авто: {list_cars}")
# redact_list_car(list_cars, name_car)

# print([i for i in range(2, int(input()) + 1, 2)])

# l, m = input().split(), input().split()
# sum_lm = []
# for i in range(len(l)):
#     sum_lm.append(int(l[i]) + int(m[i]))
# print(*sum_lm)

# s = input().split()
# s_int = list(map(int, s))
# print(f"{'+'.join(s)}={sum(s_int)}")

# number = input().split("-")
# tot = 0
# if len(number) == 4:
#     if number[0] == "7":
#         tot += 1
#     if number[1].isdigit() and len(number[1]) == 3:
#         tot += 1
#     if number[2].isdigit() and len(number[2]) == 3:
#         tot += 1
#     if number[3].isdigit() and len(number[3]) == 4:
#         tot += 1
#     if tot == 4:
#         print("YES")
#     if tot != 4:
#         print("NO")
# if len(number) == 3:
#     if number[0].isdigit() and len(number[0]) == 3:
#         tot += 1
#     if number[1].isdigit() and len(number[1]) == 3:
#         tot += 1
#     if number[2].isdigit() and len(number[2]) == 4:
#         tot += 1
#     if tot == 3:
#         print("YES")
#     if tot != 3:
#         print("NO")
# if len(number) != 3 and len(number) != 4:
#     print("NO")


# print(max([len(i) for i in input().split()]))

# s = input().split()
# d = []
# for i in s:
#     d.append(i[1:] + i[1] + "ки")
# print(*d)

# # объявление функции
# def draw_triangle():
#     n = 1
#     m = 7
#     for i in range(8):
#         print(" " * m+ "*" * n)
#         n += 2
#         m -= 1
# draw_triangle()

# # объявление функции
# def get_shipping_cost(quantity):
#     return 1000 + (quantity - 1) * 120
# n = int(input())
# print(get_shipping_cost(n))

# объявление функции
# from math import factorial
# def compute_binom(n, k):
#     return int(factorial(n) / (factorial(k) * factorial(n - k)))
#
# n = int(input())
# k = int(input())
#
# print(compute_binom(n, k))

# объявление функции
# def number_to_words(num):
#     spis_1 = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять",
#               10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать",
#               16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать"}
#     spis_2 = {2: "двадцать", 3: "тридцать", 4: "сорок", 5: "пятьдесят", 6: "шестьдесят", 7: "семьдесят",
#               8: "восемьдесят", 9: "девяносто"}
#     if 1 <= num <= 19:
#         return spis_1[num]
#     if 20 <= num <= 99:
#         if num % 10 == 0:
#             return spis_2[num // 10]
#         else:
#             return spis_2[num // 10] + " " + spis_1[num % 10]
#
# n = int(input())
# print(number_to_words(n))

# объявление функции
# def get_month(language, number):
#     ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
#     en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
#     if language == "ru":
#         return ru[number - 1]
#     else:
#         return en[number - 1]
#
# lan = input()
# num = int(input())
# print(get_month(lan, num))

# объявление функции
# def is_magic(date):
#     date = date.split('.')
#     if int(date[0]) * int(date[1]) == int(date[2][2:]):
#         return True
#     else:
#         return False
# date = input()
# print(is_magic(date))

# объявление функции
# def is_pangram(text):
#     spis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z']
#     for i in text.lower():
#         if i in spis:
#             spis.remove(i)
#     if len(spis) != 0:
#         return False
#     else:
#         return True
#
# text = input()
# print(is_pangram(text))

# spis = [1, 20, 5, 4, 4, 63, 3, 5, 5, 34, 6, 8, 6, 3, 5, 4, 5,
#         9, 7, 2, 56, 7, 9, 3, 4]
# k = 7
# def sort_double(spis, k):
#     spis.sort()
#     i = 0
#     r = len(spis) - 1
#     while i < r:
#         sum = spis[i] + spis[r]
#         if sum == k:
#             return spis[i], spis[r]
#             break
#         if sum < k:
#             i += 1
#         else:
#             r -=1
#
# print(sort_double(spis, k))

# import random
# answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом",
#            "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
#            "	Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
#            "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
#            "Перспективы не очень хорошие", "Весьма сомнительно"]
#
# print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
# name = input("Как тебя зовут?: ")
# print(f"Привет {name}")
# zap = "д"
# while zap != "н":
#     question = input("Напишите свой вопрос: ")
#     def magic(answers):
#         return random.choice(answers)
#     print(magic(answers))
#     zap = input("Хотите задать еще вопрос: Д-'да', Н-'нет': ")
# print("Спасибо что воспользовались моими услугами")

# import random
# digits = '0123456789'
# lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
# uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# punctuation = '!#$%&*+-=?@^_'
# chars = ''
#
# quantity = int(input("Введите количество паролей: "))
# length = int(input("Введите длину пароля: "))
# simbol_digit = input("Включать ли цифры 0123456789 ? да или нет: ").lower()
# simbol_lower = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ? да или нет: ").lower()
# simbol_upper = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz ? да или нет: ").lower()
# simbol_punctuation = input("Включать ли символы !#$%&*+-=?@^_ ? да или нет: ").lower()
# simbol_exceptions = input("Исключать ли неоднозначные символы il1Lo0O ? да или нет: ").lower()
#
# if simbol_digit == "да":
#     chars += digits
# if simbol_lower == "да":
#     chars += lowercase_letters
# if simbol_upper == "да":
#     chars += uppercase_letters
# if simbol_punctuation == "да":
#     chars += punctuation
# if simbol_exceptions == "да":
#     for i in 'il1Lo0O':
#         chars = chars.replace(i, '')
#
# def generate_password(length, chars):
#     return random.choices(chars, k = length)
#
# for i in range(quantity):
#     for i in generate_password(length, chars):
#         print(i, end='')
#     print()


# upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
# upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
#
# whats_direction = input('Что мы должны сделать: шифровать или дешифровать? \n').lower()
# whats_language = input('Какой нужен язык: русский или английский? \n').lower()
# whats_step = int(input('На сколько символовов мы сдвигаем буквы по алфавиту? Ответ напиши числом. \n'))
# whats_text = input('Какой текст нужно использовать сейчас? \n')
#
# for i in range(len(whats_text)):
#     if whats_language == "ru":
#         if whats_direction == "шифровать":
#             if whats_text[i].isalpha():
#                 if whats_text[i].isupper():
#                     for j in range(len(upper_rus_alphabet)):
#                         if whats_text[i] == upper_rus_alphabet[j]:
#                             if j + whats_step > 32:
#                                 tot = (j + whats_step) - 32
#                             else:
#                                 tot = j + whats_step
#                             text_rezult += upper_rus_alphabet[tot]
#
#                 if whats_text[i].islower():
#                     for j in range(len(lower_rus_alphabet)):
#                         if whats_text[i] == lower_rus_alphabet[j]:
#                             if j + whats_step > 32:
#                                 tot = (j + whats_step) - 32
#                             else:
#                                 tot = j + whats_step
#                             text_rezult += lower_rus_alphabet[tot]
#             else:
#                 text_rezult += whats_text[i]
#         if whats_direction == "дешифровать":
#             if whats_text[i].isalpha():
#                 if whats_text[i].isupper():
#                     for j in range(len(upper_rus_alphabet)):
#                         if whats_text[i] == upper_rus_alphabet[j]:
#                             if j - whats_step < 0:
#                                 tot = whats_step - j
#                             else:
#                                 tot = j - whats_step
#                             text_rezult += upper_rus_alphabet[tot]
#
#                 if whats_text[i].islower():
#                     for j in range(len(lower_rus_alphabet)):
#                         if whats_text[i] == lower_rus_alphabet[j]:
#                             if j + whats_step < 0:
#                                 tot = whats_step - j
#                             else:
#                                 tot = j - whats_step
#                             text_rezult += lower_rus_alphabet[tot]
#             else:
#                 text_rezult += whats_text[i]
#
#     if whats_language == "en":
#         if whats_direction == "шифровать":
#             if whats_text[i].isalpha():
#                 if whats_text[i].isupper():
#                     for j in range(len(upper_eng_alphabet)):
#                         if whats_text[i] == upper_eng_alphabet[j]:
#                             if j + whats_step > 26:
#                                 tot = (j + whats_step) - 26
#                             else:
#                                 tot = j + whats_step
#                             text_rezult += upper_eng_alphabet[tot]
#
#                 if whats_text[i].islower():
#                     for j in range(len(lower_eng_alphabet)):
#                         if whats_text[i] == lower_eng_alphabet[j]:
#                             if j + whats_step > 26:
#                                 tot = (j + whats_step) - 26
#                             else:
#                                 tot = j + whats_step
#                             text_rezult += lower_eng_alphabet[tot]
#             else:
#                 text_rezult += whats_text[i]
#         if whats_direction == "дешифровать":
#             if whats_text[i].isalpha():
#                 if whats_text[i].isupper():
#                     for j in range(len(upper_eng_alphabet)):
#                         if whats_text[i] == upper_eng_alphabet[j]:
#                             if j + whats_step < 0:
#                                 tot = whats_step - j
#                             else:
#                                 tot = j - whats_step
#                             text_rezult += upper_eng_alphabet[tot]
#
#                 if whats_text[i].islower():
#                     for j in range(len(lower_eng_alphabet)):
#                         if whats_text[i] == lower_eng_alphabet[j]:
#                             if j + whats_step < 0:
#                                 tot = whats_step - j
#                             else:
#                                 tot = j - whats_step
#                             text_rezult += lower_eng_alphabet[tot]
#             else:
#                 text_rezult += whats_text[i]
#
#
# print(text_rezult)


# upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
# whats_text = input("Введите текст ")
# # whats_text = "Day, mice. 'Year' is a mistake!"
# new_text = whats_text
# for i in ".,!?\"":
#     new_text = new_text.replace(i, '')
# new_text = new_text.split()
# whats_text = whats_text.split()
# text_rezult = ''
#
# for i in range(len(whats_text)):
#     for j in range(len(whats_text[i])):
#
#         if whats_text[i][j].isalpha():
#             whats_step = len(new_text[i])
#             if whats_text[i][j].isupper():
#                 for z in range(len(upper_eng_alphabet)):
#                     if whats_text[i][j] == upper_eng_alphabet[z]:
#                         if z + whats_step > 26:
#                             tot = (z + whats_step) - 26
#                         else:
#                             tot = z + whats_step
#                         text_rezult += upper_eng_alphabet[tot]
#
#             if whats_text[i][j].islower():
#                 for z in range(len(lower_eng_alphabet)):
#                     if whats_text[i][j] == lower_eng_alphabet[z]:
#                         if z + whats_step > 25:
#                             tot = (z + whats_step) - 26
#                         else:
#                             tot = z + whats_step
#                         text_rezult += lower_eng_alphabet[tot]
#         else:
#             text_rezult += whats_text[i][j]
#     text_rezult += " "
# print(text_rezult)

# zapros = input('Сколько денег, если пришло напиши п, если ушло у: ')
# tot_col = 0
# tot = 0
# while zapros != "":
#     if zapros == 'п':
#         prihod = input('Сколько пришло: ')
#         tot += int(prihod)
#     if zapros == 'у':
#         prihod = input('Сколько пришло: ')
#         tot -= int(prihod)
#
#     if tot >= 0:
#         print("Общая касса: ", tot)
#     else:
#         print("Общая касса: ", tot)
#         print('Ты в долгах дружище')
#     tot_col += 1
#
#     zapros = input('Сколько денег, если пришло напиши п, если ушло у: ')
#
# if tot >= 0:
#     print(f'По результату дня ты заработал {tot} рублей, количество заказ нарядов {tot_col}')
# else:
#     print(f'По результату дня ты нихуя не заработал, твой долг составляет {tot} рублей, количество заказ нарядов {tot_col}')

# num = int(input())
# num = str(num)
# if len(num) == 6:
#     num = num[0] + num[:0:-1]
# if len(num) == 5:
#     num = num[::-1]
# print(int(num))

# num = '1234563444'
# print('{:,}'.format(12345656))

# num = '123456'
# tot = 0
# rezult = ''
# for i in num[::-1]:
#     if tot % 3 == 0:
#         rezult += ','
#     rezult += i
#     tot += 1
#
# print(rezult[-1:0:-1])

# num = '1234534657'
# for i in range(len(num), 0, -3):
#     num = num[:i] + ',' + num[i:]
# print(num[:-1])


# n = int(input())
# k = int(input())
#
# sp = [i for i in range(1, n + 1)]
#
# while len(sp) != 1:
#     for i in range(1, k):
#         temp = sp.pop(0)
#         sp.append(temp)
#     sp.pop(0)
#
# print(*sp)

# h_1 = 0
# h_2 = 0
# h_3 = 0
# h_4 = 0
#
# for i in range(int(input())):
#     kor = input().split()
#     x = int(kor[0])
#     y = int(kor[1])
#     if x > 0 and y > 0:
#         h_1 += 1
#     if x < 0 and y > 0:
#         h_2 += 1
#     if x < 0 and y < 0:
#         h_3 += 1
#     if x > 0 and y < 0:
#         h_4 += 1
#
# print(f'Первая четверть: {h_1}')
# print(f'Вторая четверть: {h_2}')
# print(f'Третья четверть: {h_3}')
# print(f'Четвертая четверть: {h_4}')

# sp = '8 78 79 6 70 7 58 5'.split()
# tot = 0
# for i in range(1, len(sp)):
#     if int(sp[i]) > int(sp[i - 1]):
#         tot += 1
# print(tot)

# sp = '1 2 3 4 5'.split()
# if len(sp) % 2 != 0:
#     for i in range(0, len(sp) - 1, 2):
#         sp[i], sp[i + 1] = sp[i + 1], sp[i]
#     print(*sp)
# else:
#     for i in range(0, len(sp), 2):
#         sp[i], sp[i + 1] = sp[i + 1], sp[i]
#     print(*sp)

# sp = '13 489 483 43 2 3 84 1 4 3 2 5 4 3'.split()
# sp.insert(0, sp[-1])
# del sp[-1]
# print(sp)

# sp = [2, 2, 5, 5, 5, 5, 8, 10, 10]
# tot = []
# for i in sp:
#     if i not in tot:
#         tot.append(i)
# print(len(tot))

# lst = [-2, 3, 8, -11, -4, 6]
#
# def below_zero(spis):
#     count = 0
#     for i in spis:
#         if i < 0:
#             count += 1
#     return count
#
# print(below_zero(lst))


print('Hello')

