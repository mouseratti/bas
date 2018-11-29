def even(*args):
    result =set()
    for oo in args:
    	if type(oo) == int:
    		if not oo % 2:
    			result.add(oo)
    return tuple(result)
