import re
FILENAME = "regex.txt"
# def f_write(filename):
#     f = open(filename, "w")
#     f.write(text)
#     f.close()
#     return

def f_regex():
    result = re.findall("(\+7|8|9)(0|3|7|9)(1|0|4|3|7)(3|4|1|7|5)(\d{6,7})",f_read(FILENAME))
    return [''.join(x for x in y) for y in result]

def f_read(filename):
    f = open(filename, "r")
    result = f.read()
    f.close()
    return result


if __name__ == '__main__':

    print(f_regex())
    pass
