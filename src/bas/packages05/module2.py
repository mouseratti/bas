from bas.packages05.module1 import f1
import module1

module1.f1()
module1.VARIABLE == '1'


def f2(): return f1()

if __name__ == '__main__':
    print(__name__)