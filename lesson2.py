# 1 написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому
# st = input("text:  ")
# en = ""
# for i in st:
#     if i.isdecimal():
#         en +=i
#
# pr = ",".join(en)
# print(pr)

# 2 написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# st2 = input("text:  ")
# en2 = []
# s = ''
# check = False
# for e, i in enumerate(st2):
#     if i.isdecimal():
#         if not check:
#             en2.append(s)
#             s = ""
#         check = True
#         if check:
#             s += i
#         if e == len(st2) - 1:
#             en2.append(s)
#         continue
#     check = False
# pr2 = ", ".join(en2[1:])
# print(pr2)

# 3 есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр

# greeting = 'Hello, world'
# arr = [i.upper() for i in greeting]
# print(arr)

# 4  с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат

# arr2 = [pow(i, 2) for i in range(50) if i % 2]
# print(arr2)

# function


# 1- створити функцію яка виводить ліст

# def l_func():
#     return list(range(21))

#
# print(l_func())


# 2- створити функцію яка приймає три числа та виводить та повертає найменьше.

# def latest_func(a, b, c):
#     m = min(a, b, c)
#     print(m)
#     return m
#
#
# latest_func(2, 45, 6)


# 3- створити функцію яка приймає три числа та виводить та повертає найбільше.

# def greatest_func(a, b, c):
#     m = max(a, b, c)
#     print(m)
#     return m
#
#
# greatest_func(2, 45, 6)


# 4- створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def combo_func(*val):
#     print(min(val))
#     return max(val)
#
#
# print(combo_func(2, 45, 6))


# 5-- створити функцію яка повертає найменьше число з ліста

# def latest_list_func(l: list):
#     return min(l)
#
#
# print(latest_list_func([1, 5, 4, 36]))


# 6- створити функцію яка повертає найбільше число з ліста

# def greatest_list_func(l: list):
#     return max(l)
#
#
# print(greatest_list_func([1, 5, 4, 36]))


# 7- створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# def sum_list_func(l: list):
#     return sum(l)
#
#
# print(sum_list_func([1, 5, 4, 36]))


# 8- створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# def avg_list_func(l: list):
#     return sum(l) / len(l)
#
#
# print(avg_list_func([2, 4, 77, 5, 445, 7]))

#                                         Decorator

#
# def decor(func):
#     def wrap():
#         return func().replace("_", " ")
#
#     return wrap
#
#
# @decor
# def pr():
#     # print('Hello_boss_!!!')
#     return 'Hello_boss_!!!'
#
#
# print(pr())
