import os
import subprocess
#import subprocess #аргумент в виде списка

#result = os.system ("sleep 5")
#print(result)
#
# def ya():
#     f = open("stdout.log","w+")
#     result = subprocess.run('ping ya.kz -c2'.split(), stdout=f)
#     f.seek(0)
#     return f.read()

def ya():
    f = open("stdout.log","w+")
    result = subprocess.run('ping ya.kz -c2'.split(), stdout=subprocess.PIPE)
    bytestr = result.stdout
    f.write(bytestr.decode())
    f.seek(0)
    return f.read()

result = ya()

print(result)