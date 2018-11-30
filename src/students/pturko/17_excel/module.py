# https://habr.com/post/99923/
# https://habr.com/post/232291/
import xlrd
import random
d = 2
list_name = list()
dol = ['Вед. спец.отдела ЭТС', 'Гл. спец.отдела ЭТС', 'Гл. спец.отдела РПО', 'Вед. спец.отдела РПО', 'Гл. спец. ВСПП', 'Вед. спец. ВСПП']
xlsfile = xlrd.open_workbook('tabel.xls', formatting_info=True)
sheet = xlsfile.sheet_by_name('август')

for day in range(3, 34):
    for x in range(4, sheet.nrows):
        if dol.count(sheet.cell(x, 2).value) > 0:
        # if (str(sheet.cell(x, 2).value) == 'Вед. спец.отдела ЭТС') or (str(sheet.cell(x, 2).value) == 'Гл. спец.отдела ЭТС') or (str(sheet.cell(x, 2).value) == 'Гл. спец.отдела РПО') or (str(sheet.cell(x, 2).value) == 'Вед. спец.отдела РПО') or (str(sheet.cell(x, 2).value) == 'Гл. спец. ВСПП') or (str(sheet.cell(x, 2).value) == 'Вед. спец. ВСПП'):
            if sheet.cell(x, day).value == 8:
                # print('{} {} {}'.format(sheet.cell(x, 1).value, sheet.cell(3, day).value, sheet.cell(x, day).value))
                list_name.append(sheet.cell(x, 1).value)

#    print("day{} {}".format(day-2, list_name))
    if list_name:
        print('DAY {}: {}'.format(day-2, random.choice(list_name)))
    else:
        print('DAY {}: В'.format(day - 2))
    list_name.clear()

# print(list_name)
