# https://docs.python.org/3/library/argparse.html
import argparse

FILENAME = "17.txt"
ch1 = ['/tmp/fn1', '/tmp/fn2']
choises_for_most = (10,20,5)
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='filename')
    parser.add_argument("fn", metavar="FILENAME", type=str, help='--help for help' ,choices=ch1)
    parser.add_argument('-m', '--most_popular', dest='most', type=int, action='store', default=20, choices=choises_for_most)

    args = parser.parse_args()
    print(args.fn, args.most, "some another string", sep=',')

    # print(args.most)

