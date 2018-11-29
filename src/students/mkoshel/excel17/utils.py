
def get_worker_name(row:list):
    return row[1]

def is_worked(row, index):
    try:
        int(row[index])
        return True
    except:
        return False

def get_row_index_by_day(day_number:int, columns: list) -> int:
    for index, column in enumerate(columns):
        try:
            if int(column[3]) == day_number: return index
        except:
            pass
    raise Exception("index for day {} not found!!!".format(day_number))



def get_workers_on_day(day_number, columns, rows):
    index = get_row_index_by_day(day_number, columns)
    return [get_worker_name(row) for row in rows if is_worked(row, index)]
