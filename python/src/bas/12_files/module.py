from datetime import datetime
if __name__ == '__main__':
    now = datetime.now()
    f = open("filename", "a+")
    f.write("current timestamp: {}\n".format(now))
    f.write("string\n")
    f.write("next string\n")
    f.write("we need to close\n")
    # f.flush()
    f.seek(0)
    result = f.read(10)
    # print(result)
    f.close()
    if bool(f.readline()) is False:

    for line in f.readlines():
        print(line)
