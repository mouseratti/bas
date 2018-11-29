#from variables import YEARS
print("Hello, JOB12!")

g = list()
g.append(2)
i = 0
t=0
STOP = 1024

while i < 1010:
	t = g[i]*2
	g.append(t)
	print('v stepeni ',i, ' = ',g[i])
	if g[i]==STOP: break
	i += 1




