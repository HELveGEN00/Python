# 12345
# Найти произведение его цифр
# Найти среднее арифметическое его цифр
import random

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

# spisok 3

a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
c = []
for i in range(len(a)):
    if a.count(a[i]) == 1:
        c.append(a[i])
print(a)
print(c)