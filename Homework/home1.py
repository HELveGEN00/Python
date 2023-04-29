# 12345
# Найти произведение его цифр
# Найти среднее арифметическое его цифр

# num = 23569
# print(num)
# a = num % 10
# num = num // 10
# b = num % 10
# num = num // 10
# c = num % 10
# num = num // 10
# d = num % 10
# num = num // 10
# f = num % 10
# res = a * b * c * d * f
# res1 = (a + b + c + d + f) / 5
# print("res = ", res)
# print("res1 = ", res1)

# coins 2 home

# a = int(input("Введите число от 1 до 99: "))
# kop = a
# if 11 <= a <= 14:
#     print(a, "копеек")
# elif 1 <= a <= 10 or 15 <= a <= 99:
#     kop = kop % 10
#     if kop == 1:
#         print(a, "копейка")
#     elif 2 <= kop <= 4:
#         print(a, "копейки")
#     else:
#         print(a, "копеек")
# else:
#     print("Не попал в диапозон!")

# 3 home

# col = int(input("Количество символов: "))
# tip = input("Тип символа: ")
# ori = int(input("0 - горизонтальная,"
#                 "1 - вертикальная "
#                 "\nОриентация линии: "))
# i = 0
# while i < col:
#     if ori >= 2:
#         print("Введите правильную линию!")
#         break
#     if ori == 0:
#         i += 1
#         print(tip, end=" ")
#     else:
#         i += 1
#         print(tip, end="\n")


# 4isla
# otvet = 0
# number = random.randint(1, 100)
# while otvet != number:
#     otvet = int(input("Введите число от 1 до 100 "))
#     if otvet < number:
#         print("Загаданное число больше")
#     if otvet > number:
#         print("Загаданное число меньше")
#     if otvet == 0:
#         break
#
# if otvet == number:
#     print('Вы угадали число!')
# else:
#     print(' У вас не получилось, число = ', number)

# spisok

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# for i in range(len(a)):
#     if i == 0 or i % 2 == 0:
#         print(a[i], end=" ")

# spisok 2
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# for i in range(len(a)):
#     if a[i-1] < a[i]:
#         print(a[i], end=" ")

# # spisok 3
#
# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# c = []
# for i in range(len(a)):
#     if a.count(a[i]) == 1:
#         c.append(a[i])
# print(a)
# print(c)

# home massiv
# a = [int(input("Введите элемент массива = ")) for i in range(int(input("Введите длину списка = ")))]
# b = []
# for i in range(len(a)):
#     if a[i] > 0:
#         b.append(a[i])
# maximum = max(b)
#
# print("Целый список элементов", a)
# print("Положительные элементы", b)
# print("Наибольший элемент положительного массива = ", maximum)

# massiv 2

# print("Введите элементы списка: ")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print("Введите индекс: ")
# k = int(input("k: "))
# print("Введите значение: ")
# num = int(input("c: "))
# a.insert(k, num)
# print(a)

# massiv 3
# print("Введите элементы списка: ")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print("Введите число: ")
# ch = int(input("ch = "))
# for i in range(len(a)):
#     if a[i] == ch:
#         print("Число присутствует в списке")
#         break
#     else:
#         print("Число отсутствует в списке")
#         break

# random

# import random
# res = 0
# a = []
# for i in range(20):
#     a.append(random.randint(0, 100))
# print(a)
# print("Сумма всех элементов: ", sum(a))

# random matrica
# from random import randint
#
# m = [[randint(0, 10) for x in range(6)] for y in range(6)]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
# mat = [0, 8, 10, 0, 10, 7]
# print()
# print(mat)
# print()
# i = 0
# for row in m:
#     i += 1
#     if i % 2 == 1:
#         for x in mat:
#             print(x, end="\t")
#         print()
#     else:
#         for x in row:
#             print(x, end="\t")
#         print()


# функции и список
# import math
#
#
# def func1():
#     x = float(input("Введите длину прямоугольника: "))
#     y = float(input("Введите ширину прямоугольника: "))
#     res = x * y
#     print("Площадь равна : ", res)
#
#
# def func2():
#     x = float(input("Введите основание: "))
#     y = float(input("Введите высоту: "))
#     res = x * y / 2
#     print("Площадь равна : ", res)
#
#
# def func3():
#     x = float(input("Введите радиус r = "))
#     res = math.pi * (x ** 2)
#     print("Площадь равна : ", res)
#
#
# a = int(input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))
# if a == 1:
#     func1()
# if a == 2:
#     func2()
# if a == 3:
#     func3()


# spisok
# from random import *

# import math
#
# a = [lambda x: math.pi * x ** 2, lambda x, y: x * y, lambda a, b, h: (a + b) * h / 2]
# print("Площадь круга с радиусом 2: ", a[0](2))
# print("Площадь прямоугольника размером 10*13: ", a[1](10, 13))
# print("Площадь трапеции для a = 7, b = 5, h = 3: ", a[2](7, 5, 3))


# # ВНУТРИ КРУГЛЫХ СКОБОК
# s = "Дана строка сим(волов, среди которых есть одна открыв)ающаяся"
# a = s[s.find('(') + 1:s.rfind(")")]
# s = a
# print(s)
#
# # Замена подстроки
# s1 = '11 23 44 55 23 22'
# print("Строка: ", s1)
# zam = input("Заменяемая подстрока: ")
# new = input("Новая подстрока: ")
# s1 = s1.split(zam)
# s1 = new.join(s1)
# print(s1)
#
# # ежата
# s = 'Ежевику для ежат\n' \
#     'Принесли два ежа.\n' \
#     'Ежевику еле-еле\n' \
#     'Ежата возле ели съели.\n'
# print(s)
# print(s.count('Е') + s.count(' е'))

# кортеж
# k = ('ab', 'abcd', 'cde', 'abc', 'def',)
# res = input('s=')
# for i in k:
#     if res in i:
#         print(i)
#         break
#     else:
#         print("Not found")

# result symbol
# tup = tuple(input("Введите элементы без пробела:"))
# print(tup)
# for i in set(tup):
#     print(f'Символ {i}:{tup.count(i)}')


# словари
# slov = {i: i ** 3 for i in range(1, 11)}
# print(slov)
#
# # №2stroki
# s1 = input("Первая строка:")
# s2 = input("Вторая строка:")
# a = list(set(s1) - set(s2))
# print("Наши буквы")
# for i in a:
#     print(i, end=' ')

# №3 найти все буквы
# s1 = input("Первая строка:")
# s2 = input("Вторая строка:")
# a = list(set(s1) | set(s2))
# print("Наши буквы")
# for i in a:
#     print(i, end=' ')

# №4 уникальные

# s1 = input("Первая строка:")
# s2 = input("Вторая строка:")
# a = list(set(s1) ^ set(s2))
# print("Наши буквы")
# for i in a:
#     print(i, end=' ')

# # 2 spiska
# x = ['red', 'green', 'blue']
# y = ['#FF0000', '#008000', '#000FFF']
# print(dict(zip(x, y)))
#
# # 3 slovari v 1
# x = {
#     1: 10,
#     2: 20,
# }
# y = {
#     3: 30,
#     4: 40,
# }
# z = {
#     5: 50,
#     6: 60,
# }
# x.update(y)
# x.update(z)
# print(x)

# slov
# my_dict = {
#     'emp1': {
#         'name': 'Jonh',
#         'salary': 7500,
#     },
#     'emp2': {
#         'name': 'Emma',
#         'salary': 8000,
#     },
#     'emp3': {
#         'name': 'Brad',
#         'salary': 6500,
#     },
# }
# print(my_dict)
# my_dict['emp3']['salary'] = 8500
# print(my_dict)
# norecurse

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names)
# count = 0
# for i in range(len(names)):
#     count += 1
#     for j in range(len(names[i]) - 1):
#         if isinstance(names[i], list):
#             count += 1
#             for k in range(len(names[i][j]) - 1):
#                 if isinstance(names[i][j], list):
#                     count += 1
#
# print(count)

# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             self._width = width
#             self._length = length
#             if length is None:
#                 self._length = width
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть метод calc_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#             return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# t = SqTable(20)
# print(t.__dict__)
# print(t.calc_area())
# t1 = RoundTable(radius=20)
# print(t1.calc_area())
# print(t1.__dict__)

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.comp = self.Comp()
#
#     def show(self):
#         print(self.name, " => ")
#
#     class Comp:
#         def show(self):
#             print("7, i7, 16")
#


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     symbol1 = False
#     symbol2 = False
#     symbol3 = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#         elif "-" == ch:
#             symbol1 = True
#         elif "@" == ch:
#             symbol2 = True
#         elif "_" == ch:
#             symbol3 = True
#
#     if 8 <= len(password) <= 16 and has_upper and has_lower and has_num and symbol1 and symbol2 and symbol3:
#         return True
#     return False
#
#
# run = True
# # Test : My_p@ssw0rd-
# while run:
#     p = input("Введите пароль:")
#     if check_password(p):
#         print("Надежный пароль! ")
#         run = False
#     else:
#         print("Ненадежный пароль!")
#
# import re
#
# test = "123456@i.ru, 123_456@ru.name.ru,login@i.ru,логин-1@i.ru,login.3@i.ru,login.3-67@i.ru,1login@ru.name.ru"
# pattern = r".+@.+"
#
# if re.search(pattern, test):
#     print(test)
# else:
#     print("not found")


# class Car:
#     name = "name"
#     year = "0000"
#     manufacturer = "manufacturer"
#     engine_power = "engine_power"
#     car_color = "color"
#     price = "price"
#
#     def info(self):
#         print(" Данные о вашей машине ".center(50, "="))
#         print(f"Название модели:{self.name}\nГод выпуска: {self.year}\n"
#               f"Производитель:{self.manufacturer}\nМощность двигателя:{self.engine_power}\n"
#               f"Цвет машины:{self.car_color}\nЦена:{self.price}\n")
#
#     def input_print(self, name, year, manufacturer, engine_power, car_color, price):
#         self.name = name
#         self.year = year
#         self.manufacturer = manufacturer
#         self.engine_power = engine_power
#         self.car_color = car_color
#         self.price = price
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def set_year(self, year):
#         self.year = year
#
#     def get_year(self):
#         return self.year
#
#     def set_manufacturer(self, manufacturer):
#         self.manufacturer = manufacturer
#
#     def get_manufacturer(self):
#         return self.manufacturer
#
#     def set_engine_power(self, engine_power):
#         self.engine_power = engine_power
#
#     def get_engine_power(self):
#         return self.engine_power
#
#     def set_car_color(self, car_color):
#         self.engine_power = car_color
#
#     def get_car_color(self):
#         return self.car_color
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
#
# car1 = Car()
# car1.info()
# car1.input_print("X7 M50i", "2021", "BMW", "530 l.s.", "white", "1079000")
# car1.info()
# print(car1.get_car_color())
# print(car1.get_name())
# print(car1.get_year())
# print(car1.get_manufacturer())
# print(car1.get_engine_power())
# print(car1.get_price())


# Обмен местам двух строк в файле
# pos1 = int(input('pos1 = '))
# pos2 = int(input('pos2 = '))
#
# if pos2 <= pos1:
#     print("Введите корректные значения(0 и 1)")
#
# f = open('TEST1.txt', 'r')
# L = f.readlines()
# s = L[len(L) - 1]
# length = len(s)
# f_nl = True
#
# if (length > 0) and ((s[length - 1] != '\n')):
#     L[len(L) - 1] += '\n'
#     f_nl = False
#
# f.close()
# s = L[pos1]
# L[pos1] = L[pos2]
# L[pos2] = s
# f = open('TEST1.txt', 'w')
# if f_nl == False:
#     L[len(L) - 1] = L[len(L) - 1][:-1]
#
# for item in L:
#     f.write(item)
# f.close()
#
# #обратная
# f = open('TEST1.txt', 'r')
# L = f.readlines()
#
# s = L[len(L) - 1]
# length = len(s)
# f_nl = True
#
# if length > 0 and s[length - 1] != '\n':
#     L[len(L) - 1] += '\n'
#     f_nl = False
#
# f.close()
#
# L2 = []
# i = 0
# while i < len(L):
#     s = L[len(L) - i - 1]
#     L2 = L2 + [s]
#     i = i + 1
#
# if f_nl == False:
#     L2[len(L) - 1] = L2[len(L) - 1][:-1]
#
# f = open('TEST1.txt', 'w')
# for item in L2:
#     f.write(item)
# f.close()
#
# # кол-во строк и символов
# f1 = open('TEST1.txt', 'r')
# count = 0
# for line in f1.readlines():
#     print(f"Символов в строке: ", len(line))
#     count += 1
#
# print("Количество строк в файле: ", count)
# f1.close()

# # summm by rekurs method#
# a = [2, 3, 3, 4]
#
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print("average:", sum(a) / len(a))
#         return result
#
#     return wrapper()
#
#
# @decorator
# def sum_numbers(numb):
#     numb = sum(numb)
#     return numb
#
#
# print("Summa", sum_numbers(a))
#
# # zamena
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# result = ""
# for i, c in enumerate(str1):
#     if i % 2 == 1:
#         result += c
#     else:
#         if c == "N":
#             c = "P"
#         result += c
#
# print(result)
# # del
# s = '0123456789'
# print(s)
# n = int(input("Введите индекс:"))
# res = ''
# for i in range(0, len(s)):
#     if i != n:
#         res = res + s[i]
# print(res)
# #
#
# s = '012345363738494'
# print(s)
# n = str(input("Введите символ:"))
# s2 = s.replace(n, '')
# print("Удаление всех", n, ":", s2)

# 1s
# def parallep(a, b, c):
#     def inner(it, jt):
#         return it * jt
#
#     res = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return res
#
#
# print(f"First option")
# print(parallep(2, 4, 6))
# print(parallep(5, 8, 2))
# print(parallep(1, 6, 8))
#
# # 2s
# res = 0
#
#
# def parallep(a, b, c):
#     def inner(it, jt):
#         return it * jt
#
#     global res
#     res = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return res
#
#
# print(f"Second option")
# parallep(2, 4, 6)
# print(res)
# parallep(5, 8, 2)
# print(res)
# parallep(1, 6, 8)
# print(res)
#
#
# # 3s
#
#
# def parallep(a, b, c):
#     res = 0
#
#     def inner(it, jt):
#         nonlocal res
#         res += it * jt
#
#     inner(a, b)
#     inner(a, c)
#     inner(b, c)
#     return res * 2
#
#
# print(f"Thrid option")
# print(parallep(2, 4, 6))
# print(parallep(5, 8, 2))
# print(parallep(1, 6, 8))

# os
# import os
#
# path = r'C:\Proga\PYTHON'
# print(f" Сканирование директории ".center(50, "_"), "\n", os.listdir(path))
#
# if os.path.isdir(r'C:\Proga\PYTHON'):
#     print('Name:', os.path.dirname(), ' , file,  ', os.path.getsize(os.path.dirname()))

import os

print(f" Сканирование директории ".center(50, "_"))


def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


for file in files("."):
    if os.path.isfile:
        print('Name:', file, "file ", os.path.getsize(file))

