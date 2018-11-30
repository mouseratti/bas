import re, datetime
monthPattern = re.compile('.*Месяц:\s+([А-Я]+|[а-я]+)')
usersPattern = re.compile('.*(РПО|ЭТС|ВСПП)')
year = datetime.datetime.now()

def getMonths(*l1):

	for c_e in l1[1]:
		monnth = re.search(monthPattern,str(c_e))
		if monnth:
			return monnth.group(1)


def getUsers(*l1):
	users = list()

	for c_e in range(len(l1)):
		if re.search(usersPattern, l1[c_e][2]):
			users.append(l1[c_e][1])

	return users


def getDays(month, *mass):
	days = (mass[3])
	# print(days)

	users = mass[-1::]

	#print(users)

	for c_e in range(len(mass[0])):
		print(mass[c_e])
		for c_ee in range(len(users[0])):
			if users[0][c_ee] == mass[c_e][1]:
				for c_eee in range(len(days)):
					if days[c_eee]:
						# если есть 8
						if mass[c_e][c_eee] == 8.0:
							asd=1
							#print(' Работник = ', mass[c_e][1], '; Дата = ', int(days[c_eee]), '.', month, '.',
							#	  year.year, '; Часов отработанно =', int(mass[c_e][c_eee]))


