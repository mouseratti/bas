# https://habr.com/post/99923/
# https://habr.com/post/232291/
import xlrd
# columns = [sheet.col_values(x) for x in range(sheet.ncols)]
# rows = [sheet.col_values(x) for x in range(sheet.nrows)]
# result = get_workers_one_day(1, columns, rows)
# print(result)

# for rownum in range(sheet.nrows):
#     print(sheet.row_values(rownum))


class Worker:
    fullname = ""
    position = ""
    start_day = None
    end_day = None

    def __init__(self, fullname, position, start_day, end_day):
        self.fullname = fullname
        self.position = position
        self.start_day = start_day
        self.end_day = end_day

    def __str__(self):
        return "Worker {} {} {} {}".format(self.fullname, self.position, self.start_day, self.end_day)

    def is_programmer(self):
        if self.position.endswith("ЭТС"): return True
        return False


if __name__ == '__main__':

    xlsfile = xlrd.open_workbook('tabel.xls', formatting_info=True)
    sheet = xlsfile.sheet_by_name('август')
    cell_B5 = sheet.cell(4,1).value #started name start
    print(cell_B5)
    cell_C5 = sheet.cell(4,2).value #started position
    print(cell_C5)
    cell_D5 = sheet.cell(4,3).value #started workday
    print(cell_D5)
    cell_AH5 = sheet.cell(4,33).value #started endday
    print(cell_AH5)


    cell_B40 = sheet.cell(41,1).value #finished name start
    print(cell_B40)
    cell_C40 = sheet.cell(41,2).value #finished position
    print(cell_C40)
    cell_D40 = sheet.cell(41,3).value #finished workday
    print(cell_D40)
    cell_AH40 = sheet.cell(41,33).value #finished endday
    print(cell_AH40)
    worker = Worker(cell_B5, cell_C5, cell_D5, cell_AH5)
    print(worker)
    workers = [worker]
    result = [w for w in workers if w.is_programmer()]
    print(result)

# cell_C4 = sh.cell(rowx=3,colx=2).value

# print(r)
# print(c)

# for c_el in row:
#     print(c_el)