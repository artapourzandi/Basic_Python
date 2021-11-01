new_list = [
    {"name": "Nima", "salary": 5000},
    {"name": "Yalda", "salary": 1000},
    {"name": "Ali", "salary": 500}
]

""" def f(list):
    return list["name"] """

new_list.sort(key=lambda list: list["name"])

print(new_list)