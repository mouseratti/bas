def func_name(x):
    return x + 1

x = func_name(1)
y = func_name
assert y(1) == x == 2
assert y is func_name

def f(req, *args, **kwargs):
    print('args has type {} and it is {}'.format(type(args), args))
    print("req is {}".format(req))
    try:
        return args[0]
    except:
        # print("args is empty!!")
        return None

def f3(**kwargs):
    print(kwargs)
    # print(kwargs["key1"])
    return kwargs.get("key1", 1)

dict_a = {"key1":3, "key2": 2}

f3([1,2,3])
# f3(key1="val1", key2='val2')
# f3(key2="val2")

#
# def summary(*args):
#     result = 0
#     for elem in args:
#         if isinstance(elem, int):
#             result += elem
#     return result
#
# print(summary())
# print(summary(1,2,3,4,5))
# print(summary(2))




def f4(*args):
    print(args)
    return len(args)

a = (1,2,3,4,5,6,8)

assert f4(a) == 1
assert f4(*a) == 7