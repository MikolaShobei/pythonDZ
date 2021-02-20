# 1)Дан лист:
#   - найти min число в листе

# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

# print(min(list1))

# min_value = list1[0]
# for i in list1:
#     if min_value > i:
#         min_value = i
# print(min_value)


#   - удалить все одинаковые значения

# list2 = list1.copy()
# for i in list2:
#     if list1.count(i) > 1:
#         while list1.count(i) > 0:
#             list1.remove(i)
# print(list1)

#   - заменить каждое четвертое значение на "Х"
# a = -3
# for i, val in enumerate(list1):
#     if i == a + 3:
#         a += 4
#         list1.pop(i)
#         list1.insert(i, "x")
# print(list1)


#   - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа

# avg = sum(list1) / len(list1)
# l2 = []
# for e, i in enumerate(list1):
#     diff = i - avg
#     if diff < 0:
#         diff *= (-1)
#     l2.append(diff)
# print(list1[l2.index(min(l2))])



# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:

# width = 20
# height = 15
# for i in range(1, height + 1):
#     if i == 1 or i == height:
#         print("*" * width)
#     else:
#         print("*" + " " * (width - 2) + "*")


# 3) переделать первое задание под меню с помощью цикла

# print("Дан лист:")
# print("list = [22, 3,5,2,8,2,-23, 8,23,5]")
# print("1 - найти min число в листе")
# print("2 - удалить все одинаковые значения")
# print("3 - заменить каждое четвертое значение на 'X'")
# print("4 - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа")
# print("exit - щоб вийти")
# while True:
#     list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#     inp = input("Enter command: ")
#     if inp == "1":
#         print(min(list1))
#
#     elif inp == "2":
#         list2 = list1.copy()
#         for i in list2:
#             if list1.count(i) > 1:
#                 while list1.count(i) > 0:
#                     list1.remove(i)
#         print(list1)
#
#     elif inp == "3":
#         a = -3
#         for i, val in enumerate(list1):
#             if i == a + 3:
#                 a += 4
#                 list1.pop(i)
#                 list1.insert(i, "x")
#         print(list1)
#
#     elif inp == "4":
#         avg = sum(list1) / len(list1)
#         l2 = []
#         for e, i in enumerate(list1):
#             diff = i - avg
#             if diff < 0:
#                 diff *= (-1)
#             l2.append(diff)
#         print(list1[l2.index(min(l2))])
#
#     elif inp == "exit":
#         break
#
#     else:
#         print("Wrong value")


# 4) вывести табличку умножения с помощью цикла while

# i = 1
# j = 1
# while i <= 9:
#     while j <= 9:
#         if i * j < 10:
#             print(i * j, end="  ")
#         else:
#             print(i * j, end=" ")
#         j += 1
#     print("")
#     j = 1
#     i += 1
#

