print('Input n: ')
int_n = int(input())
for x in range(1,int_n):
	s = 2 ** x
	if s >= int_n:
		break
print(x-1)
print(2 ** (x-1))
