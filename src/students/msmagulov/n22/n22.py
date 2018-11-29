def even(l,*args)
    evens = []
    for n in l:
        if n % 2 == 0:
            evens.append(n)
    inputted = input("Insert numbers")
    splitted = inputted.split()
    result = count_even(splitted)
