# a = input()
# if a == a[::-1]:
#     print("YES")


# for i in range(1, 11):
#     sp = 0
#     print(i, end=' ')
#     for j in range(1, 11):
#         sp += i
#         print(sp, end=' ')
#     print()


# n = 10
# for i in range(1,10):
#     print(' ' * n, end='')
#     n -= 1
#     for j in range(1, i + 1):
#         print(j, end='')
#     print()
# for s in range(9, 0, -1):
#     print('          ',end=' ')
#     n += 1
#     for n in range(s, 0, -1):
#         print(n, end='')
#     print(' ')

# Многие в своих сообщениях не ставят заглавные буквы, особенно если используют для набора мобильные
# устройства. Создайте программу, которая
# будет принимать на вход исходную строку и возвращать строку с восстановленными заглавными буквами. По существу,
# ваша программа должна:
#  сделать заглавной первую букву в строке, не считая пробелы;
#  сделать заглавной первую букву после точки, восклицательного или
# вопросительного знака, не считая пробелы;
#  если текст на английском языке, сделать заглавными буквы «i», которым предшествует пробел или
# за которыми следует пробел, точка,
# восклицательный или вопросительный знак.
# Реализация такого рода автоматической корректуры исключит большую часть ошибок с регистром букв.
# Например, строку «what time do i have
# to be there? what’s the address? this time i’ll try to be on time!» ваша программа
# должна преобразовать в более приемлемый вариант «What time do I have
# to be there? What’s the address? This time I’ll try to be on time!». В основной
# программе запросите у  пользователя исходную строку, обработайте ее
# при помощи своей функции и выведите на экран итоговый результат.

# num = int(input())
# arr =[]
# while num != 0:
#     arr.append(num)
#     num = int(input())
# print(sorted(arr))

# num = int(input())
# arr =[]
# while num != 0:
#     arr.append(num)
#     num = int(input())
# arr.sort()
# print(arr[::-1])

# values = []
# s = input()
# while s !='':
#     s = float(s)
#     values.append(s)
#     s = input()
#
# if len(values) < 4:
#     print("Ошибка, нужно больше чисел")
# else:
#     retval = sorted(values)
#     retval.pop()
#     retval.pop(0)
#     print(values)
#     print(retval)

# words = []
# word = input("Введите значение: ")
# while word != '':
#     if word not in words:
#         words.append(word)
#     word = input("Введите значение: ")
#
# for word in words:
#     print(word)

# negatives = []
# zeros = []
# positives = []
# line = input("Введите значения: ")
# while line !='':
#     num = int(line)
#     if num < 0:
#         negatives.append(num)
#     elif num > 0:
#         positives.append(num)
#     else:
#         zeros.append(num)
#     line = input("Введите значения: ")
# for n in negatives:
#     print(n, end=' ')
# for n in zeros:
#     print(n, end=' ')
# for n in positives:
#     print(n, end=' ')

# В списке целых, заполненном  числами
# вычислить:
# ■ Сумму отрицательных чисел;
# ■ Сумму четных чисел;
# ■ Сумму нечетных чисел;
# ■ Произведение элементов с индексами кратными 3;
# ■ Произведение элементов между минимальным и
# максимальным элементом;
# ■ Сумму элементов, находящихся между первым и последним положительными элементами.

# spis = [1, 25, 6, 3, -2, -456, 545, 5, 87, -1, 7, 8, -4, ]
# sum_otr = 0
# sum_chet = 0
# sum_nchet = 0
# tot_3 = 1
# for i in spis:
#     if i < 0:
#         sum_otr += i
#     if i % 2 == 0:
#         sum_chet += i
#     if i % 2 != 0:
#         sum_nchet += i
# print(sum_otr)
# print(sum_chet)
# print(sum_nchet)
# spis_3 = spis[::3]
# tot_3 = 1
# for i in spis_3:
#     tot_3 *= i
# print(tot_3)
# spis.sort()
# new_spis = spis[1:-1]
# tot_mi_max = 1
# for i in new_spis:
#     tot_mi_max *= i
# print(tot_mi_max)
# new_spis_plus = []
# for i in spis:
#     if i > 0:
#         new_spis_plus.append(i)
# print(sum(new_spis_plus[1:-1]))

# Для выигрыша главного приза необходимо, чтобы шесть номеров на лотерейном билете совпали с шестью
# числами, выпавшими случайным образом в диапазоне от 1 до 49 во время очередного тиража.
# Напишите программу, которая будет случайным образом подбирать шесть номеров для
# вашего билета. Убедитесь в том, что среди этих чисел не будет дубликатов.
# Выведите номера билетов на экран по возрастанию.

# import random
#
# bilet_win = [4, 6, 2, 36, 22, 15]
# bilet = []
# tot = 6
# while tot != 0:
#     num = random.randint(1, 49)
#     if num not in bilet:
#         bilet.append(num)
#         tot -= 1
# print(sorted(bilet))
# print(sorted(bilet_win))

# Упражнение 119. Ниже и выше среднего (44 строки)
# Напишите программу, которая будет запрашивать у  пользователя числа, пока он не пропустит ввод.
# Сначала на экран должно быть выведено среднее значение введенного ряда чисел, после этого друг за другом необходимо вывести список чисел ниже среднего,
# равных ему (если такие найдутся) и выше среднего. Каждый список должен предваряться соответствующим заголовком.

# number = input('Введите число: ')
# sp = []
# while number != '':
#     n = int(number)
#     sp.append(n)
#     number = input('Введите число: ')
# average_value = int(sum(sp) / len(sp))
# print(f'Среднее число введенного ряда чисел: {average_value}')
# sp_low = []
# sp_high = []
# for i in sp:
#     if i < average_value:
#         sp_low.append(i)
#     if i > average_value:
#         sp_high.append(i)
# print(f'Значения ниже среднего: ', end='')
# for i in sp_low:
#     print(i, end=' ')
# print()
# if average_value in sp:
#     print('Число равное среднему значению в списке присутствует:', average_value)
# else:
#     print('Число равное среднему значению в списке отсутствует')
# print(f'Значения выше среднего: ', end='')
# for i in sp_high:
#     print(i, end=' ')

# Упражнение 115. Список собственных делителей (36 строк)
# Собственным делителем числа называется всякий его делитель, отличный от самого числа.
# Напишите функцию, которая будет возвращать список всех собственных делителей заданного числа.
# Само это число должно передаваться в  функцию в  виде единственного аргумента.
# Результатом функции будет перечень собственных делителей числа, собранных в список.
# Основная программа должна демонстрировать работу функции, запрашивая у пользователя число и выводя на экран список его собственных делителей.
# Программа должна запускаться только в том случае, если она не импортирована в виде модуля в другой файл.

# number = int(input())
# sp = []
# for i in range(1, number // 2 + 1):
#     if number % i == 0:
#         sp.append(i)
# print(f'Делители числа {number} будут: ', end='')
# for i in sp: print(i, end=' ')

# number = int(input("Введите число: "))
# def delit(number):
#     sp = []
#     for i in range(1, number // 2 + 1):
#         if number % i == 0:
#             sp.append(i)
#     print(f'Делители числа {number} будут: ', end='')
#     for i in sp: print(i, end=' ')
# delit(number)

# Упражнение 127. Список уже отсортирован? (41 строка)
# Напишите программу, показывающую, отсортирован ли переданный ей в качестве параметра список (по возрастанию или убыванию).
# Функция должна возвращать True, если список отсортирован, и False в противном случае.
# В основной программе запросите у пользователя последовательность чисел для списка, после чего выведите сообщение о том, является ли этот список отсортированным изначально.
# Можно прогнать через рандом

# number = input("Введите числа для списка: ")
# spis = []
# while number !='':
#     number = int(number)
#     spis.append(number)
#     number = input("Введите числа для списка: ")
# def sort(spis):
#     if sorted(spis) == spis:
#         return True
#     else:
#         return False
# sort(spis)
# if sort(spis) == True:
#     print("Список сортирован")
# else:
#     print("Список не сортирован")

# Многие в своих сообщениях не ставят заглавные буквы, особенно если используют для набора мобильные
# устройства. Создайте программу, которая
# будет принимать на вход исходную строку и возвращать строку с восстановленными заглавными буквами. По существу,
# ваша программа должна:
#  сделать заглавной первую букву в строке, не считая пробелы;
#  сделать заглавной первую букву после точки, восклицательного или
# вопросительного знака, не считая пробелы;
#  если текст на английском языке, сделать заглавными буквы «i», которым предшествует пробел или
# за которыми следует пробел, точка,
# восклицательный или вопросительный знак.
# Реализация такого рода автоматической корректуры исключит большую часть ошибок с регистром букв.
# Например, строку «what time do i have
# to be there? what’s the address? this time i’ll try to be on time!» ваша программа
# должна преобразовать в более приемлемый вариант «What time do I have
# to be there? What’s the address? This time I’ll try to be on time!». В основной
# программе запросите у  пользователя исходную строку, обработайте ее
# при помощи своей функции и выведите на экран итоговый результат.


# s = input("Введите текст: ")
# result = s
# pos = 0
# while pos < len(s) and result[pos] == ' ':
#     pos = pos + 1
# if pos < len(s):
#     result = result[0 : pos] + result[pos].upper() + result[pos + 1 : len(result)]
# pos = 0
# while pos < len(s):
#     if result[pos] == "." or result[pos] == "!" or result[pos] == "?":
#         pos = pos + 1
#         while pos < len(s) and result[pos] == " ":
#             pos = pos + 1
#         if pos < len(s):
#             result = result[0: pos] + \
#             result[pos].upper() + \
#             result[pos + 1: len(result)]
#     pos = pos + 1
# n = 0
# while n < len(result):
#     if result[n] == 'i' and result[n - 1] == ' ':
#         result = result[0:n] + result[n].upper() + result[n + 1: len(result)]
#     n += 1
# print(result)

