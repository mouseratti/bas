import pdb
def count_odds(*args):
    pdb.set_trace()
    l = list(args)
    for elem in args:
        pdb.set_trace()
        try:
            number = int(elem)
            if not number % 2:
                l.remove(elem)
        except:
            l.remove(elem)
    return l

if __name__ == '__main__':
    # inputted = input("Введите ряд чисел: ")
    # splitted = inputted.split()
    splitted = ['4', '&&&', '3' ,'!!!', '11']
    result = count_odds(splitted[:])
    print(result)


    # 4 &&& 3 !!! 11