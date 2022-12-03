# first_set = set(("Connor", 32, (1, 2, 3)))
# print(first_set)
# cond_set = set("Connor")
# print(cond_set)
#
# m_set = set((1, 2, 3, 4, 5))
# print(m_set.discard(5))
# print(m_set.discard(6))
# print(m_set)
# print(m_set.pop())
# print(m_set)
#
# add_set = set((1, 2, 3, 4))
# print(add_set)
#
# add_set.update((6,))
# print(add_set)
# add_set.update(("cello", "violin"))
# print(add_set)
#
# add_set.remove("violin")
# print(add_set)
#
# frst_set = {1, 2, 3, 6}
# scnd_set = {3, 4, 5, 8}
# print(frst_set.union(scnd_set))
#
# print(frst_set.intersection(scnd_set))
#
# print(scnd_set.difference(frst_set))
# print(frst_set.symmetric_difference(scnd_set))

# A | B
# A.union(B)
# Возвращает множество, являющееся объединением множеств A и B.
# A | = B
# A.update(B)
# Записывает в A объединение множеств A и B.
# A & B
# A.intersection(B)
# Возвращает множество, являющееся пересечением множеств A и B.
# A &= B
# A.intersection_update(B)
# Записывает в A пересечение множеств A и B.
# A - B
# A.difference(B)
# Возвращает разность множеств A и B (элементы, входящие в A, но не входящие в B).
# A -= B
# A.difference_update(B)
# Записывает в A разность множеств A и B.
# A ^ B
# A.symmetric_difference(B)
# Возвращает симметрическую разность множеств A и B (элементы, входящие в A или в B, но не в оба из них одновременно).
# A ^= B
# A.symmetric_difference_update(B)
# Записывает в A симметрическую разность множеств A и B.
# A <= B
# A.issubset(B)
# Возвращает true, если A является подмножеством B.
# A >= B
# A.issuperset(B)
# Возвращает true, если B является подмножеством A.
# A < B
# Эквивалентно A <= B and A != B
# A > B
# Эквивалентно A >= B and A != B

# Задание 2
# Существует два множества, содержащие названия
# городов. Необходимо создать третье множество, содержащее названия, которые есть в обоих множествах.

# gorod_one = {"Липецк", "Москва", "Воронеж"}
# gorod_two = {"Липецк", "Ростов", "Воронеж", "Курск"}
# print(gorod_one.union(gorod_two))
# # {'Липецк', 'Москва', 'Воронеж', 'Курск', 'Ростов'}
# # Задание 3
# # Существует два множества, содержащие названия
# # городов. Необходимо создать третье множество, содержащее названия, которые есть в первом множестве, но
# # нет во втором.
#
# print(gorod_one.difference(gorod_two))
# # {'Москва'}
# # Задание 4
# # Существует два множества, содержащие названия
# # городов. Необходимо создать третье множество, содержащее названия, которые есть во втором множестве, но
# # нет в первом.
#
# print(gorod_two.difference(gorod_one))
# # {'Курск', 'Ростов'}
# # Задание 5
# # Существует два множества, содержащие названия
# # городов. Необходимо создать третье множество, содержащее уникальные названия для каждого множества.
#
# print(gorod_one.symmetric_difference(gorod_two))
# # {'Москва', 'Курск', 'Ростов'}
# print(gorod_one.intersection(gorod_two))

# В словаре хранится набор пар: Название страны ->
# Столица. Нужно реализовать функциональность по добавлению, удалению, поиску и замене.

# country = {"Россия": "Москва"}
# zapros = input("1 - добавить, 2 - удалить, 3 - заменить, либо введите название страны: ")
# if zapros in country:
#     print(country[zapros])
# if int(zapros) == 1:
#     country_add = input("Введите название страны: ")
#     country[country_add] = input("Введите название столицы: ")
# if int(zapros) == 2:
#     country_del = input("Какую страну удалить: ")
#     del country[country_del]
# if int(zapros) == 3:
#     country_update = input("Столицу какой страны заменить: ")
#     country[country_update] = input("Введите новое название столицы: ")
# print(country)


# Игра в кости с использованием модуля random в Python
# Далее представлен код простой игры в кости, которая поможет понять принцип работы функций модуля random. В игре два участника и два кубика.
# Участники по очереди бросают кубики, предварительно встряхнув их;
# Алгоритм высчитывает сумму значений кубиков каждого участника и добавляет полученный результат на доску с результатами;
# Участник, у которого в результате большее количество очков, выигрывает.

# import random
# AnnaScore = 0
# AlexScore = 0
# diceOne = [1, 2, 3, 4, 5, 6]
# diceTwo = [1, 2, 3, 4, 5, 6]
#
# def playDiceGame():
#     for i in range(5):
#         random.shuffle(diceOne)
#         random.shuffle(diceTwo)
#     firstNumber = random.choice(diceOne)
#     secondNumber = random.choice(diceTwo)
#     return firstNumber + secondNumber
#
# print("Игра в кости использует модуль рандом")
#
# for i in range(3):
#     AlexTossNumber = random.randint(1,100)
#     AnnaTossNumber = random.randint(1, 100)
#
#     if AlexTossNumber > AnnaTossNumber:
#         print("Алекс выйграл жеребьевку")
#         AlexScore = playDiceGame()
#         AnnaScore = playDiceGame()
#     else:
#         print("Анна выйграл жеребьевку")
#         AnnaScore = playDiceGame()
#         AlexScore = playDiceGame()
#
#     if AlexScore > AnnaScore:
#         print("Алекс выйграл игру в кости")
#     else:
#         print("Анна выйграла игру в кости")

# В данном упражнении мы будем симулировать 1000 выбрасываний
# игральных костей. Начнем с написания функции, выполняющей случайное выбрасывание двух обычных шестигранных костей. Эта функция не
# будет принимать входных параметров, а возвращать должна число, выпавшее в сумме на двух костях.
# В основной программе реализуйте симуляцию тысячи выбрасываний
# костей. Программа должна хранить все результаты с частотой их выпадения. После завершения процесса должна быть показана итоговая таблица
# с  результатами, похожая на ту, что представлена в табл. 6.1. Выразите
# частоту выпадения каждого из чисел в процентах вместе с ожидаемым
# результатом согласно теории вероятностей.

# from random import randint
#
# NUM_RUNS = 1000
# D_MAX = 6
#
#
# def twoDice():
#     d1 = randint(1, D_MAX)
#     d2 = randint(1, D_MAX)
#     return d1 + d2
#
#
# expected = {2: 1 / 36, 3: 2 / 36, 4: 3 / 36, 5: 4 / 36, 6: 5 / 36, 7: 6 / 36, 8: 5 / 36, 9: 4 / 36, 10: 3 / 36,
#             11: 2 / 36, 12: 1 / 36}
# # Составим словарь для хранения результатов выбрасывания костей
# counts = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
# for i in range(NUM_RUNS):
#     t = twoDice()
#     counts[t] += counts[t]
#
# print(f'Всего     реальный    ожидаемый')
# print(f'          процент     процент')
# for i in sorted(counts.keys()):
#     print("%5d % 9.2f % 10.2f" % (i, counts[i] / NUM_RUNS * 100, expected[i] * 100))

# Для выигрыша главного приза необходимо, чтобы шесть номеров на лотерейном билете совпали с шестью числами,
# выпавшими случайным образом в диапазоне от 1 до 49 во время очередного тиража.
# Напишите программу, которая будет случайным образом подбирать шесть номеров для
# вашего билета. Убедитесь в том, что среди этих чисел не будет дубликатов.
# Выведите номера билетов на экран по возрастанию.

# import random
#
# ticket = []
# n = 6
# while n != 0:
#     number = random.randint(1, 49)
#     if number not in ticket:
#         ticket.append(number)
#         n -= 1
# ticket_in = []
# for i in range(6):
#     ticket_in.append(int(input("Введите число от 1 до 49 : ")))
# print(*ticket_in, "Ваш билет")
# print(*ticket, "Выинрышный билет")
# if ticket == ticket_in:
#     print("Выигрышный билет")
# else:
#     print("Попробуйте еще")

# import random
#
# def lottery():
# 	user_numbers = input("Введите 6 чисел через пробел: ").split()
# 	bingo = [random.randint(1, 49) for i in range(6)]
# 	print("Ваш билет: ".ljust(15, ' '), *user_numbers, sep="  ")
# 	print("Удачный билет: ".ljust(15, ' '), *bingo, sep="  ")
# 	if user_numbers == bingo:
# 		print("Поздравляю, вы выиграли в лотерею!")
# 	else:
# 		print("Вы выиграли в лотерею", "\U0001F614", "Попробуйте еще раз!")
#
# lottery()


# import time
# start = time.time()
#
# list_2 = [14, 46, 43, 27, 57, 41, 45, 21, 70]
# def sort_m(list):
#     list_1 = list_2
#     list_sort = []
#     for i in range(len(list)):
#         list_sort.append(min(list))
#         list.remove(min(list))
#     return list_sort
#
# print(sort_m(list_2))
# end = time.time()
# t = (end - start)*10**3
# print(f"{t:.20f}")
