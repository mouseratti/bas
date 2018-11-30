# https://docs.python.org/3/library/argparse.html
import argparse

choices = ['sum','max','min']

def make_parser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    parser.add_argument('--min', dest='accumulate', action='store_const',
                        const=min, default=max,
                        help='min the integers (default: find the max)')

    return parser


if __name__ == '__main__':
    parser = make_parser()
    args = parser.parse_args()
    print(args.integers)
    print(args.accumulate)
    print(args.accumulate(args.integers))