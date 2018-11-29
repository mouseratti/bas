from variables import YEARS
print("Hello, JOB7!")

TEXT = """
YEAR1 = {}. YEAR2 = {}. YEAR3 = {}. YEAR4 = {}      
"""

def yearCheck(god):
	print(god)
	if god%4 == 0 and god%100 == 0 and god%400 == 0:
		print('YES',god)
	else:
		print('NO',god)

for year in YEARS:
	yearCheck(year)

