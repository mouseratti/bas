# https://habr.com/post/99923/
# https://habr.com/post/232291/
import xlrd
from students.mkoshel.excel17.utils import get_workers_on_day

if __name__ == '__main__':
    xlsfile = xlrd.open_workbook('tabel.xls', formatting_info=True)
    sheet =  xlsfile.sheet_by_name('август')
    columns = [sheet.col_values(x) for x in range(sheet.ncols)]
    rows = [sheet.row_values(x) for x in range(sheet.nrows)]
    result = get_workers_on_day(1, columns, rows)
    print(result)

