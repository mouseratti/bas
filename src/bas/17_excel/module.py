# https://habr.com/post/99923/
# https://habr.com/post/232291/
import xlrd
from datetime import datetime


xlsfile = xlrd.open_workbook('tabel.xls', formatting_info=True)
sheet =  xlsfile.sheet_by_name('август')
colums = [sheet.col_values in range (sheet.ncols)]
rows = [sheet.row_values(x) for x in range (sheet.nows)]
result = get_workers_on_day()
    for rownum in range(sheet.nrows): #nrows = количество строк
        row = sheet.row_values(rownum)
    for c_el in range(1, sheet.nrows):
        for rownum in range(sheet.ncols):


