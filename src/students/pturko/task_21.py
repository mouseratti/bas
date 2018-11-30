def enum(ind, *args):
    list_ls = list(args)
    dict_d = {}
    for x in range(ind, (len(args)+ind)):
        dict_d.update({str(x): list_ls[x-ind]})
    return dict_d


list_l = list(input('Input digits in row: ').split())
int_ind = int(input('First index number: '))
print(enum(int_ind, *list_l))
