def triangle_number_func(val):
    words = open("p042_words.txt")
    pim = words.read()
    words.close()
    pim_arr = pim[1:-1].split('","')

    def letter_to_number(letter):
        if letter == "A":
            return 1
        elif letter == "B":
            return 2
        elif letter == "C":
            return 3
        elif letter == "D":
            return 4
        elif letter == "E":
            return 5
        elif letter == "F":
            return 6
        elif letter == "G":
            return 7
        elif letter == "H":
            return 8
        elif letter == "I":
            return 9
        elif letter == "J":
            return 10
        elif letter == "K":
            return 11
        elif letter == "L":
            return 12
        elif letter == "M":
            return 13
        elif letter == "N":
            return 14
        elif letter == "O":
            return 15
        elif letter == "P":
            return 16
        elif letter == "Q":
            return 17
        elif letter == "R":
            return 18
        elif letter == "S":
            return 19
        elif letter == "T":
            return 20
        elif letter == "U":
            return 21
        elif letter == "V":
            return 22
        elif letter == "W":
            return 23
        elif letter == "X":
            return 24
        elif letter == "Y":
            return 25
        elif letter == "Z":
            return 26

    def triangle_number(value):
        n = 1
        while True:
            tn = (n * (n + 1)) / 2
            if value == tn:
                return True
            if value < tn:
                return False
            n += 1

    answers = []
    for i in pim_arr:
        my_sum_arr = []
        for v in i:
            my_sum_arr.append(letter_to_number(v))
        my_sum = sum(my_sum_arr)
        answers.append(triangle_number(my_sum))
    if val:
        return answers.count(True)
    else:
        return answers.count(False)


# print(triangle_number_func(2))


def pan_digital_number():
    def check_pan(val):
        mass = list(val)
        set_mass = set(mass)
        if len(mass) == len(set_mass):
            return True
        else:
            return False

    pan = 1234567890
    sum_all_pan = 0
    for i in range(pan, 3876549210, 9):
        s = str(i)
        if check_pan(s) and int(s[1:4]) % 2 and int(s[2:5]) % 3 and int(s[3:6]) % 5 and int(s[4:7]) % 7 and int(
                s[5:8]) % 11 and int(s[6:9]) % 13 and int(s[7:10]) % 17:
            print(s)
            sum_all_pan += 1

    print(sum_all_pan)
    return sum_all_pan


def pentagonal_number(num, su):
    for k in range(num, su + 1):
        p_n = (k * (3 * k - 1)) / 2
        if p_n == su:
            return True
    return False


#
# print(pentagonal_number(int(2.0), int(145.0)))
#
#
# pentagonal = []
# n = 1
# find = 0
# t = True
# while t:
#     p = (n * (3 * n - 1)) / 2
#     # print(p, "p 122")
#     if not p % 1:
#         pentagonal.append(int(p))
#
#     for i in pentagonal[:-1]:
#         s = i + p
#         int(s)
#         # print(int(s), "s 128")
#         difference = p - i
#         int(difference)
#         # print(int(difference), "dif 130")
#         # if difference in pentagonal:
#         if (difference in pentagonal) and pentagonal_number(int(n), int(s)):
#             find = p
#             # print(difference)
#             print(s, "sum")
#             t = False
#             break
#
#     if n > 400:
#         print("Ну нахер!!! Там хер найдеш!")
#         break
#     print(n)
#     n += 1
# # print(pentagonal)
# print(find)


# Practic

#
# shop = {"3": 123456, "434": 3324, "fdwssd": 3242}
#
#
# while True:
#     print("1 - Зробити покупку")
#     print("2 - показати список всіх записів")
#     print("3 - загальна сума покупок")
#     print("4 - Найдорожча покупка")
#     print('5 - пошук по назві')
#     print("6 - вихід")
#     val = input("Чьо надо??   ")
#     if val == "1":
#         k = input("Що купив?   ")
#         price = input("Скільки заплатив?   ")
#         shop[k] = int(price)
#     elif val == "2":
#         print(shop)
#
#     elif val == "3":
#         sum_p = list(shop.values())
#         print(sum(sum_p))
#
#     elif val == "4":
#         maxi = list(shop.values())
#         print(max(maxi))
#
#     elif val == "5":
#         search = input("Введи назву: ")
#         if search in shop:
#             print("товар:", search)
#             print("ціна:", shop.get(search))
#         else:
#             print("Такого товару немає!!!")
#     elif val == "6":
#         print("6")
#         break
#     else:
#         print("Не вірне значення")
#
#
#


# # 1
# st = input("Text:  ")
# st1 = {"1": "qwe", "2": "zxcv"}
# s = set(st)
# print(s)
# for i in s:
#     print(i, st.count(i))
#

# 2

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# v = ["li" if i < 4 else "gt" for i in numbers]
# print(v)

# 3

# list1 = [1, 2, 3, 4, 5]
# list2 = [-1, 7, 10, -5, -2]
# sem = [(i,e) for i in list1 for e in list2 if i + e == 0]
# print(sem)








