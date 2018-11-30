import re
numbers = ('+79236765X97','89136645101','83812640423','8(904)541-02-03','+1(555)345-11-21','+8(3812)360-263','904-333-22-12','9333026455','+77715432100','+771222b3451','+77172123456','+7-735-543-21-00')

for num in numbers:
	if re.match('((7|8|9).(\d+).(\d+)-(\d+)-(\d+))|(\+77\d{9}|88\d{9}|89\d{9})|(^9\d{9})|((\d+)-(\d+)-(\d+)-(\d+))',num):
		print(num,' is YES')
	else:
		print(num,' is NOP')