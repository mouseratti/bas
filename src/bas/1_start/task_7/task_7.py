print('Type year: ')
a = input()
year = int(a)
x1=False
x2=False
x3=False
if year%4==0 : 
	x1=True
if year%100==0 :
	x2=True 
if year%400==0 :
	x3=True

if x1 and x3:
	print('YES')
elif x1 or x3:
	if x2==False:
		print('YES')
	else:
		print('NO')
else:
	print('NO')
