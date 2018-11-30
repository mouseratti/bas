
def is_programmer(position):
    department = ["РПО", "ВСПП", "ЭТС"]
    for element in department:
        if position.endswith(element):
            return True
    return False

def get_worker_position(row): return row[2]

def filter_rows_by_is_programmer(rows):
    return [row for row in rows if is_programmer(get_worker_position(row))]