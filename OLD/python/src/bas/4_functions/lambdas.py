dictionaries = [
    {"key": 5},
    {"key": 19},
    {"key": 1},
    {"key": 4},
    {"key": 7},
    {"key": 9},
]


# def return_dict_value(d):
#     return d["key"]

# dictionaries.sort(key=return_dict_value)

return_dict_value = lambda x: x["key"]


dictionaries.sort(key = return_dict_value)

print(dictionaries)