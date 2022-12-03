# def b(value):
#     print("->b")
#     print(value + 1)
#
# def a(value):
#     print("->a")
#     b(value)
#
# try:
#     a("10")
# except:
#     print('Ошибка')


# a = 7/0
# print(a)

# try:
#     a = 7/0
# except:
#     print("Деление на 0")

# try:
#     a = 7/0
# except ZeroDivisionError:
#     print("Ошибка деление на 0")
# except TypeError:
#     print("Ошибка не верный тип данных")

# try:
# #     b = int(input())
# #     a = b + b
# #     print(a)
# # except ValueError:
# #     print('Неверный тип данных')

# try:
#     with open(r"C:\Users\Пользователь\OneDrive\Desktop\test\test_1.txt", "r") as file:
#         file = file.read()
# except FileNotFoundError as e:
#     print("Ощибка: ", e)

# import datetime
#
# now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
#
# try:
#     with open(r"C:\Users\Пользователь\OneDrive\Desktop\test\test_1.txt", "r") as file:
#         file = file.read()
# except FileNotFoundError as e:
#     print(f"{now} [FileNotFoundError]: ", e)


# file = open(r"C:\Users\Пользователь\OneDrive\Desktop\test\test.txt", "r", encoding="utf-8")
# try:
#     line = file.readlines()
#     print(line[26])
# except IndexError:
#     print("Недостаточно строк для вывода")
# finally:
#     file.close()
#     if file.closed:
#         print("Файл закрыт")

# def sum(a, b):
#     res = 0
#     try:
#         res = a + b
#     except TypeError:
#         res = int(a) + int(b)
#     finally:
#         print(f"a = {a}, b = {b}, res = {res}")
#
# sum(1, "2")


# try:
#     b = int(input('b = '))
#     c = int(input('c = '))
#     a = b / c
# except ZeroDivisionError:
#     print('Ошибка! Деление на 0!')
# except ValueError:
#     print('Число введено не верно')
# else:
#     print(f"a = {a}")

# sp = []
# while len(sp) != 2:
#     try:
#         b = int(input('b = '))
#         c = int(input('c = '))
#         a = b / c
#     except (ZeroDivisionError, ValueError) as e:
#         sp.append(f"Ошибка {e}")
#     else:
#         print(f"a = {a}")
# [print(i) for i in sp]

# min = 100
#
# try:
#     if min > 10:
#         raise Exception('Минимальное число 10')
# except Exception:
#     print('Моя ошибка')
#     raise

# try:
#     num = input("Введите числа через запятую: ").split()
#     int_num = list(map(int, num))
#     print(int_num)
# except ValueError:
#     print("Не правильный тип данных")

# def sr_arif(nums):
#     sr = sum(nums) / len(nums)
#     print('Среднее арифметическое = ', sr)
# try:
#     nums = list(map(int, input("Введите числа через пробел ").split()))
#     if len(nums) == 0:
#         raise ZeroDivisionError
#     sr_arif(nums)
# except ValueError:
#     print("Введеные значения должны быть числами")
# except ZeroDivisionError:
#     print("Список должен иметь хотя бы один элемент")

# Напишите программу, которая запрашивает ввод двух значений.
# Если хотя бы одно из них не является числом, то должна выполняться конкатенация,
# то есть соединение, строк.
# В остальных случаях введенные числа суммируются.

# a = input("Введите число ")
# b = input("Введите число ")
# try:
#     s = int(a) + int(b)
# except ValueError:
#     s = str(a) + str(b)
#     print(s)
# else:
#     print(s)

# try:
#     in_name = input('Введите название файла: ')
#     inf = open(r'C:\Users\Пользователь\OneDrive\Desktop\test\\' + in_name + '.txt', 'r', encoding='utf-8')
# except:
#     print('При открытие файла произошла ошибка.')
#     print('Завершение работы программы')
#
# try:
#     out_name = input('Введите название нового файла: ')
#     outf = open(r'C:\Users\Пользователь\OneDrive\Desktop\test\\' + out_name + '.txt', 'w+', encoding='utf-8')
# except Exception as e:
#     print('При открытие файла произошла ошибка: ', e)
#     print('Завершение работы программы')
#
# try:
#     for line in inf:
#         pos = line.find('#')
#         if pos > -1:
#             line = line[0:pos]
#             line = line + "\n"
#         outf.write(line)
#     outf.close()
#     inf.close()
# except Exception as e:
#     print('При открытие файла произошла ошибка: ', e)
#     print('Завершение работы программы')


# try:
#     in_name = input('Введите название файла для редактирования: ')
#     inf = open(r'C:\Users\Пользователь\OneDrive\Desktop\test\\' + in_name + '.txt', 'r', encoding='utf-8')
# except Exception as es:
#     print('При открытие файла произошла ошибка: ', es)
#     print('Завершение работы программы')
#
# try:
#     sen_name = input('Введите название нового файла со служебными словами: ')
#     sen = open(r'C:\Users\Пользователь\OneDrive\Desktop\test\\' + sen_name + '.txt', 'r', encoding='utf-8')
#
#     words = []
#     line = sen.readline()
#     while line != '':
#         line = line.strip()
#         words.append(line)
#         line = sen.readline()
# except Exception as e:
#     print('При открытие файла произошла ошибка: ', e)
#     print('Завершение работы программы')
# finally:
#     sen.close()
#
# try:
#     outf_name = input('Введите название файла для сохранения результата: ')
#     outf = open(r'C:\Users\Пользователь\OneDrive\Desktop\test\\' + outf_name + '.txt', 'w+', encoding='utf-8')
# except Exception as es:
#     print('При открытие файла произошла ошибка: ', es)
#     print('Завершение работы программы')
#
# try:
#     line = inf.readline().lower()
#     while line != "":
#         for word in words:
#             line = line.replace(word, "*" * len(word))
#         outf.write(line)
#         line = inf.readline().lower()
# except Exception as es:
#     print('произошла ошибка: ', es)
#     print('Завершение работы программы')
# finally:
#     inf.close()
#     outf.close()


# Задание 1
# Дан текстовый файл. Необходимо создать новый файл
# убрав из него все неприемлемые слова. Список неприемлемых слов находится в другом файле.

# try:
#     in_file = input("Введите название файла для редактирования: ")
#     in_f = open(r'C:\Users\Пользователь\OneDrive\Desktop\test\\' + in_file + '.txt', 'r', encoding='utf-8')
# except Exception as err:
#     print("Произошла ошибка: ", err)
#
# try:
#     replace_file = input("Введите название файла со словами для удаления: ")
#     replace_f = open(r'C:\Users\Пользователь\OneDrive\Desktop\test\\' + replace_file + '.txt', 'r', encoding='utf-8')
#     spis = []
#     replace_f = replace_f.readlines()
#     for i in replace_f:
#         spis.append(i.strip())
# except Exception as err:
#     print("Произошла ошибка: ", err)
#
# try:
#     out_file = input("Введите название файла для записи нового текста: ")
#     out_f = open(r'C:\Users\Пользователь\OneDrive\Desktop\test\\' + out_file + '.txt', 'w+', encoding='utf-8')
# except Exception as err:
#     print("Произошла ошибка: ", err)
#
# try:
#     line = in_f.readline()
#     while line != "":
#         for word in spis:
#             line = line.replace(word, '')
#         out_f.write(line)
#         line = in_f.readline().lower()
#
# except Exception as err:
#     print("Произошла ошибка: ", err)
# finally:
#     in_f.close()
#     out_f.close()
#     replace_f.close()


# Задание 2
# Написать программу транслитерации с русского на
# английский и наоборот. Данные для транслитерации
# берутся из файла и записываются в другой файл.
# Направление перевода определяется через меню пользователя.

# Пользователь с клавиатуры вводит названия файлов,
# до тех пор, пока он не введет слово quit.
# После завершения ввода программа должна записать в итоговый файл
# символы, которые есть во всех перечисленных файлах
# (символы должны быть в каждом файле).

# try:
#     in_file = input("Введите название файла: ")
#     sp = []
#     text = []
#     while in_file != "quit":
#         sp.append(in_file)
#         in_file = input("Введите название файла: ")
#
#     for i in sp:
#         in_f = open(r'C:\Users\Пользователь\OneDrive\Desktop\test\\' + i + '.txt', 'r', encoding='utf-8')
#         text.append(set(in_f.read()))
#
#     s = set(text[0])
#     for i in range(1, len(text)):
#         s = s.intersection(text[i])
#
#     new_file = open(r'C:\Users\Пользователь\OneDrive\Desktop\test\\redact.txt', 'w+', encoding='utf-8')
#     new_file = new_file.write(' '.join(s))
# except Exception as err:
#     print("Произошла ошибка: ", err)
# finally:
#     in_f.close()

# Задание 2
# Написать программу транслитерации с русского на
# английский и наоборот. Данные для транслитерации
# берутся из файла и записываются в другой файл.
# Направление перевода определяется через меню пользователя.

# translation_word = {"hello": "привет", "world": "мир"}
# language = input("С какого языка будем переводить, ru или en: ")
#
# def translate(language):
#     with open(r'C:\Users\Пользователь\OneDrive\Desktop\test\\translation.txt', 'r', encoding='utf-8') as file:
#         file_translate = file.read().split()
#         print(*file_translate)
#         file_ru = []
#         if language == "en":
#             for word in file_translate:
#                 for key, value in translation_word.items():
#                     if word.istitle():
#                         if key == word.lower():
#                             file_ru.append(value.capitalize())
#                     if key == word:
#                         file_ru.append(value)
#
#         if language == "ru":
#             for word in file_translate:
#                 for key, value in translation_word.items():
#                     if word.istitle():
#                         if value == word.lower():
#                             file_ru.append(key.capitalize())
#                     if value == word:
#                         file_ru.append(key)
#
#         file_rezult = " ".join(file_ru)
#         print(file_rezult)
#
#         with open(r'C:\Users\Пользователь\OneDrive\Desktop\test\\translation_rezult.txt', 'w+', encoding='utf-8') as file:
#             file.write(str(file_rezult))
# translate(language)

# Упражнение 157. Буквенные и числовые оценки
# estimation = input("Введите оценку: ").upper()
#
# while estimation != '':
#     try:
#         base_estimation = {"1": "F", "2": "F", "3": "F", "4": "C-", "5": "C+", "6": "B-", "7": "B+", "8": "A-",
#                            "9": "A", "10": "A+"}
#         print(f"Ваша оценка: {base_estimation[estimation]}")
#     except KeyError:
#         base_estimation = dict(zip(base_estimation.values(), base_estimation.keys()))
#         if estimation in base_estimation:
#             print(f"Ваша оценка: {base_estimation[estimation]}")
#         else:
#             print("Введенное значение не является допустимым")
#     estimation = input("Введите оценку: ").upper()
