

def is_leap(year):
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
		return True
	elif x1 or x3:
		if x2==False:
			return True
		else:
			return False
	else:
		return False

