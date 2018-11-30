print('Input numbers: ')
str_num = input()
list_a = list(str_num)
print(list_a)
int_c = 0
for x in list_a:
	n = int(x) % 2
	if n:
		int_c += 1
print('uneven: {}'.format(int_c))