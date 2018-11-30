from collections import Counter
import re

FILENAME = "log"

PUT = re.compile('((PUT)\s(/.*)\?.*)|((PUT)\s(.*)\sHTTP/1.1)')
GET = re.compile('((GET)\s(/.*)\?.*)|((GET)\s(.*)\sHTTP/1.1)')
DEL = re.compile('((DELETE)\s(/.*)\?.*)|((DELETE)\s(.*)\sHTTP/1.1)')

methods = {PUT: 0, GET: 0, DEL: 0}

f = open(FILENAME)
count_PUT = Counter()
count_GET = Counter()
count_DEL = Counter()

int_PUT = 0
int_GET = 0
int_DEL = 0


if __name__ == "__main__":
    list_ls = f.readlines()
    f.close()
    print("Lines count: {}".format(len(list_ls)))
    for x in list_ls:
        for regex_binary in (PUT, GET, DEL):
            result = regex_binary.findall(x)
            if result:
                methods[regex_binary] += 1
                if regex_binary is PUT:
                    res = re.search(PUT, x)
                    if res.group(6):
                        count_PUT[res.group(6)] += 1
                    else:
                        count_PUT[res.group(3)] += 1

                if regex_binary is GET:
                    res = re.search(GET, x)
                    if res.group(6):
                        count_GET[res.group(6)] += 1
                    else:
                        count_GET[res.group(3)] += 1

                if regex_binary is DEL:
                    res = re.search(DEL, x)
                    if res.group(6):
                        count_DEL[res.group(6)] += 1
                    else:
                        count_DEL[res.group(3)] += 1

    print("PUT: {}".format(methods[PUT]))
    print("GET: {}".format(methods[GET]))
    print("DELETE: {}".format(methods[DEL]))
    print("Unique PUT: {}".format(len(count_PUT)))
    print("Unique GET: {}".format(len(count_GET)))
    print("Unique DELETE: {}".format(len(count_DEL)))
    print("Most common PUT URL: ")
    for x in count_PUT.most_common()[:20]:
        print(x)
    print("Most common GET URL: ")
    for x in count_GET.most_common()[:20]:
        print(x)
    print("Most common DELETE URL: ")
    for x in count_DEL.most_common()[:20]:
        print(x)
