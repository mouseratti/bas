def count_numbers(l=[]):
    num_list = l
    n = 0
    m = 0
    odd_num = []
    even_num = []
    for x in num_list:
        if x % 2 == 0:
            even_num.append(x)
            n += 1
        else:
            odd_num.append(x)
            m += 1
    print("Even numbers:",n)
    print("Odd numbers:",m)
    # num = int(input("Enter a number:"))
    # if (num % 2) == 0:
    #     print("{0} is Even".format(num))
    # else:
    #     print("{0} is Odd".format(num))
    #     result(count_numbers())
