# name_first = "Vladimir"
# print("Hello,", name_first)
# age = 20
# print(age)
import os

# a = 5
# print(a)
# print(type(a))
# b = "6"
# print(b)
# print(type(b))
# print(str(a) + b)
# print(a + int(b))

# a = 4
# b = 5
# print(a)
# print(id(a))
# print(id(b))
# a = b
# print(a)
# print(id(b))

# a = b = c = 5
# a, b, c = 2, "Hello", 4.5
# print(a, b, c)
#
# PI = 3.14
# print(PI)

# a = 2
# print(type(a))
# a = 2.5
# print(type(a))
# a = "2.5"
# print(type(a))
# a = False
# print(type(a))


# print("строка \
# символов")
# print('строка '
#       'символов')

# print("Документ \"file.py\" находится    по \t заданному пути:\nD:\\Pyton\\file.py")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3 * 3)

# print(432523524626234145323525)
# print(4.32523524626234145323525)

# print(6 + 2)
# print(6 - 2)
# print(7 / 2)
# print(6 * 2)
# print(6 ** 2)
# print(7.4 % 2)
# print(7 // 2)

# a = 5
# b = 7
# c = 3
# sum1 = a + b + c
# print("Сумма = ", sum1)
# print("Произведение = ", a * b * c)
# print("Среднее арифметическое = ", sum1 / 3)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)
#
# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# num = 10
# num += 5
# print(num)
#
# num -= 3
# print(num)
#
# num *= 3
# print(num)


# num = 4321
# print(num)
# a = num % 10
# print(a)
# num = num // 10
# b = num % 10
# print(b)
# num = num // 10
# c = num % 10
# print(c)
# num = num // 10
# d = num % 10
# print(d)
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 9753
# print(num)
# res = num % 10 * 1000  # 1000
# num = num // 10
# res += num % 10 * 100  # 1000 + 200 = 1200
# num = num // 10
# res += num % 10 * 10  # 1200 + 30 = 1230
# num = num // 10
# res += num % 10  # 1230 + 1 = 1230
# print("res = ", res)

# 12345
# Найти произведение его цифр
# Найти среднее арифметическое его цифр

# lesson 2


# coins

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


# match выражения:
#     case шаблон_1:
#         действие_1
#     case шаблон_2:
#         действие_2
#     сase шаблон_n:
#         действие_n
#     case _:
#         действие по умолчанию:


# day = 'суббота'
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница':
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует!")


# a, b = 30, 20
# minim = a if a < b else b
# print(minim)

# a, b = 10, 10
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a, b = 15, 5
# print("на ноль не делим" if b == 0 else a / b)

# try ... except

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Введите число!")
# print("Код далее")

# try:
#     n = int(input("Введите делимое число: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Введите число!")
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
# print("Код далее")

# try:
#     n = int(input("Введите делимое число: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Что-то пошло не так!")
# else:
#     print("Все нормально. Вы ввели числа!", n, "и", m)
# finally:
#     print("Конец программы!")
#
# print("Код далее")


# a = input('Введите первое значение')
# b = input('Введите второе значение')
# try:
#     print(int(a) + int(b))
# except ValueError:
#     print(a + b)

# n = input('Введите первое значение')
# m = input('Введите второе значение')
#
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)

# Циклы
# i = 0
# while i <= 100:
#     print("i = ", i)
#     i += 10

# i = 2
# while i <= 20:
#     print("i = ", i)
#     i += 2

# i = 2
# while i <= 20:
#     if i % 2 == 0:
#         print("i = ", i)
#     i += 1

# a = int(input("Укажите количество символов: "))
# # i = 0
# # while i < a:
# #     print("*", end="")
# #     i += 1
# while a > 0:
#     print("*", end="")
#     a -= 1

# a = int(input("Укажите количество символов: "))
# b = int(input("Укажите количество символов: "))
# res = 0
# while a <= b:
#     if a % 2:
#         res += a
#     a += 1
# print(res)


# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное число")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# sum = 1
#
# while True:
#     a = int(input("Введите число: "))
#     if a == 0:
#         break
#     sum *= a
# print(sum)

# i = 0
# while i < 3:
#     if i == 2:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)


# for i in range(9, -1, -2):
#     print(i, end=" ")
#
# print()
# i = 9
# while i > 0:
#     print(i, end=" ")
#     i -= 1

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
#     else:
#         print('done!')

# w = 16
# h = 4
# a = "*"
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print(a, end="")
#         else:
#             print(" ", end="")
#     print()

# w = [i * 2 for i in "Hello"]
# print(w)
#
# for i in 'Hello':
#     print(i)
#
# num = [i for i in range(30) if i % 2 == 0]
# print(num)


# Списки
# nums = [8, 3, 9, 4, 1[2, 5, 6], "H", 2.6, True]
# print(nums)
# print(type(nums))

# nums = [8, 3, 9, 4, 1]
# print(nums)
# print(nums[1])
# print(nums[-1])
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)

# s = [5, 1] * 6
# print(s)
# print(type(s))
#
# b = list("Hello")
# print(b)
# print(type(b))
#
# c = s + b
# print(c)


# срез
# список [start:stop:step]
# список [start:stop]
# список [:]


# s = list(range(1,8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[6:])
# print(s[-1:])
# print(s[3:4])
# print(s[-3:])
# print(s[-3:1:-1])
# print(s[2:5])
#
# a = "Hello"
# print(a[::-1])
#
# print(list(a))

# a = [6, 3, 0, 8, 2, 7]
# print(a[1:3])
# a[1:3] = [1, 1, 1, 1]
# print(a)
# a[1:2] = [20]
# print(a)
# a[2] = 50
# print(a)
# del a[2]
# print(a)
# del a[2:5]
# print(a)

# Методы списка
# append = добавляет элемент в конец списка
# extend = добавляет несколько элементов
# insert = добавляет элемент не затирая прошлый (индекс, значение)

# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a.append(99)
# print(a)
# a.extend([5, 6])
# print(a)
# a.extend("add")
# print(a)

# a = []
# # a.extend([i**2 for i in range(1, 11)])
# # [a.extend([i**2]) for i in range(1, 11)]
# for i in range(1,11):
#     a.extend([i**2])
# print(a)

# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a.insert(2, 100)
# print(a)
# a.insert(0, 200)
# print(a)
# a.insert(len(a), 300)
# print(a)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.append(x)
# print(s)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делиться на 3 без остатка")
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
#
# print(c)

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
#
# # if len(b) > len(a):
# #     for i in range(len(a)):
# #         c.append(a[i])
# #         c.append(b[i])
# #     for i in range(len(a), len(b)):
# #         c.append(b[i])
# # else:
# #     for i in range(len(b)):
# #         c.append(a[i])
# #         c.append(b[i])
# #     for i in range(len(b), len(a)):
# #         c.append(a[i])
# print(c)


# a = [5, 9, 2, 1, 4, 3, 2, 4]
# a.remove(2) # удаляет первый по совпадению элемент из списка по значению
# print(a)
# last = a.pop() # удаляет последний элемент из списка (без параметров) и возвращает удаленный элемент
# print(last)
# second = a.pop(-1) # удаляет элемент по индексу из списка и возвращает удаленный элемент
# print(a)
# print(second)
# a.clear() # очищает список
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# k = int(input("Введите индекс\nk = "))
# t = a.pop(k)
# print(a)

# a = [5, 2, 9, 2, 1, 2, 4, 3, 2, 4]
# num = a.count(8) # считает количество заданных значений в списке
# print(num)
#
# b = 8
# if b in a:
#     ind = a.index(b, 4, -1) # возвращает положение 1 индекса по заданному значению
#     print(ind)

# c = [1, 2, 3]
# d = c.copy()  # возвращает копию списка
# print("c =", c)
# print("d =", d)
# c.append(4)
# d.insert(0, 100)
# print("c =", c)
# print("d =", d)

# a = [5, 2, 9, 2, 1, 2, 4, 3, 2, 4]
# a.reverse()  # разворачиваем список в обратном порядке
# print(a)
#
# a.sort()  # отсортировали список по возрастанию
# print(a)

# a.sort(reverse=True)  # отсортировали список по убыванию
# print(a)

# b = sorted(a)
# print("b =", b)
# print("a =", a)

# s = ["Виталий", "Сергей", "Александр", "Анна"]
# s.sort(key=len)
# print(s)

# print("Hello")

# print("Проверка репозитория")

# print("Вносим изменения в клона")
#
# print("Hello")
#
# print("Одна строчка)")

# import math
#
#
# num1 = math.sqrt(4)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
# num4 = math.pi
#
# print(num1)
# print(num2)
# print(num3)
# print(num4)
#
# print(dir(math))

# from math import sqrt, floor
#
# num1 = sqrt(4)
# num3 = floor(3.8)
# print(num1)
# print(num3)
#
# from math import *
#
# num1 = sqrt(4)
# num3 = floor(3.8)
# print(num1)
# print(num3)

# длина окружности, с округлением до сотых
# from math import pi
#
# r = int(input("Введите радиус окружности\nr = "))
# lean = round(r * pi * 2, 2)
# print(lean)

# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")

# print(dir(time))

# s = time.time()
# print(s)
# b = 464988129
# local = time.ctime(b)
# print(local)
#
# res = time.localtime()
# print(res)
# print(res.tm_mday, ".0", res.tm_mon, ".", res.tm_year, sep="")
#
# print(time.strftime("%d.%m.%Y"))
# print(time.strftime("Сегодня: %B %d (%A), %Y.", time.localtime(b)))

# pause = 5
# print("Программа запущена")
# time.sleep(pause)
# print("Программа прекращена")

# text = input("Название напоминания: ")
# t = float(input("Через сколько минут: "))
# t = t * 60
# time.sleep(t)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.monotonic()  # убирает погрешность
# res = finish - start
# print(res)


# def hello(name):
#     print("Hello", name)
#
#
# hello("Vladimir")

# def get_sum(a, b):
#     print("Сумма:")
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# # get_sum("2", "5")
# print(res)

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()


# def symbol(count, a, b, ):
#     for i in range(count):
#         x = a if i % 2 else b
#         print(x, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(9, "X", "O")


# def res(a, b):
#     if a > b:
#         return a - b
#     if a < b:
#         return a + b
#     return "Числа равны"
#
#
# x = int(input("a = "))
# y = int(input("b = "))
# print(res(x, y))

# def cub(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, " в кубе = ", cub(i))

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     a = lst.pop()  # последний удаленный элемент
#     b = lst.pop(0)  # первый удаленный элемент
#     lst.append(b)
#     lst.insert(0, a)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['c', 'л', 'о', 'н']))

# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(func(10, 5))
# print(func(10, 15))
# a = 10
# b = 15
# if func(a, b):
#     print("Первое число > второго числа!")
# else:
#     print("Первое число < второго числа!")


# Проверка пароля(Хорошая задача)
# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Надежный пароль! ")
# else:
#     print("Ненадежный пароль!")


# def get_sum(a=0, b=0, c=0, d=0):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# x = 2
# print(get_sum(1, 5, d=x))
# print("Результат", get_sum(2, d=1, c=5), end="\n\n", sep="!!!!")
# print(get_sum(1, 5, d=x))


# def display_info(name, age):
#     print("Name: ", name, "\nAge: ", age, end="\n\n")
#
#
# display_info("Vladimir", 22)
# display_info(age=22, name="Vladimir")
# display_info("Igor", age=22, name="Vladimir")

# Двумерный массив(матрицы)
# from random import randint

#
# mas = [randint(0, 20) for i in range(5)]
# print(mas)

# lst = [2, 18, 9, 16, 18]
# print(len(lst))
# print(min(lst))

# a = [randint(0, 100) for i in range(10)]
# print(a)
# mas = max(a)
# print("Max = ", mas)
# a.remove(mas)
# a.insert(0, mas)
# print(a)

# lst = [randint(-20,20) for i in range(10)]
# print(lst)
# lst.sort(reverse=True)
# print(lst)

# lst = [randint(0, 100) for i in range(10)]
# print(lst)
#
# mini = min(lst)
# print(mini)
#
# ind = lst.index(mini)
#
# del lst[:ind]
# print(lst)
# from random import randint
#
# n1 = int(input("Размер первого списка: "))
# n2 = int(input("Размер второго списка: "))
#
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
#
# print("Первый список: ", a)
# print("Второй список: ", b)
#
# c = a + b
# print("Третий список: ", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
#
# print("Элементы обоих списков без повторения", c)
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы общие для двух списков: ", c)
#
# c = [min(a),min(b), max(a),max(b)]
# print(c)
# from random import randint
# n1 = int(input("Размер списка: "))
# a = []
# while len(a)< n1:

# какой-то урок
# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# # print(len(m))
# print(m)
# # print(m[1][2])
# #
# # a = [2, 'Hello', 5]
# # print(a[1][1])
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# for row in m:
#     # print(row)
#     for x in row:
#         print(x ** 2, end="\t\t")
#     print()

# matrix = [[x*y for x in range(1,10)] for y in range(1,10)]
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# for x, y, z in [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4]]:
#     print(z, ")", x, "+", y, "=", x + y)

# from random import randint

# matrix = [[randint(-20, 10) for x in range(3)] for y in range(4)]
# print(matrix)
# z = 0
# for row in matrix:
#     for x in row:
#         print(x, end="\t\t")
#         if x < 0:
#             z += 1
#     print()
# print("Kоличество отрицательных эелментов: ", z)
# from random import randint
#
# n = int(input("n = "))
# m = [[randint(0, 100) for x in range(n)] for y in range(n)]
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()
#
# t = m[0][0]
# for k in range(n):
#     if t > m[k][k]:
#         t = m[k][k]
# print(t)

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#
#     def incr():
#         nonlocal s
#         s = s + 1
#         print(city, s)
#
#     return incr
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res2()
# res2()
# res1()
#
# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
#
# }
#
#
# def make(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
#
# A = make(90, 101)
# B = make(70, 90)
# C = make(50, 70)
# D = make(0, 50)
# print("A =", A(students))
# print("B =", B(students))
# print("C =", C(students))
# print("D =", D(students))


# Анонимные функции (lambda)

# print((lambda x, y: x + y)(1, 2))
#
# (lambda x, y: print(x + y))(1, 2)
#
# func = lambda x, y: x + y

# print(func(1, 2))
# print(func('a', 'b'))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# print((lambda *args: args)(1, 2, 3, 4, 5, 6))
# print((lambda *args: args)(5))

# c = (lambda x: x * 2, lambda x: x * 3, lambda x: x * 4)
# for t in c:
#     print(t("abc_"))

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add1 = outer(5)
# print(add1(10))
#
#
# def outer1(n):
#     return lambda x: n + x
#
#
# add2 = outer1(5)
# print(add2(10))
#
# outer2 = lambda n: lambda x: x + n
# add3 = outer2(5)
# print(add3(10))
#
# print((lambda n: lambda x: x + n)(5)(10))
#
# print((lambda n: lambda x: lambda z: z + n + x)(2)(4)(6))

# def func(i):
#     return i[1]
#
#
# d = {'d': 10, 'b': 15, 'c': 4}
# # a = sorted(d)
# # print(a)
# list_d = list(d.items())
# print(list_d)
# list_d.sort(key=func)
# # list_d.sort(key=lambda i: i[1])
# print(list_d)
# print(dict(list_d))

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6},
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)

# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# print(a[0](12, 3))

# a = {'one': lambda x: x - 1, 'two': lambda x: x * (-1), 'three': lambda x: x ** 1}
#
# b = [-3, 10, 0, 4]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
# }
# d[2]()

# print((lambda a, b, c: a if a < b and a < c else b if b < c and b < a else c)(3, 1, 2))


# map(func, iterables), filter(func, iterable)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# a = list(map(mult, lst))
# print(a)
#
# a1 = list(map(lambda t: t * 2, lst))
# print(a1)

# t = (2.88, - 1.75, 100.55)
#
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)
#
# t3 = tuple(map(int, t))
# print(t3)

# areas = [3.564897, 7.4512368, 8.412578, 4.456712, 5.456782, 2.321456]
#
# print(list(map(round, areas, (2, 5, 2, 3, 6, 1))))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# print(list(map(lambda x, y: (x, y), st, num)))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))  # ([1,2,3],[4,5,6])
#
# a = l1,l2
# print(a)

# t = ('abcd', 'abc', 'cdrfg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)
# import random
#
# a = []
# for i in range(20):
#     a.append(random.randint(2, 60))
# print(a)
# res = list(filter(lambda s: 10 <= s <= 20, a))
# print(res)

# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10)))))


# Декораторы
# def hello():
#     return 'Hello, i am func "hello"'
#
#
# def super_func(func):
#     print('Hello, i am func "super_func"')
#     print(func())
#
#
# super_func(hello)

######


# print(ord('a'))
# print(ord('#'))
# print(ord('м'))

# while True:
#     n = input("->")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# s = "hello, WORLD! I am learning Python.H"

# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.print(s.lower().count("h"))

# print(s.count("h", 1, -5))  # подсчет вхождений подстроки в строку
# print(s.find("h"))  # возвращает первый индекс, который соответствует началу подстроки
# или значение -1, если элемента нет
# print(s.rfind("h"))  # возвращает последний индекс

# print(s.index("h"))  # возвращает первый индекс, который соответствует началу подстроки
# или значение ValueError, если элемента нет
# print(s.rindex("h"))  # возвращает последний индекс

# s = "один два"
# one_word = s[:s.find(' ')]
# two_word = s[s.rfind(' ') + 1:]
# print(two_word + ' ' + one_word)

# s = 'ab12c59p7dq'
# print(s)
# digits = []
# for symbol in s:
#     if '1234567890'.find(symbol) != -1:
#         digits.append(int(symbol))
#
# print(digits)

# st = 'The original words and form of a written or printed work'
# ch = "z"
# if st.count(ch) == 1:
#     print(st.find(ch))
# elif st.count(ch) >= 2:
#     print(st.find(ch), st.rfind(ch))
# s = "hello, WORLD! I am learning Python."
#
# print(s.endswith('lo', 0, 5))  # строка заканчивается заданным символом
# print(s.startswith('I am', 14))  # строка начинается заданным символом


# print('abc#123'.isalnum())  # определяет состоит ли строка из букв и цифр
#
# print('abcABC'.isalpha())  # определяет состоит ли строка из букв
# print('4567123'.isdigit())  # определяет состоит ли строка из цифр
#
# print('abc1;№%%'.islower())  # определяет состоит ли строка из символов букв в нижнем регистре (могут
# # присутствовать любые символы)
#
# print('ADF456'.isupper()) # определяет состоит ли строка из символов букв в верхнем регистре (могут
# # присутствовать любые символы)

# print("py".center(10))  # выравнивает строку по центру относительно заданного количества символов
# print("py".center(10, '-'))
# print("py".center(1))

# print('       py'.lstrip())  # удаляет пробельные символы с левой стороны
# print('py       '.rstrip())  # удаляет пробельные символы с правой стороны
# print('      py       '.strip())  # удаляет пробельные символы с правой и левой стороны

# print('https://www.python.org'.lstrip("/:pthsworg"))
# print('https://www.python.org'.rstrip("/:pthsworg"))
# print('https://www.python.org'.strip("/:pthsworg"))
#
# print('https://www.python.org'.lstrip("/:pths").rstrip('org.'))

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace('Nython', 'Python', 2))

# s = "Заменить в этой строке все появления буквы 'о' на 'О' кроме первого и последнего вхождения"
# a = s[:s.find('о') + 1]
# b = s[s.find('о') + 1:s.rfind('о')]
# c = s[s.rfind('о'):]
# s = a + b.replace('о', 'О') + c
# print(s)

# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(['1', '2']))
# print("...".join(['1', '2']))
# print(":".join("Hello"))
#
# print("H:e:l:l:o".split(":"))
# print("Строка разделенная пробелами".split())
#
# print("www.python.org.ru".split(".",2))
# print("www.python.org.ru".rsplit(".",2))

# a =  input("->").split()
# print(a)

# a = input("Введите ФИО: ")
# a = a.split()
# print(a)
# print(f"{a[0].capitalize()} {a[1][0].upper()}.{a[2][0].upper()}.")

# import re

# s = "Я ищу совпадения в 2023 году. И я их найду в два счёта."
# reg = "в"
# print(re.findall(reg, s))  # возвращает список содержащий все совпадения с шаблоном
# print(re.search(reg, s))  # возвращает месторасположения первого совпадения объекта
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# print(re.match(reg, s)) # возвращает месторасположения совпадения объекта в начале строки

# print(re.split(reg, s, 2)) # возвращает список в котором строка разбита по шаблону
# print(re.sub(reg, "В", s, 3)) # поиск и замена

# s = "Я ищу совпадения в 2023 году. И я их найду в два счёта. [-1863]"
# reg = "[12][0-9][0-9][0-9]"
# reg = r"\."
# reg = r"[0-9\[\]\-.]"
# reg = r"[^0-9]"
# print(re.findall(reg, s))
# print(ord("Я"))
# print(ord("я"))
# print(ord("а"))
# print(ord("ё"))

# s = "Час в 24-часовом формате от 00 до 23. 2021-06-15T20:59. Минуты, в диапазоне от 00 до 59. 2021-0615T01:09."
# reg = r"[0-2][0-9]:[0-5][0-9]"
# print(re.findall(reg, s))

# s = "Я ищу совпадения ^ в 2023 году. И я их найду в два счё_та. [-1863]. Hello."
# reg = r"\Bния"
# print(re.findall(reg, s))

# d = "Цифры: 7, +17, -42, 0012, 0.3.3"
# print(re.findall(r"[+-]?\d+[.\d]*", d))

# s = "06-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub(r"#.*", "", s))
# print("Дата рождения:", re.sub(r"-", r".", re.sub(r"#.*", "", s)))

# s = "author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831"
# # reg = r"\w+\s*=\s*\w+[\s\w.]*"
# reg = r"\w+\s*=[^;]+"
# print(re.findall(reg, s))

# s = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, s))

# s = "Я ищу совпадения ^ в 2023 году. И я их найду в два счё_та."
# # reg = r"^\w+\s\w+"
# reg = r"\w+\.$"
# print(re.findall(reg, s))

# def validate_login(name):
#     return re.findall(r'^[A-Za-z_0-9-]{3,16}$', name)
#
#
# print(validate_login('Python_master'))
# print(validate_login('P$yt$$09'))


# text = """Python,
# python,
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))
#
# s = "Я ищу совпадения^ в 2023 году. И я их найду в 2 счёта. 186389. Hello"
# reg = r"\d{2,}"
# print(re.findall(reg, s))

# s = "<p>Изображение <img alt='картинка' src='bg.jpg' width='200'> - фон страницы<img alt='картинка'></p>"
# # res = r'<img.*?>'
# res = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(res, s))
# print(re.sub(res, "<img src='1.jpg'>", s))

# s = "Петр, Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий"
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0, double = 8.0f, int"
# # reg = r"\w+\s*=\s*\d[.\w]*|double\s*=\s*\d[.\w]*"
# reg = r"(?:int|double)\s*=\s*(?:\d[.\w]*)"
# print(re.findall(reg, s))
# print(re.search(reg, s))


# () - сохраняющие скобки
# (?:) - несохраняющие круглые скобки

# s = "Word2016, PS6, AI5"
# reg = r"([a-z]+)(?:\d*)"
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s,re.IGNORECASE))

# s = "5 + 7*2 - 4"
# reg = r"\s*[+*-]\s*"
# print(re.split(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счё_та. 186389. Hello"
# reg = r"(\d+)\s(\D+)"
# print(re.findall(reg, s))
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[1])
# print(m[2])
# print(m[0])

# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def repl_count(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print("<select name='city'>")
# print(re.sub(r'\s*(\w+)\s*', repl_count, text))
# print("</select>")


# s = "Самолет прилетает 10/23/2021. Будем рады вас видеть после 10/24/2021"
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))  # 23.10.2021

# s = "yandex.ru and yandex.com"
# reg = r'(([a-z0-9\-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r"http://\1", s))

# Рекурсия

# def elevator(n):
#     if n == 0:  # базовый случай
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)  # 3
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже? "))
# elevator(n1)

# 1
# 2
# 3

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9])) # 25

# def sum_list(lst):  # [1, 3, 5, 7, 9],[3, 5, 7, 9],[5, 7, 9],[7, 9],[9]
#     if len(lst) == 1:
#         return lst[0]  # 9
#     else:
#         return lst[0] + sum_list(lst[1:])  # 1 +, 3 +, 5 +, 7 +
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25

# def to_str(n, base):  # to_str(254,16)
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # convert[]=
#     else:
#         return to_str(n // base, base) + convert[n % base]  # 6,
#
#
# print(to_str(254, 8))

names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]

# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))
#
# print(names[1])
# print(isinstance(names[1], list))
#
# print(names[1][1])
# print(isinstance(names[1][1], list))
#
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))

# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

# def remote(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remote(text[1:])
#     else:
#         return text[0] + remote(text[1:])
#
#
# print(remote("  Hello\tWorld "))


# Файлы
# f = open(r'C:\Proga\PYTHON\text.txt')
# f = open('text.txt')
# print(f)
# print(*f)
# print(f.mode)
# print(f.encoding)
# print(f.name)
# f.close()
# print(f.closed)

# f = open('text.txt')
# print(f.read(3))
# print(f.read())
# f.close()

# f = open('test.txt')
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# f = open('test.txt')
# print(f.readlines(16))
# print(f.readlines())
# f.close()

# f = open('test.txt')
# s = 0
# for i in f:
#     print(f)
#     s += 1
# f.close()
# print(s)

# f = open('xyz.txt', "w")
# f.write('Hello\nWorld!\n')
# f.close()

# f = open('xyz.txt', "a")
# # f.write('New text!\n')
# line = ['This is line 1 ', 'This is line 2']
# f.writelines(line)
# f.close()

# f = open('xyz.txt', "w")
# lst = [str(i ** 5) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()
# pos = int(input("Выберите позицию: "))
# f = open('text2.txt', "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# f = open('text2.txt', "r")
# read_file = f.readlines()
# print(read_file)
# read_file[pos] = 'helloWord!\n'
# print(read_file)
# f.close()
#
# f = open('text2.txt', "w")
# f.writelines(read_file)
# f.close()

# f = open('text2.txt', "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# pos = int(input("Выберите позицию: "))
# f = open('text2.txt', "r")
# read_file = f.readlines()
# print(read_file)
# # if pos >= len(read_file):
# #     print("Такого индекса не существует!")
# # else:
# #     read_file[pos-1] = 'helloWord!!!\n'
# if 0 < pos <= len(read_file):
#     del read_file[pos - 1]
# else:
#     print("Такого индекса не существует!")
# print(read_file)
# f.close()
#
# f = open('text2.txt', "w")
# f.writelines(read_file)
# f.close()


# f = open('text.txt', 'r')
# print(f.read(3))  # Hel
# print(f.tell())  # 3 - возвращает позицию условного курсора в файле
# print(f.seek(1))  # 1 - перемещает условный курсор в заданную позицию
# print(f.read())  # ello!
# print(f.tell())  # 6
# f.close()

# f = open('text.txt', 'r+')
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()

# with open('text.txt', 'w+') as f:
#     print(f.write('012345\n6789'))
#
# with open('text.txt', 'r+') as f:
#     for line in f:
#         print(line[:3])

# file_name = "res.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     print(lt)
#     return " ".join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# print('Done!')

# with open('res.txt', 'r+') as f:
#     x = f.read().split(" ")
#     print(x)
#     print(len(x))
#     print(sum(map(float, x)))

# def longest_words(file):
#     with open(file, encoding='utf-8') as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         # print(w)
#         # print(res)
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_words('test.txt'))


# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open('one.txt', 'w') as f:
#     f.write(text)


# read_file = 'one.txt'
# write_file = 'two.txt'
# three = 'three.txt'
# with open(read_file, 'r') as fr, open(write_file, 'r') as fw, open(three, 'w') as ft:
#     # for line in fr:
#     #     line = line.replace("Строка", "Линия - ")
#     #     fw.write(line)
#
#     a = fr.readlines()
#     b = fw.readlines()
#     # print(a)
#     # print(b)
#     # c = a + b
#     # print(c)
#     # for line in c:
#     #     ft.write(line)
#
#     for i, j in zip(a, b):
#         c = i + j
#         ft.write(c)

from random import randint

# s = tuple(2**i for i in range(1,13))
# print(s)

# t1 = tuple('hello')
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3)
# # print(len(t3))
# # print(t3.count('l'))
# # print(t3.count('a'))
# if 'l' in t3:
#     print(t3.index('l'))
# else:
#     print("Такого символа нет")
#
# for i in t3:
#     print(i, end=" ")



# import os.path
#
#
#
#
# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print("-" * 50)
#     for root, dirs, files in os.walk("nested1"):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена")
#     print("-" * 50)
#
#
# remove_empty_dirs("nested1")
