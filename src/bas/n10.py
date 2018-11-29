import math

number = int (input ('Enter number:'))

if not number % 2 == 0 and number != 0:
	print('Odd number')
elif number == 0:
	print('Zero number')
else:
	print('Even number')