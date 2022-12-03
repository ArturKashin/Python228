from customer import Customer
from callplan import CustomerFree, CustomerTwice


# ivan = Customer('Иван Петров', 100)
# elena = CustomerFree('Елена миронова', 100)
# ekaterina = CustomerFree('Екатерина Уфимова', 100)
# sergey = CustomerTwice('Сергей Васильев', 100)
#
# ivan.record_call('Г', 20)
# ekaterina.record_call('М', 20)
# elena.record_call('Г', 20)
# sergey.record_call('Г', 20)

# print(ivan)
# print(elena)
# print(ekaterina)
# print(sergey)

# Класс ForeignPassport является производным от класса Passport. Метод PrintInfo
# существует в обоих классах. PassportList представляет собой список, содержащий объекты
# обоих классов. Вызов метода PrintInfo для каждого элемента списка демонстрирует его
# полиморфное поведение.

# class Passport:
#     def __init__(self, first_name, last_name, country, data_of_birth, numb_of_passport):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.country = country
#         self.data_of_birth = data_of_birth
#         self.numb_of_passport = numb_of_passport
#
#     def PrintInfo(self):
#         print(f'Имя {self.last_name} {self.first_name}')
#         print(f'Дата рождения: {self.data_of_birth}')
#         print(f'Страна: {self.country}')
#         print(f'Паспортные данные: {self.data_of_birth}')
#
# class ForeigePassport(Passport):
#     def __init__(self, first_name, last_name, country, data_of_birth, numb_of_passport, visa):
#         super().__init__(first_name, last_name, country, data_of_birth, numb_of_passport)
#         self.visa = visa
#
#     def PrintInfo(self):
#         super().PrintInfo()
#         print(f'Виза: {self.visa}')
#
# PassportList = []
# reguest = ForeigePassport('Ivan', "Ivanov", "Russia", "12.02.1990", "135453452342", "USA")
# PassportList.append(reguest)
#
# reguest = Passport('Иван', "Иванов", "Россия", "12.02.1990", "135453452342")
# PassportList.append(reguest)
#
# for i in PassportList:
#     i.PrintInfo()
#     print()


# Классы Printer, Scaner и Xerox являются производными от класса Equipment. Метод
# str() перегружен только в классе Printer, для остальных используется метод из базового
# класса. Метод action() перегружен для всех производных классов. Вызов этих методов для
# каждого элемента списка демонстрирует их полиморфное поведение.

# class Equipment:
#     def __init__(self, name, make, year):
#         self.name = name
#         self.make = make
#         self.year = year
#
#     def action(self):
#         return 'Не определено'
#
#     def __str__(self):
#         return f'{self.name} {self.make} {self.year}'
#
# class Printer(Equipment):
#     def __init__(self,name, make, year, series):
#         super().__init__(name, make, year)
#         self.series = series
#
#     def __str__(self):
#         return f'{self.name} {self.make} {self.year} {self.series}'
#
#     def action(self):
#         return 'Печатает'
#
# class Scaner(Equipment):
#     def action(self):
#         return 'Сканирует'
#
# class Xerox(Equipment):
#     def action(self):
#         return 'Копирует'
#
# sklad = []
#
# scaner = Scaner('Mustek', 'BearPow 12000', 2010)
# sklad.append(scaner)
#
# xerox = Xerox('Xerox', 'Phaser 3120', 2019)
# sklad.append(xerox)
#
# printer = Printer('1200', 'hp', 'LaserJet', 2018)
# sklad.append(printer)
#
# for i in sklad:
#     print(i, end=' ')
#     print(i.action())
#
# for x in sklad:
#     if isinstance(x, Printer):
#         sklad.remove(x)
#
# print('На складе осталось:')
# for i in sklad:
#     print(i, end=' ')
#     print(i.action())

# Классы «ПЕРСОНА», «АБИТУРИЕНТ», «СТУДЕНТ», «ПРЕПОДАВАТЕЛЬ»
# Класс ПЕРСОНА, экземпляр класса инициализируется аргументами фамилия, дата
# рождения и содержит методы, позволяющие вывести информацию о персоне, а также
# определить ее возраст.
# Дочерние классы: АБИТУРИЕНТ (фамилия, дата рождения, факультет),
# СТУДЕНТ(фамилия, дата рождения, факультет, курс), ПРЕПОДАВАТЕЛЬ (фамилия, дата
# рождения, факультет, должность, стаж), содержат свои методы вывода информации.
# Создайте список из n персон, выведите полную информацию из базы, а также
# организуйте поиск персон, чей возраст попадает в заданный диапазон.

# class Persone:
#     def __init__(self, last_name, data_of_birth):
#         self.last_name = last_name
#         self.data_of_birth = data_of_birth
#
#     def __str__(self):
#         return f'{self.last_name}\n{self.data_of_birth}\nВозраст: {2022 - int(self.data_of_birth[-4:])} Года'
#
#     def age(self):
#         print(2022 - int(self.data_of_birth[-4:]))
#
# class Entrant(Persone):
#     def __init__(self, last_name, data_of_birth, faculty):
#         super().__init__(last_name, data_of_birth)
#         self.faculty = faculty
#
#     def __str__(self):
#         return f'{self.last_name}\n{self.data_of_birth}\n' \
#                f'Года\nФакультет: {self.faculty}' \
#
# class Student(Persone):
#     def __init__(self, last_name, data_of_birth, faculty, course_number):
#         super().__init__(last_name, data_of_birth)
#         self.faculty = faculty
#         self.course_number = course_number
#
#     def __str__(self):
#         return f'{self.last_name}\n{self.data_of_birth}\n' \
#                f'Возраст: {2022 - int(self.data_of_birth[-4:])} ' \
#                f'Года\nФакультет: {self.faculty}\n' \
#                f'Курс: {self.course_number}'
#
# class Teacher(Persone):
#     def __init__(self, last_name, data_of_birth, faculty, post, experience):
#         super().__init__(last_name, data_of_birth)
#         self.faculty = faculty
#         self.post = post
#         self.experience = experience
#
#     def __str__(self):
#         return f'{self.last_name}\n{self.data_of_birth}\nВозраст: {2022 - int(self.data_of_birth[-4:])}Года\n' \
#                f'Факультет: {self.faculty}\n' \
#                f'Должность: {self.post}\nСтаж: {self.experience}'
#
#
#
# spis= []
# pers1 = Persone('Сидоров', "12.12.2000")
# spis.append(pers1)
# pers2 = Entrant('Сидоров', "12.12.2000", 'Математика')
# spis.append(pers2)
# pers3 = Student('Сидоров', "12.12.2000", 'Математика', 3)
# spis.append(pers3)
# pers4 = Teacher('Смирнов', "12.12.1990", 'Физика', "Преподователь", 3)
# spis.append(pers4)
#
# # for i in spis:
# #     print(i)
# #     print()
#
# print(pers2.age())

# class Point2D:
#
#     def __init__(self, x ,y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'Точка 2D ({self.x} {self.y})'
#
#     def __add__(self, other):
#         return Point2D(self.x + other.x, self.y + other.y)
#
#     def __sub__(self, other):
#         return Point2D(self.x - other.x, self.y - other.y)
#
#     def __neg__(self):
#         return Point2D(-self.x, -self.y)
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def __ne__(self, other):
#         return not(self == other)
#
#     def distance(self):
#         return (self.x ** 2 + self.y ** 2) ** 0.5
#
# p1 = Point2D(0, 5)
# p2 = Point2D(-5, 10)
#
# print(p1 + p2)
# print(p1 - p2)
# print(-p2)
# print(p1 == p2, p1 != p2)




# Классы «Клиент»(Client) и «Банк» (Bank)
#
# Класс «Клиент» содержит поля: код клиента, ФИО, дата открытия вклада, размер
# вклада, процент по вкладу.
# Класс «Банк» (class Bank) содержит поле clientBase представляющем собой список
# клиентов и методами:
# – addClient(client) — принимает обьект клиента и помещает его в base.
# – showByMoney(money) — принимает количество денег и выводит информацию о всех
# клиентах у которых размер вклада больше
# – showByCode(cod) — принимает код и выводит всю информацию клиенте с данным
# кодом.
# – showByProc(proc) — принимает процент и выводит информацию о всех клиентах у
# которых процент по вкладу больше данного.

# class Client:
#     def __init__(self, id_client, fio, deposit_opening_date, deposit_amount, percent_deposit):
#         self.id_client = id_client
#         self.fio = fio
#         self.deposit_opening_date = deposit_opening_date
#         self.deposit_amount = deposit_amount
#         self.percent_deposit = percent_deposit
#
#     def ClientInfo(self):
#         print(f'Код киента: {self.id_client}')
#         print(f'ФИО клиента: {self.fio}')
#         print(f'Дата открытия вклада: {self.deposit_opening_date}')
#         print(f'Размер вклада: {self.deposit_amount} руб.')
#         print(f'Процент по вкладу: {self.percent_deposit} %')
#
#
# class Bank(Client):
#     def __init__(self, id_client, fio, deposit_opening_date, deposit_amount, percent_deposit, clientBase=None):
#         super().__init__(id_client, fio, deposit_opening_date, deposit_amount, percent_deposit)
#         if clientBase is None:
#             clientBase = []
#         self.clientBase = clientBase
#
#     def addClient(self):
#         Base.append(self)
#         self.clientBase.append(self)
#
#     def showByMoney(self):
#         for i in Base:
#             if i.deposit_amount > self:
#                 print(f'У клиента {i.fio}, код клиента: {i.id_client}, на дипозите больше чем {self} рублей')
#
#     def showByCode(self):
#         for i in Base:
#             if i.id_client == self:
#                 i.ClientInfo()
#
#     def showByProc(self):
#         for i in Base:
#             if i.percent_deposit > self:
#                 i.ClientInfo()
#
#
# Base = []
#
# client1 = Bank(344256, 'Петров Сергей Борисович', '01.11.2020', 100_000, 10)
# client2 = Bank(344258, 'Сидоров Сергей Борисович', '03.15.2021', 200_000, 5)
# # – addClient(client) — принимает обьект клиента и помещает его в base.
# Bank.addClient(client1)
# Bank.addClient(client2)
#
# # – showByMoney(money) — принимает количество денег и выводит информацию о всех
# # клиентах у которых размер вклада больше
# Bank.showByMoney(100400)
# print()
# # – showByCode(cod) — принимает код и выводит всю информацию клиенте с данным
# # кодом.
# Bank.showByCode(344258)
# print()
# # – showByProc(proc) — принимает процент и выводит информацию о всех клиентах у
# # которых процент по вкладу больше данного.
# Bank.showByProc(7)
