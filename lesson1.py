#key and value

#
# nazgul = {
#     "name": "Nazgul",
#     "age": 18,
#     "subjects": {
#         "python": 67,
#         "math": 80,
#     },
#     "schools": {
#         "68": 2001,
#         "13": 2005,
#     },
# }
#
#
# for i in nazgul:
#     if type(nazgul[i]) == dict:
#         for j in nazgul[i]:
#             print(nazgul[i][j])


# python = {
#     "aliza": 78,
#     "zamira": 77,
#     "smanaly": 90,
#     "nurlan": 89,
#     "aman": 66,
# }
# python["ilgiz"] = 100
# print(python.keys())
# print(python.values())
# print(python.items())
# for i, j in python.items():
#     print(i, j)
#
# python = {
#     "aliza": 78,
#     "zamira": 77,
#     "smanaly": 90,
#     "nurlan": 89,
#     "aman": 66,
# }
# print(sum(python.values()) / len(python))

# counter = 0
# for values in python.values():
#     counter += values
# print(counter / len(python))


# python = {
#     "aliza": 78,
#     "zamira": 77,
#     "smanaly": 90,
#     "nurlan": 89,
#     "aman": 66,
# }
# languages = ["python", "java", "go"]
# dict_languages = dict.fromkeys(languages, 9)
# print(dict_languages)

# python = {
#     "aliza": 78,
#     "zamira": 77,
#     "smanaly": 90,
#     "nurlan": 89,
#     "aman": 66,
# }
# python.clear()
# print(python)
#  setdefault
# pop
# popitem
# update

# while True:
#     tovar = {
#
#     }
#     prod = input()
#     tovar = eval(prod)
#     print(tovar)

# while True:
#     product = input("Vvedite prod and price: ")
#     dict_products = {}
#     key, value = product.split()
#     dict_products[key] = int(value)
#     print(dict_products)
#
#     if product == exit:
#         break

# def get_extension(filename):
#     filenames = filename.split(".")
#     if filenames == "png":
#         return f' Расширение файла -{"png"}'
#     elif filenames == "jpeg":
#         return f' Расширение файла -{jpeg}'
#     elif filenames == "html":
#         return f' Расширение файла -{html}'
#     elif filenames == "doc":
#         return f' Расширение файла -{doc}'
#     elif filenames == "xlsx":
#         return f' Расширение файла -{xlsx}'
#     # else:
#     #     return f'None'
# result = get_extension("asdad.png")
# print(result)
