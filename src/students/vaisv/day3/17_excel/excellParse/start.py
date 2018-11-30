from mods import getMonths,getUsers,getDays
import xlrd

book = xlrd.open_workbook('tabel.xls')
listNames = book.sheet_names()

def osn(sheetInt):
	l1 = list()

	sheet=book.sheet_by_name(sheetInt)

	for rownum in range(sheet.nrows):
		row = sheet.row_values(rownum)
		l1.append(row)

	#polu4aem mesyac
	month=getMonths(*l1)
	print(month)

	# polu4aem polzovateleyi
	users=getUsers(*l1)
	#print(users)

	l1.append(users)

	getDays(month,*l1)




for ii in listNames:
	#kazdii list
	osn(ii)

