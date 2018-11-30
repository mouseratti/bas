import subprocess
import re
a = re.compile('(\,.+)(.+)(\%)')
b = re.compile('(=\s\d*.\d*/)(\d*.\d*)(/\d*)')
if __name__ == "__main__":
    res = subprocess.run('ping ya.ru -c 3'.split(), stdout=subprocess.PIPE)
    txt = str(res.stdout.decode())
    print(txt)
    p = re.search(a, txt)
    trr = re.search(b, txt)

    print("Packet loss = {}%, response average time = {} ms".format(p.group(2), trr.group(2)))
    pass
