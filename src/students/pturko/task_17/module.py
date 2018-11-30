#import argparse
from collections import Counter
import sys

n = 0
#def make_parser():
#    pars = argparse.ArgumentParser()
#    pars.add_argument('filename', metavar='N', type=str)
#    pars.add_argument('most_popular', metavar='M', type=int)
#    return pars


def read_file(filename):
    f = open(filename, "r")
    result = f.read()
    f.close()
    return Counter(result.split())


if __name__ == '__main__':
    args = sys.argv
    count_txt = read_file(args[1])
    print(count_txt.most_common()[:int(args[2])])
#    parser = make_parser()
#    arg = parser.parse_args()
#    str_name = str(arg.filename)
#    count_txt = read_file(arg.filename)
#    print(count_txt.most_common()[:arg.most_popular])

