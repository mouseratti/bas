def even(*args):
    result = set()
    for pos in args:
        if isinstance(pos,int):
            if not pos % 2:
                result.add(pos)
    return tuple(result)