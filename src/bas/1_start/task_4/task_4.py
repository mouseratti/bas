n = int(input('Input n: '))
hh = n // 60
mm = n % 60

if hh > 24:
	dd = hh // 24
	hh = hh % 24
	print('{:02d} days {:02d}:{:02d}'.format(dd, hh, mm))
else:
	print('{:02d}:{:02d}'.format(hh, mm))

