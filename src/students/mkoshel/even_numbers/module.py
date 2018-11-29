def even(*args):
    result = set()
    for pos in args:
        try:
            if not pos % 2:
                result.add(pos)
        except: pass
    return tuple(result)
