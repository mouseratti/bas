import subprocess
import re

def subproc():
    f = open("stdout.log", "w+")
    result = subprocess.run("ping ya.kz -c 2".split(), stdout=subprocess.PIPE)
    bytestr = result.stdout
    f.write(bytestr.decode())
    f.seek(0)
    return f.read()
result = subproc()
print(result)

def subproc_regex():
     FILENAME = "stdout.log"
     result = re.findall("(\d%)\s([a-z]+)\s([a-z]+).\s([a-z]+)\s(\d{4}\w{2})",f_read(FILENAME))
     return [''.join(x for x in y) for y in result]

def f_read(filename):
    f = open(filename, "r")
    result = f.read()
    f.close()
    return result

print(subproc_regex())


# def stat():
#     f = open("stdout.log", "r")
#     pscount = (
