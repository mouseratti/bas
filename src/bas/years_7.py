def is_leap(year):
	if not year % 4 and year % 100: return True
	if not year % 400: return True
	return False