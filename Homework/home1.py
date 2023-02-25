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
from random import *

# import math
#
# a = [lambda x: math.pi * x ** 2, lambda x, y: x * y, lambda a, b, h: (a + b) * h / 2]
# print("Площадь круга с радиусом 2: ", a[0](2))
# print("Площадь прямоугольника размером 10*13: ", a[1](10, 13))
# print("Площадь трапеции для a = 7, b = 5, h = 3: ", a[2](7, 5, 3))


# ВНУТРИ КРУГЛЫХ СКОБОК
s = "Дана строка сим(волов, среди которых есть одна открыв)ающаяся"
a = s[s.find('(') + 1:s.rfind(")")]
s = a
print(s)

# Замена подстроки
s1 = '11 23 44 55 23 22'
print("Строка: ", s1)
zam = input("Заменяемая подстрока: ")
new = input("Новая подстрока: ")
s1 = s1.split(zam)
s1 = new.join(s1)
print(s1)

# ежата
s = 'Ежевику для ежат\n' \
    'Принесли два ежа.\n' \
    'Ежевику еле-еле\n' \
    'Ежата возле ели съели.\n'
print(s)
print(s.count('Е') + s.count(' е'))
