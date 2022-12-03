# f = open(r'C:\Users\Пользователь\OneDrive\Desktop\\nn1.txt', 'r', encoding='utf-8')
#
# m = f.read()
# print(m)
# print(f)
# f.close()

# with open(r'C:\Users\Пользователь\OneDrive\Desktop\\nn1.txt', 'r', encoding='utf-8') as file:
#     n = file.read(2)
#     m = file.read()
#     print(n)
#     print(m)
#     print(file.readline())
#     print(file.readlines(2))
#     print(file.readlines())

# with open(r'C:\Users\Пользователь\OneDrive\Desktop\\nn1.txt', 'r', encoding='utf-8') as file:
#     writing = file.write("Здесь был я")
#
# files = open(r'C:\Users\Пользователь\OneDrive\Desktop\\nn1.txt', 'r', encoding='utf-8')
# reading = files.read()
# print(reading)
# files.close()

# from random import randrange
#
# word_file = r"C:\Users\Пользователь\OneDrive\Desktop\\nn1.txt"
#
# words = []
# inf = open(word_file, 'r', encoding='utf-8')
# for line in inf:
#     line = line.rstrip()
#
#     if len(line) >= 3 and len(line) <= 7:
#         words.append(line)
# inf.close()
#
# first = words[randrange(0, len(words))]
# first = first.capitalize()
#
# password = first
#
# while len(password) < 8 or len(password) > 10:
#     second = words[randrange(0,len(words))]
#     second.capitalize()
#     password = first + second
#
# print(password)


# word_file = r'C:\Users\Пользователь\OneDrive\Desktop\\stih.txt'
#
# counts = {}
#
# for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#     counts[ch] = 0
#
# num_words = 0
# inf = open(word_file, 'r', encoding='utf-8')
#
# for word in inf:
#     word = word.upper().rstrip()
#     unique = []
#     for ch in word:
#         if ch not in unique and ch >= "A" and ch <= "Z":
#             unique.append(ch)
#
#     for ch in unique:
#         counts[ch] += 1
#
#     num_words += 1
#
# inf.close()
#
# smallest_count = min(counts.values())
# for ch in sorted(counts):
#     if counts[ch] == smallest_count:
#         smallest_letter = ch
#     percentage = counts[ch] / num_words * 100
#     print(ch, "встречается в %.2f процентах слов" % percentage)


#
# def LoadAndAdd(fname, names):
#     inf = open(fname, 'r', encoding='utf-8')
#     line = inf.readline()
#     inf.close()
#     parts = line.split()
#     name = parts[0]
#
#     if name not in names:
#         names.append(name)
#
#
# girls = []
# boys = []
#
# for year in range(2020, 2023):
#     girl_fname = r'C:\name\\' + str(year) + "_GirlsNames.txt"
#     boys_fname = r'C:\name\\' + str(year) + "_BoysNames.txt"
#     LoadAndAdd(girl_fname, girls)
#     LoadAndAdd(boys_fname, boys)
#
# print("Самые популярные имена девочек: ")
# for name in girls:
#     print(" ", name)
# print()
# print("Самые популярные имена мальчиков")
# for name in boys:
#     print(" ", name)

# with open(r"C:\Users\Пользователь\OneDrive\Desktop\Работы\Учеба Python\name\\1.txt", 'r', encoding='utf-8') as file1, open(r"C:\Users\Пользователь\OneDrive\Desktop\Работы\Учеба Python\name\\2.txt", 'r', encoding='utf-8') as file2:
#     m = file1.read()
#     n = file2.read()
#     if m == n:
#         print("Одинаковые значения!")
#     else:
#         print(m)
#         print(n)
#
#         for i in file1:
#             for j in file2:
#                 if y == x:
#                     print("Одинаковые значения")
#                 else:
#                     print(i)
#                     print(j)
# import os

# print('Текущая деректория: ', os.getcwd())
# os.mkdir(r'C:\Users\Пользователь\OneDrive\Desktop\\pidor') создание папки

# os.chder(название) - изменение текущей папки

# создание
# вложеных
# папок
# os.makedirs(r'C:\Users\Пользователь\OneDrive\Desktop\\pidor\\suka')
#
# # создание файла
# text_file = open(r'C:\Users\Пользователь\OneDrive\Desktop\\pidor\\test.txt', 'w+')
# text_file.write("Текстовый файл")
# text_file.close()

# изменение названия файла
# os.rename(r'C:\Users\Пользователь\OneDrive\Desktop\\pidor\\test.txt', r'C:\Users\Пользователь\OneDrive\Desktop\\pidor\\test1.txt')

# перенос файла в другую папку
# os.replace(r'C:\Users\Пользователь\OneDrive\Desktop\\pidor\\test1.txt', r'C:\Users\Пользователь\OneDrive\Desktop\\pidor1\\test1.txt')

# удаление файла в указанной папке
# os.remove(r'C:\Users\Пользователь\OneDrive\Desktop\\pidor1\\test1.txt')

# удаление только пустые папки
# os.rmdir(r'C:\Users\Пользователь\OneDrive\Desktop\\pidor\\')

# удаление папок рекурсивно
# os.removedirs()

# показывает инормацию о файле
# print(os.stat(r'C:\Users\Пользователь\OneDrive\Desktop\\pidor\\test.txt'))

# with open(r'C:\Users\Пользователь\OneDrive\Desktop\pidor\\test.txt') as file:
#     arr = []
#     for i in file:
#         i = i.rstrip()
#         arr.append(i)
#     num = int(input("Введите количество строк: "))
#     minimum = len(arr) - num
#     txt = arr[minimum:len(arr)]
#     for i in txt:
#         print(i)
# num = int(input("Введите количество строк: "))
# for i in range(num):
#     txt = file.readlines(num)
#     print(txt)

# with open(r'C:\Users\Пользователь\OneDrive\Desktop\\pidor\\testure.txt', 'w+', encoding='utf-8') as file:
#     text = "Напишите программу на Python для добавление текста в файл и отображения текстаd"
#     file.write(text)
#
# txt = open(r'C:\Users\Пользователь\OneDrive\Desktop\\pidor\\testure.txt', 'r', encoding='utf-8')
# print(txt.read())
# txt.close()

# with open(r'C:\Users\Пользователь\OneDrive\Desktop\\pidor\\test.txt') as file:
#     words = file.read()
#     simbol = '?!,.-:—;'
#     for i in simbol:
#         words = words.replace(i, "")
#     text = words.split()
#     n = 0
#     num = '0'
#     for i in text:
#         if n < len(i):
#             num = i
#             n = len(i)
#     print(num.rstrip())

# 9. Напишите программу на Python для подсчета количества строк в текстовом файле.
# with open(r'C:\Users\Пользователь\OneDrive\Desktop\test\\test.txt') as file:
#     print(len(file.readlines()))
#     file.close()
# 10. Напишите программу на Python для подсчета частоты слов в файле.
# with open(r'C:\Users\Пользователь\OneDrive\Desktop\test\\test.txt', 'r') as file:
#     words = file.read().strip()
#     for i in '?!,.-:—;':
#         words = words.replace(i, '')
#     words = words.split()
#     slovar = {}
#     slovar = slovar.fromkeys(words,1)
#     print(slovar)

# import csv
# import datetime
# import time
#
# with open(r'C:\Users\Пользователь\OneDrive\Desktop\test\\test1.csv', 'w+', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['№','Секунды', 'Секунда'])
#     for line in range(1, 301):
#         writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
#         time.sleep(0.01)

# with open(r'C:\Users\Пользователь\OneDrive\Desktop\\test\file_1.txt', 'r', encoding='utf-8') as file_1:
#     file_1 = file_1.read()
#     for i in '?!,.-:—;':
#         file_1 = file_1.replace(i, "")
#     file_1 = file_1.split("\n")
#
# with open(r'C:\Users\Пользователь\OneDrive\Desktop\\test\file_2.txt', 'r', encoding='utf-8') as file_2:
#     file_2 = file_2.read()
#     for i in '?!,.-:—;':
#         file_2 = file_2.replace(i, "")
#     file_2 = file_2.split("\n")
#
# for i in range(len(file_1)):
#     if file_1[i] != file_2[i]:
#         print(f"{i}-я строка: '{file_1[i]}'  из файла 'file_1' не совпадает с {i}й строкой в 'file_2'")
#
# for i in range(len(file_2)):
#     if file_2[i] not in file_1:
#         print(f"{i}-я строка: '{file_2[i]}'  из файла 'file_2' не совпадает с {i}й строкой в 'file_1'")
#
# if file_1 == file_2:
#     print(f"Строки в файлах совпадают")


# import os
#
# with open(r'C:\Users\Пользователь\OneDrive\Desktop\test\test.txt', 'r') as file:
#     simbol = file.read()
#     num_simbol = len(simbol)
#     print(num_simbol)
#
#     vowel_letters = 0
#     for i in simbol:
#         if i.lower() in "aeiouy":
#             vowel_letters += 1
#     print(vowel_letters)
#
#     consonant_letters = 0
#     for i in simbol:
#         if i.lower() in "bcdfghjklmnpqrstvwxz":
#             consonant_letters += 1
#     print(consonant_letters)
#
#     number_letters = 0
#     for i in simbol:
#         if i in "00123456789":
#             number_letters += 1
#     print(number_letters)
#
# with open(r'C:\Users\Пользователь\OneDrive\Desktop\test\test.txt', 'r') as file_str:
#     file_str = len(file_str.readlines())
#     print(file_str)
#
# with open(r'C:\Users\Пользователь\OneDrive\Desktop\test\test_rezult.txt', 'w+') as file:
#     file = file.write(f"Количество символов {num_simbol} \nКоличество строк {file_str} \nКоличество гласных букв {vowel_letters} "
#                       f"\nКоличество согласных букв {consonant_letters} \nКоличество цифр {number_letters}")


# import os
#
# with open(r'C:\Users\Пользователь\OneDrive\Desktop\test\test.txt', 'r') as file:
#     new_file = file.readlines()[:-1]
#     def fun(new_file):
#         new_str = ''
#         for i in new_file:
#             new_str += i
#         return new_str
#
# with open(r'C:\Users\Пользователь\OneDrive\Desktop\test\test_rezult.txt', 'w+') as file:
#     file = file.write(f'{fun(new_file)}')

# import os
#
# with open(r'C:\Users\Пользователь\OneDrive\Desktop\test\test.txt', 'r') as file:
#     file = file.readlines()
#     tot, str = 0, ''
#     for i in range(len(file)):
#         if len(file[i]) > tot:
#             tot = len(file[i])
#             str = file[i]
#     print(f'Самая длинная строка {file.index(str) + 1}-я: {str}')

# import os
#
# with open(r'C:\Users\Пользователь\OneDrive\Desktop\test\test.txt', 'r') as file:
#     file = file.read()
#     for i in '?!,.-:—;':
#         file = file.replace(i, '')
#     file_spis = file.split()
#     words = input("Введите слово для поиска: ").lower()
#     tot = 0
#     for i in file_spis:
#         if i.lower() == words:
#             tot += 1
#     print(f"Слово '{words}', встречается {tot} раз/разa")

# import os
#
# with open(r'C:\Users\Пользователь\OneDrive\Desktop\test\test.txt', 'r') as file:
#     file = file.read().split()
#     words = input("Введите слово для поиска и для замены через пробел: ").split()
#     for i in range(len(file)):
#         if file[i].lower() == words[0]:
#             file[i] = words[1]
#         if file[i][-1] in '?!,.-:—;':
#             if file[i][:-1].lower() == words[0]:
#                 file[i] = words[1]+ file[i][-1]
#     print(*file)


# import os
#
# with open(r"C:\Users\Пользователь\OneDrive\Desktop\test\file_1.txt", 'r') as file:
#     file_one = file.readlines()
#     for i in range(len(file_one)):
#         if '\n' in file_one[i]:
#             file_one[i] = file_one[i].replace('\n', '')
#
# with open(r"C:\Users\Пользователь\OneDrive\Desktop\test\file_2.txt", 'r') as file:
#     file_two = file.readlines()
#     for i in range(len(file_two)):
#         if '\n' in file_two[i]:
#             file_two[i] = file_two[i].replace('\n', '')
#
# def stroki():
#     new_str = ''
#     for i in range(len(file_one)):
#         new_str = new_str + (f"{file_one[i]} {file_two[i]}\n")
#     return new_str
#
# with open(r"C:\Users\Пользователь\OneDrive\Desktop\test\test_rezult.txt", 'w+') as file:
#     file = file.write(f"{stroki()}")

# from random import randint
# with open(r"C:\Users\Пользователь\OneDrive\Desktop\test\test.txt", 'r') as file:
#     file = file.readlines()
#     num = randint(0, len(file) - 1)
#     print(file[num].strip())

# with open(r"C:\Users\Пользователь\OneDrive\Desktop\test\article.txt", 'r', encoding='utf-8') as file:
#     file = file.readlines()
#     lines = int(input("Введите колличество последний строк для вывода: "))
#     def read_last(lines, file):
#         num = len(file) - lines
#         if lines < 0:
#             return print("Отрицательное число число")
#         else:
#             for i in range(num, len(file)):
#                 print(file[i].strip())
#     read_last(lines,file)


# spis = [0, 5, '', 10, 15, 20, 25, 30, '']
# for i in range(0, len(spis) - 1):
#     if spis[i] == 20:
#         spis[i] = 200
# print(spis)
#
# for i in range(0, len(spis) - 1):
#     if spis[i] == '':
#         spis.pop(i)
# print(spis)
#
# for i in range(0, len(spis) - 1):
#     spis[i] = spis[i] ** 2
# print(spis)
#
# Spis = [0, 5, '', 10, 15, 20, 25, 30, '']
# for i in range(0, len(Spis) - 1):
#     if Spis[i] == 20:
#         Spis.pop(i)
# print(Spis)

# spis = [0] * 100
# spis[0] = 1
# spis[-1] = 1
# print(spis)
#
#
# M = [3,8,2,4]
# for i in range(0, len(M)):
#     for j in range(i + 1, len(M)):
#         if M[i] + M[j] == 12:
#             print(f"Числа {M[i]} и {M[j]} дают в суммме 12")


# from random import randint
#
# m, n = int(input("Количество строк: ")), int(input("Количество столбцов: "))
# tot = 0
#
# for i in range(m):
#     for j in range(n):
#         m = randint(1, 10)
#         if m > 5:
#             tot += 1
#         if m == 10:
#             print(m, end=' ')
#         else:
#             print(m, end='  ')
#     print()
#
# print(f"Количество элементов матрицы которые больше 5 составляет: {tot}")

# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Определить образуют ли элементы массива, расположенные перед первым отрицательным элементом,
# убывающую последовательность.

# spis = [2, 3, 1, -1, 0, 1, 2, 3, 4, 5, 6]
# new_spis = []
# for i in range(0, len(spis)):
#     if spis[i] < 0:
#         new_spis = spis[:i]
# print(new_spis)
#
# flag = True
# for i in range(0, len(new_spis) - 1):
#     if new_spis[i] < new_spis[i + 1]:
#         flag = True
#     else:
#         flag = False
# if flag == True:
#     print("Убывающая последовательность присутствует")
# if flag == False:
#     print("Убывающая последовательность отсутствует")

# import re
# en = {'AEIOULNSTR': 1, 'DG': 2, 'BCMP': 3, 'FHVWY': 3, 'K': 5, 'JX': 8, 'QZ': 10}
# ru = {"АВЕИНОРСТ" : 1, 'ДКЛЬПУ': 2, 'БГЁЬЯ': 3, 'ЙЫ': 4, 'ЖЗХЦЧ': 5, 'ШЭЮ': 8, 'ФЩЪ': 10}
# tot = 0
# string = input("Введите слово: ").upper()
#
# if re.search('[а-яА-Я]', string):
#     for i in string:
#         for j in ru:
#             if i in j:
#                 tot += (ru.get(j))
# else:
#     for i in string:
#         for j in en:
#             if i in j:
#                 tot += (en.get(j))
# print(f"Стоимость введенного слова: {tot} очков")

# items = {30: "топор", 10: "нож", 40: "палатка", 10: "консервы", 50: "дрова", 20: "удочка"}
# kg = int(input("Сколько КГ вмещает рюкзак: "))
#
# sorted(items)[::-1]
# for i in items:
#     if i < kg:
#         print(items.get(i))
#         kg -= i
