# https://habr.com/post/99923/
# https://habr.com/post/232291/
import xlrd
xlsfile = xlrd.open_workbook('tabel.xls', formatting_info=True)
sheet =  xlsfile.sheet_by_name('август')
for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)
for c_el in row:
    print c_el