
tuple_a = [1,2,3]


for x in tuple_a:
    print(x)
    # break
else:
    print("end of for loop")





while tuple_a:
    _ = tuple_a.pop(0)
    print(_)
    # if not tuple_a: break
else:
    print("end of while loop!")