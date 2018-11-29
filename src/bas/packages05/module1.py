#!/usr/bin/env python
VARIABLE = '1'
def f1(): return 1


result = f1()
a = f1
result2 = a()
required = 0

def function(required, optional=0, *args, **kwargs):
    global required
    required = 5
    pass
   # return == return None
function(5)

a = lambda x: x ** x
a(2)
a(4)

if __name__ == '__main__':
    print(__name__)
