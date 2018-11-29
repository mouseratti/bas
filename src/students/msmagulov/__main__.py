from students.msmagulov.n10 import count_numbers
if __name__ == '__main__':
    x = input("insert numbers")
    integers = []
    for elem in x.split():
        try:
            integers.append(int(elem))
        except:
            print(elem + " is not a number!!!")
    count_numbers(integers)