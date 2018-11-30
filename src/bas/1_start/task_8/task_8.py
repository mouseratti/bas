print('Input n: ')
str_n = input()
int_n = int(str_n)
int_s = 0
for x in range(int_n+1):
	int_s = int_s + (x * x * x)
print(int_s)
