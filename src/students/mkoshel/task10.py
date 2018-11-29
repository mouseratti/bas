"""
Дано N чисел: 
Подсчитайте количество НЕЧЕТНЫХ среди введенных чисел и выведите это количество.
"""
inputted = input("Введите несколько чисел: ")
numbers = []
for elem in inputted.split():
    try:
        num = int(elem)
        if num % 2:
            numbers.append(num)
    except:
        print("{} is not an integer".format(elem))
print("{} НЕЧЕТНЫХ чисел: {}".format(len(numbers), numbers))
