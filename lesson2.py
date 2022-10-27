# set collection
# sets = set()
# print(type(sets))

# cities = {"Tokyo", "Biskek", "Paris", "Berlin"}
# towns = {"Naryn", "Manchester", "Cholponata", "Praga"}
# cities.add("Madrid")
# cities.clear()
# cities.discard("Tokyo")
# cities.remove("Tokyo")
# print(cities)

# union, update
# cities = {"Tokyo", "Biskek", "Paris", "Berlin"}
# towns = {"Naryn", "Manchester", "Cholponata", "Praga"}
# city_town = cities.union(towns)
# cities.update(towns)
# print(city_town)
# print(cities)


# cities = {"Tokyo", "Biskek", "Paris", "Berlin"}
# towns = {"Naryn", "Tokyo", "Manchester", "Cholponata", "Praga"}
# cities.intersection(towns))
# cities.intersection_update(towns)
# cities.symmetric_difference(towns)
# cities.symmetric_difference_update(towns)
# cities.pop()


# cities = {"Tokyo", "Biskek", "Paris", "Berlin", "Naryn", "Praga",}
# towns = {"Naryna", "Praga"}
# print(cities.issubset(towns))
# print(cities.issuperset(towns))
# print(cities.isdisjoint(towns))
#
# student = {
#     "name": "Nazgul",
#     "age": "18",
#     "year": None,
#     "subjects": {
#         "math": (80, 23, 41, 91),
#         "python": (91, 88, 87, 95),
#         "chemist": (13, 73, 66, 40),
#         "html": (41, 35, 74, 92),
#     },
#     "total": None
# }
#
# # year
# student["year"] = 2022 - student["age"]
#
# # find averagw of each subjects
# for key, value in student["subjects"].items():
#     student["subjects"][key] = sum(value) / len(value)
#
# # total average
# student["total"] = sum(student["subjects"].values()) / len(student["subjects"])
# print(student)
