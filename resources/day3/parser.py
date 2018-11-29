from collections import Counter
import re
def f_len():
    f = open("log", "r")
    f_len = sum(1 for line in f)
    f.close()
    return f_len

TOTAL_COUNT = f_len()

print("Total lines:", TOTAL_COUNT)

def f_get():
    f = open("log", "r")
    gcount = sum(1 for match in re.finditer('\"(GET)\s{1,}(\/.+) (HTTP\/1\.1)\"',f.read()))
    return gcount
print("method GET:",f_get())

def f_put():
    f = open("log", "r")
    pcount = sum(1 for match in re.finditer('\"(PUT)\s{1,}(\/.+) (HTTP\/1\.1)\"',f.read()))
    return pcount
print("method PUT:",f_put())

def f_post():
    f = open("log", "r")
    pscount = sum(1 for match in re.finditer('\"(POST)\s{1,}(\/.+) (HTTP\/1\.1)\"',f.read()))
    return pscount
print("method POST",f_post())

def f_delete():
    f = open("log", "r")
    dcount = sum(1 for match in re.finditer('\"(DELETE)\s{1,}(\/.+) (HTTP\/1\.1)\"',f.read()))
    return dcount
print("method DELETE:",f_delete())

def f_sort():
    result = {}
    regex = '\"(GET|PUT|POST|DELETE)\s{1,}(\/.+) (HTTP\/1\.1)\"'
    f = open("log", "r")
    for match in re.finditer(regex, f.read()):
        method, url = match.group(1), match.group(2)
        if method in result:
            result[method][url] +=1
        else:
            result[method] = Counter()
            result[method][url] += 1
    f.close()
    return result

result = f_sort()
common_counter = Counter()
for key in result:
    common_counter.update(result[key])
print("the most popular:")
for pos in common_counter.most_common(20):
    print(pos)
for key in result:
    print("unique values of {}: {}".format(key, len(result[key].keys())))
common_counter_total_count = sum(common_counter[x] for x in common_counter)
print(common_counter_total_count)
assert  TOTAL_COUNT == common_counter_total_count

# for pos in result['PUT']:
#     print(pos)