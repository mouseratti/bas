def even(*args):
    list_e = list(args)
    for x in args:
        if x % 2:
            list_e.remove(x)
    return list_e


list_l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even(*list_l))
