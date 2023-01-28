# name_first = "Vladimir"
# print("Hello,", name_first)
# age = 20
# print(age)

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

print("Проверка репозитория")
