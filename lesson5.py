# function

# def get_sum():
#     print(2 + 4)
#
# a = get_sum()
# print(a)

# def get_circle_square():
#     r = 16
#     s = 3.14 * r**2
#     return s
# square = get_circle_square()
# print(square)
#


# money = int(input("Vvedite dengi: "))
# year = int(input("Vvedite count year: "))
# PROCENT = 0.1
# count_money = money * PROCENT * year + money
# print(count_money)


#
# money = int(input("Vvedite dengi: "))
# year = int(input("Vvedite count year: "))
# def result_vklad(money: int, year: int) -> int:
#     PROCENT = 0.1
#     count_money = money * PROCENT * year + money
#     return count_money
#
# print(result_vklad(year=year, money=money))


# *args, **kwargs


# def get_kwargs_args(*args, **kwargs):
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)
#
# get_kwargs_args(1, "Arsen", age=17)


# def get_sth(*args):
#     from datetime import datetime
#     before = datetime.now()
#     numbers = [i for i in range(1, 10000)]
#     if args and len(args) == 1:
#         numbers = [ i for i in range(1, args[0])]
#     elif args and len(args) == 2:
#         numbers = [i for i in range (1, args[0], args[1])]
#     result = datetime.now() - before
#     return result, numbers
# print(get_sth(7))


# def findall(s):
#     lists = []
#     if type(s) == str:
#         for i in range(len(s)):
#             if s[i] == "a":
#                 lists.append(i)
#             return lists
#         else:
#             return "No str"
#
#
# result = findall("lalaofo")
# print(result)









def findall(s):
    index_of_a = []
    if type(s) == str:
        for i in range(len(s)):
            if s[i] == "a":
                index_of_a.append(i)
        return index_of_a
    else:
        return "No str"

result = findall("lalafo")
print(result)

