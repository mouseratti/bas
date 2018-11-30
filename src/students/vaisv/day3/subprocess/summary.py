import subprocess,re

result = subprocess.run('ping ww.kz -c 5'.split(), stdout=subprocess.PIPE, timeout=5)

#result = subprocess.Popen('ping ww.kz -c 22'.split(), stdout=subprocess.PIPE)

a=result.stdout
#print(result.stdout)
y=re.findall('.*(\d{1,9}\%).*\=\s.{1,5}\/(\d+\.\d{1,3})',str(a))

print(result.stdout.decode())

print('Packet loss = ',y[0][0],', responce average time = ',y[0][1],' ms')