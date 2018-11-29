# https://habr.com/post/99923/
# https://habr.com/post/232291/
import xlrd,re
xlsfile = xlrd.open_workbook('tabel.xls', formatting_info=True)

sheets = xlsfile.nsheets
monthPattern = re.compile(".*Месяц:\s+([А-Я]+|[а-я]+)")
rpoPattern =re.compile(".*РПО")

def nameDay(month,*nameANDdateRow):
    print('1111')
    for asd in nameANDdateRow[2]:
        print(asd)

    for asd in nameANDdateRow[1]:
        print(asd)

    #print(nameANDdateRow)
    return

def getName(*rows):
    monthlist=''
    names=list()
    nameANDdateRow=list()

    # dni nedeli
    dateRow = rows[3]
    #print(dateRow)

    for rowI in rows:
        month = re.search(monthPattern, str(rowI))

        #vybiraem rpo
        if re.search(rpoPattern, str(rowI)):
            names.append(rowI[1])

        if month:
            monthlist=month.group(1)

    nameANDdateRow.append(rows)
    nameANDdateRow.append(dateRow)
    nameANDdateRow.append(names)

    nameDay(monthlist,*nameANDdateRow)

def getMonth(index):
    #print('index=', index)
    sheet = xlsfile.sheet_by_index(index)
    row=list()
    names=list()

    #poluzh vse stroki
    for rownum in range(sheet.nrows):
        row.append(sheet.row_values(rownum))

    getName(*row)

    #print(dateRow)

for sheetNum in range(0,sheets):
    getMonth(sheetNum)



#sheet =  xlsfile.sheet_by_name('август')
#for rownum in range(sheet.nrows):
#    row = sheet.row_values(rownum)
#for c_el in row:
#    print c_el