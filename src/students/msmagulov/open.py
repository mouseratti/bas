from datetime import  datetime
if __name__ == '__main__':
    now = datetime.now()
    f = open("filename","a+")
    f.write("currmet timestamp: {}\n".format(now))
    f.write("string\n")
    f.write("we need to close\n")
    f.flush()
    f.seek(0)

    for line in f.readlines():
        print(line)